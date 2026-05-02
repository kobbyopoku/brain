---
type: concept
title: Retrieval-Augmented Generation
created: 2026-05-02
updated: 2026-05-02
aliases: [RAG]
tags: [llm, retrieval, contrast-case]
---

# Retrieval-Augmented Generation

> Approach where an LLM retrieves relevant chunks from a document collection at query time and uses them to generate an answer; the contrast case the [[llm-wiki-pattern]] is positioned against.

## Definition

RAG is the dominant pattern for using an LLM with a corpus of documents: the documents are indexed (typically as embeddings), and at query time the system retrieves the most relevant chunks and feeds them to the LLM as context. The LLM generates an answer grounded in the retrieved fragments. NotebookLM, ChatGPT file uploads, and most "chat with your documents" products work this way.

## Why it matters

In the [[llm-wiki-pattern]], RAG is the explicit foil. The criticism is not that RAG is wrong, but that it does no accumulation: every query rediscovers the same connections from raw fragments. Subtle questions that require synthesizing five documents force the LLM to find and piece things together every time. Nothing is built up.

The LLM Wiki pattern's claim is that, at moderate scale, **a persistent LLM-maintained wiki out-performs RAG** because synthesis is precomputed and cumulative. Cross-references, contradictions, and entity profiles already exist before the query arrives.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — characterizes RAG as "rediscovering knowledge from scratch on every question," with "no accumulation," and positions the LLM Wiki pattern as the alternative for cases where knowledge should compound.

## Sub-claims and details

- **Per-query retrieval**: chunks are pulled from raw sources at the moment of the question.
- **No cumulative artifact**: there is no wiki, no entity page, no growing synthesis — only the raw corpus and the query log.
- **Suited to scale**: RAG handles very large corpora well precisely because nothing is precomputed beyond embeddings; the LLM Wiki pattern targets *moderate* scale (~100 sources).

## Open questions and contradictions

- **Hybrid futures** — nothing prevents combining the two: a wiki for the curated portion and RAG for a long tail of less-touched sources. Worth exploring as the vault grows.
- **Where is the crossover point** at which RAG wins on cost? Karpathy gestures at "very large scale" but doesn't quantify.

## Related concepts

- [[llm-wiki-pattern]] — the pattern positioned against this one.

## Related entities

- [[wiki/entities/qmd]] — uses BM25 + vector + LLM re-ranking; sits at a hybrid point between RAG and wiki search.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
