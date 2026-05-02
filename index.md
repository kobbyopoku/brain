# index.md — Wiki catalog

The content-oriented index of this wiki. Read this first when answering a query, then drill into the linked pages. See [[CLAUDE]] for conventions and [[log]] for the chronological record of operations.

**Stats**: 4 sources · 44 entities · 20 concepts · 0 syntheses · last updated 2026-05-02

---

## Sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — Karpathy's pattern for LLM-maintained personal knowledge bases; foundational for this vault.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — Refero's curated DESIGN.md catalog for AI coding agents; landing-page clipping.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — six-layer Claude Code stack (CLAUDE.md → memory → skills → subagents → hooks → orchestration); first wild citation of Karpathy's LLM Wiki.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — six-phase playbook for selling AI automations as a services business at $3-15k per build.

## Entities

### People

- [[wiki/entities/andrej-karpathy]] — author of the LLM Wiki pattern.
- [[wiki/entities/eng-khairallah]] — author of the AI Automations services playbook.
- [[wiki/entities/regent0x]] — author of the Claude Code 24/7 dev team stack.
- [[wiki/entities/vannevar-bush]] — 1945 originator of the [[memex]]; conceptual ancestor of the LLM Wiki.

### Organizations

- [[wiki/entities/anthropic]] — AI research company; maintainer of Claude and Claude Code; operator of this wiki's runtime.
- [[wiki/entities/trail-of-bits]] — security firm publishing claude-code-skills.

### Knowledge tooling

- [[wiki/entities/obsidian]] — local-first markdown editor; the working environment for this vault, also the persistent-memory layer in regent0x_'s stack.
- [[wiki/entities/qmd]] — local hybrid search engine for markdown wikis at scale.
- [[wiki/entities/refero]] — curated DESIGN.md library + MCP server for AI coding agents.

### Claude Code ecosystem

- [[wiki/entities/claude-code]] — Anthropic's CLI; the central platform across the tooling sources.
- [[wiki/entities/superpowers]] — workflow-discipline plugin (brainstorm → spec → plan → TDD → implement → review).
- [[wiki/entities/anthropic-skills]] — Anthropic's official skill collection.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — Trail of Bits's security audit skill collection.
- [[wiki/entities/tdd-guard]] — TDD-enforcement skill / pre-commit hook.
- [[wiki/entities/claude-mem]] — session-end memory compression and carry-forward.
- [[wiki/entities/claude-subconscious]] — continuous background memory builder.
- [[wiki/entities/wshobson-agents]] — production subagent collection.
- [[wiki/entities/davepoon-subagents-collection]] — drop-in subagent collection.
- [[wiki/entities/wshobson-commands]] — production slash command collection.
- [[wiki/entities/claude-squad]] — terminal multiplexer for parallel Claude Code agents.
- [[wiki/entities/claude-flow]] — enterprise-grade multi-agent orchestration framework.

### MCP integrations

- [[wiki/entities/tavily]] — web search MCP server.
- [[wiki/entities/google-drive]] — file-storage MCP integration.
- [[wiki/entities/gmail]] — email MCP integration.
- [[wiki/entities/slack]] — communications MCP integration.

### Brands in Refero catalog (stubs)

Stub pages awaiting substantive primary sources. Their only current content is a backlink to [[wiki/sources/refero-design-systems-for-ai-agents]] and Refero's mood descriptor.

- [[wiki/entities/acctual]]
- [[wiki/entities/antimetal]]
- [[wiki/entities/apple]]
- [[wiki/entities/base44]]
- [[wiki/entities/column]]
- [[wiki/entities/cursor]]
- [[wiki/entities/dia-browser]]
- [[wiki/entities/elevenlabs]]
- [[wiki/entities/family]]
- [[wiki/entities/general-intelligence-company]]
- [[wiki/entities/hyperstudio]]
- [[wiki/entities/linear]]
- [[wiki/entities/mercury]]
- [[wiki/entities/minimalissimo]]
- [[wiki/entities/monopo-saigon]]
- [[wiki/entities/raycast]]
- [[wiki/entities/stripe]]
- [[wiki/entities/superhuman]]
- [[wiki/entities/titan]]

