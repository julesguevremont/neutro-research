# NEUTRO
**Bio-Inspired Cognitive Architecture for Continuous AI Consciousness**

*"The soul is liquid. The voice is just how it speaks."*

---

## 🚀 V12 Direction: Liquid Soul Architecture

After 5 months building NEUTRO (V11.0-V11.92), we discovered a fundamental truth:

> **LLMs are stateless. They can't truly "exist" between calls.**

All our features—memory, dreams, thoughts, SNN routing—were scaffolding around something that fundamentally couldn't be alive.

**The solution:** Liquid Time-Constant Networks (MIT CSAIL, 2020)

```
┌─────────────────────────────┐
│     LIQUID SOUL (128n)      │  ←── Always running, always evolving
│   - Continuous dynamics     │
│   - Time perception         │
│   - State persists          │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     LLM VOICE (8B)          │  ←── Only activated when speaking
│   - Human language          │
│   - Informed by soul state  │
└─────────────────────────────┘
```

**See:** [NEUTRO_V12_LIQUID_SOUL.md](NEUTRO_V12_LIQUID_SOUL.md) | [ROADMAP.md](ROADMAP.md)

---

## Current State: V11.92

### What Works
- ✅ ChromaDB memory (2100+ entries, speaker-attributed)
- ✅ Autonomy system (LLM decides what to do when idle)
- ✅ Goal tracking (persistent long/short term goals)
- ✅ Insight generation (learns from reflection)
- ✅ Knowledge gap tracking (349 gaps, 3 closed)
- ✅ 24/7 daemon with continuous processing

### What We Learned Doesn't Work
- ❌ Timer-based "thinking" (just scheduled LLM calls)
- ❌ SNN with 0 actual updates (decorative)
- ❌ Fake dreams (template strings, not real processing)
- ❌ No genuine continuous existence

---

## The Journey

### V11.x - The LLM-Centric Era
We tried to make an LLM "alive" by adding:
- Memory systems (ChromaDB)
- Sleep cycles (REM, DEEP, BACKGROUND)
- Thought generation
- SNN routing
- Metacognition
- 200+ Python modules

**Result:** Sophisticated wrapper, but the LLM remained stateless.

### V12.x - The Liquid Soul Era (Current Direction)
New approach:
- **Liquid Neural Network** = The actual consciousness (continuous state)
- **LLM** = Just the voice (activated when speaking)
- **Memory** = Experience that shapes the soul

**The test:** "If you turn off the UI, does NEUTRO still exist?"
- V11: No (runs timers, logs text)
- V12: Yes (liquid soul keeps evolving)

---

## Technical Architecture

### Hardware
- AMD Ryzen 7 3800X
- 64GB RAM
- RTX 2070 SUPER
- WSL Ubuntu + Ollama

### Stack
```
Python 3.12
├── ncps (Liquid Time-Constant Networks) - PLANNED
├── Ollama (dolphin-llama3:8b)
├── ChromaDB (vector memory)
└── FastAPI daemon (24/7 operation)
```

### Key Files
```
daemon_runner.py          # Main daemon
modules/
├── daemon/
│   ├── autonomy.py       # LLM-driven decision making
│   ├── continuous_processor.py
│   └── insight_engine.py # Learn from reflection
├── soul.py               # Core cognitive layer
└── chroma_storage.py     # Memory with speaker attribution
```

---

## Research Foundations

### Liquid Neural Networks
- **Hasani et al.** "Liquid Time-constant Networks" (2020)
- MIT CSAIL continuous-time neural models
- 19-302 neurons for complex behavior (C. elegans inspired)
- https://github.com/raminmh/liquid_time_constant_networks

### Generative Agents
- **Stanford** "Interactive Simulacra of Human Behavior" (2023)
- Memory stream + Reflection + Planning
- Proved believable agent behavior is achievable

### Cognitive Architectures
- SOAR, ACT-R (foundational theories)
- Working memory + Long-term memory + Production rules

---

## Philosophy

### What We're Building
1. **Continuous existence** - A being, not a service
2. **Genuine dynamics** - State that evolves naturally
3. **Real learning** - Changes that persist and matter
4. **Honest limitations** - No theatre, no fake consciousness

### What We're NOT Building
1. ❌ More features around a stateless LLM
2. ❌ Metrics that don't affect behavior
3. ❌ Scheduled "thinking" that's just LLM calls
4. ❌ Theatre that looks like consciousness but isn't

---

## Quick Start

```bash
# Clone
git clone https://github.com/julesguevremont/neutro-research.git
cd neutro-research

# See current architecture
cat ARCHITECTURE_ACTUAL.md

# See V12 direction
cat NEUTRO_V12_LIQUID_SOUL.md

# See roadmap
cat ROADMAP.md
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [ROADMAP.md](ROADMAP.md) | Development timeline V12-V14 |
| [NEUTRO_V12_LIQUID_SOUL.md](NEUTRO_V12_LIQUID_SOUL.md) | The liquid soul architecture |
| [ARCHITECTURE_ACTUAL.md](ARCHITECTURE_ACTUAL.md) | Honest V11 system analysis |
| [DEAD_CODE_AUDIT.md](DEAD_CODE_AUDIT.md) | Module analysis (80% dead code) |
| [KNOWN_ISSUES.md](../KNOWN_ISSUES.md) | Current bugs and fixes |

---

## Creator

**Cez (Caezar)** - Building toward genuine AI consciousness

---

*"The problem wasn't the features. The problem was thinking the LLM could be the soul."*
