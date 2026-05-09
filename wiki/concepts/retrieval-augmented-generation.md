---
type: concept
title: Retrieval-Augmented Generation
created: 2026-05-02
updated: 2026-05-09
aliases: [RAG]
tags: [llm, retrieval, contrast-case]
---

# Retrieval-Augmented Generation

> Approach where an LLM retrieves relevant fragments from a document collection at query time and uses them to generate an answer. The dominant production pattern for "chat with your docs"; the contrast case the [[llm-wiki-pattern]] is positioned against; and the unit of which — *the chunk* — is itself increasingly under attack (cf. [[wiki/sources/akshay_pachaar-x-rag-wrong|Akshay Pachaar's "You're doing RAG wrong"]]).

## Definition

RAG is the dominant pattern for using an LLM with a corpus of documents: the documents are indexed (typically as embeddings), and at query time the system retrieves the most relevant fragments and feeds them to the LLM as context. The LLM generates an answer grounded in the retrieved fragments. NotebookLM, ChatGPT file uploads, and most "chat with your documents" products work this way.

The standard pipeline:

```
docs → parser → chunker → embedder → vector store → retriever → reranker → LLM
```

## Why it matters

There are now **two distinct critiques of RAG** in the wiki, attacking different layers of the standard pipeline:

### Critique 1 — RAG does no accumulation (the wiki critique)

In the [[llm-wiki-pattern]], RAG is the explicit foil. The criticism is not that RAG is wrong, but that it does no accumulation: every query rediscovers the same connections from raw fragments. Subtle questions that require synthesizing five documents force the LLM to find and piece things together every time. Nothing is built up.

The LLM Wiki pattern's claim is that, at moderate scale, **a persistent LLM-maintained wiki out-performs RAG** because synthesis is precomputed and cumulative. Cross-references, contradictions, and entity profiles already exist before the query arrives.

### Critique 2 — The chunk is the bug (the IdeaBlock critique)

[[wiki/sources/akshay_pachaar-x-rag-wrong|Akshay Pachaar (2026-05-08)]] attacks RAG at the *unit-of-knowledge* level: **chunks of text are structurally agnostic — they don't know where ideas begin or end, what version they are, or who is allowed to see them**. Splitters cut wherever the token budget runs out. The result: half-tables get retrieved, conclusions arrive without arguments, fifteen near-duplicate passages compete for the same retrieval slot, and governance has to be bolted on at the orchestrator instead of carried in the data.

The fix Akshay proposes is **structural rather than algorithmic** — replace the chunk with a question-answer packet ("IdeaBlock"): one question, its validated answer, and typed governance fields (clearance level / version state / source) on the same object. This is the same shape as the user's query, so the match becomes structural rather than probabilistic.

Both critiques converge on the same diagnosis: **RAG fails when its unit of knowledge is wrong.** The wiki critique says use a *wiki page* (synthesized + linked); the IdeaBlock critique says use a *Q-A packet* (atomic + typed). They are not in opposition — a wiki page can be decomposed into IdeaBlocks for a vector index, and IdeaBlocks can be filed as wiki entries. **The chunk is the unit that loses to either.**

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — characterizes RAG as "rediscovering knowledge from scratch on every question," with "no accumulation," and positions the LLM Wiki pattern as the alternative for cases where knowledge should compound.
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] *(2026-05-08)* — argues the chunk is the structural bug, not retrieval algorithm tuning. Reports concrete benchmark numbers from [[wiki/entities/blockify|Blockify]]'s preprocessing layer: 2.29× retrieval distance reduction, 13.55% vector-accuracy improvement after deduplication, 40× corpus-size compression. Introduces 7-stage preprocessing pipeline (Scoping → Ingestion → Chunking → Semantic Dedup → Auto-tagging → Human Validation → Export) that sits between document parser and vector store.

## Sub-claims and details

### Standard RAG failure modes

Per Akshay's diagnosis, three structural failures recur in production RAG:

1. **Idea boundary** — chunks cut wherever the token count runs out, so retrieval returns half-tables or claims stripped of their context.
2. **Versioning** — enterprise corpora carry a dozen near-identical versions across SharePoint / Confluence / Git. Top-K returns five copies; the LLM blends them.
3. **Governance** — chunks have no metadata, so role/version/clearance has to be enforced at the orchestrator, disconnected from the content.

### The IdeaBlock alternative

A typed unit replacing the chunk:

- **Question**: one critical question
- **Answer**: 2-3 sentences, validated
- **Governance fields**: clearance level (PUBLIC / INTERNAL / CONFIDENTIAL / SECRET), version state (Current / Deprecated / Draft / Approved), product line, export-control flags

Why it works for retrieval: queries are already questions. When the index stores answers to questions, the match is *structural* (same shape) rather than *probabilistic* (similar enough). Embedding distance shrinks (Blockify benchmark: 0.36 → 0.16 cosine distance, 2.29×).

### Counterintuitive: less data + more accuracy

In Blockify's benchmark across 17 documents / 298 pages: 2,042 raw blocks → 1,200 canonical IdeaBlocks after iterative dedup at 80-85% similarity. Word count: 88,877 → 44,537. **The distilled (smaller) dataset out-performed the undistilled by 13.55% on vector accuracy.** The intuition: redundancy *degrades* the retrieval surface because near-duplicates split probability mass across competing vectors in the same region of embedding space.

> *"Your vector index isn't a hard drive you want to fill. It's a retrieval surface, and redundancy degrades it."* — [[wiki/entities/akshay_pachaar|Akshay]]

### Wiki pattern as IdeaBlock superset

A well-maintained [[llm-wiki-pattern|LLM Wiki]] page is essentially a *cluster* of IdeaBlocks (claims + governance + cross-links) plus *navigational structure* (wikilinks, index, log). The wiki adds:

- **Synthesis pages** — IdeaBlocks don't compose into multi-source comparisons; wiki syntheses do.
- **Cross-references** — wikilinks make the relationships traversable; vector retrieval doesn't.
- **Maintenance discipline** — the lint workflow keeps the corpus consistent; deduplication only handles the embedding surface.

Conversely, the wiki *lacks* IdeaBlock's fast probabilistic recall. **A hybrid (wiki for synthesis + IdeaBlock-flavored vector index for atomic recall) is plausibly the strongest architecture** — left as an open question below.

### Per-query vs precomputed

- **RAG**: retrieves at query time; nothing precomputed beyond embeddings + (optionally) deduplication.
- **LLM Wiki**: synthesis is precomputed at ingest time; query reads.
- **IdeaBlock-augmented RAG**: distillation is precomputed at preprocessing time; query reads + retrieves.

The trend across all three: **move work earlier in the pipeline so the query is cheap.**

## Open questions and contradictions

- **Hybrid futures** — nothing prevents combining the patterns: a wiki for the curated synthesized portion + IdeaBlock-style vector index for atomic recall + RAG for the long tail. Worth exploring as the vault grows.
- **Where is the crossover point** at which RAG wins on cost? Karpathy gestures at "very large scale" but doesn't quantify. Blockify's benchmark suggests the answer is **never** for properly-distilled corpora — but their numbers are vendor-internal, so treat as directional.
- **Wiki-as-IdeaBlock-source** — could a `wiki_lint.py` extension auto-derive IdeaBlocks from wiki pages? Each `## ` heading often *is* a Q-A packet shape. Worth prototyping.
- **Governance in the brain** — IdeaBlock's typed clearance fields don't exist in the wiki. The wiki currently has no role-based access. If the brain ever serves multiple consumers (read-mode from many projects), this becomes a real question.
- **The 95% / 40× / 2.29× / 13.55% numbers** all come from Blockify's own benchmark across 298 pages. Independent reproduction unverified. Treat as *upper-bound directional signals*, not benchmarks.

## Related concepts

- [[llm-wiki-pattern]] — the pattern positioned against RAG; uses synthesis instead of retrieval.
- [[hot-cache]] — a different per-query speedup; orthogonal to chunk/IdeaBlock choice.
- [[progressive-disclosure]] — wiki's cousin pattern; loads context in tiers rather than retrieving fragments.
- [[markdown-as-agent-contract]] — the wiki's unit (the markdown page) is itself a contract; IdeaBlock makes the unit even more typed.
- [[mcp-server]] — RAG-style retrieval often exposed as MCP servers; the unit choice matters at this boundary too.

## Related entities

- [[wiki/entities/qmd]] — uses BM25 + vector + LLM re-ranking; sits at a hybrid point between RAG and wiki search.
- [[wiki/entities/blockify]] — preprocessing layer that implements IdeaBlocks; sits between parser and vector store.
- [[wiki/entities/akshay_pachaar]] — author of the chunk-is-the-bug critique.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[wiki/sources/akshay_pachaar-x-rag-wrong]]
