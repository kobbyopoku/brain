---
type: source
title: On Building Agents From First Principles
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/athleticKoder/status/2057091692235481560
source_type: article
author: Anshuman Mishra (@athleticKoder)
source_date: 2026-05-20
raw_path: raw/On Building Agents From First Principles.md
content_status: substantive-verbatim
tags: [agent-training, reinforcement-learning, sft, grpo, post-training, environment-design, reward-hacking, llm-fine-tuning, trl, first-principles]
---

# On Building Agents From First Principles

> A bottom-up, framework-agnostic walkthrough of agent post-training — define an environment, generate teacher trajectories, SFT a student into the valid action space, then RL it toward higher reward — using a toy text-to-diagram (tldraw-style) agent as the running example.

## TL;DR

Anshuman Mishra argues that post-training tutorials "start too high up the stack" (with a trainer/library) when the real conceptual core is much smaller: `prompt -> model action -> environment -> reward -> gradient update`. The post builds that picture from first principles using a deliberately small text-to-diagram agent that emits JSON canvas actions. The load-bearing division of labor: **teacher trajectories solve cold-start, SFT buys you syntax (the action language), RL buys you optimization (higher-reward behavior), and evaluation tells you whether the environment measures the right thing.** Frameworks like TRL / Unsloth / verl / PRIME-RL are "not magic" — they are infrastructure around the same loop, and **agent training is environment design first, algorithm selection second.**

## Key takeaways

- **An agent is a policy inside an environment.** A language model is a distribution over sequences; used as an agent, it produces actions instead of prose. The first question is not "which RL trainer?" but "what is the environment?" — what actions are valid, what executing them does, and how success is measured.
- **The universal loop is `prompt -> model action -> environment -> reward -> gradient update`.** A browser agent, coding agent, spreadsheet agent, robotics planner, math solver, and diagram agent all share this skeleton; they differ only in environment, action space, and reward function.
- **Agent training grounds output in an executable world.** A completion is not good because it sounds plausible — it is good if the JSON parses, the schema validates, the canvas accepts the actions, the requested objects appear, arrows connect correctly, and the layout is understandable.
- **An environment needs only three things**: an input prompt, an action format, and a reward function. The post ships a ~120-line pure-Python `Canvas` env (rectangles / ellipses / diamonds / text / arrows) with no framework — "a framework would make this more scalable; it would not make it more conceptually different."
- **Reward is where the task lives** and where most of the real difficulty is. "The trainer can only optimize the reward you give it." Weak reward (`1 if JSON parses else 0`) teaches validity, not usefulness. The hard part of RL is "constructing an environment where reward is correlated with the behavior you actually want."
- **Judges should be treated as noisy components, not oracles.** For visual tasks a VLM/LLM judge may be needed; log its judgments, inspect failures, compare to human review, add negative tests, and "assume the model will eventually exploit whatever reward signal is easiest to exploit."
- **Teacher trajectories come before RL because of a state-distribution problem.** A base model places most probability mass outside the valid region, so almost every rollout gets zero reward and the gradient carries little information. A stronger model (the post uses Gemini 2.5 Flash with structured output) samples candidate actions; validated traces become the SFT dataset. "Teacher generation is not magic. It is sampling from a stronger policy, executing the output, and keeping the traces that survive."
- **SFT buys syntax; RL buys optimization.** SFT (imitation learning) pulls the student toward demonstrated trajectories — it teaches the grammar of the action space but copies the teacher's quirks and does not directly optimize reward. The canonical pipeline is `base model -> SFT on teacher traces -> RL on environment reward`; the SFT checkpoint is "the initialization that makes on-policy exploration productive," not the final model.
- **RL from first principles (GRPO intuition)**: sample a group of completions per prompt, score them, compute a group-relative advantage `A_i = (r_i - mean(r)) / (std(r) + eps)`, and the simplified loss is `loss = -advantage * logprob(completion tokens)`. Real implementations add clipping, KL penalties, reference models, token masks, distributed rollout, and vLLM — but the core is "move probability mass toward better samples."
- **RL trainers feel more complex than SFT trainers because RL data is produced by the model during training.** Generation and optimization become coupled: as the policy changes, the sampled completions, reward distribution, and gradients all shift. This coupling is why RL needs guardrails (frozen reference model, KL penalty, ratio clipping, reward normalization, length/completion masking).
- **The on-policy view**: SFT trains on external (teacher/human) trajectories with a fixed pre-training distribution; RL trains on the model's *own* trajectories, "locally reshaping probability mass toward the parts of that distribution that worked better." This is why RL can sometimes improve *beyond* the teacher traces.
- **A good environment has four properties**: (1) gives partial credit (graded failure, not all-or-zero); (2) separates syntax from semantics; (3) is hard to exploit; (4) produces useful, inspectable logs (prompt, completion, parse errors, canvas state, reward components, screenshot, judge rationale).
- **Common failure modes are environment / state-distribution failures, not algorithm failures.** No reward → policy isn't visiting valid states (simplify action space, add teacher traces, add partial rewards). Trivial diagrams → reward overvalues validity. Valid JSON ignoring the prompt → reward is mostly syntactic. "If reward goes up but human quality does not, the reward is being gamed" — the most important failure mode.
- **A real tldraw agent changes the validator, not the loop.** Instead of a fake `Canvas`, execute actions inside the real editor, read back shapes/bindings/errors, export a screenshot, and compute reward from that. Once you expose `reward(prompt, completion) -> float` (or `step(state, action) -> next_state, reward, done, info`), you can plug into a tiny trainer, TRL, Unsloth, PRIME-RL, verl, or a custom stack. "The framework changes. The shape of the problem does not."
- **Tooling specifics named**: TRL `SFTTrainer` + `GRPOTrainer`, `accelerate launch`, Qwen3-4B-Instruct as the student base model, optional LoRA/QLoRA, Gemini structured output via `google-genai` + Pydantic schemas, `gemini-2.5-flash` as teacher.
- **Methodological meta-note**: the post is an explicit experiment in AI-assisted speed-writing — "Arguments are mine; writing and structure were refined with GPT 5.5 ... keeping the actual taste, direction, and claims human."

