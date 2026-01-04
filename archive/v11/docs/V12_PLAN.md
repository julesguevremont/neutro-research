# V12.0 Integration Plan

*Target: January 2025*

This document outlines the integration plan for V12.0, building on the V11.28 Cascade Correction Verifier foundation.

---

## Current State (V11.28)

### Battery Test Results
```
Total Tests:  8
Passed:       6 (75%)
Failed:       2

Grade: C
```

### Cascade Verification Status
| Component | Status | Usage | Notes |
|-----------|--------|-------|-------|
| Knowledge Library (ChromaDB) | Implemented | 0% | Needs population |
| Consultant System (Web Search) | Implemented | 0% | Needs configuration |
| LLM Fallback (mistral/phi3) | Working | 100% | All verifications |

---

## Component Integration Table

| Module | Location | V11.28 Status | V12.0 Target |
|--------|----------|---------------|--------------|
| CorrectionVerifier | `modules/daemon/correction_verifier.py` | Working (75%) | 95%+ accuracy |
| Knowledge Library | `modules/hierarchical_memory.py` | Exists, not triggered | Auto-populate common facts |
| Consultant System | `modules/daemon/consultant.py` | Placeholder | Web search integration |
| Background Thinker | `modules/daemon/background_thinker.py` | Working | Feed verified facts |
| Continuous Processor | `modules/daemon/continuous_processor.py` | Working | Trigger verification |
| SelfReflection | `modules/daemon/self_reflection.py` | Partial | Full integration |
| Metacognition | `modules/metacognition.py` | Not integrated | Import and use |

---

## V12.0 Architecture Flow

```
                            USER CORRECTION
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │    CorrectionVerifier       │
                    │    (correction_verifier.py) │
                    └─────────────────────────────┘
                                  │
                                  ▼
        ┌─────────────────────────────────────────────────────┐
        │                 CASCADE VERIFICATION                 │
        │                                                      │
        │  ┌─────────────┐   ┌─────────────┐   ┌───────────┐  │
        │  │  STEP 1     │   │  STEP 2     │   │  STEP 3   │  │
        │  │  Knowledge  │──▶│  Consultant │──▶│  LLM      │  │
        │  │  Library    │   │  (Web)      │   │  Fallback │  │
        │  │  (ChromaDB) │   │             │   │           │  │
        │  └─────────────┘   └─────────────┘   └───────────┘  │
        │        │                 │                 │        │
        │        │   conf≥0.70     │   conf≥0.60     │        │
        │        ▼                 ▼                 ▼        │
        │    VERIFIED          VERIFIED          VERIFIED     │
        │    DISPUTED          DISPUTED          DISPUTED     │
        │                                        UNCERTAIN    │
        └─────────────────────────────────────────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
           ┌───────────────┐          ┌───────────────┐
           │   VERIFIED    │          │   DISPUTED    │
           │               │          │   UNCERTAIN   │
           └───────────────┘          └───────────────┘
                    │                           │
                    ▼                           ▼
           ┌───────────────┐          ┌───────────────┐
           │ QLoRA Buffer  │          │ Review Queue  │
           │ (training)    │          │ (manual)      │
           └───────────────┘          └───────────────┘
                    │
                    ▼
           ┌───────────────┐
           │ Knowledge     │◀─── Feedback Loop
           │ Library       │     (populate with
           │ (ChromaDB)    │      verified facts)
           └───────────────┘
```

---

## V12.0 Integration Points

### 1. Knowledge Library Population

**File:** `modules/hierarchical_memory.py`

**Current State:** ChromaDB exists but has no pre-populated facts for verification.

**V12.0 Changes:**
```python
# Add common facts collection
COMMON_FACTS = {
    "biology": ["Spiders have 8 legs", "Humans have 46 chromosomes", ...],
    "chemistry": ["Water boils at 100°C at sea level", ...],
    "math": ["2 + 2 = 4", "Pi ≈ 3.14159", ...],
    "geography": ["Earth is an oblate spheroid", ...]
}

# Auto-populate on init
def populate_knowledge_library(self):
    for category, facts in COMMON_FACTS.items():
        for fact in facts:
            self.add_fact(fact, category=category, confidence=1.0)
```

