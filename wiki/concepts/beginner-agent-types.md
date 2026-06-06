---
type: concept
title: Beginner Agent Types
created: 2026-05-02
updated: 2026-06-06
aliases: [5 agent types, common agent types]
tags: [agents, taxonomy, beginner]
---

# Beginner Agent Types

> Five common agent shapes worth choosing from when starting out, instead of trying to build an "all-purpose super agent": research, content, workflow, personal-knowledge, operator. Each maps to a typical task profile and a minimal augmentation set.

## Definition

The five **beginner agent types** are a taxonomy of common starting points. Picking one (instead of "I want an agent that does everything") narrows the design surface enough to make the agent buildable in a day:

1. **Research agent** — gather information, summarize. Tools: web search; optionally file search. Output format: clear summary + key findings + risks + verdict.
2. **Content agent** — write, rewrite, summarize, transform content. Tools: usually just a strong system prompt; optionally file access; examples of preferred style.
3. **Workflow agent** — follow a repeatable business process. Tools: classification rules; optionally custom API calls.
4. **Personal knowledge agent** — answer questions using your documents. Tools: file search or RAG. Critical rule: stay grounded in provided material.
5. **Operator agent** — take actions in an environment (read/edit files, run shell, save reports, browse). Tools: many; permissions: explicit; safety boundaries: strong.

## Why it matters

The taxonomy short-circuits the most common beginner mistake: building "an AI assistant" with web search + file access + database + memory + multi-agent handoffs + 20 tools, and shipping nothing. By naming the five common shapes, the source ([[wiki/sources/hooeem-build-an-ai-agent-today]]) gives newcomers a place to start that is *narrow enough to actually finish* and *general enough to cover most real needs*.

The types also map directly to [[agent-workflow-patterns]] — most workflow agents are routing-pattern; most research agents are prompt-chaining; most operator agents are orchestrator-workers. Choosing a type implies a pattern.

## Treatment across sources

- [[wiki/sources/hooeem-build-an-ai-agent-today]] — canonical wiki source. Lists the five types with examples ("Research the best rehab exercises for ankle sprain", "Turn my notes into a newsletter", "Classify support tickets", "Answer using my PDFs only", "Run shell commands and help me debug code") and the minimal augmentation set each needs.
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]] frames it as a worked example: its four named agents (Blueprint, Strategy Extractor, outlier analyzer, Auto-Post) map onto the research / content / workflow agent types.

## Sub-claims and details

- **The Agent formula** (per [[wiki/sources/hooeem-build-an-ai-agent-today]]): `Agent = Role + Goal + Tools + Rules + Output format`. Each of the five types fills the formula differently.
- **Operator agents are the most dangerous** of the five — they take action in the world. Strong rules and explicit permission scopes are non-negotiable.
- **Personal knowledge agents** are the wiki-relevant type — this entire vault is essentially a personal knowledge base optimized for human + LLM joint use; an agent that answers from it would be a personal knowledge agent specifically designed against the [[llm-wiki-pattern]].
- **Workflow agents** map most naturally to [[claude-code-slash-commands]]: each repeatable business process can be a slash command + a small skill file.
- **Content agents** are where [[personal-claude-prompts]] shine — many of [[wiki/sources/AnatoliKopadze-20-claude-prompts|Anatoli's 20 prompts]] are content-agent prompts.
- **Research agents** can be the most expensive — they often need [[mcp-server|MCP-mediated]] web search plus retrieval plus generation.
- **A four-agent content pipeline as a concrete instance** ([[wiki/sources/8xgrowth-100-days-to-10k-clipping]]): a Blueprint agent, a Strategy Extractor, an outlier analyzer, and an Auto-Post agent — distributing the work across research, content, and workflow types rather than building one all-purpose agent.

## Open questions and contradictions

- **Hybrids**: in practice many real agents straddle types (e.g. operator + research). The five types are starting shapes, not exhaustive categories.
- **The boundary between "personal knowledge" and "research"** is fuzzy: when do you stop searching your documents and start searching the web? This is mostly a permission and tool-availability question.
- **Multi-agent setups** (per [[wiki/sources/hooeem-build-an-ai-agent-today]]) usually don't fit the taxonomy — they're a composition of the types. See [[subagents]].

## Related concepts

- [[agent-workflow-patterns]] — choosing a type often implies a pattern.
- [[agentic-loop]] — substrate.
- [[augmented-llm]] — each type uses a different augmentation set.
- [[claude-code-skills]] — workflow agents naturally compile into skills.
- [[claude-code-slash-commands]] — workflow agents naturally surface as slash commands.
- [[llm-wiki-pattern]] — defines the substrate for a personal knowledge agent.

## Related entities

- [[wiki/entities/claude-code]] — the platform on which these are most easily built.
- [[wiki/entities/anthropic-agent-sdk]]
- [[wiki/entities/openai-agents-sdk]]

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]
- [[wiki/sources/8xgrowth-100-days-to-10k-clipping]]
