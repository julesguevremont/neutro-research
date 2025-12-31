# STDP Learning System

## Spike-Timing Dependent Plasticity in NEUTRO

---

## Overview

NEUTRO implements **real STDP (Spike-Timing Dependent Plasticity)** for biologically-plausible learning. Unlike backpropagation-based neural networks, STDP learns from the relative timing of neural spikes.

```
Pre-synaptic spike BEFORE post-synaptic → Strengthen connection (LTP)
Post-synaptic spike BEFORE pre-synaptic → Weaken connection (LTD)
```

---

## Architecture

### Core Implementation (`modules/soul_snn.py`)

```python
class STDPLearning:
    """
    Spike-Timing Dependent Plasticity

    If pre-synaptic spike arrives BEFORE post-synaptic spike → strengthen (LTP)
    If pre-synaptic spike arrives AFTER post-synaptic spike → weaken (LTD)
    """

    def __init__(self):
        self.a_plus = 0.01    # LTP rate
        self.a_minus = 0.012  # LTD rate (slightly stronger for stability)
        self.tau_plus = 20.0  # Pre-synaptic trace decay (ms)
        self.tau_minus = 20.0 # Post-synaptic trace decay (ms)
```

### Learning Rules

| Event | Direction | Effect |
|-------|-----------|--------|
| Query routed successfully | LTP (strengthen) | Route weight increases |
| User accepts response | LTP (strengthen) | Connection reinforced |
| User corrects response | LTD (weaken) | Route weight decreases |
| Prediction error high | LTD (weaken) | Wrong pattern suppressed |

---

## Integration with SNN Router

### Route Neurons

The SNN has 7 output route neurons that compete via lateral inhibition:

| Route | Purpose | Model |
|-------|---------|-------|
| BRAIN_DIRECT | Complex reasoning | dolphin-llama3:8b |
| IDENTITY | Self-awareness | phi3 (QLoRA) |
| LOGIC | Deduction, analysis | mistral:7b |
| MEMORY | Knowledge retrieval | phi3 |
| CODE | Programming | qwen-coder |
| MATH | Calculations | qwen2.5:7b |
| MOUTH | Quick responses | phi3:mini |

### Lateral Inhibition (V11.43)

Winner-take-all dynamics suppress competing routes:

```python
def lateral_inhibition(self, activations):
    winner = max(activations, key=lambda x: x[1])

    for route, activation in activations.items():
        if route != winner:
            # Suppress by 50% of winner's activation
            suppressed = activation - 0.5 * winner_activation
            activations[route] = max(0, suppressed)

    return activations, winner
```

---

## How STDP Learning Works

### Step-by-Step Flow

```
1. Query arrives
   ↓
2. SNN encodes query (384-dim embedding)
   ↓
3. Route neurons activate based on weights
   ↓
4. Lateral inhibition selects winner
   ↓
5. Winner route generates response
   ↓
6. User feedback observed
   ↓
7. STDP updates weights:
   - Success → LTP (strengthen winner)
   - Correction → LTD (weaken winner)
```

### Weight Update Formula

```python
# LTP: Pre spike came before post spike
ltp = a_plus * pre_trace * post_spikes

# LTD: Post spike came before pre spike
ltd = a_minus * pre_spikes * post_trace

# Net weight change
dw = ltp - ltd
weights += learning_rate * dw
```

---

## Current Statistics

### Live Stats (from `/introspect`)

```json
{
  "snn": {
    "neurons_total": 800,
    "neurons_born": 1281,
    "neurons_died": 581,
    "connections": 5000,
    "stdp": {
      "updates": 4,
      "ltp": 3,
      "ltd": 1
    },
    "lateral_inhibition": {
      "enabled": true,
      "strength": 0.5
    }
  }
}
```

### Interpretation

| Metric | Value | Meaning |
|--------|-------|---------|
| STDP updates | 4 | Total weight modifications |
| LTP count | 3 | Successful routes strengthened |
| LTD count | 1 | Incorrect routes weakened |
| LTP/LTD ratio | 3:1 | Learning mostly from success |

---

## Neurogenesis and Pruning

### Dynamic Neural Architecture

The SNN grows and prunes neurons based on activity:

```python
class NeuronLifecycle:
    MIN_NEURONS = 100   # Protected baseline
    MAX_NEURONS = 1000  # Upper limit
    PRUNE_INACTIVE_DAYS = 30  # Days without firing → candidate
```

### Growth Triggers

- High prediction error (surprise → need new neurons)
- New category detected (novel input type)
- Repeated pattern not captured (need specialization)

### Pruning Triggers

- Inactive for 30+ days
- Redundant (always fires with another → merge)
- Over capacity (efficiency pressure)

### Current Lifecycle Stats

```json
{
  "neurons_total": 800,
  "neurons_born": 1281,
  "neurons_died": 581
}
```

Net growth: +700 neurons since initialization.

---

## Version History

| Version | Feature | Description |
|---------|---------|-------------|
| V11.32 | STDP Stats | Track LTP/LTD counts |
| V11.39 | Debug Logging | Log STDP events |
| V11.41 | STDP Fix | Real-time weight updates working |
| V11.43 | Lateral Inhibition | Winner-take-all routing |

---

## API Access

### Check STDP Stats

```bash
curl -s http://127.0.0.1:5555/introspect | jq '.snn.stdp'
```

### Monitor Learning

```bash
# Watch STDP updates in real-time
tail -f ~/my-ai-bot/neutro/data/daemon/daemon.log | grep STDP
```

---

## Connection to Other Systems

### Correction Memory

When user corrects NEUTRO:
1. LTD weakens the wrong route
2. Correction stored in `correction_memory.json`
3. Future queries get correction context injected

### QLoRA Buffer

STDP and QLoRA are complementary:
- **STDP**: Improves routing (which model to use)
- **QLoRA**: Improves responses (what model outputs)

### Dream Consolidation

During sleep cycles:
- STDP weights are consolidated
- Weak connections pruned
- Strong patterns reinforced

---

*Last updated: December 31, 2025*