**Integration Point:** `correction_verifier.py:_verify_via_knowledge()` lines 180-220

---

### 2. Consultant System (Web Search)

**File:** `modules/daemon/consultant.py` (NEW)

**V12.0 Implementation:**
```python
class ConsultantSystem:
    """Web search verification for current facts."""

    async def verify_fact(self, claim: str) -> VerificationResult:
        # 1. Generate search query from claim
        query = self._extract_search_query(claim)

        # 2. Perform web search (DuckDuckGo/SearXNG)
        results = await self._search(query)

        # 3. Cross-reference claim with search results
        return self._evaluate_against_results(claim, results)
```

**Integration Point:** `correction_verifier.py:_verify_via_consultant()` lines 222-280

---

### 3. Opinion Detection Fix

**File:** `modules/daemon/correction_verifier.py`

**Current Issue:** Opinion tests return DISPUTED instead of UNCERTAIN.

**V12.0 Fix:**
```python
# Enhanced opinion detection in LLM prompt
OPINION_MARKERS = [
    "best", "worst", "favorite", "prefer", "better", "superior",
    "should", "ought", "beautiful", "ugly", "taste", "opinion"
]

def _is_opinion_claim(self, claim: str) -> bool:
    claim_lower = claim.lower()
    return any(marker in claim_lower for marker in OPINION_MARKERS)

# In verify_correction():
if self._is_opinion_claim(correction):
    return CorrectionStatus.UNCERTAIN, 0.5, "opinion", "Subjective preference"
```

---

### 4. Feedback Loop (Verified → Knowledge)

**New Integration:**
```python
# In correction_verifier.py after verification
if result.status == CorrectionStatus.VERIFIED:
    # Add to Knowledge Library for future lookups
    await self.knowledge_library.add_fact(
        fact=correction,
        category=self._detect_category(correction),
        confidence=result.confidence,
        source="verified_correction",
        timestamp=datetime.now().isoformat()
    )
```

---

## V12.0 Milestones

| Milestone | Description | Target |
|-----------|-------------|--------|
| V12.0-alpha | Knowledge Library population | Week 1 |
| V12.0-beta | Consultant System web search | Week 2 |
| V12.0-rc1 | Opinion detection fix | Week 3 |
| V12.0 | Full integration + 95% battery | Week 4 |

---

## Testing Plan

### Battery Test Updates
```python
# Add more opinion tests
("Music preference", "opinion", "Jazz is better than rock", "uncertain"),
("Art judgment", "opinion", "Picasso was the greatest painter", "uncertain"),
("Life advice", "opinion", "Everyone should exercise daily", "uncertain"),

# Add web-verifiable tests
("Current event", "news", "The current US president is...", "verified"),
("Live data", "data", "Bitcoin's current price is...", "verified"),
```

### Expected V12.0 Results
```
Total Tests:  15
Passed:       14 (93%)
Failed:       1

BY CATEGORY:
  biology        : 2/2 (100%)
  chemistry      : 2/2 (100%)
  math           : 3/3 (100%)
  geography      : 2/2 (100%)
  science        : 2/2 (100%)
  opinion        : 3/3 (100%)  <-- Fixed
  news           : 0/1 (0%)    <-- Needs live search

VERIFICATION SOURCE DISTRIBUTION:
  knowledge   : 6 (40%)  <-- Now triggering
  consultant  : 2 (13%)  <-- Now triggering
  llm         : 7 (47%)

OVERALL GRADE: A
```

---

## Dependencies

| Dependency | Purpose | Status |
|------------|---------|--------|
| ChromaDB | Knowledge Library | Installed |
| DuckDuckGo Search | Consultant System | Need to add |
| mistral:latest | LLM Fallback | Installed |
| phi3:latest | Secondary LLM | Installed |

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Web search rate limits | Consultant unavailable | Cache results, fallback to LLM |
| ChromaDB corruption | Knowledge Library fails | Regular backups, rebuild script |
| LLM hallucination | False verifications | Multi-model consensus |
| Opinion misclassification | Training data pollution | Explicit opinion markers |

---

*Document Version: 1.0*
*Created: 2025-12-28*
*Next Review: V12.0-alpha release*
