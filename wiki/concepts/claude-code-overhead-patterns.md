---
type: concept
title: Claude Code Overhead Patterns
created: 2026-05-02
updated: 2026-06-06
aliases: [claude code waste, the 9 overhead patterns, claude code optimization]
tags: [claude-code, optimization, cost-analysis, foundational]
---

# Claude Code Overhead Patterns

> Nine measured patterns of token-overhead in Claude Code usage that, in aggregate, can consume up to 73% of every session's tokens — leaving as little as 27% for actual productive work. Documented by Mnilax via 90 days of HTTP-proxy instrumentation.

## Definition

A **Claude Code overhead pattern** is a recurring, often-invisible category of token consumption that happens *before Claude reads what you actually asked*. The cost compounds across every turn of every session. [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 90-day study]] names nine such patterns, ranks them by measured % cost, and provides a 30-second fix for each.

The mental model the source contributes: **every Claude Code session is a long invoice that pre-charges you for** (CLAUDE.md, hook injections, skill SKILL.md content, MCP tool schemas, conversation history up to that turn, cache miss recompilation). Productive tokens are the *residual* after the overhead is paid.

## Why it matters

This concept reframes the most common 2026 complaint about Claude Code ("I'm hitting usage limits", "Claude got dumber"). Per the source: *"The model didn't get dumber. Your overhead grew."* Once you measure the patterns, you discover that better prompts barely help when 73% of tokens never reach the prompt.

The improvement potential is significant: the source's productive-token share went from 27% to ~65% after applying the nine fixes — a **2.4× capacity increase on the same plan**, no model change, no subscription upgrade.

For the brain itself, the concept is operationally critical. The wiki's [[CLAUDE]] is 188+ lines, ships multiple slash commands ([[brain/wiki/concepts/claude-code-slash-commands|/brain]], /brain-ingest, /brain-add-project, /brain-update-project), and will eventually ship hooks. Every pattern Mnilax names is a real risk surface as the brain grows.

## Treatment across sources

- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — canonical wiki source. 90-day instrumented study; 9 named patterns with measured percentages and concrete fixes; ships an audit script (`claude-audit.sh`) that flags all 9 at once.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational sibling: Nate independently identifies *"prefer API endpoints saved as markdown over MCPs"* (same as Mnilax's pattern #6) and emphasizes hardcoding values into skill.md to avoid runtime data crawls (variant of #6).
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]] — conceptual sibling: [[progressive-disclosure]] is the architectural answer to pattern #5 (skill loading on irrelevant tasks).
- [[wiki/sources/saraev-agentic-workflows-2026]] — independently observes the MCP overhead pattern in action: *"This thing has basically filled up about half of my entire context window. ... [MCP tools eat] 8.2% of my entire context window."* Third independent confirmation of Mnilax's pattern #6, with the same operational fix (load only the MCPs the directive needs).
- [[wiki/sources/nateherk-claude-design-tally-brand]] frames it as a token-economy discipline applied to Claude Design's separate weekly quota: the quota-stretching playbook (in-canvas edits over prompting, Sonnet for tweaks, one change per prompt, tight spec up front, watch-and-stop) is analogous to the measured overhead patterns.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] frames it as the consumer-chat-layer analogue — coarser and unmeasured: Steps 10/12/13 (specify output length, stop re-explaining via Projects, new-chat-per-topic to avoid context bleed) are token-overhead discipline at the chat layer.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] frames it via *"you pay for all of it on every turn"* — the cost-per-turn / context-bloat argument that motivates the keep-CLAUDE.md-lean (<60 line) prescription.

## The 9 patterns (ranked by cost)

| # | Pattern | % of total tokens | 30-second fix |
|---|---|---:|---|
| 1 | CLAUDE.md bloat | ~14% | Combined user + project < 1,500 tokens; extract repeated patterns into skills; verbose rules → 3-word imperatives |
| 2 | Conversation history re-reads | ~13% | Edit-prior instead of follow-up; hard cap 20 messages then `/compact` (not `/clear`) |
| 3 | Hook injection waste | ~11% | `cat ~/.claude/settings.json | jq '.hooks.UserPromptSubmit'`; disable any hook you can't justify |
| 4 | Cache misses on session resume | ~10% | Keep cache warm with hotkey ping (5-min default); upgrade to 1-hour cache lifetime if 10+ resumes per session |
| 5 | Skill loading on irrelevant tasks | ~7% | 7-day audit; disable any skill not actually invoked |
| 6 | "Just in case" tool definitions | ~6% | `/mcp disable <server>` per session; remove unused MCPs from auto-load |
| 7 | Extended thinking on simple questions | ~5% | Default OFF; toggle ON per-message (Alt+T) for genuinely complex tasks |
| 8 | Wrong-direction generation | ~4% | Cmd+. (Mac) / Ctrl+. stops generation; redirect from there |
| 9 | Plugin auto-update redundancy | ~3% | `cat ~/.claude/settings.json | jq '.hooks.SessionStart'`; kill "loaded" notifications |

