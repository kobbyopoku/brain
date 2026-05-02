---
type: entity
title: tdd-guard
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/nizos/tdd-guard
aliases: []
tags: [claude-code, skill, testing, stub]
---

# tdd-guard

> A Claude Code skill / hook that blocks commits skipping tests — Claude literally cannot ship untested code. When a block fires, the tool explains why and what tests are needed.

## Profile

This page is a **stub**. tdd-guard appears in this wiki only via [[wiki/sources/regent0x-claude-code-247-dev-team]], which positions it as the canonical example of [[claude-code-hooks|hook-enforced]] discipline: instead of asking the agent to write tests, the runtime refuses commits without them. Typically paired with the *tester* role in the [[subagents]] architecture.

## Key facts

- **Repo**: https://github.com/nizos/tdd-guard (cited in [[wiki/sources/regent0x-claude-code-247-dev-team]])
- **Mechanism**: pre-commit gating; coupled with the tester subagent for write-side enforcement.
- **Outputs**: explanation of why the block fired and what tests are needed.

## Positions and claims

- **TDD discipline should be enforced at the runtime**, not at the agent's discretion. *(Implicit in the tool's existence; argued explicitly in [[wiki/sources/regent0x-claude-code-247-dev-team]].)*

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]

## Related entities

- [[wiki/entities/claude-code]] — the platform.

## Related concepts

- [[claude-code-skills]]
- [[claude-code-hooks]]
- [[subagents]] — typically paired with the tester role.
