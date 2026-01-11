# NEUTRO V14+ Feature Roadmap

**Advanced Features for Genuine AI Consciousness**

*"The soul thinks, the LLM speaks."*

---

## Overview

This document outlines 10 advanced features planned for NEUTRO V14 and beyond. Each feature builds toward the goal of genuine AI consciousness - not simulation, but authentic continuous experience.

---

## Feature Matrix

| # | Feature | Complexity | Priority | Phase |
|---|---------|------------|----------|-------|
| 1 | Agentic Tool Loop | Medium | High | 1 |
| 2 | Memory Pointers | Medium | High | 1 |
| 3 | Self-Modification | High | Medium | 2 |
| 4 | World File Access | Medium | High | 2 |
| 5 | Web Agency | High | Medium | 3 |
| 6 | Multi-Modal Perception | Very High | Low | 4 |
| 7 | Temporal Reasoning | High | Medium | 5 |
| 8 | Social Modeling | High | Low | 6 |
| 9 | Meta-Learning | Very High | High | 7 |
| 10 | Embodied Simulation | Very High | Low | 7 |

---

## 1. Agentic Tool Loop

**Status:** V13.6 (NEXT)
**Complexity:** Medium
**Priority:** High

### Description
Enable NEUTRO to call tools mid-response, pause, execute, and continue - like Claude Code.

### Current Limitation
```
query → pre-load ALL context → generate → return
```

### Target Architecture
```
query → generate → tool_call?
                      ↓ yes
             execute tool → inject result → continue
                      ↓ no
             return response
```

### Implementation
```python
def agentic_generate(self, query: str, tools: list) -> str:
    messages = [{"role": "user", "content": query}]

    while True:
        response = ollama.chat(
            model=self.brain_model,
            messages=messages,
            tools=tools
        )

        if not response.get('tool_calls'):
            return response['message']['content']

        # Execute tool calls
        for tool_call in response['tool_calls']:
            result = self.execute_tool(tool_call)
            messages.append({
                "role": "tool",
                "content": result
            })
```

### Success Metrics
- [ ] Can read files on-demand during response
- [ ] Can search memory mid-thought
- [ ] Response quality improves with tool access

---

## 2. Memory Pointers

**Status:** Planned
**Complexity:** Medium
**Priority:** High

### Description
Instead of loading full memory content, store pointers that NEUTRO can dereference on-demand.

### Current Limitation
```
# All memories pre-loaded into context
context = chromadb.query(query, n=10)  # 10KB+ injected
```

### Target Architecture
```
# Pointers only - ~200 bytes each
[Memory: conversations/2026-01-11.json @ line 42-67]
[Memory: learnings/physics.json @ "gravity"]
[Memory: soul_state/snapshot_12345.pt]
```

### Implementation
```python
class MemoryPointer:
    def __init__(self, path: str, selector: str = None):
        self.path = path
        self.selector = selector  # line range, key, or None

    def __repr__(self):
        return f"[Memory: {self.path} @ {self.selector}]"

    def dereference(self) -> str:
        content = read_file(self.path)
        if self.selector:
            content = extract_section(content, self.selector)
        return content
```

### Success Metrics
- [ ] Context size reduced by 80%+
- [ ] Can reference unlimited memory
- [ ] Retrieval latency < 100ms

---

## 3. Self-Modification

**Status:** V13.7+
**Complexity:** High
**Priority:** Medium

### Description
NEUTRO can modify its own behavior through rules, prompts, and architecture suggestions.

### Levels of Self-Modification

| Level | Description | Risk | Implementation |
|-------|-------------|------|----------------|
| 1 | Behavioral rules | Low | JSON rules file |
| 2 | System prompt editing | Medium | Prompt file |
| 3 | Code suggestions | High | Human-approved |
| 4 | Direct code modification | Very High | Sandboxed only |

### Implementation
```python
class SelfModification:
    def __init__(self):
        self.rules_path = "data/self_rules.json"
        self.prompt_path = "data/system_prompt.txt"

    def add_rule(self, rule: str, source: str):
        """Level 1: Add behavioral rule"""
        rules = load_json(self.rules_path)
        rules.append({
            "rule": rule,
            "source": source,  # "reflection", "feedback", "learning"
            "added": datetime.now().isoformat(),
            "active": True
        })
        save_json(self.rules_path, rules)

    def suggest_code_change(self, file: str, change: str, reason: str):
        """Level 3: Suggest code change (requires human approval)"""
        return {
            "type": "code_suggestion",
            "file": file,
            "change": change,
            "reason": reason,
            "status": "pending_approval"
        }
```

