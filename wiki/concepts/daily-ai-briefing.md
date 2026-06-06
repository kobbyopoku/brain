---
type: concept
title: Daily AI briefing
created: 2026-06-06
updated: 2026-06-06
aliases: [morning briefing, AI daily briefing, daily-ai-briefing, automated morning synthesis]
tags: [ai-automation, obsidian, productivity, knowledge-management, n8n]
---

# Daily AI briefing

> An automated morning routine in which an LLM reads a dashboard and its referenced notes and produces a short natural-language synthesis of what the data means, delivered to the user's daily note.

## Definition

A **daily AI briefing** is a scheduled, automated synthesis: an LLM reads structured data (here, a dashboard plus the files it references) and writes a concise natural-language account of what that data *means* rather than restating it. In [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]], Claude produces a sub-300-word briefing — the most important thing, what needs attention before noon, what is at risk, which client needs attention, and one open decision — auto-delivered to the daily note via N8N at 6 AM with a Telegram ready-notification.

## Why it matters

The briefing is the interpretation layer that sits on top of a [[read-not-store-dashboard|read-not-store dashboard]]: the dashboard surfaces the data, the briefing tells the user what to do about it. This is the third instance of the pattern in the wiki (alongside the briefings attributed to Shruti and Khairallah), and the first to specify the Dataview query layer beneath it ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Treatment across sources

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]] frames it as an automated morning natural-language synthesis: Claude reads the dashboard plus referenced files and produces a sub-300-word briefing of what the data means (most important thing; what needs attention before noon; what's at risk; which client needs attention; one open decision), auto-delivered to the daily note via N8N at 6 AM with a Telegram ready-notification. The source notes this is the third instance in the wiki alongside Shruti and Khairallah, and adds the Dataview query layer beneath the briefing.

## Sub-claims and details

- **Synthesis, not restatement**: the LLM reports what the data means, not just what it says ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Briefing contents**: most important thing; what needs attention before noon; what is at risk; which client needs attention; one open decision ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Length**: under 300 words ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Delivery**: auto-delivered to the daily note via N8N at 6 AM, with a Telegram ready-notification ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).
- **Third instance in the wiki**: alongside briefings attributed to Shruti and Khairallah; this source adds the Dataview query layer beneath the briefing ([[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]).

## Open questions and contradictions

- None recorded yet.

## Related concepts

- [[read-not-store-dashboard]] — the data layer the briefing reads from.
- [[properties-as-metadata]] — the metadata substrate that makes the dashboard, and thus the briefing, possible.

## Mentioned in

- [[wiki/sources/cyrilxbt-obsidian-dashboard-everything-today]]
