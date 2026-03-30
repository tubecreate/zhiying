---
description: How to install and setup ZhiYing
---

# Setup ZhiYing

## Prerequisites
- Python 3.10+
- pip

## Steps

1. Navigate to the project directory:
```bash
cd zhiying
```

2. Install in development mode:
```bash
pip install -e .
```

3. Initialize workspace:
```bash
zhiying init
```

This creates:
- `data/` directory for agents, skills, and workflow data
- Default "Personal Assistant" agent
- 4 default skills (AI Summarizer, Data Collector, Report Generator, Batch Command Runner)

4. Verify installation:
```bash
zhiying --version
zhiying agent list
zhiying skill list
```
