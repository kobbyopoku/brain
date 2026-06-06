---
type: concept
title: Vector database
created: 2026-06-06
updated: 2026-06-06
aliases: [vector database, vector db, vector store]
tags: [vector-database, ai-engineering, semantic-search, rag, memory]
---

# Vector database

> A storage and retrieval system that holds embeddings and finds the nearest neighbors of a query vector in high-dimensional space, enabling semantic search over conceptually related data.

## Definition

A vector database stores embeddings and retrieves them by vector similarity. [[wiki/sources/techwith-ram-agentic-memory-breakdown]] calls it "the heart of any serious memory system," describing it as finding the nearest neighbors of a vector in high-dimensional space so that semantically related memories surface even with no shared words. [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] (Stage VI item 3) frames it as the storage/retrieval layer that holds useful information for RAG. [[wiki/sources/exploraX_-5-solo-ai-business-models]] names it in the AI-engineer roadmap layer 3 alongside RAG, for letting AI search your own data. [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] (Phase 4) cites concrete options — ChromaDB and LanceDB — for a RAG-over-notes project.

## Why it matters

The vector database is the retrieval backbone of both RAG and agentic memory — the infrastructure that lets an AI system search its own data semantically. It appears across roadmap, memory, and solo-business sources as a recurring building block of practical AI systems.

## Treatment across sources

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] frames it as Stage VI item 3; storage/retrieval layer that holds useful information for RAG.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] frames it as "the heart of any serious memory system"; finds nearest neighbors of a vector in high-dimensional space, enabling semantic search over conceptually related memories even with no shared words.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] frames it as named in the AI-engineer roadmap layer 3 alongside RAG for letting AI search your own data.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] frames it as the Phase 4 storage/retrieval layer for the RAG-over-notes project (ChromaDB / LanceDB).

## Sub-claims and details

- It finds nearest neighbors of a query vector in high-dimensional space ([[wiki/sources/techwith-ram-agentic-memory-breakdown]]).
- It enables retrieval of conceptually related items even with no shared words ([[wiki/sources/techwith-ram-agentic-memory-breakdown]]).
- It is the storage/retrieval layer for RAG ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]], [[wiki/sources/exploraX_-5-solo-ai-business-models]]).
- Concrete implementations named: ChromaDB and LanceDB ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).

## Open questions and contradictions

- None surfaced; sources are consistent.

## Related concepts

- [[wiki/concepts/embeddings]] — paired; the vectors a vector database stores.
- [[wiki/concepts/retrieval-augmented-generation]] — primary consumer of vector databases.
- [[wiki/concepts/ai-engineering]] — broader; vector databases are a sub-skill.

## Related entities

## Mentioned in

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]]
- [[wiki/sources/exploraX_-5-solo-ai-business-models]]
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]
