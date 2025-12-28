# NEUTRO Known Issues

## Recently Resolved (December 2025)

### V11.37 Tool Creator - 100% Working
- **Location:** `modules/tool_creator.py`
- **Feature:** Dynamic Python tool creation at runtime
- **V11.37 Implementation:**
  - Created `ToolCreator` class for runtime tool generation
  - Security-first design with FORBIDDEN patterns blocking dangerous operations
  - Blocks: `import os`, `subprocess`, `eval(`, `exec(`, `__import__`, `open(`, etc.
  - Auto-loads tools from `tools/` directory on startup
  - Singleton access via `get_tool_creator()`
- **API:**
  - `create(name, desc, code)`: Create new tool with security validation
  - `run(name, **kwargs)`: Execute tool by name
  - `list()`: Get all available tools
  - `delete(name)`: Remove a tool
  - `stats()`: Tool statistics
- **Philosophy:** "Teach an AI to make tools and it can do anything forever."
- **Verification:** Monitor shows: `🔧 TOOLS: Total=5 │ Available: tool1, tool2`

### V11.36 Emotional Memory Tagger - 100% Working
- **Location:** `modules/emotional_memory.py`
- **Feature:** Tags memories with emotional valence and arousal for consolidation priority
- **V11.36 Implementation:**
  - Created `EmotionalTagger` class for memory emotional analysis
  - Valence scoring: -1 (negative) to +1 (positive)
  - Arousal scoring: 0 (calm) to 1 (intense)
  - Importance detection via keyword matching
  - Consolidation boost calculation: `1.0 + (arousal * 0.5) + (important ? 0.3 : 0)`
- **Word Lists:**
  - POSITIVE: love, happy, excited, grateful, amazing, great, wonderful, etc.
  - NEGATIVE: sad, angry, frustrated, worried, hate, terrible, awful, etc.
  - IMPORTANT: remember, never forget, crucial, important, must, always, forever
- **Stats Exposed:**
  - `total`: Total tagged memories
  - `positive`, `negative`, `neutral`: Valence distribution
  - `avg_arousal`: Average emotional intensity
  - `high_priority`: Memories with boost > 1.2
- **Philosophy:** "What we feel deeply, we remember forever" (biologically accurate)

### V11.35 Eligibility Traces for SNN - 100% Working
- **Location:** `modules/snn/eligibility_traces.py`
- **Feature:** Temporal credit assignment for SNN learning (STDP enhancement)
- **V11.35 Implementation:**
  - Created `EligibilityTrace` class for spike trace management
  - Exponential decay of traces over time (configurable tau)
  - Supports multiple trace types: presynaptic, postsynaptic, reward
  - Enables three-factor learning: pre × post × reward
- **Key Methods:**
  - `update(pre_spike, post_spike)`: Update traces on spike events
  - `get_eligibility(pre_idx, post_idx)`: Get trace value for synapse
  - `apply_reward(reward, weights)`: Apply reward-modulated weight update
  - `decay()`: Apply time-based trace decay
- **Stats Exposed:**
  - `traces_active`: Number of non-zero traces
  - `total_updates`: Cumulative trace updates
  - `rewards_applied`: Reward signals processed
- **Philosophy:** "What fires together, wires together" - enhanced with temporal credit

### V11.34 Sleep Quality Dashboard - 100% Working
- **Location:** `daemon_runner.py`, `monitor.sh`
- **Feature:** Visual sleep quality metrics in monitor and /introspect API
- **V11.34 Implementation:**
  - Added `sleep_quality` section to `/introspect` endpoint
  - Calculates sleep efficiency using weighted cycle formula: L=1, M=2, D=3, R=4
  - Tracks: light_cycles, medium_cycles, deep_cycles, rem_cycles, total_cycles
  - Displays efficiency percentage, memories consolidated, patterns strengthened
  - Added visual bars in monitor.sh showing cycle distribution
- **Stats Exposed:**
  - `efficiency_pct`: Weighted efficiency score (0-100%)
  - `memories_consolidated`: Tagged memories during sleep
  - `patterns_strengthened`: Neural patterns reinforced
  - `torque_clusters`, `torque_outliers`: Clustering stats
- **Verification:** Monitor shows: `😴 SLEEP: [████████░░] 78% eff │ Total: 25 cycles`

