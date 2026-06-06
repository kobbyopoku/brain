---
type: concept
title: Self-evolving skills
created: 2026-06-06
updated: 2026-06-06
aliases: [self-evolving skills, agent-created skills, self-authored skills, learning loop]
tags: [agent-architecture, agent-skills, agent-learning, claude-code]
---

# Self-evolving skills

> Agent capabilities that the agent itself authors and refines during sessions, forming a learning loop where the skill library grows from the agent's own experience rather than only from pre-bundled or downloaded skills.

## Definition

Self-evolving skills are the subset of an agent's [[claude-code-skills|skills]] that the agent creates for itself during use, as opposed to skills shipped with the agent or fetched from a hub. In the Hermes agent, the `skills/` directory holds the agent's "learning loop": skills arrive three ways — bundled, hub-downloaded, or agent-created during sessions — and each skill is a `SKILL.md` plus `references/` and `scripts/`. The agent's self-authored skills are the evolving capability layer: the part of the agent that grows over time from its own work.

## Why it matters

A static skill set caps an agent at its initial capabilities. Letting the agent write and keep new skills turns capability into something that compounds with use — the agent gets more capable the more it works, and the accumulated skills are inspectable, editable artifacts rather than opaque weights. This is the capability-side analogue of [[agentic-memory]] (which compounds knowledge) and a structured alternative to [[self-annealing]] prompt drift.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]] locates Hermes's "learning loop" in the `skills/` folder: skills are bundled, hub-downloaded, or agent-created during sessions, each being `SKILL.md` + `references/` + `scripts/`. The agent's self-authored skills are framed as the evolving capability layer.

## Sub-claims and details

- In Hermes, `skills/` holds the agent's learning loop. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- Skills enter three ways: bundled with the agent, downloaded from a hub, or created by the agent during sessions. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- Each skill is structured as a `SKILL.md` plus a `references/` directory and a `scripts/` directory. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
- The agent-created skills specifically constitute the evolving capability layer. [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]

## Open questions and contradictions

- The source does not describe how the agent decides when to author a new skill, or how self-authored skills are validated or pruned.

## Related concepts

- [[skill-md]] — the file format each self-evolving skill takes.
- [[claude-code-skills]] — broader category; self-evolving skills are the agent-authored subset.
- [[skills-as-code]] — skills as inspectable, version-controllable artifacts.
- [[agentic-memory]] — knowledge-side analogue of the capability-side loop.
- [[self-annealing]] — related self-improvement dynamic.

## Related entities

- [[wiki/entities/hermes-agent]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-hermes-folder-anatomy]]
