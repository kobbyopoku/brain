---
type: entity
title: Obsidian
entity_type: product
created: 2026-05-02
updated: 2026-05-02
aliases: []
tags: [tooling, markdown, editor]
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

## Positions and claims

_(none — Obsidian is a tool, not a position-holder.)_

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]] — recommended editor; specific tips on Web Clipper, Dataview, Marp, and image localization.

## Related entities

- [[wiki/entities/andrej-karpathy]] — recommends Obsidian as part of the workflow.
- [[wiki/entities/qmd]] — complementary search tool that can run alongside Obsidian.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]]