## Notable quotes

> "Before there is a trainer, there is an environment. Before there is reinforcement learning, there is an action space. Before there is an agent, there is a policy producing actions that change some state of the world."

> "Libraries like TRL, Unsloth, PRIME-RL, verl, OpenRLHF, or custom internal trainers are not magic. They are mostly infrastructure around this loop."
> — § An Agent Is a Policy Inside an Environment

> "SFT buys you syntax. RL buys you optimization."

> "The hard part of RL for agents is usually not the policy-gradient equation. The hard part is constructing an environment where reward is correlated with the behavior you actually want."
> — § Reward Is Where the Task Lives

> "I increasingly think of agent training as environment design first and algorithm selection second. The trainer decides how to use the signal. The environment decides what signal exists."

> "Teacher trajectories solve cold start. SFT teaches the action language. RL optimizes behavior inside the environment. Evaluation tells you whether the environment measures the right thing."

> "Once you see this, a tldraw agent is not a special case. A browser agent, coding agent, spreadsheet agent, robotics planner, and math solver all have the same skeleton: state -> action -> validation -> reward -> learning. The rest is engineering."

## Notes

- **This is the wiki's first primary source on the *training* layer of agents.** Almost all prior agent coverage is at the *orchestration / harness* layer (Claude Code agents, hooks, slash commands, DOE framework, Hermes runtime). zodchiii's "job description + trigger + output" framing and this post's `state -> action -> validation -> reward -> learning` skeleton are the same agent viewed at two different altitudes: zodchiii treats the model as a fixed reasoning engine and engineers *around* it; Mishra engineers the model's *policy weights* directly. Worth a synthesis page contrasting the deploy-layer vs train-layer views of "what an agent is."
- **The "reward is being gamed" / reward-hacking emphasis** is a training-layer analogue of [[wiki/concepts/reasoning-execution-split|reasoning-execution-split]]'s reliability concerns and the [[wiki/concepts/anti-ai-slop-machinery|anti-ai-slop-machinery]] Do/Don't discipline — both are about constraining a model so it can't satisfy a metric superficially. Mishra's "add negative tests, penalize the exploit directly, don't rely on a single scalar from one brittle heuristic" is the RL-environment version of the same instinct.
- **Verifier-as-supervision** ("Verifiers turn execution into supervision") is a notable claim worth tracking as the wiki accumulates more RLVR / verifiable-reward material. The toy `validate_completion(text) -> (Canvas|None, errors)` function is a minimal verifier; the partial-credit reward decomposition (`0.25 parse + 0.20 schema + 0.20 renderer + 0.15 entities + 0.10 arrows + 0.10 layout`) is the canonical RLVR reward-shaping pattern.
- **Relevance to Godwin's interests**: directly adjacent to agentic architecture, but a layer below the AI-products / AI-services work — this is about *making* a capable agent policy, not orchestrating an off-the-shelf one. Likely most relevant if ROAM Labs ever needs a domain-specialized small model (e.g. a structured-output agent for a healthcare/GRC schema) rather than prompting a frontier model. The environment-design-first thesis transfers cleanly to any structured-output tool-use task.
- **Authorship caveat**: writing/structure GPT-5.5-assisted, arguments human (Anshuman Mishra). Treat prose as co-authored; treat the claims/taste as Mishra's. No empirical benchmarks are reported — all code is illustrative ("not production code ... meant to expose the mechanism"). The PPO ratio, GRPO advantage, and clipped objective are stated correctly but at tutorial fidelity.
- **Stub-worthy references created for completionist coverage**: Anshuman Mishra (author), Gemini (teacher model — distinct from the existing `gemini-cli` entity), TRL, Unsloth, PRIME-RL, verl, OpenRLHF, vLLM, tldraw, Qwen3 (relate to existing `qwen-cli`), Pydantic, GPT-5.5 (writing assistant). New concept pages warranted: agent post-training pipeline, environment design (RL), reward hacking, GRPO, SFT, teacher trajectories / distillation, RLVR / verifiers.

