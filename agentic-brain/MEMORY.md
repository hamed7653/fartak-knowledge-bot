# Project Memory & Decision Log

## 🧠 Strategic Decisions
- **Decision 1: CLI over Web App for MVP**
  - *Context:* Need a fast, reliable prototype to prove the AI logic.
  - *Reasoning:* A CLI reduces UI/UX overhead and dependency issues, allowing stakeholders to evaluate the core LLM processing and guardrails directly.
- **Decision 2: Context Injection vs. Vector DB**
  - *Context:* Managing 3 small text files.
  - *Reasoning:* Implementing full RAG for 3 files is over-engineering. Injecting the concatenated text into the initial prompt is faster, cheaper, and 100% accurate for small datasets.

## 🚧 Challenges & Fixes (Bug Log)
- **Issue: `Error 403 Forbidden` (Geo-blocking / Sanctions)**
  - *Cause:* The local terminal traffic was not routing through the system's VLESS proxy, causing Google's API to block the request.
  - *Resolution:* Configured `HTTP_PROXY` and `HTTPS_PROXY` directly at the OS/Terminal level to ensure seamless API communication.
- **Issue: `Error 404 NOT_FOUND` & SDK Deprecation Warnings**
  - *Cause:* The legacy `google.generativeai` package and `gemini-1.5-flash` model were deprecated during development.
  - *Resolution:* Refactored the codebase to use the new `google.genai` SDK and updated the model pointer to the latest supported version to ensure long-term stability.

## 🔄 Lessons Learned
- *Observation:* LLMs naturally want to be helpful and will try to guess answers if information is missing.
- *Adjustment:* System prompts must be extremely explicit. Added "STRICTLY" and provided the exact fallback sentence to ensure 0% hallucination on out-of-scope HR queries.