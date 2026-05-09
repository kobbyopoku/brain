---
type: entity
title: ECC
entity_type: product
created: 2026-05-08
updated: 2026-05-08
website: ""
aliases: []
tags: [claude-code, agent-harness, ai-tooling, hackathon-project, agent-shield, skill-marketplace-security, stub]
---

# ECC

> Hackathon-winning Claude Code automation tool surfaced via [[wiki/sources/noisyb0y1-x-2044692412061425748|noisyb0y1's reveal]]: **38 specialized agents + 156 skills + 72 commands**, plus an **AgentShield** security component (1,282 tests + 102 security rules). Notable for shipping with **persistent agent "instincts"** that learn user coding style across 2-3 weeks — a fresh implementation of the [[self-annealing|self-annealing]] / [[hot-cache|hot-cache]] / [[wiki/entities/hermes-agent|Hermes]] persistent-memory family.

## Profile

This page is a **stub**. ECC appears via noisyb0y1's surfacing thread. The repo URL was not retrieved in the content captured by twitter-thread.com — worth following up. *"ECC"* is the project name as cited; full expansion uncertain.

## Key facts

- **Components**:
  - **38 specialized agents** with a *Planner* coordinator.
  - **156 skills**.
  - **72 commands**.
  - **AgentShield** security: 1,282 tests + 102 security rules for auditing agent configurations.
  - **Persistent "instincts"**: cross-session learning of user coding style and conventions over 2-3 weeks.
- **Language coverage**: 12 ecosystems including TypeScript, Python, Go, Rust.
- **Performance claim**: completes day-long junior-developer tasks in 20-40 minutes (per author).
- **Cost claim**: replaces $8K-$15K/month dev teams at $20/month substrate cost.

## Notable claim that promotes a new wiki concern

> *"12% of skills on one marketplace were malware as of January 2026."* — this is a specific empirical claim about agent-tooling security worth tracking. AgentShield is the first wiki-documented tool that audits skill marketplaces for malicious patterns. Worth promoting **skill-marketplace-security** as a future wiki concept.

## Mentioned in

- [[wiki/sources/noisyb0y1-x-2044692412061425748]] — canonical wiki source (noisyb0y1 reveal).

## Related entities

- [[wiki/entities/noisyb0y1]] — surfacing author.
- [[wiki/entities/claude-code]] — substrate.
- [[wiki/entities/claude-mem]] — recommended companion (cross-session memory).
- [[wiki/entities/superpowers]] — recommended companion (structured planning).
- [[wiki/entities/trail-of-bits-claude-code-skills]] — adjacent security tool (skills *about* security; ECC's AgentShield is auditor *of* skills).

## Related concepts

- [[claude-code-skills]] — ECC ships 156; AgentShield audits them.
- [[self-annealing]] — ECC's "instincts" is a fresh mechanism in this family.
- [[hot-cache]] — adjacent.
- [[multi-agent-orchestration]] — Planner agent coordinates 38 specialists.
- [[anti-ai-slop-machinery]] — adjacent (AgentShield is security-side; anti-slop is quality-side).
- [[markdown-as-agent-contract]] — `CLAUDE.md` rules are part of ECC's recommended companion stack.
