---
type: concept
title: Agentic memory
created: 2026-06-06
updated: 2026-06-06
aliases: [agent memory, agentic memory systems]
tags: [agents, memory, architecture]
---

# Agentic memory

> A system (storage + retrieval + management) that gives an AI agent continuity, context, and learning — doing three jobs at once rather than being a single store.

## Definition

Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], **agentic memory** is defined not as a single store but as a *system* combining storage, retrieval, and management that performs three jobs simultaneously:

1. **Continuity** — identity: the agent remains "the same" agent across interactions.
2. **Context** — the current task: what the agent needs in mind to act now.
3. **Learning** — improvement over time: the agent gets better from accumulated experience.

It is the umbrella concept that the source anchors, under which sit [[in-context-memory]], [[external-memory]], and [[episodic-memory]].

## Why it matters

Memory is the difference between an agent that restarts cold every session and one that maintains identity, holds task context, and improves over time. Framing memory as a three-job *system* rather than a bucket of stored facts clarifies why a real agent needs several distinct memory mechanisms (working context vs. persistent store vs. event log) rather than one.

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as a system (storage + retrieval + management) doing three jobs at once: continuity (identity), context (current task), and learning (improvement over time). The umbrella concept the source anchors.

## Sub-claims and details

- Agentic memory is a *system* of storage + retrieval + management, not a single store. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- The three jobs it does at once: continuity (identity), context (current task), learning (improvement over time). ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- Single-source concept; the three-job taxonomy is this source's framing.

## Related concepts

- [[in-context-memory]] — narrower: the agent's working desk within the context window.
- [[external-memory]] — narrower: persistent storage that survives sessions.
- [[episodic-memory]] — narrower: memory of past events and outcomes.

## Related entities

- [[wiki/entities/techwith-ram]] — author of the source.

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
