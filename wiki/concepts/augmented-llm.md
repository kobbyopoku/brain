---
type: concept
title: Augmented LLM
created: 2026-05-02
updated: 2026-05-02
aliases: [augmented language model]
tags: [agents, foundational, agent-architecture]
---

# Augmented LLM

> A language model extended with three capabilities — tools (callable functions), retrieval (the ability to fetch external information), and memory (the ability to retain information across interactions). The minimum capability profile that turns a plain LLM into something that can run inside the [[agentic-loop]].

## Definition

A plain LLM accepts text and emits text — nothing more. An **augmented LLM** adds three capabilities:

- **Tools** — functions the model can call (calculators, databases, APIs, file operations). [[wiki/entities/anthropic]] exposes tools via JSON schemas using `input_schema`; [[wiki/entities/openai-agents-sdk|OpenAI]] wraps functions in a function object with parameters. [[mcp-server|MCP servers]] are the standard way to expose tools at scale.
- **Retrieval** — the ability to pull relevant information from external sources (search engines, documents, vector databases) into the model's context.
- **Memory** — the ability to retain information across interactions via message history or other persistent storage.

The augmented LLM is what runs inside the [[agentic-loop]]. Without these augmentations, the LLM cannot act on the world; it can only describe.

## Why it matters

The augmented-LLM framing is what makes agent architecture **modular**. Each of the three capabilities can be developed, tested, swapped, and composed independently:

- A tool is "added" to the agent — the same tool works for any LLM that supports tool-calling.
- Retrieval can be local-file (RAG with file search), vector-DB-backed, or [[mcp-server|MCP-mediated]] — the LLM doesn't care which.
- Memory can be conversation history (default), session compression ([[wiki/entities/claude-mem]]), background-built ([[wiki/entities/claude-subconscious]]), or wiki-based ([[llm-wiki-pattern]]).

The framing is also a check on premature complexity. *"Most agents don't need complex memory"* is a recurring theme in [[wiki/sources/hooeem-build-an-ai-agent-today]]; the augmented-LLM framing makes it easy to ask "which of these three capabilities does my agent actually need?" rather than installing the entire stack.

## Treatment across sources

- [[wiki/sources/hooeem-build-an-ai-agent-today]] — canonical articulation. Names tools, retrieval, and memory as the three augmentations and gives concrete tool-schema examples for both Anthropic and OpenAI. Asserts that *"workflows vs. true agents"* hinges on the augmented LLM: a deterministic workflow uses augmentation in code-controlled ways; an agent lets the LLM decide when to invoke each augmentation.

## Sub-claims and details

- **Tool design beats tool count.** *"Better tools = smarter agent. Fewer tools = more reliable agent."* (See [[wiki/sources/hooeem-build-an-ai-agent-today]] § 4.) One clear-purpose tool with a precise description outperforms many overlapping tools.
- **Retrieval-as-tool is common**: many agent setups expose retrieval as a callable tool ("search documents", "search web") rather than as a separate primitive. Functionally this collapses to "tool + retrieval" being the same primitive.
- **Memory's three layers** (per current sources):
  - **Short-term** — conversation history. Default in every SDK.
  - **Compressed long-term** — session-summarized state ([[wiki/entities/claude-mem]]).
  - **External knowledge** — files, RAG, [[wiki/entities/obsidian|Obsidian]] vaults, [[llm-wiki-pattern|LLM Wikis]].
- **Composition with [[claude-code-skills]]**: a Claude Code skill is itself a packaged augmentation — it bundles instructions and (often) tool calls into a re-usable unit.

## Open questions and contradictions

- **When does retrieval become memory?** A vector DB backing a session is augmentation #2 (retrieval); a vector DB backing the agent's long-term knowledge is augmentation #3 (memory). The line is operational, not architectural.
- **Tool-call cost vs. accuracy**: every tool call adds an LLM round-trip. The augmented-LLM framing doesn't tell you when to inline vs. tool-call. Heuristic from [[wiki/sources/hooeem-build-an-ai-agent-today]]: "if it requires external data or action, use a tool."
- **Augmentation portability**: a tool defined for Anthropic's `input_schema` doesn't directly work in OpenAI's function format; cross-provider portability of augmentations is still a manual translation.

## Related concepts

- [[agentic-loop]] — the runtime; augmented-LLM is what runs inside.
- [[mcp-server]] — the standard tool-distribution mechanism for augmentation #1.
- [[claude-code-skills]] — a packaged augmentation pattern.
- [[agent-workflow-patterns]] — patterns that constrain how augmentations are composed in the loop.
- [[llm-wiki-pattern]] — augmentation #3 (memory) implemented as a curated knowledge base.

## Related entities

- [[wiki/entities/anthropic]] — `input_schema` tool format.
- [[wiki/entities/anthropic-agent-sdk]]
- [[wiki/entities/openai-agents-sdk]]
- [[wiki/entities/claude-mem]]
- [[wiki/entities/claude-subconscious]]

## Mentioned in

- [[wiki/sources/hooeem-build-an-ai-agent-today]]
