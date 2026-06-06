---
type: concept
title: AGENTS.md
created: 2026-05-02
updated: 2026-06-06
aliases: [agents.md]
tags: [agent-config, markdown]
---

# AGENTS.md

> Markdown file that serves as the agent-contract for OpenAI Codex and other generic-agent setups; analog of [[CLAUDE]] for non-Claude agents.

## Definition

AGENTS.md is a markdown file at the root of a project that an agent reads to learn the local conventions, workflows, and constraints — one of the canonical instances of [[markdown-as-agent-contract]]. It is the OpenAI Codex (and generic-agent) analog of [[CLAUDE]]: same role and substantially the same content, different consumer and filename.

## Treatment across sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — names AGENTS.md alongside CLAUDE.md as the schema-document analog used by OpenAI Codex.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] frames it as Codex's mirror of CLAUDE.md — *"same content as CLAUDE.md, different filename"* — and notes a one-prompt conversion can generate AGENTS.md directly from an existing CLAUDE.md. First primary-source treatment in this wiki.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it thinly-corroboratively: the CLAUDE.md onboarding doc is the same agent-contract-markdown convention.

## Sub-claims and details

- Treated as the **Codex-flavored equivalent** of [[CLAUDE]] — same role (project-level conventions and instructions for an agent), different consumer.
- Belongs to the [[markdown-as-agent-contract]] family alongside [[CLAUDE]], [[design-md]], [[skill-md]], [[readme-md]].
- **Generatable from CLAUDE.md by a single prompt** — because the content is essentially identical, porting a Claude Code project to Codex is largely a filename/format conversion ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Cross-tool portability**: maintaining AGENTS.md alongside CLAUDE.md lets the same project be driven by both Claude Code and Codex with parity ([[wiki/sources/nateherk-claude-code-codex-same-project]]).

## Open questions and contradictions

- **Drift between AGENTS.md and CLAUDE.md.** When both files coexist in one repo, keeping them in sync is unaddressed by the sources — the one-prompt conversion is a one-time port, not a sync mechanism.

## Related concepts

- [[markdown-as-agent-contract]] — the meta-pattern AGENTS.md instantiates.
- [[design-md]] — sibling instance for the design-systems domain.
- [[llm-wiki-pattern]] — uses CLAUDE.md, the closest sibling.
- [[subagents]] — subagent definition files also differ across Claude Code (markdown) and Codex (TOML), paralleling the CLAUDE.md/AGENTS.md split.

## Mentioned in

- [[wiki/sources/llm-wiki-pattern-karpathy]]
- [[wiki/sources/nateherk-claude-code-codex-same-project]]
- [[wiki/sources/charliejhills-full-agent-system-6-steps]]
- [[wiki/concepts/markdown-as-agent-contract]]
