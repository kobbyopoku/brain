---
type: entity
title: claude-squad
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/smtg-ai/claude-squad
aliases: [cs]
tags: [claude-code, orchestration, multiplexer, stub]
---

# claude-squad

> Terminal multiplexer purpose-built for running multiple Claude Code agents in parallel — each in its own isolated workspace via git worktrees, so agents work on separate branches without conflicts.

## Profile

This page is a **stub**. claude-squad appears in this wiki only via [[wiki/sources/regent0x-claude-code-247-dev-team]], which uses it as the canonical example of [[multi-agent-orchestration]] at the personal scale. The author's nightly workflow: spin up 3 sessions on independent units of work, enable auto-accept (`cs -y`) for trusted tasks, close the laptop, wake to PRs.

## Key facts

- **Repo**: https://github.com/smtg-ai/claude-squad (cited in [[wiki/sources/regent0x-claude-code-247-dev-team]])
- **Install**: `brew install claude-squad`
- **Invoke**: `cs` (interactive TUI) or `cs -y` (auto-accept mode for trusted tasks).
- **Workspace isolation**: git worktrees — each agent on its own branch.
- **Persistence**: closing the terminal does not stop the agents.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]

## Related entities

- [[wiki/entities/claude-flow]] — sibling, enterprise-grade orchestration.
- [[wiki/entities/claude-code]] — the platform.

## Related concepts

- [[multi-agent-orchestration]]
- [[subagents]]
