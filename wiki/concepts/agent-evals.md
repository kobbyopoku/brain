---
type: concept
title: Agent Evals
created: 2026-06-06
updated: 2026-06-06
aliases: [agent evaluation, evals, golden dataset, agent evals]
tags: [ai-agents, evaluation, quality, ai-services]
---

# Agent Evals

> Methods for measuring whether an AI agent actually does its job — by grading it at each checkpoint of a traced human process, and by scoring its outputs against gold-standard examples of the intended outcome.

## Definition

**Agent evals** are evaluation procedures that establish, with evidence, whether an agent produces the intended result. [[wiki/sources/vasuman-forward-deployed-engineering-101]] — the wiki's first dedicated treatment — frames evals two ways:

1. **Process tracing** — trace a human's multi-step process and grade the AI at each checkpoint.
2. **Outcome scoring** — start with gold-standard examples of the intended outcome and measure the agent against them.

Both rest on a **golden dataset**: roughly 20 real queries, hand-labeled, used as the measuring stick.

## Why it matters

The source's novel angle is that evals are not only an engineering QA step — they are an **executive-trust and sales instrument**. Within the [[forward-deployed-engineering|Forward Deployed Engineering]] model, evals are how a builder proves ROI to skeptical, non-technical buyers before deployment. This reframes evaluation from "make the tests pass" to "make the customer believe," which is why the concept is promoted to a standalone page rather than folded into [[retrieval-augmented-generation|RAG]] or general testing.

## Treatment across sources

- [[wiki/sources/vasuman-forward-deployed-engineering-101]] frames it as the first dedicated treatment in the wiki, presenting evals two ways: (1) trace a human's multi-step process and grade the AI at each checkpoint; (2) start with gold-standard examples of the intended outcome and measure against them; plus building a golden dataset (20 real queries, hand-labeled). Novel angle: evals as an executive-trust / sales instrument that proves ROI, not just engineering QA. Distinct from RAG.
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames it as a four-layer framework for voice agents — infrastructure (WER; p50/p95/p99 latency), execution (task success, tool-call accuracy, groundedness via LLM-as-judge), user behavior (barge-in recovery, reprompt rate), and business outcome (containment rate as the primary target). Adds a concrete pre-launch test-set design and a weekly review loop.

## Sub-claims and details

- **Golden dataset**: ~20 real queries, hand-labeled, as the measurement baseline ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Process-tracing evals** grade the agent at each checkpoint of a human's multi-step workflow ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Outcome-scoring evals** measure the agent against gold-standard examples of the intended result ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Evals as a sales instrument** — they prove ROI to skeptical executives, not only engineering quality ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Distinct from RAG** — evals measure behavior, not retrieval ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Four-layer eval framework (voice agents)**: infrastructure (WER; p50/p95/p99 latency), execution (task success, tool-call accuracy, groundedness via LLM-as-judge), user behavior (barge-in recovery, reprompt rate), business outcome (containment rate as the primary target) ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Pre-launch test set**: a 50-conversation test set built before launch, split 40/30/15/10/5 ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Weekly review loop**: sample 20 calls, make one change, run a 48-hour A/B, ship the winner ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Open questions and contradictions

- The 20-query golden-dataset size is the source's heuristic; how it scales with task complexity is unaddressed.

## Related concepts

- [[forward-deployed-engineering]] — evals are phase 2 of the FDE job.
- [[retrieval-augmented-generation]] — the source draws an explicit distinction; evals are not RAG.
- [[ai-automation-services]] — evals are how a services builder proves a delivered agent works.

## Mentioned in

- [[wiki/sources/vasuman-forward-deployed-engineering-101]]
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
