---
type: concept
title: Context engineering
created: 2026-06-06
updated: 2026-06-06
aliases: [context engineering, designing infrastructure for intelligence]
tags: [agents, context, claude-code, engineering]
---

# Context engineering

> The discipline of designing what an LLM sees and when — curating the smallest possible set of high-signal tokens that maximize the desired outcome — framed as higher-leverage than prompt engineering.

## Definition

**Context engineering** is the middle of three concentric agent-engineering levels (prompt ⊂ context ⊂ [[harness-engineering|harness]]): managing what the model sees and when ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]). Anthropic's stated goal for it is *the smallest possible set of high-signal tokens that maximize the desired outcome*. Beyond the inference-time framing, several Claude Code sources reframe it as building the *environment* the agent reasons in — clear instructions, documentation, structured repos, memory, and predictable workflows — i.e. "designing infrastructure for intelligence."

## Why it matters

Multiple sources independently argue that context, not prompting, is where the leverage now lives. *"Claude can only reason using the environment you give it"* ([[wiki/sources/suryanshti777-stop-prompting-design-systems]]); *"The future of AI development is not prompt engineering. It's context engineering"* ([[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]]). This matters directly to the human's interest in agentic architecture: the concrete artifacts of context engineering (markdown contracts, context files) are how an agent is made reliable on a real codebase.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as the middle engineering level — managing what the model sees and when — and cites Anthropic's stated goal: the smallest possible set of high-signal tokens that maximize the desired outcome.
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] frames it as *"the highest-leverage improvement you can make,"* better than prompting, because *"Claude can only reason using the environment you give it."*
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]] makes it the central thesis: *"The future of AI development is not prompt engineering. It's context engineering"* — building environments (clear instructions, documentation, structured repos, memory, predictable workflows) is *"designing infrastructure for intelligence."*

## Sub-claims and details

- Anthropic's stated goal for context engineering: the smallest possible set of high-signal tokens that maximize the desired outcome ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Context engineering sits between prompt engineering (inside it) and [[harness-engineering]] (outside it) ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- It is framed as higher-leverage than prompting; the agent can only reason using the environment it is given ([[wiki/sources/suryanshti777-stop-prompting-design-systems]]).
- Building the environment is "designing infrastructure for intelligence" — clear instructions, documentation, structured repos, memory, predictable workflows ([[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]]).

## Open questions and contradictions

- The "smallest set of high-signal tokens" goal ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]) and the "build a rich environment" framing ([[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]]) sit in tension: one minimizes tokens, the other maximizes the surrounding scaffolding. The reconciliation is presumably that the rich environment is *retrieved from* rather than *loaded into* the window — but no source states this explicitly.

## Related concepts

- [[harness-engineering]] — the outer level that context engineering nests inside.
- [[context-management]] — the harness component that operationalizes context engineering at runtime.
- [[context-rot]] — the failure mode context engineering exists to fight.

## Related entities

- [[wiki/entities/akshay_pachaar]]
- [[wiki/entities/anthropic]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]]
- [[wiki/sources/NainsiDwiv50980-ultimate-claude-code-setup]]
