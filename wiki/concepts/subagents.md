---
type: concept
title: Subagents
created: 2026-05-02
updated: 2026-06-06
aliases: [subagent, sub-agents, claude-code-subagents]
tags: [claude-code, multi-agent, architecture]
---

# Subagents

> An architectural pattern in which one parent Claude Code session delegates work to multiple specialized agents, each with its own context, tool permissions, and single responsibility — instead of letting one session juggle every task and accumulate context pollution.

## Definition

A **subagent** is a separately-invoked Claude session, typically defined by a markdown file with a name, description, and instructions, that the parent agent can call as if it were a tool. Each subagent runs with its own scratch context, its own tool whitelist, and its own role-specific [[CLAUDE]]-style instructions. The pattern's defining move is **separation of concerns at the agent level**: a coder subagent never sees deployment configs; a reviewer subagent never writes code; an architect subagent plans but never edits.

## Why it matters

A single Claude Code session can only do one thing at a time, and its context accumulates noise as the conversation grows. By the fourth task — write a feature, review code, fix a bug, write docs — context pollution degrades quality. Subagents fix this by giving each task its own clean context, so a 10-task workflow becomes 10 fresh contexts of one task each rather than one overloaded context of 10 tasks. They also enable **parallelism** when paired with [[multi-agent-orchestration]] — multiple subagents can run simultaneously on independent work.

A second value: **role enforcement via tool scoping.** Because each subagent has its own permitted tools, "the reviewer cannot write code" is enforceable, not aspirational.

## Treatment across sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — describes a 5-role setup as a recommended baseline: **architect** (specs/plans, no code), **coder** (writes code, full tool access), **reviewer** (security-first PR review), **tester** (TDD enforcement, paired with [[wiki/entities/tdd-guard]]), **ops** (deploy/CI/CD/infra). References two pre-built collections: [[wiki/entities/wshobson-agents]] and [[wiki/entities/davepoon-subagents-collection]].
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — gives a worked example of the **context-window-isolation pattern**: a Pulse Check skill delegates heavy [[wiki/entities/clickup|ClickUp]] data work to a `clickup-searcher` sub-agent so the heavy data never blows the main context window. The principle: subagents aren't only for role specialization — they're also for **isolating expensive context loads** that would otherwise pollute the main session.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] frames it as a **cross-tool portability** concern: sub-agents diverge only in file format (markdown in Claude Code, TOML in Codex) and in routing behavior — Claude Code auto-routes to sub-agents by their description, whereas Codex requires explicit by-name invocation.
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] frames it as Step 5 of a 6-step build: *"each agent gets one file and one job"* — Strategist / Builder / QA Gate as single-purpose subagents.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] frames it as a **context-management strategy**: each subagent explores extensively but returns only a 1,000-2,000-token condensed summary to the parent, preserving the parent's context budget.

## Sub-claims and details

- **Each subagent has its own CLAUDE.md.** The parent's CLAUDE.md governs the project; each subagent's governs the role. This composes the [[markdown-as-agent-contract]] pattern — multiple contracts, one per agent, all in the repo.
- **Tool permissions are role-scoped.** A reviewer's tool list excludes Edit/Write; a coder's includes them; an ops agent has Bash and deploy tools but not Read on application code.
- **Common roles** (per regent0x_'s setup): architect, coder, reviewer, tester, ops. Other named roles seen in pre-built collections include security, design, strategy, docs.
- **Composition with skills**: a subagent can have its own skills loaded too. A reviewer subagent + the trail-of-bits security skill collection = a security-first PR reviewer.
- **Composition with [[multi-agent-orchestration]]**: subagents are the unit; orchestrators (e.g. [[wiki/entities/claude-squad]]) run multiple unit-instances in parallel via git worktrees.
- **Failure mode**: subagents that need shared state (e.g. coder writes a file the tester needs to read) require explicit handoff. Without it, isolation becomes a wall instead of a fence.
- **File format is platform-specific**: subagent definitions are markdown in Claude Code and TOML in Codex ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Routing differs by platform**: Claude Code auto-routes to a subagent by matching its description; Codex requires the parent to invoke the subagent explicitly by name ([[wiki/sources/nateherk-claude-code-codex-same-project]]).
- **Summarize-on-return is a context-preservation move**: a subagent can explore at length yet return only a 1,000-2,000-token condensed summary, keeping the parent's context lean ([[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]). This reframes subagents as a [[context-window]]-management primitive, not only a role-specialization one.
- **One-file-one-job naming**: the discipline of giving each subagent a single file and a single responsibility (e.g. Strategist / Builder / QA Gate) keeps roles legible and enforceable ([[wiki/sources/charliejhills-full-agent-system-6-steps]]).

## Open questions and contradictions

- **Where does the parent agent fit?** Is the parent itself a subagent (an "orchestrator" role), or a different category? The sources treat it as a different category but the line is blurry.
- **Re-entry**: when a subagent finishes, does its accumulated state persist for next time, or does each invocation start fresh? Design choice; not fully specified in the sources.
- **Prompt budget**: each subagent eats its own context tokens. Five subagents serially is roughly 5× the prompt cost of one session. Worth quantifying as the wiki ingests more sources on cost.

## Related concepts

- [[multi-agent-orchestration]] — running multiple subagents in parallel.
- [[markdown-as-agent-contract]] — each subagent's role file is one of these contracts.
- [[claude-code-skills]] — composes with subagents; each subagent can have its own skill stack.
- [[claude-code-hooks]] — hooks can fire during subagent invocations.

## Related entities

- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/wshobson-agents]] — pre-built subagent collection.
- [[wiki/entities/davepoon-subagents-collection]] — pre-built subagent collection.
- [[wiki/entities/tdd-guard]] — typically paired with the tester subagent.

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/nateherk-claude-code-codex-same-project]]
- [[wiki/sources/charliejhills-full-agent-system-6-steps]]
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]
