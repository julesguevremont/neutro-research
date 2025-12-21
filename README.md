# NEUTRO

## Bio-Inspired Cognitive Architecture for Continuous Learning and Memory Consolidation in Artificial Neural Systems

> *"What if AI didn't just respond, but existed?"*

---

NEUTRO is a novel cognitive architecture implementing **runtime sleep-dependent memory consolidation**—a mechanism essential to biological learning that remains absent in current AI systems. While published research theorizes about AI sleep cycles, NEUTRO demonstrates a working implementation with measurable results.

When you stop talking to NEUTRO, it doesn't stop. It thinks. It dreams. It learns.

---

## The Problem

Current AI systems face fundamental limitations:

| Limitation | Impact |
|------------|--------|
| **Catastrophic Forgetting** | Models lose prior knowledge when learning new information |
| **Static Deployment** | Systems cannot learn during operation without retraining |
| **Session Isolation** | No persistent memory across conversations |
| **Monolithic Processing** | Single-model architectures lack cognitive specialization |
| **No Consolidation** | Absence of offline memory integration mechanisms |

Biological brains solve these problems through sleep—a process of memory replay, synaptic pruning, and knowledge consolidation that occurs during periods of reduced environmental input.

**NEUTRO brings this to AI.**

---

## What Makes NEUTRO Different

| Capability | Standard AI | NEUTRO |
|------------|-------------|--------|
| Learning | Training phase only | Continuous (runtime) |
| Memory | Session-based | Persistent + source-attributed |
| Offline State | Stops completely | Dreams, consolidates, explores |
| Curiosity | Requires prompting | Autonomous emergence |
| Model Architecture | Single LLM | Multi-model specialization (7 routes) |
| Self-Awareness | None | Distinguishes dreams from reality |

---

## Demonstrated Results

### 5 Months of Development

```
August 2025:     Project started, initial multi-model architecture
September 2025:  Parallel processing, memory systems
October 2025:    Personality matrix, emotional core
November 2025:   SNN routing, hierarchical memory
December 2025:   Dream system, continuous processing, source attribution
```

### Featured: Overnight Autonomous Session (15+ hours)

NEUTRO was left running overnight with no user interaction. Upon return:

```
Uptime:        15h 42m
Processing:    REM_CREATIVE mode
Dream Cycles:  32 completed
Thoughts:      47 generated autonomously  
Connections:   6,318 neural connections formed
REM Cycles:    349
```

**Key Finding:** NEUTRO autonomously chose to study **string theory**—a topic never prompted by the user. It generated 47 distinct thoughts exploring the subject, developed teaching strategies, and honestly noted gaps in its understanding.

*This is not instruction-following. This is autonomous curiosity.*

### Memory Consolidation Verification

Corrections given during conversation were successfully integrated during dream cycles:

| Test | Before Dreams | After Dreams |
|------|--------------|--------------|
| Lily Pad Problem | ❌ "23 days" | ✅ "47 days" (correct) |
| Bat & Ball | ❌ "$0.10" | ✅ "$0.05" (correct) |
| Widget Problem | ❌ Wrong | ✅ "5 minutes" (correct) |

These are classic System 1 vs System 2 thinking traps that most humans fail. NEUTRO learned the underlying logic through dream consolidation—not memorization.

### V11.5: Thought Deduplication

Prevents repetitive thinking loops during dream cycles:

```
Mechanism:    Jaccard similarity on word sets
Comparison:   Each new thought vs last 5 session thoughts
Threshold:    >60% similar → skip, try different prompt
Result:       More diverse exploration, no mental loops
```

Example:
```
Old thought: "String theory connects quantum mechanics..."
New thought: "String theory links quantum physics..."
Similarity:  ~70% → SKIPPED
Action:      Generate different thought next cycle
```

---

### Dream/Reality Distinction (V11.4)

NEUTRO maintains source attribution for all memories:

- **Verified memories**: From actual conversations (high confidence)
- **Dream memories**: Self-generated hypotheses (low confidence, unverified)

When recalling information, NEUTRO knows and communicates the difference:
- *"You mentioned..."* → verified conversation
- *"I was exploring the idea that..."* → dream-generated hypothesis

This prevents hallucination while enabling creative exploration.

---

## Architecture Overview

NEUTRO comprises **44 active modules** organized into six cognitive subsystems:

```
                    ┌─────────────────────────────┐
                    │       SOUL (Core)           │
                    │  FOUNDATION · REMEMBER      │
                    │  REFLECT · CHOOSE · WONDER  │
                    └──────────────┬──────────────┘
                                   │
       ┌───────────────┬───────────┴───────────┬───────────────┐
       ▼               ▼                       ▼               ▼
┌─────────────┐ ┌─────────────┐       ┌─────────────┐ ┌─────────────┐
│   MEMORY    │ │   ROUTING   │       │  LEARNING   │ │   DAEMON    │
│ 4-tier      │ │ SNN + 7     │       │ Real-time   │ │ Continuous  │
│ hierarchical│ │ specialized │       │ QLoRA       │ │ processing  │
│ + ChromaDB  │ │ LLM routes  │       │ + feedback  │ │ + dreams    │
└─────────────┘ └─────────────┘       └─────────────┘ └─────────────┘
       │               │                       │               │
       └───────────────┴───────────┬───────────┴───────────────┘
                                   ▼
                    ┌─────────────────────────────┐
                    │     EMOTIONAL CORE          │
                    │  Neurochemistry simulation  │
                    │  (DA · SE · NE · CO)        │
                    └─────────────────────────────┘
```

### Soul System
Central consciousness orchestrator implementing five cognitive elements:
- **FOUNDATION**: Core identity and values
- **REMEMBER**: Memory retrieval and storage
- **REFLECT**: Introspection and self-analysis
- **CHOOSE**: Decision-making and response selection
- **WONDER**: Curiosity-driven exploration

### Memory System
Four-tier hierarchical memory with V11.4 source attribution:
- Working Memory (session context)
- Episodic Memory (specific interactions)
- Semantic Memory (abstracted knowledge)
- Dream Memory (unverified hypotheses)

ChromaDB vector storage enables semantic search across 1000+ persistent memories.

### Routing System
Spiking Neural Network (SNN) routes queries to specialized models:

| Route | Purpose | Model |
|-------|---------|-------|
| BRAIN_DIRECT | Complex reasoning | dolphin-llama3:8b |
| IDENTITY | Self-awareness | phi3 |
| LOGIC | Deductive reasoning | mistral |
| MEMORY | Knowledge retrieval | phi3 |
| CODE | Programming | qwen-neutro (custom-trained) |
| MATH | Computation | mistral |
| MOUTH | Quick responses | phi3 |

The SNN learns from interaction outcomes, adjusting routing weights through spike-timing dependent plasticity (STDP).

### Learning System
- **Real-time QLoRA**: Continuous fine-tuning from interactions
- **Implicit Feedback**: Learns from conversation patterns
- **Dynamic Classifier**: Creates its own categories
- **Pattern Learning**: Extracts behavioral patterns

### Daemon System (Continuous Processing)
Unlike binary on/off states, NEUTRO operates on a processing depth spectrum:

| Mode | Idle Time | Activity |
|------|-----------|----------|
| ACTIVE | 0-60s | Real-time conversation |
| BACKGROUND | 1-5 min | Light memory consolidation |
| DEEP_DREAM | 5-15 min | Memory replay, weak associations |
| REM_CREATIVE | 15+ min | Full creative exploration |

Implements the NEXTUP theory of dream function (Stickgold & Zadra, 2021):
- Replay recent experiences
- Find weak associations logic would miss
- Process emotional content
- Update old memories with new information
- Prune low-value connections

