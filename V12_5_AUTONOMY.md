# NEUTRO V12.5: Autonomous Research & Scientific Discovery

*Released: January 2, 2026*

V12.5 introduces **autonomous scientific research capabilities** - NEUTRO can now independently discover, read, and integrate knowledge from academic papers without human intervention.

---

## New Capabilities

### 1. Knowledge Graph (`/knowledge` endpoint)

NEUTRO now builds a **semantic knowledge graph** from research findings:

```
GET /knowledge
```

Response:
```json
{
  "stats": {
    "concept_count": 10,
    "relation_count": 5,
    "categories": {"molecule": 3, "protein": 1, "process": 3}
  },
  "mermaid": "graph LR\n  NAD+ -->|activates| Sirtuins\n  Sirtuins -.->|inhibits| Aging",
  "recent_concepts": [
    {"name": "NAD+", "category": "molecule", "confidence": 0.5},
    {"name": "Sirtuins", "category": "protein", "confidence": 0.6}
  ],
  "recent_relations": [
    {"source": "NAD+", "relation": "activates", "target": "Sirtuins"}
  ]
}
```

**Features:**
- Automatic concept extraction from papers
- Relationship mapping (activates, inhibits, increases, decreases)
- Mermaid diagram generation for visualization
- Contradiction detection between sources

---

### 2. Hypothesis Engine (`/hypotheses` endpoint)

NEUTRO generates and tracks **scientific hypotheses** based on accumulated knowledge:

```
GET /hypotheses
```

Response:
```json
{
  "stats": {
    "total_hypotheses": 3,
    "by_status": {"untested": 3},
    "by_confidence": {"medium": 1, "low": 2}
  },
  "hypotheses": [
    {
      "id": "9f4428ed6315",
      "statement": "NAD+ supplementation may slow cellular aging through sirtuin activation",
      "category": "intervention",
      "confidence": "medium",
      "status": "untested",
      "evidence_count": 2
    }
  ]
}
```

**Features:**
- Automatic hypothesis generation from knowledge graph patterns
- Priority scoring based on evidence and testability
- Category classification (intervention, biomarker, combination)
- Evidence tracking from multiple sources

---

### 3. Code Executor (`/execute` endpoint)

NEUTRO can now **execute Python code** in a secure sandbox for data analysis:

```
POST /execute
Content-Type: application/json

{
  "code": "import math; print(math.pi)",
  "approved": true
}
```

Response:
```json
{
  "success": true,
  "stdout": "3.141592653589793\n",
  "stderr": "",
  "execution_time_ms": 1.5,
  "blocked_calls": []
}
```

**Security Features:**
- AST-based code validation before execution
- Whitelist-only imports (math, statistics, json, datetime, etc.)
- Blocked dangerous operations (file I/O, network, subprocess)
- Thread-based timeout (works in HTTP handler threads)
- Maximum output size limits

---

### 4. ArXiv Paper Reader

NEUTRO autonomously searches and reads academic papers:

```python
# Automatic during idle research
BackgroundThinker.generate_thought()
  -> searches arXiv for learning goals
  -> downloads and reads full paper PDFs
  -> extracts concepts to knowledge graph
  -> generates hypotheses from findings
```

**Current Learning Goals:**
- Telomere biology
- Senolytics research
- NAD+ metabolism
- Brain preservation
- Connectome mapping

---

## Configuration Changes

### Faster Research Activation

```python
# daemon_runner.py
AUTO_THINKING_IDLE_MINUTES = 2  # V12.5: Was 10, now 2 minutes
```

NEUTRO begins autonomous research after just 2 minutes of idle time.

---

## Bug Fixes in V12.5

| Issue | Cause | Fix |
|-------|-------|-----|
| `/knowledge` slice error | Dict slicing `kg.concepts[-10:]` | Changed to `list(kg.concepts.values())[-10:]` |
| `/execute` signal error | `signal.alarm()` in worker threads | Replaced with `threading.Thread` + `join(timeout=...)` |
| Hypothesis iteration error | `for h in engine.hypotheses` on dict | Changed to `engine.hypotheses.values()` |
| ExecutionResult subscript error | `result['success']` on dataclass | Changed to `result.to_dict()['success']` |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     V12.5 AUTONOMY MODULE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐        │
│  │ Paper Reader │──▶│  Knowledge   │──▶│  Hypothesis  │        │
│  │   (arXiv)    │   │    Graph     │   │    Engine    │        │
│  └──────────────┘   └──────────────┘   └──────────────┘        │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│  ┌──────────────────────────────────────────────────────┐      │
│  │              Background Thinker                       │      │
│  │  (Coordinates research during idle periods)           │      │
│  └──────────────────────────────────────────────────────┘      │
│         │                  │                  │                 │
│         ▼                  ▼                  ▼                 │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐              │
│  │ /knowledge │   │/hypotheses │   │  /execute  │              │
│  │  endpoint  │   │  endpoint  │   │  endpoint  │              │
│  └────────────┘   └────────────┘   └────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Research Activity Example

```
[2026-01-02 20:10:02] ARXIV [connectome mapping]:
  Read 'A Connectome Based Hexagonal Lattice Convolutional Network
  Model of the Drosophila Visual System' by Fabian David Tschopp

[2026-01-02 20:12:51] WEB_RESEARCH [connectome mapping]:
  Found Connectome Mapper processing pipeline for brain mapping

[2026-01-02 20:15:39] WEB_RESEARCH [brain preservation]:
  Found "10 Mind-Blowing Brain Discoveries from 2025"
```

---

## Files Changed

| File | Changes |
|------|---------|
| `daemon_runner.py` | Added `/knowledge`, `/hypotheses`, `/execute` endpoints; fixed dict iteration |
| `modules/sandbox/code_executor.py` | Replaced signal timeout with threading-based timeout |
| `modules/research/knowledge_graph.py` | New - semantic knowledge graph with concept/relation extraction |
| `modules/research/hypothesis_engine.py` | New - hypothesis generation and tracking |
| `modules/research/paper_reader.py` | New - arXiv search and PDF reading |
| `modules/daemon/background_thinker.py` | Integrated with V12.5 research modules |

---

## Next Steps (V12.6+)

- [ ] Automated experiment design from hypotheses
- [ ] Cross-paper citation analysis
- [ ] Confidence calibration from evidence strength
- [ ] Integration with external databases (PubMed, bioRxiv)
- [ ] Collaborative research with human feedback loop

---

*Created by Cez - NEUTRO continues to grow.*
