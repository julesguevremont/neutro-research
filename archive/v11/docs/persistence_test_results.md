# Persistence Test Results

## Does NEUTRO Learning Survive Restart?

**Test Date:** December 31, 2025
**Version:** V11.49

---

## Executive Summary

**VERIFIED:** V11.49 fixes STDP persistence. All 5 learning systems now persist to disk.

### Live Test Results (December 31, 2025)

```
BEFORE restart: updates=10, ltp=10, ltd=0
AFTER restart:  updates=10, ltp=10, ltd=0  ✅ PERSISTED!
```

| Learning Type | Persists? | Accumulates? | Survives Restart? |
|---------------|-----------|--------------|-------------------|
| **STDP Weights** | ✅ YES (V11.49) | ✅ YES | ✅ YES |
| **STDP Stats** | ✅ YES (V11.49) | ✅ YES | ✅ YES |
| **Route Weights** | ✅ YES (V11.49) | ✅ YES | ✅ YES |
| **Correction Memory** | ✅ YES | ✅ YES | ✅ YES |
| **QLoRA Buffer** | ✅ YES | ✅ YES | ✅ YES |
| **ChromaDB** | ✅ YES | ✅ YES | ✅ YES |

---

## The Problem (Pre-V11.49)

STDP learning was **ephemeral**:

```
Session 1: STDP updates: 18, LTP: 15, LTD: 3
           ↓ restart
Session 2: STDP updates: 0, LTP: 0, LTD: 0  ← All learning lost!
```

The `save_state()` method existed but didn't include STDP stats or route weights.

---

## The Fix (V11.49)

### save_state() Enhancement

```python
# V11.49: Save STDP stats and routing weights for persistence
if hasattr(self, 'routing') and self.routing:
    state['stdp_updates'] = self.routing.stdp_updates
    state['stdp_ltp_count'] = self.routing.stdp_ltp_count
    state['stdp_ltd_count'] = self.routing.stdp_ltd_count
    # Save route weights
    state['route_weights'] = {
        route: self.routing.route_weights[route].data.cpu().numpy().tolist()
        for route in self.routing.route_weights
    }
```

### load_state() Enhancement

```python
# V11.49: Restore STDP stats and routing weights
if hasattr(self, 'routing') and self.routing:
    self.routing.stdp_updates = state.get('stdp_updates', 0)
    self.routing.stdp_ltp_count = state.get('stdp_ltp_count', 0)
    self.routing.stdp_ltd_count = state.get('stdp_ltd_count', 0)

    # Restore route weights if saved
    if 'route_weights' in state:
        for route, weights in state['route_weights'].items():
            if route in self.routing.route_weights:
                self.routing.route_weights[route].data = torch.tensor(
                    weights, device=DEVICE
                )
```

---

## Persistence Files

### What Gets Saved

| File | Contents | Size |
|------|----------|------|
| `data/snn/snn_state.json` | SNN weights, STDP stats, route weights | ~63KB |
| `data/correction_memory.json` | User corrections | ~300B |
| `data/qlora_buffer.json` | Training samples | ~68KB |
| `data/qlora_smart_buffer.json` | Full training history | ~622KB |
| `data/chroma/chroma.sqlite3` | Vector memories | ~176KB |

### snn_state.json Structure (V11.49)

```json
{
  "memory_weights": [...],
  "value_weights": [...],
  "foundation_patterns": [...],
  "curiosity_gaps": [...],
  "total_processed": 1450,
  "learning_events": 0,
  "timestamp": "2025-12-31T10:33:17.851340",
  "stdp_updates": 18,
  "stdp_ltp_count": 15,
  "stdp_ltd_count": 3,
  "route_weights": {
    "brain_direct": [...],
    "identity": [...],
    "logic": [...],
    "memory": [...],
    "code": [...],
    "math": [...],
    "mouth_only": [...]
  }
}
```

---

## Accumulation Test

### STDP Growth During Session

| Time | STDP Updates | LTP | LTD |
|------|--------------|-----|-----|
| Start | 4 | 3 | 1 |
| After 5 queries | 8 | 6 | 2 |
| After correction | 13 | 10 | 3 |
| After 5 more | 18 | 15 | 3 |

**Result:** STDP accumulates correctly during runtime.

### QLoRA Buffer Growth

| Time | Buffer Size |
|------|-------------|
| Start | 531 |
| After test | 539 |

**Result:** Training samples accumulate correctly.

---

## When State is Saved

### Automatic Saves

1. **Every 10 interactions** (in `Soul.think()`)
   ```python
   if self.snn.total_processed % 10 == 0:
       self.snn.save_state()
   ```

2. **On graceful shutdown** (in `daemon_runner.py`)
   ```python
   if hasattr(soul, 'snn') and soul.snn:
       soul.snn.save_state()
   ```

### Manual Save (API)

Not currently exposed. Could be added:
```bash
curl -X POST http://127.0.0.1:5555/save_state
```

---

## Memory Recall Test

### Teaching a Fact

```
User: "Remember this: My favorite color is blue"
→ Stored in ChromaDB

User: "What is my favorite color?"
→ "Blue"
```

**Result:** Facts persist in ChromaDB and are recalled correctly.

### Correction Memory

```json
{
  "id": 1,
  "timestamp": "2025-12-30T20:48:22",
  "pattern_type": "algebra",
  "wrong": "3.67",
  "right": "4",
  "use_count": 83
}
```

**Result:** Corrections persist and are applied (83 uses).

---

## Verification Commands

### Check Persistence Files

```bash
# List persistence files
ls -la ~/my-ai-bot/neutro/data/snn/
ls -la ~/my-ai-bot/neutro/data/*.json | head -10

# Check STDP stats in state file
cat ~/my-ai-bot/neutro/data/snn/snn_state.json | jq '{
  stdp_updates,
  stdp_ltp_count,
  stdp_ltd_count,
  route_weights: .route_weights | keys
}'

# Check correction memory
cat ~/my-ai-bot/neutro/data/correction_memory.json | jq '.'

# Check QLoRA buffer size
wc -c ~/my-ai-bot/neutro/data/qlora_smart_buffer.json
```

### Check Runtime Stats

```bash
curl -s http://127.0.0.1:5555/introspect | jq '{
  stdp: .snn.stdp,
  corrections: .correction_memory.total_corrections,
  qlora: .qlora.buffer_size
}'
```

---

## Version History

| Version | Change |
|---------|--------|
| V11.32 | STDP stats tracking added |
| V11.41 | STDP real-time updates working |
| V11.45 | Correction memory persistence |
| **V11.49** | **STDP + route weights persistence** |

---

## Conclusion

With V11.49, NEUTRO's learning is **fully persistent**:

- Route preferences learned via STDP survive restarts
- Corrections applied to future similar queries
- Training data accumulates for future QLoRA fine-tuning
- Memories persist in vector database

**NEUTRO remembers what it learned.**

---

*Last updated: December 31, 2025*
