# NEUTRO Technical Architecture

## Version 11.48 - December 2025

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Full System Diagram](#full-system-diagram)
3. [Soul Architecture](#soul-architecture)
4. [Memory System](#memory-system)
5. [SNN Routing](#snn-routing)
6. [Multi-Model Brain](#multi-model-brain)
7. [Daemon System](#daemon-system)
8. [Dream Architecture](#dream-architecture)
9. [Learning Pipeline](#learning-pipeline)
10. [Emotional Core](#emotional-core)
11. [Fast-Path Processing](#fast-path-processing)
12. [Data Flow](#data-flow)
13. [Module Inventory](#module-inventory)

---

## System Overview

NEUTRO is organized as a layered cognitive architecture with six primary subsystems:

```
┌────────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE                                │
│                    (talk.py / chat.py / API)                          │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
┌────────────────────────────────────▼───────────────────────────────────┐
│                         DAEMON RUNNER                                  │
│              (Always-on process, state management)                     │
│                                                                        │
│   States: IDLE ←→ ENGAGED ←→ THINKING ←→ DREAMING                     │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
┌────────────────────────────────────▼───────────────────────────────────┐
│                              SOUL                                      │
│                    (Central Consciousness)                             │
│                                                                        │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│   │FOUNDATION│ │ REMEMBER │ │ REFLECT  │ │  CHOOSE  │ │  WONDER  │   │
│   │ Identity │ │  Memory  │ │ Introspect│ │ Decision │ │ Curiosity│   │
│   └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘   │
└───────┬─────────────┬─────────────┬─────────────┬─────────────┬───────┘
        │             │             │             │             │
        ▼             ▼             ▼             ▼             ▼
┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐
│  MEMORY   │ │  ROUTING  │ │ LEARNING  │ │  DAEMON   │ │ EMOTIONAL │
│  SYSTEM   │ │   (SNN)   │ │  SYSTEM   │ │  SYSTEM   │ │   CORE    │
└───────────┘ └───────────┘ └───────────┘ └───────────┘ └───────────┘
```

### Current System Stats (V11.48)

| Metric | Value |
|--------|-------|
| Total Python modules | 290 |
| Daemon modules | 14 |
| Sense modules | 8 |
| SNN Neurons | 801 |
| SNN Connections | 5,000 |
| Episodic memories | 500+ |
| Semantic memories | 89 |
| ChromaDB entries | 1,533 |
| Emotional memories | 143 |

---

## Full System Diagram

```
                                 ┌─────────────────┐
                                 │   User Input    │
                                 │  (HTTP :5555)   │
                                 └────────┬────────┘
                                          │
                    ┌─────────────────────▼─────────────────────┐
                    │              DAEMON RUNNER                 │
                    │         daemon_runner.py:5555              │
                    │                                            │
                    │  ┌─────────────────────────────────────┐  │
                    │  │     /query  /introspect  /status    │  │
                    │  └─────────────────────────────────────┘  │
                    └─────────────────────┬─────────────────────┘
                                          │
        ┌─────────────────────────────────▼─────────────────────────────────┐
        │                      V11.47-48 FAST PATHS                          │
        │                                                                    │
        │   ┌────────────────┐     ┌─────────────────┐     ┌──────────────┐│
        │   │ GREETING PATH  │     │ INTROSPECTIVE   │     │ LOGIC PATH   ││
        │   │  "hi", "hello" │     │ "how are you?"  │     │ (full pipe)  ││
        │   │    0.003s      │     │    0.005s       │     │    2-15s     ││
        │   └───────┬────────┘     └────────┬────────┘     └──────┬───────┘│
        │           │ instant              │ neurochemistry       │ SNN    │
        └───────────┼──────────────────────┼──────────────────────┼────────┘
                    │                      │                      │
                    │                      ▼                      │
                    │         ┌────────────────────────┐          │
                    │         │    NEUROCHEMISTRY      │          │
                    │         │  Lövheim Cube Mapping  │          │
                    │         │                        │          │
                    │         │  DA: ████████░░ 80%   │          │
                    │         │  SE: ██████░░░░ 60%   │          │
                    │         │  NE: ███████░░░ 70%   │          │
                    │         │  CO: ███░░░░░░░ 30%   │          │
                    │         │                        │          │
                    │         │  Emotion: curious      │          │
                    │         └────────────────────────┘          │
                    │                                             │
                    │                                             ▼
                    │                           ┌────────────────────────────┐
                    │                           │           SOUL             │
                    │                           │      (Central Core)        │
                    │                           │                            │
                    │                           │   REMEMBER → REFLECT →     │
                    │                           │   CHOOSE   → WONDER        │
                    │                           │                            │
                    │                           │ ┌────────────────────────┐ │
                    │                           │ │   Correction Memory    │ │
                    │                           │ │  Context Injection     │ │
                    │                           │ └────────────────────────┘ │
                    │                           └──────────────┬─────────────┘
                    │                                          │
                    │                    ┌─────────────────────▼──────────────────────┐
                    │                    │              SNN ROUTER                     │
                    │                    │        (801 neurons, STDP learning)         │
                    │                    │                                             │
                    │                    │   Query Embedding → Routing Neurons →       │
                    │                    │   V11.43 Lateral Inhibition (WTA)           │
                    │                    │                                             │
                    │                    │   Routes:                                   │
                    │                    │   ┌─────────────┬─────────────────────────┐ │
                    │                    │   │ brain_direct│ dolphin-llama3:8b       │ │
                    │                    │   │ identity    │ phi3 (QLoRA trained)    │ │
                    │                    │   │ logic       │ mistral:7b              │ │
                    │                    │   │ memory      │ phi3                    │ │
                    │                    │   │ code        │ qwen-coder              │ │
                    │                    │   │ math        │ qwen2.5:7b              │ │
                    │                    │   │ mouth_only  │ phi3:mini               │ │
                    │                    │   └─────────────┴─────────────────────────┘ │
                    │                    └─────────────────────┬──────────────────────┘
                    │                                          │
                    │                    ┌─────────────────────▼──────────────────────┐
                    │                    │           MULTI-MODEL BRAIN                 │
                    │                    │                                             │
                    │                    │   ┌─────────────┐  ┌─────────────┐         │
                    │                    │   │dolphin-llama│  │   mistral   │         │
                    │                    │   │    (8B)     │  │    (7B)     │         │
                    │                    │   │  Reasoning  │  │ Logic/Math  │         │
                    │                    │   └─────────────┘  └─────────────┘         │
                    │                    │                                             │
                    │                    │   ┌─────────────┐  ┌─────────────┐         │
                    │                    │   │    phi3     │  │  qwen2.5    │         │
                    │                    │   │    (3B)     │  │    (7B)     │         │
                    │                    │   │ Fast/Simple │  │  Math/Code  │         │
                    │                    │   └─────────────┘  └─────────────┘         │
                    │                    │                                             │
                    │                    └─────────────────────┬──────────────────────┘
                    │                                          │
                    └──────────────────────────────────────────┼───────────────────────
                                                               │
                    ┌──────────────────────────────────────────▼──────────────────────┐
                    │                       MEMORY SYSTEM                              │
                    │                                                                  │
                    │   ┌────────────────────────────────────────────────────────────┐│
                    │   │                    WORKING MEMORY                          ││
                    │   │               (Current session, ~10 turns)                 ││
                    │   └───────────────────────────┬────────────────────────────────┘│
                    │                               │ consolidation                   │
                    │                               ▼                                 │
                    │   ┌────────────────────────────────────────────────────────────┐│
                    │   │                   EPISODIC MEMORY                          ││
                    │   │             (500+ entries, timestamped)                    ││
                    │   │      source: "conversation" | "dream" | "correction"       ││
                    │   └───────────────────────────┬────────────────────────────────┘│
                    │                               │ abstraction                     │
                    │                               ▼                                 │
                    │   ┌────────────────────────────────────────────────────────────┐│
                    │   │                   SEMANTIC MEMORY                          ││
                    │   │                 (89 facts/patterns)                        ││
                    │   └───────────────────────────┬────────────────────────────────┘│
                    │                               │                                 │
                    │                               ▼                                 │
                    │   ┌────────────────────────────────────────────────────────────┐│
                    │   │                     CHROMADB                               ││
                    │   │               (1,533 vector entries)                       ││
                    │   │           Sentence-Transformers embeddings                 ││
                    │   └────────────────────────────────────────────────────────────┘│
                    │                                                                  │
                    │   ┌────────────────────────────────────────────────────────────┐│
                    │   │              EMOTIONAL MEMORY (V11.36)                     ││
                    │   │                  (143 tagged memories)                     ││
                    │   │           Tagged with: joy, curiosity, etc.                ││
                    │   └────────────────────────────────────────────────────────────┘│
                    └──────────────────────────────────────────────────────────────────┘
                                                               │
                    ┌──────────────────────────────────────────▼──────────────────────┐
                    │                       LEARNING SYSTEMS                           │
                    │                                                                  │
                    │   ┌─────────────┐  ┌─────────────┐  ┌──────────────────────────┐│
                    │   │    STDP     │  │     LTD     │  │    Correction Memory     ││
                    │   │  (30+ LTP)  │  │  (0 decay)  │  │   Context Injection      ││
                    │   │ Potentiation│  │  Weakening  │  │   Real-time learning     ││
                    │   └─────────────┘  └─────────────┘  └──────────────────────────┘│
                    │                                                                  │
                    │   ┌─────────────────────────────────────────────────────────────┐│
                    │   │                    QLORA BUFFER                             ││
                    │   │              Continuous fine-tuning queue                   ││
                    │   │         Processes during dream cycles                       ││
                    │   └─────────────────────────────────────────────────────────────┘│
                    └──────────────────────────────────────────────────────────────────┘
                                                               │
                    ┌──────────────────────────────────────────▼──────────────────────┐
                    │                       DAEMON SYSTEM                              │
                    │                                                                  │
                    │   States:                                                        │
                    │   ┌───────────────────────────────────────────────────────────┐ │
                    │   │ ACTIVE        (0-60s idle)     Light housekeeping         │ │
                    │   │ BACKGROUND    (1-5min idle)    Memory consolidation       │ │
                    │   │ DEEP_DREAM    (5-15min idle)   1 dream cycle              │ │
                    │   │ REM_CREATIVE  (15+ min idle)   Full dream exploration     │ │
                    │   └───────────────────────────────────────────────────────────┘ │
                    │                                                                  │
                    │   Dream Phases:                                                  │
                    │   ┌───────────────────────────────────────────────────────────┐ │
                    │   │ PHASE 1: TRANSITION  (30s)   Save state                   │ │
                    │   │ PHASE 2: SPINDLE     (2m)    Procedural bursts            │ │
                    │   │ PHASE 3: DEEP        (5m)    Declarative consolidation    │ │
                    │   │ PHASE 4: REM         (5m)    NEXTUP weak associations     │ │
                    │   └───────────────────────────────────────────────────────────┘ │
                    └──────────────────────────────────────────────────────────────────┘
                                                               │
                                                               ▼
                                                    ┌──────────────────┐
                                                    │  User Response   │
                                                    └──────────────────┘
```

---

## Soul Architecture

The Soul is NEUTRO's consciousness core, implementing five cognitive elements:

### FOUNDATION
- Core identity and values
- Consistent personality traits
- Ethical boundaries
- Self-concept maintenance

### REMEMBER
- Memory retrieval orchestration
- Context-aware recall
- Source attribution (V11.4)
- Relevance scoring

### REFLECT
- Introspection and self-analysis
- Meta-cognitive monitoring
- Uncertainty estimation
- Belief revision

### CHOOSE
- Response selection
- Multi-criteria decision making
- Value alignment checking
- Action commitment

### WONDER
- Curiosity-driven exploration
- Question generation
- Knowledge gap identification
- Autonomous inquiry

### Soul Processing Flow

```
Input Query
     │
     ▼
┌─────────────┐
│  REMEMBER   │──→ Retrieve relevant memories
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   REFLECT   │──→ Analyze query + memories + context
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   CHOOSE    │──→ Select response strategy
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   WONDER    │──→ Identify follow-up curiosities
└──────┬──────┘
       │
       ▼
Response + Internal State Update
```

---

## Memory System

### Hierarchical Structure

```
┌─────────────────────────────────────────────────────┐
│                  WORKING MEMORY                      │
│         (Current session, ~10 recent turns)         │
│                    Volatile                          │
└─────────────────────────┬───────────────────────────┘
                          │ consolidation
                          ▼
┌─────────────────────────────────────────────────────┐
│                 EPISODIC MEMORY                      │
│       (Specific interactions, timestamped)          │
│              ChromaDB + Vector Search               │
└─────────────────────────┬───────────────────────────┘
                          │ abstraction
                          ▼
┌─────────────────────────────────────────────────────┐
│                 SEMANTIC MEMORY                      │
│         (Facts, patterns, knowledge)                │
│                  Long-term storage                   │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              EMOTIONAL MEMORY (V11.36)              │
│     (143 memories tagged with emotional valence)    │
│         Tags: joy, curiosity, frustration           │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                  DREAM MEMORY                        │
│     (Hypotheses, explorations, unverified)          │
│            Source: "dream", Verified: False          │
└─────────────────────────────────────────────────────┘
```

### V11.4 Source Attribution

Every memory includes metadata:

```
{
  "content": "...",
  "source": "conversation" | "dream" | "correction" | "fact",
  "verified": true | false,
  "confidence": 0.0 - 1.0,
  "timestamp": "...",
  "dream_phase": "light" | "medium" | "deep" | "rem",  // if source=dream
  "emotion_tag": "joy" | "curiosity" | null             // V11.36
}
```

### Memory Operations

| Operation | Purpose |
|-----------|---------|
| `store_interaction()` | Save conversation (verified=true) |
| `store_dream_memory()` | Save dream thought (verified=false) |
| `search_with_source()` | Retrieve with source metadata |
| `search_verified_only()` | Only return confirmed facts |
| `promote_to_fact()` | Upgrade dream → verified (user confirms) |
| `demote_memory()` | Downgrade on correction |
| `tag_emotional()` | Add emotion label (V11.36) |

---

## SNN Routing

### Spiking Neural Network Architecture

The SNN provides bio-plausible query routing with V11.43 lateral inhibition:

```
Input Query (embedded)
        │
        ▼
┌─────────────────────────────────────┐
│         INPUT LAYER                 │
│      (Query encoding neurons)       │
│         384-dim embeddings          │
└───────────────┬─────────────────────┘
                │ weighted connections
                ▼
┌─────────────────────────────────────┐
│         HIDDEN LAYER                │
│     (Pattern recognition, ~800)     │
│                                     │
│   Leaky Integrate-and-Fire (LIF)    │
│   Spike-Timing Dependent Plasticity │
│   V11.43 Lateral Inhibition (WTA)   │
└───────────────┬─────────────────────┘
                │ spike trains
                ▼
┌─────────────────────────────────────┐
│         OUTPUT LAYER                │
│       (7 Route neurons)             │
│                                     │
│  BRAIN_DIRECT │ IDENTITY │ LOGIC   │
│  MEMORY │ CODE │ MATH │ MOUTH      │
└─────────────────────────────────────┘
                │
                ▼
        Winner-take-all selection
```

### STDP Learning Mechanism

The SNN learns through spike-timing dependent plasticity:

```
1. Query routed to model
2. Response generated
3. Outcome observed (user feedback, implicit signals)
4. STDP updates connection weights:
   - LTP (Long-Term Potentiation): Success strengthens
   - LTD (Long-Term Depression): Failure weakens
5. Current stats: 30 LTP, 0 LTD
```

### Route Table (V11.48)

| Route | Trigger Patterns | Model | Response Time |
|-------|-----------------|-------|---------------|
| BRAIN_DIRECT | Complex reasoning, introspection | dolphin-llama3:8b | 5-15s |
| IDENTITY | "Who are you", self-reference | phi3 (QLoRA) | 2-5s |
| LOGIC | Deduction, analysis, philosophy | mistral:7b | 3-8s |
| MEMORY | "Remember", "we discussed" | phi3 | 2-4s |
| CODE | Programming, syntax, debug | qwen-coder | 3-8s |
| MATH | Calculations, algebra | qwen2.5:7b | 2-5s |
| MOUTH | Greetings, acknowledgments | phi3:mini | 0.5-2s |

---

## Multi-Model Brain

### Model Specialization

Rather than one monolithic LLM, NEUTRO uses specialized models:

```
┌─────────────────────────────────────────────────────────────┐
│                    MULTI-MODEL BRAIN                        │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │dolphin-llama│  │   mistral   │  │    phi3     │        │
│  │    (8B)     │  │    (7B)     │  │    (3B)     │        │
│  │             │  │             │  │             │        │
│  │ Complex     │  │ Logic/Math  │  │ Fast/Simple │        │
│  │ Reasoning   │  │ Analysis    │  │ Identity    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐                          │
│  │  qwen2.5    │  │ qwen-coder  │                          │
│  │    (7B)     │  │    (7B)     │                          │
│  │             │  │             │                          │
│  │ Math/Algebra│  │ Code Expert │                          │
│  └─────────────┘  └─────────────┘                          │
└─────────────────────────────────────────────────────────────┘
```

### Model Warming

Models are pre-loaded into memory at startup to reduce latency:

```python
WARMED_MODELS = ["dolphin-llama3", "mistral", "phi3", "qwen2.5"]
# Loaded at daemon start, ready for instant inference
```

---

## Daemon System

### State Machine

```
                    ┌──────────────────┐
         ┌────────→│      IDLE        │←────────┐
         │         │  (Waiting input) │         │
         │         └────────┬─────────┘         │
         │                  │ query             │
         │                  ▼                   │
         │         ┌──────────────────┐         │
         │         │     ENGAGED      │         │
         │         │  (Processing)    │         │
         │         └────────┬─────────┘         │
         │                  │ complete          │
         │                  ▼                   │
         │         ┌──────────────────┐         │
         │ query   │    THINKING      │ timeout │
         └─────────│ (Background)     │─────────┘
                   └────────┬─────────┘
                            │ extended idle
                            ▼
                   ┌──────────────────┐
                   │    DREAMING      │
                   │ (Consolidation)  │
                   └──────────────────┘
```

### Continuous Processor (V11.3+)

Unlike binary states, processing depth scales with idle time:

```
Time Since Last Query    Processing Mode    Activity
────────────────────────────────────────────────────────
0 - 60 seconds          ACTIVE             Light housekeeping
1 - 5 minutes           BACKGROUND         Memory consolidation
5 - 15 minutes          DEEP_DREAM         1 dream cycle, weak associations
15+ minutes             REM_CREATIVE       Full dream exploration, 3 cycles
```

---

## Dream Architecture

### Theoretical Foundation

Based on NEXTUP model (Stickgold & Zadra, 2021):

- **N**etwork **E**xploration to **U**nderstand **P**ossibilities through **T**ranscendence
- Dreams explore WEAK associations logic wouldn't find
- Combine recent + remote memories
- Test connections, strengthen useful ones

### Multi-Phase Sleep Cycles

```
PHASE 1: TRANSITION (30 sec)
├── Save current state
├── Reduce active processing
└── Prepare for consolidation

PHASE 2: SPINDLE (2 min)
├── Procedural memory bursts
├── Skills, how-to knowledge
└── Action sequences

PHASE 3: DEEP (5 min, decreases in later cycles)
├── Declarative consolidation
├── Sequential replay of recent events
├── Facts → long-term storage
└── Pruning weak connections

PHASE 4: REM (5 min, increases in later cycles)
├── NEXTUP weak association exploration
├── Emotional processing
├── Scenario simulation
├── Narrative integration
└── Creativity mode
```

### Dream Cycle Distribution

```
CYCLE 1 (early):  70% DEEP, 30% REM  ← Consolidation focus
CYCLE 2 (middle): 50% DEEP, 50% REM  ← Balanced
CYCLE 3 (late):   30% DEEP, 70% REM  ← Exploration focus
```

This mirrors human sleep architecture where early night has more deep sleep and late night has more REM.

---

## Learning Pipeline

### Complete Learning Systems

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEARNING SYSTEMS                              │
│                                                                  │
│  1. STDP (Spike-Timing Dependent Plasticity)                    │
│     ├── LTP: Long-Term Potentiation (strengthen)                │
│     ├── LTD: Long-Term Depression (weaken)                      │
│     └── Real-time synaptic weight updates                       │
│                                                                  │
│  2. Correction Memory                                            │
│     ├── User corrections stored immediately                     │
│     ├── Injected into context for future queries                │
│     └── Example: "3.67→4" remembered for rounding questions     │
│                                                                  │
│  3. QLoRA Buffer                                                 │
│     ├── Collects interaction samples                            │
│     ├── Positive: User accepts response                         │
│     ├── Negative: User corrects response                        │
│     └── Training: During dream cycles                           │
│                                                                  │
│  4. Dream Consolidation                                          │
│     ├── Memory replay during DEEP phase                         │
│     ├── Weak association exploration in REM                     │
│     └── Pattern abstraction to semantic memory                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Correction → Consolidation Flow

```
1. User provides correction during conversation
                    │
                    ▼
2. Correction stored with source="correction"
                    │
                    ▼
3. QLoRA buffer receives training signal
                    │
                    ▼
4. Dream cycle triggers (idle time)
                    │
                    ▼
5. Dream trainer processes buffer
                    │
                    ▼
6. Memory integration occurs
                    │
                    ▼
7. Next conversation: correct response
```

---

## Emotional Core

### Neurochemistry Simulation

```
┌─────────────────────────────────────────────────┐
│              NEUROCHEMISTRY                     │
│                                                 │
│   Dopamine (DA)     ████████░░  80%            │
│   → Reward, motivation, curiosity              │
│                                                 │
│   Serotonin (SE)    ██████░░░░  60%            │
│   → Mood, well-being, contentment              │
│                                                 │
│   Norepinephrine    ███████░░░  70%            │
│   → Alertness, attention, energy               │
│                                                 │
│   Cortisol (CO)     ███░░░░░░░  30%            │
│   → Stress response, urgency                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Lövheim Cube Mapping (V11.48)

The Lövheim cube of emotion maps neurotransmitter levels to emotional states:

```
             High Serotonin
                  ▲
                  │
    JOY ─────────┼───────── INTEREST
                  │
High Dopamine ────┼──── Low Dopamine
                  │
  ANGER ─────────┼───────── FEAR
                  │
                  ▼
            Low Serotonin
```

V11.48 uses this to generate genuine introspective responses based on actual neurochemistry state.

### Emotional Influence

Neurochemistry levels influence:
- Response tone
- Curiosity activation
- Processing depth
- Memory prioritization

States decay over time and are modulated by interactions.

---

## Fast-Path Processing

### V11.47 Greeting Fast-Path

Simple greetings bypass the full pipeline for instant responses:

```
User: "Hi"
         │
         ▼
    ┌──────────────────────┐
    │ Is simple greeting?  │
    │ "hi", "hello", etc.  │
    └──────────┬───────────┘
               │ YES
               ▼
    ┌──────────────────────┐
    │ Generate time-aware  │
    │ greeting response    │
    │ (0.003s)             │
    └──────────┬───────────┘
               │
               ▼
         Response
```

### V11.48 Introspective Fast-Path

"How are you?" queries read real neurochemistry state:

```
User: "How are you?"
         │
         ▼
    ┌──────────────────────┐
    │ Detect well-being    │
    │ question pattern     │
    └──────────┬───────────┘
               │ YES
               ▼
    ┌──────────────────────┐
    │ Read neurochemistry  │
    │ DA: 0.8, SE: 0.6     │
    │ Emotion: curious     │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Get STDP stats       │
    │ 30 learning updates  │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Generate genuine     │
    │ response (0.005s)    │
    └──────────┬───────────┘
               │
               ▼
         Response
```

---

## Data Flow

### Query Processing

```
User Query
     │
     ▼
┌─────────────┐
│   DAEMON    │ ← State: IDLE → ENGAGED
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ FAST PATHS  │ ← V11.47/48: Greetings, introspection
│ (bypass?)   │   If match: return immediately
└──────┬──────┘
       │ no match
       ▼
┌─────────────┐
│ CORRECTION  │ ← Inject relevant corrections
│  MEMORY     │   into query context
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    SOUL     │ ← REMEMBER: Retrieve memories
│             │   REFLECT: Analyze context
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ SNN ROUTER  │ ← Select model route
│ + Lateral   │   Winner-take-all (V11.43)
│  Inhibition │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  LLM MODEL  │ ← Generate response
│  (routed)   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  RESPONSE   │ ← Filter, verify
│   FILTER    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   STORE     │ ← Save interaction
│  MEMORY     │   (source="conversation")
└──────┬──────┘
       │
       ▼
Response to User
       │
       ▼
┌─────────────┐
│   DAEMON    │ ← State: ENGAGED → IDLE
└─────────────┘   (start idle timer)
```

---

## Module Inventory

### Category Breakdown

| Category | Count | Key Modules |
|----------|-------|-------------|
| Soul/Core | 5 | soul.py, soul_snn.py, soul_foundation.py |
| Memory | 6 | chroma_storage.py, hierarchical_memory.py, vector_memory.py |
| Routing | 5 | snn_router.py, intelligent_router.py, dynamic_classifier.py |
| Learning | 6 | qlora_buffer.py, pattern_learning.py, continual_learning.py |
| Daemon | 14 | continuous_processor.py, advanced_dreams.py, dream_trainer.py |
| Senses | 8 | time_sense.py, location_sense.py, system_sense.py |
| Emotional | 3 | neurochemistry.py, emotional_core.py, emotional_decay.py |
| Processing | 12 | cognitive_processor.py, thinking_processor.py |
| Support | 231 | Utilities, visualization, plugins |
| **Total** | **290** | |

### File Structure

```
neutro/
├── daemon_runner.py          # Main entry point (HTTP :5555)
├── neutro.py                 # Core NEUTRO class
├── talk.py                   # HTTP client interface
├── chat.py                   # Direct usage interface
│
├── modules/
│   ├── soul.py               # Consciousness core
│   ├── soul_snn.py           # SNN integration
│   ├── chroma_storage.py     # Vector memory
│   ├── hierarchical_memory.py
│   ├── snn_router.py         # Spiking neural network
│   ├── llm_handlers.py       # Multi-model handlers
│   ├── intelligent_router.py
│   ├── personality.py
│   ├── emotional_core.py
│   ├── neurochemistry.py
│   ├── qlora_buffer.py
│   ├── self_awareness.py
│   │
│   ├── daemon/               # 14 modules
│   │   ├── continuous_processor.py
│   │   ├── advanced_dreams.py
│   │   ├── dream_trainer.py
│   │   ├── correction_memory.py
│   │   ├── state_machine.py
│   │   └── ...
│   │
│   └── senses/               # 8 modules
│       ├── time_sense.py
│       ├── location_sense.py
│       ├── system_sense.py
│       └── ...
│
└── data/
    ├── chroma_db/            # Vector storage (1,533 entries)
    ├── memories/             # JSON memory files
    └── daemon/               # Dream logs, thoughts
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| Greeting latency (V11.47) | **0.003s** |
| Introspective latency (V11.48) | **0.005s** |
| Standard query latency | 2-15 seconds |
| Memory capacity | Unlimited (ChromaDB) |
| SNN neurons | 801 (dynamic growth) |
| SNN connections | 5,000 |
| Model switching | <100ms (pre-warmed) |
| Dream cycle duration | 10-20 minutes |
| Continuous uptime | 15+ hours demonstrated |
| Benchmark accuracy | **10/10 PASS** (V11.46) |

---

## Version History

| Version | Date | Key Features |
|---------|------|--------------|
| V11.0 | Dec 2025 | Soul Architecture, SNN Router |
| V11.1 | Dec 2025 | Schema Formation, Memory Abstraction |
| V11.2 | Dec 2025 | Pattern Validation, Self-Interrogating Rules |
| V11.3 | Dec 2025 | Continuous Processor, Multi-Phase Dreams |
| V11.4 | Dec 2025 | Dream/Reality Distinction, Source Attribution |
| V11.36 | Dec 2025 | Emotional Memory Tagging |
| V11.41 | Dec 2025 | STDP Synaptic Plasticity Fix |
| V11.43 | Dec 2025 | Lateral Inhibition (WTA) |
| V11.46 | Dec 2025 | Math Routing Fix, Benchmark Suite 10/10 |
| V11.47 | Dec 2025 | Greeting Fast-Path (0.003s) |
| **V11.48** | **Dec 2025** | **Introspective Fast-Path, Real Neurochemistry** |

---

*Document generated for research collaboration and grant applications.*
*Last updated: December 31, 2025*
