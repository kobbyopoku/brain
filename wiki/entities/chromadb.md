---
type: entity
title: ChromaDB
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [ChromaDB, Chroma]
tags: [database, vector-store, rag, agentic-memory]
---

# ChromaDB

> Open-source local vector store; in this wiki it is the reference backend for an agentic-memory implementation and a recommended vector store for RAG-over-notes projects.

## Profile

ChromaDB ("Chroma") is a vector database used to store and query embeddings by semantic meaning. In this wiki it appears as the local vector store in the reference implementation of an agentic-memory breakdown, where its `PersistentClient` persists vectors to disk across restarts. It is recommended as the starting point for local development before scaling to managed stores like [[wiki/entities/pinecone]] or [[wiki/entities/qdrant]].

## Key facts

- Used as the local vector store in the thread's reference implementation — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Its `PersistentClient` stores vectors on disk and persists across restarts — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Recommended as the starting point for local development — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Collections are configured with metadata `{'hnsw:space': 'cosine'}` for cosine similarity — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Named as a vector store for building a RAG system over personal notes (Phase 4) — [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]].

## Positions and claims

*(none yet.)*

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — local persistent vector store used as the reference implementation's backend.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — vector store option for the Phase-4 RAG-over-notes project.

## Related entities

- [[wiki/entities/pinecone]] — managed vector store recommended for scale.
- [[wiki/entities/qdrant]] — vector store recommended for scale.
- [[wiki/entities/pgvector]] — Postgres vector extension alternative.

## Related concepts

*(none yet.)*
