---
title: "15 Claude Code Settings Most Developers Never Touch (And Why They Should)"
source: "https://x.com/zodchiii/status/2053042131111927976"
author:
  - "[[@zodchiii]]"
published: 2026-05-09
created: 2026-05-09
description: "Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026. Most people noticed Claude \"getting worse\" but b..."
tags:
  - "claude"
---
![Image](https://pbs.twimg.com/media/HH3WFy6X0AkUnY1?format=jpg&name=large)

Anthropic silently lowered Claude Code's thinking effort from high to medium in March 2026.

Most people noticed Claude "getting worse" but blamed the model. It wasn't the model. It was two default settings that changed without announcement.

These are just 2 of 15 settings most developers have never touched. Save the full list to be ahead of everyone 👇

Before we dive in, I share daily notes on AI & vibe coding in my Telegram channel: [https://t.me/zodchixquant](https://t.me/zodchixquant)🧠

![Image](https://pbs.twimg.com/media/HH3SyKfWwAISvSH?format=jpg&name=large)

## 1\. Effort level (the biggest one)

**Problem:** Default effort was lowered from high to medium in March 2026. Claude thinks less, writes worse code, makes fewer tool calls, adds fewer comments.

**Fix:**

```text
/effort high
```

Or permanently in your shell config:

```text
export CLAUDE_CODE_DEFAULT_EFFORT=high
```

Boris Cherny confirmed this on Hacker News. For serious coding work, high or max restores the pre-February quality.

## 2\. Adaptive thinking

**Problem:** Since February 2026, Claude autonomously decides how much to reason per turn. On "easy" tasks it barely thinks, even when thinking would catch bugs.

**Fix:**

```text
export CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1
```

Forces a fixed reasoning budget every turn instead of letting Claude skip thinking on tasks it considers simple.

## 3\. Default permission mode

**Problem:** default mode asks permission for nearly every tool call. One developer counted 47 confirmation prompts in a single morning.

**Fix:** In settings.json:

```json
{
  "permissions": {
    "defaultMode": "acceptEdits"
  }
}
```

Six modes exist: **default**, **acceptEdits**, **plan**, **auto**, **dontAsk**, **bypassPermissions**. Use **acceptEdits** for projects you know. Use plan for unfamiliar repos. Switch mid-session with **Shift+Tab**.

## 4\. Allow/deny rules

**Problem:** Without allow rules, Claude asks permission for npm install, git commit, running tests. Without deny rules, Claude can read .env and .ssh.

**Fix:**

```json
{
  "permissions": {
    "allow": [
      "Read", "Glob", "Grep", "LS", "Edit",
      "Bash(npm run *)", "Bash(git status)", "Bash(git diff *)",
      "Bash(git add *)", "Bash(git commit *)"
    ],
    "deny": [
      "Read(**/.env*)", "Read(**/.ssh/**)", "Read(**/.aws/**)",
      "Bash(rm -rf *)", "Bash(sudo *)", "Bash(git push *)"
    ]
  }
}
```

## 5\. Model switching

**Problem:** Most people use one model for everything. Opus for simple questions costs 5x more than Sonnet.

**Fix:**

```text
/model sonnet     → daily coding, reviews, tests
/model opus       → complex refactors, architecture
/model haiku      → quick questions, formatting
```

Switch mid-session. No need to restart. Use Sonnet for 80% of tasks.

## 6\. Compact with custom instructions

**Problem:** Default /**compact** summarizes your conversation generically. Important context gets lost.

**Fix:**

```text
/compact preserve all architecture decisions, file paths mentioned, and error messages
```

Custom instructions tell Claude what to keep when summarizing. Your project-specific context survives compaction.

## 7\. Memory

**Problem:** Claude forgets learned patterns between sessions. You re-explain the same project conventions every time.

**Fix:**

```text
/memory
```

Check what Claude has auto-learned. Add entries manually:

```text
/memory add "this project uses pnpm, not npm"
/memory add "auth logic is in src/lib/auth/, never put it in components"
```

Persists at **~/.claude/projects/<project>/memory/.**

## 8\. Hooks for auto-formatting

**Problem:** Claude writes code, you manually run prettier, then continue. Every edit cycle includes a manual formatting step.

**Fix:** In settings.json:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write(*.ts)",
        "hooks": [{ "type": "command", "command": "npx prettier --write $file" }]
      }
    ]
  }
}
```

Every .ts file auto-formats after Claude writes it.

## 9\. Preprocessing hooks for logs

**Problem:** Claude reads a 10,000-line log file. Costs thousands of tokens. Most of it is noise.

**Fix:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash(cat *log*)",
        "hooks": [{ "type": "command", "command": "grep -n 'ERROR\\|WARN' $file | head -50" }]
      }
    ]
  }
}
```

Claude sees 50 relevant lines instead of 10,000.

## 10\. Git worktree isolation

**Problem:** Claude edits files in your working branch. One bad refactor and your uncommitted work is mixed with Claude's changes.

**Fix:**

```text
claude -w
```

Or check the worktree box in settings. Claude works in a separate git worktree. Your main branch stays untouched.

## 11\. Bare mode for speed

**Problem:** Claude Code loads all configs, reads CLAUDE.md, scans project on every startup. Takes seconds you don't need for quick questions.

**Fix:**

```text
claude --bare
```

Skips config search, loads minimally. Saves startup time when you start Claude Code dozens of times a day.

## 12\. Budget cap for automation

**Problem:** Headless Claude Code in CI/CD can loop indefinitely, burning tokens with nobody watching.

**Fix:**

```text
claude -p "refactor auth module" --max-budget-usd 5.00
```

Stops after $5 spent on that single task.

## 13\. Thinking summaries

**Problem:** The UI shows summarized thinking by default. You think Claude is reasoning less, but it might just be hidden.

**Fix:**

```text
{
  "showThinkingSummaries": true
}
```

Shows full thinking, not summaries. The UI redaction is cosmetic, but seeing the full chain helps you debug when Claude makes wrong decisions.

## 14\. Parallel subagent limits

**Problem:** Agent fan-out spawns too many subagents. 20+ parallel instances burning tokens on a simple task.

**Fix:** Specify agent count explicitly in your prompt:

```text
"Spawn exactly 3 subagents: one for style review, one for bug detection, one for security scan. No more."
```

Or use --max-budget-usd to cap total spend across all agents.

## 15\. MCP server tool counts

**Problem:** MCP servers load 18K+ tokens per turn per server. Most projects connect 5+ servers. That's 90K tokens of overhead before your first prompt.

**Fix:**

```text
/mcp
```

Check which servers are connected and how many tools each loads. Remove servers you're not actively using. Each removed server saves thousands of tokens per session.

## The one-minute setup

Copy these 4 lines into your shell config (.zshrc or .bashrc) and reload:

```text
export CLAUDE_CODE_DEFAULT_EFFORT=high
export CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1
```

Then update settings.json with permission rules and hooks from this article.

Two environment variables + one config file. That's the difference between Claude Code working against you and working for you.

Thanks for reading!

I share daily notes on AI, finance, and vibe coding in my Telegram channel: [https://t.me/zodchixquant](https://t.me/zodchixquant)

![Image](https://pbs.twimg.com/media/HH3V1SGXoAY0qZj?format=jpg&name=large)