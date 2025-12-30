# NEUTRO Research Roadmap

*Last updated: December 29, 2025*

This roadmap connects NEUTRO's architecture to current AI research and outlines development priorities based on scientific literature.

---

## Recent Achievements (V11.31 - V11.41)

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

### Gaps to Address
- [ ] Add lateral inhibition for winner-take-all dynamics
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

### Gaps to Address
- [ ] Metacognitive planning (what to learn next)
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

### Gaps to Address
- [ ] Topic difficulty estimation
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
- [ ] LTD (Long-Term Depression) for corrections
- [ ] Multi-day continuous operation validation

### v13.0 (Target)
- [ ] Self-directed learning with goal persistence
- [ ] Lateral inhibition in SNN
- [ ] Topic difficulty estimation

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

## References

1. Tadros et al. (2022). "Sleep-like unsupervised replay reduces catastrophic forgetting in artificial neural networks"
2. Diekelmann & Born (2010). "The memory function of sleep"
3. Tononi & Cirelli (2014). "Sleep and the price of plasticity"
4. Zhu et al. (2023). "Spiking neural networks for natural language processing"
5. Oudeyer et al. (2007). "Intrinsic motivation systems for autonomous mental development"
6. Baars (1988). "A Cognitive Theory of Consciousness"

---

*This roadmap is updated as new research emerges and implementation progresses.*
