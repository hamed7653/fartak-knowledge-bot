# Project Brief: Mini Company Knowledge Bot

## Objective
Create a lightweight, locally-runnable knowledge base assistant (MVP) that allows employees to query internal company documents naturally.

## Architecture
- **Knowledge Base:** Text files located in the `docs/` directory.
- **Interface:** Command Line Interface (CLI) built with Python.
- **Engine:** LLM API (acting as the reasoning engine to extract and synthesize answers).

## Success Criteria
- The bot correctly answers questions strictly based on the provided files.
- The system handles missing information gracefully (hallucination prevention).