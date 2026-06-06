---
type: concept
title: Context window
created: 2026-06-06
updated: 2026-06-06
aliases: [context window, context length]
tags: [context-window, ai-engineering, model-selection, memory]
---

# Context window

> The bounded amount of input and output a model can handle at once — a finite substrate where every token costs money and time, and overflow forces information to be dropped.

## Definition

A context window is how much input and output a model can process in a single call. [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] (Stage VI item 4) frames it as how much input/output a model handles and which data types it supports — a factor that drives model choice for cost, speed, and reliability. [[wiki/sources/techwith-ram-agentic-memory-breakdown]] presents it as the bounded substrate of in-context memory ("the desk has a size limit"), where every token costs money and time and overflow produces the sliding-window problem. [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] lists it among the four Phase-1 plain-English-explanation targets (tokens, embeddings, transformers, context windows).

## Why it matters

The context window is the constraint that shapes model selection, cost, and memory architecture. Understanding it is what motivates retrieval, summarization, and memory systems — and the sources treat it as a foundational concept an AI engineer must be able to explain plainly.

## Treatment across sources

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] frames it as Stage VI item 4; how much input/output a model handles and which data types it supports — drives model choice for cost/speed/reliability.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as the bounded substrate of in-context memory ("the desk has a size limit"); every token costs money/time; overflow produces the sliding-window problem.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] frames it as a Phase-1 plain-English-explanation target alongside tokens/embeddings/transformers.

## Sub-claims and details

- It determines how much input/output a model handles and which data types it supports ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]).
- It drives model choice on cost, speed, and reliability ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]).
- Every token in the window costs money and time ([[wiki/sources/techwith-ram-agentic-memory-breakdown]]).
- Overflow of the window produces the sliding-window problem ([[wiki/sources/techwith-ram-agentic-memory-breakdown]]).

## Open questions and contradictions

- None surfaced; sources are complementary (roadmap framing vs. memory-mechanics framing).

## Related concepts

- [[wiki/concepts/embeddings]] — sibling Phase-1 foundational concept; also a route to handling data beyond the window.
- [[wiki/concepts/retrieval-augmented-generation]] — a response to context-window limits.
- [[wiki/concepts/ai-engineering]] — broader; the context window is a foundational concept within it.

## Related entities

## Mentioned in

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]
