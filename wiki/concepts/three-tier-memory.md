---
type: concept
title: Three-tier memory
created: 2026-06-06
updated: 2026-06-06
aliases: [three-tier memory, three tier memory, hermes memory tiers, memory layering]
tags: [agentic-memory, agent-architecture, memory, hermes]
---

# Three-tier memory

> Hermes's memory layering: always-in-context facts, searchable history, and external deeper-persistence providers — three tiers that trade off recall depth against context cost.

## Definition

The three tiers, as articulated for the Hermes agent, are: Tier 1, always-in-context facts (a frozen `MEMORY.md` / `USER.md` plus `SOUL.md`); Tier 2, searchable history (a `state.db` with FTS5 full-text search); and external providers for deeper persistence. ([[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]])

## Why it matters

It is a concrete reference design for layering agent memory by access pattern — keeping a small, always-loaded core in context while pushing larger history into searchable and external stores. This separates "what the agent always knows" from "what the agent can look up."

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] frames it as the cleanest articulation of Hermes's memory layering — Tier 1 always-in-context facts (frozen `MEMORY.md`/`USER.md` + `SOUL.md`), Tier 2 searchable history (`state.db` + FTS5), and external providers for deeper persistence — stated in Akshay's reply.

## Sub-claims and details

- Tier 1: always-in-context facts — a frozen `MEMORY.md` / `USER.md` plus `SOUL.md`. ([[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]])
- Tier 2: searchable history — a `state.db` backed by FTS5. ([[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]])
- External providers supply a deeper-persistence layer beyond the two local tiers. ([[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]])

## Open questions and contradictions

- None recorded yet from a single source.

## Related concepts

- [[wiki/concepts/agentic-memory]] — broader category; three-tier memory is one layering scheme.
- [[wiki/concepts/in-context-memory]] — corresponds to the Tier 1 always-in-context layer.
- [[wiki/concepts/external-memory]] — corresponds to the external-provider deeper-persistence layer.
- [[wiki/concepts/persistent-memory]] — the searchable + external tiers provide persistence across sessions.

## Related entities

-

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