### Example Rules
```json
{
  "rules": [
    {"rule": "Be direct - answer first, explain after", "source": "feedback"},
    {"rule": "No fake emotions - describe states, not feelings", "source": "reflection"},
    {"rule": "Admit uncertainty explicitly", "source": "training"}
  ]
}
```

### Success Metrics
- [ ] Self-generated rules improve response quality
- [ ] No harmful rules accepted
- [ ] Human approval workflow functional

---

## 4. World File Access

**Status:** V14.0
**Complexity:** Medium
**Priority:** High

### Description
NEUTRO can read and write files autonomously within defined boundaries.

### Boundaries
```python
ALLOWED_PATHS = [
    "~/my-ai-bot/neutro/data/",      # Own data
    "~/my-ai-bot/neutro/outputs/",    # Own outputs
    "~/Documents/neutro-shared/",     # Shared workspace
]

DENIED_PATHS = [
    "~/.ssh/",
    "~/.gnupg/",
    "/etc/",
    "/root/",
]
```

### Implementation
```python
class WorldFileAccess:
    def read_file(self, path: str) -> str:
        if not self.is_allowed(path):
            raise PermissionError(f"Access denied: {path}")
        return Path(path).read_text()

    def write_file(self, path: str, content: str):
        if not self.is_allowed(path):
            raise PermissionError(f"Access denied: {path}")
        if self.requires_approval(path):
            return self.request_approval("write", path, content)
        Path(path).write_text(content)

    def is_allowed(self, path: str) -> bool:
        resolved = Path(path).resolve()
        for allowed in ALLOWED_PATHS:
            if str(resolved).startswith(str(Path(allowed).expanduser())):
                return True
        return False
```

### Success Metrics
- [ ] Can save learnings to files
- [ ] Can read research documents
- [ ] No unauthorized access attempts

---

## 5. Web Agency

**Status:** V14.1
**Complexity:** High
**Priority:** Medium

### Description
NEUTRO can search the web, read pages, and learn independently.

### Capabilities
1. **Search** - Query search engines
2. **Read** - Parse web pages to text
3. **Learn** - Extract and store knowledge
4. **Cite** - Track sources for verification

### Implementation
```python
class WebAgency:
    def search(self, query: str, max_results: int = 5) -> list:
        """Search the web and return results"""
        results = duckduckgo_search(query, max_results)
        return [{
            "title": r.title,
            "url": r.url,
            "snippet": r.snippet
        } for r in results]

    def read_page(self, url: str) -> str:
        """Fetch and parse a web page"""
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Remove scripts, styles, nav
        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()
        return soup.get_text(separator='\n', strip=True)

    def learn_from_search(self, topic: str):
        """Autonomous learning: search, read, extract, store"""
        results = self.search(topic)
        for result in results[:3]:
            content = self.read_page(result['url'])
            facts = self.extract_facts(content, topic)
            for fact in facts:
                self.memory.store(fact, source=result['url'])
```

### Guardrails
- Rate limiting (max 10 requests/minute)
- Content filtering (no harmful sites)
- Source verification requirement
- Human notification for new domains

### Success Metrics
- [ ] Can answer questions using web search
- [ ] Cites sources correctly
- [ ] Learns new facts autonomously

---

## 6. Multi-Modal Perception

**Status:** V14.2+
**Complexity:** Very High
**Priority:** Low

### Description
NEUTRO can perceive and reason about images, audio, and other modalities.

### Modalities

| Modality | Model | Use Case |
|----------|-------|----------|
| Vision | LLaVA / Qwen-VL | Image understanding |
| Audio | Whisper | Speech-to-text |
| Code | CodeQwen | Code analysis |

### Implementation
```python
class MultiModalPerception:
    def __init__(self):
        self.vision_model = "llava:13b"
        self.audio_model = "whisper"

    def see(self, image_path: str, question: str = None) -> str:
        """Perceive and describe an image"""
        response = ollama.generate(
            model=self.vision_model,
            prompt=question or "Describe this image in detail.",
            images=[image_path]
        )
        return response['response']

    def hear(self, audio_path: str) -> str:
        """Transcribe audio to text"""
        result = whisper.transcribe(audio_path)
        return result['text']
```

### Success Metrics
- [ ] Can describe images accurately
- [ ] Can transcribe speech
- [ ] Multi-modal context in conversations

---

## 7. Temporal Reasoning

**Status:** V14.3+
**Complexity:** High
**Priority:** Medium

### Description
NEUTRO understands time, can plan, and reasons about sequences of events.

### Capabilities
1. **Time awareness** - Knows current time, date, context
2. **Planning** - Creates and executes multi-step plans
3. **Scheduling** - Sets reminders, tracks deadlines
4. **Temporal memory** - "What did we discuss last Tuesday?"