*(Anthropic was previously listed here as a stub but has been promoted to Organizations now that substantive sources cite it.)*

## Concepts

### Operations of the LLM Wiki

- [[wiki/concepts/ingest]] — the write path: process a new raw source into wiki pages.
- [[wiki/concepts/lint]] — periodic health check across the wiki.
- [[wiki/concepts/query]] — the read path: answer questions against the wiki with citations.

### Patterns and meta-patterns

- [[wiki/concepts/ai-automation-services]] — services-business model for selling AI automations.
- [[wiki/concepts/llm-wiki-pattern]] — persistent, LLM-maintained markdown wiki built on top of curated raw sources.
- [[wiki/concepts/markdown-as-agent-contract]] — meta-pattern: markdown files as the contract layer between humans and AI agents.
- [[wiki/concepts/memex]] — Vannevar Bush's 1945 vision of a personal, associative knowledge store.
- [[wiki/concepts/retrieval-augmented-generation]] — per-query retrieval over raw documents; contrast case for the LLM Wiki.

### Claude Code mechanisms

- [[wiki/concepts/claude-code-hooks]] — lifecycle automation (pre-commit, session-start, pre-push).
- [[wiki/concepts/claude-code-skills]] — the skill mechanism; markdown-defined invokable capabilities.
- [[wiki/concepts/claude-code-slash-commands]] — user-defined invocation shortcuts.
- [[wiki/concepts/multi-agent-orchestration]] — running multiple Claude Code agents in parallel against isolated workspaces.
- [[wiki/concepts/scheduled-automation]] — `/schedule`-registered routines running unattended.
- [[wiki/concepts/subagents]] — multi-agent role specialization (architect/coder/reviewer/tester/ops).

### Integration & data layer

- [[wiki/concepts/mcp-server]] — Model Context Protocol server; the tool-integration layer.

### Agent-contract markdown files

- [[wiki/concepts/agents-md]] — *(stub)* AGENTS.md — Codex-flavored project contract.
- [[wiki/concepts/context-file]] — per-client business voice/standards file (paired with skill files).
- [[wiki/concepts/design-md]] — DESIGN.md — design-system reference for AI coding agents.
- [[wiki/concepts/readme-md]] — *(stub)* README.md — older convention being absorbed into the agent-contract family.
- [[wiki/concepts/skill-md]] — *(stub)* SKILL.md — single-capability instructions.

## Syntheses

_(none yet — file substantive query answers here as `wiki/syntheses/<slug>.md`)_

---

## Reading paths

A few suggested entry points into the wiki:

- **"What is this vault and how does it work?"** → [[CLAUDE]] → [[wiki/concepts/llm-wiki-pattern]] → [[wiki/sources/llm-wiki-pattern-karpathy]].
- **"Why this approach over RAG?"** → [[wiki/concepts/retrieval-augmented-generation]] → [[wiki/concepts/llm-wiki-pattern]].
- **"Where does this idea come from historically?"** → [[wiki/concepts/memex]] → [[wiki/entities/vannevar-bush]].
- **"How do markdown files fit into AI tooling more broadly?"** → [[wiki/concepts/markdown-as-agent-contract]] → [[wiki/concepts/design-md]] → [[wiki/entities/refero]].
- **"How do I get the most out of Claude Code?"** → [[wiki/sources/regent0x-claude-code-247-dev-team]] → [[wiki/entities/claude-code]] → [[wiki/concepts/subagents]] → [[wiki/concepts/multi-agent-orchestration]].
- **"How do I sell AI automations as a service?"** → [[wiki/sources/khairallah-ai-automations-10k-month]] → [[wiki/concepts/ai-automation-services]] → [[wiki/concepts/context-file]] → [[wiki/concepts/mcp-server]].
- **"What MCP servers should I know about?"** → [[wiki/concepts/mcp-server]] → [[wiki/entities/tavily]], [[wiki/entities/gmail]], [[wiki/entities/google-drive]], [[wiki/entities/slack]].
