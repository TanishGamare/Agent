# Agents

A collection of lightweight terminal-based agents powered by OpenRouter.

## Setup

1. Clone the repo and create a virtual environment
2. Install dependencies with `pip install openai` or You can use uv too.
3. Create a `.env` file in the project root and add your key:


## Agents

### mini_claude_code
A minimal agent that can only read files. Good for quick file inspection and summarization tasks.

```bash
python mini_claude_code.py
```

### claude_agent
A full-featured coding agent that can list files, read and write files, and run shell commands — all driven by a language model using tool calling.

```bash
python claude_agent.py
```

Type your task in plain English and the agent will figure out what tools to use. Type `exit` or `quit` to stop.

## Model

Both agents use `nvidia/nemotron-3.5-lightning:free` via OpenRouter by default. Change the `MODEL` variable in either script to swap models.
