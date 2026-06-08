---
type: concept
title: Multi-agent delegation with Verifier
created: 2026-06-08
updated: 2026-06-08
aliases: [persona-family-with-verifier, delegating-loop-with-second-pass, verifier-gated-side-effects]
tags: [agent-architecture, llm-pattern, safety, multi-agent, ai-pattern]
---

# Multi-agent delegation with Verifier

> An agent architecture where a primary persona synchronously delegates to specialized personas for narrow tasks, AND an independent Verifier persona gates any destructive side-effect before it ships — separating *who decides what to do* from *who confirms it's safe to do*.

## Definition

The pattern composes two distinct mechanisms:

1. **Delegation by persona, not by tool.** Instead of a single LLM with N tools, the architecture defines several personas (each with its own system prompt, role, and capability scope) and one primary persona that can synchronously call into the others as if they were tools. A user-facing persona (Compass in Kivora) handles conversation and planning; specialized personas (Pulse for monitoring, Autopilot for batch operations, Scribe for NLG) take focused subtasks. Each persona's context is bounded to what it needs.
2. **A Verifier persona gates destructive side-effects independently of the executing persona.** Before any tool call with real-world consequences (mutating cloud resources, sending external messages, deleting data), the system invokes a separate Verifier persona with a narrowly-scoped prompt (typically "given the proposed action, refuse if it would cause unintended harm"). The Verifier's refusal-bias is a second AI opinion that the executing persona cannot itself produce, because the executing persona's context is biased toward completing the task.

The combination matters because each mechanism alone is incomplete: delegation without a Verifier means each specialized persona can still ship side-effects unchecked; a Verifier without delegation means the same model is reasoning AND verifying its own decision, which is well-documented to fail (sycophancy, motivated reasoning, blind-spots inherited from the planning context).

## Why it matters

LLM agents fail in two predictable ways:

- **Context overload.** Stuffing N capabilities into one system prompt makes the planning persona worse at each individual capability and dramatically increases the chance of inappropriate tool selection.
- **Self-confirmation bias.** A persona that has just decided "I should run command X" is uniquely bad at evaluating "is X safe to run?" — the decision's biased context contaminates the verification.

Delegation addresses the first; a Verifier addresses the second. Independently, each is well-known (delegation appears in most multi-agent frameworks; verification appears as "self-critique" loops). Together, they create a configuration where each persona's role is narrowly defined AND every destructive action requires confirmation from an independent context.

The pattern matters most in **enterprise AI agents** where the side-effects are real (cloud resources, customer data, financial transactions) and the audit story has to be defensible. "We delegated to a specialized persona AND ran the action past an independent Verifier with its own refusal-trained context" is a meaningfully stronger answer than "we asked the LLM to be careful."

## When to use it

- The agent has destructive capabilities (mutating cloud resources, sending external comms, modifying state customers see).
- Different subtasks within a session have meaningfully different contexts (planning vs monitoring vs execution).
- Single-loop tool use is producing context-overload failures (wrong tool selected, irrelevant context dragged into a subtask).
- The audit / compliance posture for "what verified this action" matters.

## When *not* to use it

- The agent is purely read-only. Verifier has nothing to gate; delegation overhead may not be worth it for single-context tasks.
- Single-turn agents (one prompt → one response). The pattern's value is in multi-turn workflows where personas accumulate context differently.
- Latency-sensitive paths where the extra Verifier round-trip is too expensive. Reserve the Verifier for the destructive subset, not every tool call.
- Resource-constrained deployments (the Verifier is another model invocation; cost adds up).

## Anatomy

```
        ┌────────────────────────────────────────────────┐
        │  PRIMARY (e.g., Compass): user-facing chat,    │
        │  plans, calls tools or delegates.              │
        └────────────────────────────────────────────────┘
              │              │              │
   reads      │   delegates  │   delegates  │   wants to execute
   tools      ▼              ▼              ▼   destructive tool
        ┌──────────┐   ┌──────────┐   ┌──────────┐         │
        │ Pulse:   │   │ Autopilot│   │ Scribe:  │         │
        │ monitor  │   │ batch ops│   │ NLG/docs │         │
        └──────────┘   └──────────┘   └──────────┘         │
                                                            ▼
                                              ┌────────────────────────┐
                                              │  VERIFIER (separate    │
                                              │  context, refusal-     │
                                              │  biased prompt):       │
                                              │  "Refuse if the action │
                                              │  would cause harm."    │
                                              └────────────────────────┘
                                                          │
                                                 ┌────────┴────────┐
                                            APPROVED            REFUSED
                                                 │                 │
                                                 ▼                 ▼
                                         ┌──────────────┐  ┌──────────────┐
                                         │ Execute      │  │ Block, log,  │
                                         │ side-effect  │  │ surface to   │
                                         │              │  │ user         │
                                         └──────────────┘  └──────────────┘
```

Key implementation details:

