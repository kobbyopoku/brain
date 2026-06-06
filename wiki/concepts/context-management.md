---
type: concept
title: Context management
created: 2026-06-06
updated: 2026-06-06
aliases: [context window management]
tags: [agents, harness, context, stub]
---

# Context management

> The harness component responsible for keeping an agent's context window populated with the right tokens at the right time — via compaction, masking, just-in-time retrieval, and delegation.

## Definition

**Context management** is harness component #4 in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]: the runtime machinery that decides what goes into, stays in, and leaves the context window. It is the operational counterpart to [[context-engineering]] and the harness's primary defense against [[context-rot]].

## Why it matters

Context management is where the agent's reliability under long-running tasks is won or lost; it is the concrete mechanism that turns the principles of [[context-engineering]] into runtime behavior.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as harness component #4, listing strategies: compaction, observation masking (JetBrains Junie), just-in-time retrieval (grep/glob/head/tail), and sub-agent delegation (1-2k-token condensed summaries). Cites ACON: 26-54% token reduction at 95%+ accuracy.

## Sub-claims and details

- Strategy — compaction ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Strategy — observation masking, as in JetBrains Junie ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Strategy — just-in-time retrieval via grep/glob/head/tail ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Strategy — sub-agent delegation returning 1-2k-token condensed summaries ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- ACON reports 26-54% token reduction at 95%+ accuracy ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Open questions and contradictions

- Unresolved by current sources: how the strategies trade off against each other and when each is preferred.

## Related concepts

- [[harness-engineering]] — the discipline; context management is one of its components.
- [[context-engineering]] — the principles context management operationalizes.
- [[context-rot]] — the failure mode it defends against.
- [[agent-harness]] — the artifact it is a component of.

## Related entities

- [[wiki/entities/akshay_pachaar]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
