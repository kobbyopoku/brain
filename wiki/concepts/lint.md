---
type: concept
title: Lint
created: 2026-05-02
updated: 2026-05-02
aliases: [lint, linting, wiki health check]
tags: [operation, llm-wiki, foundational]
---

# Lint

> One of the three core operations of the [[llm-wiki-pattern]]: a periodic health check that surfaces contradictions, stale claims, orphan pages, broken wikilinks, missing pages, index drift, and frontmatter drift across the wiki.

## Definition

To **lint** the wiki is to pass over every page looking for the kinds of decay that come with growth: pages that contradict each other, claims older sources made that newer sources have superseded, pages with no inbound links, wikilinks pointing to nonexistent targets, concepts mentioned across multiple pages without their own page, entries in `index.md` that no longer correspond to a file (and vice versa), and frontmatter fields that have drifted out of sync with the page they describe. Lint produces a report; it does *not* automatically fix things, except for high-confidence mechanical corrections.

## Why it matters

Without periodic linting, the wiki accumulates entropy. Every [[ingest]] is a write to many files, and writes drift apart over time — a fact updated in one place but not another, a renamed entity that left dangling references, an index entry that points to a deleted page. Humans abandon wikis at exactly this stage; LLMs do not get bored, so the maintenance burden the human cannot sustain stays manageable. Lint is the operational answer to the [[memex]]'s unsolved problem of who keeps the trails current.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — defines the operation: "Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for."

## Sub-claims and details

- **Lint categories** (per [[CLAUDE]] § Workflows → Lint):
  1. **Contradictions** between pages. Flag, do not auto-resolve.
  2. **Stale claims** superseded by newer sources. Annotate or update.
  3. **Orphans** — pages with no inbound wikilinks. Either link them in or delete.
  4. **Missing pages** — concepts/entities mentioned across multiple pages but lacking their own page. Propose creation.
  5. **Broken wikilinks** — pointing to nonexistent pages.
  6. **Index drift** — pages missing from `index.md`, or index entries pointing to deleted pages.
  7. **Frontmatter drift** — `updated:` dates that haven't moved, missing tags, type/directory mismatches.
- **Output**: a lint report. Auto-fixes only for high-confidence mechanical issues (broken-link repair where the rename is obvious, missing index entries, frontmatter `updated:` corrections). Anything requiring judgment is flagged for the human.
- **Logging**: every lint pass appends a `## [YYYY-MM-DD] lint | <summary>` entry to `log.md` per the schema.
- **Tooling**: this vault ships a Python lint script at `bin/wiki_lint.py` that automates the mechanical checks (broken links, ambiguous links, orphans, index drift, frontmatter issues). The script is used by both manual lint passes and the weekly remote lint routine. Semantic checks (contradictions, stale claims, missing-but-implied pages) still require an LLM read pass.
- **Cadence**: this vault runs a remote lint weekly (Mondays 09:00 UTC), plus ad-hoc whenever the human asks.

## Open questions and contradictions

- **Stale-claim detection** is the hardest category — there is no mechanical signal that a claim has been superseded; it requires reading both the old page and the new source. The script cannot do this; only the LLM can. As the wiki grows, this will become the slowest part of a lint pass.
- **Orphan policy**: should orphans always be linked or deleted? Some pages might legitimately exist as reference material that the wiki has not yet wired up. Currently the schema says "either link them in or delete them"; a softer "or annotate as deliberately-unlinked" might be useful.
- **Lint frequency**: weekly is the current default but as the wiki gets large, lint may need to chunk over multiple runs.

## Related concepts

- [[llm-wiki-pattern]] — the parent pattern.
- [[ingest]] — sibling operation; lint catches what ingest missed.
- [[query]] — sibling operation; lint surfaces missing pages that future queries would want.

## Related entities

- [[wiki/entities/andrej-karpathy]] — defined the operation.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[CLAUDE]]
- [[wiki/entities/obsidian]] — references lint as a use case for the graph view.
