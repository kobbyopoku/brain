---
type: entity
title: Obsidian
entity_type: product
created: 2026-05-02
updated: 2026-06-06
website: https://obsidian.md
aliases: []
tags: [tooling, markdown, editor, claude-code-ecosystem]
---

# Obsidian

> Local-first markdown editor and knowledge graph; the recommended environment for working with an LLM Wiki.

## Profile

Obsidian is a local-first markdown editor that treats a folder of markdown files as a "vault" and renders inter-file `[[wikilinks]]` as a navigable graph. It's the environment this wiki lives in. In Karpathy's pattern, Obsidian is the human's read/browse interface while the LLM agent edits files alongside it — *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*

## Key facts

- **Markdown-native and local-first** — the wiki is plain `.md` files on disk, portable to any other tool.
- **Graph view** — visualizes the wikilink network, useful for spotting hubs and orphans during a [[lint]] pass.
- **Plugin ecosystem relevant to the LLM Wiki**:
  - **Web Clipper** — browser extension that converts web articles to markdown, dropping them into `raw/`. Cited in [[wiki/sources/llm-wiki-pattern-karpathy]].
  - **Dataview** — runs queries over page YAML frontmatter; pairs well with the `type:` and `tags:` fields used in this vault.
  - **Marp** — markdown-based slide decks; lets the LLM produce presentations directly from wiki content.
- **Hotkey trick** — bind "Download attachments for current file" to localize images from clipped articles into `raw/assets/`.

## Use as a Claude Code memory layer (regent0x_)

[[wiki/sources/regent0x-claude-code-247-dev-team]] uses Obsidian beyond the LLM Wiki pattern: as a structured **dev knowledge base** that Claude Code reads and writes to between sessions. Specific structure recommended in that source:

```
/vault
  /decisions      — every architecture decision with context
  /errors         — bugs we hit and how we fixed them
  /patterns       — code patterns that work in our codebase
  /sessions       — summaries of what happened each day
  /stack          — documentation for every tool we use
  Memory.md       — who I am, what I'm building, my preferences
  index.md        — master index of everything in the vault
```

Combined with [[wiki/entities/claude-mem]] (session compression) and [[wiki/entities/claude-subconscious]] (continuous background memory), this turns the vault into the durable memory of a Claude Code workflow.

## As a live dashboard / operating-system substrate (CyrilXBT)

CyrilXBT builds on Obsidian as the **storage layer (Layer 1)** of a personal operating system — the plain-text Markdown vault holding all of the user's information — structured into exactly eight numbered folders (`00 - CAPTURE` through `07 - ARCHIVE`), each note in exactly one folder ([[wiki/sources/cyrilxbt-personal-operating-system]]). In a companion build, a single root note (`Dashboard.md`) reads from the vault to surface "everything that matters today"; two Obsidian features make this possible — **Dataview** (community plugin, installed via Settings → Community Plugins → Browse) and **Properties** (YAML frontmatter metadata) ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Positions and claims

_(none — Obsidian is a tool, not a position-holder.)_

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]] — recommended editor; specific tips on Web Clipper, Dataview, Marp, and image localization.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — used as the persistent-memory layer of a Claude Code dev workflow with the `/decisions`, `/errors`, `/patterns`, `/sessions`, `/stack` structure.
- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — host environment for a single-note live dashboard (`Dashboard.md`) built on Dataview + Properties.
- [[wiki/sources/cyrilxbt-personal-operating-system]] — Layer 1 (storage) of a personal operating system; vault structured into eight numbered folders (`00 - CAPTURE` … `07 - ARCHIVE`).
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — Day-1 environment install; target of the Phase-4 RAG-over-notes "searchable second brain" project.

## Related entities

- [[wiki/entities/andrej-karpathy]] — recommends Obsidian as part of the workflow.
- [[wiki/entities/dataview]] — community plugin / query engine over the vault; powers CyrilXBT's live dashboard.
- [[wiki/entities/n8n]] — orchestration layer that reads/writes the vault on a schedule in CyrilXBT's setups.
- [[wiki/entities/qmd]] — complementary search tool that can run alongside Obsidian.
- [[wiki/entities/claude-mem]] — pairs with Obsidian for session-end memory compression.
- [[wiki/entities/claude-subconscious]] — pairs with Obsidian for continuous background memory.
- [[wiki/entities/claude-code]] — the agent that reads and writes the vault in regent0x_'s setup.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]]
- [[markdown-as-agent-contract]]
