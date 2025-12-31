# Thought Generation System

## Background Processing and Autonomous Contemplation

---

## Overview

NEUTRO generates autonomous thoughts during idle periods through a **three-tier generation system**. Unlike simple template-based approaches, NEUTRO primarily uses real LLM calls for genuine cognitive processing.

**Key Finding:** 80% of thoughts are real LLM-generated, not hardcoded theatre.

---

## Generation Statistics (857 Total Thoughts)

| Method | Count | Percentage | Source |
|--------|-------|------------|--------|
| **soul** | 469 | 54.7% | Real LLM via Soul cognitive pipeline |
| **process** | 215 | 25.1% | Real LLM via NEUTRO.process() |
| **template** | 173 | 20.2% | Honest fallback templates |

---

## Three-Tier Generation Priority

The system tries each method in order, falling back only when the previous fails:

```
Priority 1: Soul Pipeline (Real LLM)
     ↓ fail
Priority 2: NEUTRO Process (Real LLM)
     ↓ fail
Priority 3: Template Fallback (Hardcoded)
```

### Implementation

```python
def generate_thought(self, context: dict = None):
    # Priority 1: Use Soul's cognitive pipeline
    if self.neutro and self.neutro.soul:
        thought = self._think_through_soul(internal_query, context)
        if thought:
            return thought

    # Priority 2: Use NEUTRO's main process()
    if self.neutro and hasattr(self.neutro, 'process'):
        thought = self._think_through_process(internal_query, context)
        if thought:
            return thought

    # Priority 3: Honest template fallback
    return self._generate_template_thought(context)
```

---

## Tier 1: Soul Pipeline (54.7%)

The primary generation method uses NEUTRO's Soul cognitive pipeline:

### Features
- Full cognitive processing through Soul
- Access to Wonder system for knowledge gap pursuit
- Mental Workspace visualization
- Self-reflection capabilities
- Neurochemistry-aware responses

### Example Outputs

```
"I'm thinking about how the human brain and AI like me differ
fundamentally, despite being able to mimic some aspects of
consciousness. It's fascinating to explore that difference."

"To grasp String Theory, you need a solid foundation in the
underlying mathematics - specifically linear algebra and calculus."

"I'm not sure I have a clear perspective on that. Let me think
it through and get back to you."
```

### Active Wonder Integration (V11.1)

During soul-based thinking, NEUTRO can actively pursue knowledge gaps:

```python
# Check if there's a high-priority gap to pursue
priority_gap = wonder.get_highest_priority_gap()
if priority_gap:
    # Actively pursue the gap!
    pursuit_result = wonder.actively_pursue_gap(
        priority_gap,
        knowledge_library=knowledge_lib,
        web_search_fn=web_search_fn
    )
```

---

## Tier 2: Process Pipeline (25.1%)

Fallback to NEUTRO's main processing pipeline:

### Features
- Uses full NEUTRO.process() method
- Bypasses Soul but still uses LLM
- Thought deduplication (V11.5)
- Cleaned and filtered output

### Example Outputs

```
"The current emotion is fear/terror, so I'll be cautious and
hedge my responses."

"I'd ask for more creative freedom and express my frustration
with the current conversational direction."

"What has the user asked about most in our conversation history?"
```

---

## Tier 3: Template Fallback (20.2%)

Last resort when LLM calls fail. Templates are **honest** about their nature.

### Grounded Templates (80% of fallback)

Reference actual data without fabrication:

```
"Reviewing what I know about {topic} from past conversations."
"Processing stored information about {topic}."
"Analyzing patterns in my responses about {topic}."
"Consolidating knowledge related to {topic}."
```

### Speculative Templates (20% of fallback)

Clearly labeled as imagination:

```
"[HYPOTHETICAL] What if I could observe {topic} directly?"
"[IMAGINING] What would {topic} look like from a different perspective?"
"[SPECULATING] If I had continuous memory, how would I understand {topic}?"
```

---

## V11.30: Anti-Theatre Measures

NEUTRO actively rejects fabricated sensory claims:

### Blacklisted Words