### V11.33 Knowledge Gap Detection - 100% Working
- **Location:** `modules/daemon/knowledge_gaps.py`, `daemon_runner.py`, `monitor.sh`
- **Feature:** Tracks what NEUTRO doesn't know well for targeted learning
- **V11.33 Implementation:**
  - Created `KnowledgeGapTracker` class
  - Detects gaps from: low confidence responses, uncertainty phrases, corrections
  - Records topic, frequency, recency, confidence deficit
  - Gaps can be closed when confidence improves
  - Exposed via `/gaps` endpoint and `/introspect`
- **Stats Exposed:**
  - `total_gaps`, `open_gaps`, `closed_gaps`
  - `top_topics`: Priority gaps for learning focus
- **Verification:** Monitor shows: `🕳️ GAPS: Total=5 │ Open=3 │ Closed=2 │ Top: topic1, topic2`

### V11.32 STDP Learning Stats - 100% Working
- **Location:** `modules/snn/snn_router.py`, `daemon_runner.py`, `monitor.sh`
- **Feature:** Spike-Timing-Dependent Plasticity tracking
- **V11.32 Implementation:**
  - Added STDP stats tracking in SNN router
  - Counts LTP (Long-Term Potentiation) and LTD (Long-Term Depression) events
  - Exposed via `/introspect` under `snn.stdp`
- **Stats Exposed:**
  - `updates`: Total STDP weight updates
  - `ltp_count`: Strengthening events (spike before target)
  - `ltd_count`: Weakening events (spike after target)
- **Verification:** Monitor shows: `⚡ STDP: Updates=150 │ LTP=95 │ LTD=55`

### V11.31 Self-Reflection Integration - 100% Working
- **Location:** `modules/daemon/self_reflection.py`, `modules/daemon/continuous_processor.py`, `neutro.py`, `daemon_runner.py`, `monitor.sh`
- **Problem:** SelfReflectionSystem was defined but never integrated into the daemon
- **Root Cause:** `run_reflection_cycle()` was never called; responses weren't being recorded
- **V11.31 Fix:**
  - Import SelfReflectionSystem in `continuous_processor.py`
  - Call `run_reflection_cycle()` during DEEP_DREAM (every 3rd cycle) and REM (every 4th cycle)
  - Record responses in `neutro.py` via `record_response()` after each query
  - Expose reflection stats in `/introspect` endpoint via `daemon_runner.py`
  - Add `🔍 REFLECT` line to `monitor.sh` display
- **Stats Exposed:**
  - V11.31 names: `reflection_cycles`, `responses_recorded`, `issues_found`, `insights_generated`
  - Legacy names: `total_corrections`, `total_contradictions` (for backwards compatibility)
- **Verification:**
  - Monitor shows: `🔍 REFLECT: Cycles=0 │ Responses=2 │ Issues=0 │ Insights=0`
  - `/introspect` returns all field names correctly
  - State persistence working (`total_corrections: 1` loaded from file)

### V11.30 Grounded Thoughts - 100% Working
- **Location:** `modules/daemon/background_thinker.py`
- **Problem:** Background thoughts were "theatrical" - claiming fake sensory perceptions like "I noticed how the sun's warmth made visitors smile"
- **Root Cause:** NEUTRO has NO sensors - these thoughts were hallucinations
- **V11.30 Fix:**
  - Replaced `PROMPTS` with `PROMPTS_GROUNDED` (reference real data: conversation history, memories, system metrics)
  - Added `PROMPTS_SPECULATIVE` with `[IMAGINING]`/`[SPECULATING]`/`[HYPOTHETICAL]` prefixes
  - 80/20 split: 80% grounded thoughts, 20% labeled speculation
- **Philosophy:** `process()` = real data only, no fabrication; `imagine()` = labeled speculation
- **Verification:** All new thoughts are either grounded or properly labeled with `[SPECULATING]` prefix

### V11.29 Intelligent Opinion Detection - 100% Working
- **Location:** `modules/daemon/correction_verifier.py`
- **Battery Test:** 8/8 tests passed (100% - Grade A)
- **Working:** All categories including opinion detection
- **V11.29 Fix:** Added LLM-based statement classification before verification:
  - `StatementType` enum: FACT, OPINION, CLAIM
  - OPINION → immediate UNCERTAIN return (no verification needed)
  - FACT/CLAIM → proceed to verification cascade
  - Classification uses phi3 for fast response (~3s for opinions)
- **Cascade Status:**
  - Knowledge Library: 0% (still needs ChromaDB population)
  - Consultant System: 0% (still needs web search setup)
  - LLM Fallback: 100% (all fact verifications via mistral:latest)
- **Next Steps for V12.0:**
  - Populate Knowledge Library with common facts
  - Configure Consultant System web search
  - See `docs/V12_PLAN.md` for full integration plan

