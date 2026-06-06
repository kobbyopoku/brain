---
type: concept
title: SOUL.md (agent identity file)
created: 2026-06-06
updated: 2026-06-06
aliases: [SOUL.md, soul file, agent identity file, persona file]
tags: [agent-architecture, claude-code, agent-identity, markdown-contract]
---

# SOUL.md (agent identity file)

> A markdown file that holds an agent's stable identity — personality, tone, communication style, and hard limits — and is injected into the system prompt so everything the agent does passes through it.

## Definition

`SOUL.md` is the identity slot of an agent's configuration: a markdown file describing *who the agent is* rather than *what it knows* or *what it can do*. In the Hermes agent it is "slot #1" of the `~/.hermes` folder — the system-prompt file that fixes personality, tone, communication style, and hard limits. It is a persona-as-contract variant of [[markdown-as-agent-contract]]: where most agent-contract files encode knowledge or capabilities, `SOUL.md` encodes identity.

## Why it matters

Separating identity (`SOUL.md`) from knowledge (`MEMORY.md`) and the user model (`USER.md`) makes an agent's persona an editable, version-controllable artifact rather than something diffused through prompts. Because everything the agent writes and remembers passes through the identity file, it functions as a governing layer over the rest of the agent's behavior — the place where tone and hard limits are set once and inherited everywhere.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] frames it as Hermes's slot-#1 system-prompt identity file — personality, tone, communication style, and hard limits — and notes that everything the agent writes and remembers passes through it. A persona-as-contract instance of [[markdown-as-agent-contract]].

## Sub-claims and details

- In Hermes, `SOUL.md` is the system-prompt identity file (slot #1). [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- It encodes personality, tone, communication style, and hard limits. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- Everything the agent writes and remembers passes through it. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- It sits alongside `MEMORY.md` (knowledge) and `USER.md` (user model) as the identity portion of the Hermes contract. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]

## Open questions and contradictions

- How `SOUL.md` interacts with conflicting instructions in memory or skills (precedence) is not specified by the source.

## Related concepts

- [[markdown-as-agent-contract]] — broader pattern; `SOUL.md` is the persona-as-contract variant.
- [[agents-md]] — sibling agent-configuration markdown file.
- [[persona-consistency]] — the property `SOUL.md` is meant to enforce.
- [[agentic-memory]] — contrasted with: identity vs. accumulated knowledge.

## Related entities

- [[wiki/entities/hermes-agent]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
