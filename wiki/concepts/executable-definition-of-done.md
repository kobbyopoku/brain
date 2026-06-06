---
type: concept
title: Executable Definition of Done
created: 2026-06-06
updated: 2026-06-06
aliases: [executable done, definition of done as contract, target-state spec]
tags: [product-management, specs, agentic-ai, evaluation]
---

# Executable Definition of Done

> A requirement reframed as a target state with observable behavior — a contract that defines where effort stops rather than a prompt that asks for effort — paired with required validation evidence so an evaluator can judge a transcript on proof rather than vibes.

## Definition

An **executable definition of done**, per [[wiki/sources/nurijanian-goal-for-product-managers]], turns a requirement into a target state with: observable behavior, negative cases, scope boundaries, validation evidence, stop conditions, status-report expectations, and customer-facing success criteria. It is framed as a contract that defines *where effort stops*, not a prompt that asks for effort. Required validation evidence lets an evaluator judge a work transcript on proof rather than on impressions.

## Why it matters

It is the central product-management implication the source draws from agent-loop patterns: for an agent running unattended in a loop to know when it has actually finished, "done" must be specified as something checkable, not described as something desirable. By bundling negative cases, scope boundaries, and stop conditions into the spec, the PM defines the agent's success contract up front, and by requiring validation evidence, the spec makes evaluation auditable instead of subjective.

## Treatment across sources

- [[wiki/sources/nurijanian-goal-for-product-managers]] frames it as the central PM implication: requirements must become target states with observable behavior, negative cases, scope boundaries, validation evidence, stop conditions, status-report expectations, and customer-facing success criteria — a contract that defines where effort stops, not a prompt that asks for effort. Paired with required validation evidence so an evaluator can judge a transcript on proof, not vibes.

## Sub-claims and details

- A requirement should become a target state with observable behavior. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- The spec must include negative cases, scope boundaries, and stop conditions. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- The spec must include status-report expectations and customer-facing success criteria. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- It is a contract that defines where effort stops, not a prompt that asks for effort. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- Required validation evidence lets an evaluator judge a transcript on proof, not vibes. ([[wiki/sources/nurijanian-goal-for-product-managers]])

## Open questions and contradictions

- The source does not specify a fixed format or template for capturing these elements, nor how completeness of the contract is itself verified.

## Related concepts

- [[ralph-wiggum-loop]] — the bash-loop pattern this contract gives a checkable "done" to each iteration.
- [[ralph-loop]] — the multi-session variant that likewise depends on a durable, checkable progress spec.

## Related entities

## Mentioned in

- [[wiki/sources/nurijanian-goal-for-product-managers]]
