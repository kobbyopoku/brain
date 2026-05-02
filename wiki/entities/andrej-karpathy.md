---
type: entity
title: Andrej Karpathy
entity_type: person
created: 2026-05-02
updated: 2026-05-02
aliases: [Karpathy]
tags: [ml, llm, education, founder]
---

# Andrej Karpathy

> AI researcher and educator; author of the LLM Wiki pattern that this vault is built on.

## Profile

Karpathy is a researcher and educator known for foundational work in deep learning and for popular educational content on neural networks and LLMs. He appears in this wiki as the originator of the [[llm-wiki-pattern]] — the design pattern for LLM-maintained personal knowledge bases that this vault instantiates. The framing in his gist (the LLM as bookkeeper, the human as curator) is the operating philosophy of this entire vault.

## Key facts

- **Pattern authored**: [[llm-wiki-pattern]] — published as a public gist, dated April 2026 (cited in [[wiki/sources/llm-wiki-pattern-karpathy]]).
- **Recommended workflow**: LLM agent on one side, Obsidian on the other; human curates, LLM maintains.

## Positions and claims

- **Persistent wiki beats per-query RAG** at moderate scale, because knowledge compounds rather than being re-derived. See [[llm-wiki-pattern]], [[retrieval-augmented-generation]].
- **The human's role is curatorial, not custodial.** The LLM does the bookkeeping that humans abandon. Cited in [[wiki/sources/llm-wiki-pattern-karpathy]].
- **The schema is the key configuration file.** What makes the LLM a disciplined wiki maintainer rather than a generic chatbot is a co-evolved instructions document (e.g. `CLAUDE.md`).
- **Index + log replace embedding-based RAG infrastructure** at the scale this pattern targets (~100 sources).

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]] — author and framing voice.

## Related entities

- [[wiki/entities/vannevar-bush]] — Karpathy cites Bush's [[memex]] as a spiritual ancestor of the pattern.
- [[wiki/entities/obsidian]] — Karpathy's recommended editor for working with the wiki.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]]
- [[wiki/concepts/memex]]
- [[wiki/concepts/retrieval-augmented-generation]]
