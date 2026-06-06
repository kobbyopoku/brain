---
type: concept
title: Properties as metadata
created: 2026-06-06
updated: 2026-06-06
aliases: [YAML frontmatter metadata, queryable metadata, properties-as-metadata]
tags: [obsidian, dataview, metadata, knowledge-management]
---

# Properties as metadata

> The practice of giving each note type a consistent YAML frontmatter schema so that its fields become a queryable substrate for Dataview, with strict naming and typing rules so notes remain visible to queries.

## Definition

**Properties as metadata** treats YAML frontmatter as structured, queryable data rather than freeform notes. [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] prescribes a consistent property schema per note type — project, task, client, daily — and notes that property names must match exactly between notes and queries, since a single typo makes a note invisible to its query.

## Why it matters

The whole read-not-store dashboard pattern depends on this substrate: queries can only surface what the metadata reliably encodes. Strict naming and typing discipline is therefore not pedantry but the precondition for the dashboard working at all ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Treatment across sources

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] frames consistent YAML frontmatter per note type (project / task / client / daily) as the queryable substrate. Property names must match exactly between notes and queries — one typo makes a note invisible. Dates must be YYYY-MM-DD; numeric fields (e.g. mrr) must be numbers, not strings. A folder convention (01 PROJECTS / 02 TASKS / 03 CLIENTS / 04 DAILY) encodes note type and scopes queries for speed.

## Sub-claims and details

- **Per-type schema**: each note type (project, task, client, daily) carries a consistent frontmatter schema ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Exact-match rule**: property names must match exactly between notes and queries; one typo makes a note invisible ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Typing rules**: dates must be `YYYY-MM-DD`; numeric fields (e.g. `mrr`) must be numbers, not strings ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Folder convention**: `01 PROJECTS / 02 TASKS / 03 CLIENTS / 04 DAILY` encodes note type and scopes queries for speed ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Open questions and contradictions

- None recorded yet.

## Related concepts

- [[read-not-store-dashboard]] — the dashboard pattern that reads this metadata substrate.
- [[daily-ai-briefing]] — the AI layer that interprets the metadata the dashboard surfaces.

## Mentioned in

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]
