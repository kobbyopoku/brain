---
type: concept
title: LLM Wiki Pattern
created: 2026-05-02
updated: 2026-05-02
aliases: [LLM Wiki, Karpathy wiki pattern]
tags: [pattern, knowledge-management, foundational, agent-config]
---

# LLM Wiki Pattern

> A pattern in which an LLM incrementally builds and maintains a persistent, interlinked markdown wiki on top of a curated raw-source collection, instead of retrieving from raw documents on every query.

## Definition

The LLM Wiki pattern places a **persistent, LLM-maintained markdown wiki** between a human's raw source collection and the human's queries. The LLM owns the wiki layer: it ingests new sources, updates entity and concept pages, maintains cross-references, flags contradictions, and grows a synthesis over time. The human curates sources, asks questions, and judges what matters. A schema document (e.g. `CLAUDE.md`) defines conventions and workflows so the LLM behaves like a disciplined maintainer rather than a generic chatbot.

## Why it matters

It changes the unit of work from "retrieve at query time" to "compile knowledge over time." Cross-references already exist; contradictions are already flagged; the synthesis already reflects everything previously read. The wiki gets richer with every source ingested and every question asked — knowledge **compounds**. Contrast with [[retrieval-augmented-generation]], where every query starts from raw fragments.

This is also a workable answer to a problem [[memex]] left open in 1945: *who does the maintenance?* LLMs handle bookkeeping (cross-references, summary updates, consistency) at near-zero marginal cost, which is the part humans abandon when wikis grow.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — original framing of the pattern. Lays out the three-layer architecture (raw / wiki / schema), the three core operations (ingest / query / lint), and the index-vs-log distinction. Frames the human as curator and the LLM as bookkeeper.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — first secondary citation in the wild. Treats Karpathy's LLM Wiki as the conceptual basis for a Claude Code persistent-memory layer, instantiated as a structured Obsidian vault with `/decisions`, `/errors`, `/patterns`, `/sessions`, `/stack` directories plus `Memory.md` and `index.md`. Combines the wiki with [[wiki/entities/claude-mem]] (session-end compression) and [[wiki/entities/claude-subconscious]] (continuous background memory). The source slightly mis-cites the LLM Wiki location (links to a `github.com/karpathy/llm-wiki` URL rather than the gist this wiki uses); content claim is faithful, URL claim is not.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — second wild secondary citation. nateherk runs two LLM Wikis in production (a YouTube transcripts vault with 36+ ingested videos, and a personal "Herk Brain" with meeting notes / decisions / priorities). Cites Karpathy's pattern directly: *"No fancy RAG. No embeddings. No vector DB. Just a folder with markdown files, an index file, and a log file."* Adds one operational extension to the pattern: the [[hot-cache]] (`_hot.md`) — a 500-token file capturing what's most recently active, loaded first on read-mode queries. Cites an X user who reduced query token usage by 95% by introducing this layer (unverified upper bound). Two independent secondary citations is a strong signal the pattern is propagating in the wild.

## Sub-claims and details

- **Three layers, strictly separated**: raw sources (immutable, human-curated), wiki (LLM-owned markdown), schema (co-owned configuration).
- **Three core operations**:
  - [[ingest]] — process a new source into summaries, entities, concepts; update index and log.
  - [[query]] — answer questions against the wiki, with citations; optionally file substantive answers back as synthesis pages.
  - [[lint]] — periodic health check for contradictions, stale claims, orphans, broken links.
- **Index-vs-log distinction**: `index.md` is content-oriented (a catalog), `log.md` is chronological (append-only operations record).
- **Greppable log convention**: entries prefixed `## [YYYY-MM-DD] action | Title` so simple Unix tools can extract the timeline.
- **Compounding**: substantive query answers should be filed back as `synthesis` pages so explorations don't disappear into chat history.
- **Scale**: the pattern targets moderate scale (~100 sources, hundreds of pages). Index file is enough for retrieval at this size; embedding-based RAG infrastructure is unnecessary.
- **Optional tooling**: at larger scale, add a local search engine like [[qmd]] (BM25 + vector + LLM re-rank, with CLI and MCP).
- **Wiki voice**: encyclopedic, cited; speculation belongs in clearly-labeled syntheses.

## Open questions and contradictions

- **How to handle disagreement between LLM synthesis and human intuition?** The pattern is silent on override semantics. Reasonable extension: human edits to wiki pages are authoritative; LLM updates other pages around them.
- **When does the index become a bottleneck?** Karpathy says "moderate scale." A concrete threshold (in number of pages or tokens) would help; absent that, watch for the moment the LLM struggles to read the index in a single pass.
- **Cross-vault links** — when knowledge spans multiple LLM Wikis, how do they reference each other? Not addressed.

## Related concepts

- [[markdown-as-agent-contract]] — the broader meta-pattern; the LLM Wiki is one instance of this family alongside [[design-md]], [[agents-md]], [[skill-md]], [[readme-md]].
- [[retrieval-augmented-generation]] — the contrast case the pattern is positioned against.
- [[memex]] — the 1945 conceptual ancestor.
- [[ingest]] — one of the three core operations.
- [[query]] — one of the three core operations.
- [[lint]] — one of the three core operations.
- [[hot-cache]] — extension to the pattern (nateherk's `_hot.md`) optimizing for recency-of-query.
- [[ai-os-pattern]] — the LLM Wiki sits inside the Knowledge / Context layer of an AI OS.

## Related entities

- [[wiki/entities/andrej-karpathy]] — author of the pattern.
- [[wiki/entities/obsidian]] — recommended editor.
- [[wiki/entities/qmd]] — optional scale-up search tool.
- [[wiki/entities/vannevar-bush]] — predecessor thinker.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
