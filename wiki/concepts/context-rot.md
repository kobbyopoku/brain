---
type: concept
title: Context rot
created: 2026-06-06
updated: 2026-06-06
aliases: [lost in the middle, context decay]
tags: [agents, context, failure-mode]
---

# Context rot

> The degradation of an LLM's performance when important content sits in the middle of a long context window, or when a long-running conversation accumulates and loses nuance.

## Definition

**Context rot** is the failure mode in which an LLM's reasoning degrades because of *where* or *how much* content sits in its context window — not because the content is absent. [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] documents 30%+ performance degradation when key content sits mid-window (Chroma research, corroborated by Stanford's "Lost in the Middle"), a failure that persists even in million-token windows. [[wiki/sources/nurijanian-goal-for-product-managers]] describes the conversational variant: a single bloated chat decays through compaction and loses nuance buried tens of thousands of tokens ago.

## Why it matters

Context rot is the concrete reason that larger context windows do not solve agent reliability, and the reason [[context-management]] and out-of-conversation sources of truth exist. It connects directly to the wiki's [[hot-cache]] and [[llm-wiki-pattern]] concepts, which are strategies for keeping the right content reachable without leaning on a single decaying window.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as 30%+ performance degradation when key content sits mid-window (Chroma research; corroborated by Stanford's "Lost in the Middle"), persisting even in million-token windows — the failure that [[context-management]] exists to fight.
- [[wiki/sources/nurijanian-goal-for-product-managers]] frames it as the failure mode the loop defends against: a single bloated chat decays through compaction and loses nuance buried tens of thousands of tokens ago; the defense is keeping the source of truth (spec, plan, tests, status file) outside the conversation and reloading it each fresh turn.

## Sub-claims and details

- 30%+ performance degradation occurs when key content sits mid-window (Chroma research) ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Corroborated by Stanford's "Lost in the Middle" ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- The degradation persists even in million-token windows ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- A single bloated chat decays through compaction, losing nuance buried tens of thousands of tokens ago ([[wiki/sources/nurijanian-goal-for-product-managers]]).
- The defense is to keep the source of truth (spec, plan, tests, status file) outside the conversation and reload it each fresh turn ([[wiki/sources/nurijanian-goal-for-product-managers]]).

## Open questions and contradictions

- Whether the mid-window degradation ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]) and the compaction-driven decay ([[wiki/sources/nurijanian-goal-for-product-managers]]) are the same mechanism or two distinct failure modes that share a name.

## Related concepts

- [[context-management]] — the harness component that fights context rot.
- [[context-engineering]] — the discipline; context rot is the failure it targets.
- [[hot-cache]] — strategy for keeping high-signal content reachable.
- [[llm-wiki-pattern]] — keeping a durable source of truth outside the conversation.

## Related entities

- [[wiki/entities/akshay_pachaar]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
- [[wiki/sources/nurijanian-goal-for-product-managers]]
