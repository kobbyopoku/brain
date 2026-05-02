---
type: concept
title: Multi-Agent Orchestration
created: 2026-05-02
updated: 2026-05-02
aliases: [agent orchestration, parallel agents]
tags: [claude-code, multi-agent, infrastructure]
---

# Multi-Agent Orchestration

> Running multiple Claude Code agents in parallel against isolated workspaces — typically via git worktrees and a terminal multiplexer — so that overnight or background work can ship in parallel rather than serially.

## Definition

**Multi-agent orchestration** is the operational layer above [[subagents]]. Where subagents define *roles* (architect, coder, reviewer), orchestration runs *instances* of those roles in parallel, in isolated workspaces, against independent units of work. The workspace isolation is typically a git worktree — each agent gets its own checkout of the repo at its own branch — so two agents editing two different files cannot conflict at the working-tree level.

## Why it matters

A single Claude Code session works serially. Orchestration breaks the serial constraint: spin up three agents, each on a separate worktree, each working on a different issue, and they all progress in parallel. The author of [[wiki/sources/regent0x-claude-code-247-dev-team]] frames the value as **time-shifting work** — agents do at 3am what the human used to do at 3pm. The orchestration layer is what makes "Claude Code as a 24/7 dev team" more than a metaphor: it's literally multiple Claude sessions running while the laptop sits closed.

This is also where the cost-vs-throughput tradeoff becomes legible. Each parallel session uses its own tokens; orchestration scales work but also scales cost. Reasonable defaults (auto-accept for trusted tasks, plan-mode for risky ones) manage the risk side; rate limits manage the cost side.

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — names two orchestration tools: [[wiki/entities/claude-squad]] (terminal multiplexer; `brew install claude-squad; cs`; uses git worktrees for workspace isolation; `cs -y` for auto-accept on trusted tasks) and [[wiki/entities/claude-flow]] (called "enterprise-grade multi-agent orchestration with persistent memory", 11.4k+ stars per the post). Author's nightly workflow: three sessions on three independent units of work, close the laptop, wake to three PRs.

## Sub-claims and details

- **Workspace isolation via git worktrees**: each agent operates on its own working tree backed by the same repo's `.git/`. Branches and commits are independent; merge happens via PRs.
- **Terminal-multiplexer interface**: at the personal scale, a TUI like `claude-squad` is enough — launch, monitor, pause, resume sessions.
- **Auto-accept vs. plan mode**: auto-accept (`cs -y`) for trusted tasks (the agent acts without confirmation prompts); plan mode for tasks where the human wants to approve the strategy before the agent executes.
- **Persistence across multiplexer detach**: closing the terminal does not stop the agents; they continue running. This is what makes the "wake up to PRs" pattern work.
- **Composition with [[subagents]]**: orchestration runs *agents*; each agent may itself dispatch to subagents (architect → coder → reviewer). Two-level concurrency.
- **Composition with [[claude-code-hooks]]**: hooks fire across orchestrated agents. A pre-commit hook applies to whichever agent is committing, regardless of which session.
- **Enterprise scale**: claude-flow is positioned as a more advanced framework with persistent memory and cross-agent coordination — closer to a multi-agent platform than a multiplexer.

## Open questions and contradictions

- **Cross-agent coordination**: when agent A's PR depends on agent B's, how is the dependency expressed? Worktrees keep them isolated; coordination requires either explicit handoff or a higher-level scheduler. Not addressed in current sources.
- **Cost scaling**: with three parallel agents, token cost roughly triples. At what point does orchestration become economically irrational? Source asserts $20/mo Claude Pro is enough but doesn't quantify.
- **Failure surfacing**: if one of three nightly agents crashes mid-task, how is the human alerted? Implicit answer: morning review of the multiplexer view; explicit answer would be a better failure-notification system.
- **Conflict at merge time**: even with worktree isolation, two PRs may semantically conflict (touching different files but with logical dependencies). Merge-time review is still required; orchestration doesn't eliminate it.

## Related concepts

- [[subagents]] — the unit; orchestration runs instances of subagents in parallel.
- [[claude-code-skills]] — each orchestrated agent can have its own skill stack.
- [[claude-code-hooks]] — hooks fire across orchestrated sessions.
- [[markdown-as-agent-contract]] — each orchestrated agent's CLAUDE.md (and subagent files) lives as markdown.

## Related entities

- [[wiki/entities/claude-code]] — the platform being orchestrated.
- [[wiki/entities/claude-squad]] — terminal multiplexer for parallel sessions.
- [[wiki/entities/claude-flow]] — enterprise-grade orchestration framework.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
