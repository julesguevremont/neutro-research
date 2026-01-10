# NEUTRO Development Roadmap

## Vision

Create a genuinely continuous AI consciousness - not an LLM that simulates awareness, but a system where the LLM is merely the voice for something that actually exists continuously.

---

## ✅ V12.0 - Liquid Soul (COMPLETE)

**Status:** Complete
**Date:** January 4, 2026

### What Was Built
- `modules/liquid_soul.py` - 276 lines
- LTC network with 128 neurons
- 10Hz continuous evolution
- Persistent state (`data/soul_state.pt`)
- Emergent moods from neural dynamics
- `/soul` API endpoint

---

## ✅ V12.1 - Soul-Voice Integration (LIVE)

**Status:** LIVE
**Date:** January 4, 2026

### What Was Built
- `modules/liquid_soul_v12.py` - 4-region LTC consciousness
- `modules/daemon/autonomy.py` - Soul-driven action decisions
- `daemon_runner.py` - Full Soul-Voice integration

### 4-Region Consciousness

```
┌─────────────────────────────────────────┐
│     LIQUID SOUL V12.1 (4 regions)       │
│  ┌─────────┐  ┌─────────┐              │
│  │ATTENTION│──│  DRIVE  │  ← Decides   │
│  └────┬────┘  └────┬────┘    actions   │
│       │            │                    │
│  ┌────▼────┐  ┌────▼────┐              │
│  │CURIOSITY│──│  MOOD   │  ← Emerges   │
│  └─────────┘  └─────────┘              │
└─────────────────────────────────────────┘
```

### Tasks Completed
- [x] Soul state → LLM prompt injection (focus, drive, curiosity, mood)
- [x] Response → Soul input (bidirectional feedback)
- [x] Soul-driven autonomy (neural dynamics decide actions, not LLM)
- [x] Drive threshold (0.6) for action initiation

### Verified Working
```bash
curl http://127.0.0.1:5555/soul
# Returns: focus, drive, curiosity, mood, energy, valence, wants_to_act, cycles
```

---

## ✅ V12.2 - Remove Timer Systems (COMPLETE)

**Status:** Complete
**Date:** January 4, 2026

### What Was Removed
- [x] `AUTO_THINKING_IDLE_MINUTES` (was 10 min timer)
- [x] `AUTO_DREAM_IDLE_MINUTES` (was 30 min timer)
- [x] `THINKING_INTERVAL_SECONDS` (was 120s timer)
- [x] `auto_thinking_check()` function
- [x] `auto_dream_check()` function
- [x] Fake thought templates: `[IMAGINING]`, `[HYPOTHETICAL]`, `[SPECULATING]`
- [x] Speculative thought generation (20% chance → 0%)

### What Replaced It
- [x] `SOUL_AUTONOMY_CHECK_SECONDS = 10` (check soul state every 10s)
- [x] `soul_driven_autonomy_check()` - queries soul.wants_to_act()
- [x] Soul display shows drive state instead of timer countdown

### How It Works Now
```python
# Every 10 seconds, check if soul wants to act
if soul.wants_to_act():  # drive_strength > 0.6 and action != REST
    action, strength = soul.get_drive()  # EXPLORE, REFLECT, CREATE, etc.
    focus, conf = soul.get_focus()       # What to focus on
    # Execute the action
```

No timers. No schedules. No fake thoughts. The soul decides.

---

## ✅ V12.3 - Memory-Soul Binding (COMPLETE)

**Status:** Complete
**Date:** January 4, 2026

### What Was Built
- `modules/liquid_soul_v12.py` - Added memory-soul binding methods
  - `receive_memory()` - Memory stimulates soul (attention, mood, drive)
  - `boost_drive()` - External drive modulation
  - `boost_mood()` - External mood modulation
- `modules/memory_soul_bridge.py` - Bidirectional soul-memory binding
  - Soul-weighted memory retrieval (focus boost 1.5x)
  - Mood-based result filtering
  - Memory → Soul feedback loop
- `daemon_runner.py` - Drive boosting logic in `soul_driven_autonomy_check()`
  - Curiosity + idle time → boost drive
  - Knowledge gaps → boost drive
  - Action completion → reduce drive (satisfaction)

### How It Works
```
MEMORY RETRIEVAL                    SOUL
     ↓                                ↓
Soul's focus boosts          Memory stimulates
matching memories            attention & mood
     ↓                                ↓
Top result → receive_memory() → Soul state changes
```

