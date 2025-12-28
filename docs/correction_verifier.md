# Correction Verification Layer (V11.27)

## Purpose

Prevents training data poisoning by verifying user corrections against base LLM knowledge before storing them for learning.

## Problem Solved

Users can correct NEUTRO during conversation, but blindly trusting all corrections could poison the learning system:
- Malicious users could feed false information
- Honest mistakes could be learned as facts
- Subjective opinions could be stored as facts

## How It Works

### Verification Flow

1. **Detection**: User correction detected in chat or via `/correct` endpoint
2. **Verification**: Base LLM asked: "Is {correction} factually accurate?"
3. **Classification**:
   - **VERIFIED**: LLM agrees correction is factually correct
   - **DISPUTED**: LLM disagrees with the correction
   - **UNCERTAIN**: Cannot determine (opinion/preference)
4. **Storage**: Correction stored in appropriate file based on status

### Only VERIFIED Corrections Train

```
User: "Actually, spiders have 8 legs, not 6"
  ↓
LLM Verification: "Is 'spiders have 8 legs' factually correct?"
  ↓
LLM Response: "VERIFIED - spiders have 8 legs, not 6"
  ↓
Correction stored → QLoRA buffer → Wound planted
```

### DISPUTED Corrections Blocked

```
User: "Actually, the sky is green"
  ↓
LLM Verification: "Is 'the sky is green' factually correct?"
  ↓
LLM Response: "DISPUTED - the sky appears blue due to Rayleigh scattering"
  ↓
Logged for review → NOT used for training
```

---

## Classification Types

| Status | Meaning | Training |
|--------|---------|----------|
| `VERIFIED` | LLM confirms correction is factually accurate | Used for training |
| `DISPUTED` | LLM disagrees with correction | Logged, NOT trained |
| `UNCERTAIN` | Opinion/preference, not verifiable | Flagged, NOT trained |
| `PENDING` | Awaiting verification | Queued |

---

## Storage Paths

Corrections are stored in JSONL files by status:

```
data/corrections/
├── verified.jsonl    # Used for training
├── disputed.jsonl    # Logged for review
└── uncertain.jsonl   # Flagged as opinions
```

Each record contains:
```json
{
  "timestamp": "2025-12-28T14:30:00",
  "query": "How many legs does a spider have?",
  "wrong_answer": "Spiders have 6 legs",
  "correction": "Spiders have 8 legs",
  "status": "verified",
  "reasoning": "Correct - spiders are arachnids with 8 legs",
  "confidence": 0.95
}
```

---

## Detection Patterns

Corrections are detected in chat using these patterns:

- "no, i meant..."
- "actually it's..."
- "wrong,"
- "not correct"
- "that's not right"
- "you misunderstood"
- "no, it's..."
- "actually,"
- "that's wrong"
- "incorrect"
- "the correct answer is..."
- "it should be..."

---

## API Integration

### Via Chat (`/query`)

Corrections are automatically detected in regular conversation:

```bash
curl -X POST http://localhost:5555/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Actually, that is wrong. The capital of Australia is Canberra."}'
```

Response includes correction metadata:
```json
{
  "response": "You're right, I apologize...",
  "correction_detected": true,
  "correction_verified": true,
  "correction_status": "verified"
}
```

### Via `/correct` Endpoint

Direct correction submission:

```bash
curl -X POST http://localhost:5555/correct \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is 2+2?",
    "wrong_response": "2+2 is 5",
    "correct_response": "2+2 is 4"
  }'
```

Response:
```json
{
  "status": "verified",
  "reasoning": "Correct - 2+2 equals 4",
  "confidence": 0.99,
  "learned": true
}
```

---

## Verification Model

Uses `llama3.2:3b` for verification with:
- Temperature: 0.1 (low for consistent answers)
- Max tokens: 200
- Direct Ollama call as fallback

---

## Implementation Files

| File | Purpose |
|------|---------|
| `modules/daemon/correction_verifier.py` | Core verification logic |
| `daemon_runner.py:59-64` | Import statements |
| `daemon_runner.py:148-149` | DaemonState attribute |
| `daemon_runner.py:689-739` | Chat flow integration |
| `daemon_runner.py:1308-1311` | Initialization |

---

## Statistics

Access correction stats via `/introspect`:

```json
{
  "correction_verifier": {
    "total_checked": 45,
    "verified": 38,
    "disputed": 5,
    "uncertain": 2,
    "verified_rate": 0.84,
    "disputed_rate": 0.11
  }
}
```

---

*Technical documentation for V11.27. Implementation in `modules/daemon/correction_verifier.py`.*
