---
type: concept
title: LLM evaluation
created: 2026-06-06
updated: 2026-06-06
aliases: [llm evaluation, llm eval, evaluation, llm-as-a-judge]
tags: [ai-engineering, evaluation, llmops, deepeval, ragas]
---

# LLM evaluation

> The systematic measurement of an LLM system's output quality before and after deployment — without which, per the source, a deployed AI system is "a hallucination machine waiting to fail."

## Definition

LLM evaluation is the practice of systematically measuring the quality of an LLM system's outputs. [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] places it as Phase 6 of an AI-engineer roadmap and names three approaches/tools: DeepEval, RAGAS, and LLM-as-a-Judge.

## Why it matters

The source presents evaluation as non-optional: "A deployed AI system without evaluation is basically a hallucination machine waiting to fail." It is identified as the strongest wiki-novel concept the source exposes — no existing wiki page covers it.

## Treatment across sources

- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] frames it as Phase 6 of the AI-engineer roadmap, naming DeepEval, RAGAS, and LLM-as-a-Judge, with the warning that an unevaluated deployed system is a hallucination machine waiting to fail.

## Sub-claims and details

- Phase 6 of the AI-engineer roadmap ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).
- Named tools/approaches: DeepEval, RAGAS, LLM-as-a-Judge ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).
- "A deployed AI system without evaluation is basically a hallucination machine waiting to fail" ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).

## Open questions and contradictions

- Relationship to [[wiki/concepts/agent-evals]] (agent-specific evaluation) versus general LLM-output evaluation is not delineated by the source.

## Related concepts

- [[wiki/concepts/agent-evals]] — narrower, agent-specific evaluation.
- [[wiki/concepts/ai-engineering]] — broader discipline this is a phase of.
- [[wiki/concepts/llmops]] — operational context for ongoing evaluation.
- [[wiki/concepts/retrieval-augmented-generation]] — RAGAS evaluates RAG pipelines.

## Related entities

## Mentioned in

- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]
