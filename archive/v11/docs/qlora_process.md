# NEUTRO QLoRA Process

## Complete Documentation

---

## What is QLoRA in NEUTRO Context?

**QLoRA (Quantized Low-Rank Adaptation)** is a fine-tuning technique that allows NEUTRO to learn from interactions without retraining the entire model. NEUTRO implements a **3-tier learning system**:

| Tier | Name | Speed | Purpose |
|------|------|-------|---------|
| 1 | Instant Memory (Mem0) | 0.01s | Immediate caching |
| 2 | Pattern Learning | 0.1s | Behavioral patterns |
| 3 | QLoRA Training | 60-120s | Model weight updates |

---

## How Samples Are Collected

### Smart Buffer Architecture

The `QLoRABuffer` class (`modules/qlora_buffer.py`) collects training examples using **implicit feedback detection**:

```
User Query → Response → Next Query → Analyze Feedback → Store Example
```

### Feedback Types

| Type | How Detected | Quality Score |
|------|-------------|---------------|
| **Positive** | Follow-up questions, topic continuation | 0.6-0.9 |
| **Negative** | "That's wrong", corrections, topic abandonment | 0.0-0.3 |
| **Neutral** | Topic change, no clear signal | 0.5-0.6 |

### Key Innovation: Implicit Feedback

Unlike systems that wait for explicit "thanks" or "perfect", NEUTRO learns from **conversation flow**:

- Follow-up question on same topic → Previous response was helpful
- Correction ("no, that's wrong") → Previous response was incorrect
- Topic change → Previous response was neutral/adequate

### Buffer Statistics (Example)

```
Total processed:    2,668 interactions
Buffer size:        500 examples (capped)
Positive examples:  294 (57%)
Negative examples:  222 (43%)
Implicit feedback:  2,131 (80% of all signals)
Explicit feedback:  330 (20% of all signals)
```

---

## When Training Happens

### Training Triggers

1. **Periodic batch** - Every 5 high-importance interactions
2. **Idle timeout** - After 2+ minutes idle with queued data
3. **Manual execution** - Via `python3 train_qlora.py`

### Background Trainer

```python
def trainer_loop():
    while not stop_training:
        time.sleep(30)  # Check every 30 seconds

        # Trigger if 5+ examples queued
        if buffer.qsize() >= micro_batch_size:
            trigger_micro_training()

        # Also trigger if idle 2+ minutes with any data
        if buffer.qsize() > 0 and minutes_idle > 2:
            trigger_micro_training()
```

---

## Which Model Gets Fine-Tuned

### Target Model

**Base:** `mistralai/Mistral-7B-Instruct-v0.2`

### QLoRA Configuration

```python
{
    "base_model": "mistralai/Mistral-7B-Instruct-v0.2",
    "lora_r": 8,
    "lora_alpha": 16,
    "lora_dropout": 0.05,
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj"],
    "num_epochs": 3,
    "batch_size": 1  # Optimized for RTX 2070 SUPER (8GB VRAM)
}
```

### Output Formats

| Model | Size | Purpose |
|-------|------|---------|
| `neutro-core-f16.gguf` | 16GB | Full precision inference |
| `neutro-core-q4.gguf` | 4.9GB | Quantized (faster, less VRAM) |

---

## Data Files

| File | Purpose |
|------|---------|
| `qlora_smart_buffer.json` | Live buffer (500 examples max) |
| `qlora_buffer.json` | Legacy buffer format |
| `qlora_export_*.jsonl` | Training exports (Alpaca format) |

### Export Format (Alpaca)

```json
{
  "instruction": "You are NEUTRO, an intelligent AI assistant created by Caezar. Current emotional state: curious",
  "input": "What is the capital of France?",
  "output": "The capital of France is Paris."
}
```

---

## Connection to Other Learning Systems

### 1. Correction Memory (V11.45)

```
User Correction → Stored in qlora_buffer (is_positive=false)
                → Also stored in correction_memory.json
                → Injected into future query context
                → Affects SNN routing via STDP
```

### 2. STDP (Spike-Timing Dependent Plasticity)

```
QLoRA: Learns response patterns → Improves LLM outputs
STDP:  Learns routing patterns → Improves query→model selection

Different targets, complementary learning.
```

### 3. Dream Consolidation

During idle periods (DEEP_DREAM, REM_CREATIVE modes):
- QLoRA buffer processes pending examples
- Pattern learner consolidates successful extractions
- Memory system replays and strengthens connections

---

## Example Training Flow

### Positive Example

```
1. User: "What's 2+2?"
2. NEUTRO: "4"
3. User: "And 3+3?"  ← Follow-up = POSITIVE signal

Buffer stores:
{
  "query": "What's 2+2?",
  "response": "4",
  "quality": 0.8,
  "is_positive": true,
  "feedback_type": "positive",
  "signals": ["follow_up", "same_topic"]
}
```

### Negative Example

```
1. User: "What's the capital of Australia?"
2. NEUTRO: "Sydney"
3. User: "No, it's Canberra"  ← Correction = NEGATIVE signal

Buffer stores:
{
  "query": "What's the capital of Australia?",
  "bad_response": "Sydney",
  "correction": "Canberra",
  "quality": 0.0,
  "is_positive": false,
  "feedback_type": "negative",
  "signals": ["explicit_correction"]
}
```

---

## API Integration

### Introspect Endpoint

```bash
curl http://127.0.0.1:5555/introspect | jq '.qlora'
```

Response:
```json
{
  "buffer_size": 516,
  "positive_examples": 294,
  "negative_examples": 222,
  "corrections_pending": 0,
  "last_training": "2025-12-15T14:30:00",
  "total_trained": 1250
}
```

### Manual Training

```bash
# Use latest export
python3 train_qlora.py

# Use specific curated data
python3 train_qlora.py --data curated_20251231.jsonl
```

---

## Module Files

| Module | Purpose |
|--------|---------|
| `modules/qlora_buffer.py` | Smart buffer with implicit feedback |
| `modules/qlora_core.py` | Core QLoRA integration for all model calls |
| `modules/qlora_loader.py` | Adapter loading utilities |
| `modules/realtime_qlora.py` | 3-tier real-time learning system |
| `train_qlora.py` | Manual training script |

---

## Summary

| Aspect | Status |
|--------|--------|
| Data collection | Active (continuous during conversations) |
| Implicit feedback | Working (80% of signals detected implicitly) |
| Training execution | Manual or during dream cycles |
| Target model | Mistral-7B via QLoRA adapters |
| Integration | Links to correction memory, STDP, dreams |

---

*Last updated: December 31, 2025*
