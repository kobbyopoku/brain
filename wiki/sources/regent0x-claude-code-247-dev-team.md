---
type: source
title: How I Turned My Claude Code Into 24/7 Dev Team — regent0x_
created: 2026-05-02
updated: 2026-05-02
source_url: https://x.com/regent0x_/status/2049499354323399002
source_type: x-thread
author: regent0x_
source_date: 2026-04-29
raw_path: raw/How I Turned My Claude Code Into 247 Dev Team (Full Guide + Repos).md
tags: [claude-code, multi-agent, persistent-memory, tooling, llm-wiki-citation]
---

# How I Turned My Claude Code Into 24/7 Dev Team — regent0x_

> A six-layer recipe for using Claude Code as a continuously-learning, multi-agent dev team — CLAUDE.md → persistent memory → skills → subagents → hooks → orchestration — all on a $20/mo subscription. Notable as the first source in this wiki to explicitly cite Karpathy's [[llm-wiki-pattern]] in the wild.

## TL;DR

regent0x_ presents a stack of six layers that turn Claude Code from a stateless chatbot into an opinionated, persistent, parallel-running dev team. The foundation is an opinionated [[CLAUDE]] file with sections for project, conventions, architecture decisions, current focus, and rules. On top sits a persistent-memory layer (an Obsidian vault structured like Karpathy's [[llm-wiki-pattern]], plus `claude-mem` for session compression and `claude-subconscious` as a background memory builder). Skills (notably the `superpowers` plugin) discipline the agent's workflow into brainstorm → spec → plan → TDD → implement → review. [[subagents]] split work across specialized roles (architect/coder/reviewer/tester/ops). [[claude-code-hooks|Hooks]] and [[claude-code-slash-commands|slash commands]] automate repetitive moves. Finally, `claude-squad` (terminal multiplexer using git worktrees) orchestrates parallel sessions overnight. The author's central claim: the result is "agents doing work at 3am that I used to do at 3pm."

## Key takeaways

- **The foundation layer is a structured [[CLAUDE]] file**, not a generic intro. Concrete sections shown: `## project` (stack, deployment, monorepo paths), `## conventions` (naming, format rules, test colocation, commit format), `## architecture decisions` (with dates and rationale, e.g. "chose prisma over drizzle (dec 2024): type safety priority"), `## current focus`, `## rules` (e.g. "never mass edit more than 3 files without showing me the plan first"). This is a more **engineering-domain-specific** instantiation of [[markdown-as-agent-contract]] than this wiki's own CLAUDE.md.
- **The persistent-memory layer combines three tools**: an Obsidian vault structured as a wiki (`/decisions`, `/errors`, `/patterns`, `/sessions`, `/stack`, `Memory.md`, `index.md`), `claude-mem` for end-of-session compression and carry-forward, and `claude-subconscious` as a background agent that watches files and builds memory passively. The vault structure is **explicitly inspired by Karpathy's [[llm-wiki-pattern]]** — the post links to a `github.com/karpathy/llm-wiki` URL (see *Notes* below for a discrepancy).
- **Skills layer**: `superpowers` plugin (170k+ stars per the post; this wiki has corroborating context that the plugin is in the Anthropic plugin marketplace) enforces a brainstorm → spec → plan → TDD → implement → review workflow. Stacked with `trail-of-bits/claude-code-skills` (security audit), `anthropic/skills` (PDF/DOCX/XLSX, official), and `tdd-guard` (blocks commits that skip tests). See [[claude-code-skills]].
- **[[subagents]] architecture**: 5 specialized agents — **architect** (specs/plans, no code), **coder** (writes code, full tools), **reviewer** (security-first PR review), **tester** (TDD enforcement, paired with `tdd-guard`), **ops** (deploy/CI/CD/infra). Each agent has its own CLAUDE.md and tool-permission scope. Clean separation of concerns. Pre-built collections referenced: `wshobson/agents` (25k+ stars, claimed) and `davepoon/claude-code-subagents-collection` (100+ agents, claimed).
- **[[claude-code-hooks|Hooks]] and [[claude-code-slash-commands|slash commands]]** automate repetitive instructions. Specific examples: `/fix-issue 456` (read GitHub issue, branch, fix with tests, open PR), `/review` (reviewer agent + security + coverage), `/deploy staging`. Lifecycle hooks: pre-commit (tdd-guard test enforcement), session-start (load memory from Obsidian + recent session logs), pre-push (security review). The framing: **"you stop reminding claude of your rules because the rules enforce themselves."** Reference: `wshobson/commands` (1.7k+ stars per the post: 15 workflows + 42 tools).
- **Orchestration via `claude-squad`** — a terminal multiplexer specifically for parallel AI agent sessions. Each agent runs in an isolated git worktree to avoid branch conflicts. Author's nightly workflow: spin up three sessions ("fix all open bug issues", "write missing tests", "refactor dashboard to new design tokens"), enable auto-accept (`cs -y`) for trusted tasks, sleep, wake to three PRs. For more advanced multi-agent work, `claude-flow` (11.4k+ stars per the post) is referenced as enterprise-grade. See [[multi-agent-orchestration]].
- **Cost model**: $0 infrastructure + $20/mo Claude subscription (Pro plan). All six layers are free/open-source.
- **Quantified productivity claim**: 47 minutes/day saved by replacing repeated session-context-explanation. Plus the asynchronous overnight work via orchestration. Author tracked productivity for two weeks before/after but the source includes only an image of the comparison, not numeric data.
- **Bonus / on-ramp**: The author recommends starting with three layers in one afternoon (Claude.md + persistent memory + one skill plugin) before adding the rest.

## Notable quotes

> "most people use claude code like a chatbot. i turned mine into a 24/7 dev team that remembers everything and gets smarter every session"
> — opening framing

> "the idea comes from andrej karpathy's LLM wiki concept - instead of claude re-discovering knowledge from scratch every session, it reads from a persistent wiki that compounds over time"
> — § Part 2, persistent memory

> "you stop reminding claude of your rules because the rules enforce themselves"
> — § Part 5, hooks and slash commands

> "the agents are now doing work at 3am that i used to do at 3pm"
> — closing argument on ROI

## Notes

- **URL discrepancy worth flagging**: the post links to `github.com/karpathy/llm-wiki` as the source of the LLM Wiki concept. This wiki's foundational source ([[wiki/sources/llm-wiki-pattern-karpathy]]) is the gist at `gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`, not the URL the post cites. The repo URL the post links to may not exist; the gist URL is the authoritative one as of this wiki's reading.
- This is the **first secondary citation of Karpathy's LLM Wiki** captured in this wiki. Karpathy's pattern is now visibly propagating in the wild.
- The post's [[CLAUDE]] template style is **more engineering-domain-specific** than this wiki's own CLAUDE.md. It partially answers an open question on [[markdown-as-agent-contract]] ("does the pattern scale beyond moderate complexity?") — the answer demonstrated here is "yes, by being highly structured per-domain rather than generic."
- **Star-count and stars/share claims are unverified.** The post asserts 170k+ for superpowers, 25k+ for wshobson/agents, 11.4k+ for claude-flow, 1.7k+ for wshobson/commands, "100+" for davepoon. Treat as the post's claim, not independently verified.
- **Session-start hook to load Obsidian memory** is a useful concrete pattern that this vault could adopt: a hook that runs at session start and reads recent log entries plus index.md before the LLM begins.
- The author's nightly orchestration pattern is essentially **batch [[ingest|ingestion]] of work** rather than knowledge — same compounding idea, different artifact (PRs instead of wiki pages).
- **Ergonomic value**: the structured CLAUDE.md template at the top of the post is reusable as a starting point for engineering vaults. Worth keeping in mind for any future codebase work.

## Mentioned entities

### People
- [[wiki/entities/regent0x]] — author of the source.

### Organizations
- [[wiki/entities/anthropic]] — Claude Code maintainer; ships the official skills repo and the plugin marketplace.
- [[wiki/entities/trail-of-bits]] — security firm publishing claude-code-skills for security audits.

### Products and tools
- [[wiki/entities/claude-code]] — the Anthropic CLI; central subject of the source.
- [[wiki/entities/obsidian]] — recommended editor for the persistent-memory layer.
- [[wiki/entities/superpowers]] — Claude Code plugin enforcing the brainstorm → spec → plan → TDD → implement → review workflow.
- [[wiki/entities/claude-mem]] — session-compression memory tool.
- [[wiki/entities/claude-subconscious]] — background memory-building agent.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — security audit skill collection.
- [[wiki/entities/anthropic-skills]] — Anthropic's official skill collection (PDF/DOCX/XLSX/etc.).
- [[wiki/entities/tdd-guard]] — TDD enforcement; blocks commits that skip tests.
- [[wiki/entities/wshobson-agents]] — production subagent collection.
- [[wiki/entities/davepoon-subagents-collection]] — drop-in subagent collection.
- [[wiki/entities/wshobson-commands]] — slash command collection.
- [[wiki/entities/claude-squad]] — terminal multiplexer for parallel AI agent sessions.
- [[wiki/entities/claude-flow]] — enterprise-grade multi-agent orchestration framework.

## Related concepts

- [[llm-wiki-pattern]] — the source's persistent-memory layer is an explicit instantiation of this concept.
- [[markdown-as-agent-contract]] — the source's CLAUDE.md template is a domain-specific example.
- [[subagents]] — multi-agent specialization architecture.
- [[claude-code-skills]] — the skill mechanism the source heavily relies on.
- [[claude-code-hooks]] — lifecycle automation.
- [[claude-code-slash-commands]] — repetitive-instruction automation.
- [[multi-agent-orchestration]] — running parallel agents (claude-squad, claude-flow).

## Related sources

- [[wiki/sources/llm-wiki-pattern-karpathy]] — directly cited; this source's persistent-memory layer is built on Karpathy's pattern.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — sibling source on the same Claude Code primitives (CLAUDE.md, skills, MCP, /schedule) but framed as service-business economics rather than personal productivity.