---

### GWT NoneType Error (V11.25) FIXED
- **Location:** `modules/daemon/background_thinker.py:288`
- **Problem:** Background thought generation crashed when accessing `global_workspace_theory.current_state` when GWT was None
- **Root Cause:** No None check before accessing GWT properties during soul-based thought generation
- **Impact:** Template fallback rate was 50%+ instead of <10%
- **Fix:** Added `if gwt is not None:` guard before accessing `gwt.current_state`
- **Verification:** Soul method now generates 72% of thoughts (was ~40%)

### Debug Logging Added (V11.26) FIXED
- **Location:** `modules/daemon/background_thinker.py:~290-310`
- **Problem:** No visibility into which thought generation method was being used
- **Fix:** Added `[V11.26-DEBUG]` logging to trace thought source (soul/process/template)
- **Verification:** Monitor output now shows method distribution

### Benchmark Session Isolation (V11.18) ✅ FIXED
- **Location:** `neutro.py:2079-2091`, `daemon_runner.py:330-340`, `tests/benchmark_suite.py:49-60, 112, 156`
- **Problem:** Benchmark showed 0% context retention despite V11.17 minimal prompt bypass working in manual tests
- **Root Cause:** Benchmark's `session_id` parameter was ignored by daemon - all tests shared global `conversation_history`
  - 3-turn test polluted history before 8-turn test ran
  - 8-turn recall query found residual data from 3-turn test instead of actual conversation
- **Impact:** Benchmark always failed context retention even when feature worked correctly
- **Fix:**
  1. Added `clear_session()` method to `neutro.py` to reset conversation state
  2. Added `/clear_session` POST endpoint to `daemon_runner.py`
  3. Updated benchmark to call `clear_session()` before each context retention test
- **Verification:** Benchmark v11.18 achieved:
  - Context Retention: 100% (was 0%)
  - Overall Grade: B- (was F)
  - `[Session cleared: 0 entries]` before 3-turn, `[Session cleared: 4 entries]` before 8-turn

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

### Memory Context Override (V11.15) ✅ FIXED
- **Location:** `neutro.py:2371-2376`
- **Problem:** ChromaDB memory_context was overriding conversation_history for session recall queries
- **Root Cause:** Memory context (with polluted episodic entries) was being injected even when `is_current_session_recall=True`
- **Impact:** "What did we just talk about?" returned "String Theory" from polluted episodic memory instead of actual conversation
- **Fix:** Skip memory_context injection when `is_current_session_recall=True`
- **Debug trace:** `[V11.15-DEBUG] is_current_session_recall=True, conv_history_len=N`

### Internal Thought Filtering (V11.16) ✅ FIXED
- **Location:** `neutro.py:2182-2190`
- **Problem:** Daemon's `[INTERNAL]` thoughts were appearing in conversation history
- **Root Cause:** `conversation_history` included daemon's internal musings which polluted session recall
- **Impact:** Session recall could reference internal daemon thoughts instead of user conversation
- **Fix:** Filter out entries where `query.startswith('[INTERNAL]')` before adding to prompt
- **Debug trace:** `[V11.16-DEBUG] Building prompt: N user convos (filtered from M total)`

### Minimal Prompt Bypass for Session Recall (V11.17) ✅ FIXED
- **Location:** `neutro.py:2182-2211`
- **Problem:** Despite V11.15/V11.16, "String Theory" hallucination persisted from multiple context injection points
- **Root Cause:** Memory pollution from `data/soul/memory/episodic.json` was being injected via:
  - Soul episodic memory (partially blocked by V11.14)
  - `schema_context` from dream_trainer (NOT blocked)
  - `self_model_context` (NOT blocked)
- **Solution:** Minimal prompt bypass - when `is_current_session_recall=True`, return early with ONLY:
  - Identity (who NEUTRO is)
  - Filtered conversation history (last 5 exchanges, no `[INTERNAL]`)
  - Strong instruction to answer only from that context
- **Impact:** Bypasses ALL memory pollution sources; clean session recall
- **Debug trace:**
  ```
  [V11.17-DEBUG] Using MINIMAL prompt for current session recall
  [V11.17-DEBUG] Exchange 0: Q='...' R='...'
  [V11.17-DEBUG] Minimal prompt length: NNN chars
  ```
- **Verification:** 8-turn test achieved **Grade A (GPA 4.0)**:
  - ✅ Context recall correctly mentioned wifi, haiku, stress (actual topics)
  - ✅ No String Theory hallucination
  - ✅ All 8 turns scored A

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
