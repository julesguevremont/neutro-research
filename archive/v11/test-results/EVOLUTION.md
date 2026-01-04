# NEUTRO Evolution Tracking

This directory contains automated benchmark results that track NEUTRO's development over time.

## Benchmark Categories

| Category | Description | Target |
|----------|-------------|--------|
| Context Retention | 3-turn and 8-turn conversation recall | 100% |
| Naturalness | Response variety, tone consistency, no prompt leakage | 100% |
| Conversation Flow | Follow-ups, topic switching, disagreement handling | 100% |
| Factual Accuracy | Knowledge questions (capital, math, science) | 100% |
| Emotional Intelligence | Stress, excitement, neutral responses | 100% |
| Response Time | Average query latency | <5s |

## Version History

### V11.23 (December 27, 2025) - A-
- **Overall Grade: A-** (first clean benchmark run)
- Context Retention: 100% (3-turn PASS, 8-turn PASS)
- Naturalness: 100% (greeting variety, tone consistency, no prompt leakage)
- Conversation Flow: 67% (follow_up FAIL, topic_switch PASS, disagreement PASS)
- Factual Accuracy: 80% (4/5 - spider legs question failed)
- Emotional Intelligence: 100%
- Response Time: 5.8s avg
- Daemon stability verified - 37+ min uptime, 70+ queries

### V11.22 (December 27, 2025)
- **Context Retention: 100%** (3-turn PASS, 8-turn PASS)
- Fix: Increased conversation history window from 10 to 15 exchanges
- Fix: Added "just discuss", "just talk" to session recall markers
- Fix: Anti-hallucination instructions in session recall prompt

### V11.21 (December 27, 2025)
- Context Retention: 50% (3-turn PASS, 8-turn FAIL)
- Implemented minimal prompt bypass for session recall queries
- Prevented LLM from hallucinating topics not discussed

### V11.20 (December 27, 2025)
- Initial benchmark suite implementation
- Identified context retention failures

## Test Files

| File | Description |
|------|-------------|
| `v11.XX_YYYY-MM-DD.json` | Raw benchmark results with full conversation logs |
| `v11.XX_YYYY-MM-DD.md` | Human-readable markdown summary |

## Interpreting Results

- **PASS**: Score >= 50% for category
- **FAIL**: Score < 50% for category
- **Overall Grade**: Average of all category scores
  - A: 90%+
  - B: 80-89%
  - C: 70-79%
  - D: 60-69%
  - F: <60%
