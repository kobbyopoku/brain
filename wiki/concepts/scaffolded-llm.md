---
type: concept
title: Scaffolded LLM
created: 2026-06-06
updated: 2026-06-06
aliases: [model-as-cpu, harness-as-scaffolding, llm-scaffolding]
tags: [agent-harness, agentic-ai, llm-infrastructure, co-evolution]
---

# Scaffolded LLM

> The framing of an agent harness as temporary scaffolding built around a model — the model acting as the "CPU" and the harness as the surrounding "operating system" — where the scaffolding is expected to shrink and be removed as models improve.

## Definition

A **scaffolded LLM** treats the model as a compute core (a "CPU") and the agent harness as the operating system and scaffolding wrapped around it. Per Beren Millidge's framing as relayed in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]], building an agent harness amounts to having "reinvented the Von Neumann architecture": the model is the processing unit and the harness supplies memory, I/O, tools, and control flow around it. The scaffolding metaphor carries a temporal claim — scaffolding exists to support construction and is removed as the building completes.

## Why it matters

The framing sets an explicit expectation about *where harness complexity goes over time*: as models get more capable, the scaffolding required to make them useful should shrink, not grow. It reframes harness engineering as a transitional discipline rather than a permanent surface, and it foregrounds **co-evolution** — models are post-trained with specific harnesses in the loop, so model and harness are not independent.

## Treatment across sources

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it via Millidge: harness = OS / scaffolding around the model-as-CPU; building one means having "reinvented the Von Neumann architecture." Scaffolding is removed as the building completes — harness complexity should shrink as models improve. Notes co-evolution: models are post-trained with specific harnesses in the loop.

## Sub-claims and details

- The model is positioned as a "CPU"; the harness is the surrounding operating system / scaffolding. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Building an agent harness is described as having "reinvented the Von Neumann architecture." ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Scaffolding is temporary by definition — it is removed as the build completes, so harness complexity should decrease as models improve. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])
- Co-evolution: models are post-trained with specific harnesses in the loop, coupling model and harness. ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]])

## Open questions and contradictions

- The claim that harness complexity will shrink as models improve is a prediction, not yet settled; a counter-source could argue harnesses accrete capability (more tools, more orchestration) rather than thin out.

## Related concepts

- [[agent-harness]] — the scaffolding-LLM framing is a lens on what a harness *is*.
- [[agent-post-training]] — the co-evolution claim: models trained with harnesses in the loop.
- [[augmented-llm]] — adjacent framing of a model extended with external capabilities.

## Related entities

- (none yet cited)

## Mentioned in

- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
