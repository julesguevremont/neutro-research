# Memory System

## Hierarchical Memory Architecture with Source Attribution

---

## Overview

NEUTRO implements a four-tier hierarchical memory system inspired by human memory organization. Unlike traditional AI systems that treat all information equally, NEUTRO distinguishes between memory types and—critically—tracks the *source* of each memory.

---

## Memory Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                     WORKING MEMORY                          │
│                                                             │
│   Current conversation context                              │
│   ~10 most recent turns                                     │
│   Volatile (cleared on session end)                         │
│   Purpose: Immediate coherence                              │
└─────────────────────────────────┬───────────────────────────┘
                                  │ consolidation
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    EPISODIC MEMORY                          │
│                                                             │
│   Specific interactions with timestamps                     │
│   "You asked about X on December 20th"                      │
│   Vector-indexed for semantic retrieval                     │
│   Purpose: Personal history, context                        │
└─────────────────────────────────┬───────────────────────────┘
                                  │ abstraction
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                    SEMANTIC MEMORY                          │
│                                                             │
│   Abstracted facts and patterns                             │
│   "User prefers concise responses"                          │
│   Extracted from episodic memories                          │
│   Purpose: General knowledge, preferences                   │
└─────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                     DREAM MEMORY                            │
│                                                             │
│   Hypotheses generated during sleep cycles                  │
│   NOT verified—explorations, not facts                      │
│   Low confidence until confirmed                            │
│   Purpose: Creative connections, candidates for learning    │
└─────────────────────────────────────────────────────────────┘
```

---

## V11.4: Source Attribution

### The Problem

Without source tracking, AI systems can confuse:
- What users actually said
- What the system generated internally
- What was corrected vs original

This leads to hallucination and false confidence.

### The Solution

Every memory in NEUTRO includes metadata:

```
Memory Entry:
├── content: "User lives in Montreal"
├── source: "conversation" | "dream" | "correction" | "fact"
├── verified: true | false
├── confidence: 0.0 - 1.0
├── timestamp: when created
└── dream_phase: (if source=dream) "light" | "deep" | "rem"
```

### Source Types

| Source | Meaning | Verified | Confidence |
|--------|---------|----------|------------|
| `conversation` | From actual user interaction | true | 0.9 |
| `dream` | Generated during sleep cycle | false | 0.3 |
| `correction` | User corrected previous belief | true | 0.95 |
| `fact` | Promoted from dream (confirmed) | true | 0.95 |

---

## Memory Operations

### Storage

**Conversation Memory**
- Stored immediately after interaction
- Marked as verified
- High confidence

**Dream Memory**
- Generated during idle processing
- Marked as unverified
- Low confidence
- Tagged with dream phase

### Retrieval

**Standard Search**
- Returns all relevant memories
- Includes source metadata
- Caller decides how to weight

**Verified-Only Search**
- Returns only confirmed facts
- Used when certainty required
- Excludes dream hypotheses

**Source-Aware Search**
- Returns memories with full context
- Enables appropriate response framing:
  - Verified: "You mentioned..."
  - Dream: "I was thinking about..."
  - Uncertain: "I'm not sure if we discussed..."

### Promotion / Demotion

**Promote to Fact**
- Dream hypothesis confirmed by user
- Confidence raised to 0.95
- Source changed to "fact"
- Now usable as verified knowledge

**Demote Memory**
- User corrects previous belief
- Confidence lowered to 0.1
- Source changed to "correction"
- Prevents future use as fact

---

## How Dreams Use Memory

During dream cycles, NEUTRO:

1. **Replays** episodic memories
2. **Explores** weak associations between memories
3. **Generates** new connections (stored as dream memories)
4. **Consolidates** repeated patterns into semantic memory
5. **Prunes** low-value connections

Dream memories are *candidates* for knowledge, not knowledge itself. Only user confirmation promotes them to facts.

---

## Memory Flow Example

```
Day 1:
User: "I live in Montreal"
→ Stored: source=conversation, verified=true, confidence=0.9

Night 1 (Dream):
System explores: "Montreal → AI hub → MILA → research"
→ Stored: source=dream, verified=false, confidence=0.3
  Content: "User might be interested in MILA"

Day 2:
User: "What do you remember about me?"
→ NEUTRO: "You mentioned you live in Montreal."
  (Uses verified memory, states as fact)

→ NEUTRO: "I was thinking—are you connected to 
   the AI research community there?"
  (Uses dream memory, frames as exploration)

User: "Yes, I know people at MILA"
→ Dream hypothesis CONFIRMED
→ promote_to_fact() called
→ Now stored: source=fact, verified=true, confidence=0.95
```

---

## Technical Implementation

### Storage Backend

- **ChromaDB**: Vector database for semantic search
- **Embedding Model**: Sentence transformers for vectorization
- **Persistence**: Disk-backed, survives restarts

### Performance

| Operation | Latency |
|-----------|---------|
| Store memory | ~15ms |
| Exact match search | ~12ms |
| Semantic search | ~45ms |
| Cross-session retrieval | ~67ms |

### Capacity

- No hard limit (ChromaDB scales)
- Tested with 1000+ memories
- Pruning during dreams manages growth

---

## Why This Matters

### Prevents Hallucination
System knows what it imagined vs what it learned.

### Enables Creativity
Dreams can explore freely without polluting knowledge.

### Builds Trust
Users can rely on verified statements.

### Supports Learning
Hypotheses can become facts through confirmation.

---

## Research Questions

1. What's the optimal confidence threshold for using dream memories?
2. How should promotion/demotion affect related memories?
3. Can source attribution improve long-term factual accuracy?
4. How does memory hierarchy affect retrieval relevance?

---

*Conceptual documentation. Implementation details available for research collaboration.*
