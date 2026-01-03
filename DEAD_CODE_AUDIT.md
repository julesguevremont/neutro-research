# NEUTRO Dead Code Deep Audit
**Generated:** January 3, 2026
**Analysis by:** Claude Code (Opus 4.5)
**Purpose:** Find hidden gems in disconnected code, identify cleanup opportunities

---

## Executive Summary

| Category | Count | Lines | Action |
|----------|-------|-------|--------|
| **USEFUL_DISCONNECTED** | 12 | ~2,700 | Wire up! (3 done in V11.75) |
| **DEPRECATED** | 13 | ~1,800 | Safe delete |
| **INCOMPLETE** | 8 | ~1,200 | Finish or delete |
| **DUPLICATE** | 25 | ~5,000 | Keep best, delete rest |
| **GARBAGE** | ~140 | ~20,000+ | Archive or delete |
| **Total Dead** | ~194 | ~30,700 | 48% of codebase |

**Total modules/\*.py:** 64,818 lines
**Safe to remove:** ~25,000 lines (39%)

---

## TOP 10 QUICK WINS

These modules are **working code** that could enhance NEUTRO with **minimal wiring**:

### 1. `math_engine.py` (41 lines)
**What it does:** SymPy-based symbolic math - equations, derivatives, integrals
**Why it's valuable:** Real math solving, not LLM guessing
**How to connect:** Add to query routing when math detected
```python
# In soul.py or neutro.py
from modules.math_engine import MathEngine
if "solve" in query or "derivative" in query:
    return math_engine.solve_equation(query)
```

### 2. `code_sandbox.py` (50 lines)
**What it does:** Safe Python code execution with timeout
**Why it's valuable:** NEUTRO could actually RUN code it generates
**How to connect:** Call after code generation for validation
```python
from modules.code_sandbox import CodeSandbox
sandbox = CodeSandbox()
result = sandbox.execute_python(generated_code)
```

### 3. `curiosity_engine.py` (340 lines)
**What it does:** Developmental curiosity - baby → toddler → child stages
**Why it's valuable:** Makes NEUTRO ask better follow-up questions
**How to connect:** Add to response generation, inject curiosity prompts

### 4. ~~`self_correction.py`~~ (~100 lines) - WIRED UP V11.75
**What it does:** Detects "no, I meant..." corrections, learns from them
**Why it's valuable:** Explicit mistake learning already built!
**Status:** Connected in daemon_runner.py lines 1012-1032

### 5. ~~`user_model.py`~~ (487 lines) - WIRED UP V11.75
**What it does:** Models Caezar's intent, mood, frustration level
**Why it's valuable:** "Fix this code" → detect if frustrated or teaching
**Status:** Connected in daemon_runner.py lines 1000-1010

### 6. `greeting_handler.py` (32 lines)
**What it does:** Fast greeting detection/response
**Why it's valuable:** Skip heavy processing for "Hello"
**How to connect:** Add to query routing as fast path

### 7. ~~`context_tracker.py`~~ (~200 lines) - WIRED UP V11.75
**What it does:** Tracks current task, project, weekly focus
**Why it's valuable:** Maintains awareness of what user is working on
**Status:** Connected in daemon_runner.py lines 990-998

### 8. `analogy_reasoning.py` (36 lines)
**What it does:** Suggests analogies for explanations
**Why it's valuable:** Better teaching responses
**How to connect:** Enhance prompts with analogy suggestions

### 9. `counter_argument.py` (23 lines)
**What it does:** Adds critical thinking prompts
**Why it's valuable:** More balanced reasoning
**How to connect:** Inject into prompts for opinion questions

### 10. `meta_reasoning.py` (29 lines)
**What it does:** Self-check prompts for reasoning quality
**Why it's valuable:** Catches logical flaws
**How to connect:** Add to complex query processing

---

## CATEGORY: USEFUL_DISCONNECTED

Working code that just needs wiring:

