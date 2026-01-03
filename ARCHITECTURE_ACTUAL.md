# NEUTRO Architecture: What ACTUALLY Works
**Generated:** January 3, 2026
**Analysis by:** Claude Code (Opus 4.5)
**Purpose:** Honest documentation of real system behavior, not aspirational claims

---

## 1. REAL DATA FLOW: What Happens When You Send a Query

```
┌─────────────────────────────────────────────────────────────────────┐
│                    HTTP POST /query {"text": "..."}                 │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  daemon_runner.py:956                                               │
│  do_POST() → daemon.neutro.process_with_soul(query)                 │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  neutro.py:776  process_with_soul()                                 │
│  ├── self.hierarchical_memory.add(...)   # Store user query         │
│  ├── self.soul.think(query)              # Main processing          │
│  └── return response                                                │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  modules/soul.py - Soul.think()                                     │
│  The "5 Elements" of Soul:                                          │
│  ├── Foundation: Core identity, personality traits                  │
│  ├── Remember: ChromaDB search for relevant memories                │
│  ├── Reflect: Self-assessment, metacognition                        │
│  ├── Choose: Response selection strategy                            │
│  └── Wonder: Curiosity, question generation                         │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  LLM Call (Ollama)                                                  │
│  Model: qwen2.5:14b or configured model                             │
│  Prompt includes: Soul context + Memories + Query                   │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│  Response stored in ChromaDB with speaker="neutro"                  │
│  Background processes triggered:                                    │
│  ├── continuous_processor: Autonomous thinking loop                 │
│  ├── self_reflection: Metacognitive evaluation                      │
│  └── seed_growth: Plant insights for future processing              │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Files in Query Path (Actually Used)

| File | Function | Line |
|------|----------|------|
| `daemon_runner.py` | HTTP server, `do_POST()` | 956 |
| `neutro.py` | `process_with_soul()` | 776 |
| `modules/soul.py` | `Soul.think()` | 500+ |
| `modules/chroma_storage.py` | Vector storage | - |
| `modules/hierarchical_memory.py` | Memory abstraction | - |

---

## 2. MODULE INVENTORY: Active vs Dead Code

### Summary Statistics

| Category | Count |
|----------|-------|
| Total .py files in `modules/` | 242 |
| Subdirectory modules (`daemon/`, `senses/`) | 25 |
| **Actually imported** | ~48 unique (V11.75+3) |
| **Dead code candidates** | ~194 files (80%) |

### ACTIVE Modules (Actually Imported)

Sorted by import frequency:

| Module | Import Count | Purpose |
|--------|-------------|---------|
| `senses/*` | 31 | Time, location, system awareness |
| `soul` | 23 | Core cognitive layer |
| `daemon/*` | 16 | Background processing |
| `storage` | 8 | Data persistence |
| `hierarchical_memory` | 7 | Memory abstraction |
| `neurochemistry` | 6 | Emotional state modeling |
| `mental_workspace` | 6 | Working memory |
| `state_memory` | 5 | Session state |
| `soul_foundation` | 5 | Identity/personality base |
| `natural_intelligence` | 5 | Response naturalization |
| `soul_snn` | 4 | Spiking neural network |
| `emotional_core` | 4 | Emotion processing |
| `torque_clustering` | 3 | Concept organization |
| `smart_feedback` | 3 | Learning from corrections |
| `qlora_buffer` | 3 | Training data buffer |
| `pattern_learner` | 3 | Pattern extraction |
| `embeddings` | 3 | Vector embeddings |
| `cognitive_workspace` | 3 | Thought staging |
| `chroma_storage` | 2 | ChromaDB wrapper |
| `spreading_activation` | 2 | Memory activation |
| `self_model` | 2 | Self-representation |
| `knowledge_library` | 2 | Learned facts |
| `consultant_system` | 2 | Expert consultation |
| `web_search` | 2 | Internet search |
| `user_model` | 1 | User intent/mood detection (V11.75) |
| `context_tracker` | 1 | Project/task tracking (V11.75) |
| `self_correction` | 1 | Learns from corrections (V11.75) |

*Plus 21 more modules imported exactly once*

### DEAD CODE CANDIDATES (Never Imported)

These ~194 files exist in `modules/` but are **never imported** by any active code:

<details>
<summary>Click to expand dead code list (partial)</summary>

Notable unused modules:
- `ab_mcts_collaboration.py` - Monte Carlo Tree Search
- `advanced_memory.py` - Unused memory system
- `ai_orchestrator.py` - Unused orchestrator
- `analogy_reasoning.py` - Never integrated
- `autonomous_creator.py` - Self-creation (unused)
- `balanced_cognitive_processing.py` - Alternative processor
- `brain_inspired_thinking.py` - Unused thinking model
- `claude_teacher.py` - Claude integration (unused)
- `code_expert.py` / `code_expert_2025.py` - Code analysis
- `cognee_memory.py` - Cognee integration (unused)
- `comprehension_engine.py` - Language understanding
- `conscious_reasoning_chain.py` - CoT implementation
- `context_aware.py` - Context tracking
- `continual_learning.py` - Learning system
- `counter_argument.py` - Argumentation
- `ctm_orchestration.py` - CTM framework
- `dual_brain.py` - Dual process theory
- `dynamic_brain.py` - Dynamic architecture
- `enhanced_ewc.py` - Elastic Weight Consolidation
- `extended_thinking.py` - Long-form reasoning
- `free_sketch_agent.py` - Creative drawing
- `global_workspace.py` - GWT implementation
- `graph_reasoning.py` - Graph-based logic
- `improved_conscious_chain.py` - Better CoT
- `integrated_consciousness.py` - Consciousness model
- `intelligent_fast_consciousness.py` - Fast thinking
- `math_engine.py` - Math processing
- `mem0_integration.py` / `mem0_memory.py` - Mem0 (unused)
- `meta_reasoning.py` - Meta-level reasoning
- `multi_model_brain.py` - Multi-model routing
- `neutro_brain.py` - Alternative brain
- `neutro_visual_cortex.py` - Vision processing
- `parallel_activator.py` - Parallel processing
- `physics_engine.py` - Physics simulation
- `pipecat_integration.py` - Pipecat voice
- `plugin_curiosity_advanced.py` - Curiosity plugin
- `plugin_ewc.py` - EWC plugin
- `plugin_memory_consolidation.py` - Memory plugin
- `plugin_self_modification.py` - Self-mod plugin
- `query_decomposer.py` - Query breakdown
- `real_learning.py` - Learning system
- `realtime_qlora.py` - Real-time training
- `research_2025_integration.py` - Research papers
- ~~`self_correction.py`~~ - Now active (V11.75)
- `sketch_rnn_neural.py` - Sketch generation
- `snn_router.py` - SNN routing
- `spatial_imagination.py` - Spatial reasoning
- `unified_processor.py` - Unified processing
- `value_emergence.py` - Value learning
- ... and 150+ more

</details>

---

## 3. INTEGRATION MAP: What Actually Connects

### Soul → SNN Integration

```
modules/soul.py:3021
    from modules.soul_snn import SoulSpikingNetwork

Soul.think()
    └── SoulSpikingNetwork (800 neurons)
        ├── Neurons born/die based on usage
        ├── Activation patterns stored
        └── Influences response selection
```

**Reality:** SNN is imported and instantiated. Neuron counts tracked (1631 born, 931 died = 800 active). Used for activation-based memory retrieval weighting.

### Memory → LLM Integration

```
ChromaDB (2099+ memories)
    │
    ├── search_similar(query, k=5)
    │   └── Returns relevant memories
    │
    └── Injected into LLM prompt:
        "Based on these memories: [...]
         User asks: [query]
         Respond as NEUTRO..."
```

**Reality:** Memories directly concatenated into prompt. Speaker attribution (V11.74) ensures user facts vs NEUTRO facts distinction.

### Dreams → Memory Integration

```
modules/daemon/dream_engine.py
    │
    ├── DreamEngine.dream()
    │   ├── Retrieves 50 random memories
    │   ├── Runs consolidation patterns
    │   └── Generates "dream narrative"
    │
    └── Stores results with speaker="dream"
        └── ChromaDB collection
```

**Reality:** Dream engine runs during idle periods. Creates synthetic memories marked as dreams. These are stored but filtered differently during recall.

### Background Processing Loop

```
daemon_runner.py starts:
    │
    ├── ContinuousProcessor (background thread)
    │   └── Generates thoughts when idle
    │
    ├── RealtimeVerifier
    │   └── Validates facts against memory
    │
    ├── SeedGrowth
    │   └── Develops planted ideas over time
    │
    └── SelfReflection
        └── Metacognitive evaluation
```

### V11.75: User Understanding Integration

```
daemon_runner.py query processing:
    │
    ├── ContextTracker (modules/context_tracker.py)
    │   ├── update_from_interaction(query)
    │   ├── Tracks current project/task/weekly focus
    │   └── Persists to data/current_context.json
    │
    ├── UserModel (modules/user_model.py)
    │   ├── analyze_query(query)
    │   ├── Returns: intent, mood, frustration, prompt_injection
    │   └── Builds user profile in data/user_model/profile.json
    │
    └── SelfCorrectionSystem (modules/self_correction.py)
        ├── recognize_correction(query, context)
        ├── Detects "no, I meant...", "actually it's...", etc.
        └── learn_from_mistake() for training data
```

**Key integration points in daemon_runner.py:**
- Line 990-998: Context tracker updates before each query
- Line 1000-1010: User model analysis (intent/mood/frustration detection)
- Line 1012-1032: Self-correction detection and learning
- Line 1097-1099: Query/response storage for future correction detection

**What this enables:**
- NEUTRO adjusts responses based on user frustration level
- Context awareness of current project/task being worked on
- Explicit learning from user corrections ("No, I meant X not Y")

---

## 4. DEAD CODE ANALYSIS

### The "44 Modules" Claim vs Reality

Many NEUTRO docs claim "44 integrated modules." The reality:

| Claim | Reality |
|-------|---------|
| 44 integrated modules | ~45 actually imported |
| All modules active | 197 files never imported |
| Everything connected | Most are standalone experiments |

### Why So Much Dead Code?

1. **Experimental Development:** Many modules were prototypes that never reached integration
2. **Feature Branches Merged:** Code added but never wired up
3. **Alternative Approaches:** Multiple implementations of same concept (e.g., 5 different memory systems)
4. **Research Code:** Academic paper implementations not production-ready

### Modules That Could Be Deleted

Safe to delete (never imported, no tests reference them):
- All `*_old.py` and `*.py.backup` files
- `modules/cognee_memory.py` - Cognee never integrated
- `modules/mem0_integration.py` - Mem0 never integrated
- `modules/pipecat_integration.py` - Pipecat unused
- `modules/claude_teacher.py` - Claude API unused
- Most files with single-digit line counts

---

## 5. WHAT ACTUALLY WORKS (Verified by Testing)

Based on V11.74 interactive testing (11/11 tests passed):

| Feature | Status | Evidence |
|---------|--------|----------|
| Identity awareness | Working | "I am NEUTRO, created by Cez" |
| Memory attribution | Working | "YOUR pet's name is Max" (V11.74) |
| Math reasoning | Working | Solved bat/ball problem correctly |
| Code generation | Working | Correct factorial/recursion |
| Ethical reasoning | Working | Nuanced trolley problem response |
| Self-awareness | Working | Honest limitations assessment |
| Creative writing | Working | Original haiku generated |
| SNN neuron tracking | Working | 800 neurons, births/deaths logged |
| ChromaDB storage | Working | 2099+ memories |
| Background thinking | Working | 534 reflection cycles |

---

## 6. HONEST DIAGRAM

```
                    ┌─────────────────────────────────────────┐
                    │         WHAT NEUTRO ACTUALLY IS         │
                    └─────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────┐
    │                     ACTIVE CORE (~45 modules)                     │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │
    │  │    SOUL     │  │   MEMORY    │  │   SENSES    │               │
    │  │  (5 elem)   │──│  (ChromaDB) │──│  (time/loc) │               │
    │  └─────────────┘  └─────────────┘  └─────────────┘               │
    │         │                │                │                       │
    │         ▼                ▼                ▼                       │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │
    │  │    SNN      │  │   DAEMON    │  │  EMOTIONAL  │               │
    │  │ (800 nrns)  │  │ (bg tasks)  │  │    CORE     │               │
    │  └─────────────┘  └─────────────┘  └─────────────┘               │
    │                                                                   │
    │  Entry: daemon_runner.py → neutro.py → soul.py → Ollama LLM      │
    └───────────────────────────────────────────────────────────────────┘

    ┌───────────────────────────────────────────────────────────────────┐
    │                    DEAD CODE (~197 modules)                       │
    │                                                                   │
    │  Experiments, prototypes, alternative implementations that       │
    │  exist in the codebase but are NEVER imported or executed.       │
    │                                                                   │
    │  Examples: cognee, mem0, pipecat, claude_teacher, dual_brain,    │
    │  global_workspace, physics_engine, 5+ memory systems, etc.       │
    └───────────────────────────────────────────────────────────────────┘
```

---

## Appendix: How to Verify This Analysis

```bash
# Count total module files
ls modules/*.py | wc -l  # → 242

# Find actually imported modules
grep -roh "from modules\.[a-zA-Z_]*" *.py modules/*.py | \
    sed 's/from modules\.//' | sort -u | wc -l  # → ~45

# Trace a query through the code
grep -n "process_with_soul" daemon_runner.py neutro.py

# Check SNN integration
grep -n "soul_snn\|SoulSpikingNetwork" modules/soul.py
```

---

*This document represents the ACTUAL state of NEUTRO as of V11.74, not aspirational documentation.*

*Generated by Claude Code analyzing real imports and execution paths.*
