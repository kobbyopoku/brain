---
type: concept
title: Ralph Wiggum Loop
created: 2026-06-06
updated: 2026-06-06
aliases: [ralph wiggum, bash-loop agent, fresh-context loop]
tags: [agentic-loop, agent-harness, long-horizon-tasks, agentic-ai]
---

# Ralph Wiggum Loop

> An agent pattern in which a coding agent is run repeatedly inside a bash loop, given the same repo context on every iteration, and asked to read the spec + plan, pick the next unchecked task, complete it, run a test, mark it done only if the test passes, and then restart — relying on fresh context per iteration rather than a smarter model.

## Definition

The **Ralph Wiggum loop**, per [[wiki/sources/nurijanian-goal-for-product-managers]], puts an agent in a bash loop that re-runs it against the same repository context each iteration. Every run, the agent reads the spec and plan, selects the next unchecked task, completes it, runs a test, marks the task done only if the test passes, and then the loop restarts. The load-bearing insight is that the value comes from **fresh context per iteration** — durable files (spec, plan, progress) are reloaded each run — not from a more capable model.

## Why it matters

It reframes long-horizon agent reliability as a context-management problem rather than a model-capability problem: progress accrues because each iteration starts clean and reloads durable artifacts, sidestepping context degradation across a long session. The source treats it as the foundational pattern that the `/goal` command productizes.

## Treatment across sources

- [[wiki/sources/nurijanian-goal-for-product-managers]] frames it as the foundational pattern that `/goal` productizes: put an agent in a bash loop, give it the same repo context every run, have it read the spec + plan, pick the next unchecked task, complete it, run a test, mark done only if the test passes, then restart. The load-bearing insight is that the value is fresh context per iteration (durable files reloaded), not a smarter model.

## Sub-claims and details

- The agent runs inside a bash loop and is re-invoked each iteration. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- Each run receives the same repo context. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- The per-iteration cycle is: read spec + plan → pick the next unchecked task → complete it → run a test → mark done only if the test passes → restart. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- The value derives from fresh context per iteration with durable files reloaded, not from a smarter model. ([[wiki/sources/nurijanian-goal-for-product-managers]])
- `/goal` productizes this pattern. ([[wiki/sources/nurijanian-goal-for-product-managers]])

## Open questions and contradictions

- The source does not specify a stop condition for the outer loop, nor how it handles a task that never passes its test.

## Related concepts

- [[ralph-loop]] — the Anthropic two-phase Initializer/Coding-agent variant of the same filesystem-as-continuity idea.
- [[executable-definition-of-done]] — the spec contract that gives each iteration an unambiguous "done" check.
- [[agentic-loop]] — broader substrate; the Ralph Wiggum loop is a specific bash-loop instance.
- [[agent-harness]] — the harness-level concern this pattern addresses.
- [[context-window]] — the constraint that fresh-context-per-iteration is built to work around.

## Related entities

## Mentioned in

- [[wiki/sources/nurijanian-goal-for-product-managers]]
