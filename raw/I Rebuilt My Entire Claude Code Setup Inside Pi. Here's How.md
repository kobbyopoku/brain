---
title: "I Rebuilt My Entire Claude Code Setup Inside Pi. Here's How"
source: "https://x.com/tomcrawshaw01/status/2079559394942206156"
author:
  - "[[@tomcrawshaw01]]"
published: 2026-07-21
created: 2026-07-22
description: "A full tutorial on harness engineering: what it is, why it matters more than the model, and exactly how to set up your own harness in Pi.Wha..."
tags:
  - "clippings"
  - "agent-tooling"
  - "claude-code"
---
![Image](https://pbs.twimg.com/media/HNpYJKub0AAmbaI?format=jpg&name=large)

A full tutorial on harness engineering: what it is, why it matters more than the model, and exactly how to set up your own harness in Pi.

## What is harness engineering?

Every AI agent is two parts. The model, which is the raw brain you rent from Anthropic, OpenAI, or Moonshot. And the harness, which is everything you build around it. Your instructions, your tools, your memory, your rules.

The shorthand the field has settled on:

**Agent = Model + Harness**

Harness engineering is the craft of configuring that second part on purpose, so a model's raw capability turns into reliable behaviour you can trust with real work. Same model, better harness, dramatically better output. That gap is where almost all of your leverage lives.

And if you use Claude Code, you've already been doing it. Your CLAUDE.md, your skills folder, your custom commands. That is a harness. You've been engineering it by instinct.

The reason this tutorial exists: for about a year my harness only ran on one model.

When I wanted to put Kimi K3 through real work, switching felt like tearing everything down. So I rebuilt the whole setup inside a coding agent called Pi, where the harness is just plain files you can see and edit.

This is the full setup, commands and all.

## Step one: install Pi and log in

```text
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
cd /path/to/your-project
pi
```

Then inside Pi:

/login

That one command covers almost everything you'll need. You can log in with your existing Claude Pro/Max subscription, a ChatGPT/Codex plan, GitHub Copilot, or OpenRouter, which is what I'm using to run Kimi K3.

Log in once and every model from that provider shows up in your list.

From then on, switching models is:

/model

That's the whole job. Ctrl+L does the same thing.

(If you ever want something exotic that isn't built in, like a local Ollama model, one JSON file at ~/.pi/agent/models.json adds it. Most people will never need to touch it.)

## Step two: let Pi port your Claude Code setup for you

This is the move that makes the whole thing take an afternoon instead of a week.

Don't rebuild anything by hand. Point Pi at your existing setup and ask it to copy itself over.

The actual prompt I used, more or less:

Review my entire Claude Code setup. My CLAUDE.md, my .claude/skills folder, my saved prompts and commands, my tool connections. Then write the equivalent configuration for yourself, optimised for how I actually work.

The agent set up the agent. It read my instruction files, moved my skills across, recreated my shortcuts, and wrote its own config.

I reviewed what it wrote, fixed the few things it got wrong, and I was running.

That's the moment harness engineering stops feeling like admin. Everything below is what it set up, so you know what to check and what to tweak.

## Step three: your context files

Every rule I'd written for Claude Code lived in a single CLAUDE.md. Pi reads CLAUDE.md and AGENTS.md directly, so months of tuning came across untouched.

Two layers worth knowing:

- ~/.pi/agent/AGENTS.md is global. It follows you into every project, so this is where rules about you and how you work go.
- AGENTS.md or CLAUDE.md in a project root is about that project only.

Change either file and run /reload to pick it up without restarting.

If you've spent any time teaching your current agent how you work, that work is portable. You just didn't know it yet.

## Step four: customise the system prompt (the thing Claude Code won't let you do)

This is Pi's killer feature, and it's worth stating plainly. Claude Code and Codex don't let you touch the system prompt. Pi hands you the whole thing.

The system prompt is the agent's standing behaviour, loaded before anything you type. Two files control it, in .pi/ per project or ~/.pi/agent/ globally:

- APPEND\_SYSTEM.md adds your rules on top of Pi's default. Safe, reversible, start here.
- SYSTEM.md replaces the default entirely. Powerful, and easy to break. The default is what makes Pi good at editing files and running commands, so don't replace it until you know what it does for you.

My advice: start with a few behaviour rules in APPEND\_SYSTEM.md and watch them show up in every session.

It's the difference between renovating a room and knocking the house down.

## Step five: skills and saved prompts

The easiest path here is the same as step two: tell Pi to grab your skills folder and move it over, or point it at the folder you already use and let it wire things up.

Pi uses the same skills standard as Claude Code, so mine came across with zero conversion.

For the prompts you type over and over, drop a markdown file into ~/.pi/agent/prompts/ and it becomes a slash command.

A file called daily-email.md means typing /daily-email fires that whole prompt in a keystroke.

## Step six: build the custom pieces your old harness never had

Because everything in Pi is a file, anything you can describe you can build. This is where harness engineering gets fun.

Example: I wanted the agent to learn as we work, the way tools like Hermes advertise auto-learning memory. So I built it myself in about ten minutes.

A memory file in the project, plus a saved prompt that tells the agent to review the session and append anything worth remembering to that file. Now the agent compounds.

Every session starts smarter than the last one started, and the memory is a markdown file I can read and edit myself.

That's the real point of this step. You're not limited to what the tool ships with.

If you can describe a behaviour, a memory system, a quality gate, a weekly review habit, you can make it part of the harness. Most of my custom pieces are one file and one saved prompt each.

## The day-to-day loop

Once it's set up, everything runs on a handful of commands.

Pick a model with /model and start. Mid-task, if you want a different brain, run /model again and carry on.

Cheap model for testing, strong model for the real work, same setup.

When a conversation gets long, my move is a handoff document. I ask Pi to write a summary of where we are, what we decided, and what's next, saved as a markdown file.

Then I run /new, start a fresh session, and point it at the handoff. Pi doesn't have a "clear" button, and honestly this is better. You get a written record of every long task for free.

And keep an eye on the footer. Pi shows live token count and session cost in real money (or run /session for the full breakdown).

When you can see the meter, you make cheaper choices without thinking about it.

## Why I'd use Pi over Claude Code

Concrete, no manifesto.

You control the system prompt. Claude Code and Codex lock it.

Pi lets you append to it or replace it, per project or globally, which means the agent's personality is yours to shape.

Every part of the harness is a file you own. Context, skills, prompts, model config.

Nothing is hidden behind a UI, so you can version it, back it up, and rebuild it anywhere.

And you can run any model behind your setup. Your files, your skills, your rules, pointed at Claude today, Kimi K3 tomorrow, whatever lands next month.

Worth saying clearly: you don't need a new subscription to do this. Your existing Claude Code subscription logs straight into Pi, so you can try everything in this article on the plan you already pay for.

Cheap model for testing, strong model for real work, no rebuild in between.

Models come and go. The harness you build around them is yours.

## The honest downsides

Pi has no built-in sandbox. It runs with your full permissions, the same as you sitting at your own machine.

That's fine when you trust what you're working on, but anything sitting in a project can try to steer the agent. If you run it on code you don't trust, put it inside a container first. Don't skip that.

It's also young and it moves fast. Things change week to week. If you want a tool that never surprises you, this isn't that yet.

And yes, it's do-it-yourself. Nobody hands you a finished harness. But step two in this article is the shortcut: you ask the agent to build it for you, and the whole thing takes an afternoon instead of a week.

One last honest one. A great harness makes a good model better. It can't make a weak model good. The floor is still the model, so pick a capable one.

## The model gets the headlines. The harness does the work.

If you build anything with AI agents, harness engineering is the skill I'd start on this year. Not prompt tricks. The setup around the model.

In 2026 the models change every few weeks. Something faster or cheaper lands, everyone scrambles, and the people who built a portable harness just swap the brain and keep going.

Save this if you want the map. I'm writing more of it.

The model gets the headlines. The harness does the work.