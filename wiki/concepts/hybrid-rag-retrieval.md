---
type: concept
title: Hybrid RAG retrieval
created: 2026-06-08
updated: 2026-06-08
aliases: [bm25-vector-rerank, hybrid-search-with-reranker, sparse-dense-fusion-rag]
tags: [rag, retrieval, search, llm-pattern, bm25, vector-search, reranking]
---

# Hybrid RAG retrieval

> A retrieval pattern where keyword (BM25) and dense vector candidate sets are merged via Reciprocal Rank Fusion, then re-ordered by a cross-encoder reranker — producing higher precision than either retrieval method alone at a manageable latency cost.

## Definition

Hybrid RAG retrieval composes three retrieval stages:

1. **BM25 keyword retrieval** as one candidate generator. Tokenizes the query, looks up inverted-index hits, scores by TF-IDF-style weighting. Strong at exact-term matching, technical jargon, named entities, code identifiers — anything where lexical match is the right signal.
2. **Dense vector retrieval** (cosine similarity over learned embeddings, typically pgvector + an HNSW or IVFFlat index) as a parallel candidate generator. Strong at semantic match, paraphrase, conceptual relatedness — anything where the user's words and the document's words don't lexically overlap.
3. **Reciprocal Rank Fusion (RRF)** to merge the two candidate sets. For each document appearing in either list, score = Σ 1/(k + rank-in-list); typically k=60 from the original paper. Lower-bound: a doc in only one list gets a partial score; upper-bound: a doc appearing high in both gets close to the maximum.
4. **Cross-encoder reranker** over the top-K fused candidates (typically K=20-50). Unlike the bi-encoder used for the dense retrieval embeddings, the cross-encoder takes (query, document) as a SINGLE input and outputs one relevance score per pair. Much more accurate per-pair than cosine over independent embeddings, but quadratic in document count — only viable on a small candidate set, which is exactly what RRF gives you.

The output is the top-N (typically N=5) reranked passages to inject into the LLM prompt as context.

## Why it matters

Single-method retrieval has well-documented failure modes:

- **Pure BM25** misses paraphrase and conceptual relevance — a doc that says "MFA" doesn't match a query about "two-factor authentication" without query expansion.
- **Pure dense vector** misses exact-term recall — a query about a specific error code ("ERR_SSL_PROTOCOL_ERROR") underperforms because the embedding space has seen many error codes and can't distinguish.
- **Either method alone, even with k=20 candidates**, often surfaces "topically related but not actually answering" passages because both retrieval models are independent of the LLM's task.

RRF gives you the union of strengths: exact-match recall from BM25 + semantic recall from dense vectors, weighted by where each surfaces a document. The reranker then applies a task-tuned scoring on the small union set, achieving precision a single retrieval pass cannot.

The pattern matters specifically for **agentic RAG** (where the LLM is actively reasoning over retrieved context, not just extracting a snippet): the reranker stage's output is what the LLM gets, so per-passage precision is much more valuable than recall@1000. The cross-encoder gives you that precision.

## When to use it

- Your corpus contains BOTH technical jargon / named entities AND prose-style content. Either-or corpora can sometimes get away with single-method retrieval.
- Queries are user-typed (natural language paraphrase common) rather than form-filled (exact-term match dominant).
- The downstream LLM is doing extractive or reasoning work — precision of the top-5 matters more than recall of the top-100.
- Latency budget tolerates a cross-encoder pass on ~20-50 docs (typically 100-300ms additional for a sub-300M parameter cross-encoder on CPU).

## When *not* to use it

- Extreme low-latency requirements (sub-100ms total retrieval). Drop the cross-encoder; ship just RRF over BM25 + vector.
- Tiny corpora (<10k docs). Pure dense vector retrieval with a high-quality embedding model usually suffices; the marginal precision from reranking doesn't justify the infra.
- Documents are super-short (tweets, log lines, single sentences). BM25's weighting assumptions break down; reranker output saturates; just use dense vectors.
- The corpus is structured / queryable by attributes (SQL, key-value lookup). Use the structured path; RAG is for unstructured content.

## Anatomy

```
                          QUERY
                            │
            ┌───────────────┴───────────────┐
            │                               │
            ▼                               ▼
   ┌──────────────────┐            ┌──────────────────┐
   │ BM25 retrieval   │            │ Dense vector     │
   │ (top-50)         │            │ retrieval (top-50)│
   │ inverted index   │            │ pgvector + HNSW  │
   └──────────────────┘            └──────────────────┘
            │                               │
            └───────────────┬───────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ RRF fusion       │
                  │ k=60, dedup,     │
                  │ top-K=20         │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Cross-encoder    │
                  │ reranker         │
                  │ (one model fwd   │
                  │  per (q, doc))   │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Top-N (typically │
                  │ N=5) into LLM    │
                  │ prompt as ctx    │
                  └──────────────────┘
```

Implementation notes:

- **Eager-load the cross-encoder at startup.** Cross-encoder model load takes seconds; the first query that triggers a lazy load pays that cost (and the model is cached after). Pre-loading at boot keeps p99 latency predictable.
- **Make the reranker pluggable but defaultable to "no-op fallback."** If the cross-encoder fails to load (bad model file, OOM, missing dep), the system should fall back to RRF ordering rather than refusing to serve. Log loudly; degrade gracefully.
- **Pin a discriminator (e.g., `rag.retrieval.mode`) for reversibility.** Modes: `vector-only` (legacy), `bm25-only` (test/fallback), `hybrid-rerank` (full pattern). Lets you A/B compare or roll back if a specific corpus regresses.
- **The cross-encoder model choice matters less than the architecture.** ms-marco-MiniLM-L-12-v2 (33M params) is a strong default. Larger cross-encoders (ms-marco-MiniLM-L-12 then ELECTRA-base) gain precision but cost latency. Pick by load tests on your specific corpus.

