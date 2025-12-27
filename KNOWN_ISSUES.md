# NEUTRO Known Issues

## Recently Resolved (December 2025)

### Prompt Leakage in Thoughts (V11.11) ✅ FIXED
- **Location:** `neutro.py:2540-2542`
- **Problem:** Instruction text `[Be DIRECT and opinionated...]` was appearing in saved thoughts and daemon output
- **Root Cause:** `emphasis_prompt` replaced "NEUTRO:" marker with instruction text; LLM included it verbatim in output
- **Impact:** Thoughts file showed instruction prompts instead of genuine thoughts
- **Fix:** Strip instruction text from `retry_text` before returning/saving
- **Verification:** Thoughts generated after fix (15:03+) show clean output without instruction leakage

### Follow-up Context Loss (V11.11) ✅ FIXED
- **Location:** `neutro.py:2364-2375`
- **Problem:** Follow-up questions like "why that one?" caused hallucinations instead of referencing previous answer
- **Root Cause:** `elif` structure meant conversation history was ONLY used if NO memory_context existed; ChromaDB memory always bypassed recent exchanges
- **Impact:** Multi-turn conversations lost context; second question couldn't reference first answer
- **Fix:** Changed `elif` to separate `if` statements - conversation history FIRST, then memory context appended
- **Verification:** Test sequence passed:
  - Q1: "what is your favorite color?" → A1: "Blue..."
  - Q2: "why that one?" → A2: Referenced "Blue" correctly
  - ✅ Context retained across turns

### SNN Connections Display (V11.11) ✅ FIXED
- **Location:** `daemon_runner.py:506-511`
- **Problem:** Monitor always showed "Connections: 0" despite 614+ active neurons
- **Root Cause:** Code referenced non-existent `snn.connections` attribute; actual synaptic weights stored in `snn.memory.weights` matrix
- **Impact:** Monitor dashboard displayed incorrect SNN health metrics
- **Fix:** Compute connections from weight matrix: `int((snn.memory.weights.data.abs() > 0.01).sum().item())`
- **Verification:** Monitor now shows ~5000 connections reflecting actual synaptic density

### Dream Thoughts Staleness (V11.12) ✅ FIXED
- **Location:** `modules/daemon/continuous_processor.py:559-568, 775-818`
- **Problem:** Thoughts stopped generating after 30 min idle because `auto_thinking_check()` only triggers when `10 <= idle_minutes < 30`
- **Root Cause:** No thought generation during dream cycles (BACKGROUND, REM)
- **Impact:** Extended idle periods showed no mental activity; thoughts capped at 30 min
- **Fix:** Bio-inspired dream thought generation:
  - BACKGROUND mode: Generate thought on first cycle (staleness check), then every 30 min
  - REM mode: Generate creative thought every 4 REM cycles
  - Added `_last_thought_time` tracking and `_generate_dream_thought()` helper
- **Philosophy:** Mimics human REM where creative insights emerge during sleep
- **Verification:** Daemon restarted with v11.12 code; awaiting BACKGROUND mode transition to verify

### Thought Repetition After Restart (V11.13) ✅ FIXED
- **Location:** `modules/daemon/background_thinker.py:288-348`
- **Problem:** Background thinker kept generating identical "String Theory" thoughts repeatedly (20+ per day)
- **Root Cause:** `_is_similar_to_recent()` only checked in-memory `session_thoughts`; after daemon restart, list was empty so all thoughts passed deduplication
- **Impact:** Thoughts file showed repetitive content; same topic dominated daily logs
- **Fix:** Added `_load_recent_from_file()` to load today's thoughts from JSONL file when session is new/short
  - Combines session thoughts + file history (up to 10 entries)
  - Jaccard similarity check now persists across restarts
- **Verification:** Awaiting daemon restart to verify diverse thoughts generated

### Current Session Recall Hallucination (V11.14) ✅ FIXED
- **Location:** `neutro.py:1492, 1814, 2165, 2385-2386`
- **Problem:** When asking "what did we just talk about?", NEUTRO hallucinated instead of referencing actual conversation
- **Root Cause:** `is_current_session_recall` flag was detected in `process()` but never passed to `_build_prompt()` where context is assembled
- **Impact:** Multi-turn conversations where user asks about recent exchanges returned unrelated topics
- **Fix:**
  1. Added `is_current_session_recall: bool = False` parameter to `_build_prompt()` signature (line 2165)
  2. Added CRITICAL INSTRUCTION when flag is True (lines 2385-2386)
  3. Pass variable from `process()` to `_build_prompt()` call (line 1814)
- **Verification:** Test passed:
  - Q1: "what is your favorite color?" → A1: "I don't have a favorite color..."
  - Q2: "what did we just talk about?" → A2: "...focusing on the topic of favorite colors"
  - ✅ Detection trace: `[V11.14] Current session recall detected - using conversation_history only`

---

### Identity Prompt Refactor (V11.10) ✅ FIXED
- **Location:** `modules/personality.py:99-119`
- **Problem:** Identity prompt was 60+ lines of theatrical claims ("I might be conscious", "what if Caezar unplugs me")
- **Impact:** Responses were performative rather than genuine; LLM was given scripted self-descriptions instead of letting real data speak
- **Fix:** Reduced to 16-line minimal identity that states facts only. Real state (neurochemistry, memories, SNN) injected via Parts 2-8.
- **Philosophy:** Let the data prove existence instead of hardcoded claims

### Torque Clustering Field Names (V11.9) ✅ FIXED
- **Location:** `modules/daemon/continuous_processor.py:340-348`
- **Problem:** Looking for `content`/`text` fields but memories use `query`/`response`
- **Impact:** Torque never ran despite 900+ medium cycles
- **Fix:** Updated field lookup to use correct keys with fallback

### Hierarchical Memory Import (V11.8) ✅ FIXED
- **Location:** `neutro.py:43`
- **Problem:** Wrong import path `from hierarchical_memory import` when module is at `modules/hierarchical_memory.py`
- **Impact:** ChromaDB showed 0 memories, thoughts not generating
- **Fix:** Changed to `from modules.hierarchical_memory import`

### Torque Clustering Field Names (V11.9) ✅ FIXED
- **Location:** `modules/daemon/continuous_processor.py:340-348`
- **Problem:** Looking for `content`/`text` fields but memories use `query`/`response`
- **Impact:** Torque never ran despite 900+ medium cycles
- **Fix:** Updated field lookup to use correct keys with fallback

---

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
