---
type: source
title: "techwith_ram — Agentic Memory: A Detailed Breakdown"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/techwith_ram/status/2037499938574110770
source_type: x-thread
author: techwith_ram (@techwith_ram)
source_date: 2026-03-27
raw_path: raw/Agentic Memory A Detailed Breakdown.md
content_status: substantive-verbatim
tags: [agentic-memory, memory, vector-database, embeddings, episodic-memory, rag, agent-architecture, chromadb, openai, anthropic]
---

# techwith_ram — Agentic Memory: A Detailed Breakdown

> A practitioner's reference on **agentic memory** — the storage + retrieval + management system that turns a stateless LLM into an agent that carries context, learns from its own history, and improves over time; with a runnable Python/ChromaDB reference implementation.

## TL;DR

The thread argues that memory is what separates a stateless chatbot from an agent that can evolve, and that memory does three jobs at once — **continuity** (identity), **context** (the current task), and **learning** (improving over time). It catalogs four memory types (in-context, external, episodic, semantic/parametric), shows how they flow through an agent loop (retrieve before the LLM call, write after), and provides a working `MemoryStore` + `EpisodicLogger` + `MemoryAugmentedAgent` built on Python + OpenAI embeddings + ChromaDB. It closes with memory-management strategies — time-based decay, importance scoring at write time, and periodic consolidation — because real systems must curate, not just accumulate. (All code is AI-generated, per the author's own disclaimer.)

## Key takeaways

- **Memory does three jobs simultaneously**: *continuity* (who the user is, what's been built together), *context* (current task state — last tool call, result, next step), and *learning* (what worked vs. didn't, improving decisions over time).
- **The field has converged on four memory types**, framed as parts of a brain: in-context, external, episodic, and semantic/parametric. A well-designed system uses a different storage backend for each.
- **In-context memory** is the agent's "working desk" — system prompt, conversation history, tool-call results, retrieved memories, scratchpad. Instantly accessible in a single forward pass, no retrieval step, but bounded by the context window and wiped when the session ends.
- **The sliding-window problem**: long histories overflow the context limit; naive truncation loses early context. Better strategies are summarization (compress old turns), selective retention (keep facts/decisions/tool results, drop small talk), and offload-to-external-memory.
- **External memory** persists outside the model and survives session boundaries, in two flavors: *structured stores* for exact lookup (PostgreSQL, Redis, SQLite — query by key/ID/SQL) and *vector stores* for semantic search (Pinecone, Chroma, pgvector — query by meaning).
- **"Good memory architecture is 20% storage and 80% retrieval design."** Retrieval is the bottleneck — if you don't retrieve the right memory, the agent behaves as if it doesn't exist.
- **Episodic memory** is "the most underappreciated type" — it stores *events* (outcomes of past actions) rather than facts. The simplest form is a structured log written after each completed task (task, approach, outcome, duration, token cost, quality score, notes, embedding).
- **Episodic recall is few-shot learning from personal history**: on a new task, the agent retrieves the most semantically similar past episodes and uses them to pick a strategy — learning from its own experience rather than a handcrafted dataset. A reflection loop closes the cycle.
- **Semantic/parametric memory** is the knowledge baked into model weights at training time. Always available, no retrieval, but frozen at training cutoff, non-updatable at runtime, opaque, and hallucination-prone. The guidance: don't rely on it for time-sensitive, domain-specific, or private data — use external retrieval; treat parametric memory as the fallback for general world knowledge.
- **Mental model**: parametric memory is the agent's "general education"; external + episodic + in-context are its "on-the-job experience." The best agents combine both.
- **Memory bookends the LLM call**: retrieval before, writing after. "The model itself is stateless; the memory system is what gives the illusion of a stateful, aware agent."
- **Reference implementation**: a `MemoryStore` class (ChromaDB persistent client, OpenAI `text-embedding-3-small`, cosine space) exposing `remember` / `recall` (with k, type filter, `min_relevance` threshold) / `forget` (for GDPR/stale data); an `EpisodicLogger` layering `Episode` dataclass logging + `recall_similar`; and a `MemoryAugmentedAgent` that injects retrieved memories into the system prompt before an Anthropic Claude call, then writes memory + logs the episode.
- **Vector-DB guidance**: embeddings are ~1,536 floats (OpenAI); similarity uses cosine similarity (1.0 identical, 0.0 unrelated, −1.0 opposite). Recommended progression — **ChromaDB** for local dev, **pgvector** if already on Postgres (zero extra infra), **Pinecone or Qdrant** for serious scale.
- **Memory management requires a forgetting strategy**, since an ever-growing unfocused store gets noisier, slower, and self-contradictory. Three approaches: (1) **time-based decay** scoring relevance + importance + recency (formula credited to the *Generative Agents* paper, Park et al., 2023); (2) **importance scoring at write time** (ask the LLM to rate 0–1, store only high-scoring items — uses Haiku); (3) **periodic consolidation** — a nightly job merging near-duplicate memories into a canonical summary, "analogous to how human sleep consolidates memories."

## Notable quotes

> "Memory is what turns a stateless system into something that can actually evolve."
> — opening framing

> "Good memory architecture is 20% storage and 80% retrieval design."
> — §External memory

> "The model itself is stateless; the memory system is what gives the illusion of a stateful, aware agent."
> — §How does memory flow through an agent loop?

> "Real memory systems don't just accumulate. They curate."
> — §Memory management

> "Codes are AI-generated."
> — author disclaimer (closing)

## Notes

- This is a **clean, well-structured systematization** of agentic memory rather than novel research — it consolidates patterns already circulating (the four-type taxonomy, the Generative Agents decay formula, vector-DB tiering) into one runnable reference. Useful precisely as a canonical concept anchor for the wiki's memory cluster.
- The thread's **20%-storage / 80%-retrieval** claim directly echoes the wiki's existing RAG critique ([[wiki/sources/akshay_pachaar-x-rag-wrong]]): both argue the hard part is *what you retrieve and how you represent it*, not the storage substrate. Worth cross-referencing — Akshay attacks the chunk-as-unit; techwith_ram attacks retrieval design generally and adds episodic/typed memory as the structured alternative.
- The **episodic-memory-as-few-shot-from-personal-history** idea is the conceptual core that connects this source to [[wiki/sources/nousresearch-hermes-agent]]: Hermes implements exactly this (creates skills/episodes from experience, recalls them on similar tasks) as agent-internal state. This thread is the *generic architecture*; Hermes is one *concrete product* instantiation. The wiki should treat them as theory ↔ implementation pair.
- The four-type taxonomy also maps onto Karpathy's [[wiki/concepts/llm-wiki-pattern]]: an LLM-maintained markdown wiki is one concrete realization of *external memory* (structured-ish, file-backed, human-curated) — distinct from the vector-store flavor this thread emphasizes. Useful contrast: external memory need not be a vector DB.
- The code targets a **dual-vendor stack**: OpenAI for embeddings, Anthropic Claude (`claude-opus-4-6`, `claude-3-haiku-20240307`) for generation — a common production pattern (cheap/strong embeddings from one provider, reasoning from another). Note the model IDs in the source are illustrative/placeholder; the author flags Haiku "use the current available model."
- **Uncertainty / caveats**: the author explicitly states all code is AI-generated — treat the implementations as illustrative scaffolds, not battle-tested. The `consolidate_memories` routine in particular does a `delete(where={})` then re-populate, which is not actually atomic (the author hedges "atomic-ish"); a production version needs transactional or shadow-collection swap semantics.
- The **importance-scoring-at-write-time** pattern (LLM rates its own output 0–1, store only high scorers) is a concrete instance of LLM-as-judge applied to memory curation — a reusable primitive worth filing under memory-management.
- Relevant to [[wiki/projects/clarvyn]] and [[wiki/projects/kivora]] (both ship FastAPI Claude agents with pgvector RAG): the thread's pgvector-when-already-on-Postgres guidance and its episodic-log pattern are directly applicable; episodic memory of past agent actions is currently absent from those stacks per the wiki's notes.

## Mentioned entities

- [[wiki/entities/techwith-ram]] — author of the thread; designed all the accompanying diagrams.
- [[wiki/entities/openai]] — provider of the embedding model (`text-embedding-3-small`, ~1,536 dims) used in the reference code.
- [[wiki/entities/anthropic]] — provider of the Claude models used for generation and importance-scoring in the reference agent.
- [[wiki/entities/chromadb]] — local persistent vector store used as the reference implementation's backend; recommended for local dev.
- [[wiki/entities/pinecone]] — managed vector store cited for serious-scale semantic search.
- [[wiki/entities/pgvector]] — Postgres extension recommended when already on Postgres (zero extra infra).
- [[wiki/entities/qdrant]] — vector store cited alongside Pinecone for scale.
- [[wiki/entities/postgres]] — structured store for exact-lookup external memory.
- [[wiki/entities/redis]] — structured key-value store for exact-lookup external memory.
- [[wiki/entities/sqlite]] — structured store for exact-lookup external memory.
- [[wiki/entities/generative-agents]] — Park et al. (2023) paper credited as the inspiration for the memory-decay scoring formula.

## Related concepts

- [[wiki/concepts/agentic-memory]] — the umbrella concept this source defines (continuity + context + learning; four memory types).
- [[wiki/concepts/in-context-memory]] — the context-window "working desk"; this source's first memory type.
- [[wiki/concepts/external-memory]] — persistent storage beyond the session; structured vs. vector flavors.
- [[wiki/concepts/episodic-memory]] — event/outcome logging; few-shot learning from personal history.
- [[wiki/concepts/parametric-memory]] — knowledge frozen in model weights; the fallback layer.
- [[wiki/concepts/vector-database]] — nearest-neighbor semantic search; "the heart of any serious memory system."
- [[wiki/concepts/embeddings]] — text → vector representation enabling semantic similarity.
- [[wiki/concepts/cosine-similarity]] — the similarity metric used for memory recall.
- [[wiki/concepts/context-window]] — the bounded substrate of in-context memory; source of the sliding-window problem.
- [[wiki/concepts/memory-consolidation]] — periodic merging of near-duplicate memories; one of three forgetting strategies.
- [[wiki/concepts/agentic-loop]] — memory operations bookend the LLM call (retrieve before, write after).
- [[wiki/concepts/retrieval-augmented-generation]] — this source's "20% storage, 80% retrieval" reframes the RAG retrieval-quality problem.
- [[wiki/concepts/augmented-llm]] — memory is one of the augmentations that turns a base LLM into an agent.

## Related sources

- [[wiki/sources/nousresearch-hermes-agent]] — Hermes is a concrete product implementation of this thread's episodic/self-improving memory architecture (agent-internal state).
- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — shares the "retrieval design is the hard part" thesis; attacks the chunk-as-unit where this thread attacks retrieval generally.
- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's LLM-maintained markdown wiki is an alternative (file-backed, human-curated) realization of external memory.
