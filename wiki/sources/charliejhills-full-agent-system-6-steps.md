---
type: source
title: charliejhills — Build a full Claude Code agent system in 6 steps
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/charliejhills/status/2056374837237764428
source_type: x-thread
author: Charlie Hills (@charliejhills)
source_date: 2026-05-18
raw_path: raw/Post by @charliejhills on X.md
content_status: substantive-verbatim
tags: [claude-code, agents, skills, memory, context-file, claude-routines, multi-agent, ai-os-pattern]
---

# charliejhills — Build a full Claude Code agent system in 6 steps

> Charlie Hills's 6-step ladder for turning Claude Code from a code-writer into a self-running "agent system" — Install → Context → Memory → Skills → Agents → Routines — closing on *"It's a system that works without you in the room."*

## TL;DR

A short X post framing [[wiki/entities/claude-code|Claude Code]] as the substrate for a personal agent system rather than just a coding tool. The six steps stack into the now-familiar [[ai-os-pattern|AI-OS layering]]: a surface choice, a `CLAUDE.md` onboarding doc, per-correction memory files, slash-command skills, role-specialized subagents, and Claude Routines for scheduled cloud execution. Each layer "compounds" on the one below. The post is promotional (links to a Substack written guide and a YouTube video) but the architecture it sketches matches the wiki's existing six-layer Claude Code stack sources almost beat-for-beat.

## Key takeaways

- The thesis is that Claude Code "does more than write code" — it is the host for a full agent system, built in 6 ordered steps where "everything below it compounds."
- **Step 1 — Install**: Claude Code runs as a terminal tool, a desktop app, or a VS Code extension; the author says to "pick whichever surface fits how you work." The surface is a choice, not a constraint.
- **Step 2 — Build context**: `~/CLAUDE.md` is framed as "the onboarding doc" that "Claude reads before every session" and "every chat loads automatically" — a verbatim restatement of the [[context-file]] / [[agents-md]] pattern.
- **Step 3 — Build memory**: "Every correction becomes its own .md file" so "the same mistake never lands twice" — corrections externalized to individual markdown files, distinct from the single context doc.
- **Step 4 — Build skills**: a skill is "one command [that] fires a whole workflow across tools," removing the need to retype "a 200-word prompt every time." Worked shape: `/your-skill → Notion → Gmail → Drive → Output` (the [[claude-code-slash-commands]] / [[claude-code-skills]] pattern).
- **Step 5 — Build agents**: "Each agent gets one file and one job." Three named roles — **Strategist (Opus)** analyses the task, **Builder (Sonnet)** executes the output, **QA Gate** "fails anything below 95/100" — a model-tiered [[multi-agent-orchestration|multi-agent]] split with a quality gate.
- **Step 6 — Run on autopilot**: "Claude Routines run your team on Anthropic's cloud" on a schedule — e.g. "Daily 8am UK → runs in cloud," "Weekly Monday → drops to Notion." The [[scheduled-automation]] layer.
- The closing reframe: "This isn't 'using Claude.' It's a system that works without you in the room."
- The post links two companion guides: a Substack written guide (*"Build your 1st AI agent in Claude"*) and a YouTube video walkthrough.
- A reply from **@thearslaniqbal** independently endorses the QA-gate idea as drift prevention: "That's how you prevent agent drift" — an external articulation of the quality-gate-against-[[reasoning-execution-split|agent-drift]] rationale.

## Notable quotes

> "Claude Code does more than write code. How to build a full agent system in 6 steps."

> "~/CLAUDE.md is the onboarding doc — Claude reads before every session. Every chat loads it automatically."

> "Every correction becomes its own .md file. The same mistake never lands twice."

> "Each agent gets one file and one job. Strategist (Opus) → analyses the task. Builder (Sonnet) → executes the output. QA Gate → fails anything below 95/100."

> "This isn't 'using Claude.' It's a system that works without you in the room."

## Notes

