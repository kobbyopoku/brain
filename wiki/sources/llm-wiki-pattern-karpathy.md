---
type: source
title: LLM Wiki — Karpathy
created: 2026-05-02
updated: 2026-05-02
content_status: substantive
source_url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
source_type: gist
author: Andrej Karpathy
source_date: 2026-04
raw_path: raw/llm-wiki-pattern-karpathy.md
tags: [pattern, knowledge-management, llm, wiki, foundational]
---

# LLM Wiki — Karpathy

> Karpathy's pattern for using an LLM to incrementally build and maintain a personal knowledge base in markdown, instead of querying raw documents via RAG.

## TL;DR

A persistent, LLM-maintained wiki sits between the human and their raw sources. The LLM ingests each new source, extracts key information, and updates entity pages, concept pages, and cross-references — so knowledge **compounds** instead of being re-derived on every query. The human curates sources and asks questions; the LLM does all the bookkeeping. The wiki is a directory of markdown files; a schema document (e.g. `CLAUDE.md`) is the configuration that makes the LLM a disciplined maintainer rather than a generic chatbot.

## Key takeaways

- The fundamental shift is from **retrieval per query** (RAG) to **a persistent, cumulative artifact** that gets richer with every source ingested. See [[llm-wiki-pattern]] vs [[retrieval-augmented-generation]].
- Three layers, strictly separated: **raw sources** (immutable), **the wiki** (LLM-owned markdown), **the schema** (e.g. `CLAUDE.md`, co-evolved by human and LLM).
- Three core operations: **ingest**, **query**, **lint**. Each is a defined workflow the schema captures so future sessions stay consistent.
- **`index.md`** is content-oriented (catalog of pages); **`log.md`** is chronological (append-only operations record). Together they replace the need for embedding-based RAG infrastructure at moderate scale (~100 sources, hundreds of pages).
- Log-entry prefix convention `## [YYYY-MM-DD] action | Title` makes the log greppable with simple Unix tools.
- Good answers from queries should be **filed back** as `synthesis` pages, so explorations compound just like ingested sources.
- The wiki only works because LLMs handle the bookkeeping that humans abandon — cross-referencing, summary updating, contradiction flagging across many files in one pass. The maintenance burden, not the reading or thinking, is what kills human-maintained wikis.
- Workflow style: Karpathy keeps the LLM agent open on one side and Obsidian on the other. The LLM edits; the human browses live, follows links, watches the graph view. *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*
- Optional tooling layer: a local search engine over the wiki (Karpathy mentions [[qmd]], a hybrid BM25/vector search for markdown). Not needed at small scale — the index file is enough.
- Ergonomic tips: Obsidian Web Clipper for capturing articles; "Download attachments for current file" hotkey to localize images; Obsidian graph view for shape; Marp for slide output; Dataview for frontmatter queries.
- Spiritual ancestor: Vannevar Bush's 1945 [[memex]]. Bush's vision was a private, curated knowledge store with associative trails — closer to this pattern than to what the public web became. The unsolved piece in 1945 was *who maintains it*; LLMs are now that answer.
- The document is **deliberately abstract**. Karpathy frames it as an "idea file" meant to be pasted into your own LLM agent so the two of you can co-design a concrete instantiation that fits your domain.

## Notable quotes

> "The wiki is a persistent, compounding artifact."
> — § The core idea

> "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions."
> — § The core idea

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
> — § The core idea

> "The wiki stays maintained because the cost of maintenance is near zero."
> — § Why this works

> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
> — § Why this works

## Notes

- This source is **constitutive** of this vault: the schema in [[CLAUDE]] is a direct instantiation of the pattern described here. Treat it as the foundational reference — when the schema and the gist disagree, examine which one is wrong.
- Karpathy explicitly avoids prescribing directory layout or page formats; that's the human-LLM pair's job. Our specific instantiation lives in [[CLAUDE]] and the four `templates/*.md` files.
- Listed example domains where the pattern applies: personal/journal, deep research, reading a book, business/team wikis, competitive analysis, due diligence, trip planning, course notes, hobby deep-dives. Useful prompts when deciding what new vaults to spin up.
- The pattern is opinionated about **moderate scale**. At very small scale you don't need it; at very large scale (thousands of sources) you'd need real search infrastructure. The sweet spot is dozens to low hundreds of sources.
- One thing the gist underspecifies: how to handle disagreement between the LLM's synthesis and the human's intuition. In practice, the schema should make space for the human to override or annotate.

## Mentioned entities

- [[wiki/entities/andrej-karpathy]] — author of the gist; framing voice throughout.
- [[wiki/entities/vannevar-bush]] — 1945 Memex predecessor cited as spiritual ancestor.
- [[wiki/entities/obsidian]] — the recommended editor; the gist's working environment.
- [[wiki/entities/qmd]] — optional local search engine for markdown wikis at scale.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]] — the pattern itself, abstracted from this source.
- [[wiki/concepts/retrieval-augmented-generation]] — the contrast case the pattern is positioned against.
- [[wiki/concepts/memex]] — the 1945 conceptual ancestor.

## Related sources

_(none yet — this is the first ingested source)_
