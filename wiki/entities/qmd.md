---
type: entity
title: qmd
entity_type: product
created: 2026-05-02
updated: 2026-05-02
aliases: []
tags: [tooling, search]
---

# qmd

> Local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking; an optional scale-up tool for an LLM Wiki.

## Profile

qmd is a local-first search engine over a directory of markdown files, combining BM25 keyword search with vector search and LLM-based re-ranking, all on-device. It exposes both a CLI (so an LLM can shell out to it) and an MCP server (so an LLM can call it as a native tool). Karpathy mentions it as the recommended option once a wiki outgrows the point where an `index.md` file is sufficient as a retrieval mechanism.

## Key facts

- **Repo**: https://github.com/tobi/qmd (cited in [[wiki/sources/llm-wiki-pattern-karpathy]])
- **Hybrid retrieval**: BM25 + vector search + LLM re-ranking.
- **Two interfaces**: CLI and MCP server.
- **Scope**: local, on-device — no external service required.

## Positions and claims

_(none — qmd is a tool.)_

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]] — recommended as a scale-up option for wiki search.

## Related entities

- [[wiki/entities/obsidian]] — different tool for a different layer (editing/browsing vs. search).

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]]
- [[wiki/concepts/retrieval-augmented-generation]]
