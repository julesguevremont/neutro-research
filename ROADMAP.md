# NEUTRO Research Roadmap

*Last updated: December 2025*

This roadmap connects NEUTRO's architecture to current AI research and outlines development priorities based on scientific literature.

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

### Gaps to Address
- [ ] Implement spike-timing-dependent plasticity (STDP)
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

### Current Implementation (V11.8)
- Real-time response evaluation after every reply
- Loop detection via response similarity tracking
- Quality scoring based on response characteristics
- Confidence calibration from SNN + response quality

### Gaps to Address
- [ ] Metacognitive planning (what to learn next)
- [ ] Self-model updates based on corrections
- [ ] Reflection bank in ChromaDB

---

## 4. Self-Directed Learning (Planned)

### Research Foundation
| Paper | Key Insight | NEUTRO Application |
|-------|-------------|-------------------|
| "Intrinsically motivated learning" (Oudeyer 2007) | Curiosity drives efficient exploration | Autonomous thought generation |
| "Autotelic agents" (Colas 2022) | Self-generated goals improve learning | Dream-time goal setting |
| "Learning progress hypothesis" (Schmidhuber 2010) | Seek intermediate difficulty | Filter boring/impossible thoughts |

### Planned Implementation
- Track "interestingness" of topics during dreams
- Generate exploration goals based on knowledge gaps
- Balance novelty-seeking with consolidation

### Prerequisites
- [ ] Knowledge gap detection
- [ ] Topic difficulty estimation
- [ ] Goal persistence across sessions

---

## 5. Global Workspace Theory (Planned)

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
| STDP in SNN | Strong | High | Medium | P2 |
| Self-directed learning | Medium | High | High | P2 |
| Global workspace | Strong | Very High | High | P3 |

---

## Milestones

### v12.0 (Target)
- [ ] Metacognitive planning integrated
- [ ] Reflection bank in ChromaDB
- [ ] Sleep cycle metrics dashboard

### v13.0 (Target)
- [ ] Self-directed learning basics
- [ ] STDP implementation
- [ ] Knowledge gap detection

### v14.0 (Target)
- [ ] Global workspace architecture
- [ ] Full self-model updates
- [ ] Autotelic goal generation

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
