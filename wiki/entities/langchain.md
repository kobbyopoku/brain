---
type: entity
title: LangChain
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [LangChain]
tags: [llm-framework, agents, orchestration]
---

# LangChain

> Framework for building LLM-powered applications — connecting models to prompts, tools, vector databases, and retrieval workflows; also a reference case for how much an agent harness (vs. the model) drives performance.

## Profile

LangChain is a framework for wiring LLMs into larger systems. In this wiki it appears as a stage-IV framework on an AI-engineer roadmap and, more substantively, as a case study in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] for the leverage that the non-model "harness" infrastructure has over agent benchmark performance.

## Key facts

- Connects LLMs to prompts, tools, vector databases, and retrieval workflows; gives structure for building applications that use AI as part of a larger system instead of manually wiring each model call — [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]].
- Changing only the infrastructure wrapping its LLM (same model/weights) moved LangChain from outside the top 30 to rank 5 on TerminalBench 2.0 — [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]].
- Its `AgentExecutor` was deprecated in v0.2 for being hard to extend and lacking multi-agent support — [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]].
- Its **Deep Agents** product explicitly uses the term "agent harness" — [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]].
- Listed among the frameworks/libraries [[wiki/entities/context7|Context7]] keeps fresh docs for — [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]].

## Positions and claims

- **The harness, not just the model, drives agent performance** — demonstrated via the harness-only TerminalBench jump documented in [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]].

## Mentioned in

- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — named docs target for Context7.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — stage-IV framework #1.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — demonstrated the harness's leverage via a harness-only TerminalBench jump.

## Related entities

- [[wiki/entities/openai]] — model provider commonly wired through LangChain.

## Related concepts

*(none yet.)*