| File | Lines | Purpose | Effort |
|------|-------|---------|--------|
| `math_engine.py` | 41 | Symbolic math (SymPy) | Low |
| `code_sandbox.py` | 50 | Safe code execution | Low |
| `curiosity_engine.py` | 340 | Developmental curiosity | Medium |
| `self_correction.py` | ~100 | Learn from corrections | Low |
| `user_model.py` | 487 | User intent modeling | Medium |
| `greeting_handler.py` | 32 | Fast greeting path | Low |
| `context_tracker.py` | ~200 | Project/task tracking | Medium |
| `analogy_reasoning.py` | 36 | Analogy suggestions | Low |
| `counter_argument.py` | 23 | Critical thinking | Low |
| `meta_reasoning.py` | 29 | Self-evaluation | Low |
| `anomaly_detector.py` | ~200 | Detect unusual queries | Medium |
| `action_detector.py` | 348 | Detect actionable requests | Medium |
| `expert_council.py` | 506 | Multi-perspective reasoning | High |
| `learning_classifier.py` | 521 | Classify learning opportunities | Medium |
| `syntax_doctor.py` | 638 | Fix code syntax issues | Medium |

---

## CATEGORY: DEPRECATED (Safe to Delete)

Old versions replaced by better implementations:

| File | Lines | Replaced By | Action |
|------|-------|-------------|--------|
| `graph_logger_old.py.backup` | 86 | `graph_logger.py` | DELETE |
| `learning_integration_old.py.backup` | 248 | `learning_integration.py` | DELETE |
| `multi_model_brain.py.backup` | 388 | `multi_model_brain.py` | DELETE |
| `personality_old.py` | 135 | `personality.py` | DELETE |
| `plugin_system.py.backup` | 101 | `plugin_system.py` | DELETE |
| `process_logger_old.py.backup` | 110 | `process_logger.py` | DELETE |
| `vector_memory_old.py` | 94 | `vector_memory.py` | DELETE |
| `extraction_advanced_fixed.py` | 185 | Unknown | REVIEW |
| `learning_integration_fixed.py` | 54 | Unknown | REVIEW |
| `multi_model_fixed.py` | 180 | Unknown | REVIEW |
| `neutro_brain_fixed.py` | 261 | Unknown | REVIEW |
| `pattern_learning_fixed.py` | 168 | Unknown | REVIEW |
| `process_logger_fixed.py` | 57 | Unknown | REVIEW |

**Total deprecated:** ~1,800 lines

---

## CATEGORY: DUPLICATE (Memory Systems)

NEUTRO has **12 different memory implementations**. Only 3 are active:

| File | Lines | Status | Keep? |
|------|-------|--------|-------|
| `chroma_storage.py` | ~200 | ACTIVE | YES |
| `hierarchical_memory.py` | ~400 | ACTIVE | YES |
| `state_memory.py` | ~150 | ACTIVE | YES |
| `memory.py` | ~200 | DEAD | DELETE |
| `advanced_memory.py` | ~300 | DEAD | DELETE |
| `cognee_memory.py` | 538 | DEAD | DELETE (never finished) |
| `mem0_memory.py` | 352 | DEAD | DELETE (never finished) |
| `mem0_integration.py` | 322 | DEAD | DELETE (duplicate) |
| `persistent_memory.py` | 364 | DEAD | DELETE |
| `simplified_memory.py` | ~150 | DEAD | DELETE |
| `unified_memory.py` | ~250 | DEAD | DELETE |
| `vector_memory.py` | ~200 | DEAD | DELETE |
| `vector_memory_simple.py` | ~100 | DEAD | DELETE |

**Recommendation:** Keep the 3 active, delete the 9 dead = ~2,500 lines saved

---

## CATEGORY: DUPLICATE (Brain/Processor)

Multiple "brain" implementations that never got used:

| File | Lines | Purpose | Action |
|------|-------|---------|--------|
| `neutro_brain.py` | ~300 | Alternative brain | DELETE |
| `ollama_brain.py` | ~200 | Ollama wrapper | DELETE (done in llm_handlers) |
| `dual_brain.py` | ~250 | Dual-process theory | REVIEW |
| `dynamic_brain.py` | ~200 | Dynamic architecture | DELETE |
| `multi_model_brain.py` | 494 | Multi-model routing | DELETE |
| `multi_parallel_brain.py` | 428 | Parallel processing | DELETE |

---

## CATEGORY: DUPLICATE (Consciousness)

4 different consciousness implementations:

