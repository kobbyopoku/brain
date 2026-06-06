---
type: entity
title: Qwen
entity_type: product
created: 2026-06-06
updated: 2026-06-06
website: https://github.com/QwenLM
aliases: [qwen3, qwen3-4b-instruct, qwen3-4b-instruct-2507]
tags: [open-model, alibaba, llm, student-model, distillation]
---

# Qwen

> Alibaba's open model family. In this wiki Qwen appears as the **student base model** fine-tuned in the SFT and RL scripts of [[wiki/sources/athletickoder-building-agents-first-principles|On Building Agents From First Principles]]. Distinct from [[wiki/entities/qwen-cli|Qwen CLI]] (the coding-agent CLI built on the same model family).

## Profile

Qwen is Alibaba's family of open-weight language models. Within the first-principles agent-building tutorial it plays the role of the small, trainable **student** model that learns from a larger teacher's structured outputs — `Qwen3-4B-Instruct-2507` is fine-tuned first with supervised fine-tuning (SFT), then further with reinforcement learning (RL) starting from the SFT checkpoint.

## Key facts

- **Publisher**: Alibaba (Qwen team).
- **Model used as student**: `Qwen3-4B-Instruct-2507` — passed to TRL's `SFTTrainer` in `train_sft.py` (cited to [[wiki/sources/athletickoder-building-agents-first-principles]]).
- **RL initialization**: the RL trainer initializes from the SFT checkpoint of that student (`outputs/diagram-sft/final`) (cited to [[wiki/sources/athletickoder-building-agents-first-principles]]).

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]] — Qwen3-4B-Instruct is the student base model fine-tuned in the SFT and RL scripts.

## Related entities

- [[wiki/entities/qwen-cli]] — coding-agent CLI built on the same Qwen model family.

## Related concepts

- [[markdown-as-agent-contract]]
