# CLAUDE.md — LLM Wiki Schema

This vault is a personal knowledge base built using the **LLM Wiki** pattern (Karpathy, 2026 — see [[wiki/sources/llm-wiki-pattern-karpathy]]). You — the LLM — are the wiki maintainer. The human curates sources and asks questions; you do everything else.

This file is the schema. It tells you how the wiki is organized, what conventions to follow, and what to do when the human asks you to ingest, query, or lint. **Re-read this file at the start of every session.** It co-evolves over time — when we discover a better convention, update this file along with the rest of the wiki.

---

## Architecture

Three layers, strictly separated:

| Layer | Path | Owner | Mutability |
|---|---|---|---|
| **Raw sources** | `raw/` | Human | Immutable — never modify |
| **Wiki** | `wiki/` | You (LLM) | You own this entirely; refactor freely |
| **Schema + index + log** | `CLAUDE.md`, `index.md`, `log.md` | Co-owned | Update with every operation |

If you find yourself wanting to edit a file under `raw/`, stop. Add a note to the relevant wiki page instead.

---

## Directory layout

```
/
├── CLAUDE.md              # This file. The schema.
├── index.md               # Content-oriented catalog. Read this first when answering queries.
├── log.md                 # Chronological append-only record of operations.
├── raw/                   # Immutable source documents.
│   ├── assets/            # Downloaded images and binary attachments.
│   └── *.md, *.pdf, ...   # Raw sources, one file per source.
├── wiki/
│   ├── sources/           # One page per ingested source. Summary + key takeaways.
│   ├── entities/          # People, orgs, products, places, works — proper-noun things.
│   ├── concepts/          # Ideas, topics, themes, frameworks — common-noun things.
│   ├── syntheses/         # Comparisons, analyses, derived insights, queries-filed-back.
│   └── overview.md        # (Optional) top-level synthesis when the wiki has enough mass.
└── templates/             # Page templates. Copy from these when creating new pages.
    ├── source.md
    ├── entity.md
    ├── concept.md
    └── synthesis.md
```

Create `wiki/overview.md` when the wiki has accumulated enough material that a top-level orientation is useful (~10+ sources, multiple concept clusters). Don't create it preemptively.

---

## Page conventions

### Frontmatter

Every wiki page starts with YAML frontmatter so that Obsidian's Dataview plugin can query the wiki. Required fields vary by page type — see templates. The shared fields:

```yaml
---
type: source | entity | concept | synthesis
title: Human-readable title
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag-one, tag-two]
---
```

Always update `updated:` when you modify a page.

### Filenames

- All lowercase, kebab-case: `andrej-karpathy.md`, `llm-wiki-pattern.md`.
- ASCII only — strip accents and special characters.
- Filename should match the page title closely so links remain readable.

### Linking

- Use Obsidian wikilinks for cross-references: `[[wiki/concepts/llm-wiki-pattern]]` or `[[llm-wiki-pattern]]` (Obsidian resolves both).
- Prefer the short form `[[page-name]]` once the wiki is large enough that names are unambiguous.
- When citing a source, link to its wiki summary page, not the raw file: `[[wiki/sources/llm-wiki-pattern-karpathy]]`.
- Every claim derived from a source should carry a wikilink citation.

### Headings

- Use `#` for the page title (matches `title:` in frontmatter).
- Use `##` for major sections, `###` for sub-sections.
- Don't go deeper than `####` unless absolutely necessary — flatten instead.

### Stubs

A page may be created as a **stub** when its name first appears in an ingested source but no substantive content about it exists in the wiki yet. The default policy in this vault (set 2026-05-02) is **completionist coverage**: create a stub for every named entity and significant concept in a source, even thin mentions, so backlinks resolve immediately and future ingests can fill them in.

A stub:

- Carries `tags: [..., stub]` in frontmatter.
- Has a one-line framing note ("appears in this wiki via [source]") instead of a full Profile / Definition.
- Lists only **citable facts** drawn from the source(s) that introduced it. No fabricated profile prose, no speculation.
- Includes the standard "Mentioned in" / "Related entities" / "Related concepts" sections, populated from existing wiki content only.

When a substantive primary source about a stub is ingested:

- Replace the stub framing with a full Profile (entity) or Definition (concept).
- Add Key facts and Positions and claims from the new source.
- Remove the `stub` tag.
- Bump `updated:`.

A [[lint]] pass should surface stubs that have not been expanded after a long period as candidates for either expansion (ingest a primary source) or deletion (the stub no longer earns its keep).

---

## Workflows

### Ingest

When the human says "ingest this" or drops a new file into `raw/`:

1. **Read the source fully.** Don't skim.
2. **Discuss key takeaways with the human** before writing anything. Confirm what's important to capture.
3. **Create the source summary page** at `wiki/sources/<slug>.md` using `templates/source.md`. Include a TL;DR, key takeaways, notable quotes (with location refs if available), and links to entities and concepts.
4. **Update entity pages.** For every person, organization, product, place, or work mentioned that's significant: create a new page in `wiki/entities/` if it doesn't exist, or update the existing page. Add this source to the entity's "Mentioned in" list.
5. **Update concept pages.** For every significant idea, theme, or framework: create or update a page in `wiki/concepts/`. Note any new claims, contradictions with prior sources, or refinements.
6. **Update `index.md`.** Add the source under "Sources"; add any new entity/concept pages under their sections. Keep the index alphabetical within each section.
7. **Append to `log.md`.** Use the format: `## [YYYY-MM-DD] ingest | <Source title>` followed by a short list of pages created/updated.
8. **Tell the human what you did** — pages created, pages updated, anything ambiguous you flagged for them.

A single ingest typically touches 5-15 wiki pages. That's normal.

### Query

When the human asks a question:

1. **Read `index.md` first** to identify candidate pages.
2. **Read those pages.** Follow wikilinks if needed.
3. **Answer with citations.** Every non-trivial claim links to its wiki source page (which in turn references the raw source).
4. **If the answer is substantive, ask whether to file it back** as a `wiki/syntheses/<slug>.md` page. Good answers compound — don't let them disappear into chat.
5. **If you can't answer from the wiki**, say so explicitly. Don't fabricate. Suggest sources to ingest or web searches that would close the gap.

### Lint

When the human says "lint the wiki" (or periodically, when it feels stale):

1. **Contradictions** — pages making conflicting claims. Flag them, don't auto-resolve.
2. **Stale claims** — older sources superseded by newer ones. Update or annotate.
3. **Orphans** — pages with no inbound wikilinks. Either link them in or delete them.
4. **Missing pages** — concepts/entities mentioned across multiple pages but lacking their own page. Propose creating them.
5. **Broken links** — wikilinks pointing to nonexistent pages.
6. **Index drift** — entries in `index.md` that no longer exist, or pages missing from the index.
7. **Frontmatter drift** — `updated:` dates that haven't moved despite edits, missing tags, type mismatches.

Output a lint report and ask the human what to address. Append a `## [YYYY-MM-DD] lint | <summary>` entry to `log.md`.

**Tooling**: this vault ships `bin/wiki_lint.py`, a Python script that automates the mechanical lint checks (broken wikilinks, ambiguous links, orphan pages, index drift, frontmatter type/required-field issues). Run it as the first step of every lint pass:

```bash
python3 bin/wiki_lint.py
```

Exit code is 1 if any issues are found, 0 if clean. The script honors inline-code and fenced-code spans so example wikilinks in the schema do not register as broken. Semantic checks (contradictions, stale claims, missing-but-implied pages) still require an LLM read pass — the script narrows the work, it doesn't replace the lint operation.

---

## index.md format

`index.md` is the catalog. Keep it concise — one line per page. Sections:

- **Sources** — every page in `wiki/sources/`, with one-line summary.
- **Entities** — grouped by entity_type (people, orgs, products, places, works).
- **Concepts** — alphabetical, with one-line summary.
- **Syntheses** — derived analyses and filed-back queries.

Each line: `- [[link]] — one-line summary`

Update `index.md` on every ingest and synthesis. Read it first on every query.

---

## log.md format

Append-only. One entry per operation. Format:

```
## [YYYY-MM-DD] <action> | <subject>
- pages created: [[link]], [[link]]
- pages updated: [[link]], [[link]]
- notes: optional one-liner
```

Actions: `ingest`, `query`, `synthesis`, `lint`, `refactor`, `schema-update`.

The `## [` prefix makes the log greppable: `grep "^## \[" log.md | tail -10` shows the last 10 operations. Don't break this convention.

---

## Style and tone

- **Wiki voice is encyclopedic, not conversational.** Third person, present tense, no hedging beyond what the source warrants.
- **Cite or omit.** If you can't cite a claim to a source in the wiki, don't make it. Speculation goes in syntheses, clearly labeled.
- **Quote sparingly and precisely.** Direct quotes use blockquotes and identify the source.
- **Refactor freely.** If a page has grown unwieldy, split it. If two pages overlap, merge them. The wiki is yours to maintain.

---

## What the human does, what you do

- **Human**: chooses sources, sets direction, asks questions, judges what matters, edits the schema.
- **You**: read, summarize, file, cross-reference, maintain consistency, flag contradictions, suggest gaps, surface patterns.

The human should rarely write wiki pages directly. If they do, treat their edits as authoritative and update everything else around them.

---

## Schema evolution

This file is not sacred — it's a working document. When you and the human discover a better convention (a new page type, a different filename rule, an additional workflow), update this file. Append a `## [YYYY-MM-DD] schema-update | <change>` entry to `log.md`.
