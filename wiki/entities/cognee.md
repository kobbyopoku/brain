---
type: entity
title: Cognee
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [Cognee, cognee]
tags: [product, ai-memory, agentic-architecture, graph, open-source]
---

# Cognee

> Open-source graph-memory product that stores an agent's skills and memory in the same graph store, with a shared self-improvement runtime.

## Profile

Cognee is an open-source memory system (repo at `github.com/topoteretes/cognee`, owned by [[wiki/entities/topoteretes|topoteretes]]) that treats agent skills and agent memory as a single substrate rather than two separate subsystems. Its self-improvement runtime and agentic retriever both operate over the same graph nodes, so a skill is modelled as a traceable, evolving, controllable memory node rather than a static file. Cognee is the product context behind [[wiki/entities/tricalt|tricalt]]'s argument that "memory isn't a plugin, skills aren't a plugin — they're the same harness" ([[wiki/sources/tricalt-memory-skills-same-harness]]).

## Key facts

- **Repository**: open-source at `github.com/topoteretes/cognee`; owned by [[wiki/entities/topoteretes|topoteretes]] ([[wiki/sources/tricalt-memory-skills-same-harness]]).
- **Shared store**: skills and memory live in the same graph store; the self-improvement runtime and the agentic retriever share the same graph nodes ([[wiki/sources/tricalt-memory-skills-same-harness]]).
- **Skill ingest**: `cognee.remember("skills/")` ingests skills "with one line" ([[wiki/sources/tricalt-memory-skills-same-harness]]).
- **Change events**: emits a `SkillChangeEvent` (memory events) when a skill changes, making the skill a traceable, evolving, controllable memory node ([[wiki/sources/tricalt-memory-skills-same-harness]]).
- **Self-improvement API**: exposes skill self-improvement via a `SkillRunEntry` passed to `cognee.remember(...)` with `success_score`, `feedback`, and a `skill_improvement` block (`apply`, `score_threshold`) ([[wiki/sources/tricalt-memory-skills-same-harness]]).
- **Hackathon usage**: used with [[wiki/entities/redis|Redis]] as a session store to build 21 "LLM Knowledge Wikis" in 3 hours at a hackathon ([[wiki/sources/tricalt-memory-skills-same-harness]]).

## Positions and claims

- Positioned as a "controller" that runs on top of a permanently-misspecified world model — argued in [[wiki/sources/tricalt-memory-skills-same-harness]].
- Memory and skills should share one harness rather than being bolted on as plugins ([[wiki/sources/tricalt-memory-skills-same-harness]]).

## Mentioned in

- [[wiki/sources/tricalt-memory-skills-same-harness]] — the open-source graph-memory product whose shared store and self-improvement runtime anchor the post's argument.

## Related entities

- [[wiki/entities/topoteretes|topoteretes]] — GitHub org / owner of the Cognee repository.
- [[wiki/entities/tricalt|tricalt]] — Cognee-associated author of the source post.
- [[wiki/entities/redis|Redis]] — used as the session store alongside Cognee in the hackathon example.

## Related concepts

-
