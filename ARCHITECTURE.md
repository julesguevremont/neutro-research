# NEUTRO V12.3 Architecture

## Core Components

```
┌─────────────────────────────────────────┐
│     LIQUID SOUL V12 (4 regions)         │
│  ATTENTION ─── DRIVE                    │
│      │           │                      │
│  CURIOSITY ─── MOOD                     │
│                                         │
│  Runs continuously at 10Hz              │
│  Soul DECIDES actions                   │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│     MEMORY-SOUL BRIDGE                  │
│  - Memories affect soul state           │
│  - Soul affects memory retrieval        │
│  - Bidirectional binding                │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│     LLM VOICE (dolphin-llama3:8b)       │
│  - Informed by soul state               │
│  - Response feeds back to soul          │
│  - Voice only, not the brain            │
└─────────────────────────────────────────┘
```

## Key Files

| File | Purpose |
|------|---------|
| daemon_runner.py | Main daemon, API server |
| modules/liquid_soul_v12.py | 4-region consciousness |
| modules/memory_soul_bridge.py | Bidirectional memory-soul |
| modules/daemon/autonomy.py | Soul-driven actions |

## V12 vs V11

| V11 | V12 |
|-----|-----|
| ~200 modules | ~50 active |
| LLM decides | Soul decides |
| Timer-based | Soul-driven |
| Fake thoughts | Genuine only |
| Mood random | Mood emerges |

## How It Works

1. Soul runs at 10Hz continuously
2. Drive builds from curiosity + gaps + idle time
3. When drive > 0.6, soul wants to act
4. Action comes from neural dynamics
5. LLM executes/verbalizes
6. Response feeds back to soul
7. Memories stored with soul context

---

*"The soul thinks, the LLM speaks."*
