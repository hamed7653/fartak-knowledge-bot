# Mini Company Knowledge Bot (Fartak Tech)

A lightweight AI-powered CLI assistant that answers employee queries based on internal company documents. Built as a demonstration of AI integration, context management, and project documentation.

## 📁 Project Structure

```text
fartak-knowledge-bot/
├── bot.py                   # Main application (CLI bot)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API Key)
├── README.md                # This file
├── docs/                    # Company knowledge base (plain text)
│   ├── it_support.txt       # IT & Network policies
│   ├── leave_policy.txt     # Employee Leave Policy 
│   └── product_specs.txt    # Services & Product Overview (EPMS)
└── agentic-brain/           # Project context & management docs
    ├── PROJECT_BRIEF.md
    ├── AGENT_CONTEXT.md
    ├── MEMORY.md
    ├── TASKS.md
    └── EVALS.md
    
## Features
- **Dynamic Context Loading:** Reads `.txt` files from the `docs/` directory automatically.
- **Strict Guardrails:** Instructed to avoid hallucinations and only answer based on provided context.
- **Agentic Brain:** Includes a structured `agentic-brain/` directory detailing the project brief, memory, tasks, and evaluations.

## How to Run

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


