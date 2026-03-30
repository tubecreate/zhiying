# Ollama Local Model Manager — AI Skill Guide

## Extension: ollama
Manages local Ollama AI models for agents to use without cloud API keys.

## Available Commands

### Server Status
```
zhiying ollama status
```

### List Models
```
zhiying ollama models
```

### Pull Model
```
zhiying ollama pull qwen:latest
zhiying ollama pull llama3:8b
zhiying ollama pull gemma2:9b
```

### Remove Model
```
zhiying ollama remove qwen:latest
```

### Show Model Details
```
zhiying ollama show qwen:latest
```

### List Running Models
```
zhiying ollama running
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/ollama/status` | Server status |
| GET | `/api/v1/ollama/models` | List models |
| GET | `/api/v1/ollama/running` | List loaded models |
| POST | `/api/v1/ollama/pull` | Pull model |
| DELETE | `/api/v1/ollama/models` | Remove model |
| GET | `/api/v1/ollama/models/{name}` | Model details |
| POST | `/api/v1/ollama/assign` | Assign model to agent |

## AI Usage
1. Check if Ollama is running: `GET /api/v1/ollama/status`
2. List available models: `GET /api/v1/ollama/models`
3. If needed model not installed, pull it: `POST /api/v1/ollama/pull {"model": "qwen:latest"}`
4. Assign to agent: `POST /api/v1/ollama/assign {"agent_id": "...", "model": "qwen:latest"}`
