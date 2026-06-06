---
type: concept
title: Tool scoping
created: 2026-06-06
updated: 2026-06-06
aliases: [tool-minimization, minimal-tool-set, lazy-tool-loading]
tags: [agent-harness, tool-use, context-engineering, agentic-ai]
---

# Tool scoping

> The agent-harness principle that exposing fewer, well-chosen tools improves performance — expose the minimum tool set needed for the current step rather than the full catalog.

## Definition

**Tool scoping** is the design decision, in an agent harness, to limit which tools a model can see at a given moment. Per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]], it is "harness decision #6," and its governing observation is that "more tools often means worse performance." The principle is to expose the minimum tool set needed for the current step, frequently implemented via lazy loading so that the full tool catalog is not held in context at once.

## Why it matters

Tool count interacts directly with context cost and decision quality: a large always-on tool list inflates the context window and gives the model more ways to choose wrong. Scoping tools to the active step both reduces context consumption and narrows the model's choice space, which the source ties to measured performance gains.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as harness decision #6: "more tools often means worse performance." Vercel removed 80% of v0's tools and improved; Claude Code achieves 95% context reduction via lazy loading. Principle: expose the minimum tool set needed for the current step.

## Sub-claims and details

- Described as "harness decision #6" with the maxim "more tools often means worse performance." ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Vercel removed 80% of v0's tools and saw improved performance. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Claude Code achieves a 95% context reduction via lazy loading of tools. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- The governing principle is to expose the minimum tool set needed for the current step. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])

## Open questions and contradictions

- The source gives two anecdotes and one principle but no general rule for *how* to scope (by phase, by intent classification, by retrieval) — the mechanism of selecting the right minimal set is unspecified.

## Related concepts

- [[agent-harness]] — tool scoping is one of the harness's design decisions.
- [[progressive-disclosure]] — lazy loading of tools is progressive disclosure applied to capabilities.
- [[context-window]] — scoping is partly a context-budget optimization.
- [[function-calling]] — the tool-invocation mechanism being scoped.
- [[mcp-server]] — a common source of tools that scoping constrains.

## Related entities

- (Vercel / v0, Claude Code — referenced in source; not yet cited as wiki entities here)

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
