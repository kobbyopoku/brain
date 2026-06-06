---
type: concept
title: Harness engineering
created: 2026-06-06
updated: 2026-06-06
aliases: [agent harness engineering]
tags: [agents, harness, engineering, stub]
---

# Harness engineering

> The outermost of three concentric engineering disciplines for agents — building the runtime scaffolding (tool orchestration, state, error recovery, verification, safety, lifecycle) that surrounds an LLM, beyond just prompting and context.

## Definition

**Harness engineering** is the discipline of building the [[agent-harness]] — the runtime layer that wraps an LLM and makes it a working agent. In [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] it is the outermost of three concentric engineering levels: prompt engineering ⊂ [[context-engineering]] ⊂ harness engineering. It encompasses tool orchestration, state persistence, error recovery, verification loops, safety enforcement, and lifecycle management.

## Why it matters

Framing the agent stack as three nested levels makes explicit that prompting and context are necessary but not sufficient — production agents stand or fall on the surrounding harness. Harness engineering names the broadest of those levels and the work that distinguishes demos from production systems.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as the outermost of three concentric engineering levels (prompt ⊂ context ⊂ harness); it encompasses tool orchestration, state persistence, error recovery, verification loops, safety enforcement, and lifecycle management.

## Sub-claims and details

- The three levels are concentric: prompt engineering is inside [[context-engineering]], which is inside harness engineering ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Harness engineering's scope: tool orchestration, state persistence, error recovery, verification loops, safety enforcement, lifecycle management ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Open questions and contradictions

- Where the boundary sits between harness engineering and [[context-engineering]] when a harness component (e.g. [[context-management]]) is itself about managing context.

## Related concepts

- [[agent-harness]] — the artifact this discipline builds.
- [[context-engineering]] — the middle level, nested inside harness engineering.
- [[context-management]] — a harness component.
- [[verification-loops]] — a harness component.

## Related entities

- [[wiki/entities/akshay_pachaar]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
