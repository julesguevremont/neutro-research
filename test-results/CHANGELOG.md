# NEUTRO Benchmark Changelog

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
