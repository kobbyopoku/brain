---
type: concept
title: Agentic Loop
created: 2026-05-02
updated: 2026-05-02
aliases: [agent loop, core agent loop]
tags: [agents, foundational, agent-architecture]
---

# Agentic Loop

> The core runtime pattern shared by every AI agent: user input → LLM thinks → LLM decides (respond or call a tool) → if tool, execute and feed the result back → repeat. Frameworks wrap this loop with abstractions; they don't change its essence.

## Definition

The **agentic loop** is the minimal runtime structure of an AI agent. A user submits input; the LLM reasons about it; the LLM decides to either emit a final response or call a tool; if the LLM called a tool, the tool runs and its result is fed back into the LLM's context; the loop repeats until the LLM produces a final response. Every agent framework (LangGraph, CrewAI, Anthropic Agent SDK, OpenAI Agents SDK) is fundamentally a wrapper around this loop with extra abstractions for state, tool registration, parallelism, and observability.

## Why it matters

Once you see the loop, every framework becomes transparent rather than magical. You debug agents faster (because you know there are only a few places things can go wrong: the prompt, the tool description, the result-handling, the termination condition). You choose tools more wisely (because you understand that every tool addition expands the LLM's decision surface inside the loop). And you stop being intimidated by framework choice — frameworks are decoration; the loop is the work.

The loop is also why agents are simultaneously "conceptually simple" and "operationally demanding" — the loop is fifty lines of Python; the operational work is in the tool descriptions, the rules for when to call which tool, the failure handling, the evaluation. The loop doesn't tell you anything about that.

## Treatment across sources

- [[wiki/sources/hooeem-build-an-ai-agent-today]] — canonical articulation in this wiki. Frames the loop as: *"User input → LLM thinks → LLM decides (respond or call a tool) → if tool: execute it, feed result back → repeat."* Names the pieces *"brain / hands / notepad"* (LLM / tools / memory). Asserts the loop is invariant across LangGraph, CrewAI, Anthropic SDK, and OpenAI Agents SDK.

## Sub-claims and details

- **Termination conditions**: the loop ends when the LLM emits a response that's not a tool call, or when a configured maximum iteration count is hit.
- **Tool calls are the LLM's "decision"**: at each loop iteration, the LLM produces structured output indicating either content or a tool call (with arguments). Anthropic exposes this via `input_schema`; OpenAI via the function-object schema.
- **Memory-as-loop-state**: the conversation history accumulating in the loop is the agent's short-term memory. Long-term memory is anything outside the loop the agent can read from (files, vector DBs, [[mcp-server|MCP-mediated]] sources).
- **Loop ≠ agent**: the loop is the *substrate*. An [[augmented-llm]] running inside the loop with tools and memory is an agent. Without tools, it's a chatbot.
- **Frameworks compose loops**: in [[agent-workflow-patterns|orchestrator-workers]], the orchestrator runs a loop in which each "tool call" might itself be a sub-agent running its own loop. Loops nest.
- **Failure modes inside the loop** (per [[wiki/sources/hooeem-build-an-ai-agent-today]]): the loop can spin forever if the LLM keeps calling tools without progressing; the tool description can be ambiguous so the LLM picks the wrong tool; the tool can return a result the LLM misinterprets. Each failure has a specific mitigation (max-iterations, clearer descriptions, structured tool errors).

## Open questions and contradictions

- **Streaming vs. discrete iterations**: the canonical loop is discrete. In practice some implementations interleave streaming output with tool-call decisions. The semantics of streaming-mid-loop are not standardized.
- **Loop observability**: each loop iteration is a debuggable decision point, but standard tooling for tracing loops across frameworks is still emerging.

## Related concepts

- [[augmented-llm]] — the *capability profile* that runs inside the loop (LLM + tools + retrieval + memory).
- [[agent-workflow-patterns]] — five patterns that compose or constrain the loop.
- [[subagents]] — multiple loops, one per role.
- [[multi-agent-orchestration]] — running multiple loops in parallel.
- [[mcp-server]] — most non-trivial loops include MCP-mediated tool calls.

## Related entities

- [[wiki/entities/anthropic-agent-sdk]] — wraps the loop with Anthropic's tool conventions.
- [[wiki/entities/openai-agents-sdk]] — wraps the loop with OpenAI's tool conventions.
- [[wiki/entities/langgraph]] — orchestration over loops.
- [[wiki/entities/crewai]] — multi-agent loops with role coordination.

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]
