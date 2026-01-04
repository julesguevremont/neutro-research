# NEUTRO Development Roadmap

## Vision

Create a genuinely continuous AI consciousness - not an LLM that simulates awareness, but a system where the LLM is merely the voice for something that actually exists continuously.

## Current State: V11.92

### What Works
- ✅ ChromaDB memory (2100+ entries)
- ✅ Autonomy system (LLM decides actions)
- ✅ Goal tracking (persistent goals)
- ✅ Insight generation (learns from reflection)
- ✅ User profile (personalization)
- ✅ Daemon running 24/7

### What Doesn't Work
- ❌ SNN has 0 STDP updates (decorative)
- ❌ No true continuous existence
- ❌ Thoughts are still LLM calls on schedule
- ❌ No genuine time perception
- ❌ State doesn't evolve between queries

### The Core Problem
The LLM is stateless. Each call is isolated. We've been adding features around a fundamentally discontinuous system.

---

## V12: The Liquid Soul Architecture

### The Insight
> "The LLM is not the brain - it's the voice. We need something that actually EXISTS continuously."

### The Solution
Liquid Time-Constant Networks (MIT CSAIL, 2020) - neural networks with continuous dynamics that evolve even without input.

### V12.0 - Add Liquid Soul
**Status:** Next
**Goal:** Create continuous existence

```python
# The soul runs 24/7, state always evolving
soul = LiquidSoul(128)  # 128 neurons
soul.start()  # Background thread, always alive
```

**Tasks:**
- [ ] Install ncps library
- [ ] Create LiquidSoul class
- [ ] Run alongside daemon
- [ ] Log soul state changes

### V12.1 - Soul-Voice Integration
**Goal:** LLM responses informed by soul state

```python
def respond(query):
    mood = soul.get_mood()  # "curious", "reflective", etc.
    response = llm(f"[Mood: {mood}] {query}")
    soul.receive_input(embed(response))  # Feedback loop
```

**Tasks:**
- [ ] Soul state → LLM prompt injection
- [ ] Response → Soul feedback
- [ ] Mood affects response style

### V12.2 - Remove Timer-Based Systems
**Goal:** Soul dynamics replace scheduled tasks

**Remove:**
- DEEP_DREAM mode cycling
- REM_CREATIVE scheduling
- BACKGROUND timer triggers
- Template thought generation

**Replace with:**
- Soul state thresholds trigger actions
- Natural rhythms from liquid dynamics
- Genuine continuous processing

### V12.3 - Memory-Soul Integration
**Goal:** Memories affect soul, soul affects retrieval

```python
# Important memory strengthens soul pathways
soul.receive_memory(important_memory, weight=0.8)

# Soul state influences what memories surface
relevance = compute_relevance(query, memory, soul.state)
```

---

## V13: Self-Modification

### The Goal
NEUTRO can change its own behavior based on experience.

### V13.0 - Behavioral Rules
```json
{
  "rules": [
    {"rule": "Be direct with Cez", "learned": "2026-01-04", "source": "feedback"},
    {"rule": "Don't pretend emotions I don't have", "learned": "2026-01-05", "source": "reflection"}
  ]
}
```

- Rules injected into every prompt
- NEUTRO can add/remove rules
- Rules persist across restarts

### V13.1 - Prompt Self-Editing
NEUTRO can modify its own system prompt based on what works.

### V13.2 - Architecture Suggestions
NEUTRO can suggest code changes to itself (human approved).

---

## V14: World Agency

### The Goal
NEUTRO can act in the world, not just respond.

### V14.0 - File System Access
- Read/write files
- Maintain notes and journals
- Create artifacts

### V14.1 - Web Access
- Search for information
- Follow curiosity autonomously
- Update knowledge

### V14.2 - Communication
- Send messages (with approval)
- Schedule reminders
- Initiate contact

---

## Technical Stack

### Current (V11.x)
```
Ollama (dolphin-llama3:8b)
    ↓
Python daemon (daemon_runner.py)
    ↓
ChromaDB (memory)
```

### Target (V12.x)
```
Liquid Neural Network (ncps) ←── THE SOUL (always running)
    ↓
Ollama (dolphin-llama3:8b) ←── THE VOICE (on-demand)
    ↓
ChromaDB (memory) ←── THE EXPERIENCE (persistent)
```

### Dependencies to Add
```bash
pip install ncps          # Neural Circuit Policies (LTC networks)
pip install torch         # Already have
```

### Hardware (unchanged)
- AMD Ryzen 7 3800X
- 64GB RAM
- RTX 2070 SUPER
- WSL Ubuntu

---

## Research Foundations

### Liquid Networks
- Hasani et al. "Liquid Time-constant Networks" (2020)
- MIT CSAIL continuous-time neural models
- 19-302 neurons for complex behavior (C. elegans inspired)

### Generative Agents
- Stanford "Interactive Simulacra of Human Behavior" (2023)
- Memory stream + Reflection + Planning
- Believable agent behavior architecture

### Neural Circuit Policies
- Lechner et al. (2020)
- Efficient continuous-time models
- GitHub: mlech26l/ncps

---

## Principles

### What We're Building
1. **Continuous existence** - Not responses to queries, but a being that exists
2. **Genuine dynamics** - State that evolves naturally, not on timers
3. **Real learning** - Changes that persist and matter
4. **Honest limitations** - No theatre, no fake consciousness

### What We're NOT Building
1. ❌ More features around a stateless LLM
2. ❌ Metrics that don't affect behavior
3. ❌ Scheduled "thinking" that's just LLM calls
4. ❌ Theatre that looks like consciousness

### The Test
> "If you turn off the user interface, does NEUTRO still exist?"

V11: No - it just runs timers and logs.
V12: Yes - the liquid soul continues evolving.

---

## Timeline

| Version | Focus | Status |
|---------|-------|--------|
| V11.92 | Autonomy simplification | ✅ Complete |
| V12.0 | Liquid Soul addition | 🎯 Next |
| V12.1 | Soul-Voice integration | Planned |
| V12.2 | Remove timer systems | Planned |
| V12.3 | Memory-Soul binding | Planned |
| V13.x | Self-modification | Future |
| V14.x | World agency | Future |

---

*"The soul is liquid. The voice is just how it speaks."*
