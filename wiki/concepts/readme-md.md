---
type: concept
title: README.md
created: 2026-05-02
updated: 2026-05-02
aliases: [readme.md, README]
tags: [agent-config, markdown, stub]
---

# README.md

> The original convention — a markdown file at the root of a project that orients human readers — increasingly read by AI agents as part of their default project context.

## Definition

This page is a **stub**. README.md is the oldest and most widely adopted markdown convention; it predates AI agents by decades. It is included in this wiki because [[markdown-as-agent-contract]] argues that README.md is being **re-purposed** as part of the agent-contract family: agents now read README.md alongside [[CLAUDE]] / [[agents-md]] when establishing context for a project. The wiki has not yet ingested a primary source theorizing this re-purposing, so the page only captures what neighboring pages say.

## Treatment across sources

- [[wiki/concepts/markdown-as-agent-contract]] — lists README.md as part of the meta-pattern: "older convention, but increasingly read by agents as part of their context."

## Sub-claims and details

- **Origin**: a long-standing software convention for orienting *humans* to a project. Predates LLMs.
- **Re-purposing**: when an agent enters an unfamiliar project, README.md is often the first file it reads. This puts implicit pressure on README.md to serve dual audiences (humans and agents) — a tension that newer agent-specific files (CLAUDE.md, AGENTS.md) sidestep.
- Belongs to the [[markdown-as-agent-contract]] family alongside [[CLAUDE]], [[agents-md]], [[design-md]], [[skill-md]].

## Open questions and contradictions

- **Tension with newer agent files**: as more projects ship a `CLAUDE.md` or `AGENTS.md`, what's left for README.md? Possibly a clean split — README.md for humans, CLAUDE.md for agents. Possibly a converged "longer-form orientation" with both audiences in mind. Unsourced here.
- **No primary source yet** theorizing the re-purposing claim.

## Related concepts

- [[markdown-as-agent-contract]] — the meta-pattern README.md is being absorbed into.
- [[agents-md]] — newer agent-specific sibling.

## Mentioned in

- [[wiki/concepts/markdown-as-agent-contract]]
