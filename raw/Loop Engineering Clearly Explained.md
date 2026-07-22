---
title: "Loop Engineering Clearly Explained"
source: "https://x.com/Sumanth_077/status/2078489959439437976"
author:
  - "[[@Sumanth_077]]"
published: 2026-07-18
created: 2026-07-21
description: "Stop prompting AI agents. Design the loops that prompt them instead!Boris Cherny, Head of Claude Code at Anthropic, puts it directly: \"I don..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "loop-engineering"
---
![Image](https://pbs.twimg.com/media/HNhHYNNbkAAJDLt?format=jpg&name=large)

Stop prompting AI agents. Design the loops that prompt them instead!

Boris Cherny, Head of Claude Code at Anthropic, puts it directly: "I don't prompt Claude anymore. I have loops running that prompt Claude and figure out what to do. My job is to write loops."

AI coding agents have always had the same workflow: write a prompt, read the output, prompt again to continue. You held the agent the entire time, one turn after another.

The problem is that you are the bottleneck. Every step depends on you showing up, reading the result, and deciding what happens next. The whole thing can only move as fast as you can sit there and run it.

Loop engineering is about changing that. Boris Cherny, the head of Claude Code, described the shift directly: he no longer prompts Claude. He has loops running that do the prompting and figure out what to do next. His job is to write those loops.

Peter Steinberger, the creator of OpenClaw also said the same thing independently: stop prompting your coding agent and start designing loops that prompt it for you.

So what does loop engineering actually mean in practice?

## How It Works

Loop engineering is the practice of replacing yourself as the person who prompts the agent. Instead of managing each turn manually, you build a small system that finds the work, hands it to the agent, checks what came back, and decides what happens next until the goal is met.

![Image](https://pbs.twimg.com/media/HNg__NCbMAA2p5_?format=jpg&name=large)

But before building one, it helps to understand what a loop is actually made of. A loop has five components and one memory layer. None of them are complicated on their own. The value comes from how they work together.

## The Five Building Blocks

Each one fills a specific role. Skip one and either the loop breaks, or you end up filling that gap yourself.

1\. Automations

Automations are what make a loop run on its own. You give it a prompt, a project, and a schedule. Every morning, every hour, whatever cadence fits. It runs, finds anything that needs attention, and surfaces it. Runs that find nothing archive themselves. Runs that find something come to you.

The more important detail is how the loop decides when it is done. In Claude Code for example, /goal keeps running until a condition you define is actually true, with a separate smaller model checking after each turn.

The agent doing the work is not the one deciding when to stop. You write something like "run until all tests in this folder pass and the linter is clean" and walk away. What you are really automating is the judgment about whether the work is finished, not just the work itself.

2\. Worktrees

The moment you run more than one agent at the same time, they start colliding. Two agents writing the same file is the same problem as two engineers committing to the same lines without talking first.

A git worktree gives each agent its own working directory on its own branch, while still sharing the same repo history. One agent's changes cannot reach another's files. Conflicts only surface at merge time, where standard git tooling can catch them, instead of happening silently during active work.

3\. Skills

Every session, the agent starts cold. It has no memory of your conventions, your build steps, or the decisions your team made last month. When it hits a gap, it guesses.

A skill is a folder with a SKILL.md file inside it. It holds your project knowledge in a place the agent reads on every run. Write it once. The agent stops guessing and starts working from what is actually true about your project.

4\. Plugins and Connectors

A loop that can only see the filesystem cannot do much on its own. Connectors, built on MCP, are what let the agent reach the tools your work actually lives in: your issue tracker, a database, a staging API, Slack.

The difference between an agent that hands you a fix and a loop that opens the PR, links the ticket, and posts in the team channel is connectors. Without them, the agent can only describe what it would do. It cannot finish what it started.

5\. Sub-agents

The most important structural decision in a loop is separating the agent that does the work from the agent that checks it. A model grading its own output tends to be generous and talks itself into "done" before it actually is.

A second agent, given different instructions and sometimes a different model, is told to assume the work is broken and find where. In Claude Code, /goal applies this same logic to the stopping condition. A separate model decides whether the loop is done, so the agent that did the work does not get to make that call.

**And the one thing that holds all of it together: memory.**

A loop with no memory resets completely between runs. The model forgets everything when the context window closes, so the next run has no idea what the last one tried, what passed, or what is still open.

A markdown file in the repo, a Linear board, a JSON file beside it, anything that lives outside the conversation and holds the current state solves this. The next run reads it at the start and picks up where the last one left off.

## What One Loop Looks Like

Say you want to wake up every morning to a clear picture of what broke overnight, with fixes already drafted and PRs ready for your review. Here is what a loop for that looks like when the five building blocks are wired together.

At 7am, an automation fires on your repo and kicks off this sequence:

1. A skill reads yesterday's failed tests, open issues, and recent commits
2. The findings get written into a memory file
3. For each issue worth addressing, the loop opens a separate worktree so agents can work in parallel without touching each other's files
4. One sub-agent drafts a fix per issue
5. A second sub-agent reviews each draft against your project skills and existing tests
6. If the fix passes, connectors open the pull request and update the linked ticket automatically
7. Anything too ambiguous to handle gets flagged and left in an inbox for you

By the time you sit down, the grunt work is done. You are reviewing, not triaging.

The memory file tracks what was tried, what passed, and what is still open. The next morning, the loop picks up exactly where it left off.

You designed that system once. Every step after that ran without you.

## Where to Start

The two main tools for loop engineering right now are Claude Code and OpenAI Codex. Both ship all five building blocks. If you are already using Claude Code, you have everything you need to build your first loop today.

Start with one task you already do repeatedly with an agent: a daily triage, a nightly test run, a recurring code review. Pick something low-stakes so the loop can make mistakes without it mattering.

Here is a practical first loop setup:

1. Create a .claude/skills/ folder in your repo and add a SKILL.md file with your project conventions: how tests are run, naming rules, anything the agent would otherwise guess wrong
2. Create a progress.md file at the root. This is your memory file. Every run should read it at the start and update it at the end
3. In Claude Code, run /goal "review open issues, identify the top three worth fixing, and write your findings to progress.md". This is your first loop: a defined goal with a verifiable stopping condition
4. Once you are comfortable with that, use /loop to run it on a schedule so it fires automatically without you triggering it

A few things to keep in mind before you scale up. Start read-only. Let the loop summarize and report for a few runs before you give it permission to open PRs or update tickets. Set a token budget before walking away from any unattended run. Add a verifier sub-agent once the loop is touching production code.

Direct prompting still works and still has its place. A loop is not a replacement for it. It is the right tool for work that is recurring, parallel, or needs to run while you are not there.

## Where It Goes Wrong

A loop changes what you do. It does not remove you from the picture. A few problems tend to surface once you start running one.

1. **Unattended mistakes.** A loop running without you is also making mistakes without you. Splitting the verifier from the maker makes the loop's judgment more trustworthy, but "done" is still a claim, not a proof. You still own what gets shipped.
2. **Comprehension debt.** The faster the loop writes code you did not write, the wider the gap between what exists in your codebase and what you actually understand. A smooth loop grows that gap quickly if you let it.
3. **Token costs.** An unattended loop spends tokens unattended. A loop with a tight stopping condition and a well-defined goal tends to be cheap because it finishes fast. A loose loop with a vague rubric can run for hours without you knowing. Set budget limits before you walk away.
4. **Designing the loop to avoid thinking.** Two developers can build the exact same loop and get completely different results. One uses it to move faster on work they understand well. The other uses it to avoid understanding the work at all. The loop has no way to tell the difference. You do.

## Final Thoughts

Prompting directly still works and still has its place. Loop engineering is not a replacement for it. What changed is where the hard work sits.

Designing a loop you can actually trust to run without you is a systems-engineering problem, not a writing one. It raises the ceiling on what you can get done, and raises your responsibility for what runs in your name.