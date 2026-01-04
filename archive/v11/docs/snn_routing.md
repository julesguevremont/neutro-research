# SNN Routing

## Bio-Plausible Query Routing with Spiking Neural Networks

---

## Overview

NEUTRO uses a Spiking Neural Network (SNN) to route queries to specialized language models. Instead of using a single monolithic LLM for all tasks, NEUTRO maintains multiple specialist models and dynamically selects the most appropriate one for each query.

The SNN provides bio-plausible routing that learns from experience—improving route selection over time based on interaction outcomes.

---

## Why Multi-Model?

### The Problem with Monolithic Models

Single large models must be good at everything:
- Complex reasoning
- Quick responses
- Code generation
- Mathematical computation
- Personal identity
- Memory retrieval

This leads to:
- Unnecessary compute for simple tasks
- Suboptimal performance on specialized tasks
- No ability to improve specific capabilities

### The Brain's Solution

Biological brains use specialized regions:
- Language processing in specific cortical areas
- Visual processing in occipital regions
- Mathematical reasoning in parietal areas
- Memory retrieval via hippocampus

Information is *routed* to appropriate regions based on the task.

### NEUTRO's Approach

Multiple specialized models, with an SNN that learns optimal routing:

```
Query → SNN Router → Appropriate Model → Response
```

---

## The 7 Routes

| Route | Purpose | Model | When Used |
|-------|---------|-------|-----------|
| **BRAIN_DIRECT** | Complex reasoning | dolphin-llama3:8b | Multi-step thinking, analysis |
| **IDENTITY** | Self-awareness | phi3 | "Who are you?", self-reference |
| **LOGIC** | Deduction | mistral | Reasoning, analysis |
| **MEMORY** | Retrieval | phi3 | "Remember when...", history |
| **CODE** | Programming | qwen-neutro (custom) | Coding, syntax |
| **MATH** | Computation | mistral | Calculations, numbers |
| **MOUTH** | Quick responses | phi3 | Greetings, acknowledgments |

---

## SNN Architecture

### Spiking Neural Network Basics

Unlike traditional neural networks with continuous activations, SNNs use discrete spikes:

```
Traditional NN:
Input → Weights → Activation Function → Continuous Output

Spiking NN:
Input → Spikes → Membrane Potential → Threshold → Spike/No Spike
```

SNNs are:
- More biologically plausible
- Event-driven (efficient)
- Temporal (timing matters)
- Capable of online learning

### NEUTRO's SNN Structure

```
┌─────────────────────────────────────────────────────────────┐
│                      INPUT LAYER                            │
│                                                             │
│   Query text → Embedding → Input neurons                    │
│   Each dimension of embedding activates input neurons       │
│                                                             │
└─────────────────────────────┬───────────────────────────────┘
                              │ weighted connections
                              │ (plastic, learning)
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     HIDDEN LAYER                            │
│                                                             │
│   ~500 Leaky Integrate-and-Fire (LIF) neurons              │
│   Spike-Timing Dependent Plasticity (STDP)                 │
│   Pattern recognition and feature extraction               │
│                                                             │
└─────────────────────────────┬───────────────────────────────┘
                              │ spike trains
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     OUTPUT LAYER                            │
│                                                             │
│   7 neurons (one per route)                                │
│   Winner-take-all selection                                │
│   Highest activity = selected route                        │
│                                                             │
│   [BRAIN] [IDENTITY] [LOGIC] [MEMORY] [CODE] [MATH] [MOUTH]│
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Neuron Model

Leaky Integrate-and-Fire (LIF):

```
Membrane potential V(t):
- Accumulates input spikes
- Decays over time (leak)
- Fires spike when threshold reached
- Resets after firing

Parameters:
- Threshold: Firing trigger point
- Decay: Membrane time constant
- Reset: Post-spike potential
```

---

## Learning Mechanism

### Spike-Timing Dependent Plasticity (STDP)

STDP adjusts connection weights based on spike timing:

```
Pre-synaptic spike BEFORE post-synaptic spike:
→ Strengthen connection (LTP)
→ "This input contributed to firing"

