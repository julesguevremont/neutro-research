# NEUTRO Benchmark Changelog

## [v11.30] - 2025-12-28

### Fixed
- **Theatrical Thought Generation** - Removed fake sensory perceptions from background thoughts
- NEUTRO has NO sensors - thoughts claiming "I noticed how the sun's warmth made visitors smile" are hallucinations
- All thoughts now grounded in real data OR clearly labeled as speculation

### Changed
- `modules/daemon/background_thinker.py`:
  - Replaced `PROMPTS` with `PROMPTS_GROUNDED` (reference real data: conversation history, memories, system metrics)
  - Added `PROMPTS_SPECULATIVE` with `[IMAGINING]`/`[SPECULATING]`/`[HYPOTHETICAL]` prefixes
  - Updated template thoughts: grounded templates reference actual system state
  - Updated `_build_internal_query()` to enforce grounding instructions
  - 80/20 split: 80% grounded thoughts, 20% labeled speculation

### Philosophy
- `process()` = real data only, no fabrication
- `imagine()` = labeled speculation, honest about limitations
- If no real data available, say "I don't have data on this" not "I noticed..."

### Files Changed
- `modules/daemon/background_thinker.py` - Grounding enforcement

---

## [v11.29] - 2025-12-28

### Added
- **Intelligent Opinion Detection** - LLM-based statement classification before verification:
  1. Classification Step (phi3 fast) - categorizes as FACT, OPINION, or CLAIM
  2. OPINION → immediate UNCERTAIN return (no verification needed)
  3. FACT/CLAIM → proceed to verification cascade
- `StatementType` enum: FACT, OPINION, CLAIM
- `_classify_statement()` method with 10s timeout
- `_query_llm_fast()` helper for fast LLM queries
- Classification stats tracking: `classified_as_fact`, `classified_as_opinion`, `classified_as_claim`

### Battery Test Results
```
Total Tests:  8
Passed:       8 (100%)
Failed:       0

BY CATEGORY:
  biology        : 1/1 (100%)
  chemistry      : 1/1 (100%)
  math           : 2/2 (100%)
  geography      : 1/1 (100%)
  science        : 1/1 (100%)
  opinion        : 2/2 (100%)  <-- FIXED!

VERIFICATION SOURCE DISTRIBUTION:
  knowledge   :  0 (0%)
  consultant  :  0 (0%)
  llm         :  4 (100%)

CLASSIFICATION STATS:
  classified_as_fact   : 2
  classified_as_opinion: 2  <-- Early exit for opinions
  classified_as_claim  : 4

OVERALL GRADE: A
```

### Performance
- Opinion tests now complete in <3s (vs 25-36s for fact verification)
- No hardcoded keyword lists - pure LLM-based classification

### Files Changed
- `modules/daemon/correction_verifier.py` - Added classification layer

---

## [v11.28] - 2025-12-28

### Added
- **Cascade Verification System** - 3-step verification cascade:
  1. Knowledge Library (ChromaDB) - high confidence matches
  2. Consultant System (web search) - current facts
  3. LLM Fallback (mistral/phi3) - final verification
- Battery test suite: `tests/test_correction_verifier_v11_28.py`
- Test results saved to `data/benchmarks/correction_verifier_v11.28.json`

### Battery Test Results
```
Total Tests:  8
Passed:       6 (75%)
Failed:       2

BY CATEGORY:
  biology        : 1/1 (100%)
  chemistry      : 1/1 (100%)
  math           : 2/2 (100%)
  geography      : 1/1 (100%)
  science        : 1/1 (100%)
  opinion        : 0/2 (0%)

VERIFICATION SOURCE DISTRIBUTION:
  knowledge   :  0 (0%)
  consultant  :  0 (0%)
  llm         :  4 (100%)

OVERALL GRADE: C
```

### Known Issues
- Opinion/preference tests fail (marked DISPUTED instead of UNCERTAIN)
- Knowledge Library and Consultant System not triggering (0% usage)
- All verifications fall through to LLM fallback

### Files Changed
- `modules/daemon/correction_verifier.py` - Cascade verification logic
- `tests/test_correction_verifier_v11_28.py` - Battery test suite (NEW)
- `data/benchmarks/correction_verifier_v11.28.json` - Test results (NEW)

---

## [v11.27] - 2025-12-28

