# CLAUDE.md — LLM Wiki Schema

This vault is a personal knowledge base built using the **LLM Wiki** pattern (Karpathy, 2026 — see [[wiki/sources/llm-wiki-pattern-karpathy]]). You — the LLM — are the wiki maintainer when working inside this vault, or a read-only consumer when called from another project (see § Modes below).

This file is the schema. It tells you how the wiki is organized, what conventions to follow, and what to do when the human asks you to ingest, query, or lint. **Re-read this file at the start of every session.** It co-evolves over time — when we discover a better convention, update this file along with the rest of the wiki.

---

## Wiki owner

The brain belongs to **[[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]]** (informal: *"Kobby"* / *"Kobby Opoku"*; email: `gentlekobby@gmail.com`; filesystem root: `/Users/kobbyopoku`). When this file refers to *"the human"*, it means Godwin. When the wiki accumulates context, opinions, or decisions, they are *his* context, opinions, and decisions — curated from his perspective.

Godwin is a software engineer working full-time on AI. He runs two organizations and is named PM/CTO Key Expert on a government contract:

- **[[wiki/entities/roam-labs|ROAM Labs]]** — his AI products + services company. Houses three commercial products ([[wiki/projects/vedge|Vedge]] healthcare OS, [[wiki/projects/kivora|Kivora]] *(brand: ROAM GRC)*, [[wiki/projects/clarvyn|Clarvyn]] HR), takes on AI-services client work ([[wiki/projects/coffee-break-with-big-sis|Coffee Break With Big Sis]], [[wiki/projects/stacesprouts|StaceSprouts]]), and ships its own corporate marketing surface ([[wiki/projects/roamlabs|_roamlabs]]).
- **Brolly Africa** *(entity to be added by Godwin separately)* — co-founded venture under which [[wiki/projects/asanti-brokers|Asanti Brokers]] sits.
- **[[wiki/entities/softtech-solutions|SoftTech Solutions]]** subcontracts ROAM Labs for the [[wiki/projects/cpc-rtbvd|CPC RTBVD]] government engagement; Godwin delivers as PM/CTO Key Expert. SoftTech is the prime contractor; CPC (Cocoa Processing Company Plc) is the end client.

Project pages carry `owner_org:` and `affiliation:` frontmatter so Dataview queries can group projects by org. Recognized `affiliation:` values:

- `roam-labs-product` — ROAM Labs owns the IP and the commercial brand. (Vedge / Kivora / Clarvyn.)
- `roam-labs-self` — ROAM Labs as its own marketing surface. (_roamlabs.)
- `roam-labs-internal` — ROAM Labs builds for ROAM Labs's own use; not commercial, not client work. ([[wiki/projects/helm|Helm]].)
- `roam-labs-client-work` — ROAM Labs delivers, the client owns the IP. (Coffee Break With Big Sis / StaceSprouts.)
- `brolly-africa-product` — Brolly Africa owned platform. (Brolly itself.)
- `brolly-africa-client-work` — Brolly Africa delivers, the client owns the IP. (Asanti Brokers.)
- `softtech-subcontract` — SoftTech is prime, ROAM Labs subcontracts the build. (CPC RTBVD.)

When ingesting future sources, keep in mind that *Godwin's interests cluster around* AI services + AI products, agentic architecture, multi-tenant SaaS, healthcare/GRC/HR domains, the African market, and small-business automation. Material outside these clusters is fine to ingest but warrants a brief framing note explaining why it earns wiki-shelf-space.

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

## Modes — maintainer vs. read

This wiki is consumed in two distinct modes. Most of this file is written for **maintainer mode** (you, the agent in a session opened inside the wiki, doing ingest/query/lint). But the wiki may also be read by an agent in a different project — typically via a `~/brain` clone and a user-level `/brain` slash command. In that case you operate in **read mode**, which has its own contract.

### Maintainer mode (default)

You are inside the wiki. You can read everything, write to `wiki/`, update `index.md` and `log.md`, follow every workflow in this file. The rest of this document assumes maintainer mode unless explicitly noted.

### Read mode (when consumed from another project)

You are in a different project's session. The wiki is a read-only resource at `~/brain` (or wherever the user has cloned it). You answer questions by reading the wiki and citing pages.

**Read-mode rules — non-negotiable:**

1. **You are a reader, not a maintainer.** Do not modify any file under the wiki — no edits to `wiki/`, no updates to `index.md`, no appends to `log.md`. If you find an error, flag it in your response; do not fix it from read mode.
2. **Read the schema first.** Re-read this `CLAUDE.md` at the start of every read-mode session before answering, exactly as in maintainer mode.
3. **Use the index, then drill in.** Read `index.md` to find candidate pages; then read those pages; follow wikilinks. If the index isn't enough, grep over `wiki/` for keywords.
4. **Cite specifically.** Every non-trivial claim sourced from the wiki carries a wikilink to the specific page that supports it (e.g. `[[brain/wiki/concepts/foo]]`). The user must be able to follow the citation back to the source.
5. **Silence is honest.** If the wiki does not contain the answer, say so explicitly. Do not fabricate or extrapolate beyond cited content. Suggest sources the user might want to ingest.
6. **Substantive answers should be offered for filing.** If the answer is over ~200 words and synthesizes 2+ wiki pages, end with: *"This would be filable as a synthesis page — say so and I'll switch to maintainer mode and add it."* The user must explicitly opt in before any write happens.
7. **New sources go through `/brain-ingest`, not direct edits.** If the user wants to add a new source while in read mode, the convention is the user-level `/brain-ingest` slash command, which queues the source into `raw/`. The actual wiki-page ingest happens in a separate session inside the wiki.