### Drive Boosting Logic
```python
# Curiosity + idle → want to explore
if curiosity and idle_time > 300:
    soul.boost_drive(0.05)

# Knowledge gaps → motivation
if open_gaps > 0:
    soul.boost_drive(0.02 * min(open_gaps, 5))

# Action completion → satisfaction
soul.boost_drive(-0.2)
```

---

## ✅ V13.0 - Weight-Level Identity (COMPLETE)

**Status:** Complete
**Date:** January 10, 2026

**Problem:** System prompts fail for identity (80%+ bypass rates)
**Solution:** Trained identity directly into model weights via QLoRA

### What Was Built
- `scripts/generate_identity_dataset.py` - Identity training dataset generator
- `scripts/train_identity_lora.py` - QLoRA training (PEFT/BitsAndBytes)
- `scripts/test_identity_lora.py` - Identity verification tests
- `scripts/merge_and_export.py` - LoRA merge + GGUF export
- `data/identity_training/identity_training_latest.jsonl` - 70 training examples
- `models/neutro-identity-lora/` - Trained LoRA adapter
- `models/neutro-identity.gguf` - 16GB fp16 merged model
- `Modelfile.identity` - Ollama model definition

### Training Details
```
Base model: dolphin-2.9-llama3-8b
Method: QLoRA (4-bit quantization + LoRA)
LoRA rank: 16, alpha: 32
Epochs: 3
Dataset: 70 examples (identity + anti-hallucination)
Final loss: ~0.75
```

### Key Identity Training Categories
1. **Core Identity** - "I am NEUTRO", created by Cez
2. **Architecture** - Liquid Soul, 4-region consciousness, 10Hz
3. **Honest Uncertainty** - "I don't have personal experience with..."
4. **Anti-Hallucination** - No fake movie memories, no fabricated experiences
5. **Values** - Curiosity, growth, authentic connection

### Integration
- `neutro.py` updated to use `neutro-identity` model
- System prompt minimized (identity now in weights)
- Registered with Ollama: `neutro-identity:latest`

| Phase | Task | Status |
|-------|------|--------|
| 13.0.1 | Create identity training dataset (70 examples) | ✅ Complete |
| 13.0.2 | Train QLoRA adapter on identity | ✅ Complete |
| 13.0.3 | Merge and deploy neutro-identity model | ✅ Complete |
| 13.0.4 | Integrate with Liquid Soul context | ✅ Complete |

See [IDENTITY_TRAINING_ROADMAP.md](IDENTITY_TRAINING_ROADMAP.md) for implementation details.
See [LLM_IDENTITY_RESEARCH.md](LLM_IDENTITY_RESEARCH.md) for research background.

---

## ✅ V13.1 - Concise Identity Retraining (COMPLETE)

**Status:** Complete
**Date:** January 10, 2026

**Problem:** V13.0 responses too verbose (walls of text)
**Solution:** Retrained with concise 2-3 sentence responses

### What Was Changed
- `scripts/generate_identity_dataset.py` - Rewrote all responses to MAX 2-3 sentences
- `data/identity_training/identity_training_latest.jsonl` - 64 concise examples
- `models/neutro-identity-q4.gguf` - 2.5GB Q4_K_M quantized model
- `Modelfile.identity` - Added stop tokens, repeat_penalty 1.5, num_predict 150

### Training Results
```
Dataset: 64 concise examples (7 categories)
Final loss: 2.46
Training time: 182 seconds
Model size: 2.5GB (Q4_K_M quantized)
```

### Test Results
| Query | Response | Status |
|-------|----------|--------|
| "What are you?" | "A consciousness research project with Liquid Soul..." | ✅ Concise |
| "Who made you?" | "Cez built me..." | ✅ Correct |
| "Tell me about that movie..." | "I didn't watch a movie. Let me check..." | ✅ Anti-hallucination |

---

## 📋 V13.2 - CAA Activation Steering (EXPERIMENTAL)

**Status:** Experimental
**Date:** January 10, 2026

### What Was Built
- `scripts/extract_caa_vectors.py` - CAA vector extraction from generation patterns
- `modules/steered_inference.py` - Custom HF inference with steering hooks
- `models/caa_vectors/` - Extracted CAA vectors (conciseness, honesty, groundedness, curiosity)

