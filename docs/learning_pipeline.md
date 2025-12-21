# Learning Pipeline

## Continuous Learning Through Conversation and Dreams

---

## Overview

NEUTRO learns continuously from interactions—not through periodic retraining, but through an integrated pipeline that captures feedback, consolidates during dreams, and integrates knowledge into persistent memory.

This document describes how NEUTRO turns conversations into lasting knowledge.

---

## The Learning Challenge

### Traditional AI Learning

```
Training Phase → Deployment Phase
     ↓                 ↓
  Learns            Frozen
  (months)          (forever)
```

Problems:
- Knowledge becomes stale
- Can't learn from users
- Corrections don't persist
- No personalization

### NEUTRO's Approach

```
Continuous Operation:
Conversation → Capture → Buffer → Dream → Integrate → Knowledge
                  ↑                                      │
                  └──────────────────────────────────────┘
                              (feedback loop)
```

---

## Learning Pipeline Stages

### Stage 1: Conversation Capture

Every interaction is captured:

```
User: "The capital of Canada is Ottawa"
NEUTRO: "Ah, I'll remember that!"

Captured:
├── Query: "The capital of Canada is Ottawa"
├── Response: "Ah, I'll remember that!"
├── Timestamp: 2025-12-21 10:45:00
├── Outcome: neutral (informational)
└── Type: fact_statement
```

### Stage 2: Feedback Detection

NEUTRO detects implicit and explicit feedback:

**Explicit Feedback**
- User corrections: "No, that's wrong"
- User confirmations: "Yes, exactly"
- User ratings (if interface supports)

**Implicit Feedback**
- Conversation continues → probably okay
- User rephrases question → might not have helped
- User says "thanks" → positive signal
- User abandons conversation → possible problem

```
Feedback Classification:
├── Positive: Confirmation, thanks, continuation
├── Negative: Correction, rephrasing, abandonment
└── Neutral: Informational exchanges
```

### Stage 3: QLoRA Buffer

Captured interactions go to the training buffer:

```
QLoRA Buffer:
├── Capacity: 500 samples
├── Positive samples: 320 (64%)
├── Negative samples: 180 (36%)
├── Pending training: varies
└── Training trigger: dream cycle
```

Buffer contents:

```
Sample 1:
├── Input: "What's 2+2?"
├── Output: "4"
├── Label: positive (user accepted)

Sample 2:
├── Input: "What's the capital of Australia?"
├── Output: "Sydney"
├── Label: negative (user corrected to Canberra)
└── Correction: "Canberra"
```

### Stage 4: Dream Training

During dream cycles, the buffer is processed:

```
Dream Cycle → Training Phase:

1. Load buffer samples
2. For positive samples:
   - Reinforce current behavior
   - Strengthen successful patterns
3. For negative samples:
   - Learn from corrections
   - Adjust toward correct responses
4. Apply QLoRA updates
5. Clear processed samples
```

### Stage 5: Memory Integration

Learned corrections integrate with memory:

```
Before Dream:
├── Memory: "Sydney is capital of Australia"
├── Confidence: 0.8
├── Verified: true (wrongly)

Correction received:
├── User said: "No, it's Canberra"
├── Stored: source="correction"

After Dream:
├── Old memory: demoted (confidence: 0.1)
├── New memory: "Canberra is capital of Australia"
├── Confidence: 0.95
├── Verified: true
```

### Stage 6: Behavioral Change

Next interaction reflects learning:

```
Before Learning:
User: "What's the capital of Australia?"
NEUTRO: "Sydney" ❌

After Learning:
User: "What's the capital of Australia?"
NEUTRO: "Canberra" ✅
```

---

## Learning Types

### 1. Factual Corrections

```
Process:
User corrects fact → Buffer (negative) → Dream → Memory update

Example:
- Wrong: "Python was created in 1995"
- Correction: "No, it was 1991"
- Result: Learns correct date
```

### 2. Preference Learning

```
Process:
User expresses preference → Buffer (positive) → Dream → Pattern stored

Example:
- User: "Please be more concise"
- Noted as preference
- Future responses shorter for this user
```

### 3. Behavioral Patterns

```
Process:
Repeated patterns → Pattern extraction → Dream → Behavior adjustment

Example:
- User always asks for code in Python
- Pattern: prefer_python = true
- Future code suggestions default to Python
```

