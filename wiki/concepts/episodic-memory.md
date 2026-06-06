---
type: concept
title: Episodic memory
created: 2026-06-06
updated: 2026-06-06
aliases: [episodic memory, event memory]
tags: [agents, memory, learning]
---

# Episodic memory

> Memory of events and outcomes — what the agent did and how it turned out — stored as a structured log per completed task, recalled to learn few-shot from its own history.

## Definition

Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], **episodic memory** stores *events and outcomes* of past actions, as distinct from facts. It takes the form of a structured log entry per completed task. Recalling similar past episodes amounts to **few-shot learning from the agent's own personal history**, and the mechanism is closed by a **reflection loop** that turns completed episodes into recallable memory. The source calls it *"the most underappreciated type."* It is one of the memory types under [[agentic-memory]].

## Why it matters

Episodic memory is the substrate for an agent learning from experience rather than from static facts: by recalling how similar tasks went before, the agent few-shots itself from its own track record. The source's framing — that it is the most underappreciated memory type — flags it as an underused lever for agents that should improve over time.

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as storing events and outcomes of past actions (vs. facts), as a structured log per completed task, where recall of similar past episodes is few-shot learning from personal history, closed by a reflection loop. Calls it "the most underappreciated type."

## Sub-claims and details

- Stores events and outcomes of past actions, not facts. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Takes the form of a structured log per completed task. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Recall of similar past episodes = few-shot learning from personal history. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Closed by a reflection loop. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Described as "the most underappreciated type." ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- Single-source concept.

## Related concepts

- [[agentic-memory]] — broader: the umbrella system this is one type of.
- [[external-memory]] — implementation substrate: episodic logs are typically persisted there.
- [[in-context-memory]] — contrasted with: ephemeral working context vs. durable event log.

## Related entities

- [[wiki/entities/techwith-ram]] — author of the source.

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
