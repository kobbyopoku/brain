---
type: concept
title: External memory
created: 2026-06-06
updated: 2026-06-06
aliases: [external memory, persistent agent memory, long-term memory]
tags: [agents, memory, storage, retrieval]
---

# External memory

> Persistent storage outside the model that survives sessions — in two flavors: structured stores for exact lookup and vector stores for semantic search.

## Definition

Per [[wiki/sources/techwith-ram-agentic-memory-breakdown]], **external memory** is persistent storage outside the model that survives sessions (unlike [[in-context-memory]], which is wiped at session end). It comes in two flavors:

- **Structured stores** — exact lookup (e.g. Postgres, Redis, SQLite).
- **Vector stores** — semantic search (e.g. Pinecone, Chroma, pgvector).

The source emphasizes that the hard part is retrieval, not storage: *"20% storage, 80% retrieval design."* It is one of the memory types under [[agentic-memory]].

## Why it matters

External memory is what lets an agent persist beyond a single session — the substrate for continuity and learning. The source's "20/80" framing reorients effort: standing up a database is easy; designing retrieval that surfaces the right memory at the right time is where the work lives.

## Treatment across sources

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as persistent storage outside the model that survives sessions, in two flavors — structured stores (exact lookup: Postgres/Redis/SQLite) and vector stores (semantic search: Pinecone/Chroma/pgvector) — and stresses that it is "20% storage, 80% retrieval design."

## Sub-claims and details

- Persistent storage outside the model; survives sessions. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Structured stores do exact lookup: Postgres, Redis, SQLite. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- Vector stores do semantic search: Pinecone, Chroma, pgvector. ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])
- *"20% storage, 80% retrieval design."* ([[wiki/sources/techwith-ram-agentic-memory-breakdown]])

## Open questions and contradictions

- Single-source concept.

## Related concepts

- [[agentic-memory]] — broader: the umbrella system this is one type of.
- [[in-context-memory]] — complement: the ephemeral working desk that offloads into external memory.
- [[episodic-memory]] — narrower-related: episodic logs are typically persisted in external memory.
- [[retrieval-augmented-generation]] — adjacent: vector-store retrieval is the same machinery as RAG.

## Related entities

- [[wiki/entities/techwith-ram]] — author of the source.

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
