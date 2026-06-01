# Task Tracker & Backlog

## ✅ Phase 1: MVP Setup (Completed)
- [x] Establish Git repository, `.gitignore`, and commit naming conventions.
- [x] Create `docs/` directory with dummy corporate data (HR, IT, Product).
- [x] Build the Python CLI (`bot.py`) for dynamic document loading.
- [x] Integrate LLM API and configure system instructions.
- [x] Test network routing (Proxy/VLESS) for API access.
- [x] Refactor code to the latest API SDK (resolve deprecations).
- [x] Setup the `agentic-brain` folder to document meta-context.

## 🔜 Phase 2: Enhancements (Backlog)
- [ ] Add an `--eval` CLI flag to automatically run test cases from `EVALS.md` and output a pass/fail report.
- [ ] Implement chunking and a local VectorDB (e.g., Chroma) for scalable document retrieval.
- [ ] Create a Slack/Discord bot wrapper around the Python logic.
- [ ] Support parsing for `.pdf` and `.docx` file formats.