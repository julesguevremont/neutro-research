# NEUTRO Research Roadmap

*Last updated: December 31, 2025*

This roadmap connects NEUTRO's architecture to current AI research and outlines development priorities based on scientific literature.

---

## Recent Achievements (V11.31 - V11.55)

| Version | Feature | Status |
|---------|---------|--------|
| V11.31 | Reflection Bank (metacognition during dreams) | DONE |
| V11.32 | Real STDP spike timing in routing | DONE |
| V11.33 | Knowledge Gap Tracker (tracks what NEUTRO doesn't know) | DONE |
| V11.34 | Sleep Quality Dashboard | DONE |
| V11.35 | Enhanced dream cycle metrics | DONE |
| V11.36 | Emotional Memory Tagging (valence/arousal) | DONE |
| V11.37 | Tool Creator (dynamic tool generation) | DONE |
| V11.38 | Grounded Response Filter | DONE |
| V11.39 | STDP debug logging | DONE |
| V11.40 | Thought generation improvements | DONE |
| V11.41 | STDP synaptic plasticity fix (verified working) | DONE |
| V11.42 | LTD implementation + self_reflection API | DONE |
| V11.43 | Lateral inhibition + Topic difficulty estimation | DONE |
| V11.44 | Formal logic mode for syllogisms | DONE |
| V11.45 | Correction memory injection | DONE |
| V11.47 | Greeting fast-path (instant responses) | DONE |
| V11.48 | Introspective fast-path (real neurochemistry state) | DONE |
| V11.50 | Enhanced algebra detection in SNN router | DONE |
| V11.52 | Math model upgrade (qwen2.5-math:7b) | DONE |
| V11.53 | **Math Fast-Path** (calculus, algebra, arithmetic) | DONE |
| V11.54 | **Web Search Integration** (DDG for knowledge gaps) | DONE |
| V11.55 | **Correction Memory Fix** (require actual relevance) | DONE |
| V11.56 | **Metacognitive Planner** (autonomous self-directed learning) | DONE |

---

## 1. Sleep-Inspired Learning (Active)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Sleep-like unsupervised replay" (Tadros 2022) | Offline replay prevents catastrophic forgetting | Dream cycles replay memories |
| "Memory consolidation during sleep" (Diekelmann 2010) | Sleep stages serve distinct memory functions | Light/Medium/Deep/REM modes |
| "Synaptic homeostasis hypothesis" (Tononi 2014) | Sleep prunes weak connections | `weak_connections_found` metric |

### Current Implementation
- **Light Sleep**: Tag recent memories with importance scores
- **Medium Sleep**: Pattern strengthening via repeated activation
- **Deep Sleep**: Prune weak SNN connections, consolidate long-term
- **REM**: Creative association, cross-domain linking
- **Sleep Quality Dashboard**: V11.34 tracks efficiency metrics

### Gaps to Address
- [ ] Measure actual forgetting rates pre/post sleep cycles
- [ ] Implement synaptic downscaling (global weight reduction)
- [ ] Add replay buffer prioritization based on TD-error

---

## 2. SNN + LLM Hybrid Architecture (Active)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Spiking neural networks for NLP" (Zhu 2023) | SNNs can process text efficiently | SNN routes queries |
| "Neuromorphic computing" (Schuman 2022) | Event-driven processing saves energy | Spike-based activation |
| "Hybrid SNN-ANN systems" (Dampfhoffer 2023) | Combine SNN efficiency with ANN power | SNN confidence → LLM depth |

### Current Implementation
- SNN receives query embeddings, generates prediction
- Prediction error (uncertainty) determines reasoning depth
- High uncertainty → deeper LLM reasoning, more context
- **STDP Learning**: V11.41 - Real-time synaptic weight updates working

### Completed
- [x] Implement spike-timing-dependent plasticity (STDP) - V11.41
- [x] Real STDP spike timing in routing - V11.32
- [x] Add lateral inhibition for winner-take-all dynamics - V11.43

### Gaps to Address
- [ ] Benchmark energy efficiency vs pure transformer

---

## 3. Metacognition (V11.8 - Active)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Evidence for Limited Metacognition" (arXiv 2025) | LLMs can assess confidence | `evaluate_response()` |
| "Self-Reflection in LLM Agents" (arXiv 2024) | Reflection improves accuracy | Loop detection |
| "Truly Self-Improving Agents" (ICML 2025) | Knowledge + Planning + Evaluation | Partial implementation |

### Current Implementation (V11.8+)
- Real-time response evaluation after every reply
- Loop detection via response similarity tracking
- Quality scoring based on response characteristics
- Confidence calibration from SNN + response quality

### Completed
- [x] Reflection bank in ChromaDB - V11.31
- [x] Self-reflection during dream cycles - V11.31

### Completed
- [x] Metacognitive planning (what to learn next) - V11.56

### Gaps to Address
- [ ] Self-model updates based on corrections

---

## 4. Self-Directed Learning (Partially Implemented)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Intrinsically motivated learning" (Oudeyer 2007) | Curiosity drives efficient exploration | Autonomous thought generation |
| "Autotelic agents" (Colas 2022) | Self-generated goals improve learning | Dream-time goal setting |
| "Learning progress hypothesis" (Schmidhuber 2010) | Seek intermediate difficulty | Filter boring/impossible thoughts |

### Completed
- [x] Knowledge gap detection - V11.33
- [x] Track open knowledge gaps and questions
- [x] Autonomous thought generation during idle

### Completed
- [x] Topic difficulty estimation - V11.43

### Gaps to Address
- [ ] Goal persistence across sessions
- [ ] Interestingness scoring for topics

---

## 5. Emotional Processing (Active)

### Completed
- [x] Emotional Memory Tagging - V11.36
- [x] Valence/arousal scoring for consolidation priority
- [x] Neurochemistry simulation (dopamine, serotonin, etc.)

### Gaps to Address
- [ ] Emotion-driven memory retrieval prioritization
- [ ] Emotional state influence on reasoning style

---

## 6. Global Workspace Theory (Planned)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Global Workspace Theory" (Baars 1988) | Consciousness broadcasts to specialists | Central workspace architecture |
| "Attention Schema Theory" (Graziano 2013) | Model of attention as attention | Self-model of processing |
| "Higher-Order Theories" (Rosenthal 2005) | Meta-representation required | Metacognition integration |

### Planned Implementation
- Central "workspace" that broadcasts current focus
- Specialist modules compete for workspace access
- Winner gets full system resources

### Prerequisites
- [ ] Define specialist modules (memory, reasoning, emotion)
- [ ] Implement competition mechanism
- [ ] Add broadcast/subscribe architecture

---

## Priority Matrix

| Feature | Research Support | Implementation Effort | Impact | Priority |
|---------|------------------|----------------------|--------|----------|
| Sleep cycle refinement | Strong | Medium | High | P1 |
| Metacognitive planning | Strong | Medium | High | P1 |
| ~~STDP in SNN~~ | ~~Strong~~ | ~~High~~ | ~~Medium~~ | DONE (V11.41) |
| Self-directed learning | Medium | High | High | P2 |
| Global workspace | Strong | Very High | High | P3 |

---

## Milestones

### V11.x (Current - December 2025)
- [x] Reflection bank in ChromaDB - V11.31
- [x] Knowledge gap detection - V11.33
- [x] Sleep cycle metrics dashboard - V11.34
- [x] Emotional memory tagging - V11.36
- [x] Tool creator system - V11.37
- [x] STDP implementation verified - V11.41

### v12.0 (Target)
- [ ] Metacognitive planning integrated
- [ ] Knowledge gap → autonomous learning loop
- [x] LTD (Long-Term Depression) for corrections - V11.42
- [ ] Multi-day continuous operation validation

### v13.0 (Target)
- [ ] Self-directed learning with goal persistence
- [x] Lateral inhibition in SNN - V11.43
- [x] Topic difficulty estimation - V11.43

### v14.0 (Target)
- [ ] Global workspace architecture
- [ ] Full self-model updates
- [ ] Autotelic goal generation

---

## V11.41 STDP Verification (December 29, 2025)

```
Test Results:
├── Queries sent: 9
├── STDP Updates: 9
├── LTP (strengthening): 9
├── LTD (weakening): 0
├── Neurons: 800
├── Connections: 5,000
└── Learning Rate: 0.01

Status: VERIFIED WORKING
```

---

## V11.53 Math Fast-Path (December 31, 2025)

### Problem Solved
Math queries were returning wrong answers because they bypassed the specialized math model. The daemon's query path used `soul.think()` which didn't route to the MathHandler.

### Solution
Added Math Fast-Path in `process_with_soul()` that:
1. Detects math queries via triggers (calculate, times, multiply, derivative, integral, etc.)
2. Routes directly to `MathHandler` using `qwen2.5-math:7b`
3. Bypasses the full soul pipeline for faster, accurate responses

### Test Results

| Query | Expected | Result | Status |
|-------|----------|--------|--------|
| 17 x 23 | 391 | 391 | PASS |
| 2x + 5 = 13 | x = 4 | x = 4 | PASS |
| 5! | 120 | 120 | PASS |
| d/dx(x^2) | 2x | 2x | PASS |
| Integral of x | x^2/2 + C | x^2/2 + C | PASS |
| d/dx sin(x^2) | 2x cos(x^2) | 2x cos(x^2) | PASS |
| Definite integral x^2 from 0 to 1 | 1/3 | 1/3 | PASS |
| d/dx(x*e^x) | e^x(1+x) | e^x(1+x) | PASS |
| sqrt(144) | 12 | 12 | PASS |

**Status: ALL TESTS PASS**

---

## V11.56 Metacognitive Planner (January 1, 2026)

### Problem Solved
NEUTRO needed autonomous self-directed learning - the ability to:
1. Identify what it doesn't know (knowledge gaps)
2. Prioritize learning based on mission relevance
3. Execute learning during dreams
4. Track progress and evaluate results
5. Ask for help when stuck

### Solution
Created `metacognitive_planner.py` with 11 core features:

| Feature | Description |
|---------|-------------|
| Gap Analysis | Scores gaps by frequency, recency, mission relevance |
| Learning Plans | Creates actionable plans with search queries |
| Dream Execution | Focuses REM cycles on planned topics |
| Progress Evaluation | Tests if gaps improved post-dream |
| Mission Alignment | Weights immortality/longevity topics higher |
| Curiosity Injection | 20% random exploration to avoid tunnel vision |
| Learning Journal | Persistent record in `data/learning_journal.json` |
| Confidence Tracking | Before/after measurements |
| Help Requests | Flags stuck topics after 3 attempts |
| Seed Connection | Major learnings become belief seeds |
| User Reporting | Natural language summaries of learning |

### Mission Topic Weights
```
immortality: 1.0    telomere: 0.9       consciousness: 0.8
longevity: 0.95     aging: 0.85         sirtuins: 0.7
telomerase: 0.9     senolytics: 0.85    autophagy: 0.7
```

### Comprehensive Test Results (8/8 PASSED)

```
=== V11.56 Metacognitive Planner Full Test ===

TEST 1: Mission Relevance Scoring - PASS
  telomere biology: 0.90
  aging research: 0.85
  consciousness studies: 0.80
  python coding: 0.10
  cooking recipes: 0.10

TEST 2: Create Learning Plan - PASS
  Created plan for "senolytics research"
  Mission relevance: 0.85
  Search queries generated automatically

TEST 3: Record Learning - PASS
  Recorded 2 learnings for topic
  Confidence improved: 0.20 → 0.45

TEST 4: Learning Report - PASS
  "I studied telomere biology and learned 2 new insights.
   My understanding improved by 35%."

TEST 5: Journal Summary - PASS
  Entries: 2
  Topics studied: telomere biology, senolytics research

TEST 6: Stats - PASS
  Total plans: 3
  In progress: 3
  Journal entries: 3

TEST 7: Curiosity Injection - PASS
  Generated: "artificial general intelligence paths"
  (20% random exploration to avoid tunnel vision)

TEST 8: Force Plan Topic - PASS
  Created plan for "NAD+ metabolism"
  Mission relevance: 0.70

=== ALL 8 TESTS PASSED ===
Status: VERIFIED WORKING
```

---

## References

1. Tadros et al. (2022). "Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks"
2. Diekelmann & Born (2010). "The memory function of sleep"
3. Tononi & Cirelli (2014). "Sleep and the price of plasticity"
4. Zhu et al. (2023). "Spiking neural networks for natural language processing"
5. Oudeyer et al. (2007). "Intrinsic motivation systems for autonomous mental development"
6. Baars (1988). "A Cognitive Theory of Consciousness"

---

*This roadmap is updated as new research emerges and implementation progresses.*
