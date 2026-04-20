# Security policy

This repo is a public testing playground for the [agent-team](https://github.com/verkyyi/github-agent-runner/tree/main/catalog/agent-team) pattern. Its purpose is to dogfood agentic workflows; it isn't production software.

## Reporting

Please email **verky.yi@gmail.com** for anything security-relevant. Do **not** open a public issue for security reports.

In scope:

- Ways a fork PR or outside contributor could gain access to the repo's Actions secrets (notably `CLAUDE_CODE_OAUTH_TOKEN`).
- Ways to trigger the agent-team pipeline without write access to this repo.
- Anything that would exfiltrate secrets from workflow logs or artifacts.

Out of scope:

- The bugs intentionally seeded in `src/` for agents to fix.
- The agents themselves opening PRs with questionable code — that's expected behavior; a human reviewer gates every merge.
- Token-cost concerns from abusive labeling — only collaborators with write access can label issues, so this reduces to "trust your collaborators."

## Related

Upstream plugin: [verkyyi/github-agent-runner](https://github.com/verkyyi/github-agent-runner). Issues with the agent-team pattern itself (not this playground's specific state) belong there.