- **Each persona is its own file** with its own system prompt + tool/scope declaration. Kivora's `souls/` package convention: one Python module per persona (`souls/compass.py`, `souls/pulse.py`, `souls/autopilot.py`, `souls/scribe.py`, `souls/verifier.py`).
- **Delegation is a tool call from the primary's perspective.** Compass sees `delegate_to_pulse` and `delegate_to_autopilot` as tools; the dispatch layer maps them to a fresh persona invocation with its own bounded context.
- **The Verifier sees ONLY the proposed action**, not the full conversation history. This bounds its context to what's needed for safety judgment and isolates it from the planning bias of the executing persona.
- **The Verifier's prompt is explicitly refusal-biased.** Wording matters: "default to refuse if uncertain" outperforms "evaluate whether to allow." The asymmetry of consequences (false positive = user friction; false negative = real-world damage) justifies the asymmetric default.

## Sub-claims and details

- **Persona ≠ subagent in the orchestration sense.** A persona shares the model + infrastructure with the primary; it's a different *prompt + tool scope + context boundary*, not a different process or model. Cheap to spawn (one model invocation), cheap to add a new one (one file).
- **Synchronous delegation, not async.** The primary calls a persona and waits; the persona returns; the primary integrates. This keeps the agent loop deterministic from the user's perspective. Async delegation is a different pattern (more like job dispatch) and harder to reason about.
- **The Verifier is the ONLY persona with strict refusal training in its prompt.** Other personas may refuse for capability reasons (Pulse can't write SQL because it has no write tools) but only Verifier is trained to refuse based on judgment about consequences.
- **The Verifier gate runs AFTER the executing persona has committed to the action.** Pre-decision verification doesn't work — the executing persona's reasoning is still in flux. Post-decision but pre-execution is the right moment.
- **Per-tool minimum-role declarations layer ON TOP of the Verifier**, not in place of it. RBAC ensures the executing persona can't propose a tool call the user lacks permission for; the Verifier ensures the proposed call is sensible regardless of permission. Both gates fire on every destructive action.
- **Personas share the same audit ledger.** Whatever Compass does, Pulse does, Autopilot does, Verifier does — all events go into the same signed audit log. The audit trail's value comes from being complete; if Verifier refuses something, the refusal is logged.

## Treatment across sources

- The classic "multi-agent" framing in **AutoGPT / BabyAGI / CrewAI** is task-decomposition: a planner delegates discrete subtasks to worker agents. That pattern lacks the Verifier gate — workers can ship side-effects directly. The Kivora pattern is closer to the *system prompt segmentation* idea in Anthropic's tool-use docs, extended with an explicit safety persona.
- **OpenAI's Swarm framework** lets multiple agents take turns owning the conversation but doesn't separate execution from verification — any agent can call any tool.
- **The "LLM as judge" pattern** (used in eval suites) is structurally similar to the Verifier role but isolated to evaluation, not execution gating. Verifier-gated execution applies the judge pattern in production, on every destructive call.
- The **agentic-loop literature** (see [[wiki/concepts/agentic-loop]]) typically frames a single persona as the orchestrator. Delegation-with-Verifier is a specialization where the loop has structural roles, not just a single tool-calling LLM.

## Open questions and contradictions

- **Verifier alignment failure modes.** If the Verifier is trained on the same corpus / family as the executing persona, they may share blind spots. Diversification across model families (e.g., Claude as executor, GPT-4 as Verifier) might surface different refusals. No public study yet; Kivora uses the same family for both.
- **Latency vs safety tradeoff.** Every destructive call pays the Verifier round-trip cost. For low-risk destructive calls (e.g., creating a ticket in Jira), is the gate worth it? Threshold-based gating (e.g., gate only Tier-1 destructive operations) is one answer; some implementations skip the gate for "reversible" mutations and require it for irreversibles.
- **The Verifier as an attack surface.** A user could in principle craft a request that elicits a Verifier-friendly framing from the executing persona, bypassing the gate. Prompt-injection defenses for the Verifier are a separate research area.
- **Multiple Verifiers.** Some implementations run N parallel Verifiers and require K-of-N to approve. This costs N× the Verifier latency but reduces the false-negative rate. Optimal K and N are tunable per blast-radius tier.

## Related concepts

- [[wiki/concepts/reasoning-execution-split]] — the parent pattern; multi-agent-delegation-with-verifier extends it from "code executes, LLM reasons" to "different LLMs play different roles, and an independent LLM verifies."
- [[wiki/concepts/agentic-loop]] — the single-loop alternative; this pattern composes multiple loops with structural roles.
- [[wiki/concepts/agent-workflow-patterns]] — workflow patterns vs autonomous loops; delegation-with-Verifier is a workflow with a safety stage embedded.
- [[wiki/concepts/augmented-llm]] — adjacent; both add structure around an LLM. Augmented-llm focuses on tool use; this pattern focuses on persona separation.
- [[wiki/concepts/markdown-as-agent-contract]] — the per-persona system prompts are a concrete instance of "markdown as contract."

## Worked example

- [[wiki/projects/kivora|Kivora]] — 2026-06-04 `souls/` package refactor split a single `soul.py` into Compass / Scribe / Pulse / Autopilot. Compass synchronously delegates to Pulse for posture queries and Autopilot for batch operations (Phase 3 Level 1). Verifier persona (`souls/verifier.py`, shipped via `c55c1dd`) gates every destructive Composio action — `execute_remediation`, `composio_execute` — independently of the executing persona. The Verifier is invoked with a narrow context (just the proposed action), not the full conversation, and is prompted to default to refusal under uncertainty. Audit ledger captures Verifier verdicts alongside agent actions.
