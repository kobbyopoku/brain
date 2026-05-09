---
type: source
title: zodchiii — 15 Claude Code settings most developers never touch
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/zodchiii/status/2053042131111927976
source_type: x-thread
author: zodchiii (darkzodchi)
source_date: 2026-05-09
raw_path: raw/15 Claude Code Settings Most Developers Never Touch (And Why They Should).md
content_status: substantive-verbatim
tags: [claude-code, settings, configuration, claude-code-overhead-patterns, hooks, permissions]
---

# zodchiii — 15 Claude Code settings most developers never touch

> Technical Claude Code configuration tour by [[wiki/entities/zodchiii|zodchiii (darkzodchi)]] — distinct from his earlier ethically-flagged Teamly content-marketing thread. Opens with a load-bearing claim worth verifying: *"Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026 — Boris Cherny confirmed this on Hacker News."* Whether or not the specific timeline is accurate, the post lands a *one-minute setup* (4 lines in shell config + permissions in settings.json) that materially changes Claude Code behavior, and surfaces specific overhead patterns that compose with [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 9 overhead patterns]].

## TL;DR

15 settings grouped by purpose:

- **Effort/thinking (1-2)**: `CLAUDE_CODE_DEFAULT_EFFORT=high` + `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` to override the March 2026 default downshift.
- **Permissions (3-4)**: 6 permission modes (default / acceptEdits / plan / auto / dontAsk / bypassPermissions) + explicit allow/deny rules covering `.env`, `.ssh`, `.aws`, `rm -rf`, `sudo`, `git push`.
- **Model selection (5)**: `/model sonnet|opus|haiku` per turn. Sonnet for 80% of tasks; Opus 5× more expensive than Sonnet for simple questions.
- **Memory and compaction (6-7)**: custom `/compact` instructions + `/memory` for persistent project conventions at `~/.claude/projects/<project>/memory/`.
- **Hooks (8-9)**: `PostToolUse` for auto-formatting (prettier on `Write(*.ts)`); `PreToolUse` for log preprocessing (grep ERROR/WARN before Claude reads 10K-line logs).
- **Workflow isolation (10-11)**: `claude -w` for git worktree per session; `claude --bare` to skip config search for quick questions.
- **Cost control (12)**: `claude -p "..." --max-budget-usd 5.00` to cap headless CI/CD agents.
- **Observability (13)**: `showThinkingSummaries: true` to see full chain-of-thought instead of UI-redacted summaries.
- **Subagent control (14)**: explicit count in prompt ("Spawn exactly 3 subagents…") + budget cap.
- **MCP cost (15)**: `/mcp` to inspect connected servers and tool counts. *"MCP servers load 18K+ tokens per turn per server. 5+ servers = 90K tokens of overhead before your first prompt."*

The "one-minute setup" closer:

```bash
export CLAUDE_CODE_DEFAULT_EFFORT=high
export CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1
```

Plus `permissions.allow`/`deny` blocks and `PostToolUse` hooks in `settings.json`.

## Key takeaways

### The March 2026 default-effort downshift (load-bearing claim, unverified by us)

zodchiii's headline: *"Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026. Most people noticed Claude 'getting worse' but blamed the model. It wasn't the model. It was two default settings that changed without announcement."*

Cited evidence: Boris Cherny on Hacker News. Not independently verified in this wiki. **Treat as a directional signal**: regardless of the exact provenance, the env-var overrides exist and the fix is concrete. Worth flagging for the [[wiki/sources/trq212-x-html-effectiveness|Thariq Shihipar]] entity / wider Anthropic-internals lookup if it ever becomes load-bearing for a recommendation.

### Specific overhead numbers to absorb

