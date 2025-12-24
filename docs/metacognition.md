# Metacognition in NEUTRO

## Current Research (2024-2025)

| Paper | Source | Key Finding |
|-------|--------|-------------|
| "Evidence for Limited Metacognition in LLMs" | arXiv Sept 2025 | Frontier LLMs can assess confidence, anticipate own answers |
| "Self-Reflection in LLM Agents" | arXiv 2024 | Self-reflection helps identify/correct mistakes |
| "Truly Self-Improving Agents" | ICML 2025 | 3 components: knowledge, planning, evaluation |
| "Dual-loop reflection" | Nature 2025 | Extrospection + introspection with reflection bank |

---

## ICML 2025 Framework vs NEUTRO

| Component | Research Definition | NEUTRO Implementation | Status |
|-----------|--------------------|-----------------------|--------|
| Metacognitive Knowledge | Self-assessment of capabilities | self_model.py | Defined, unused |
| Metacognitive Planning | Deciding what/how to learn | - | Missing |
| Metacognitive Evaluation | Reflecting on learning | metacognition.py | Defined, unused |
| Confidence calibration | Know what you know | SNN prediction error | Working |
| Error correction | Fix mistakes | /correct endpoint | Working |
| Loop detection | Notice repetition | detailed_logger | Tracks only, no protection |

---

## Audit Results (December 2025)

### Working & Integrated

| Feature | Module | Status |
|---------|--------|--------|
| Self-reflection query detection | `pipeline_improvements.py:93` | Routes "what did you learn" queries |
| Correction counter | `daemon_runner.py:751` | Tracks corrections made |
| VERIFYING state | `daemon_runner.py:948` | Valid daemon state |
| SNN uncertainty | `snn.py` | Prediction error drives reasoning depth |

### Defined But Not Called

| Feature | Module | Issue |
|---------|--------|-------|
| Metacognition class | `modules/metacognition.py` | Never instantiated in main system |
| CognitiveTools | `modules/cognitive_tools.py` | Not imported in neutro.py/daemon_runner.py |
| ConsciousnessStream | `modules/consciousness_stream.py` | Standalone script, not integrated |
| SelfReflectionSystem methods | `modules/daemon/self_reflection.py` | Only `corrections_made` used; `run_reflection_cycle()` never called |

### Missing/Minimal

| Feature | Status |
|---------|--------|
| Loop detection | Only `detailed_logger_processor` tracks repeats |
| Confidence calibration | Scattered across modules, not unified |
| Self-model updates | `get_self_insight()` exists but never called |
| Metacognitive reasoning | No "thinking about thinking" in response generation |

---

## The Gap

Research shows that metacognition in AI requires three integrated components:

1. **Knowledge** - knowing what you can/can't do
2. **Planning** - deciding what to learn next
3. **Evaluation** - reflecting on whether learning worked

NEUTRO has pieces of each but they're not connected:

```
Current state:
  metacognition.py ──── (never called)
  self_reflection.py ── (only counter used)
  consciousness_stream.py ── (standalone)

Should be:
  Dream cycle → calls run_reflection_cycle()
              → stores insights in ChromaDB
              → updates self_model
              → informs next learning
```

---

## Roadmap

### Phase 1: Connect Existing Code
1. Import metacognition.py in daemon_runner.py
2. Call `run_reflection_cycle()` during DEEP/REM modes
3. Store reflection results in ChromaDB

### Phase 2: Add Reflection Bank
1. Create `reflection_memories` collection in ChromaDB
2. Store insights with timestamps and confidence
3. Retrieve relevant reflections during response generation

### Phase 3: Loop Protection
1. Track recent thought topics in working memory
2. Block repeated thoughts (>3 similar in 24h)
3. Force topic diversity during autonomous exploration

### Phase 4: Self-Model Updates
1. Call `get_self_insight()` during REM cycles
2. Update capability assessments based on corrections
3. Adjust confidence calibration from actual accuracy

---

## References

- [Evidence for Limited Metacognition in LLMs](https://arxiv.org/abs/2509.21545) (2025)
- [Self-Reflection in LLM Agents](https://arxiv.org/abs/2405.06682) (2024)
- [Truly Self-Improving Agents](https://openreview.net/forum?id=4KhDd0Ozqe) (ICML 2025)

---

*Audit conducted December 2025. See [KNOWN_ISSUES.md](../KNOWN_ISSUES.md) for integration gaps.*
