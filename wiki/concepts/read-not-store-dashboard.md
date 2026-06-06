---
type: concept
title: Read-not-store dashboard
created: 2026-06-06
updated: 2026-06-06
aliases: [live query dashboard, Dataview dashboard, read-not-store, zero-maintenance dashboard]
tags: [obsidian, dataview, productivity, knowledge-management, dashboards]
---

# Read-not-store dashboard

> A single note that contains only live queries reading structured metadata from across a vault, displaying what is relevant now — never storing its own content and never requiring manual maintenance.

## Definition

A **read-not-store dashboard** is a dashboard note built entirely from live Dataview queries. It reads structured metadata scattered across other notes and surfaces what matters today, holding no content of its own and needing no manual upkeep. [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] defines six canonical sections — Today's Priorities, Active Projects, Next 7 Days, Client Health, Open Loops, and Revenue Pulse.

## Why it matters

The pattern inverts the usual dashboard, which is a note someone has to keep updating. By reading rather than storing, the dashboard cannot drift out of date — it always reflects the current state of the underlying notes. This fits the wiki owner's interests in knowledge-management systems and small-business operations ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Treatment across sources

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] frames it as the core pattern: a single note containing only live Dataview queries that read structured metadata from across the vault and display what is relevant now, never storing its own content and never requiring manual maintenance. Six canonical sections (Today's Priorities / Active Projects / Next 7 Days / Client Health / Open Loops / Revenue Pulse). LIMIT is used as a prioritization forcing function, not a display cap.

## Sub-claims and details

- **Read-not-store property**: the dashboard holds only queries; it stores no content and needs no manual maintenance ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Six canonical sections**: Today's Priorities, Active Projects, Next 7 Days, Client Health, Open Loops, Revenue Pulse ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **LIMIT as forcing function**: query `LIMIT` is used to force prioritization, not merely to cap what is displayed ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Open questions and contradictions

- None recorded yet.

## Related concepts

- [[properties-as-metadata]] — the queryable substrate the dashboard reads from.
- [[daily-ai-briefing]] — an AI layer that reads this dashboard and synthesizes what the data means.

## Mentioned in

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]
