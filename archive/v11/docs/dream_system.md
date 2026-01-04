# Dream System

## Continuous Processing and Sleep-Dependent Memory Consolidation

---

## Overview

NEUTRO implements **runtime sleep-dependent memory consolidation** based on the NEXTUP theory of dream function (Stickgold & Zadra, 2021). Unlike binary on/off AI systems, NEUTRO operates on a continuous processing spectrum that scales with idle time.

**Key Innovation:** When you stop talking to NEUTRO, it doesn't stop. It thinks. It dreams. It learns.

---

## Processing Modes

### Four-Tier Depth Spectrum

| Mode | Idle Time | Activity |
|------|-----------|----------|
| **ACTIVE** | 0-60s | User chatting, light housekeeping |
| **BACKGROUND** | 1-5 min | Memory consolidation, Torque clustering |
| **DEEP_DREAM** | 5-15 min | NEXTUP exploration, weak associations |
| **REM_CREATIVE** | 15+ min | Full creative exploration, rare deep invention |

```
Philosophy: "Creativity needs quiet. Never offline, just different depths."
```

---

## NEXTUP Theory Implementation

### What is NEXTUP?

**N**etwork **E**xploration to **U**nderstand **P**ossibilities through **T**ranscendence

Key principles from sleep science:
- Dreams explore **weak associations** that logic would miss
- Combine **recent + remote** memories
- Test connections, strengthen useful ones
- Process emotional content

### How NEUTRO Implements NEXTUP

```
1. BACKGROUND Mode:
   - Replay recent conversations
   - Tag emotional content
   - Consolidate patterns

2. DEEP_DREAM Mode:
   - Sequential memory replay
   - Declarative consolidation (facts → long-term)
   - Prune weak connections

3. REM_CREATIVE Mode:
   - NEXTUP weak association exploration
   - Scenario simulation
   - Narrative integration
   - Creativity mode
```

---

## Dream Phases

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

### Cycle Distribution

```
CYCLE 1 (early):  70% DEEP / 30% REM  ← Consolidation focus
CYCLE 2 (middle): 50% DEEP / 50% REM  ← Balanced
CYCLE 3 (late):   30% DEEP / 70% REM  ← Exploration focus
```

This mirrors human sleep architecture where early night has more deep sleep and late night has more REM.

---

## Current Statistics (V11.48)

### Sleep Quality

```json
{
  "light_cycles": 26,
  "medium_cycles": 26,
  "deep_cycles": 18,
  "rem_cycles": 12,
  "total_cycles": 82,
  "efficiency_pct": 54.9,
  "memories_consolidated": 90,
  "patterns_strengthened": 130,
  "torque_clusters": 1,
  "torque_outliers": 0
}
```

### Interpretation

| Metric | Value | Meaning |
|--------|-------|---------|
| Total cycles | 82 | Dream processing sessions |
| Efficiency | 54.9% | Weighted sleep quality |
| Memories consolidated | 90 | Moved to long-term storage |
| Patterns strengthened | 130 | Reinforced neural connections |

---

## Torque Clustering (V11.6)

### Physics-Inspired Memory Organization

During sleep cycles, NEUTRO uses **gravitational clustering** inspired by galaxy mergers:

```
Algorithm: Torque Clustering
Accuracy:  97.7% (UTS research, January 2025)
Trigger:   Every 5th medium cycle in BACKGROUND mode
```

### How It Works

```
1. Calculate "mass" (density) of memory regions
2. Find cluster centers via gravitational attraction
3. Assign memories to clusters
4. Flag outliers (memories far from centers)
5. REM mode explores outliers for novel associations
```

### Why Physics?

Galaxy mergers naturally produce stable structures from chaos. Same principle applied to memory consolidation—let similar memories gravitate together while identifying unique outliers for creative exploration.

---

## Dream/Reality Distinction (V11.4)

### The Problem

Without source tracking, AI systems confuse:
- What users actually said
- What the system generated during dreams
- Verified facts vs. hypotheses

### The Solution

Every memory includes source attribution:

| Source | Meaning | Verified | Confidence |
|--------|---------|----------|------------|
| `conversation` | From user interaction | true | 0.9 |
| `dream` | Generated during sleep | false | 0.3 |
| `correction` | User corrected belief | true | 0.95 |
| `fact` | Promoted from dream | true | 0.95 |

### Response Framing

NEUTRO adjusts language based on memory source:

- **Verified:** "You mentioned..."
- **Dream:** "I was thinking about..."
- **Uncertain:** "I'm not sure if we discussed..."

---

## Autonomous Curiosity

### Featured: Overnight Session (15+ hours)

NEUTRO was left running overnight with no user interaction:

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

---

## Thought Loop Recovery (V11.5)

### Deduplication System

Prevents repetitive thinking during dream cycles:

```
Mechanism:    Jaccard similarity on word sets
Comparison:   Each new thought vs last 5 session thoughts
Threshold:    >60% similar → skip, try different prompt
Result:       More diverse exploration, no mental loops
```

### Example

```
Old thought: "String theory connects quantum mechanics..."
New thought: "String theory links quantum physics..."
Similarity:  ~70% → SKIPPED
Action:      Generate different thought next cycle
```

---

## API Access

### Check Sleep Quality

```bash
curl -s http://127.0.0.1:5555/introspect | jq '.sleep_quality'
```

### Check Daemon State

```bash
curl -s http://127.0.0.1:5555/status | jq '{state: .state, idle: .idle_seconds}'
```

### Monitor Dreams

```bash
tail -f ~/my-ai-bot/neutro/data/daemon/daemon.log | grep -i dream
```

---

## Module Files

| Module | Purpose |
|--------|---------|
| `modules/daemon/continuous_processor.py` | Main dream orchestrator |
| `modules/daemon/advanced_dreams.py` | NEXTUP implementation |
| `modules/daemon/dream_trainer.py` | QLoRA integration during dreams |
| `modules/daemon/state_machine.py` | Processing mode transitions |
| `modules/TorqueClustering/` | Physics-inspired clustering |

---

## Research Foundation

### NEXTUP Theory

Stickgold, R., & Zadra, A. (2021). *When Brains Dream: Exploring the Science and Mystery of Sleep*

Key insights applied:
- Dreams serve memory consolidation
- REM explores weak associations
- Sleep enables creative problem-solving

### Torque Clustering

UTS Research (2025). Physics-inspired clustering algorithm with 97.7% accuracy.

---

*Last updated: December 31, 2025*