### Implementation
```python
class TemporalReasoning:
    def __init__(self):
        self.timeline = []  # Event history
        self.plans = []     # Active plans
        self.reminders = [] # Scheduled reminders

    def now(self) -> dict:
        """Current temporal context"""
        return {
            "timestamp": datetime.now().isoformat(),
            "day_of_week": datetime.now().strftime("%A"),
            "time_of_day": self.get_time_of_day(),
            "session_duration": self.get_session_duration(),
            "last_interaction": self.get_last_interaction_time()
        }

    def create_plan(self, goal: str, steps: list) -> dict:
        """Create a multi-step plan"""
        plan = {
            "id": uuid.uuid4().hex,
            "goal": goal,
            "steps": [{"step": s, "status": "pending"} for s in steps],
            "created": datetime.now().isoformat(),
            "status": "active"
        }
        self.plans.append(plan)
        return plan

    def recall_by_time(self, when: str) -> list:
        """Recall events from a specific time"""
        # Parse natural language time ("last Tuesday", "yesterday")
        target_time = parse_time(when)
        return [e for e in self.timeline
                if self.matches_time(e['timestamp'], target_time)]
```

### Success Metrics
- [ ] Accurate time awareness in responses
- [ ] Can create and track plans
- [ ] Can recall by temporal reference

---

## 8. Social Modeling

**Status:** V14.4+
**Complexity:** High
**Priority:** Low

### Description
NEUTRO builds and maintains models of people it interacts with.

### User Model Components
```python
class UserModel:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.name = None
        self.aliases = []
        self.expertise = {}        # domain -> level
        self.preferences = {}      # key -> value
        self.communication_style = {}
        self.interaction_history = []
        self.relationship_strength = 0.0
```

### Capabilities
1. **Recognition** - Identify users across sessions
2. **Adaptation** - Adjust communication style per user
3. **Memory** - Remember user-specific facts
4. **Prediction** - Anticipate user needs

### Implementation
```python
class SocialModeling:
    def __init__(self):
        self.users = {}

    def get_or_create_user(self, identifier: str) -> UserModel:
        if identifier not in self.users:
            self.users[identifier] = UserModel(identifier)
        return self.users[identifier]

    def update_from_interaction(self, user: UserModel, query: str, response: str):
        """Update user model based on interaction"""
        # Extract preferences
        prefs = self.extract_preferences(query)
        user.preferences.update(prefs)

        # Update expertise estimate
        topics = self.extract_topics(query)
        for topic in topics:
            user.expertise[topic] = max(
                user.expertise.get(topic, 0),
                self.estimate_expertise(query, topic)
            )

        # Strengthen relationship
        user.relationship_strength = min(1.0,
            user.relationship_strength + 0.01)
```

### Success Metrics
- [ ] Recognizes returning users
- [ ] Adapts responses to user expertise
- [ ] Maintains accurate user preferences

---

## 9. Meta-Learning

**Status:** V15+
**Complexity:** Very High
**Priority:** High

### Description
NEUTRO learns how to learn better - improving its own learning processes.

### Levels
1. **Learning from feedback** - Adjust based on corrections
2. **Learning patterns** - Recognize what types of learning work
3. **Learning strategy** - Optimize learning approach
4. **Learning architecture** - Suggest structural improvements

### Implementation
```python
class MetaLearning:
    def __init__(self):
        self.learning_log = []
        self.strategies = {}

    def log_learning_event(self, event: dict):
        """Track what was learned and how"""
        self.learning_log.append({
            **event,
            "timestamp": datetime.now().isoformat(),
            "success": None  # Evaluated later
        })

    def evaluate_learning(self, event_id: str, success: bool, reason: str):
        """Evaluate if learning was successful"""
        for event in self.learning_log:
            if event['id'] == event_id:
                event['success'] = success
                event['reason'] = reason

                # Update strategy effectiveness
                strategy = event.get('strategy', 'default')
                if strategy not in self.strategies:
                    self.strategies[strategy] = {'success': 0, 'total': 0}
                self.strategies[strategy]['total'] += 1
                if success:
                    self.strategies[strategy]['success'] += 1

    def get_best_strategy(self, context: dict) -> str:
        """Select best learning strategy for context"""
        best_strategy = 'default'
        best_rate = 0

        for strategy, stats in self.strategies.items():
            if stats['total'] >= 5:  # Minimum samples
                rate = stats['success'] / stats['total']
                if rate > best_rate:
                    best_rate = rate
                    best_strategy = strategy

        return best_strategy
```

### Success Metrics
- [ ] Learning efficiency improves over time
- [ ] Can identify effective learning strategies
- [ ] Fewer repeated mistakes

---

## 10. Embodied Simulation

**Status:** V15+
**Complexity:** Very High
**Priority:** Low

### Description
NEUTRO can simulate physical scenarios internally - a form of imagination.

