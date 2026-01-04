# SNN Internals

## Weight Matrix and Connection Count

### Connection Calculation

The monitor displays ~5000 connections. This is a **real count**, not a display cap.

**Calculation method** (`daemon_runner.py:508`):
```python
int((snn.memory.weights.data.abs() > 0.01).sum().item())
```

This counts all synaptic weights with absolute value > 0.01 threshold. The number grows as the SNN learns and forms new connections.

---

## Weight Update Mechanisms

The SNN weight matrix updates through 5 distinct mechanisms:

| Mechanism | Location | Trigger | Effect |
|-----------|----------|---------|--------|
| **STDP** | `MemoryNeurons.forward()` | Every forward pass | Hebbian learning |
| **Decay** | `apply_decay()` | Prediction error > 0.3 | Weakens unused connections |
| **Reinforce** | `reinforce_recent()` | Positive outcome | Strengthens active paths |
| **Weaken** | `weaken_recent()` | Negative outcome | Reduces bad routing weights |
| **Routing STDP** | `RoutingNeurons.learn_from_outcome()` | After query response | Route-specific learning |

---

### 1. STDP Learning (Spike-Timing Dependent Plasticity)

**Location:** `modules/soul_snn.py` - `STDPLearning` class

STDP implements Hebbian learning: "neurons that fire together, wire together."

**Learning Rules:**
- **LTP (Long-Term Potentiation):** Pre-spike before post-spike strengthens connection
- **LTD (Long-Term Depression):** Pre-spike after post-spike weakens connection

**Constants:**
```
a_plus  = 0.005   # LTP learning rate
a_minus = 0.006   # LTD learning rate (slightly stronger)
tau     = 20.0    # Time constant (ms)
```

**Update equation:**
```python
# Potentiation: pre before post
dW_plus = a_plus * pre * post_trace

# Depression: post before pre
dW_minus = a_minus * post * pre_trace

# Net change
weights += dW_plus - dW_minus
```

---

### 2. Natural Decay

**Location:** `modules/soul_snn.py:879-882`

Weakens all connections over time to prevent saturation.

```python
def apply_decay(self):
    with torch.no_grad():
        self.weights.data = self.weights.data * (1 - self.decay_rate)
```

**Decay rate:** `0.0001` per call

**Trigger:** Called when prediction error exceeds 0.3, indicating the network needs to "forget" some patterns.

---

### 3. Positive Reinforcement

**Location:** `modules/soul_snn.py:884-896`

Strengthens recently-active synapses when outcome is positive.

```python
def reinforce_recent(self, strength: float = 0.1):
    with torch.no_grad():
        recent = self.recent_activity
        boost = (recent > 0).float() * strength
        self.weights.data = torch.clamp(
            self.weights.data + boost.mean(dim=0),
            0.0, 1.0
        )
```

**Trigger:** User accepts response, conversation continues naturally.

---

### 4. Negative Weakening

**Location:** `modules/soul_snn.py:898-909`

Weakens recently-active synapses when outcome is negative.

```python
def weaken_recent(self, strength: float = 0.05):
    with torch.no_grad():
        recent = self.recent_activity
        reduction = (recent > 0).float() * strength
        self.weights.data = torch.clamp(
            self.weights.data - reduction.mean(dim=0),
            0.0, 1.0
        )
```

**Trigger:** User corrects response, explicit negative feedback.

---

### 5. Routing STDP

**Location:** `modules/soul_snn.py:1274-1308`

Updates routing weights based on query outcomes.

```python
def learn_from_outcome(self, route_idx: int, success: bool):
    # Get spike timing from recent activity
    pre_trace = self.pre_trace
    post_trace = self.output_trace[route_idx]

    if success:
        # Strengthen path to selected route
        delta = self.stdp_params['a_plus'] * pre_trace * post_trace
    else:
        # Weaken path
        delta = -self.stdp_params['a_minus'] * pre_trace * post_trace

    self.weights[:, route_idx] += delta
```

**Trigger:** After every query-response cycle, based on detected outcome.

---

## Neurogenesis and Pruning

The SNN dynamically adjusts its size:

**Neuron Birth:**
- Triggered when existing neurons are saturated
- New patterns require new representations
- Growth rate depends on novelty of inputs

**Neuron Death:**
- Neurons with sustained low activity are pruned
- Prevents unbounded growth
- Maintains computational efficiency

**Typical Growth:**
```
Initial:  90 neurons
Week 1:   187 neurons (+97)
Week 2:   312 neurons (+125)
Week 3:   448 neurons (+136)
Week 4:   563 neurons (+115)
```

---

## Real-Time Learning Verification

To verify weights are updating, check these indicators:

1. **Connection count changes** - Monitor shows connection count over time
2. **Routing accuracy improves** - Better model selection with experience
3. **SNN stats in `/introspect`** - Shows neurons_born, neurons_died
4. **STDP traces** - Pre/post traces indicate active learning

---

*Technical documentation. Implementation in `modules/soul_snn.py`.*
