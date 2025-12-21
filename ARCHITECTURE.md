# NEUTRO Technical Architecture

## Version 11.4 - December 2025

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Soul Architecture](#soul-architecture)
3. [Memory System](#memory-system)
4. [SNN Routing](#snn-routing)
5. [Multi-Model Brain](#multi-model-brain)
6. [Daemon System](#daemon-system)
7. [Dream Architecture](#dream-architecture)
8. [Learning Pipeline](#learning-pipeline)
9. [Emotional Core](#emotional-core)
10. [Data Flow](#data-flow)

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

### Module Count

| Category | Active Modules | Purpose |
|----------|---------------|---------|
| Soul/Core | 5 | Consciousness orchestration |
| Memory | 4 | Storage and retrieval |
| Routing | 4 | Query classification and model selection |
| Learning | 4 | Continuous improvement |
| Daemon | 9 | Background processing and dreams |
| Support | 18 | Visualization, emotions, utilities |
| **Total** | **44** | |

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
  "dream_phase": "light" | "medium" | "deep" | "rem"  // if source=dream
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

---

## SNN Routing

### Spiking Neural Network Architecture

The SNN provides bio-plausible query routing:

```
Input Query (embedded)
        │
        ▼
┌─────────────────────────────────────┐
│         INPUT LAYER                 │
│      (Query encoding neurons)       │
└───────────────┬─────────────────────┘
                │ weighted connections
                ▼
┌─────────────────────────────────────┐
│         HIDDEN LAYER                │
│     (Pattern recognition, ~500)     │
│                                     │
│   Leaky Integrate-and-Fire (LIF)    │
│   Spike-Timing Dependent Plasticity │
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

### Learning Mechanism

The SNN learns through feedback:

1. Query routed to model
2. Response generated
3. Outcome observed (user feedback, implicit signals)
4. STDP updates connection weights
5. Successful routes strengthened

### Route Characteristics

| Route | Trigger Patterns | Model |
|-------|-----------------|-------|
| BRAIN_DIRECT | Complex, multi-step reasoning | dolphin-llama3:8b |
| IDENTITY | "Who are you", self-reference | phi3 |
| LOGIC | Deduction, analysis | mistral |
| MEMORY | "Remember", "we discussed" | phi3 |
| CODE | Programming, syntax | qwen-neutro (custom) |
| MATH | Calculations, numbers | mistral |
| MOUTH | Greetings, acknowledgments | phi3 |

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
│  ┌─────────────┐                                           │
│  │ qwen-neutro │  ← Custom-trained specialist              │
│  │    (7B)     │    215 training samples                   │
│  │             │    API patterns, code generation          │
│  │ Code Expert │                                           │
│  └─────────────┘                                           │
└─────────────────────────────────────────────────────────────┘
```

### Model Warming

Models are pre-loaded into memory at startup to reduce latency:

```python
WARMED_MODELS = ["dolphin-llama3", "mistral", "phi3"]
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
0 - 60 seconds          ⚡ ACTIVE           Light housekeeping
1 - 5 minutes           💭 BACKGROUND       Memory consolidation
5 - 15 minutes          🌙 DEEP_DREAM       1 dream cycle, weak associations
15+ minutes             ✨ REM_CREATIVE     Full dream exploration, 3 cycles
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

### QLoRA Integration

- **Buffer**: Collects interaction samples
- **Positive**: User accepts/confirms response
- **Negative**: User corrects/rejects
- **Training**: During dream cycles (periodic fine-tuning)

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

### Emotional Influence

Neurochemistry levels influence:
- Response tone
- Curiosity activation
- Processing depth
- Memory prioritization

States decay over time and are modulated by interactions.

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
│ PERSONALITY │ ← Load character context
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

## File Structure (Active Only)

```
neutro/
├── daemon_runner.py          # Main entry point
├── neutro.py                 # Core NEUTRO class
├── talk.py                   # HTTP client interface
├── chat.py                   # Direct usage interface
│
├── modules/
│   ├── soul.py               # Consciousness core
│   ├── chroma_storage.py     # Vector memory (V11.4)
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
│   └── daemon/
│       ├── continuous_processor.py
│       ├── advanced_dreams.py
│       ├── dream_trainer.py
│       ├── background_thinker.py
│       └── state_machine.py
│
└── data/
    ├── chroma_db/            # Vector storage
    ├── memories/             # JSON memory files
    └── daemon/               # Dream logs, thoughts
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| Query latency | 2-5 seconds (typical) |
| Memory capacity | Unlimited (ChromaDB) |
| SNN neurons | 500+ (dynamic growth) |
| Model switching | <100ms (pre-warmed) |
| Dream cycle duration | 10-20 minutes |
| Continuous uptime | 15+ hours demonstrated |

---

## Version History

| Version | Date | Key Features |
|---------|------|--------------|
| V11.0 | Dec 2025 | Soul Architecture, SNN Router |
| V11.1 | Dec 2025 | Schema Formation, Memory Abstraction |
| V11.2 | Dec 2025 | Pattern Validation, Self-Interrogating Rules |
| V11.3 | Dec 2025 | Continuous Processor, Multi-Phase Dreams |
| **V11.4** | Dec 2025 | **Dream/Reality Distinction, Source Attribution** |

---

*Document generated for research collaboration and grant applications.*