## Sub-claims and details

### What makes this hard to see

- **Each pattern is small in isolation.** A 6,000-token MCP schema is "just" a few cents per request; the problem is it loads every request, regardless of whether the MCP is relevant.
- **Auto-invocation is conservative.** Skills load on uncertain relevance (when in doubt, load) — 9 skills × 1,500 tokens each is normal until you measure it.
- **Cache misses are silent.** The 5-minute default lifetime means a coffee break causes a full re-tokenization of system prompt + CLAUDE.md + tool schemas at full price (vs 0.1× for cache hits).

### What didn't work (per Mnilax)

The source explicitly tested and dismissed several "obvious" advice:

- **Switching to Haiku for simple tasks**: ~3% reduction. Cheaper model on bloated context still costs more than expensive model on lean context.
- **Aggressive `/clear`**: counter-productive (lost needed context).
- **Disabling all skills**: net negative (started typing same instructions manually).
- **Off-peak scheduling**: ~7% of users affected per Anthropic; bigger lever is overhead patterns.
- **Subscription downgrade**: cost per work-hour stayed the same.

### The audit script

Single shell script that flags all 9 patterns at once: CLAUDE.md word count, active hooks, UserPromptSubmit injections, installed plugins/skills, connected MCPs, recent token usage averages. Saved as `claude-audit.sh`; designed to run weekly until every line is in target.

### The Anthropic context (March 2026)

Anthropic acknowledged the broader usage-limit problem in late March 2026: Max 5 quota exhausted in 19 minutes vs expected 5 hours; Pro $200/yr maxed every Monday, didn't reset until Saturday. **Two cache-layer bugs silently inflated costs 10-20× for some sessions** — patched after a user reverse-engineered the Claude Code binary (GitHub issue #40524). Most remaining usage-limit pain is in the user's own setup, not Anthropic's bugs.

## Open questions and contradictions

- **Pattern composition**: do the percentages add cleanly, or do they overlap? Mnilax presents them as additive (sum = ~73%), but conversation re-reads and CLAUDE.md bloat probably double-count for some sessions.
- **The audit script's coverage**: it flags configuration-level overhead well but doesn't measure conversation-history cost (pattern #2) or wrong-direction generation (pattern #8). Those need behavioral discipline.
- **Cost vs capability tradeoff**: skills, hooks, and MCPs all add real capabilities. The fixes recommend cutting them aggressively; the right floor is unclear and probably user-specific.
- **The 27% → 65% claim is one author's experience.** The methodology is sound but the absolute starting and ending percentages may not generalize.

## Related concepts

- [[CLAUDE]] — pattern #1 is bloat in this file family.
- [[claude-code-skills]] — pattern #5 is skill-loading overhead.
- [[claude-code-hooks]] — patterns #3 and #9 are hook overhead.
- [[mcp-server]] — pattern #6 is MCP tool-definition overhead.
- [[claude-code-slash-commands]] — `/compact`, `/clear`, `/mcp` are referenced as fixes.
- [[progressive-disclosure]] — architectural answer to several of these patterns.
- [[markdown-as-agent-contract]] — adjacent: agent-contract files have a real cost discipline that's not part of the original pattern.

## Related entities

- [[wiki/entities/anthropic]] — operator of Claude Code; acknowledged usage-limit issues March 2026.
- [[wiki/entities/claude-code]] — the platform.
- [[wiki/entities/mnilax]] — author of the canonical source.

## Mentioned in

- [[wiki/sources/Mnilax-430-hours-claude-code-waste]]
- [[wiki/sources/nateherk-claude-code-os-3m-business]]
- [[wiki/sources/NainsiDwiv50980-equipping-agents-for-real-world]]
- [[wiki/sources/nateherk-claude-design-tally-brand]] — *2026-06-06*. Token-economy discipline applied to Claude Design's separate weekly quota (in-canvas edits, Sonnet for tweaks, one change per prompt, tight spec, watch-and-stop).
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] — *2026-06-06*. Consumer-chat-layer analogue (Steps 10/12/13): output-length control, Projects to stop re-explaining, new-chat-per-topic.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — *2026-06-06*. *"You pay for all of it on every turn"*; motivates the <60-line CLAUDE.md prescription.
- [[wiki/sources/nousresearch-hermes-agent]] — *2026-05-05*. [[wiki/entities/hermes-agent|Hermes Agent]]'s AGENTS.md elevates **prompt-cache preservation** to an architectural rule — state-changing commands default to *deferred* invalidation with explicit `--now` opt-in, rather than the naive "every change invalidates immediately" default. This is the structural answer to Mnilax's measured cache-invalidation cost pattern: rather than asking users to be careful, encode the discipline in command semantics.
