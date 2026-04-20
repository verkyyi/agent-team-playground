# AGENTS.md

Conventions for agents (human or AI) working on this repo.

## Test command

```bash
pip install -r requirements.txt
pytest
```

`pytest` must pass before any PR.

## Style

- Python 3.11+.
- Match existing formatting (4-space indent, no trailing whitespace).
- Use `snake_case` for functions, `PascalCase` for classes.
- Type hints on public functions.

## Scope

- This repo is a playground for testing agentic workflows, not a real project.
- Make the smallest change that satisfies the issue. Do not refactor surrounding code.
- Do not add new dependencies without a note in the PR body.

## Identity

If you are an AI agent submitting a change, identify yourself clearly in PR body and comments (`🤖 <agent name>`).
