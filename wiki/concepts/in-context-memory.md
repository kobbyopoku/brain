---
type: concept
title: In-context memory
created: 2026-06-06
updated: 2026-06-06
aliases: [in context memory, working memory, context-window memory]
tags: [agents, memory, context-window]
---

# In-context memory

> An agent's "working desk" — everything inside the context window (system prompt, conversation history, tool results, retrieved memories, scratchpad) — bounded by the window and wiped at session end, with no retrieval step.

## Definition

Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], **in-context memory** is the agent's working desk: the contents of the context window, comprising the system prompt, conversation history, tool results, retrieved memories, and a scratchpad. It has **no retrieval step** (everything is already present in context), is **bounded by the context window**, and is **wiped at session end**. It is one of the memory types under [[agentic-memory]].

## Why it matters

In-context memory is where the agent actually thinks — but it is finite and ephemeral. Its boundedness forces an engineering problem (the sliding-window problem) and motivates the persistent stores of [[external-memory]]: anything that must survive the window or the session has to be offloaded.

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as the agent's "working desk" (system prompt, conversation history, tool results, retrieved memories, scratchpad), with no retrieval step, bounded by the context window, and wiped at session end. Names the sliding-window problem and its mitigations.

## Sub-claims and details

- Contents: system prompt, conversation history, tool results, retrieved memories, scratchpad. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- No retrieval step — everything is already in context. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Bounded by the context window; wiped at session end. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- The **sliding-window problem** is mitigated by summarization, selective retention, and offload (to [[external-memory]]). ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- Single-source concept.

## Related concepts

- [[agentic-memory]] — broader: the umbrella system this is one type of.
- [[external-memory]] — complement: persistent store that survives the session in-context memory cannot.
- [[episodic-memory]] — adjacent memory type under the same umbrella.

## Related entities

- [[wiki/entities/techwith-ram]] — author of the source.

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
