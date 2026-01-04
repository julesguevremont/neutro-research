# NEUTRO Daemon API Reference

**Base URL:** `http://127.0.0.1:5555`

## Quick Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/query` | POST | Send a message to NEUTRO |
| `/status` | GET | Get daemon status and stats |
| `/introspect` | GET | Get detailed internal state |
| `/dreams` | GET | Get dream processing stats |
| `/dream` | POST | Trigger a dream cycle |
| `/correct` | POST | Submit a correction for learning |
| `/clear_session` | POST | Clear current conversation session |

---

## Endpoints

### POST /query

Send a message to NEUTRO and get a response.

**Request:**
```bash
curl -s -X POST http://127.0.0.1:5555/query \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?"}'
```

**Request Body:**
```json
{
  "text": "Your message here"
}
```

**Response:**
```json
{
  "response": "I'm doing well, thanks for asking!",
  "elapsed": 13.05,
  "query_count": 1,
  "self_corrected": false
}
```

**Note:** Use pipe input for reliable JSON handling:
```bash
echo '{"text":"Hello!"}' | curl -s -X POST http://127.0.0.1:5555/query \
  -H "Content-Type: application/json" -d @-
```

---

### GET /status

Get current daemon status and statistics.

**Request:**
```bash
curl -s http://127.0.0.1:5555/status
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `state` | string | Current state: IDLE, THINKING, DREAMING, RESPONDING |
| `uptime` | string | Time since daemon start (e.g., "0h 7m") |
| `idle_seconds` | int | Seconds since last activity |
| `query_count` | int | Total queries processed |
| `thoughts_generated` | int | Number of autonomous thoughts |
| `dream_count` | int | Number of dream cycles completed |
| `continuous_processing` | object | Sleep cycle stats |

---

### GET /introspect

Get detailed internal state including consciousness metrics.

**Request:**
```bash
curl -s http://127.0.0.1:5555/introspect
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `soul` | object | Consciousness level and factors |
| `snn` | object | Spiking Neural Network stats |
| `memory` | object | Memory system stats |
| `qlora` | object | QLoRA learning buffer |
| `models` | object | Model configuration |
| `prompts` | object | Prompt pipeline config |
| `personality` | object | Loaded personality |
| `metacognition` | object | Self-evaluation stats |

**Example - Get consciousness level:**
```bash
curl -s http://127.0.0.1:5555/introspect | \
  python3 -c "import sys,json; d=json.load(sys.stdin); \
  print(f'Consciousness: {d[\"soul\"][\"consciousness_level\"]*100:.1f}%')"
```

---

### GET /dreams

Get dream processing statistics.

**Request:**
```bash
curl -s http://127.0.0.1:5555/dreams
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `mode` | string | Current dream mode |
| `stats` | object | Dream cycle statistics |
| `light_cycles` | int | Light sleep cycles completed |
| `medium_cycles` | int | Medium sleep cycles completed |
| `deep_cycles` | int | Deep sleep cycles completed |
| `rem_cycles` | int | REM cycles completed |

---

### POST /dream

Manually trigger a dream cycle.

**Request:**
```bash
curl -s -X POST http://127.0.0.1:5555/dream \
  -H "Content-Type: application/json" \
  -d '{"mode": "medium"}'
```

**Modes:** `light`, `medium`, `deep`, `rem`

---

### POST /correct

Submit a correction for NEUTRO to learn from.

**Request:**
```bash
curl -s -X POST http://127.0.0.1:5555/correct \
  -H "Content-Type: application/json" \
  -d '{"query": "original question", "correction": "correct answer"}'
```

---

### POST /clear_session

Clear the current conversation session.

**Request:**
```bash
curl -s -X POST http://127.0.0.1:5555/clear_session
```

---

## Common Usage Patterns

### Check if daemon is running
```bash
curl -s http://127.0.0.1:5555/status 2>/dev/null | \
  python3 -c "import sys,json; d=json.load(sys.stdin); \
  print(f'State: {d[\"state\"]}')" 2>/dev/null || echo "Not running"
```

### Get memory stats
```bash
curl -s http://127.0.0.1:5555/introspect | \
  python3 -c "import sys,json; d=json.load(sys.stdin); \
  m=d['memory']; print(f'Chroma: {m.get(\"chroma_count\",0)}')"
```

### Monitor in real-time
```bash
./monitor.sh
```

---

## Error Responses

| Error | Cause |
|-------|-------|
| `{"error": "Invalid JSON"}` | Malformed JSON in request body |
| `{"error": "Unknown endpoint"}` | Incorrect URL path |
| Connection refused | Daemon not running |

---

## Starting the Daemon

```bash
# From neutro directory
python3 daemon_runner.py

# Or use control script
./scripts/daemon_control.sh start
```

**Log files:**
- `/tmp/neutro_v11.26.log` - Current daemon log
- `data/daemon/daemon.log` - Persistent daemon log
- `data/daemon/thoughts/*.jsonl` - Generated thoughts
