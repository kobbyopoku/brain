---
type: concept
title: World model
created: 2026-06-06
updated: 2026-06-06
aliases: [world model, agent world model]
tags: [ai, agents, memory, context, stub]
---

# World model

> The aggregate of whatever an agent is aware of and uses to predict its next action — the full context a harness loads, of which memory and skills are two slices.

## Definition

Across sources the term carries two readings. In an agent-harness sense it is the entire context an agent is aware of when predicting the next action; in a generative-AI sense it appears as a named model-research investment area. The wiki currently holds both as citable mentions.

## Why it matters

Appears in this wiki as a unifying frame for agent context — the post that introduces it argues that memory and skills are not separate plugins but two views of one world model — and as one of a vendor's stated AI investment areas.

## Treatment across sources

- [[wiki/sources/tricalt-memory-skills-same-harness]] frames it as the central new concept: "whatever the agent is aware of and what it uses to predict the next action" — the entire aggregate of context the harness loads (codebase layout, tool schemas, file system, last ~20 turns, user preferences). The post argues memory and skills are two slices of one world model, and that every world model outside board games is permanently misspecified.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] lists it as one of Google's investment areas under Gemini Omni (alongside multimodal AI, video generation, AI coding, and AI UI generation) — a thin mention.

## Sub-claims and details

- The agent's world model includes codebase layout, tool schemas, the file system, the last ~20 conversational turns, and user preferences. ([[wiki/sources/tricalt-memory-skills-same-harness]])
- Memory and skills are presented as two slices of one world model, not separate plugins. ([[wiki/sources/tricalt-memory-skills-same-harness]])
- Every world model outside board games is held to be permanently misspecified. ([[wiki/sources/tricalt-memory-skills-same-harness]])

## Open questions and contradictions

- The two sources use "world model" in different registers (agent-context vs. generative-model research). The wiki does not yet reconcile whether these are the same concept or homonyms.

## Related concepts

- [[wiki/concepts/agentic-memory]] — memory as one slice of the world model.
- [[wiki/concepts/claude-code-skills]] — skills as the other slice.
- [[wiki/concepts/context-window]] — the budget the world model is loaded into.
- [[wiki/concepts/multimodal-ai]] — co-listed investment area in the keynote source.

## Related entities

## Mentioned in

- [[wiki/sources/tricalt-memory-skills-same-harness]]
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]]
