---
type: entity
title: CrewAI
entity_type: product
created: 2026-05-02
updated: 2026-06-06
website: https://github.com/crewAIInc/crewAI
aliases: [crewAIInc/crewAI]
tags: [multi-agent, framework, open-source]
---

# CrewAI

> Multi-agent coordination framework that gives agents defined roles, responsibilities, and handoffs. Cross-cited in this wiki as a canonical implementation of the [[agent-workflow-patterns|orchestrator-workers pattern]] and as a "tech lead replacement" in the open-source AI engineering stack.

## Profile

CrewAI is an open-source framework for coordinating multiple AI agents with defined roles, responsibilities, and handoffs — essentially a runtime for the [[agent-workflow-patterns|orchestrator-workers pattern]] applied at the team-of-agents scale. The framework is referenced by both major tooling sources in this wiki: [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] positions it as a "tech lead replacement" claimed at Fortune-500 adoption; [[wiki/sources/hooeem-build-an-ai-agent-today]] names it among the canonical agent frameworks (alongside [[wiki/entities/langgraph|LangGraph]], [[wiki/entities/anthropic-agent-sdk|Anthropic Agent SDK]], [[wiki/entities/openai-agents-sdk|OpenAI Agents SDK]]).

## Key facts

- **Repo**: https://github.com/crewAIInc/crewAI
- **Role**: multi-agent role coordination — agents with named roles, responsibilities, and handoff protocols.
- **Position in the wiki**: implementation of [[subagents]] + [[multi-agent-orchestration]] + [[agent-workflow-patterns|orchestrator-workers]].
- **Adoption claim** (per heynavtoor, unverified): used across Fortune 500.
- **Architecture**: role-based — `Agent` (role / goal / backstory / tools), `Task`, and `Crew` (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Flows layer**: adds a "deterministic backbone with intelligence where it matters" for routing and validation (per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).
- **Stack position**: named among agent orchestration frameworks at Layer 10 (per [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).

## Positions and claims

- **Multi-agent coordination is a real pattern, not just a buzzword.** *(Implicit by the framework's existence and adoption.)*

## Mentioned in

- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — "tech lead replacement"; named as a multi-agent framework.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — named as a canonical framework alongside LangGraph and the Anthropic/OpenAI SDKs.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — role-based multi-agent harness architecture (Agent / Task / Crew + Flows).
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] — orchestration framework (Layer 10).

## Related entities

- [[wiki/entities/langgraph]] — sibling framework, often co-cited.
- [[wiki/entities/anthropic-agent-sdk]] — sibling framework.
- [[wiki/entities/openai-agents-sdk]] — sibling framework.

## Related concepts

- [[agentic-loop]] — substrate.
- [[agent-workflow-patterns]] — CrewAI is an implementation.
- [[subagents]] — CrewAI formalizes role-specialized subagents.
- [[multi-agent-orchestration]] — runtime layer.