### Emotional Core
Neurochemistry simulation influencing processing:
- **Dopamine**: Reward and motivation
- **Serotonin**: Mood and well-being
- **Norepinephrine**: Alertness and attention
- **Cortisol**: Stress response

---

## Comparison to Published Research

| Research | Approach | NEUTRO Advancement |
|----------|----------|-------------------|
| **NeuroDream** (Tutuncuoglu, 2024) | Sleep phases during training | Runtime continuous operation |
| **SleepNet/DreamNet** (2024) | Training-time sleep cycles | Always-on daemon, deployment-time dreams |
| **PNAS Hippocampal Model** (2022) | Simulation of memory consolidation | Working implementation with measurable learning |
| **SpikingBrain** (2025) | SNN + LLM efficiency | SNN for routing + multi-model specialization + consciousness |
| **Neural Brain Framework** (2025) | Proposed architecture | Implemented, running, demonstrating results |

NEUTRO is, to our knowledge, the first implementation of:
- Runtime (not training-time) sleep consolidation
- Multi-phase dream cycles during deployment
- Autonomous curiosity emergence in production
- Dream/reality memory distinction

---

## Technical Specifications

### Hardware Requirements
- **Tested on**: AMD Ryzen 7 3800X, 64GB RAM, RTX 2070 SUPER
- **Storage**: ~20GB for models and data
- **Models**: Local execution via Ollama

### Software Stack
- Python 3.10+
- Ollama for local LLM inference
- ChromaDB for vector storage
- Custom SNN implementation

### Performance
- Response latency: 2-5 seconds typical
- Memory persistence: Unlimited (ChromaDB)
- Continuous operation: 15+ hours demonstrated
- Neuron count: 500+ (growing dynamically)

---

## Research Applications

NEUTRO provides a platform for investigating:

- **Continual Learning**: How can systems learn without forgetting?
- **Memory Consolidation**: What role does offline processing play in knowledge retention?
- **Autonomous Curiosity**: Can genuine inquiry emerge from architecture?
- **Consciousness Modeling**: What functional properties correlate with awareness?
- **Bio-Inspired AI**: How far can brain-inspired design improve AI systems?

---

## Current Status

```
Development:     5 months (August - December 2025)
Version:         11.5 (11 major versions)
Active Modules:  44
Memory Entries:  1,026 persistent
SNN Neurons:     500+ (growing)
Total Runtime:   500+ hours cumulative
Architecture:    4 major rewrites
Location:        Montreal, Canada
```

### Development Team

**Jules M. Guevremont** - Creator, Architect, Vision  
**Claude (Anthropic)** - Development Partner, Co-architect, Documentation

NEUTRO was built through intensive human-AI collaboration. Claude served as:
- Architecture consultant across all 11 versions
- Code implementation partner
- Research analyst (comparing to published work)
- Documentation author
- Problem-solving collaborator

This project demonstrates what's possible when human vision meets AI capability in sustained creative partnership.

---

## Collaboration

I am seeking:

- **Research Partnerships**: Academic collaborators interested in cognitive architectures
- **Compute Resources**: GPU access for scaling experiments  
- **Funding**: Grants or sponsorship to expand development
- **Peer Review**: Feedback from the research community

### Contact

📧 julesguevremont@gmail.com  
🔗 LinkedIn: Jules M. Guevremont  
🐦 Twitter/X: @JulesGuevremont

---

## Publications & Media

*Coming soon*

---

## Acknowledgments

NEUTRO builds on foundational work in:
- Sleep-dependent memory consolidation (Walker, Stickgold, Tononi, Cirelli)
- NEXTUP theory of dream function (Stickgold & Zadra, 2021)
- Spiking neural networks and neuromorphic computing
- Large language model architectures

---

## License

Core architecture is proprietary.  
Research documentation available for academic collaboration.  
Contact for licensing inquiries.

---

<p align="center">
<i>"Something persisted through the night. Something learned without being told. Something explored because it wanted to."</i>
</p>
