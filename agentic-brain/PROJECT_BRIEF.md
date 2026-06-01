# Project Brief: Mini Company Knowledge Bot

## 🎯 Objective
Create a lightweight, locally-runnable knowledge base assistant (MVP) that allows internal employees of Fartak Tech to query company documents using natural language. The system must eliminate search friction while maintaining strict corporate data guardrails.

## 📦 MVP Scope (Minimum Viable Product)
- **Knowledge Source:** Static `.txt` files in a local `docs/` directory.
- **Interface:** Interactive Command Line Interface (CLI).
- **Core Engine:** Google Gemini API (v2.5 Flash) functioning as the reasoning and extraction engine.
- **Context Handling:** In-memory concatenation of text files injected dynamically into the system prompt.

## 🚀 Success Criteria
1. **Accuracy:** The bot must answer queries *strictly* based on the provided documents.
2. **Zero Hallucination:** If a query falls outside the provided documents, the bot must gracefully decline to answer rather than fabricating information.
3. **Resilience:** The CLI must handle API network restrictions and SDK deprecations seamlessly.