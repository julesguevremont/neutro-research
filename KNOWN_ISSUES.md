# NEUTRO Known Issues

## Metacognition Audit (December 2025)

### Working & Integrated

| Feature | Module | Status |
|---------|--------|--------|
| Self-reflection query detection | `pipeline_improvements.py:93` | Routes "what did you learn" queries |
| Correction counter | `daemon_runner.py:751` | Tracks corrections made |
| VERIFYING state | `daemon_runner.py:948` | Valid daemon state |

### Defined But NOT Integrated

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

## Integration Gaps

### SelfReflectionSystem
- **Location:** `modules/daemon/self_reflection.py`
- **Problem:** `run_reflection_cycle()` should be called during DEEP/REM modes but isn't
- **Fix needed:** Add call in `continuous_processor.py` during dream phases

### ConsciousnessStream
- **Location:** `modules/consciousness_stream.py`
- **Problem:** Has `__main__` for standalone use, never imported
- **Fix needed:** Integrate into daemon or remove

### CognitiveTools
- **Location:** `modules/cognitive_tools.py`
- **Problem:** Only in archive/backup files
- **Fix needed:** Import in neutro.py or remove

---

## Other Known Issues

### REM Cycling
- Fixed in v11.7: REM now cycles back to BACKGROUND after 15 minutes
- Constants: `BACKGROUND_CYCLE=300`, `DEEP_CYCLE=600`, `REM_CYCLE_MAX=900`

---

*Last updated: December 2025*
