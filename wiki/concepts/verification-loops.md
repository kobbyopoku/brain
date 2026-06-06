---
type: concept
title: Verification loops
created: 2026-06-06
updated: 2026-06-06
aliases: [verification, agent verification]
tags: [agents, harness, verification, stub]
---

# Verification loops

> The harness component that checks an agent's output against ground truth — via rules, visual inspection, or an LLM judge — and the factor that separates toy demos from production agents.

## Definition

**Verification loops** are harness component #10 in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]: the machinery by which an agent's output is validated before it is accepted. The source calls verification the thing that *"separates toy demos from production agents."*

## Why it matters

Verification is the reliability lever in the harness: per the source, it roughly doubles-to-triples output quality, and it is what makes an agent's work trustworthy enough to ship. It is the runtime sibling of the evaluator-optimizer [[agent-workflow-patterns|workflow pattern]].

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as harness component #10 that *"separates toy demos from production agents,"* with three approaches — rules-based (tests/linters/types), visual (Playwright screenshots), and LLM-as-judge. Cites Cherny (verification = 2-3x quality) and Fowler (guides = feedforward vs sensors = feedback).

## Sub-claims and details

- Approach — rules-based verification: tests, linters, type checks ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Approach — visual verification: Playwright screenshots ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Approach — LLM-as-judge ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Cherny: verification yields 2-3x quality ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- Fowler frames verification as guides (feedforward) vs sensors (feedback) ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Open questions and contradictions

- Unresolved by current sources: when to combine the three approaches and how to weigh their cost against the 2-3x quality gain.

## Related concepts

- [[harness-engineering]] — the discipline; verification loops are one of its components.
- [[agent-harness]] — the artifact this is a component of.
- [[agent-workflow-patterns]] — the evaluator-optimizer pattern is the workflow-level analogue.

## Related entities

- [[wiki/entities/akshay_pachaar]]

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
