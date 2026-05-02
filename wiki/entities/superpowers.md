---
type: entity
title: Superpowers
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://github.com/obra/superpowers
aliases: [superpowers plugin]
tags: [claude-code, plugin, skill-collection, workflow]
---

# Superpowers

> A Claude Code plugin that imposes a disciplined development workflow (brainstorm → spec → plan → TDD → implement → review) on the agent — a [[claude-code-skills|skills]] collection rather than a single skill.

## Profile

Superpowers is a Claude Code plugin distributed through the Anthropic plugin marketplace as `superpowers@claude-plugins-official` (per [[wiki/sources/regent0x-claude-code-247-dev-team]]). Instead of letting Claude jump straight into writing code, the plugin enforces a workflow: ask what the user is really trying to build, write a spec for approval, create a plan detailed enough for a junior dev, then execute with test-driven development. In this wiki it appears as the most prominently-named element of [[claude-code-skills]] usage in the wild.

## Key facts

- **Repo**: https://github.com/obra/superpowers (cited in [[wiki/sources/regent0x-claude-code-247-dev-team]])
- **Plugin marketplace install**: `/plugin install superpowers@claude-plugins-official`
- **Claimed star count** (per [[wiki/sources/regent0x-claude-code-247-dev-team]]): 170k+. *(Unverified; treat as the source's claim.)*
- **Workflow imposed**: brainstorm → spec → plan → TDD → implement → review.

## Positions and claims

- **Workflow discipline beats raw code generation.** Forcing the agent through brainstorm-spec-plan-TDD-implement-review produces better software than letting it write code reactively.
- **Plugin marketplace distribution is the right channel for skill collections** at this scale of adoption. *(Implicit by virtue of the marketplace listing.)*

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — first skill plugin recommended; "transforms claude code from 'write code when asked' into a complete development methodology."

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/anthropic]] — operator of the plugin marketplace.

## Related concepts

- [[claude-code-skills]]
- [[markdown-as-agent-contract]]
