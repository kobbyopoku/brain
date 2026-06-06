---
type: concept
title: Agent Harness
created: 2026-06-06
updated: 2026-06-06
aliases: [agent-harness, harness, the-harness]
tags: [agentic-ai, agent-architecture, agent-config]
---

# Agent Harness

> The complete non-model software infrastructure — orchestration loop, tools, memory, context management, state, error handling, guardrails, verification — that wraps an LLM to turn raw weights into a working agent. "If you're not the model, you're the harness."

## Definition

The **agent harness** is everything around the model in an agentic system. [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] defines it as the complete non-model software infrastructure wrapping an LLM, and asserts that two products running on identical weights can differ by 20+ TerminalBench positions on harness quality alone. [[wiki/sources/tricalt-memory-skills-same-harness]] uses "harness" more broadly, framing memory and skills as harnesses of differing breadth — the harness being what loads the world model used to decide the next step.

## Why it matters

The harness is the layer the wiki owner actually builds. Model weights are largely a commodity choice; differentiation, reliability, and capability come from the surrounding orchestration, tools, memory, and guardrails. Treating "the harness" as a first-class concept — distinct from the existing [[wiki/concepts/agents-md|agent-config]] file-format pages — lets the wiki reason about where agent quality is won.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as the core concept it defines: the complete non-model software infrastructure (orchestration loop, tools, memory, context management, state, error handling, guardrails, verification) wrapping an LLM. "If you're not the model, you're the harness." Two products on identical weights can differ by 20+ TerminalBench positions on harness alone. The source enumerates 12 components and 7 decisions.
- [[wiki/sources/tricalt-memory-skills-same-harness]] frames memory as a "broad harness" and skills as a "specific" one; the harness is what loads the world model to decide the next step. The page notes this is distinct from existing agent-config pages and worth a dedicated concept page.

## Sub-claims and details

- The harness comprises the orchestration loop, tools, memory, context management, state, error handling, guardrails, and verification. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- "If you're not the model, you're the harness." ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Two products built on identical weights can differ by 20+ TerminalBench positions on the strength of the harness alone. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- The source enumerates 12 components and 7 decisions for building a harness. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Memory is a "broad harness" and skills are a "specific" harness; both load the world model that decides the next step. ([[wiki/sources/tricalt-memory-skills-same-harness]])

## Open questions and contradictions

- The two sources use "harness" at different granularities — Pachaar as the whole non-model infrastructure, tricalt as a spectrum from broad (memory) to specific (skills). Whether tricalt's broad/specific framing is a subset of, or orthogonal to, Pachaar's 12-component enumeration is not resolved here.

## Related concepts

- [[wiki/concepts/agentic-loop]] — the orchestration loop is the harness's core component.
- [[wiki/concepts/world-model]] — the harness loads the world model used to decide the next step.
- [[wiki/concepts/agentic-memory]] — memory as a "broad harness."
- [[wiki/concepts/skill-md]] — skills as a "specific harness."
- [[wiki/concepts/agent-guardrails]] — guardrails and verification are harness components.
- [[wiki/concepts/agents-md]] — agent-config file formats, distinct from the harness as infrastructure.

## Related entities

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
- [[wiki/sources/tricalt-memory-skills-same-harness]]
