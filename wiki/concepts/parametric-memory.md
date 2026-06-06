---
type: concept
title: Parametric memory
created: 2026-06-06
updated: 2026-06-06
aliases: [weight memory, in-weights memory]
tags: [agents, memory, agent-architecture]
---

# Parametric memory

> Knowledge encoded directly in a model's weights during training — always available without a retrieval step, but frozen at the training cutoff, non-updatable at inference, and opaque.

## Definition

**Parametric memory** is knowledge that lives in a language model's weights, learned at training time, as distinct from knowledge supplied at inference through retrieval or context. Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], it is always available (no retrieval needed) but carries structural limitations: it is frozen at the training cutoff, cannot be updated, is opaque, and is hallucination-prone.

## Why it matters

Parametric memory sets the baseline that agentic memory systems are built to compensate for. Because it is frozen and opaque, it cannot serve time-sensitive, private, or domain-specific data — those needs are what external/retrieval-based memory exists to address. Understanding parametric memory as the fallback layer clarifies *why* an agent needs a separate memory system at all.

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as knowledge encoded in model weights at training: always available, no retrieval, but frozen at cutoff, non-updatable, opaque, and hallucination-prone. Treated as the fallback for general world knowledge, not for time-sensitive, private, or domain data.

## Sub-claims and details

- Parametric memory requires no retrieval step — it is intrinsic to the model. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- It is frozen at the training cutoff and cannot be updated at inference. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- It is opaque and hallucination-prone. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Its appropriate role is general world knowledge; it is not suited to time-sensitive, private, or domain-specific data. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- Unresolved from current sources: where exactly the boundary sits between relying on parametric memory and routing a query to external memory.

## Related concepts

- [[augmented-llm]] — retrieval and memory augmentations compensate for parametric memory's limits.
- [[agentic-loop]] — memory bookends the loop; parametric memory is what remains when no external memory is present.
- [[retrieval-augmented-generation]] — supplies non-parametric knowledge at inference.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
