---
type: concept
title: Multi-Agent Orchestration
created: 2026-05-02
updated: 2026-06-06
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
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — frames the cadence layer of the [[ai-os-pattern|AI OS]] as the third part of orchestration: capabilities make Claude useful when you ask, **cadence** makes it useful when you don't. Three options with explicit tradeoffs (Cloud Routines / Local Scheduled Tasks / Loop) — see [[scheduled-automation]]. The author's framing of why this matters: *"Capabilities make Claude useful when you ask. Cadence makes it useful when you don't."*
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] frames it as Blueprint 03 (Autonomous Stack): a three-agent system — Content Agent (generates), Analytics Agent (reads X performance), Optimization Agent (updates the Voice Style Guide) — fully autonomous with a weekly feedback loop.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] frames it as Checkpoint-3: multi-agent pipelines / parallel architectures — split the job so one agent plans, others execute, one synthesizes.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] frames it as two agents (Claude Code + Codex) running in two terminals on the same folder; nateherk warns to coordinate which agent owns which file to avoid simultaneous-edit overwrites.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it as a model-tiered multi-agent split (Step 5): Opus Strategist → Sonnet Builder → QA Gate at 95/100.
- [[wiki/sources/gregisenberg-36-startup-opportunities]] frames it as the basis of the "agentic AI applied to vertical X" opportunity cluster (#2 employees, #11 dealership advisor, #21 bookkeeping agents, #31 trip rebooking) — each presumes orchestrated agents performing work autonomously.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as harness component #11: Claude Code's Fork/Teammate/Worktree, OpenAI's agents-as-tools + handoffs, LangGraph's nested state graphs. Decision rule #1: maximize a single agent first; split only past ~10 overlapping tools or clearly separate domains.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] frames it as Pattern 1: senior engineers launch parallel `claude -p` agents on different codebase regions (auth refactor / tests / docs) and review-discard-merge; Farhan Thawar calls it *"orchestrating intelligent systems."* Enterprise-scale instance of the wiki's existing solo-operator descriptions.
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] refines this concept at Layer 10 by splitting **runtime** (where a single agent executes) from **orchestration** (how a network coordinates state, handoffs, parallelism, failure recovery) as separate concerns and separate procurement decisions. ~86% of 2026 enterprise copilot spend (~$7.2B) goes to agent-based systems; 59% of orgs run 3+ LLMs needing coordination.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] adds the Orchestrator/Builder/Reviewer role triad and a Kanban-card handoff model — every goal is a card storing PID/repo/done-criteria; the board replaces terminal-hunting. Parallelism only across clear boundaries (worktrees/repos/branches); one-writer-per-file rule.

## Sub-claims and details

- **Workspace isolation via git worktrees**: each agent operates on its own working tree backed by the same repo's `.git/`. Branches and commits are independent; merge happens via PRs.
- **Terminal-multiplexer interface**: at the personal scale, a TUI like `claude-squad` is enough — launch, monitor, pause, resume sessions.
- **Auto-accept vs. plan mode**: auto-accept (`cs -y`) for trusted tasks (the agent acts without confirmation prompts); plan mode for tasks where the human wants to approve the strategy before the agent executes.
- **Persistence across multiplexer detach**: closing the terminal does not stop the agents; they continue running. This is what makes the "wake up to PRs" pattern work.
- **Composition with [[subagents]]**: orchestration runs *agents*; each agent may itself dispatch to subagents (architect → coder → reviewer). Two-level concurrency.
- **Composition with [[claude-code-hooks]]**: hooks fire across orchestrated agents. A pre-commit hook applies to whichever agent is committing, regardless of which session.
- **Enterprise scale**: claude-flow is positioned as a more advanced framework with persistent memory and cross-agent coordination — closer to a multi-agent platform than a multiplexer.
- **Runtime vs orchestration are distinct concerns**: per [[wiki/sources/awrigh01-technical-stack-autonomous-agents]], runtime is where a single agent executes; orchestration is how a network coordinates state, handoffs, parallelism, and failure recovery — separate layers with separate procurement decisions.
- **Single-agent-first rule**: per [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]], maximize a single agent before splitting; split only past ~10 overlapping tools or when domains are clearly separate.
- **Role-based splits**: orchestrations recur as role triads — Orchestrator/Builder/Reviewer ([[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]); Content/Analytics/Optimization ([[wiki/sources/doublenickk-personal-x-agent-algorithm]]); model-tiered Opus Strategist → Sonnet Builder → QA Gate ([[wiki/sources/charliejhills-full-agent-system-6-steps]]); plan/execute/synthesize ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **One-writer-per-file**: when agents share a folder, coordinate file ownership to avoid simultaneous-edit overwrites ([[wiki/sources/nateherk-claude-code-codex-same-project]], [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]).
- **Market signal**: ~86% of 2026 enterprise copilot spend (~$7.2B) goes to agent-based systems; 59% of orgs run 3+ LLMs needing coordination ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).

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
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]]
- [[wiki/sources/vasuman-forward-deployed-engineering-101]]
- [[wiki/sources/nateherk-claude-code-codex-same-project]]
- [[wiki/sources/charliejhills-full-agent-system-6-steps]]
- [[wiki/sources/gregisenberg-36-startup-opportunities]]
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]
- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]]
