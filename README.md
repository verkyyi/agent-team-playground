# agent-team-playground

Long-lasting dogfooding ground for the [agent-team](https://github.com/verkyyi/github-agent-runner/tree/main/catalog/agent-team) pattern and other workflows shipped by [github-agent-runner](https://github.com/verkyyi/github-agent-runner).

Everything here is disposable. Code is intentionally simple so the agents have room to do real work without tripping over real-project complexity.

## Layout

```
src/
  greet.py          toy module — bugs to find, features to add
tests/
  test_greet.py     pytest scaffold
.github/
  workflows/
    ci.yml          runs pytest on every PR (so the reviewer has CI signal)
    *.lock.yml      installed agent-team workflows (via /install-agent-team)
```

## How to dispatch a task

1. Open an issue describing a change you want.
2. Add the `agent-team` label.
3. Watch the spec → plan → impl → review thread; merge the approved PR.

Full pattern docs: [catalog/agent-team/README.md](https://github.com/verkyyi/github-agent-runner/blob/main/catalog/agent-team/README.md).
