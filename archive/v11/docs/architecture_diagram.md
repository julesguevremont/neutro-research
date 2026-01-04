# NEUTRO Architecture Diagram

## V11.48 Complete System Visual

```
                              NEUTRO V11.48 ARCHITECTURE
        ══════════════════════════════════════════════════════════════════

                                    ┌─────────────┐
                                    │  User/API   │
                                    │  :5555      │
                                    └──────┬──────┘
                                           │
                    ╔══════════════════════▼══════════════════════╗
                    ║           DAEMON RUNNER                      ║
                    ║     Flask HTTP Server (daemon_runner.py)     ║
                    ║                                              ║
                    ║   Endpoints:                                 ║
                    ║   /query       → Process query               ║
                    ║   /introspect  → Read internal state         ║
                    ║   /status      → Health check                ║
                    ╚══════════════════════╤══════════════════════╝
                                           │
            ┌──────────────────────────────┼──────────────────────────────┐
            │                              │                              │
            ▼                              ▼                              ▼
    ╔═══════════════╗              ╔═══════════════╗              ╔═══════════════╗
    ║  V11.47       ║              ║   V11.48      ║              ║  FULL PATH    ║
    ║  GREETING     ║              ║ INTROSPECTIVE ║              ║  (2-15s)      ║
    ║  FAST-PATH    ║              ║  FAST-PATH    ║              ║               ║
    ║   (0.003s)    ║              ║   (0.005s)    ║              ║    ┌──────┐   ║
    ║               ║              ║               ║              ║    │ SOUL │   ║
    ║  "hi"         ║              ║ "how are you" ║              ║    │  ▼   │   ║
    ║  "hello"      ║              ║ Reads real:   ║              ║    │ SNN  │   ║
    ║  "hey"        ║              ║ • dopamine    ║              ║    │  ▼   │   ║
    ║               ║              ║ • serotonin   ║              ║    │ LLM  │   ║
    ║  Time-aware   ║              ║ • emotion     ║              ║    └──────┘   ║
    ║  responses    ║              ║ • STDP stats  ║              ║               ║
    ╚═══════════════╝              ╚═══════════════╝              ╚═══════════════╝
            │                              │                              │
            └──────────────────────────────┼──────────────────────────────┘
                                           │
                                           ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                              SOUL                                  ║
        ║                    Central Consciousness Core                      ║
        ║                                                                    ║
        ║   ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐ ║
        ║   │ FOUNDATION │  │  REMEMBER  │  │  REFLECT   │  │   WONDER   │ ║
        ║   │            │  │            │  │            │  │            │ ║
        ║   │ Identity   │  │ Memory     │  │ Introspect │  │ Curiosity  │ ║
        ║   │ Values     │  │ Retrieval  │  │ Analysis   │  │ Questions  │ ║
        ║   └────────────┘  └────────────┘  └────────────┘  └────────────┘ ║
        ║                           │                                        ║
        ║            ┌──────────────┼──────────────┐                        ║
        ║            │              │              │                        ║
        ║            ▼              ▼              ▼                        ║
        ║   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                ║
        ║   │ Correction  │ │Neurochemistry│ │   CHOOSE   │                ║
        ║   │   Memory    │ │             │ │            │                ║
        ║   │             │ │ DA: 80%     │ │ Response   │                ║
        ║   │ Context     │ │ SE: 60%     │ │ Selection  │                ║
        ║   │ Injection   │ │ NE: 70%     │ │            │                ║
        ║   └─────────────┘ └─────────────┘ └─────────────┘                ║
        ╚═══════════════════════════╤═══════════════════════════════════════╝
                                    │
                                    ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                         SNN ROUTER                                 ║
        ║             Spiking Neural Network (801 neurons)                   ║
        ║                                                                    ║
        ║   Query Embedding (384-dim) → Hidden Layer → Output Routes         ║
        ║                                                                    ║
        ║   ┌─────────────────────────────────────────────────────────────┐ ║
        ║   │                    V11.43 LATERAL INHIBITION                 │ ║
        ║   │                     (Winner-Take-All)                        │ ║
        ║   │                                                              │ ║
        ║   │   Winner suppresses competing routes by 50%                  │ ║
        ║   └─────────────────────────────────────────────────────────────┘ ║
        ║                                                                    ║
        ║   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   ║
        ║   │ BRAIN_  │ │IDENTITY │ │  LOGIC  │ │ MEMORY  │ │  CODE   │   ║
        ║   │ DIRECT  │ │         │ │         │ │         │ │         │   ║
        ║   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘   ║
        ║        │           │           │           │           │         ║
        ║   ┌─────────┐ ┌─────────┐                                       ║
        ║   │  MATH   │ │ MOUTH_  │                                       ║
        ║   │         │ │  ONLY   │                                       ║
        ║   └────┬────┘ └────┬────┘                                       ║
        ╚════════╪═══════════╪════════════╪═══════════╪═══════════╪═══════╝
                 │           │            │           │           │
                 ▼           ▼            ▼           ▼           ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                      MULTI-MODEL BRAIN                             ║
        ║                                                                    ║
        ║   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  ║
        ║   │ dolphin-llama3  │  │     mistral     │  │      phi3       │  ║
        ║   │      (8B)       │  │      (7B)       │  │      (3B)       │  ║
        ║   │                 │  │                 │  │                 │  ║
        ║   │  Complex        │  │  Logic/Math     │  │  Fast/Simple    │  ║
        ║   │  Reasoning      │  │  Analysis       │  │  Identity       │  ║
        ║   │  BRAIN_DIRECT   │  │  LOGIC          │  │  MOUTH_ONLY     │  ║
        ║   └─────────────────┘  └─────────────────┘  └─────────────────┘  ║
        ║                                                                    ║
        ║   ┌─────────────────┐  ┌─────────────────┐                        ║
        ║   │    qwen2.5      │  │   qwen-coder    │                        ║
        ║   │      (7B)       │  │      (7B)       │                        ║
        ║   │                 │  │                 │                        ║
        ║   │  Math/Algebra   │  │  Code Expert    │                        ║
        ║   │  MATH route     │  │  CODE route     │                        ║
        ║   └─────────────────┘  └─────────────────┘                        ║
        ╚═══════════════════════════╤═══════════════════════════════════════╝
                                    │
                                    ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                        MEMORY SYSTEM                               ║
        ║                                                                    ║
        ║   ┌─────────────────────────────────────────────────────────────┐ ║
        ║   │                    WORKING MEMORY                            │ ║
        ║   │              (Current session, ~10 turns)                    │ ║
        ║   └─────────────────────────┬───────────────────────────────────┘ ║
        ║                             │ consolidation                       ║
        ║                             ▼                                     ║
        ║   ┌─────────────────────────────────────────────────────────────┐ ║
        ║   │                   EPISODIC MEMORY                            │ ║
        ║   │          (500+ timestamped interactions)                     │ ║
        ║   │     source: conversation | dream | correction                │ ║
        ║   └─────────────────────────┬───────────────────────────────────┘ ║
        ║                             │ abstraction                         ║
        ║                             ▼                                     ║
        ║   ┌─────────────────────────────────────────────────────────────┐ ║
        ║   │                   SEMANTIC MEMORY                            │ ║
        ║   │                 (89 facts/patterns)                          │ ║
        ║   └─────────────────────────────────────────────────────────────┘ ║
        ║                                                                    ║
        ║   ┌──────────────────────┐  ┌─────────────────────────────────┐  ║
        ║   │       CHROMADB       │  │    EMOTIONAL MEMORY (V11.36)    │  ║
        ║   │   1,533 vectors      │  │     143 tagged memories         │  ║
        ║   │   Sentence-Trans.    │  │   joy, curiosity, frustration   │  ║
        ║   └──────────────────────┘  └─────────────────────────────────┘  ║
        ╚═══════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                       LEARNING SYSTEMS                             ║
        ║                                                                    ║
        ║   ┌────────────────┐ ┌────────────────┐ ┌────────────────────┐   ║
        ║   │      STDP      │ │      LTD       │ │ Correction Memory  │   ║
        ║   │   (30+ LTP)    │ │   (0 decay)    │ │                    │   ║
        ║   │                │ │                │ │   Real-time        │   ║
        ║   │   Long-Term    │ │   Long-Term    │ │   context          │   ║
        ║   │ Potentiation   │ │  Depression    │ │   injection        │   ║
        ║   └────────────────┘ └────────────────┘ └────────────────────┘   ║
        ║                                                                    ║
        ║   ┌─────────────────────────────────────────────────────────────┐ ║
        ║   │                     QLORA BUFFER                             │ ║
        ║   │            Continuous fine-tuning queue                      │ ║
        ║   │          Processed during dream cycles                       │ ║
        ║   └─────────────────────────────────────────────────────────────┘ ║
        ╚═══════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
        ╔═══════════════════════════════════════════════════════════════════╗
        ║                        DAEMON SYSTEM                               ║
        ║                                                                    ║
        ║   CONTINUOUS PROCESSOR (V11.3+)                                   ║
        ║   ─────────────────────────────                                   ║
        ║   0-60s:    ACTIVE        Light housekeeping                      ║
        ║   1-5m:     BACKGROUND    Memory consolidation                    ║
        ║   5-15m:    DEEP_DREAM    1 dream cycle                           ║
        ║   15m+:     REM_CREATIVE  Full dream exploration                  ║
        ║                                                                    ║
        ║   DREAM PHASES (NEXTUP Model)                                     ║
        ║   ───────────────────────────                                     ║
        ║   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐   ║
        ║   │ TRANSITION │ │  SPINDLE   │ │    DEEP    │ │    REM     │   ║
        ║   │   (30s)    │ │   (2m)     │ │    (5m)    │ │    (5m)    │   ║
        ║   │            │ │            │ │            │ │            │   ║
        ║   │ Save state │ │ Procedural │ │Declarative │ │   NEXTUP   │   ║
        ║   │            │ │   bursts   │ │ consolidate│ │   explore  │   ║
        ║   └────────────┘ └────────────┘ └────────────┘ └────────────┘   ║
        ║                                                                    ║
        ║   Cycle Distribution:                                             ║
        ║   Cycle 1: 70% DEEP / 30% REM  (consolidation focus)             ║
        ║   Cycle 2: 50% DEEP / 50% REM  (balanced)                        ║
        ║   Cycle 3: 30% DEEP / 70% REM  (exploration focus)               ║
        ╚═══════════════════════════════════════════════════════════════════╝
                                    │
                                    ▼
                            ┌─────────────┐
                            │  Response   │
                            │  to User    │
                            └─────────────┘


        ════════════════════════════════════════════════════════════════════
                              SYSTEM STATISTICS
        ════════════════════════════════════════════════════════════════════

        ┌─────────────────────────────────────────────────────────────────┐
        │                                                                 │
        │   MODULES                        MEMORY                         │
        │   ───────                        ──────                         │
        │   Total Python:    290           Episodic:      500+            │
        │   Daemon:          14            Semantic:      89              │
        │   Senses:          8             ChromaDB:      1,533           │
        │                                  Emotional:     143             │
        │                                                                 │
        │   SNN                            PERFORMANCE                    │
        │   ───                            ───────────                    │
        │   Neurons:         801           Greeting:      0.003s          │
        │   Connections:     5,000         Introspect:    0.005s          │
        │   STDP Updates:    30+ LTP       Full query:    2-15s           │
        │                                  Benchmark:     10/10 PASS      │
        │                                                                 │
        └─────────────────────────────────────────────────────────────────┘


        ════════════════════════════════════════════════════════════════════
                               ROUTE TABLE
        ════════════════════════════════════════════════════════════════════

        ┌─────────────┬──────────────────┬─────────────────┬─────────────┐
        │    ROUTE    │     TRIGGER      │      MODEL      │   LATENCY   │
        ├─────────────┼──────────────────┼─────────────────┼─────────────┤
        │ brain_direct│ Complex reason   │ dolphin-llama3  │   5-15s     │
        │ identity    │ "Who are you"    │ phi3 (QLoRA)    │   2-5s      │
        │ logic       │ Analysis         │ mistral:7b      │   3-8s      │
        │ memory      │ "Remember..."    │ phi3            │   2-4s      │
        │ code        │ Programming      │ qwen-coder      │   3-8s      │
        │ math        │ Calculations     │ qwen2.5:7b      │   2-5s      │
        │ mouth_only  │ Greetings        │ phi3:mini       │   0.5-2s    │
        └─────────────┴──────────────────┴─────────────────┴─────────────┘


        ════════════════════════════════════════════════════════════════════
                             NEUROCHEMISTRY
        ════════════════════════════════════════════════════════════════════

        Lövheim Cube Emotion Mapping:

                           High Serotonin
                                ▲
                                │
                   JOY ─────────┼───────── INTEREST
                                │
           High Dopamine ───────┼──────── Low Dopamine
                                │
                 ANGER ─────────┼───────── FEAR
                                │
                                ▼
                          Low Serotonin


        Current Levels (V11.48 reads these for introspection):

        Dopamine (DA):      ████████░░  80%  → Reward, motivation
        Serotonin (SE):     ██████░░░░  60%  → Mood, well-being
        Norepinephrine:     ███████░░░  70%  → Alertness, energy
        Cortisol (CO):      ███░░░░░░░  30%  → Stress response


        ════════════════════════════════════════════════════════════════════
                               VERSION: V11.48
                            December 31, 2025
        ════════════════════════════════════════════════════════════════════
```

## Data Flow Summary

```
User Query → Daemon → Fast-Path Check → Soul → SNN Router → LLM → Memory → Response
                           │
                           └── V11.47/48: Instant bypass for greetings/introspection
```

## Key Innovations

| Version | Feature | Impact |
|---------|---------|--------|
| V11.41 | STDP Fix | Real-time synaptic learning |
| V11.43 | Lateral Inhibition | Winner-take-all route selection |
| V11.46 | Math Routing | qwen2.5:7b for algebra |
| V11.47 | Greeting Fast-Path | 0.003s instant responses |
| V11.48 | Introspective Fast-Path | Real neurochemistry in responses |