Pre-synaptic spike AFTER post-synaptic spike:
→ Weaken connection (LTD)
→ "This input didn't contribute"
```

### Feedback Learning

NEUTRO learns from interaction outcomes:

```
1. Query arrives
2. SNN routes to model (e.g., CODE route)
3. Response generated
4. Outcome observed:
   - User accepts → positive signal
   - User corrects → negative signal
   - Conversation continues → neutral/positive
5. STDP updates weights:
   - Positive: Strengthen path that led to CODE
   - Negative: Weaken path, explore alternatives
```

### Learning Over Time

```
Week 1: 67% appropriate route selection
Week 2: 78% (+11%)
Week 3: 84% (+6%)
Week 4: 89% (+5%)
```

The SNN learns patterns like:
- "How do I..." + code keywords → CODE route
- "Remember when..." → MEMORY route
- "Calculate..." → MATH route
- "Hi" / "Thanks" → MOUTH route

---

## Neuron Growth

NEUTRO's SNN grows dynamically:

```
Neurogenesis (new neurons):
- Added when existing neurons are saturated
- New patterns require new representations

Pruning (neuron death):
- Neurons with low utility removed
- Prevents unbounded growth
- Maintains efficiency

Growth Tracking:
Initial:  90 neurons
Week 1:   187 neurons (+97)
Week 2:   312 neurons (+125)
Week 3:   448 neurons (+136)
Week 4:   563 neurons (+115)
```

---

## Route Selection Process

```
1. ENCODE
   Query: "Write a function to sort a list"
   → Embedding: [0.23, -0.45, 0.12, ...]
   → Input spikes generated

2. PROPAGATE
   Spikes travel through hidden layer
   Neurons integrate inputs
   Pattern matching occurs

3. COMPETE
   Output neurons accumulate activity:
   - BRAIN:    0.12
   - IDENTITY: 0.03
   - LOGIC:    0.18
   - MEMORY:   0.05
   - CODE:     0.67  ← highest
   - MATH:     0.21
   - MOUTH:    0.01

4. SELECT
   Winner: CODE route
   Query sent to qwen-neutro model

5. LEARN
   If outcome positive: strengthen CODE path
   If outcome negative: weaken, try BRAIN next time
```

---

## Model Warming

To reduce latency, frequently-used models are pre-loaded:

```
At daemon startup:
├── dolphin-llama3:8b  [WARM]
├── mistral            [WARM]
├── phi3               [WARM]
└── qwen-neutro        [WARM on first use]

Warm models: <100ms switching
Cold models: 2-3 second load time
```

---

## Advantages of SNN Routing

### Biological Plausibility
- Mimics brain's specialized regions
- Uses realistic neuron dynamics
- Learns through biologically-inspired STDP

### Efficiency
- Simple queries → fast models
- Complex queries → powerful models
- Compute allocated appropriately

### Adaptability
- Learns from experience
- Adjusts to user patterns
- Improves over time

### Specialization
- Custom models for specific tasks
- CODE route uses trained specialist
- Each route can be independently improved

---

## Comparison to Alternatives

| Approach | Method | Limitation |
|----------|--------|------------|
| Single Large Model | One model for all | Wasteful, no specialization |
| Keyword Routing | If "code" → code model | Brittle, no learning |
| Classifier Routing | Trained classifier | Static, no online learning |
| **SNN Routing** | Bio-plausible learning | Adapts continuously |

---

## Research Questions

1. What's the optimal hidden layer size for routing efficiency?
2. Can SNN routing generalize to new task types without retraining?
3. How does routing accuracy affect downstream response quality?
4. Can routing decisions explain themselves (interpretability)?
5. What's the relationship between neuron growth and capability growth?

---

## Future Directions

- **More Routes**: Add specialists for specific domains
- **Hierarchical Routing**: Route within categories
- **Confidence Signals**: SNN outputs uncertainty, not just selection
- **Meta-Learning**: SNN learns how to learn routing

---

*Conceptual documentation. Implementation details available for research collaboration.*
