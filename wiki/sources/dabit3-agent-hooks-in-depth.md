---
type: source
title: Nader Dabit — Agent Hooks (Deterministic Control for Agent Workflows)
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/dabit3/status/2055319214202777894
source_type: x-thread
author: Nader Dabit (dabit3)
source_date: 2026-05-15
raw_path: raw/Agent Hooks Deterministic Control for Agent Workflows.md
content_status: substantive-verbatim
tags: [agent-hooks, claude-code-hooks, deterministic-control, lifecycle-events, agent-workflows, programmable]
---

# Nader Dabit — Agent Hooks (Deterministic Control for Agent Workflows)

> Nader Dabit's deep-dive on **agent hooks** — the mechanism that makes agent workflows *programmable* by attaching user-defined handlers to specific lifecycle points in an agent session. Companion GitHub repo: [`dabit3/agent-hooks-in-depth`](https://github.com/dabit3/agent-hooks-in-depth). Frames the value proposition crisply: *"Use prompts for guidance. Use hooks for behavior that should run every time."* Six lifecycle points covered as a starter set: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop`, `SessionEnd`.

## TL;DR — the value proposition

Prompts say *"please do X"* and rely on the model to remember and follow. Hooks **inspect and act at lifecycle points** deterministically.

| Prompt example | Hook equivalent |
|---|---|
| *"Do not edit generated files."* | `PreToolUse` hook inspects the attempted edit and **blocks it** before it happens. |
| *"Run tests before finishing."* | `PostToolUse` hook runs the test suite after edits; `Stop` hook **prevents completion** when the last test run failed. |

> *"Hooks make the agent workflow programmable. If you've ever reminded an agent twice to avoid a file, run a test, or follow a release rule, you have already found a use case for hooks."*

> *"The main value proposition is deterministic control: rules already captured in scripts, tests, policy checks, and runbooks can run at known lifecycle points in the agent workflow instead of depending on the model to remember and voluntarily follow them."*

## The six starter-set lifecycle points

| Hook | When | Use for |
|---|---|---|
| **SessionStart** | Session starts | Load project conventions, active constraints, environment facts, runbook context |
| **UserPromptSubmit** | Before model sees prompt | Add context, route the request, block known-bad prompts |
| **PreToolUse** | Before tool call runs | Block / approve / modify behavior per project policy |
| **PostToolUse** | After successful tool call | Validation: run tests, formatting, scanning, logging, state capture |
| **Stop** | Before agent finishes turn | Check whether agent is allowed to finish (e.g. tests must pass) |
| **SessionEnd** | Session ends | Final logs, flush metrics, export summary, clean up temp state |

Other hooks exist (per [code.claude.com/docs/en/hooks#hook-lifecycle](https://code.claude.com/docs/en/hooks#hook-lifecycle) and `cli.devin.ai/docs/extensibility/hooks/lifecycle-hooks`) — these six cover *"the main flow developers usually need first."*

## The operating model

```
event → optional matcher/filter → handler → outcome
```

- **event** — lifecycle point (e.g. `PreToolUse`).
- **matcher/filter** — narrow which calls/events the handler responds to (e.g. only `PreToolUse` for `Write` on `*.generated.ts`).
- **handler** — user-defined function/script that receives event data.
- **outcome** — return context, make a decision, perform a side effect, or block.

## How this composes with the wiki

- [[wiki/concepts/claude-code-hooks]] — **major refresh** required. Dabit's source provides:
  - The 6-lifecycle-point taxonomy (the wiki currently has informal references; Dabit names them canonically).
  - The *event → matcher → handler → outcome* operating model.
  - The *"prompts for guidance, hooks for every-time behavior"* discipline rule.
  - The companion GitHub repo with example code.
- [[wiki/sources/zodchiii-x-claude-code-settings]] — companion source. zodchiii's earlier post showed concrete `PostToolUse` (auto-prettier) and `PreToolUse` (log preprocessing) hook examples. Dabit's source generalizes the pattern.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — sibling. zodchiii lists hooks as one of three host surfaces for Claude Code agents; Dabit provides the depth treatment.
- [[wiki/concepts/markdown-as-agent-contract]] — hooks complement markdown contracts. Contracts say what the agent *should* do; hooks enforce what the agent *must* do. The two compose: contract is the soft layer, hooks are the hard layer.
- [[wiki/projects/helm]] — Helm's APScheduler-based scheduled jobs are *agent-level* hooks (cron triggers). Worth absorbing Dabit's 6-lifecycle-point model into Helm's master CLAUDE.md as the in-session enforcement layer (vs the cross-session orchestration layer Helm already has).
- [[wiki/concepts/anti-ai-slop-machinery]] — Open Design's pre-emit gates / P0/P1/P2 / blacklist are conceptually *PreToolUse hooks for content output*. Dabit's general model formalizes what anti-ai-slop-machinery articulates for one specific domain.

## Notable quotes

> *"Use prompts for guidance. Use hooks for behavior that should run every time."*

> *"A project instruction can say 'do not edit generated files,' but a PreToolUse hook can inspect the attempted edit and block it before it happens."*

> *"Rules already captured in scripts, tests, policy checks, and runbooks can run at known lifecycle points in the agent workflow instead of depending on the model to remember and voluntarily follow them."*

## Mentioned entities

- [[wiki/entities/dabit3]] — *(new)* Nader Dabit; AWS Amplify alumnus; agent-systems author.
- [[wiki/entities/claude-code]] — primary surface.
- [[wiki/entities/devin-cli]] — *(stub candidate)* alternate hook implementation; named via `cli.devin.ai/docs/extensibility/hooks/lifecycle-hooks`.

## Related concepts

- [[claude-code-hooks]] — concept page primary upgrade target.
- [[markdown-as-agent-contract]] — soft layer; hooks are the hard layer.
- [[anti-ai-slop-machinery]] — domain-specific instance of hook-style enforcement.
- [[reasoning-execution-split]] — hooks are the deterministic-execution counterpart to model-driven reasoning.

## Related sources

- [[wiki/sources/zodchiii-x-claude-code-settings]] — concrete hook examples.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — agents-via-hooks pattern.
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — Hook implementation maps to NainsiDwiv's 7-step (Step 3 Error handling and Step 7 Evaluation become concrete via `Stop` and `PostToolUse` hooks).