### Added
- **Correction Verification Layer** (anti-poisoning for training data)
- LLM-based verification of user corrections before storing for training
- New module: `modules/daemon/correction_verifier.py`
- Detection patterns for corrections in chat (e.g., "actually it's...", "that's wrong")
- JSONL storage for corrections by verification status

### Technical
- `CorrectionVerifier` class with async verification using `llama3.2:3b`
- `CorrectionStatus` enum: VERIFIED, DISPUTED, UNCERTAIN, PENDING
- Only VERIFIED corrections used for QLoRA training
- DISPUTED corrections logged separately for review
- Integration at `daemon_runner.py:689-739` for chat flow
- Direct `/correct` endpoint support for explicit corrections

### Security
- Prevents training data poisoning by malicious users
- Blocks factually incorrect corrections from entering training buffer
- Separates opinions/preferences from facts

---

## [v11.26] - 2025-12-28

### Added
- Debug logging for thought generation method tracking
- Method distribution reporting in monitor output

### Technical
- Added `[V11.26-DEBUG]` markers for tracing thought source (soul/process/template)
- Verified thought distribution: soul (72%), process (20%), template (8%)

---

## [v11.25] - 2025-12-28

### Fixed
- **GWT NoneType error** - `background_thinker.py:288` crashed when `global_workspace_theory` was None
- Template fallback reduced from 50%+ to <10% of thoughts

### Changed
- `background_thinker.py` line ~288: Added None check before accessing `gwt.current_state`
- Thought generation now properly uses soul/process methods instead of falling back to templates

### Results
- Soul method now generates 72% of thoughts (was ~40%)
- Process method now generates 20% of thoughts (was ~10%)
- Template fallback down to 8% (was 50%+)

---

## [v11.23] - 2025-12-27

### Fixed
- **Daemon stability verified** - Clean benchmark run with no crashes
- All 6 test categories completed successfully

### Results
```
Context Retention:      100%  (3-turn PASS, 8-turn PASS)
Naturalness:            100%  (greeting variety, tone, no prompt leakage)
Conversation Flow:      67%   (topic_switch PASS, disagreement PASS, follow_up FAIL)
Factual Accuracy:       80%   (4/5 - spider legs question failed)
Emotional Intelligence: 100%  (stress, excitement, neutral all PASS)
Response Time:          5.8s avg

OVERALL GRADE: A-
```

### Notes
- Daemon uptime: 37+ minutes without interruption
- 70+ queries handled during benchmark
- No connection errors or crashes

---

## [v11.22] - 2025-12-27

### Fixed
- **8-turn recall test now passing** - Increased history window from 10 to 15 exchanges
- Session recall markers now include "just discuss" and "just talk" patterns
- Added `[V11.22-DEBUG]` logging for history window tracking

### Changed
- `neutro.py` line ~2263: `user_conversations[-15:]` (was `-10:`)

### Results
```
Context Retention:      100%  (3-turn PASS, 8-turn PASS)
Naturalness:            67%
Conversation Flow:      33%
Factual Accuracy:       20%   (daemon crashed mid-test)
Emotional Intelligence: 0%    (daemon crashed mid-test)
```

---

## [v11.21] - 2025-12-27

### Added
- Minimal prompt bypass for current session recall queries
- Anti-hallucination instructions: "DO NOT make up topics"
- Session recall marker detection patterns

### Fixed
- **3-turn recall test now passing** - Stopped LLM from hallucinating discussed topics

### Results
```
Context Retention:      50%   (3-turn PASS, 8-turn FAIL)
```

---

## [v11.20] - 2025-12-27

### Added
- Initial benchmark suite (`tests/benchmark_suite.py`)
- 6 test categories with automated scoring
- JSON and Markdown report generation

### Identified Issues
- Context retention failing on both 3-turn and 8-turn tests
- Session recall queries polluting prompt with unrelated context

---

## Running Benchmarks

```bash
# Start daemon
./scripts/daemon_control.sh start

# Wait for daemon to be ready
sleep 30

# Run benchmark
python3 tests/benchmark_suite.py

# Results saved to:
# - data/benchmarks/YYYY-MM-DD_vX.XX.json
# - public-docs/test-results/vX.XX_YYYY-MM-DD.json
# - public-docs/test-results/vX.XX_YYYY-MM-DD.md
```
