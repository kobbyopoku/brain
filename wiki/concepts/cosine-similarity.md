---
type: concept
title: Cosine similarity
created: 2026-06-06
updated: 2026-06-06
aliases: [cosine distance]
tags: [embeddings, memory, retrieval, stub]
---

# Cosine similarity

> A similarity metric used to compare embedding vectors by the angle between them, used in agentic memory systems to rank stored memories by semantic relevance to a query.

## Definition

**Cosine similarity** measures how alike two vectors are by the cosine of the angle between them. Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], the metric ranges over: `1.0` for identical meaning, `0.0` for unrelated, and `-1.0` for opposite. In the source's reference recall code, relevance is derived as `1 - cosine distance`.

## Why it matters

Cosine similarity is the concrete mechanism by which an agent's memory system decides *which* stored memories are relevant to recall for a given query — the retrieval step that bookends the [[agentic-loop]].

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as the similarity metric for memory recall: `1.0` identical meaning, `0.0` unrelated, `-1.0` opposite; relevance derived as `1 - cosine distance` in the reference recall code.

## Sub-claims and details

- Value semantics: `1.0` = identical meaning, `0.0` = unrelated, `-1.0` = opposite. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- In the reference recall code, relevance = `1 - cosine distance`. (per [[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- (none surfaced by current sources)

## Related concepts

- [[retrieval-augmented-generation]] — retrieval scoring commonly uses cosine similarity over embeddings.
- [[memory-consolidation]] — near-duplicate detection for merging relies on high similarity.
- [[agentic-loop]] — recall is the pre-call half of memory bookending the loop.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
