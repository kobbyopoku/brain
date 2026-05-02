---
type: concept
title: Query
created: 2026-05-02
updated: 2026-05-02
aliases: [query, querying]
tags: [operation, llm-wiki, foundational]
---

# Query

> One of the three core operations of the [[llm-wiki-pattern]]: answering a question against the wiki by reading existing pages and synthesizing a cited response, with the option to file substantive answers back as new synthesis pages.

## Definition

To **query** the wiki is to ask a question of it and receive an answer that draws on the pages already written, not on the raw sources directly. The LLM reads the index, identifies candidate pages, follows wikilinks, and produces an answer with citations to the wiki pages it used (which in turn cite the underlying raw sources). Query is the *read path* of the LLM Wiki — the dual of [[ingest]].

## Why it matters

Query is where the human actually consumes the wiki's value. Because synthesis is precomputed during ingest, queries are fast and cheap: the LLM reads compiled knowledge, not raw fragments. A subtle question that would force a [[retrieval-augmented-generation|RAG]] system to find and stitch fragments from five documents is, in the LLM Wiki pattern, often answered by reading two or three already-synthesized pages and citing them.

A second crucial property: **good answers compound**. When a query produces a substantive answer — a comparison, a thesis, a non-trivial synthesis — the answer should be filed back as a `wiki/syntheses/<slug>.md` page. This way exploration accumulates in the wiki the same way ingested sources do. Queries that disappear into chat history are wasted compute.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — defines the operation: "You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas." Karpathy emphasizes that good answers should be filed back as synthesis pages so explorations compound.

## Sub-claims and details

- **Workflow** (per [[CLAUDE]] § Workflows → Query):
  1. Read `index.md` first to identify candidate pages.
  2. Read those pages; follow wikilinks if needed.
  3. Answer with citations — every non-trivial claim links to its wiki source page.
  4. If the answer is substantive, ask whether to file it back as a synthesis.
  5. If the wiki cannot answer, say so explicitly. Don't fabricate. Suggest sources to ingest.
- **Output formats are flexible**: prose, comparison tables, slide decks (Marp), charts, canvases — whatever fits the question. Markdown is the default.
- **Citations are mandatory.** Every non-trivial claim in an answer carries a wikilink to its supporting page.
- **Failure mode**: the LLM hallucinates beyond what the wiki contains. Mitigation: the schema mandates "if you can't cite, don't claim," and queries should explicitly flag gaps where the wiki is silent.

## Open questions and contradictions

- **When to file back?** The schema says "if substantive, ask the human." A more concrete heuristic — e.g. "any answer over 200 words that synthesizes 2+ wiki pages" — would reduce the asking. Worth refining.
- **Cross-vault query**: queries that span this wiki and external knowledge (e.g. a web search) are not yet a defined operation. They could be a fourth core operation, or an extension of query.

## Related concepts

- [[llm-wiki-pattern]] — the parent pattern.
- [[ingest]] — sibling operation; ingest writes, query reads.
- [[lint]] — sibling operation; lint surfaces queries the human should ask but hasn't.
- [[retrieval-augmented-generation]] — contrast: per-query retrieval over raw sources rather than against compiled wiki pages.

## Related entities

- [[wiki/entities/andrej-karpathy]] — defined the operation.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[CLAUDE]]
