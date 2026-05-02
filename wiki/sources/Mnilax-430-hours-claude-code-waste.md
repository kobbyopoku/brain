---
type: source
title: I Tracked 430 Hours of Claude Code Usage — 73% Was Wasted on These 9 Patterns — Mnilax
created: 2026-05-02
updated: 2026-05-02
source_url: https://x.com/Mnilax/status/2050261839653556522
source_type: x-thread
author: Mnilax
source_date: 2026-05-01
raw_path: raw/I tracked 430 hours of Claude Code usage. 73% was wasted on these 9 patterns..md
tags: [claude-code-overhead, optimization, instrumentation, cost-analysis]
---

# I Tracked 430 Hours of Claude Code Usage — 73% Was Wasted on These 9 Patterns — Mnilax

> An instrumented 90-day study of Claude Code usage. The author ran an HTTP proxy between Claude Code and the Anthropic API, logged every request, and found **73% of tokens went to nine identifiable overhead patterns**. Each pattern is named with measured % cost and a 30-second fix. The wiki's canonical source on [[claude-code-overhead-patterns]].

## TL;DR

Mnilax ran an HTTP proxy between Claude Code and the Anthropic API for 90 days, logging 430 hours of work, 6M input tokens, $1,340 in API spend. After categorizing tokens into productive vs overhead, only **27% were productive**. The remaining 73% went to nine specific overhead patterns: CLAUDE.md bloat, conversation history re-reads, hook-injection waste, cache misses on session resume, skill loading on irrelevant tasks, "just in case" tool definitions, extended thinking on simple tasks, wrong-direction generation, and plugin auto-update redundancy. Each pattern has a measured percentage cost and a 30-second fix. After applying all nine fixes, the author's productive-token share went from 27% to ~65% — a 2.4× improvement on the same plan.

## Key takeaways

### Methodology
- HTTP proxy between Claude Code and Anthropic API; logged every request (full payload, response, token counts in/out/cache, latency, model).
- 90 days, 430 hours of active work, 6M input tokens, $1,340 spend.
- Categorized tokens: productive / cache-hit-free / cache-miss-paid / conversation history / hook injection / skill loading / tool overhead / extended thinking / CLAUDE.md.

### The 9 patterns (ranked by cost)

#### 1. CLAUDE.md bloat (~14%)
- Author's CLAUDE.md grew to 4,800 tokens. Every turn loaded all 4,800. Every session reloaded.
- 5,000-token CLAUDE.md × 200 turns/week ≈ 1M tokens/week tax just for CLAUDE.md.
- **Fix**: target combined (user + project) < 1,500 tokens. Cut framework rules to project-level. Extract repeated patterns into skills. Convert verbose rules into 3-word imperatives.
- Author cut from 4,800 → 900 tokens; **31% baseline reduction instantly**.

#### 2. Conversation history re-reads (~13%)
- Every follow-up re-tokenizes the entire conversation. Message 30 in a chat costs ~30× message 1.
- Author had 60+ message sessions; last message paid for 60 prior.
- **Fix**: edit-prior instead of follow-up; hard cap at 20 messages then `/compact` (not `/clear`).
- Author went from 60 → 15 average; **40% drop** in re-read cost.

#### 3. Hook injection waste (~11%)
- 4 plugins → 3 UserPromptSubmit hooks → 6,200 tokens of injection on every prompt before Claude reads what you asked.
- **Fix**: `cat ~/.claude/settings.json | jq '.hooks.UserPromptSubmit'`; disable any hook you can't justify per-task.
- Author 4 → 1 hook; **5,800 tokens saved per prompt**.

#### 4. Cache misses on session resume (~10%)
- Default 5-minute prompt cache lifetime. Coffee break = miss = full price for ~8K tokens of cached content.
- Happened ~640× across 90 days.
- **Fix**: keep cache warm with a hotkey-bound ping. Or upgrade (paid plans) to 1-hour cache lifetime; cache writes 2× base / cache reads 0.1× — pays for itself with 10+ resumes per session.
- Author runs 1-hour cache; **80% drop in cache-miss cost**.

#### 5. Skill loading on irrelevant tasks (~7%)
- 9 skills × ~1,500 tokens each = 13,500 tokens of overhead per task that didn't need any of them.
- Auto-invocation is conservative: when in doubt, load.
- **Fix**: 7-day audit (`grep "skill_invoked" ~/.claude/logs/*.log`); disable everything not in output.
- Author 11 → 4 skills; **9,000+ tokens saved per task**.

#### 6. "Just in case" tool definitions (~6%)
- 12 MCP servers connected; each ships its tool schema to every request. PostgreSQL MCP alone is ~1,200 tokens.
- 12 MCPs × ~600 avg = 7,200 tokens of tool defs per request.
- **Fix**: `/mcp disable <server>` per session; edit `~/.claude/settings.json` for permanent control.
- Author 12 → 3 always-on MCPs; **6,000 tokens saved per request**.

