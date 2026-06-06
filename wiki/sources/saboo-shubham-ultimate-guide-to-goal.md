---
type: source
title: Shubham Saboo — The ultimate guide to /goal
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/Saboo_Shubham_/status/2054988166541770782
source_type: x-thread
author: Shubham Saboo (@Saboo_Shubham_)
source_date: 2026-05-12
raw_path: raw/The ultimate guide to goal.md
content_status: substantive-verbatim
tags: [goal-command, hermes-agent, codex-cli, claude-code, multi-agent-orchestration, verification, kanban, agent-primitive, autonomous-agents]
---

# Shubham Saboo — The ultimate guide to /goal

> Argues that `/goal` is not a feature but an emerging **cross-vendor primitive** — *"HTTP is a primitive. JSON is a primitive. /goal is becoming one for coding agents."* — and that its convergence across [[wiki/entities/codex-cli|Codex]], [[wiki/entities/claude-code|Claude Code]], and [[wiki/entities/hermes-agent|Hermes Agent]] is what lets an orchestrator route work between tools that *"share nothing else."*

## TL;DR

Saboo frames `/goal` as the shift from **prompting** (you steering every turn) to **assigning** (the agent driving toward a done-state you defined once and walked away from). The load-bearing thesis is convergence: three independently-built tools — Codex (builder), Claude Code (reviewer), Hermes (orchestrator) — all accept the same `/goal` instruction format, which is precisely what makes them composable into one pipeline. The companion thesis is verification: *"Without verification, /goal is just a fancier prompt. With verification, it becomes a contract"* — the orchestrator re-runs the worker's claimed tests/build itself rather than trusting the worker's self-report. A worked end-to-end run (one Telegram message → six Kanban cards → Codex builds → Claude Code reviews → Hermes verifies) demonstrates the model.

## Key takeaways