zodchiii cites *"MCP servers load 18K+ tokens per turn per server"* — significantly higher than [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax's 600-token average]]. The discrepancy is probably PostgreSQL-MCP-tier servers (Mnilax cited 1,200 tokens for that one specifically). zodchiii rounds up; Mnilax instruments precisely. Both motivate the same action: trim MCP server count.

### Permission modes (worth promoting to schema)

The 6 named permission modes deserve a sub-pattern note in the wiki:

| Mode | When to use |
|---|---|
| `default` | New repos; max safety; high prompt-fatigue |
| `acceptEdits` | Repos you trust; remove confirmation cycle |
| `plan` | Unfamiliar codebases; review before action |
| `auto` | Headless CI; combine with `--max-budget-usd` |
| `dontAsk` | Specific session; aggressive |
| `bypassPermissions` | Sandboxed worktree only; never on main |

Switch mid-session with **Shift+Tab**. Aligns with [[claude-code-overhead-patterns]] — the *"47 confirmation prompts in a single morning"* one developer counted is exactly the friction overhead `acceptEdits` removes.

### Hook examples worth lifting

The PreToolUse log-grepping hook is the strongest single pattern:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash(cat *log*)",
      "hooks": [{"type": "command", "command": "grep -n 'ERROR\\|WARN' $file | head -50"}]
    }]
  }
}
```

Claude sees 50 relevant lines instead of 10,000. Direct application of [[wiki/concepts/claude-code-hooks|hooks]] for cost control. Worth absorbing into a concept-page sub-section.

### Parallel subagent caps

*"Specify agent count explicitly in your prompt: 'Spawn exactly 3 subagents: one for style review, one for bug detection, one for security scan. No more.'"* Pairs with [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_'s]] 5-role specialization at architectural scale (where the 5-agent count is a *design constraint*, not a runtime cap). Same instinct: bound the fan-out explicitly.

## Notable quotes

> "Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026." *(load-bearing; unverified)*

> "MCP servers load 18K+ tokens per turn per server. Most projects connect 5+ servers. That's 90K tokens of overhead before your first prompt."

> "Two environment variables + one config file. That's the difference between Claude Code working against you and working for you."

## How this composes with the wiki

- [[wiki/concepts/claude-code-overhead-patterns]] — 15 settings is operational counterpart to Mnilax's diagnostic 9 patterns. The Mnilax post says *what's wasted*; zodchiii says *what to set to fix it*. Read together.
- [[wiki/concepts/claude-code-hooks]] — PostToolUse + PreToolUse examples are the most actionable hook-cookbook entries in the wiki so far.
- [[wiki/concepts/mcp-server]] — adds a *third* token-cost data point (18K+ per server in zodchiii's estimate vs Mnilax's 600-1,200 per server), strengthening the "trim MCP servers" canon.
- [[wiki/sources/zodchiii-x-2052368125480354000]] — sibling post by same author. Different domain (Teamly content-marketing thread; ethical_flag) vs this technical configuration tour. **Author's range is now substantively wider in the wiki.**

## Mentioned entities

- [[wiki/entities/claude-code]] — primary subject.
- [[wiki/entities/anthropic]] — vendor; subject of the "silently lowered effort" claim.
- [[wiki/entities/zodchiii]] — author.
- [[wiki/entities/boris-cherny]] — *(stub candidate)* Anthropic Claude Code engineer cited as confirmation source on Hacker News.

## Related concepts

- [[claude-code-overhead-patterns]] — operational fix-list for Mnilax's diagnostic patterns.
- [[claude-code-hooks]] — concrete PostToolUse + PreToolUse examples.
- [[mcp-server]] — adds 18K-tokens-per-server cost figure.
- [[reasoning-execution-split]] — `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` forces fixed reasoning budget per turn.
- [[subagents]] — explicit count constraint pattern.

## Related sources

- [[wiki/sources/zodchiii-x-2052368125480354000]] — same author, different domain (Teamly content-marketing).
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — diagnostic counterpart; same overhead concerns.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — operational layered version with similar markdown-cheap-API-docs-expensive instinct.
