---
type: entity
title: TRL
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [Transformer Reinforcement Learning]
tags: [product, rl-trainer, huggingface, stub]
---

# TRL

> Appears in this wiki via [[wiki/sources/athletickoder-building-agents-first-principles]].

Hugging Face library used as the worked framework target for training agents in that source.

## Key facts

- **Vendor**: Hugging Face library, cited to [[wiki/sources/athletickoder-building-agents-first-principles]].
- **Characterization**: named alongside [[wiki/entities/unsloth|Unsloth]], [[wiki/entities/prime-rl|PRIME-RL]], [[wiki/entities/verl|verl]], and [[wiki/entities/openrlhf|OpenRLHF]] as "not magic ... mostly infrastructure around this loop" — cited to [[wiki/sources/athletickoder-building-agents-first-principles]].
- **Components used**: provides `SFTConfig`/`SFTTrainer` (used in `train_sft.py`) and `GRPOConfig`/`GRPOTrainer` (used in `train_grpo_trl.py`) — cited to [[wiki/sources/athletickoder-building-agents-first-principles]].
- **GRPOTrainer interface**: accepts a model, a dataset of prompts, and one or more reward functions; it handles generation, reward computation, advantage estimation, and optimization — cited to [[wiki/sources/athletickoder-building-agents-first-principles]].
- **Documentation referenced**: `huggingface.co/docs/trl/index` and the GRPOTrainer docs — cited to [[wiki/sources/athletickoder-building-agents-first-principles]].

## Mentioned in

- [[wiki/sources/athletickoder-building-agents-first-principles]] — Hugging Face Transformer Reinforcement Learning library; SFTTrainer and GRPOTrainer are the worked framework targets.

## Related entities

- [[wiki/entities/unsloth|Unsloth]] — named alongside as alternative trainer infrastructure.
- [[wiki/entities/prime-rl|PRIME-RL]] — named alongside as alternative trainer infrastructure.
- [[wiki/entities/verl|verl]] — named alongside as alternative trainer infrastructure.
- [[wiki/entities/openrlhf|OpenRLHF]] — named alongside as alternative trainer infrastructure.

## Related concepts
