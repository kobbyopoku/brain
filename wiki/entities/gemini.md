---
type: entity
title: Gemini
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: []
tags: [google, ai-model, llm, stub]
---

# Gemini

> Google's AI model/assistant family, positioned in this wiki as the connective intelligence layer at the center of Google and used as a "teacher" model for SFT data generation.

## Profile

This page is a **stub**. Gemini appears in the wiki via [[wiki/sources/shabnam-google-2026-roadmap-keynote]] and [[wiki/sources/athletickoder-building-agents-first-principles]]. No primary source dedicated to Gemini has been ingested.

> Note: distinct from [[wiki/entities/gemini-cli|Gemini CLI]] (a command-line tool). This page covers the Gemini model family.

## Key facts

- Positioned in the I/O 2026 roadmap thread as "the center of Google" — "Not Search. Not Android. Not Chrome. Gemini." ([[wiki/sources/shabnam-google-2026-roadmap-keynote]]).
- Connects previously separate products (Gmail, Maps, Docs, YouTube, Chrome, Android) through one intelligence layer ([[wiki/sources/shabnam-google-2026-roadmap-keynote]]).
- Named Gemini upgrades at I/O 2026 (per cited press): [[wiki/entities/gemini-omni|Gemini Omni]], Gemini 3.5 Flash, Gemini Spark ([[wiki/sources/shabnam-google-2026-roadmap-keynote]]).
- Used as the stronger "teacher" model to sample candidate diagram actions for an SFT dataset ([[wiki/sources/athletickoder-building-agents-first-principles]]).
- Specific model used in the teacher-generation script: `gemini-2.5-flash` ([[wiki/sources/athletickoder-building-agents-first-principles]]).
- Accessed via the google-genai client with `response_mime_type='application/json'` and a JSON schema (structured output) ([[wiki/sources/athletickoder-building-agents-first-principles]]).

## Mentioned in

- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — positioned as the connective intelligence layer at the center of Google.
- [[wiki/sources/athletickoder-building-agents-first-principles]] — used as the stronger "teacher" model (`gemini-2.5-flash`) to generate validated SFT trajectories via structured output.

## Related entities

- [[wiki/entities/gemini-omni]] — multimodal Gemini model highlighted at I/O 2026.
- [[wiki/entities/gemini-cli]] — Google's Gemini command-line tool (distinct from this model family).
- [[wiki/entities/shabnam-774]] — frames Gemini as the center of Google.

## Related concepts
