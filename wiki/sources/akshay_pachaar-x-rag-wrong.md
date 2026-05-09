---
type: source
title: Akshay Pachaar — You're doing RAG wrong (chunk-as-unit is the bug; IdeaBlocks)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/akshay_pachaar/status/2052743644411765230
source_type: x-thread
author: Akshay Pachaar
source_date: 2026-05-08
raw_path: raw/You're doing RAG wrong.md
content_status: substantive
tags: [rag, retrieval, chunking, ideablocks, blockify, vector-search, ai-architecture]
---

# Akshay Pachaar — You're doing RAG wrong (chunk-as-unit is the bug; IdeaBlocks)

> Akshay Pachaar's substantive argument: **the chunk is the wrong unit of knowledge to embed**. RAG stacks have spent years patching downstream symptoms (rerankers, hybrid search, threshold tuning, prompt engineering) — all of which compensate for an upstream architecture problem the chunk creates. The fix is to make the unit of knowledge structurally explicit: embed *one validated claim with typed governance fields*, not a window of prose. Surfaces [[wiki/entities/blockify|Blockify]] / IdeaBlocks as the production-ready preprocessing layer that implements this. **Major refresh of the wiki's [[retrieval-augmented-generation]] concept page.**

## TL;DR

Three measured improvements claimed by the IdeaBlock approach (per Blockify's internal benchmark across 17 documents / 298 pages):

- **40× corpus-size reduction** (relative to raw chunks).
- **3× tokens-per-query reduction**.
- **2.3× vector-search relevance improvement** (cosine retrieval distance: 0.1585 IdeaBlocks vs 0.3624 naive chunks = 2.29× reduction).

Plus a 13.55% vector-accuracy improvement after iterative semantic deduplication (80-85% similarity, 3-5 rounds): 2,042 raw blocks → 1,200 canonical blocks; word count 88,877 → 44,537.

## Key takeaways

### Why the chunk is a bad unit

A chunk of text is **structurally agnostic** — it knows nothing about:
- Where its ideas begin or end.
- Which version of a document it came from.
- Who is allowed to see it.

The splitter cuts wherever the token count runs out. You retrieve half a table, a conclusion with no argument, a claim stripped of context that makes it true. The model has no way to know what's missing.

### The version problem

Most enterprise corpora have the same document in dozens of near-identical versions across SharePoint, Confluence, Git. Top-K retrieval returns five copies of the same paragraph — current and deprecated mixed together. The LLM blends them into an answer that's *confidently wrong*. Pure retrieval-quality work cannot fix this; it's an architecture problem.

### The IdeaBlock alternative

Replace the chunk with an **IdeaBlock** = `{ question, validated_answer, typed_governance_fields }`. Each block is a single atomic claim, not a window of narrative.

Three downstream consequences:

1. **Query construction gets simpler** — your queries are already questions. When the index stores *answers to questions*, the match becomes structural rather than probabilistic.
2. **Governance moves into the data layer** — role / version / clearance as typed fields per block, not logic bolted onto the orchestrator. A sales engineer querying the same index as a legal reviewer gets a different dataset *because the blocks themselves carry the access boundary*.
3. **Updates propagate from a single record** — when a spec changes, you update one IdeaBlock. With naive chunking, the same fact lives in dozens of near-duplicate passages across multiple documents; finding all of them at enterprise scale is intractable.

### The 7-stage Blockify pipeline

(Detailed in [[wiki/entities/blockify]].) Scoping → Ingestion → Chunking & extraction → Semantic deduplication → Auto-tagging → Human validation → Export. Each stage has defined input/output, so failures are localizable.

### The counterintuitive finding: less data, more accuracy

Most people expect that shrinking the corpus hurts retrieval. Akshay's data shows the opposite — distilled corpus outperforms undistilled by 13.55% on vector accuracy. The reason: **fifteen near-duplicates of the same paragraph create fifteen competing vectors in the same region of embedding space**. Retrieval distributes probability mass across all of them, pulling the match score down for the canonical version. Collapse them into one canonical block and the signal sharpens.

> "Your vector index isn't a hard drive you want to fill. It's a retrieval surface, and redundancy degrades it."

## Notable quotes

> "There's a new approach that cuts corpus size by 40×, reduces tokens per query by 3×, improves vector search relevance by 2.3×. And it doesn't touch your retrieval algorithm, your reranker, or your embedding model."

> "Every RAG pipeline starts with the same assumption: a chunk of text is the right unit of knowledge to embed. That assumption is almost never examined. And it's the source of most of the retrieval failures people try to fix downstream."

> "RAG stacks are beginning to grow a distillation layer between parsing and vectorization, the way web stacks grew a CDN layer between origin and browser."

> "The chunk is a parsing convenience that became a retrieval assumption."

## Notes

- **Cross-cite with [[wiki/concepts/retrieval-augmented-generation]]**: this thread substantively complicates the wiki's existing RAG coverage, which had treated chunk-based retrieval as the default. The chunk-as-unit-is-the-bug argument needs to be promoted into the concept page.
- **Cross-cite with [[wiki/concepts/markdown-as-agent-contract]]**: an IdeaBlock's typed-fields shape (`question, validated_answer, governance_fields`) is structurally similar to YAML-frontmatter + markdown-body conventions other agent-contract patterns use. Same atomic-unit-with-explicit-shape principle, applied to RAG retrieval rather than agent input.
- **Cross-cite with [[wiki/entities/blockify]]**: the production-ready implementation that ships this. New entity stub created in this batch.
- **Open question**: how does this interact with the [[wiki/sources/cyrilxbt-x-2052235121416188114|Karpathy LLM Wiki pattern]]? Karpathy's pattern is *"folder of markdown files + index + log"* with no embedding layer — chunk-as-unit isn't the failure mode there because there's no chunking. Worth thinking through.

## Mentioned entities

- [[wiki/entities/akshay_pachaar]] — author.
- [[wiki/entities/blockify]] — surfaced product.

## Related concepts

- [[retrieval-augmented-generation]] — major refresh; chunk-as-unit-is-the-bug now first-class.
- [[markdown-as-agent-contract]] — IdeaBlock's typed-shape is structurally similar.
- [[mcp-server]] — adjacent (MCP-served knowledge bases benefit from IdeaBlock-shaped data).
- [[reasoning-execution-split]] — adjacent (the LLM reasons over retrieved IdeaBlocks; the deterministic preprocessing pipeline executes the dedup/clean).

## Related sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — alternative knowledge architecture (no embeddings; pure markdown).
- [[wiki/sources/cyrilxbt-x-2052235121416188114]] — Karpathy-pattern variant; lives in the same problem space (knowledge organization for LLMs).