## Mentioned entities

- [[wiki/entities/anshuman-mishra]] — author (@athleticKoder); writes the argument, GPT-5.5 refines structure.
- [[wiki/entities/gemini]] — stronger teacher model (`gemini-2.5-flash`) used to generate validated SFT trajectories via structured output.
- [[wiki/entities/trl]] — Hugging Face RL library; `SFTTrainer` + `GRPOTrainer` are the worked framework targets.
- [[wiki/entities/unsloth]] — RL/fine-tuning library named as alternative trainer infrastructure.
- [[wiki/entities/prime-rl]] — RL trainer named as scalable alternative.
- [[wiki/entities/verl]] — distributed RL trainer named as scalable alternative.
- [[wiki/entities/openrlhf]] — RL trainer named as alternative infrastructure.
- [[wiki/entities/vllm]] — high-throughput inference engine referenced for RL rollout generation.
- [[wiki/entities/tldraw]] — the canvas editor the toy diagram agent miniaturizes; "a real tldraw agent changes the validator, not the loop."
- [[wiki/entities/qwen]] — Qwen3-4B-Instruct is the student base model in the SFT/RL scripts (relate to existing [[wiki/entities/qwen-cli|qwen-cli]]).
- [[wiki/entities/pydantic]] — used to define the teacher's structured-output JSON schema.
- [[wiki/entities/huggingface]] — host of TRL, `datasets`, and `transformers` used throughout.

## Related concepts

- [[wiki/concepts/agent-post-training]] — this source is the canonical first-principles statement of the SFT→RL pipeline.
- [[wiki/concepts/environment-design]] — "environment design first, algorithm selection second"; the four properties of a good environment.
- [[wiki/concepts/reward-hacking]] — "assume the model will eventually exploit whatever reward signal is easiest"; the most important failure mode.
- [[wiki/concepts/grpo]] — group-relative advantage `A_i = (r_i - mean(r))/(std(r)+eps)`; the RL method demonstrated.
- [[wiki/concepts/supervised-fine-tuning]] — "SFT buys you syntax"; imitation learning into the valid action space.
- [[wiki/concepts/teacher-trajectories]] — stronger-model distillation that solves the RL cold-start problem.
- [[wiki/concepts/rlvr]] — verifiers turning execution into supervision; partial-credit reward decomposition.
- [[wiki/concepts/reasoning-execution-split]] — the deploy-layer reliability concern that mirrors training-layer reward-hacking discipline.
- [[wiki/concepts/agentic-loop]] — `prompt -> action -> environment -> reward -> update` is the training-time analogue of the runtime agentic loop.

## Related sources

- [[wiki/sources/zodchiii-10-claude-code-agents]] — same "what is an agent" question at the orchestration layer ("job description + trigger + output") vs this source's training layer ("policy inside an environment").
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — "reliable agents treat the model as a reasoning engine, not an execution engine"; the deploy-side counterpart to grounding output in an executable environment.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — foundational agent-building course at the harness level; this source is the post-training complement.