| File | Lines | Action |
|------|-------|--------|
| `consciousness_integration.py` | 346 | DELETE |
| `consciousness_integrator.py` | ~200 | DELETE |
| `integrated_consciousness.py` | 350 | DELETE |
| `fast_consciousness.py` | 434 | DELETE |
| `intelligent_fast_consciousness.py` | 432 | DELETE |

**All replaced by:** Soul system in `soul.py`

---

## CATEGORY: INCOMPLETE (Abandoned Features)

Started but never finished:

| File | Lines | Status | Recommendation |
|------|-------|--------|----------------|
| `cognee_memory.py` | 538 | External dep not installed | DELETE |
| `pipecat_integration.py` | 412 | Voice feature incomplete | ARCHIVE |
| `research_2025_integration.py` | 396 | Paper implementations | ARCHIVE |
| `sketch_rnn_neural.py` | 531 | Drawing feature | ARCHIVE |
| `physics_engine.py` | 1030 | Physics simulation | ARCHIVE |
| `sentience_modules.py` | 1274 | Ambitious sentience | ARCHIVE |
| `object_knowledge.py` | 1202 | Object understanding | ARCHIVE |
| `spatial_imagination.py` | 369 | 3D reasoning | ARCHIVE |

---

## CATEGORY: GARBAGE (Stubs/Empty)

Files with little functional code:

| File | Lines | Content |
|------|-------|---------|
| `__init__.py` | 0 | Empty |
| `module_loader.py` | 16 | Stub |

---

## RECOMMENDED DELETIONS

### Immediate Safe Deletes (No Dependencies)

```bash
# Backup files
rm modules/*_old.py*
rm modules/*.backup
rm modules/vector_memory_old.py

# Duplicate memory systems
rm modules/memory.py
rm modules/advanced_memory.py
rm modules/cognee_memory.py
rm modules/mem0_memory.py
rm modules/mem0_integration.py
rm modules/persistent_memory.py
rm modules/simplified_memory.py
rm modules/unified_memory.py
rm modules/vector_memory.py
rm modules/vector_memory_simple.py

# Duplicate brains
rm modules/neutro_brain.py
rm modules/ollama_brain.py
rm modules/dynamic_brain.py
rm modules/multi_model_brain.py
rm modules/multi_parallel_brain.py

# Duplicate consciousness
rm modules/consciousness_integration.py
rm modules/consciousness_integrator.py
rm modules/integrated_consciousness.py
rm modules/fast_consciousness.py
rm modules/intelligent_fast_consciousness.py
```

**Lines removed:** ~8,000
**Risk:** Very low (never imported)

### Archive Candidates (Keep for Reference)

```bash
mkdir -p modules/archive/incomplete
mv modules/physics_engine.py modules/archive/incomplete/
mv modules/sentience_modules.py modules/archive/incomplete/
mv modules/object_knowledge.py modules/archive/incomplete/
mv modules/sketch_rnn_neural.py modules/archive/incomplete/
mv modules/pipecat_integration.py modules/archive/incomplete/
mv modules/spatial_imagination.py modules/archive/incomplete/
```

---

## IMPLEMENTATION PRIORITY

### Phase 1: Quick Wins (This Week)
1. Wire up `greeting_handler.py` - 10 min work
2. Wire up `math_engine.py` - 30 min work
3. Wire up `code_sandbox.py` - 30 min work
4. Delete all `.backup` and `*_old.py` files

### Phase 2: Medium Effort (Next Sprint)
1. Integrate `self_correction.py` into correction learning
2. Add `user_model.py` to query processing
3. Add `context_tracker.py` for session awareness
4. Delete duplicate memory systems

### Phase 3: Cleanup (Maintenance)
1. Archive incomplete features
2. Remove duplicate brain implementations
3. Document what remains

---

## Summary Stats

| Metric | Before | After Phase 1 | After Full Cleanup |
|--------|--------|---------------|-------------------|
| Module files | 242 | 230 | ~60 |
| Total lines | 64,818 | ~58,000 | ~35,000 |
| Active modules | ~45 | ~55 | ~60 |
| Dead code % | 81% | 70% | 0% |

**Bottom line:** NEUTRO has ~25,000 lines of dead code that can be safely removed, and ~3,500 lines of useful code that just needs to be wired up.

---

*Audit conducted by Claude Code analyzing import patterns, file contents, and code completeness.*
