---
title: "How to Use Your Claude Code Projects in Codex in 5 Mins"
source: "https://x.com/nateherk/status/2056456654015639567"
author:
  - "[[@nateherk]]"
published: 2026-05-18
created: 2026-05-21
description: "Run Claude Code and Codex in the Same ProjectA lot of people treat this like an either/or choice, but it's not.Lately I've been getting bail..."
tags:
  - "codex"
  - "claude"
  - "projects"
---
![Image](https://pbs.twimg.com/media/HIn_5gKXQAAdC5K?format=jpg&name=large)

Run Claude Code and Codex in the Same Project

A lot of people treat this like an either/or choice, but it's not.

Lately I've been getting bailed out by Codex pretty frequently. Claude Code would get stuck on the same error, burning through my tokens and my time. I'd hand the exact same project over to Codex with all the same files and context, and it'd fix it in seconds.

I'm not saying Codex is superior. I still do most of my work in Claude Code, but it's worth knowing how to run both.

## TL;DR

→ Both agents read from the same shared knowledge base. The setup difference is small.

→ Claude Code looks for CLAUDE.md and a .claude folder. Codex looks for AGENTS.md, a .codex folder, and a .agents folder.

→ Skills are markdown with YAML frontmatter in both tools. Same file, different folder.

→ Sub-agents are markdown in Claude Code and TOML in Codex. Same job, different file type.

→ Convert any project in one prompt by telling Codex to do it for you.

→ Once wired up, run both in separate terminals and hand off when one gets stuck.

![Image](https://pbs.twimg.com/media/HIoAA7QWAAErjTH?format=jpg&name=large)

## The Three Layers

Every coding agent project breaks down into three layers.

1️⃣ Shared knowledge → wiki, references, scripts, decisions, archives, brand assets, project files. Anything markdown. Any agent can read it. This layer never changes.

2️⃣ Workflows and skills → the prompts and reusable agents you've built. Same format, different folder per tool.

3️⃣ Tool-specific config → settings.json for Claude Code, config files for Codex. Small. Easy to mirror.

![Image](https://pbs.twimg.com/media/HIoAG8sXEAAAfVD?format=png&name=large)

The trick is recognizing that the first layer is huge and doesn't move. Most of what makes your project actually work sits there. The other two layers are the part you mirror.

## What Each Tool Actually Looks For

This is the whole reason people get confused.

Claude Code wants two things at the root of your project:

→ CLAUDE.md (your instructions file, like a system prompt)

→ .claude folder (config, settings, skills, agents)

Codex wants three:

→ AGENTS.md (same content as CLAUDE.md, different filename)

→ .codex folder (config and agents)

→ .agents folder (your skills)

Both tools also respect the global vs project-level split. You can have a user-level CLAUDE.md at ~/.claude that applies to every project, and a project-level one inside the repo. Codex works the same way.

## Skills Are Plug-and-Play

Here's what stood out when I first set this up.

Skills in Claude Code are markdown files with YAML frontmatter. Skills in Codex are markdown files with YAML frontmatter.

Same format. Same structure. The only thing different is which folder the tool checks. Claude Code looks in .claude/skills. Codex looks in .agents.

Drop the same file in both places. Both tools can run it. No rewrite, no translation.

## Sub-Agents Differ in Format Only

Sub-agents are where the formats actually diverge.

Claude Code uses markdown. Codex uses TOML.

Take my ClickUp searcher agent. In Claude Code it's a markdown file describing what it does, what model it runs on, what tools it can call. In Codex it's a TOML file describing the same things in different syntax. Same job. Different wrapper.

One caveat worth flagging. Codex sub-agents don't auto-invoke. You have to explicitly call them. In Claude Code, the model routes to sub-agents based on their description. In Codex, you call them by name.

## The Convert Prompt

You don't need to memorize any of this. The fastest way to convert a project is to just tell Codex to do it for you.

![Image](https://pbs.twimg.com/media/HIoARr3XAAAtnxZ?format=png&name=large)

"Hey, I built this project using Claude Code, but I need you Codex to be able to use it too. Create an AGENTS.md file using CLAUDE.md as inspiration. Set up a .codex config. Put all the skills in an .agents folder. Put all the agents in .codex. Research the Codex and Claude Code documentation and make sure everything important converts over.

That's the whole prompt. Codex will read your CLAUDE.md, mirror the structure, do its own documentation research, and set up the parallel files.

Maintenance after that is small. If you make a major change to CLAUDE.md, mirror it in AGENTS.md. If you build a new skill, the same file works in both places.

## Running Both at Once

Once you're wired up, both tools live in the same folder. I open one terminal and type "claude." I open another and type "codex." Same project, two agents, different terminals.

I actually built the HTML cheat sheet for this video using both at the same time. Had each one do its own research, then compare findings. Claude Code styled the page. Codex came in after and said "I kept Claude's dark design but restored the value that got lost in the styling pass." They were collaborating on the same file.

One warning. If both agents are working on the same file at the same time, they will overwrite each other. Coordinate which one owns which file.

I've also moved most of my work to the terminal over the VS Code extensions. Both tools have an extension, but typing "claude" or "codex" in a terminal inside the project is faster and keeps the workflow clean.

## The Session Handoff Move

Here's where it gets practical.

When Claude Code spirals on the same error, I run a skill I built called session-handoff. It summarizes what we've talked about, which files are active, what decisions we made, and what the next steps are.

I copy that summary, paste it into Codex, and keep going.

Sometimes Codex fixes in 10 seconds what Claude Code was looping on for ten minutes. Sometimes it's the other way around. The point is having both ready to go means a stuck session never has to stay stuck.

## Wrap

The point isn't that one tool is better than the other. The point is don't get locked into one ecosystem.

Yes, two subscriptions. But when Claude Code goes down for a day, you keep building at the same speed because Codex is already wired into the same project.

If you've mastered Claude Code, you've basically mastered Codex. The mental model is the same. The file names are different.

I walk through this step by step in the full video. Link in the first reply.