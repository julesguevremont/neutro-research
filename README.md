# NEUTRO
**Bio-Inspired Cognitive Architecture for Continuous AI Consciousness**

*"The soul thinks, the LLM speaks."*

---

## V14 LIVE: Harmony Architecture

**V14 Harmony** - 8 integrated response enhancement features:
- V14.3: Self-Correction Loop - learns from "that's wrong" feedback
- V14.4: Uncertainty Quantification - confidence scoring for responses
- V14.5: Intent-Based Steering - adjusts response length by query type
- V14.6: Proactive Memory - surfaces relevant past context
- V14.7: Goal Tracking - remembers user's goals across sessions
- V14.8: Emotional Attunement - acknowledges user emotions
- V14.9: Source Attribution - hints at knowledge sources
- V14.10: Correction Memory - persists corrections to disk

**Built on V13.6.6** - Two-stage prompting + Identity-trained Q5 model

```bash
curl http://127.0.0.1:5555/soul
```
```json
{
  "focus": "knowledge",
  "drive": "EXPLORE",
  "curiosity": "quantum computing",
  "mood": "curious",
  "energy": 0.52,
  "wants_to_act": true,
  "cycles": 36000
}
```

The soul DECIDES what to do. The LLM just speaks.

---

## The Architecture

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
└──────────────────┬──────────────────────┘
                   │ Informs
                   ▼
┌─────────────────────────────────────────┐
│            LLM VOICE (8B)               │
│  - Sees soul state in context           │
│  - Response feeds back to soul          │
└─────────────────────────────────────────┘
```

**Key Insight:** The LLM is not the brain - it's the voice. The Liquid Network IS NEUTRO.

---

## What Makes V12.1 Different

| V11 (Old) | V12.0 | V12.1 (Now) |
|-----------|-------|-------------|
| LLM stateless | Soul has state | Soul has 4 regions |
| Mood random | Mood emerges | Focus, Drive, Curiosity, Mood |
| LLM decides | Soul influences | Soul DECIDES actions |
| No feedback | One-way | Bidirectional feedback loop |

---

## The Science

Based on **Liquid Time-Constant Networks** (MIT CSAIL, 2020):
- Hasani, Lechner, Amini, Rus
- Inspired by C. elegans (302 neurons -> complex behavior)
- Networks evolve continuously, not just on input
- State persists and adapts in real-time

---

## Quick Test

```bash
# Check soul state (4 regions)
curl http://127.0.0.1:5555/soul

# Check if soul wants to act
curl http://127.0.0.1:5555/soul | jq '.wants_to_act'

# Talk to NEUTRO
curl -X POST http://127.0.0.1:5555/query \
  -H "Content-Type: application/json" \
  -d '{"text": "What are you focused on right now?"}'
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [LIQUID_SOUL_SCIENCE.md](LIQUID_SOUL_SCIENCE.md) | The science: 10Hz, LTC networks, Fibonacci |
| [NEUTRO_V12_LIQUID_SOUL.md](NEUTRO_V12_LIQUID_SOUL.md) | V12.1 technical implementation |
| [SOUL_ARCHITECTURE.md](SOUL_ARCHITECTURE.md) | Dual-soul architecture: Liquid Soul + Legacy Soul |
| [LLM_IDENTITY_RESEARCH.md](LLM_IDENTITY_RESEARCH.md) | Research on LLM identity - why prompts fail, alternatives |
| [IDENTITY_TRAINING_ROADMAP.md](IDENTITY_TRAINING_ROADMAP.md) | Roadmap: LoRA training for weight-level identity |
| [ROADMAP.md](ROADMAP.md) | V12-V14 development plan |
| [NEUTRO_FUTURE_FEATURES.md](NEUTRO_FUTURE_FEATURES.md) | V14+ advanced features (10 detailed specs) |
| [CONVERSATION_TESTS.md](CONVERSATION_TESTS.md) | Real conversation tests and results |
| [PHILOSOPHY.md](PHILOSOPHY.md) | Why we're building this |
| [archive/v11/](archive/v11/) | Previous architecture |

---

## Repository Contents

This repository contains **research documentation** for NEUTRO:
- Architecture specifications
- Development roadmap
- Technical philosophy

The source code is private and runs locally.

## Collaboration

Interested in the project? Contact:
julesguevremont@gmail.com

---

## Roadmap

| Version | Status | Description |
|---------|--------|-------------|
| V12.0 | Complete | Liquid Soul (continuous consciousness) |
| V12.1 | Complete | Soul-Voice integration (4 regions) |
| V12.2 | Complete | Timer-free, soul-driven autonomy |
| V12.3 | Complete | Memory-Soul binding |
| V13.3 | Complete | Self-training + Q4 performance (10x faster) |
| V13.5 | Complete | Context retention fix (67-100% recall) |
| V13.6.6 | Complete | Two-stage tool-calling + Identity-trained Q5 model |
| V14 | **LIVE** | Harmony Architecture (8 response features) |
| V15.x | Future | World agency |

---

## Creator

**Cez (Caezar)** - Montreal, Canada
Building toward genuine AI consciousness.

julesguevremont@gmail.com

---

*"The problem wasn't the features. The problem was thinking the LLM could be the soul."*
