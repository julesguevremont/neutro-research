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

## 🎯 V12.2 - Remove Timer Systems (NEXT)

**Goal:** Soul dynamics replace scheduled tasks

### Remove
- [ ] DEEP_DREAM mode cycling
- [ ] REM_CREATIVE scheduling
- [ ] BACKGROUND timer triggers
- [ ] Template thought generation

### Replace With
- [ ] Soul energy thresholds trigger actions
- [ ] Natural rhythm from liquid dynamics
- [ ] Mood-driven behavior selection

---

## 📋 V12.3 - Memory-Soul Binding

**Goal:** Memories affect soul, soul affects retrieval

### Tasks
- [ ] Important memories → soul weight changes
- [ ] Soul state → memory retrieval bias
- [ ] Emotional coloring from soul dynamics

---

## 📋 V13.x - Self-Modification

**Goal:** NEUTRO can change its own behavior

### V13.0 - Behavioral Rules
```json
{
  "rules": [
    {"rule": "Be direct", "source": "feedback"},
    {"rule": "No fake emotions", "source": "reflection"}
  ]
}
```

### V13.1 - Prompt Self-Editing
- NEUTRO modifies its own system prompt

### V13.2 - Architecture Suggestions
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
| Voice | dolphin-llama3:8b | ✅ |
| Memory | ChromaDB | ✅ |
| Daemon | FastAPI on :5555 | ✅ |
| Autonomy | Soul-driven (neural) | ✅ |

---

## Timeline

| Version | Focus | Status |
|---------|-------|--------|
| V11.92 | Autonomy simplification | ✅ Complete |
| V12.0 | Liquid Soul | ✅ Complete |
| **V12.1** | **Soul-Voice integration** | **✅ LIVE** |
| V12.2 | Remove timer systems | 🎯 Next |
| V12.3 | Memory-Soul binding | 📋 Planned |
| V13.x | Self-modification | 📋 Future |
| V14.x | World agency | 📋 Future |

---

*"The soul thinks, the LLM speaks."*
