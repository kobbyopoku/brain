---
type: concept
title: Fine-tuning
created: 2026-06-06
updated: 2026-06-06
aliases: [fine-tuning, finetuning, fine tuning]
tags: [fine-tuning, ai-engineering, model-adaptation, lora]
---

# Fine-tuning

> Adapting an existing model to a narrower task by further training it on a smaller, domain-specific dataset — not training a base model from scratch.

## Definition

Fine-tuning is the practice of taking a pre-trained model and adapting it to a narrower task using a smaller, domain-specific dataset. [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] (Stage VI item 2) is explicit that it means adapting an existing model, not training a base model from scratch. [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] (Phase 4) treats it as a modern-LLM-engineering skill, paired with the parameter-efficient methods LoRA and QLoRA.

## Why it matters

Fine-tuning is the adaptation lever between pure prompting and full model training — relevant when domain specialization (e.g., healthcare, GRC, HR) demands behavior a base model does not deliver out of the box. The pairing with LoRA/QLoRA signals the cost-efficient modern approach.

## Treatment across sources

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] frames it as Stage VI item 2; adapting an existing model to a narrower task on a smaller domain-specific dataset, not training a base model from scratch.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] frames it as a Phase 4 modern-LLM-engineering skill, paired with LoRA/QLoRA.

## Sub-claims and details

- It adapts an existing model rather than training one from scratch ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]).
- It uses a smaller, domain-specific dataset targeting a narrower task ([[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]).
- Modern practice pairs it with parameter-efficient methods LoRA and QLoRA ([[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).

## Open questions and contradictions

- Neither source specifies when fine-tuning is preferred over retrieval-augmented generation for injecting domain knowledge; the trade-off is left unstated.

## Related concepts

- [[wiki/concepts/ai-engineering]] — broader; fine-tuning is a sub-skill.
- [[wiki/concepts/retrieval-augmented-generation]] — contrasted with; an alternative route to domain-specific behavior.
- [[wiki/concepts/embeddings]] — sibling representation-layer skill in the same roadmap stage.

## Related entities

## Mentioned in

- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]
