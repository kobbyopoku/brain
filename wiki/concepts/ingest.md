---
type: concept
title: Ingest
created: 2026-05-02
updated: 2026-05-02
aliases: [ingest, ingestion]
tags: [operation, llm-wiki, foundational]
---

# Ingest

> One of the three core operations of the [[llm-wiki-pattern]]: processing a new raw source into wiki summaries, entity pages, concept pages, and updates to the index and log.

## Definition

To **ingest** a source is to read it, extract the durable knowledge it carries, and integrate that knowledge into the existing wiki — creating new pages where needed and updating existing pages where the source touches them. It is the *write path* of the LLM Wiki: raw sources flow in, wiki pages flow out (and get amended). The contract is that after a successful ingest, every claim made by the source that the human cares about is either captured in a wiki page or explicitly noted as out of scope.

## Why it matters

Ingest is what makes the wiki **compound** rather than re-derive. Each new source touches multiple existing pages, strengthening or challenging the synthesis already there. Cross-references are added; contradictions are flagged; entities and concepts gain detail. The cost of ingesting source N is roughly constant, but the value compounds because source N is now linked to sources 1..N-1 wherever they overlap. Without ingest, the wiki would be a flat list of summaries — the architecture in [[llm-wiki-pattern]] would collapse to RAG-with-summaries (see [[retrieval-augmented-generation]]).

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — defines the operation in plain terms: "the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages." Karpathy notes that batch ingestion is possible but recommends one-at-a-time with human supervision for higher-fidelity capture.

## Sub-claims and details

- **Workflow steps** (per [[CLAUDE]] § Workflows → Ingest, which instantiates Karpathy's framing for this vault):
  1. Read the source fully.
  2. Discuss key takeaways with the human before writing.
  3. Create the source summary page (`wiki/sources/<slug>.md`).
  4. Create or update entity pages for every significant person, organization, product, place, or work mentioned.
  5. Create or update concept pages for every significant idea, theme, or framework.
  6. Update `index.md`.
  7. Append an entry to `log.md`.
  8. Tell the human what was done.
- **Typical fan-out**: 5-15 wiki pages touched per source. Higher for foundational sources; lower for narrow ones.
- **Cadence**: one source at a time with human supervision, or batched with less supervision. The vault's current convention is one-at-a-time (see [[CLAUDE]]).
- **Discussion-before-writing**: the schema mandates a brief takeaways discussion *before* the LLM creates pages. This is a fidelity safeguard — it lets the human steer emphasis before the wiki accretes.
- **Stub-creation policy**: per the convention introduced 2026-05-02, every named entity in a source gets at least a stub page, even thin mentions, so backlinks resolve immediately. See [[CLAUDE]] § Stubs.

## Open questions and contradictions

- **When does ingest fail mid-flight?** No formal partial-rollback policy exists. If the LLM creates 5 of 10 intended pages and then errors, the wiki is in an intermediate state. Reasonable: append a `## [date] ingest-incomplete | ...` log entry and resume on next run.
- **Re-ingestion**: how do you re-ingest a source whose understanding has shifted (e.g. after the wiki has grown)? Currently undefined. Likely needs a `re-ingest` action distinct from `ingest`.

## Related concepts

- [[llm-wiki-pattern]] — the parent pattern; ingest is one of three core operations.
- [[query]] — sibling operation; ingest writes, query reads.
- [[lint]] — sibling operation; lint catches what ingest missed or where ingests have drifted apart.

## Related entities

- [[wiki/entities/andrej-karpathy]] — defined the operation.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[CLAUDE]]