#### 7. Extended thinking on simple questions (~5%)
- "Advanced Thinking" globally on; 3,000+ thinking tokens on tasks like "rename this variable to camelCase."
- **Fix**: default OFF; toggle ON per-message for genuinely complex tasks (architecture, debugging) — Alt+T in Claude Code.

#### 8. Wrong-direction generation (~4%)
- Claude starts a 400-line response; first 50 lines reveal it's going wrong; user lets it finish, re-prompts. Remaining 350 lines = wasted output tokens (output tokens are billed).
- **Fix**: Cmd+. (Mac) / Ctrl+. stops generation; redirect from there. Double-Esc in terminal opens a checkpoint scroller for rewinding.

#### 9. Plugin auto-update redundancy (~3%)
- 9 plugins × multiple SessionStart messages = ~1,400 tokens at every session start, just for "loaded successfully" notifications.
- **Fix**: `cat ~/.claude/settings.json | jq '.hooks.SessionStart'`; kill any "loaded" notifications.
- Author 9 → 2 SessionStart hooks; **1,200 tokens saved per session start**.

### What didn't work
- **Switching to Haiku for "simple" tasks**: ~3% reduction. The waste isn't the model, it's the bloat. Cheap model on bloated context still loses to expensive model on lean context.
- **Aggressive `/clear`**: counter-productive, lost needed context.
- **Disabling all skills**: net negative — author started typing the same 200-token instructions manually.
- **Off-peak scheduling**: partial; ~7% of users affected per Anthropic, but the bigger lever is the patterns above.
- **Pure subscription downgrade**: cost per work-hour stayed the same.
- **Hunting the March 2026 caching bug**: not worth it for individuals; Anthropic patched it.

### The mental model shift

> "Every session is a long invoice that pre-charges you for: your CLAUDE.md (always), every active plugin's hooks (always), every active skill's SKILL.md (when relevance detected), every connected MCP's tool schema (always), conversation history up to that turn (always), cache miss recompilation (when session resumes after 5 min). **Productive tokens are the residual.**"

Better prompts only help when overhead is small. When overhead is 73%, prompts barely matter.

### The audit script

The source ships a single shell script (`claude-audit.sh`) that flags all 9 patterns at once: CLAUDE.md word count, active hooks, UserPromptSubmit injections, installed plugins/skills, connected MCPs, recent token usage averages.

## Notable quotes

> "73% of my tokens went to nine invisible patterns that I'd been doing on autopilot."

> "Every session is a long invoice that pre-charges you for [overhead]. Productive tokens are the residual."

> "Cheaper model on bloated context still costs more than expensive model on lean context."

> "Most 'Claude got dumber' complaints in 2026 trace back to this. The model didn't get dumber. Your overhead grew."

> "Cut the tax, the same plan suddenly has 2-3× more capacity."

## Notes

- **This source is directly applicable to this wiki's own setup.** The brain has a CLAUDE.md, multiple slash commands, hooks (eventually), skills (eventually). Worth running Mnilax's audit script against `~/.claude/CLAUDE.md` and `~/brain/CLAUDE.md` after this ingest. The risk surface is identical to the author's pre-fix state.
- **Anthropic admitted the problem in late March 2026**: usage limits hit faster than expected (Max 5 quota exhausted in 19 minutes; Pro $200/yr maxed every Monday, didn't reset until Saturday). Two cache-layer bugs inflated costs 10-20× silently for some sessions. Patched after a user reverse-engineered the binary (GitHub issue #40524).
- **The 27% → 65% productive-token improvement** is on the same plan with the same model. This is a 2.4× capacity increase from cleanup alone.
- **Worth tracking as a metric**: productive-token share. The wiki should consider adding a "what's the productive % of brain operations" question to periodic lints.
- The author promises a Part 2 on prompt-cache deep-dive — worth ingesting if/when it appears.

## Mentioned entities

### People
- [[wiki/entities/mnilax]] — author.

### Organizations
- [[wiki/entities/anthropic]] — operator of Claude / Claude Code; acknowledged the usage-limit issue in March 2026.

## Related concepts

- [[claude-code-overhead-patterns]] — canonical wiki source.
- [[claude-code-skills]] — skill loading is one of the 9 patterns.
- [[claude-code-hooks]] — hook injection is one of the 9 patterns.
- [[mcp-server]] — tool-definition overhead is one of the 9 patterns.
- [[claude-code-slash-commands]] — `/compact`, `/clear`, `/mcp` are referenced as fixes.
- [[CLAUDE]] — CLAUDE.md bloat is the largest single pattern.
- [[markdown-as-agent-contract]] — adjacent: the cost discipline of agent-contract files.

## Related sources

- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational sibling: nateherk's "prefer API endpoints saved as markdown over MCPs" is the same insight as Mnilax's MCP overhead pattern.
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — conceptual sibling: progressive disclosure is the architectural answer to the skill-loading-overhead pattern Mnilax measures.
- [[wiki/sources/regent0x-claude-code-247-dev-team]] — adds-tools sibling; Mnilax is the cuts-tools sibling. Both perspectives matter.