- This is **the same six-layer Claude Code stack** the wiki has now seen multiple times — compare directly with [[wiki/sources/regent0x-claude-code-247-dev-team]] (CLAUDE.md → memory → skills → subagents → hooks → orchestration) and [[wiki/sources/nateherk-claude-code-os-3m-business]] (the AI OS playbook). Hills's ordering swaps hooks for "Routines" at the top, but the **install → context → memory → skills → agents → schedule** spine is identical. Worth treating as a *corroborating* source for [[ai-os-pattern]] rather than a novel one.
- **Step 3's "every correction becomes its own .md file"** is a notably crisp statement of memory-as-per-correction-files, distinct from the single-context-doc framing. This is close to the wiki owner's own auto-memory convention (one feedback file per learned preference). It is the same instinct as [[hot-cache]] but at finer granularity — one file per mistake rather than one rolling hot-context file. Mild uncertainty: the post doesn't specify *where* these files live or how Claude is pointed at them (a memory directory referenced from CLAUDE.md is the likely implementation, but it's not stated).
- **The Opus-Strategist / Sonnet-Builder / QA-Gate triad** is a concrete model-tiering recipe: reasoning-heavy planning on the expensive model, execution on the cheaper model, plus a numeric quality gate (95/100). This is a cleaner consumer-facing articulation of the [[reasoning-execution-split]] than most prior sources, and the "one file, one job" rule matches zodchiii's *job description + trigger + output* framing ([[wiki/sources/zodchiii-10-claude-code-agents]]).
- **"Claude Routines ... on Anthropic's cloud"** is the load-bearing platform claim. It implies a first-party Anthropic scheduled-execution surface ("Routines") that runs agents in the cloud on a cron-like schedule. The wiki's [[scheduled-automation]] coverage to date is mostly third-party (Hermes cron, APScheduler in Helm, SDK + cron in zodchiii). If "Claude Routines" is a real first-party Anthropic feature, it's worth a dedicated entity/concept once a primary Anthropic source is ingested. **Treat as author-asserted until confirmed** — this single promotional X post is not strong evidence on its own.
- The post is **promotional in shape** (lead magnet → Substack + YouTube), consistent with the broader X-creator content cluster in this wiki. Its value is corroboration of the AI-OS layering and the unusually clean memory-per-correction and model-tiering articulations, not new primary architecture.
- The replies include a vendor-pitch comment (@maguyvaai promoting "maguyva.ai — MCP Code Intelligence") arguing that *repo intelligence* is "the actual gap" after building the agent — a thread-level signal that codebase-context-for-agents is a perceived missing layer, though not part of Hills's own argument.

## Mentioned entities

- [[wiki/entities/charlie-hills]] — author (@charliejhills); X creator; runs the charliehills.substack.com guide series.
- [[wiki/entities/claude-code]] — the platform the entire 6-step system is built on.
- [[wiki/entities/claude-routines]] — Anthropic cloud scheduled-execution surface named in Step 6 (author-asserted).
- [[wiki/entities/anthropic]] — Routines run on "Anthropic's cloud."
- [[wiki/entities/notion]] — appears as a skill destination (Step 4 workflow) and Routine output target ("drops to Notion").
- [[wiki/entities/gmail]] — appears in the Step 4 skill workflow (`Notion → Gmail → Drive`).
- [[wiki/entities/google-drive]] — appears in the Step 4 skill workflow as "Drive."

## Related concepts

- [[ai-os-pattern]] — this post is a clean restatement of the layered Claude-Code-as-OS stack.
- [[context-file]] / [[agents-md]] — Step 2's `~/CLAUDE.md` onboarding doc.
- [[markdown-as-agent-contract]] — both the CLAUDE.md context and per-correction memory files are markdown contracts.
- [[hot-cache]] — Step 3's per-correction memory files are a finer-grained sibling of the rolling hot-context pattern.
- [[claude-code-skills]] / [[claude-code-slash-commands]] — Step 4's `/your-skill` one-command-fires-a-workflow.
- [[subagents]] / [[multi-agent-orchestration]] — Step 5's one-file-one-job Strategist/Builder/QA roles.
- [[reasoning-execution-split]] — Opus-strategist reasons, Sonnet-builder executes; QA gate guards against drift.
- [[scheduled-automation]] — Step 6's Claude Routines on a daily/weekly schedule.

## Related sources

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — the canonical six-layer Claude Code stack; near-identical spine.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — the AI OS playbook; same layering, introduces [[hot-cache]].
- [[wiki/sources/zodchiii-10-claude-code-agents]] — *job description + trigger + output*; matches Step 5's "one file, one job."
- [[wiki/sources/TheAIWorld22-x-claude-md-21-instructions]] — deep dive on the CLAUDE.md context layer (Step 2).