- **`/goal` is positioned as a primitive, not a feature.** Analogy: HTTP and JSON are primitives; `/goal` is becoming one for coding agents. Value comes from *convergence* across vendors, not from any single tool shipping it.
- **Prompting vs. assigning is the core distinction.** A regular prompt asks for the next response (you steer every turn); a `/goal` records what "done" looks like, is submitted once, and the agent works toward it until reached.
- **A goal has a lifecycle.** It "stays active until it's achieved, paused, blocked, cleared, or it runs out of budget."
- **The primitive lives inside an interactive worker session, not a one-shot command.** `codex exec 'goal: build the app'` is "still a prompt with a label"; the real `/goal` is launched in the CLI, submitted, then walked away from.
- **Timeline of adoption.** OpenAI's Codex CLI added `/goal` "a few weeks ago"; Claude Code added it "this week" (≈ 2026-05-12); Hermes Agent has had it "for a while."
- **Three roles are stable even as tools change**: Orchestrator (owns the control loop — decomposition, worker selection, Kanban, verification, summary), Builder (spec → working code; bottleneck is implementation), Reviewer (finds what's wrong with code that looks right; bottleneck is correctness).
- **Tool-to-role mapping in Saboo's setup**: Codex = builder (strong at implementation given a clear spec); Claude Code = reviewer (strong at the inverse — spec compliance, safety, error states, security holes); Hermes = orchestrator (not a coding worker; coordinates the other two).
- **The Kanban board is what `/goal` becomes once an orchestrator sits on top of it.** Every goal gets a card; each card stores process id/PID, repo, and done criteria; every handoff leaves a trail. Replaces "hunting through terminals" with watching work move across columns on a phone.
- **The verifier is what turns a `/goal` into a contract instead of a promise.** Hermes never trusts the worker's self-report — after Codex marks the build done, Hermes itself runs `npm test` (17 tests passed) and `npm run build` (vite build passed).
- **Coding agents are confidently wrong.** "They'll tell you the build passes when the build was never run. They'll tell you tests pass when they wrote tests that never executed." The verifier closes that gap.
- **Setup itself becomes a goal.** Saboo didn't hand-install Codex and Claude Code on the Mac Mini; he messaged Hermes to install both and log him in. "Setup is just another goal."
- **Parallelism requires clear boundaries.** Default is one main builder per repo; parallelism is added across boundaries where workers can't collide (different repos/branches, git worktrees, separate packages, docs-vs-code, tests-vs-implementation). The bad pattern is three workers editing the same file in the same repo (conflicts, partial overwrites, silent undo).
- **One-writer-at-a-time is the safe rule.** Builder writes, reviewer only reads, fix-goals stay scoped — or run competing approaches in separate worktrees and let the orchestrator pick the winner.
- **Skipped cards still carry meaning.** In the worked run, the "Codex fix loop" and "final verification" cards were skipped because the review passed — demonstrating the orchestrator can model conditional work.
- **The portability payoff is forward-looking.** "The next coding tool that adopts /goal will join this pipeline without me changing anything. I'll just route work to it."

## The worked run (one message, end to end)

Goal given to Hermes: *"Build a CLI tool that finds X mentions of me and pings me when something blows up."* Hermes decomposed it into six cards:

1. **Spec** — Hermes writes SPEC.md (stack, repo path, read-only constraints, mock-mode requirements, tests, verification commands). PM role.
2. **Codex builds** — runs `/goal` against SPEC.md; creates files, implements UI + backend, adds tests, reaches passing state (~15 min). `npm test` and `npm run build` pass; `git status` shows only relevant new files.
3. **Claude Code reviews** — runs `/goal` to review: spec compliance, read-only safety, API-key handling, error states, tests, UI usefulness, bugs, security. Result: PASS, no blocking issues.
4. **Codex fix loop** — skipped (review passed); would have re-handed findings to Codex as a new `/goal` if blocked.
5. **Claude Code final verification** — skipped (same reason).
6. **Hermes final summary** — working app at local path, UI + API verified in mock mode.

## Notable quotes

> "/goal is not a feature. It is a primitive. HTTP is a primitive. JSON is a primitive. /goal is becoming one for coding agents."

> "The shift is from prompting (you driving) to assigning (the agent driving toward a target you defined)."

> "Three different teams converged on the same primitive, and that convergence is what makes it possible to compose them."

> "The verifier is what makes a /goal a contract instead of a promise. Don't trust the worker's self-report as final. Trust the verifier."

> "Without verification, /goal is just a fancier prompt. With verification, it becomes a contract."

> "The workers can change, but the primitive stays the same."

## Notes

- **This source pairs tightly with [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide|Igor Buzovskyi's Hermes /goal full guide]].** Buzovskyi documents `/goal` *inside* Hermes (the v0.14 command surface: `/goal`, `/goal status/pause/resume/clear`, `/subgoal`, `/handoff`). Saboo zooms out one level — `/goal` as a *cross-vendor* primitive shared by Codex + Claude Code + Hermes, with the orchestrator routing between them. Buzovskyi is the "how Hermes implements it"; Saboo is the "why convergence on the format matters." They do not contradict; they are complementary altitudes.
- **The verification rule is the most transferable idea for Godwin's work.** "Trust the verifier, not the worker's self-report" is directly applicable to [[wiki/projects/helm|Helm]]'s multi-agent build and to any multi-tenant SaaS CI gate. It is the agent-orchestration analogue of the existing [[wiki/concepts/reasoning-execution-split|reasoning/execution split]]: the agent reasons and claims, but an external execution step (re-running tests/build) is the source of truth.
- **The role triad (Orchestrator / Builder / Reviewer) maps cleanly onto the wiki's existing [[wiki/concepts/do-framework|DOE framework]].** Orchestrator ≈ Orchestration layer; Builder + Reviewer ≈ Execution layer; the `/goal` text itself ≈ Directive. Saboo independently arrives at the same decomposition [[wiki/sources/zodchiii-10-claude-code-agents|zodchiii]] reaches via "job description + trigger + output."
- **"Setup is just another goal" is a small but notable claim** — it pushes the orchestrator's scope from task execution to environment provisioning, i.e. the orchestrator owns mechanical work end to end.
- **Uncertainty / dating**: the raw clipping's frontmatter gives `published: 2026-05-12` and an embedded board screenshot dated "May 12"; used as `source_date`. The "Claude Code added it this week" line places authorship in the same week. The specific Codex/Claude-Code `/goal` ship dates are Saboo's claim and are not independently verified here.
- The post is a marketing surface for Saboo's Hermes/OpenClaw/24-7-agent-team content (closes with a follow CTA); the technical argument stands on its own but the tool-recommendation framing is promotional.

## Mentioned entities

- [[wiki/entities/saboo-shubham]] — author; runs Hermes on a Mac Mini as a personal orchestrator coordinating Codex + Claude Code.
- [[wiki/entities/hermes-agent]] — the orchestrator role; has had `/goal` "for a while"; creates Kanban cards, picks workers, verifies output.
- [[wiki/entities/codex-cli|Codex]] — the builder role; OpenAI's coding CLI; "a few weeks ago" added `/goal`.
- [[wiki/entities/claude-code|Claude Code]] — the reviewer role; Anthropic's coding CLI; "this week" added `/goal`.
- [[wiki/entities/openai]] — publisher of Codex.
- [[wiki/entities/anthropic]] — publisher of Claude Code.
- [[wiki/entities/telegram]] — the surface Saboo messages Hermes from ("over Telegram from my phone").

## Related concepts

- [[goal-command]] — this source's central subject; framed as a cross-vendor agent primitive (prompting → assigning).
- [[agent-verification]] — "trust the verifier, not the worker's self-report"; what turns a goal into a contract.
- [[multi-agent-orchestration]] — Orchestrator/Builder/Reviewer triad; Kanban-card handoffs between tools that "share nothing else."
- [[do-framework]] — the role triad maps onto Directive / Orchestration / Execution.
- [[reasoning-execution-split]] — the verifier is the execution-as-source-of-truth side of the split.
- [[scheduled-automation]] — background `/goal` runs tracked on a durable board; "setup is just another goal."
- [[markdown-as-agent-contract]] — SPEC.md as the written done-criteria the builder runs against.

## Related sources

- [[wiki/sources/IBuzovskyi-x-hermes-goal-full-guide]] — companion: the in-Hermes command surface for `/goal` (v0.14). Saboo is the cross-vendor altitude; Buzovskyi is the Hermes-internal altitude.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — Codex + Claude Code as builder/reviewer on the same project; the two-tool half of Saboo's three-role model.
- [[wiki/sources/nousresearch-hermes-agent]] — the Hermes Agent product Saboo runs as orchestrator.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — "job description + trigger + output" is the same decomposition as Saboo's role triad.
- [[wiki/sources/shannholmberg-hermes-agent-operator]] — Hermes-as-orchestrator operator patterns; control-room / fleet framing.
