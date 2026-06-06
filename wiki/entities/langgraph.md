---
type: entity
title: LangGraph
entity_type: product
created: 2026-05-02
updated: 2026-06-06
website: https://github.com/langchain-ai/langgraph
aliases: [langchain-ai/langgraph]
tags: [agent-framework, orchestration, open-source]
---

# LangGraph

> Stateful, durable, observable orchestration framework for production AI systems. Cross-cited as the orchestration layer "every production AI system is being built on in 2026" and as one of the canonical agent frameworks alongside [[wiki/entities/crewai|CrewAI]] and the [[wiki/entities/anthropic-agent-sdk|Anthropic]] / [[wiki/entities/openai-agents-sdk|OpenAI]] SDKs.

## Profile

LangGraph is an orchestration framework from LangChain — a graph-based runtime for composing stateful, durable, observable AI workflows. It supports all five [[agent-workflow-patterns|workflow patterns]] (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) and is positioned in this wiki's tooling sources as the "architect replacement" of the open-source AI engineering stack.

## Key facts

- **Repo**: https://github.com/langchain-ai/langgraph
- **Maintainer**: LangChain (langchain-ai).
- **Role per heynavtoor**: architect replacement; orchestration layer for production AI systems.
- **Properties** (per heynavtoor): stateful, durable, observable.
- **Claimed stars** (per heynavtoor): 11.4k+ — *(unverified; same number cited for [[wiki/entities/claude-flow]], so cross-check against repo data.)*
- **Positioning vs LangChain**: described as more advanced than LangChain; lets you define steps, track state, branch on conditions, and control agent movement through a workflow (per [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]).
- **Lineage**: evolved from LangChain's deprecated `AgentExecutor` (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Positions and claims

- **Production AI systems need a graph-shaped orchestration layer**, not just a prompt + tool call. *(Implicit by the framework's positioning.)*
- **The agent harness is an explicit state graph** — `akshay_pachaar` models the harness as `llm_call` and `tool_node` nodes joined by a conditional edge, with typed-dictionary state flowing through nodes and reducers merging updates (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Checkpointing enables resume and time-travel debugging** — LangGraph checkpoints at super-step boundaries (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Four error types** — distinguishes transient, LLM-recoverable, user-fixable, and unexpected errors (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Mentioned in

- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — "architect replacement"; orchestration layer.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — named as a canonical framework wrapping the [[agentic-loop]].
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — Stage IV framework #2; advanced workflow control beyond LangChain.
- [[wiki/sources/exploraX_-5-solo-ai-business-models]] — named in layer 3 (intelligent systems) for building multi-step workflows.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — models the agent harness as an explicit state graph.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — orchestration framework (Layer 10) where multi-agent state, handoffs, parallelism, and failure recovery get encoded.

## Related entities

- [[wiki/entities/crewai]] — sibling framework, multi-agent-coordination focused.
- [[wiki/entities/anthropic-agent-sdk]] — sibling SDK.
- [[wiki/entities/openai-agents-sdk]] — sibling SDK.
- [[wiki/entities/claude-flow]] — adjacent enterprise orchestration framework.

## Related concepts

- [[agentic-loop]] — substrate.
- [[agent-workflow-patterns]] — supports all five.
- [[multi-agent-orchestration]]
