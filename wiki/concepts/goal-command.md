---
type: concept
title: /goal command
created: 2026-06-06
updated: 2026-06-06
aliases: ["/goal", "goal command", "goal primitive"]
tags: [agentic-ai, coding-agents, primitive, claude-code, orchestration]
---

# /goal command

> An emerging cross-vendor coding-agent primitive that shifts the interaction model from *prompting* to *assigning*: a goal records a done-state, is submitted once, and stays active until achieved, paused, blocked, cleared, or out of budget.

## Definition

`/goal` is an interactive-session primitive for coding agents. [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] defines it by contrast with a prompt: where a prompt is a one-shot instruction, a goal records a *done-state*, is submitted once, and remains active until it is achieved, paused, blocked, cleared, or runs out of budget. Saboo argues a real `/goal` is distinct from a one-shot prompt that merely carries a "goal:" label.

## Why it matters

Saboo frames `/goal` as an emerging cross-vendor primitive — "HTTP is a primitive... /goal is becoming one for coding agents" — i.e. a standardizing building block for how coding agents are operated, encoding a prompting-to-assigning shift in the interaction model.

## Treatment across sources

- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] frames it as the central subject — an emerging cross-vendor primitive defining the prompting-to-assigning shift, and distinguishes a true interactive-session goal from a one-shot prompt with a "goal:" label.

## Sub-claims and details

- "HTTP is a primitive... /goal is becoming one for coding agents" — framed as cross-vendor ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- A goal records a done-state, is submitted once, and stays active until achieved / paused / blocked / cleared / out-of-budget ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- The real interactive-session primitive is distinct from a one-shot prompt with a "goal:" label ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).

## Open questions and contradictions

- Cross-vendor standardization is asserted as in-progress ("becoming one"), not settled ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).

## Related concepts

- [[wiki/concepts/agent-verification]] — the verifier is what makes a `/goal` a contract rather than a promise.
- [[wiki/concepts/reasoning-execution-split]] — related orchestration pattern.
- [[wiki/concepts/agentic-loop]] — broader execution pattern a goal drives.

## Related entities

## Mentioned in

- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]
