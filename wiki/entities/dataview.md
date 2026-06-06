---
type: entity
title: Dataview
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [DataviewJS]
tags: [obsidian, plugin, query-engine, knowledge-vault]
---

# Dataview

> Obsidian community plugin that acts as a query engine over a vault; the single plugin that powers CyrilXBT's live "everything that matters today" dashboard.

## Profile

Dataview is an Obsidian community plugin that functions as a query engine for a vault. It lets a user write queries inside any note that pull information from other notes based on their properties, tags, or content, with results rendering live every time the note is opened. It reads YAML frontmatter properties (Obsidian "Properties") and renders `TABLE` / `LIST` queries plus inline DataviewJS expressions. In [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] it is the only plugin the core dashboard requires.

## Key facts

- **Type**: Obsidian community plugin; query engine over the vault ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Inputs**: reads YAML frontmatter properties, tags, and note content.
- **Outputs**: `TABLE` and `LIST` queries plus inline DataviewJS expressions; results render live on every open.
- **Role in CyrilXBT's dashboard**: the only plugin the core dashboard requires; powers every dashboard section.

## Mentioned in

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] — query engine that makes the single-note live dashboard possible (alongside Obsidian Properties).

## Related entities

- [[wiki/entities/obsidian]] — host application; Dataview is installed from Settings → Community Plugins → Browse.
- [[wiki/entities/cyrilxbt]] — author of the dashboard build that relies on Dataview.

## Related concepts

- [[wiki/concepts/llm-wiki-pattern]] — Dataview is the query layer commonly paired with the `type:`/`tags:` frontmatter this pattern uses.
