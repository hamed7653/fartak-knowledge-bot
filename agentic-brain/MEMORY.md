# Project Memory & Decision Log

## Decisions Made
- **Decision 1:** Chose a Python CLI over a Web App for the MVP. *Reasoning:* Reduces overhead, proves the core concept faster, and minimizes dependency issues for reviewers.
- **Decision 2:** Context Injection via System Prompt. *Reasoning:* For only 3 short files, creating a full RAG pipeline (chunking + embeddings) is over-engineering. Concatenating texts is optimal for this scale.

## Lessons Learned & Adjustments
- *Initial thought:* Allow the AI to use general knowledge if the doc is missing info.
- *Correction:* Strictly prompted the AI to say "I don't have information on that" to prevent hallucinations in a corporate environment.