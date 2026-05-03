---
type: concept
title: Agent Workflow Patterns
created: 2026-05-02
updated: 2026-05-02
aliases: [5 workflow patterns, anthropic agent patterns]
tags: [agents, patterns, foundational]
---

# Agent Workflow Patterns

> Five named patterns documented by Anthropic for composing LLM calls into useful workflows: prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer. Each is a constrained shape of the [[agentic-loop]] that is easier to reason about and cheaper to run than a fully-autonomous agent.

## Definition

An **agent workflow pattern** is a structured arrangement of LLM calls (sometimes with tool calls in between) that constrains the [[agentic-loop]] to a recognizable shape. The shape buys you reliability, lower cost, and easier debugging — at the price of less dynamic flexibility than a fully-autonomous agent. Anthropic's "Building effective agents" guidance documents five canonical patterns that cover the majority of real use cases.

The five patterns:

1. **Prompt chaining** — Sequential steps; each LLM call processes the output of the previous one. Programmatic gates between steps verify quality before continuing.
2. **Routing** — Classify incoming input, then dispatch to a specialized handler. Each handler gets its own optimized prompt.
3. **Parallelization** — Run multiple LLM calls simultaneously. Two sub-flavors: **sectioning** (split task into independent subtasks) and **voting** (run the same task multiple times and aggregate for confidence).
4. **Orchestrator-workers** — A central LLM (the orchestrator) dynamically breaks down a task and delegates subtasks to worker LLMs at runtime. Unlike parallelization, the subtasks are **not predefined**.
5. **Evaluator-optimizer** — One LLM generates output; another evaluates and provides feedback. Failed evaluations loop back. Repeat until criteria met.

## Why it matters

Most agent problems can be solved by choosing the right pattern instead of jumping to a fully-autonomous agent. *"Workflows are deterministic; your code controls execution and the same input always produces the same path. They are ideal for well-defined tasks with fixed steps and are cheaper (fewer LLM calls). Agents are dynamic; the LLM decides the next step."* ([[wiki/sources/hooeem-build-an-ai-agent-today]])

Patterns also give you a vocabulary for describing existing agent setups. The 5-role [[subagents]] architecture in [[wiki/sources/regent0x-claude-code-247-dev-team]] is essentially **orchestrator-workers** (parent agent dispatches to architect/coder/reviewer/tester/ops) composed with **evaluator-optimizer** (the reviewer evaluates and feeds back). Naming the patterns makes the design legible.

## Treatment across sources

- [[wiki/sources/hooeem-build-an-ai-agent-today]] — canonical wiki source. Names all five patterns, describes when each applies, and gives concrete use cases. Argues *"most problems can actually be solved without needing full autonomy."*
- [[wiki/sources/saraev-agentic-workflows-2026]] — independently arrives at the workflow-vs-agent tradeoff via the [[reliability-decay-math]] argument: chained probabilistic steps decay multiplicatively, so deterministic workflow patterns are economically necessary for client-grade reliability. Saraev's [[do-framework]] is a specific implementation of orchestrator-workers where the workers (executions) are deterministic Python rather than additional LLM calls.

## Sub-claims and details

### Pattern 1: Prompt chaining
- **Shape**: A → check → B → check → C
- **Use when**: Task decomposes cleanly into fixed subtasks. Trade speed for accuracy by making each LLM call simpler.
- **Examples**: Generate marketing copy then translate it. Write an outline, verify coverage, then write the full document.

### Pattern 2: Routing
- **Shape**: classifier → (handler_1 | handler_2 | handler_3 | ...)
- **Use when**: Different categories of input need fundamentally different treatment.
- **Examples**: Customer service triage (billing / technical / sales).

### Pattern 3: Parallelization
- **Shape (sectioning)**: split → (worker_1, worker_2, worker_3) → merge
- **Shape (voting)**: dispatch_same_task → (worker, worker, worker) → aggregate
- **Use when**: Subtasks are independent (sectioning) or you need consensus on a critical decision (voting).
- **Note**: The [[claude-code-slash-commands|/lint]] script in this wiki uses a simple parallelization-by-section pattern internally — broken-link checks, frontmatter checks, and orphan checks are independent and could run in parallel.

### Pattern 4: Orchestrator-workers
- **Shape**: orchestrator → (decides at runtime: worker_a, worker_b, ...) → orchestrator integrates
- **Use when**: Complex tasks where you cannot predict structure in advance.
- **Examples**: Code generation across files, research, report writing.
- **Cross-cut**: This is the pattern [[subagents]] formalize. Tools like [[wiki/entities/crewai]] are dedicated implementations.

### Pattern 5: Evaluator-optimizer
- **Shape**: generator → evaluator → (feedback → generator → evaluator → ...) → final
- **Use when**: Clear evaluation criteria exist; iterative refinement adds measurable value.
- **Examples**: Translation, code generation, writing.
- **Cross-cut**: [[wiki/entities/tdd-guard]] is a runtime evaluator-optimizer for code (write code → test → fail → revise).

## Open questions and contradictions

- **Pattern composition semantics**: how do patterns nest cleanly? An orchestrator-workers system whose orchestrator uses prompt chaining internally is a real shape but isn't given a name. As shapes get composed, the vocabulary gets thinner.
- **When to graduate from pattern to agent**: the sources say "start with the simplest pattern that works." A heuristic for when fixed patterns become too constraining would help.
- **Cost models per pattern**: prompt chaining is N LLM calls, parallelization is N calls in parallel, orchestrator-workers is N+1 (the orchestrator plus the workers), evaluator-optimizer is 2N+ (each iteration is generator + evaluator). The wiki should track this when cost becomes load-bearing.

## Related concepts

- [[agentic-loop]] — patterns are constrained shapes of this.
- [[augmented-llm]] — the unit that fills each role in a pattern.
- [[subagents]] — orchestrator-workers at the role-specialization scale.
- [[multi-agent-orchestration]] — running pattern instances in parallel.
- [[beginner-agent-types]] — five common agent types, often best implemented as one of these patterns.

## Related entities

- [[wiki/entities/crewai]] — explicit implementation of orchestrator-workers.
- [[wiki/entities/langgraph]] — graph orchestration that supports all five patterns.
- [[wiki/entities/anthropic]] — origin of the documented patterns.
- [[wiki/entities/anthropic-agent-sdk]]
- [[wiki/entities/openai-agents-sdk]]

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]
- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — multi-agent frameworks (CrewAI, LangGraph) implement these patterns.