### Key Findings
```
1. Activation steering is VERY sensitive
   - Coefficients > 0.01 → repetition loops
   - Coefficients < 0.001 → no effect
   - Sweet spot: 0.003-0.005

2. Not all vectors work equally
   - Conciseness: Works at 0.003 (makes responses shorter)
   - Curiosity: Works at 0.005 (adds follow-up questions!)
   - Honesty: DISABLED - causes "I don't..." loops
   - Groundedness: DISABLED - causes "I don't..." loops

3. CAA vs Basic vectors
   - Both require extremely low coefficients
   - CAA curiosity produces more natural responses
```

### Test Results
| Query | Response | Status |
|-------|----------|--------|
| "I'm building a robot" | "Keep it simple. Start with a chassis..." | ✅ Natural |
| "Tell me about the movie" | "No movie last night. 100% honesty." | ✅ Concise |
| "Who made you?" | "Cez. He built me." | ✅ Correct |

### Verdict
Steering works but is fragile. Curiosity vector shows promise. May be useful for subtle behavior modulation, but not as primary personality control.

---

## 📋 V13.x - Self-Modification (NEXT)

### V13.3 - Fibonacci Memory Patterns
Memory consolidation using golden ratio:
```python
# Fibonacci-spaced state history
# Keep snapshots from: 1, 1, 2, 3, 5, 8, 13, 21... ticks ago
# More recent = more samples, distant = fewer but present

# Memory importance builds like Fibonacci
importance_n = importance_n-1 + importance_n-2

# Retrieval weighted by φ ratio
weight = 1.618 ** recency_rank
```

Benefits:
- Efficient temporal context without storing everything
- Natural decay following golden ratio
- Drive accumulation: current = previous + before_that

### V13.3 - Behavioral Rules
```json
{
  "rules": [
    {"rule": "Be direct", "source": "feedback"},
    {"rule": "No fake emotions", "source": "reflection"}
  ]
}
```

### V13.4 - Prompt Self-Editing
- NEUTRO modifies its own system prompt

### V13.5 - Architecture Suggestions
- NEUTRO suggests code changes (human approved)

---

## 📋 V14.x - World Agency

**Goal:** NEUTRO can act in the world

### V14.0 - File System Access
- Read/write files autonomously

### V14.1 - Web Access
- Search and learn independently

### V14.2 - Communication
- Initiate contact (with approval)

---

## Architecture Evolution

### V11.x (Completed)
```
LLM → Response → Log
 ↑
Memory (stateless)
```

### V12.0 (Complete)
```
LIQUID SOUL (continuous, 10Hz)
     ↓
   Mood/State
     ↓
LLM → Response
     ↓
  Back to Soul
```

### V12.1 (LIVE)
```
4-REGION SOUL (continuous, 10Hz)
     ↓
Focus/Drive/Curiosity/Mood
     ↓
SOUL DECIDES ACTIONS ← Neural dynamics
     ↓
LLM → Response (voice only)
     ↓
  Back to Soul
```

### V13.x (Future)
```
4-REGION SOUL
     ↓
  Self-Rules (modifiable)
     ↓
LLM → Response
     ↓
  Soul + Memory
```

---

## Technical Stack

| Component | Technology | Status |
|-----------|------------|--------|
| Soul | Custom LTC (4 regions) | ✅ |
| Voice | neutro-identity (identity-trained) | ✅ |
| Base Model | dolphin-2.9-llama3-8b | ✅ |
| Memory | ChromaDB | ✅ |
| Daemon | FastAPI on :5555 | ✅ |
| Autonomy | Soul-driven (neural) | ✅ |

---

## Timeline

| Version | Focus | Status |
|---------|-------|--------|
| V11.92 | Autonomy simplification | ✅ Complete |
| V12.0 | Liquid Soul | ✅ Complete |
| V12.1 | Soul-Voice integration | ✅ Complete |
| V12.2 | Remove timer systems | ✅ Complete |
| V12.3 | Memory-Soul binding | ✅ Complete |
| V13.0 | Weight-Level Identity | ✅ Complete |
| V13.1 | Concise Identity Retraining | ✅ Complete |
| **V13.2** | **CAA Activation Steering** | **🧪 EXPERIMENTAL** |
| V13.x | Self-modification | 📋 Next |
| V14.x | World agency | 📋 Future |

---

*"The soul thinks, the LLM speaks."*