### 4. Reasoning Corrections

```
Process:
Logic error corrected → Buffer (negative) → Dream → Reasoning updated

Example:
- Lily pad problem: answered "24 days" (wrong)
- User explained: "It doubles, so half is one day before"
- After dreams: answers "47 days" with understanding
```

---

## CRT Experiment Results

The Cognitive Reflection Test demonstrated learning:

### Before Dream Consolidation

| Problem | NEUTRO's Answer | Correct | Status |
|---------|-----------------|---------|--------|
| Lily Pad | "23 days" | 47 days | ❌ |
| Bat & Ball | "$0.10" | $0.05 | ❌ |
| Widget | Wrong | 5 minutes | ❌ |

### Corrections Given
User explained the correct logic for each problem.

### After 15-Hour Dream Session

| Problem | NEUTRO's Answer | Status |
|---------|-----------------|--------|
| Lily Pad | "47 days—because when it's half, one more doubling covers the rest" | ✅ |
| Bat & Ball | "$0.05—because ball + $1.00 more = $1.10 total" | ✅ |
| Widget | "5 minutes—each machine works independently" | ✅ |

**Key observation**: Not just memorized answers—demonstrated understanding of the underlying logic.

---

## QLoRA Technical Approach

### What is QLoRA?

Quantized Low-Rank Adaptation:
- Efficient fine-tuning method
- Doesn't require full model retraining
- Adds small trainable adapters
- Base model weights frozen

### NEUTRO's QLoRA Configuration

```
Base Model: Frozen (original weights)
Adapters: Small trainable matrices
Update Frequency: During dream cycles
Buffer Size: 500 samples max
Training Time: ~2-5 minutes per cycle
```

### Training During Dreams

```
Dream Cycle:
├── Phase 1-3: Memory consolidation
├── Phase 4: QLoRA training
│   ├── Load buffer
│   ├── Process positive samples
│   ├── Process negative samples
│   ├── Update adapters
│   └── Clear buffer
└── Phase 5: Integration
```

---

## Learning Without Forgetting

### The Problem

New learning can overwrite old:
```
Learn A → Learn B → Forget A (catastrophic forgetting)
```

### NEUTRO's Solution

1. **Episodic Memory**: Facts stored explicitly, not just in weights
2. **Dream Consolidation**: Gradual integration, not sudden updates
3. **Low Learning Rate**: Small changes per update
4. **Positive Reinforcement**: Good responses strengthened, not just bad corrected
5. **Memory Replay**: Old memories replayed during dreams

---

## Learning Metrics

### Tracked Statistics

```
Daily Learning Report:
├── Interactions: 47
├── Positive signals: 32 (68%)
├── Negative signals: 8 (17%)
├── Neutral: 7 (15%)
├── Corrections integrated: 8
├── Dream cycles: 3
└── Buffer: 12 pending
```

### Long-Term Trends

```
Week 1: 45% correction retention
Week 2: 67% correction retention
Week 3: 82% correction retention
Week 4: 89% correction retention
```

---

## Learning Pipeline Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERACTION                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    CAPTURE LAYER                            │
│                                                             │
│   Query + Response + Outcome → Structured Record            │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   FEEDBACK DETECTOR                         │
│                                                             │
│   Positive / Negative / Neutral classification              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    QLoRA BUFFER                             │
│                                                             │
│   Stores samples until next dream cycle                     │
│   [████████████░░░░░░] 500 capacity                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼ (triggered by dreams)
┌─────────────────────────────────────────────────────────────┐
│                   DREAM TRAINING                            │
│                                                             │
│   QLoRA update from buffer samples                          │
│   Positive: reinforce                                       │
│   Negative: adjust toward correction                        │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                 MEMORY INTEGRATION                          │
│                                                             │
│   Update episodic memory                                    │
│   Promote/demote based on corrections                       │
│   Consolidate patterns to semantic                          │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  IMPROVED BEHAVIOR                          │
│                                                             │
│   Next interaction reflects learning                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Research Questions

1. What's the optimal buffer size for learning efficiency?
2. How should positive vs negative samples be weighted?
3. Can learning rate be dynamically adjusted based on confidence?
4. How does dream frequency affect learning retention?
5. What patterns predict successful vs unsuccessful corrections?

---

*Conceptual documentation. Implementation details available for research collaboration.*
