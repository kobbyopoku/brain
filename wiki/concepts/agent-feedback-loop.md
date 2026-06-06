---
type: concept
title: Agent feedback loop
created: 2026-06-06
updated: 2026-06-06
aliases: [agent feedback loops, feedback loops not perfect prompts]
tags: [agents, agent-skills, evaluation]
---

# Agent feedback loop

> The reframing that for judgement-heavy agent work the engineering problem is the feedback loop, not the prompt — because judgement work lacks the cheap external check that code enjoys, the loop must let the agent generalize feedback and must live where the team already works.

## Definition

The **agent feedback loop** is the central reframing of [[wiki/sources/petradonka-agents-need-feedback-loops]]: for judgement-heavy work, the engineering problem is the loop, not the prompt. Judgement work lacks a cheap external check — unlike code, which has tests and builds — so the loop must (a) let the agent generalize from feedback rather than memorize cases, and (b) live where the team already works.

## Why it matters

It relocates the effort of building reliable agents away from prompt-crafting and toward designing the loop that turns real-world feedback into improved behaviour. The framing explains *why* judgement work is harder to get right than code work (no automatic correctness signal), and it sets up the source's companion arguments — [[principles-over-rules]] (generalize feedback) and [[skills-as-code]] (govern the changes).

## Treatment across sources

- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it as the source's central reframing: for judgement-heavy work the engineering problem is the loop, not the prompt. Judgement work lacks a cheap external check (unlike code's tests/builds); the loop must let the agent generalize feedback and must live where the team already works.

## Sub-claims and details

- For judgement-heavy work, the engineering problem is the loop, not the prompt. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- Judgement work lacks a cheap external check, unlike code which has tests and builds. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- The loop must let the agent generalize feedback (not memorize cases). (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- The loop must live where the team already works. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])

## Open questions and contradictions

- (none surfaced by current sources)

## Related concepts

- [[principles-over-rules]] — how the agent generalizes feedback rather than overfitting.
- [[skills-as-code]] — how feedback-driven changes are governed (reviewed PRs).
- [[agentic-loop]] — the runtime loop; distinct from this improvement/feedback loop over instructions.

## Related entities

- [[wiki/entities/petra-donka]]

## Mentioned in

- [[wiki/sources/petradonka-agents-need-feedback-loops]]
