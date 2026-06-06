---
title: "On Building Agents From First Principles"
source: "https://x.com/athleticKoder/status/2057091692235481560"
author:
  - "[[@athleticKoder]]"
published: 2026-05-20
created: 2026-05-21
description: "How to define an environment, generate teacher trajectories, fine-tune a student, and improve it with reinforcement learning.Authors: Anshum..."
tags:
  - "agent"
  - "building-agents"
  - "first-principle"
---
![Image](https://pbs.twimg.com/media/HIxBzZ6bAAA6skQ?format=jpg&name=large)

How to define an environment, generate teacher trajectories, fine-tune a student, and improve it with reinforcement learning.

**Authors:** Anshuman Mishra & GPT 5.5 May 20, 2026

\[Editor’s note: Arguments are mine; writing and structure were refined with GPT 5.5. This is partly an experiment in using AI to help speed-write technical research blogs from rough notes, while keeping the actual taste, direction, and claims human.\]

The tutorials on post training start too high up the stack. They begin with a framework. Install this library, define this reward function, run this trainer, watch the reward curve move. That is useful once you already understand what is happening. It is less useful when you are trying to build a mental model of the whole system.

I find it more helpful to start lower down. Before there is a trainer, there is an environment. Before there is reinforcement learning, there is an action space. Before there is an agent, there is a policy producing actions that change some state of the world.

This post is an attempt to build that picture from first principles.

The example will be deliberately small: a text-to-diagram agent. The user asks for a simple diagram, and the model outputs structured JSON actions that create shapes on a canvas. You can think of this as a tiny version of a tldraw-style agent. Instead of clicking around a real editor, the model emits actions like “create a rectangle,” “add a label,” and “connect these two nodes.”

The goal is not to build the world’s best diagram agent. The goal is to understand the shape of agent training itself.

At a high level, the loop is:

**prompt -> model action -> environment -> reward -> gradient update**

Almost every agent-training system is a scaled-up version of this loop. A browser agent, a coding agent, a spreadsheet agent, a robotics planner, a math solver, and a diagramming agent all have the same basic structure. They differ in the environment, the action space, and the reward function.

This is the part that is easy to miss when using frameworks. Libraries like TRL, Unsloth, PRIME-RL, verl, OpenRLHF, or custom internal trainers are not magic. They are mostly infrastructure around this loop: batching, rollout generation, distributed inference, reward computation, logging, reference models, clipping, checkpointing, and scaling.

The conceptual core is much smaller.

## An Agent Is a Policy Inside an Environment

A language model is a distribution over sequences. When we use it as an agent, we are asking this distribution to produce actions instead of ordinary prose.

Given an observation, the model emits an action. In a chat model, the observation is the conversation and the action is the assistant message. In a browser agent, the observation might be the DOM and the action might be a click or a keystroke. In a coding agent, the observation might be the repository state and the action might be a patch. In a diagram agent, the observation is the user request and the action is a JSON object describing shapes and connections.

So the first question is not “which RL trainer should I use?”

The first question is: what is the environment?

The environment defines what actions are valid, what happens when those actions are executed, and how success is measured. In ordinary supervised fine-tuning, this environment is often implicit. We show the model examples of good behavior and ask it to imitate them. In reinforcement learning, the environment becomes explicit. The model tries something, the environment responds, and the reward function decides whether that attempt was good.

For a diagram agent, a completion is not good merely because it sounds plausible. It is good if the JSON parses, the schema is valid, the canvas accepts the actions, the requested objects appear, the arrows connect the right nodes, and the final layout is understandable.

That is the core difference between ordinary chat fine-tuning and agent training. Agent training grounds the model’s output in an executable world.

## The Action Language

Let us start with the smallest possible action space.

The model must return JSON with an actions array. Each action either creates a shape or connects two shapes. A valid completion might look like this:

```json
{
  "actions": [
    {
      "type": "create_shape",
      "id": "frontend",
      "shape": "rectangle",
      "x": 80,
      "y": 100,
      "w": 180,
      "h": 80,
      "text": "Frontend"
    },
    {
      "type": "create_shape",
      "id": "api",
      "shape": "rectangle",
      "x": 340,
      "y": 100,
      "w": 180,
      "h": 80,
      "text": "API"
    },
    {
      "type": "connect",
      "from": "frontend",
      "to": "api",
      "text": "request"
    }
  ]
}
```

This looks simple, but it already contains the essential structure of tool use. The model is no longer just generating text. It is generating instructions that another system will execute.

That changes the training problem. The model has to learn not just what to say, but what the environment will accept.

It has to create shapes before connecting them. It has to use stable IDs. It has to avoid duplicate IDs. It has to keep coordinates finite. It has to avoid invalid shape types. It has to emit parseable JSON. These are not philosophical details. They determine whether the policy can even enter the valid region of the action space.

This is why SFT is often necessary before RL. Before the model can optimize reward, it has to learn the language of the environment.

## A Tiny Environment Without a Framework

An environment needs only three things: an input prompt, an action format, and a reward function.

Here is a minimal pure-Python canvas environment. It supports rectangles, ellipses, diamonds, text blocks, and arrows. The point is not that this canvas is sophisticated. The point is that it gives us a deterministic world in which model outputs can succeed or fail.

```python
# env.py
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from typing import Any

ALLOWED_SHAPES = {"rectangle", "ellipse", "diamond", "text"}

@dataclass
class Shape:
    id: str
    shape: str
    x: float
    y: float
    w: float
    h: float
    text: str = ""

@dataclass
class Arrow:
    source: str
    target: str
    text: str = ""

@dataclass
class Canvas:
    shapes: dict[str, Shape] = field(default_factory=dict)
    arrows: list[Arrow] = field(default_factory=list)

    def create_shape(self, action: dict[str, Any]) -> None:
        shape_id = require_str(action, "id")
        shape_type = require_str(action, "shape")
        if shape_type not in ALLOWED_SHAPES:
            raise ValueError(f"unknown shape type: {shape_type}")
        if shape_id in self.shapes:
            raise ValueError(f"duplicate shape id: {shape_id}")

        x = require_number(action, "x")
        y = require_number(action, "y")
        w = require_number(action, "w")
        h = require_number(action, "h")
        if w <= 0 or h <= 0:
            raise ValueError("shape width and height must be positive")
        if w > 1000 or h > 1000:
            raise ValueError("shape too large")

        self.shapes[shape_id] = Shape(
            id=shape_id,
            shape=shape_type,
            x=x,
            y=y,
            w=w,
            h=h,
            text=str(action.get("text", "")),
        )

    def connect(self, action: dict[str, Any]) -> None:
        source = require_str(action, "from")
        target = require_str(action, "to")
        if source not in self.shapes:
            raise ValueError(f"arrow source does not exist: {source}")
        if target not in self.shapes:
            raise ValueError(f"arrow target does not exist: {target}")
        if source == target:
            raise ValueError("arrow cannot connect a shape to itself")
        self.arrows.append(Arrow(source=source, target=target, text=str(action.get("text", ""))))

    def apply(self, action: dict[str, Any]) -> None:
        action_type = require_str(action, "type")
        if action_type == "create_shape":
            self.create_shape(action)
        elif action_type == "connect":
            self.connect(action)
        else:
            raise ValueError(f"unknown action type: {action_type}")

def require_str(obj: dict[str, Any], key: str) -> str:
    value = obj.get(key)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{key} must be a non-empty string")
    return value

def require_number(obj: dict[str, Any], key: str) -> float:
    value = obj.get(key)
    if not isinstance(value, int | float) or not math.isfinite(value):
        raise ValueError(f"{key} must be a finite number")
    return float(value)

def parse_actions(text: str) -> list[dict[str, Any]]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise ValueError("model output does not contain JSON")
        data = json.loads(text[start : end + 1])

    actions = data.get("actions")
    if not isinstance(actions, list):
        raise ValueError("missing actions array")
    if not actions:
        raise ValueError("actions array is empty")
    if len(actions) > 40:
        raise ValueError("too many actions")
    if not all(isinstance(action, dict) for action in actions):
        raise ValueError("each action must be an object")
    return actions

def validate_completion(text: str) -> tuple[Canvas | None, list[str]]:
    errors: list[str] = []
    canvas = Canvas()

    try:
        actions = parse_actions(text)
    except Exception as exc:
        return None, [str(exc)]

    for i, action in enumerate(actions):
        try:
            canvas.apply(action)
        except Exception as exc:
            errors.append(f"action {i}: {exc}")

    return canvas, errors
```

This already gives us the core of a verifier environment. The model emits text. The environment parses that text, executes the action sequence, and returns errors if something goes wrong.

A framework would make this more scalable. It would not make it more conceptually different.

## Reward Is Where the Task Lives

Once the environment can execute actions, we need to define success.

This is where most of the real difficulty lives. The trainer can only optimize the reward you give it. If the reward is mostly syntactic, the model will learn syntax. If the reward measures task satisfaction, the model has a chance of learning useful behavior. If the reward is brittle, the model will eventually find the brittleness.

For the toy diagram agent, we can combine a few signals. We can reward outputs that parse, actions that validate, layouts that do not overlap, labels that are present, arrows that connect objects, and labels that cover important words from the user request.

```python
# reward.py
from __future__ import annotations

import re

from env import Canvas, validate_completion

def score_layout(canvas: Canvas) -> float:
    if not canvas.shapes:
        return 0.0

    score = 1.0

    shapes = list(canvas.shapes.values())
    for i, a in enumerate(shapes):
        for b in shapes[i + 1 :]:
            ax2, ay2 = a.x + a.w, a.y + a.h
            bx2, by2 = b.x + b.w, b.y + b.h
            overlap = not (ax2 < b.x or bx2 < a.x or ay2 < b.y or by2 < a.y)
            if overlap:
                score -= 0.15

    labeled = sum(1 for shape in shapes if shape.text.strip())
    score += 0.1 * min(labeled, 5)

    score += 0.1 * min(len(canvas.arrows), 5)

    return max(0.0, min(1.0, score))

def score_semantics(prompt: str, canvas: Canvas) -> float:
    prompt_words = set(re.findall(r"[a-zA-Z][a-zA-Z0-9_-]+", prompt.lower()))
    label_words: set[str] = set()
    for shape in canvas.shapes.values():
        label_words.update(re.findall(r"[a-zA-Z][a-zA-Z0-9_-]+", shape.text.lower()))

    important = {w for w in prompt_words if len(w) >= 4}
    if not important:
        return 0.5

    coverage = len(important & label_words) / max(1, len(important))
    return max(0.0, min(1.0, coverage))

def reward(prompt: str, completion: str) -> float:
    canvas, errors = validate_completion(completion)
    if errors or canvas is None:
        return 0.0

    validity = 1.0
    layout = score_layout(canvas)
    semantics = score_semantics(prompt, canvas)

    return 0.4 * validity + 0.3 * layout + 0.3 * semantics
```

This reward is intentionally imperfect. It will miss many things humans care about. It may overvalue labels. It may undervalue aesthetics. It may fail on synonyms. It may reward a diagram that contains the right words but has the wrong structure.

That is fine for a toy environment. In fact, it is useful because it exposes the central problem.

The hard part of RL for agents is usually not the policy-gradient equation. The hard part is constructing an environment where reward is correlated with the behavior you actually want.

A weak reward for this task would be:

1 if JSON parses, else 0

That teaches the model to be valid, but not useful.

A stronger reward might look like this:

```python
reward =
  0.25 * parses_as_json
  0.20 * schema_valid
  0.20 * renderer_accepts
  0.15 * requested_entities_present
  0.10 * arrows_connect_expected_entities
  0.10 * layout_quality
```

For a real tldraw-like agent, some of these can be checked with code. You can validate the schema, execute actions inside the real editor, inspect final shapes, check arrow bindings, count overlaps, and export a screenshot. Other parts may require a judge model. You might ask a VLM or LLM judge whether the screenshot satisfies the user’s intent.

But even then, the judge should be treated as a noisy component of the environment, not as an oracle. Log its judgments. Inspect failures. Compare against human review. Add negative tests. Assume the model will eventually exploit whatever reward signal is easiest to exploit.

## Why Teacher Trajectories Come Before RL

If we start RL from a model that cannot produce valid actions, almost every rollout receives zero reward.

This is not merely an optimization inconvenience. It is a state-distribution problem. Before SFT, the model’s policy places most of its probability mass outside the valid region of the environment. It writes explanations, markdown, malformed JSON, invalid IDs, impossible connections, or plausible-looking actions that the canvas rejects. The environment returns zero. The gradient has very little useful information.

This is why teacher trajectories matter.

A stronger model, such as Gemini, can generate examples of the action language. We can sample multiple completions, validate them, keep the ones that work, and turn them into an SFT dataset. In a single-turn environment, a trajectory is just:

observation: user prompt action: JSON actions reward: validation score

In a multi-turn environment, it becomes:

obs\_0 -> action\_0 -> obs\_1 -> action\_1 -> obs\_2 -> reward

For a richer tldraw-style setup, the trajectory might contain the user request, the visible canvas state, the selected shapes, the model’s action batch, the validator output, the final screenshot, and the reward.

The key point is that teacher generation is not magic. It is sampling from a stronger policy, executing the output in the environment, and keeping the traces that survive.

Here is a minimal sketch using Gemini structured output.

This produces the dataset we need for the first phase. The teacher moves the student into the valid action manifold. It does not solve the whole task. It gives RL somewhere useful to start.

```python
# teacher_generate.py
from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from google import genai
from pydantic import BaseModel, Field

from reward import reward
from env import validate_completion

class CreateShape(BaseModel):
    type: Literal["create_shape"]
    id: str
    shape: Literal["rectangle", "ellipse", "diamond", "text"]
    x: float
    y: float
    w: float
    h: float
    text: str = ""

class Connect(BaseModel):
    type: Literal["connect"]
    from_: str = Field(alias="from")
    to: str
    text: str = ""

class AgentResponse(BaseModel):
    actions: list[CreateShape | Connect]

SYSTEM_PROMPT = """You are a diagramming agent.

The user will ask for a small diagram. Return only JSON with an \`actions\`
array. You can create shapes and connect them.

Rules:
- Create every shape before connecting it.
- Use stable, meaningful shape ids.
- Prefer simple left-to-right or top-to-bottom layouts.
- Avoid overlaps.
- Put short readable labels inside shapes.
- Return only JSON. No markdown.
"""

PROMPTS = [
    "Draw a three step data pipeline: client, API, database.",
    "Draw a login flow with user, auth service, token, and dashboard.",
    "Draw a simple RAG system with documents, embeddings, vector DB, retriever, and LLM.",
    "Draw a CI pipeline with commit, tests, build, deploy.",
    "Draw a checkout flow with cart, payment, fraud check, and receipt.",
]

def generate_one(client: genai.Client, model: str, prompt: str) -> str:
    response = client.models.generate_content(
        model=model,
        contents=f"{SYSTEM_PROMPT}\n\nUser request: {prompt}",
        config={
            "response_mime_type": "application/json",
            "response_json_schema": AgentResponse.model_json_schema(),
        },
    )
    return response.text

def main() -> None:
    client = genai.Client()
    model = "gemini-2.5-flash"

    out_dir = Path("data/diagram_teacher")
    out_dir.mkdir(parents=True, exist_ok=True)
    accepted = out_dir / "train.jsonl"
    rejected = out_dir / "rejected.jsonl"

    with accepted.open("w") as good, rejected.open("w") as bad:
        for prompt in PROMPTS:
            for attempt in range(4):
                completion = generate_one(client, model, prompt)
                canvas, errors = validate_completion(completion)
                score = reward(prompt, completion)

                row = {
                    "prompt": prompt,
                    "completion": completion,
                    "reward": score,
                    "errors": errors,
                }

                if canvas is not None and not errors and score >= 0.6:
                    good.write(
                        json.dumps(
                            {
                                "messages": [
                                    {"role": "system", "content": SYSTEM_PROMPT},
                                    {"role": "user", "content": prompt},
                                    {"role": "assistant", "content": completion},
                                ],
                                "reward": score,
                            }
                        )
                        + "\n"
                    )
                else:
                    bad.write(json.dumps(row) + "\n")

if __name__ == "__main__":
    main()
```

## SFT Buys You Syntax

Supervised fine-tuning is imitation learning.

Given a prompt and a teacher action, the model is trained to increase the probability of that action. For a chat model, each row looks like this:

```json
{
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "Draw a three step data pipeline."},
    {"role": "assistant", "content": "{\"actions\": [...]}"}
  ]
}
```

The important thing to notice is what SFT is and is not doing.

SFT is not asking whether the completion is better than another completion. It is not directly optimizing the reward. It is not exploring the environment. It is pulling the student toward demonstrated trajectories.

For agent training, this is still extremely useful. SFT teaches the model the grammar of the action space. It teaches the model to return JSON, use the right schema, create shapes before connections, and avoid obviously invalid action sequences.

In this sense, SFT buys syntax. It moves the policy from a region where almost every rollout fails into a region where some rollouts are valid enough for reinforcement learning to become meaningful.

A minimal TRL SFT script looks like this:

```python
# train_sft.py
from datasets import load_dataset
from trl import SFTConfig, SFTTrainer

dataset = load_dataset("json", data_files="data/diagram_teacher/train.jsonl", split="train")

args = SFTConfig(
    output_dir="outputs/diagram-sft",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-5,
    num_train_epochs=3,
    max_length=4096,
    logging_steps=10,
    save_steps=100,
)

trainer = SFTTrainer(
    model="Qwen/Qwen3-4B-Instruct-2507",
    args=args,
    train_dataset=dataset,
)

trainer.train()
trainer.save_model("outputs/diagram-sft/final")
```

Run it with:

```bash
accelerate launch train_sft.py
```

You can add LoRA or QLoRA if you want. You can scale the dataset. You can use multiple teachers. Those are important engineering choices, but they do not change the conceptual role of this phase.

After SFT, the model should produce syntactically valid action sequences much more often. That is enough to unlock the next phase.

## RL Buys You Optimization

If SFT teaches the model to imitate good traces, why do RL at all?

Because the teacher traces are static. They show what the teacher did on the prompts we generated. They do not directly optimize the metric we care about.

SFT says: make this teacher answer more likely.

RL says: make high-reward answers more likely.

That difference matters.

Suppose the teacher creates a valid diagram, but the layout is cramped. SFT will copy the cramped layout. RL can discover a cleaner layout if the reward values spacing. Suppose the teacher labels a node “DB,” but the reward gives higher semantic coverage for “Database.” RL can move toward “Database.” Suppose there are many valid diagrams for the same prompt. SFT collapses toward the teacher’s style. RL can reinforce whichever variants score better under the environment.

This is the basic division of labor:

SFT buys you syntax. RL buys you optimization.

The usual pipeline is therefore:

base model -> SFT on teacher traces -> RL on environment reward

The SFT checkpoint is not the final model. It is the initialization that makes on-policy exploration productive.

## RL From First Principles

The simplest online RL loop for LLMs is not complicated.

Sample a batch of prompts. Generate multiple completions for each prompt. Score each completion with the environment. Convert those scores into advantages. Increase the probability of completions that did better than their siblings. Decrease, or at least stop increasing, the probability of completions that did worse.

This is the intuition behind group-relative methods like GRPO. For a prompt x, the model samples a group of completions:

y\_1, y\_2, ..., y\_G

The environment scores them:

r\_1, r\_2, ..., r\_G

Then we compute a group-relative advantage:

**A\_i = (r\_i - mean(r)) / (std(r) + eps)**

If a completion is better than its siblings, its advantage is positive. If it is worse, its advantage is negative.

The simplified loss is:

**loss = - advantage \* logprob(completion tokens)**

Real implementations add clipping, KL penalties, reference models, token masks, distributed rollout generation, vLLM inference, caching, and many stability tricks. But the core idea is still this: sample from the current policy, evaluate with the environment, and move probability mass toward better samples.

Here is a deliberately bare trainer sketch. It is not production code. It is meant to expose the mechanism.

```python
# train_rl_minimal.py
from __future__ import annotations

import json
import random

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from reward import reward

SYSTEM_PROMPT = """You are a diagramming agent. Return only JSON with an actions array."""

PROMPTS = [
    "Draw a three step data pipeline: client, API, database.",
    "Draw a login flow with user, auth service, token, and dashboard.",
    "Draw a simple RAG system with documents, embeddings, vector DB, retriever, and LLM.",
    "Draw a CI pipeline with commit, tests, build, deploy.",
    "Draw a checkout flow with cart, payment, fraud check, and receipt.",
]

def format_prompt(tokenizer, user_prompt: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

def generate_group(model, tokenizer, prompt: str, group_size: int, max_new_tokens: int) -> list[str]:
    encoded = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **encoded,
        do_sample=True,
        temperature=0.8,
        top_p=0.95,
        max_new_tokens=max_new_tokens,
        num_return_sequences=group_size,
        pad_token_id=tokenizer.eos_token_id,
    )

    completions = []
    prompt_len = encoded["input_ids"].shape[1]
    for output in outputs:
        completion_ids = output[prompt_len:]
        completions.append(tokenizer.decode(completion_ids, skip_special_tokens=True))
    return completions

def completion_logprob(model, tokenizer, prompt: str, completion: str) -> torch.Tensor:
    full_text = prompt + completion
    full = tokenizer(full_text, return_tensors="pt").to(model.device)
    prompt_ids = tokenizer(prompt, return_tensors="pt").to(model.device)["input_ids"]
    prompt_len = prompt_ids.shape[1]

    input_ids = full["input_ids"]
    attention_mask = full["attention_mask"]

    logits = model(input_ids=input_ids, attention_mask=attention_mask).logits
    logprobs = torch.log_softmax(logits[:, :-1, :], dim=-1)
    target_ids = input_ids[:, 1:]

    token_logprobs = logprobs.gather(-1, target_ids.unsqueeze(-1)).squeeze(-1)

    completion_token_logprobs = token_logprobs[:, prompt_len - 1 :]
    return completion_token_logprobs.mean()

def main() -> None:
    model_name = "outputs/diagram-sft/final"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )
    model.train()

    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-6)

    group_size = 4
    max_new_tokens = 1024

    for step in range(500):
        user_prompt = random.choice(PROMPTS)
        prompt = format_prompt(tokenizer, user_prompt)
        completions = generate_group(model, tokenizer, prompt, group_size, max_new_tokens)
        rewards = torch.tensor([reward(user_prompt, c) for c in completions], device=model.device)

        if rewards.std() < 1e-6:
            print(f"step={step} skipped zero-variance rewards={rewards.tolist()}")
            continue

        advantages = (rewards - rewards.mean()) / (rewards.std() + 1e-6)

        losses = []
        for completion, advantage in zip(completions, advantages, strict=True):
            logp = completion_logprob(model, tokenizer, prompt, completion)
            losses.append(-advantage.detach() * logp)

        loss = torch.stack(losses).mean()
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        print(
            json.dumps(
                {
                    "step": step,
                    "loss": float(loss.detach().cpu()),
                    "reward_mean": float(rewards.mean().cpu()),
                    "reward_max": float(rewards.max().cpu()),
                    "rewards": [float(r) for r in rewards.cpu()],
                }
            )
        )

        if step and step % 100 == 0:
            model.save_pretrained(f"outputs/diagram-rl/step-{step}")
            tokenizer.save_pretrained(f"outputs/diagram-rl/step-{step}")

if __name__ == "__main__":
    main()
```

This trainer has many flaws. It computes log probabilities inefficiently. It does not use a frozen reference model. It does not use PPO or GRPO clipping. It does not separate generation from training. It does not handle distributed training. It uses a very simplified token objective.

But it shows the loop.

The model samples multiple diagrams for the same prompt. The environment scores them. The loss nudges the model toward the better diagrams.

That is the basic mechanism behind RL for LLM agents.

## Why RL Trainers Feel More Complicated Than SFT Trainers

SFT data is fixed. RL data is produced by the model during training.

That one difference explains a lot of the complexity.

In SFT, the dataset exists before optimization starts. You can shuffle it, batch it, and train on it. The model does not affect which examples appear next.

In RL, the policy determines the training data. As the model changes, the sampled completions change. As the completions change, the reward distribution changes. As the reward distribution changes, the gradient changes. Generation and optimization become coupled.

This is why RL trainers need guardrails.

A completion that gets a high reward might get reinforced too aggressively. A low-reward completion might be punished too strongly. The model can drift away from general language quality. It can exploit the reward. It can collapse into short, safe completions. It can overfit quirks of the verifier.

Modern RL trainers usually introduce some combination of a frozen reference model, KL penalties, ratio clipping, reward normalization, length masking, and completion masking.

The reference model is often the SFT checkpoint. The policy model is the one being updated. If the policy starts assigning much higher probability to a completion than the old model or reference model did, the update can be clipped or penalized.

A simplified PPO-style ratio looks like this:

ratio = exp(logprob\_policy - logprob\_old)

The clipped objective prevents the policy from moving too far in one step:

min(ratio \* advantage, clip(ratio, 1 - eps, 1 + eps) \* advantage)

An educational version would store the log probability from the model that generated the completion:

old\_logp = completion\_logprob(model, tokenizer, prompt, completion).detach()

Then, during optimization:

```python
new_logp = completion_logprob(model, tokenizer, prompt, completion)
ratio = torch.exp(new_logp - old_logp)
unclipped = ratio * advantage
clipped = torch.clamp(ratio, 0.8, 1.2) * advantage
loss = -torch.minimum(unclipped, clipped)
```

You can also add a reference-model KL term:

```python
policy_logp = completion_logprob(policy, tokenizer, prompt, completion)
ref_logp = completion_logprob(reference, tokenizer, prompt, completion).detach()
kl_estimate = policy_logp - ref_logp
loss = rl_loss + beta * kl_estimate
```

This is still simplified, but it explains why PPO and GRPO implementations look more complex than SFT implementations. They are not just fitting a static dataset. They are controlling the movement of a policy while the policy is also generating its own training data.

## The On-Policy View

The most useful way to think about this is through state distributions.

In SFT, the model trains on external trajectories. These trajectories may come from humans, a stronger teacher model, or a curated dataset. The current model did not produce them. The data distribution is fixed before training.

In RL, the model trains on its own trajectories. The completions come from the current policy. This creates a very different geometry.

The model is not being pulled toward an arbitrary external behavior distribution. It is sampling from its current behavior distribution, receiving reward, and locally reshaping probability mass toward the parts of that distribution that worked better.

This is one reason RL often feels less like imitation and more like capability refinement. SFT can teach a model to speak the action language, but it may also pull the model toward the teacher’s quirks. RL starts from the model’s own attempts and asks which of those attempts succeed in the environment.

For agent training, this matters a lot.

A model after SFT may produce valid JSON but still make poor diagrams. RL does not need to know the one correct answer. It only needs enough variation in the model’s own samples and a reward function that can distinguish better attempts from worse attempts.

This is also why RL can sometimes improve beyond the teacher traces. The teacher dataset may contain one valid diagram per prompt. The student’s rollouts may contain many variants. If the environment can score those variants, optimization can move toward completions the teacher never demonstrated.

## Mapping This to TRL

Once the loop is clear, TRL becomes much easier to understand.

GRPOTrainer accepts a model, a dataset of prompts, and one or more reward functions. It handles generation, reward computation, advantage estimation, and optimization.

The diagram task becomes:

```python
# train_grpo_trl.py
from datasets import Dataset
from trl import GRPOConfig, GRPOTrainer

from reward import reward

prompts = [
    "Draw a three step data pipeline: client, API, database.",
    "Draw a login flow with user, auth service, token, and dashboard.",
    "Draw a simple RAG system with documents, embeddings, vector DB, retriever, and LLM.",
    "Draw a CI pipeline with commit, tests, build, deploy.",
]

dataset = Dataset.from_list([{"prompt": prompt} for prompt in prompts])

def diagram_reward_func(prompts, completions, **kwargs):
    scores = []
    for prompt, completion in zip(prompts, completions, strict=True):
        text = completion if isinstance(completion, str) else completion[0]["content"]
        scores.append(reward(prompt, text))
    return scores

args = GRPOConfig(
    output_dir="outputs/diagram-grpo",
    learning_rate=1e-6,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    num_generations=4,
    max_prompt_length=1024,
    max_completion_length=1024,
    logging_steps=1,
)

trainer = GRPOTrainer(
    model="outputs/diagram-sft/final",
    reward_funcs=diagram_reward_func,
    args=args,
    train_dataset=dataset,
)

trainer.train()
```

This looks much shorter than the minimal trainer because the infrastructure is hidden. But conceptually it is the same loop:

prompt batch -> generate completions -> score completions -> compute advantages -> update policy

This is the right way to use frameworks. Not as magic boxes, but as implementations of mechanisms you already understand.

## What Makes an Environment Good?

The quality of an RL agent is often bottlenecked by the quality of the environment.

This is especially true for tool-using agents. The model can only optimize what the environment can measure. If your validator only checks JSON validity, your agent will learn to emit valid JSON. If your reward checks schema validity and task completion, it can learn task completion. If your reward includes a brittle LLM judge, the model may learn the judge’s preferences instead of the user’s.

A good environment has a few properties.

First, it gives partial credit. If every failure receives zero, learning becomes difficult. A malformed JSON output should score worse than a valid-but-incomplete diagram, and a valid-but-incomplete diagram should score worse than a complete, readable one.

Second, it separates syntax from semantics. Validity is necessary, but it is not the task. The reward should distinguish “the action sequence executed” from “the result satisfied the request.”

Third, it should be hard to exploit. If the model can maximize reward by creating huge text boxes containing every prompt word, it will eventually learn that. If it can get high reward with disconnected shapes, it will do that. If it can satisfy a judge with superficial labels, it will do that.

Fourth, it should produce useful logs. Every rollout should be inspectable: prompt, completion, parse errors, canvas state, reward components, final screenshot, and judge rationale if a judge is used. Without this, reward hacking becomes invisible.

This is why I increasingly think of agent training as environment design first and algorithm selection second.

The trainer decides how to use the signal. The environment decides what signal exists.

## Common Failure Modes

Many RL failures look mysterious until you view them as environment or state-distribution failures.

If the model never gets reward, the policy is probably not visiting valid states. This usually means the action schema is too strict, the base model cannot speak the action language, or SFT was skipped. The fix is not to stare at the RL algorithm. The fix is to make the valid region reachable: simplify the action space, generate teacher traces, add partial rewards, and train the model to produce valid actions.

If the model learns to emit tiny trivial diagrams, the reward probably overvalues validity and undervalues task satisfaction. The environment is saying “valid is enough,” and the model is listening. Add entity coverage, minimum shape counts, structure checks, and prompt-conditioned semantic scoring.

If the model emits valid JSON but ignores the prompt, the reward is mostly syntactic. The action language has been learned, but the task has not. Add checks that compare the prompt to the final canvas.

If the model overfits teacher style, the SFT data is too narrow or the RL phase is too weak. Add teacher diversity, sample multiple attempts per prompt, use multiple teacher models, or let the environment reward alternative valid solutions.

If the RL run is unstable, the update is probably too aggressive relative to reward quality and batch size. Lower the learning rate, shorten completions, add clipping, add a reference-model KL penalty, increase batch size, and inspect reward variance.

If reward goes up but human quality does not, the reward is being gamed. This is the most important failure mode. Inspect examples manually. Decompose the reward. Add negative tests. Penalize the exploit directly. Avoid relying on a single scalar from one brittle heuristic.

## What Changes for a Real tldraw Agent?

The toy Python canvas is educational. A real tldraw environment changes the validator, not the loop.

Instead of applying actions to a fake Canvas, you would execute them inside the real editor. Start the tldraw app or a validator page. Send JSON actions into the editor. Let tldraw sanitize and apply them. Read back the final shapes, bindings, selections, and errors. Export a screenshot. Compute reward from the shape state, the screenshot, and any validator errors.

The policy still receives an observation and emits an action. The environment still executes the action. The reward still scores the result. The trainer still updates the model.

This is why environment design is such a powerful abstraction. Once you can expose:

**reward(prompt, completion) -> float**

or, for richer settings:

**step(state, action) -> next\_state, reward, done, info**

you can plug the environment into a tiny educational trainer, TRL, Unsloth, PRIME-RL, verl, or a custom distributed training stack.

The framework changes. The shape of the problem does not.

## The Full Pipeline

The complete pipeline looks like this.

First, define the environment. This means the action schema, parser, validator, simulator or renderer, and reward function. This is the most important part because it defines what the model is actually optimizing.

Then generate prompts. Start with hand-written seed prompts, then expand with synthetic prompts. Make the prompts varied enough that the model cannot survive by memorizing a narrow pattern.

Then generate teacher trajectories. Use a stronger model to sample candidate actions. Validate them through the environment. Keep the traces that pass. Save rejected traces too, because they are useful for debugging the schema and reward.

Then SFT the student. The purpose of SFT is to move the model into the valid action space. Measure valid-action rate and average reward before doing RL.

Then run RL. Sample prompts, generate multiple completions per prompt, score them with the environment, compute group-relative advantages, and update the policy.

Then evaluate. Use held-out prompts. Track parse rate, schema-valid rate, environment reward, semantic score, reward distribution, and human review of rendered diagrams. For visual tasks, inspect screenshots. For tool tasks, inspect final states.

Then iterate. Improve the reward. Add harder prompts. Refresh teacher traces. Tune RL hyperparameters. Add negative tests. Repeat.

A useful compressed mental model is:

Teacher trajectories solve cold start. SFT teaches the action language. RL optimizes behavior inside the environment. Evaluation tells you whether the environment measures the right thing.

## Closing

The magic of agent training is not in the framework.

The framework matters, especially at scale. Distributed rollout generation, vLLM serving, batching, LoRA training, checkpointing, reference models, logging, and reproducibility are all real engineering problems. But they are not the conceptual center.

The conceptual center is smaller.

Define the action space. Define success. Generate traces. Imitate good traces. Sample new attempts. Reward good attempts. Update the model.

That is the shape of the system.

SFT and RL play different roles in this shape. SFT moves the model into the valid region of the action space. RL uses the environment to reshape the policy toward higher-reward behavior. Teacher trajectories solve the cold-start problem. Verifiers turn execution into supervision.

Once you see this, a tldraw agent is not a special case. A browser agent, coding agent, spreadsheet agent, robotics planner, and math solver all have the same skeleton:

state -> action -> validation -> reward -> learning

The rest is engineering.

## References

- Gemini text generation docs: [https://ai.google.dev/gemini-api/docs/text-generation](https://ai.google.dev/gemini-api/docs/text-generation)
- Gemini structured output docs: [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)
- TRL documentation: [https://huggingface.co/docs/trl/index](https://huggingface.co/docs/trl/index)
- TRL GRPOTrainer docs: [https://huggingface.co/docs/trl/grpo\_trainer](https://huggingface.co/docs/trl/grpo_trainer)
- Unsloth RL guide: [https://docs.unsloth.ai/get-started/reinforcement-learning-rl-guide](https://docs.unsloth.ai/get-started/reinforcement-learning-rl-guide)