---
type: entity
title: Akshay Pachaar
entity_type: person
created: 2026-05-09
updated: 2026-05-09
website: https://x.com/akshay_pachaar
aliases: [akshay_pachaar]
tags: [author, ml-educator, rag, ai-agents, content-creator]
---

# Akshay Pachaar

> ML / LLM / AI-agents educator on X. Author of *"You're doing RAG wrong"* — a substantive 2026-05-08 post arguing that **the chunk is the wrong unit of knowledge to embed**. Surfaced [[wiki/entities/blockify|Blockify]] / IdeaBlocks as the upstream-fix alternative to the chunk-as-unit assumption that most RAG stacks build on.

## Profile

Akshay's content sits in the *technical educator* lane of AI-content X — adjacent to but distinct from [[wiki/entities/avi-chawla|Avi Chawla]]. Recurring topics: RAG architecture, LLM internals, AI agent patterns, ML tutorials. Tagline-style outro: *"For more insights and tutorials on LLMs, AI Agents, and Machine Learning!"*

## Key facts

- **X handle**: [@akshay_pachaar](https://x.com/akshay_pachaar).
- **Posts in wiki**: 1 substantive (status 2052743644411765230; 588+ likes — *"You're doing RAG wrong"*).
- **Substantive contribution**: surfaced the **chunk-as-unit-is-the-bug** argument and Blockify's IdeaBlock alternative to the wiki. Major refresh of [[retrieval-augmented-generation]] concept page.

## Positions and claims

- **The chunk is a parsing convenience that became a retrieval assumption** — and the source of most retrieval failures people try to fix downstream with rerankers, hybrid search, threshold tuning, prompt engineering.
- **Embed claims, not chunks.** A *question + validated answer + typed governance fields* is the right atomic unit.
- **Less data, more accuracy.** Distilled corpus (semantic dedup at 80-85%) outperforms undistilled by 13.55% on vector accuracy (per Blockify's internal benchmark).
- **Governance belongs in the data layer**, not bolted onto the orchestrator. Role / version / clearance as typed fields per IdeaBlock.

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — canonical wiki source.

## Related entities

- [[wiki/entities/blockify]] — preprocessing layer Akshay surfaced (new entity stub in this batch).

## Related concepts

- [[retrieval-augmented-generation]] — Akshay's argument complicates the chunk-as-unit assumption that this concept's earlier wiki coverage took for granted.
- [[markdown-as-agent-contract]] — IdeaBlock's typed-fields shape is structurally similar to other agent-contract markdown shapes.