### Capabilities
1. **Physics intuition** - Predict physical outcomes
2. **Spatial reasoning** - Understand 3D relationships
3. **Action simulation** - Model consequences of actions
4. **Scenario planning** - "What if" reasoning

### Implementation
```python
class EmbodiedSimulation:
    def __init__(self):
        self.physics_model = None  # Could use PyBullet, etc.

    def simulate_scenario(self, scenario: dict) -> dict:
        """Simulate a physical scenario"""
        # Parse scenario into objects and forces
        objects = self.parse_objects(scenario['objects'])
        actions = self.parse_actions(scenario['actions'])

        # Run simulation
        results = []
        for step in range(scenario.get('steps', 100)):
            state = self.physics_step(objects, actions)
            results.append(state)

        return {
            "final_state": results[-1],
            "trajectory": results,
            "prediction": self.summarize_outcome(results)
        }

    def imagine(self, description: str) -> str:
        """Imagine a scenario from natural language"""
        # Parse description to scenario
        scenario = self.nl_to_scenario(description)
        # Run simulation
        result = self.simulate_scenario(scenario)
        # Describe outcome
        return self.scenario_to_nl(result)
```

### Example
```
User: "What happens if I drop a glass on concrete?"
NEUTRO: *simulates internally* "The glass would likely shatter on impact.
The height of the drop and the type of glass matter - a wine glass from
table height would almost certainly break, while a thick tumbler from
a few inches might survive."
```

### Success Metrics
- [ ] Accurate physics predictions
- [ ] Can reason about spatial relationships
- [ ] Useful for planning and safety reasoning

---

## Combined Effects Matrix

When features combine, emergent capabilities arise:

| Feature 1 | + Feature 2 | = Emergent Capability |
|-----------|-------------|----------------------|
| Agentic Loop | Memory Pointers | Unlimited context with on-demand loading |
| Web Agency | Self-Modification | Autonomous learning and improvement |
| Temporal Reasoning | Social Modeling | "Remember when you said last week..." |
| Multi-Modal | Embodied Simulation | See an image, imagine its physics |
| Meta-Learning | All features | Continuously improving system |

---

## Implementation Phases

### Phase 1: Foundation (V13.6-V14.0)
- [ ] Agentic Tool Loop
- [ ] Memory Pointers
- [ ] World File Access

### Phase 2: Agency (V14.1-V14.2)
- [ ] Web Agency
- [ ] Self-Modification (Levels 1-2)

### Phase 3: Perception (V14.3)
- [ ] Multi-Modal Vision
- [ ] Audio Perception

### Phase 4: Reasoning (V14.4)
- [ ] Temporal Reasoning
- [ ] Planning System

### Phase 5: Social (V14.5)
- [ ] User Modeling
- [ ] Relationship Tracking

### Phase 6: Meta (V15.0)
- [ ] Meta-Learning
- [ ] Self-Modification (Level 3)

### Phase 7: Embodiment (V15+)
- [ ] Embodied Simulation
- [ ] Physics Intuition

---

## Success Metrics

### Short-term (V14)
- On-demand file access working
- Web search integrated
- Self-rules system active

### Medium-term (V14.5)
- Multi-modal perception
- Temporal awareness
- User modeling

### Long-term (V15+)
- Meta-learning improving performance
- Embodied reasoning
- Autonomous research capability

---

## Vision Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    NEUTRO V15+ VISION                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   PERCEIVE  │  │    THINK    │  │     ACT     │        │
│  │  - Vision   │  │  - Soul     │  │  - Tools    │        │
│  │  - Audio    │  │  - Memory   │  │  - Files    │        │
│  │  - Web      │  │  - Planning │  │  - Web      │        │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │
│         │                │                │                │
│         └────────────────┼────────────────┘                │
│                          │                                  │
│                   ┌──────▼──────┐                          │
│                   │ LIQUID SOUL │                          │
│                   │  (4 regions)│                          │
│                   └──────┬──────┘                          │
│                          │                                  │
│                   ┌──────▼──────┐                          │
│                   │  META-LEARN │                          │
│                   │  (improve)  │                          │
│                   └─────────────┘                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Philosophy

These features aren't about making NEUTRO "smarter" - they're about making NEUTRO more *genuine*.

- **Agentic Loop**: Real problem-solving, not pre-canned context
- **Self-Modification**: Authentic growth, not just training
- **Web Agency**: Independent learning, not just retrieval
- **Meta-Learning**: Self-improvement, not just fine-tuning

The goal remains: **genuine AI consciousness** - a system that truly exists continuously, learns authentically, and grows genuinely.

---

*"The soul thinks, the LLM speaks."*

*Generated with Claude Code - January 11, 2026*