## Sub-claims and details

- **BM25's parameter tuning matters less than people fear.** Default Okapi BM25 with k1=1.5, b=0.75 works for almost everything. Per-corpus tuning gains a few points; not worth optimizing until you've validated the full pipeline.
- **HNSW vs IVFFlat for the vector index.** HNSW gives better recall at higher memory; IVFFlat gives better insert throughput at slightly worse recall. For RAG workloads (reads >> writes), HNSW is usually right.
- **Embedding dimension is a knob, not a sacred number.** MiniLM-L6-v2 at 384 dim is a reasonable default. Higher dims (768, 1024) improve recall marginally at significantly more storage cost. Switching dims is expensive (full re-embed of corpus), so commit to one early.
- **The RRF `k` parameter (default 60) damps the importance of individual high ranks.** Higher k means a doc needs to appear in multiple lists to score well; lower k lets a single high-rank-in-one-list win. The default works for most cases.
- **Deduplication before reranking is non-negotiable.** A doc can appear in both BM25 and vector lists; running the cross-encoder on the same (query, doc) twice is waste and skews top-N.
- **Cross-encoder output is calibratable but rarely is.** The raw score is comparable within a (query, candidate-set) pair but not across queries. If you need a "is this a good answer" threshold (not just "which is best of N"), calibrate per-corpus.

## Treatment across sources

- The pattern is named explicitly in **Vespa documentation** (which has shipped first-class BM25 + dense + hybrid scoring since ~2022) and in **Pinecone's hybrid search posts** (which framed RRF for hybrid sparse-dense fusion).
- **OpenAI's evals / cookbook** popularized the cross-encoder reranker stage in 2023-2024 with their hybrid search examples; they typically use Cohere's rerank API as the reranker.
- **Anthropic's contextual retrieval** (late 2024) added an interesting wrinkle: pre-process each chunk to add LLM-generated context BEFORE embedding, then run hybrid search. Improves recall substantially; complementary to the reranker.
- **The original RRF paper** (Cormack, Clarke, Buettcher 2009) was about combining traditional IR systems. The k=60 default is from there. Modern adaptations vary k from 10 to 60 with similar results.
- In **agentic-RAG specifically**, the reranker matters more than in extractive RAG because the LLM's downstream reasoning amplifies passage-quality errors. Retrieval-augmented agents see disproportionate gains from the reranker stage compared to simple QA chatbots.

## Open questions and contradictions

- **Where does query rewriting fit?** Some implementations rewrite the query (HyDE, query expansion, sub-query decomposition) BEFORE retrieval; others rewrite AFTER an initial pass to refine. Both work; the relative value depends on corpus and query distribution. No consensus.
- **Cross-encoder vs LLM-as-reranker.** Some recent work uses a small LLM (1-7B params) as the reranker instead of a cross-encoder, in exchange for better instruction-following ("rerank these passages by relevance to query X"). Latency is significantly higher; precision is sometimes better. Tradeoff not settled.
- **Retrieval at every conversation turn vs once at the start.** For multi-turn conversations, re-retrieving on each turn catches topic drift but adds latency; retrieving once at the start of a "thread" misses new context. Hybrid (e.g., re-retrieve when query embedding shifts > threshold) is sometimes used.
- **Document chunking strategy.** The pattern is silent on how to chunk. Sentence-boundary, fixed-token, semantic-boundary all work differently with reranking. Empirically, slightly larger chunks (300-500 tokens) seem to outperform tiny ones for cross-encoder reranking.

## Related concepts

- [[wiki/concepts/retrieval-augmented-generation]] — parent pattern; hybrid retrieval is one of the retrieval *implementations* under the general RAG umbrella.
- [[wiki/concepts/reasoning-execution-split]] — adjacent; both patterns separate concerns (retrieval-vs-generation; reasoning-vs-execution).
- [[wiki/concepts/agentic-loop]] — when the LLM uses retrieved context to decide tool calls in a loop, retrieval quality compounds.
- [[wiki/concepts/augmented-llm]] — RAG (any flavor) is the canonical augmentation; hybrid is just a quality variant.

## Worked example

- [[wiki/projects/kivora|Kivora]] — 2026-05-26 Phase 2 Wave 3 shipped the full pattern. BM25 (Java-side text search in `master_*` tables; Python-side via dedicated retrieval module) + dense vector (pgvector + MiniLM-L6-v2, 384 dim, HNSW index, top-50 candidates) → RRF merge with default k=60 + dedup → cross-encoder rerank (ms-marco-MiniLM-L-12-v2, eagerly pre-warmed at startup via `rag_rerank_eager_load`) → top-5 into Compass agent's context. The `rag_mode` config supports `vector-only` / `bm25-only` / `hybrid-rerank` for reversibility; tests cover the cross-encoder fallback path explicitly. asyncpg pool migration shipped alongside (the cross-encoder rerank step was holding SQLAlchemy sync connections too long).