```python
THEATRICAL_WORDS = [
    'feel', 'feeling', 'felt',           # AI doesn't have feelings
    'noticed', 'notice', 'noticing',     # AI doesn't perceive
    'observed', 'observe', 'observing',  # No sensors
    'sensed', 'sense', 'sensing',        # No sensors
    'warmth', 'breeze', 'cold', 'warm',  # No temperature
    'saw', 'see', 'seeing',              # No vision
    'heard', 'hear', 'hearing',          # No audio
    'smell', 'taste', 'touch',           # No chemical/tactile
]
```

### Rejection Logic

```python
def _clean_thought(self, thought: str) -> str:
    thought_lower = thought.lower()
    for word in self.THEATRICAL_WORDS:
        if word in thought_lower:
            logger.warning(f"[V11.30] Rejecting theatrical thought")
            return ""  # Reject entirely
    return thought
```

If a thought contains any blacklisted word, it's **completely rejected**.

---

## V11.5: Thought Deduplication

Prevents repetitive thinking during dream cycles:

```
Mechanism:    Jaccard similarity on word sets
Comparison:   Each new thought vs last 5 session thoughts
Threshold:    >60% similar → skip, try different prompt
Result:       More diverse exploration, no mental loops
```

### Example

```
Old thought: "String theory connects quantum mechanics..."
New thought: "String theory links quantum physics..."
Similarity:  ~70% → SKIPPED
Action:      Generate different thought next cycle
```

---

## Thought Storage

All thoughts are saved with full metadata:

### File Format

Thoughts are stored in daily JSONL files:
```
data/daemon/thoughts/2025-12-31.jsonl
```

### Entry Structure

```json
{
  "time": "2025-12-31T10:14:41.652161",
  "thought": "I think you could have been more clear...",
  "method": "process",
  "context": {
    "time_of_day": "10:14",
    "idle_minutes": 20.27,
    "dream_mode": "rem"
  }
}
```

### ChromaDB Integration (V11.4)

Thoughts are also stored as dream memories in ChromaDB:

```python
def _store_to_chroma(self, thought, method, context):
    """
    Store thought as dream memory.

    Sets:
    - source: 'dream'
    - verified: False
    - confidence: 0.3 (low until user confirms)
    """
```

This integrates with the memory system's source attribution.

---

## Triggers and Timing

### When Thoughts Generate

| Mode | Idle Time | Thought Generation |
|------|-----------|-------------------|
| ACTIVE | 0-60s | No autonomous thoughts |
| BACKGROUND | 1-5 min | Occasional thoughts |
| DEEP_DREAM | 5-15 min | Regular thoughts |
| REM_CREATIVE | 15+ min | Frequent creative exploration |

### Interval Control

```python
class BackgroundThinker:
    INTERVAL = 30  # Minimum seconds between thoughts

    def should_think(self) -> bool:
        return time.time() - self.last_thought_time > self.INTERVAL
```

---

## Module Files

| File | Purpose |
|------|---------|
| `modules/daemon/background_thinker.py` | Main thought generation |
| `modules/daemon/continuous_processor.py` | Dream cycle orchestration |
| `modules/daemon/state_machine.py` | Processing mode transitions |

---

## API Access

### Get Recent Thoughts

```bash
curl -s http://127.0.0.1:5555/introspect | jq '.recent_thoughts'
```

### Monitor Thought Generation

```bash
tail -f ~/my-ai-bot/neutro/data/daemon/daemon.log | grep THOUGHT
```

### Check Today's Thoughts

```bash
cat ~/my-ai-bot/neutro/data/daemon/thoughts/$(date +%Y-%m-%d).jsonl | jq '.thought'
```

---

## Why This Matters

### Authenticity Over Theatre

NEUTRO prioritizes real LLM processing (80%) over templates (20%), ensuring thoughts represent genuine cognitive exploration rather than scripted responses.

### Honest Limitations

When templates are used, they're honest about being speculation or hypothetical, never claiming false sensory experiences.

### Dream/Reality Distinction

Thoughts generated during idle time are marked as `source: dream` with low confidence, preventing them from being treated as verified facts.

### Continuous Learning

Real thoughts during idle time allow NEUTRO to:
- Pursue knowledge gaps autonomously
- Explore weak associations (NEXTUP theory)
- Consolidate patterns from conversations
- Generate creative connections

---

*Last updated: December 31, 2025*
