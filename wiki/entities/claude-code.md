---
type: entity
title: Claude Code
entity_type: product
created: 2026-05-02
updated: 2026-05-02
website: https://claude.com/claude-code
aliases: [claude-code, Claude Code CLI]
tags: [claude-code-ecosystem, ai-tooling]
---

# Claude Code

> Anthropic's command-line AI coding agent — the platform that the [[markdown-as-agent-contract]] family ([[CLAUDE]], [[claude-code-skills]], [[claude-code-hooks]], [[claude-code-slash-commands]]) is built around. The runtime substrate underneath nearly every tooling source ingested in this wiki.

## Profile

Claude Code is Anthropic's official CLI for working with Claude models. It is positioned as an interactive coding agent that can read files, edit them, run shell commands, invoke MCP servers, and orchestrate subagents. In this wiki it is the **central platform** — both ingested sources on AI tooling ([[wiki/sources/regent0x-claude-code-247-dev-team]] and [[wiki/sources/khairallah-ai-automations-10k-month]]) treat Claude Code as the substrate on which their stacks are built. The patterns this wiki tracks ([[CLAUDE]], [[claude-code-skills]], [[claude-code-hooks]], [[claude-code-slash-commands]], [[subagents]], [[multi-agent-orchestration]]) are all Claude Code mechanisms.

## Key facts

- **Maintainer**: [[wiki/entities/anthropic]].
- **Distribution**: CLI; also surfaces in Anthropic's desktop app, web app at claude.ai/code, and IDE extensions (VS Code, JetBrains).
- **Subscription model**: Pro plan $20/mo per [[wiki/sources/regent0x-claude-code-247-dev-team]]'s claim. Anthropic's pricing pages are the authoritative source.
- **Mechanisms** layered on top:
  - [[CLAUDE]] / `CLAUDE.md` — project-level contract.
  - [[claude-code-skills]] — invokable capabilities (markdown + frontmatter).
  - [[claude-code-hooks]] — lifecycle automation (pre-commit, session-start, etc.).
  - [[claude-code-slash-commands]] — invocation shortcuts.
  - [[subagents]] — role-specialized session delegation.
  - [[mcp-server]] — external tool integration via Model Context Protocol.
  - [[scheduled-automation]] — `/schedule`-registered routines.
- **Plugin marketplace**: ships official plugins (e.g. `superpowers@claude-plugins-official`); third-party plugin distribution by repo.
- **Orchestration ecosystem**: external tools like [[wiki/entities/claude-squad]] (terminal multiplexer) and [[wiki/entities/claude-flow]] (enterprise orchestration framework) are built around Claude Code.

## Positions and claims

- **Claude Code is enough**, with the right configuration, to function as a "24/7 dev team" on a $20/mo subscription. *(Claim of [[wiki/sources/regent0x-claude-code-247-dev-team]]; this wiki's own existence is corroborating evidence at smaller scale.)*
- **Claude Code is the platform on which a viable AI automations services business runs.** *(Claim of [[wiki/sources/khairallah-ai-automations-10k-month]].)*

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — central subject.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — implicit platform across all six phases.

## Related entities

- [[wiki/entities/anthropic]] — maintainer.
- [[wiki/entities/superpowers]] — workflow plugin built for Claude Code.
- [[wiki/entities/claude-mem]] — persistent-memory tool.
- [[wiki/entities/claude-subconscious]] — background-memory agent.
- [[wiki/entities/anthropic-skills]] — official skill collection.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — third-party skill collection.
- [[wiki/entities/tdd-guard]] — TDD-enforcement skill.
- [[wiki/entities/claude-squad]] — terminal multiplexer for parallel Claude Code agents.
- [[wiki/entities/claude-flow]] — enterprise orchestration framework.
- [[wiki/entities/wshobson-agents]] — subagent collection.
- [[wiki/entities/davepoon-subagents-collection]] — subagent collection.
- [[wiki/entities/wshobson-commands]] — slash command collection.

## Related concepts

- [[CLAUDE]]
- [[claude-code-skills]]
- [[claude-code-hooks]]
- [[claude-code-slash-commands]]
- [[subagents]]
- [[multi-agent-orchestration]]
- [[mcp-server]]
- [[scheduled-automation]]
- [[markdown-as-agent-contract]]
