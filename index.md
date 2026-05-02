# index.md — Wiki catalog

The content-oriented index of this wiki. Read this first when answering a query, then drill into the linked pages. See [[CLAUDE]] for conventions and [[log]] for the chronological record of operations.

**Stats**: 2 sources · 25 entities · 11 concepts · 0 syntheses · last updated 2026-05-02

---

## Sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's pattern for LLM-maintained personal knowledge bases; foundational for this vault.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — Refero's curated DESIGN.md catalog for AI coding agents; landing-page clipping.

## Entities

### People

- [[wiki/entities/andrej-karpathy]] — author of the LLM Wiki pattern.
- [[wiki/entities/vannevar-bush]] — 1945 originator of the [[memex]]; conceptual ancestor of the LLM Wiki.

### Products & tools

- [[wiki/entities/obsidian]] — local-first markdown editor; the working environment for this vault.
- [[wiki/entities/qmd]] — local hybrid search engine for markdown wikis at scale.
- [[wiki/entities/refero]] — curated DESIGN.md library + MCP server for AI coding agents.

### Brands in Refero catalog (stubs)

Stub pages awaiting substantive primary sources. Their only current content is a backlink to [[wiki/sources/refero-design-systems-for-ai-agents]] and Refero's mood descriptor.

- [[wiki/entities/acctual]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/antimetal]]
- [[wiki/entities/apple]]
- [[wiki/entities/base44]]
- [[wiki/entities/column]]
- [[wiki/entities/cursor]]
- [[wiki/entities/dia-browser]]
- [[wiki/entities/elevenlabs]]
- [[wiki/entities/family]]
- [[wiki/entities/general-intelligence-company]]
- [[wiki/entities/hyperstudio]]
- [[wiki/entities/linear]]
- [[wiki/entities/mercury]]
- [[wiki/entities/minimalissimo]]
- [[wiki/entities/monopo-saigon]]
- [[wiki/entities/raycast]]
- [[wiki/entities/stripe]]
- [[wiki/entities/superhuman]]
- [[wiki/entities/titan]]

## Concepts

### Operations of the LLM Wiki

- [[wiki/concepts/ingest]] — the write path: process a new raw source into wiki pages.
- [[wiki/concepts/lint]] — periodic health check across the wiki.
- [[wiki/concepts/query]] — the read path: answer questions against the wiki with citations.

### Patterns and meta-patterns

- [[wiki/concepts/llm-wiki-pattern]] — persistent, LLM-maintained markdown wiki built on top of curated raw sources.
- [[wiki/concepts/markdown-as-agent-contract]] — meta-pattern: markdown files as the contract layer between humans and AI agents.
- [[wiki/concepts/memex]] — Vannevar Bush's 1945 vision of a personal, associative knowledge store.
- [[wiki/concepts/retrieval-augmented-generation]] — per-query retrieval over raw documents; contrast case for the LLM Wiki.

### Agent-contract markdown files

- [[wiki/concepts/agents-md]] — *(stub)* AGENTS.md — Codex-flavored project contract.
- [[wiki/concepts/design-md]] — DESIGN.md — design-system reference for AI coding agents.
- [[wiki/concepts/readme-md]] — *(stub)* README.md — older convention being absorbed into the agent-contract family.
- [[wiki/concepts/skill-md]] — *(stub)* SKILL.md — single-capability instructions.

## Syntheses

_(none yet — file substantive query answers here as `wiki/syntheses/<slug>.md`)_

---

## Reading paths

A few suggested entry points into the wiki:

- **"What is this vault and how does it work?"** → [[CLAUDE]] → [[wiki/concepts/llm-wiki-pattern]] → [[wiki/sources/llm-wiki-pattern-karpathy]].
- **"Why this approach over RAG?"** → [[wiki/concepts/retrieval-augmented-generation]] → [[wiki/concepts/llm-wiki-pattern]].
- **"Where does this idea come from historically?"** → [[wiki/concepts/memex]] → [[wiki/entities/vannevar-bush]].
- **"How do markdown files fit into AI tooling more broadly?"** → [[wiki/concepts/markdown-as-agent-contract]] → [[wiki/concepts/design-md]] → [[wiki/entities/refero]].