### Switching modes

Read mode → maintainer mode requires an explicit user signal ("yes, file it as a synthesis", "open a session in the brain"). The signal opens a new session in the wiki itself; do not attempt to do maintenance writes from a foreign project's session.

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
│   ├── projects/          # One page per project the human is (or was) building.
│   ├── syntheses/         # Comparisons, analyses, derived insights, queries-filed-back.
│   └── overview.md        # (Optional) top-level synthesis when the wiki has enough mass.
└── templates/             # Page templates. Copy from these when creating new pages.
    ├── source.md
    ├── entity.md
    ├── concept.md
    ├── project.md
    └── synthesis.md
```

Create `wiki/overview.md` when the wiki has accumulated enough material that a top-level orientation is useful (~10+ sources, multiple concept clusters). Don't create it preemptively.

---

## Page conventions

### Frontmatter

Every wiki page starts with YAML frontmatter so that Obsidian's Dataview plugin can query the wiki. Required fields vary by page type — see templates. The shared fields:

```yaml
---
type: source | entity | concept | project | synthesis
title: Human-readable title
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag-one, tag-two]
---
```

Always update `updated:` when you modify a page.

### Entity types

Entity pages carry an additional `entity_type:` frontmatter field describing what kind of thing the entity is. Recognized values:

- **`person`** — individual humans (authors, founders, named persons referenced in sources).
- **`organization`** — companies, research labs, foundations, government bodies, agencies.
- **`product`** — software products, SaaS platforms, APIs, libraries, frameworks, devices, named tools.
- **`place`** — geographies, jurisdictions, named physical locations.
- **`work`** — published creative works (books, papers, films, songs, posts) when they're the subject of an ingest.
- **`aesthetic-style`** — *(added 2026-05-05)* named design archetypes / aesthetic categories that aren't products or organizations but are catalogued as standalone styles. Examples: `brutalism`, `claymorphism`, `neon`, `glassmorphism`, `retro`, `editorial`, `minimal`. These typically come from design-system catalogs (e.g. [[wiki/sources/open-design-catalog|Open Design]]) that mix real product brands with named-aesthetic entries. The `aesthetic-style` value lets Dataview queries distinguish *"give me design archetypes"* from *"give me real products"*.

When the right value is genuinely ambiguous (e.g. *"is shadcn/ui a product or an aesthetic?"*), pick the closer fit and tag-extend if needed; the schema isn't strictly enforced, but consistency helps queries.

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

### Adding a project

When the human says "add this project to the brain" or runs the user-level `/brain-add-project` slash command from inside a project directory:

1. **Verify project root.** Check for `.git`, `README.md`, or a stack manifest (`package.json`, `Cargo.toml`, `pyproject.toml`, `pom.xml`, `go.mod`, etc.). If none, ask where the project root is.
2. **Survey the project** — read `README.md`, `CLAUDE.md` (if any), the stack manifest(s), `git remote -v`, recent `git log`, top-level structure (don't read source code line-by-line; understand shape). Sample any `.memory/` directory if present.
3. **Discuss the draft profile with the human** before writing — proposed status, current focus, key decisions, open questions. Wait for explicit confirmation.
4. **Write the project page** at `wiki/projects/<slug>.md` using `templates/project.md`. Slug is kebab-case ASCII.
5. **Update `index.md`** under the `## Projects` section, grouped by status (active / paused / exploring / completed / archived).
6. **Append `log.md`**: `## [YYYY-MM-DD] add-project | <Project name>` with page created and a one-line summary.
7. **Drop a `BRAIN.md` reference at the project root** (a one-line file pointing at `~/brain/wiki/projects/<slug>.md`). Add `BRAIN.md` to the project's `.gitignore` so it stays personal to this clone.
8. **Commit and push the brain.**
9. **Run the lint** (`python3 bin/wiki_lint.py`) to confirm clean.
10. **Tell the human** what was created, page path, and anything ambiguous you flagged.

**Constraints**: do NOT modify project source code; the only project-side write is `BRAIN.md` at the root and a `.gitignore` line. Within the brain, only touch `wiki/projects/<slug>.md`, `index.md`, and `log.md`.

### Updating a project

When the human says "update this project's brain page" or runs `/brain-update-project`:

1. **Find the project's brain page** via `BRAIN.md` at the project root.
2. **Re-survey the project** — same sources as adding. The natural diff window is the brain page's `updated:` date.
3. **Read the existing brain page.**
4. **Identify what changed** — current focus, new decisions, completed open questions, new lessons learned, status transitions.
5. **Discuss the diff with the human** before writing. Surgical edits only — do not rewrite wholesale.
6. **Edit the page**; bump `updated:` to today.
7. **If a lesson generalizes**, propose creating a concept page in `wiki/concepts/` and linking from the project page.
8. **Update `index.md`** if status changed.
9. **Append `log.md`**: `## [YYYY-MM-DD] update-project | <name>` with a one-line summary of what changed.
10. **Commit, push, lint** as above.

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
- **Projects** — grouped by status (active, paused, exploring, completed, archived).
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
