---
title: "Sumanth on X: \"Stop prompting AI agents. Design the loops that prompt them instead.This is the core idea behind Loop Engineering, a methodology for building automated systems that orchestrate your AI coding agents instead of prompting them manually.Boris Cherny, Head of Claude Code at https://t.co/Fun2VlgxF9\""
source: "https://x.com/Sumanth_077/status/2079207813038149772"
author:
published: 2026-07-18
created: 2026-07-21
description:
tags:
  - "clippings"
  - "agentic-engineering"
  - "loop-engineering"
---
## Post

## Conversation

Stop prompting AI agents. Design the loops that prompt them instead. This is the core idea behind Loop Engineering, a methodology for building automated systems that orchestrate your AI coding agents instead of prompting them manually. Boris Cherny, Head of Claude Code at Anthropic, puts it directly: "I don't prompt Claude anymore. I have loops running that prompt Claude and figure out what to do. My job is to write loops." A loop is an automated pipeline that runs on a schedule. It checks what needs to be done, prompts your AI coding agent with the right context, verifies the result, and either commits the fix or escalates to you. Then it runs again. This repo is a starter kit and reference guide for building these loops. Seven production-ready patterns, CLI tools to scaffold your setup, and documentation covering failure modes, anti-patterns, safety, and multi-loop coordination. The seven patterns: Daily Triage, PR Babysitter, CI Sweeper, Dependency Sweeper, Changelog Drafter, Post-Merge Cleanup, and Issue Triage. Each one ships with a starter kit, cadence recommendation, and token cost estimate. Three CLI tools handle setup. "loop-init" scaffolds skills, state, and budget files and prints your Loop Ready score. "loop-audit" checks how ready your setup is and suggests improvements. "loop-cost" estimates token spend before you run anything. Works with Claude Code, Codex, Grok, OpenCode, Cursor, and GitHub Actions. Key capabilities: • 7 production loop patterns with starters and token cost estimates • loop-init scaffolds your setup and prints a Loop Ready score • loop-audit scores readiness and suggests improvements • loop-cost estimates token spend per cadence • Failure modes, anti-patterns, and safety documentation included • Works with Claude Code, Codex, Grok, OpenCode, Cursor 100% open source. I've shared the link in the replies!

[![Image](https://pbs.twimg.com/media/HNrUcJWbQAAY2UO?format=jpg&name=medium)](https://x.com/Sumanth_077/status/2079207813038149772/photo/1)

Quote

Sumanth

@Sumanth\_077

Jul 18

Loop Engineering Clearly Explained

Stop prompting AI agents. Design the loops that prompt them instead! Boris Cherny, Head of Claude Code at Anthropic, puts it directly: "I don't prompt Claude anymore. I have loops running that prompt...

Post your reply

This changes how you think about working with AI agents[Sumanth](https://x.com/Sumanth_077)[@Sumanth\_077](https://x.com/Sumanth_077)

Yeah your job becomes writing the loop, not the prompt

We did it! El Salvadors favorite abuelitos dream came true

<video aria-label="Embedded video" controls=""><source type="video/mp4" src="blob:https://x.com/07c19158-b21a-444d-a5f6-e53b5c13ded0"></video> ![](https://pbs.twimg.com/amplify_video_thumb/1908190771791998978/img/GraQJGw7QqLM0qtn.jpg)[1.9M](https://x.com/MURPHSLIFE/status/1908190880344781312/analytics)