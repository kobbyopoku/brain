---
title: "How to Build an AI Agent with Claude Code (Full Guide)"
source: "https://x.com/0xJeyx/status/2074514494999417175"
author:
  - "[[@0xJeyx]]"
published: 2026-07-07
created: 2026-07-22
description: "You do not need Python or a developer setup. By the end of this guide you have a working team of agents that research, write, and ship for y..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HMonzW-XgAAM2Yd?format=jpg&name=large)

## You do not need Python or a developer setup. By the end of this guide you have a working team of agents that research, write, and ship for you, built in plain English.

> You hand Claude a goal, not a script. It plans the steps, runs them in order, checks its own work, and hands you a finished result. That is an agent, and you can build one today.

Most people are still prompting one thing at a time. Ask, copy the answer, ask the next one. Useful, and also the most limited way there is to work.

There is a level above that. You give Claude a real outcome and it plans the steps, runs them in order, checks itself, and delivers. That is an agent, and you can build one inside Claude Code without touching code.

You write plain English. No code, no framework docs, no terminal commands to memorize. The tutorials make agents feel developer-only. They are not.

This is the full guide. What an agent actually is, the one file that makes or breaks it, and two working agents you build today. One that researches. One that turns a single script into a week of content.

# Three levels, and most people never leave the first

There are three ways to work with Claude. Most people are stuck on level one without knowing the other two exist.

- **Level one is chat.** You ask, it answers. A definition, a summary, a quick explanation. Genuinely useful, and still the most limited way to use it.
- **Level two is builder mode.** You stop asking and start telling it to make things. Write this script. Draft this email. Analyze this document. Real output now, but you carry every step. You decide what comes next, you review each piece, you move the project forward by hand.
- **Level three is agentic.** You hand over the goal and it figures out how to get there. It breaks the work into phases, asks when something is unclear, runs each phase in order, reviews itself, and delivers. You set the destination. The agent drives.

Almost everything people call an "AI workflow" is level two wearing a level-three costume. The gap between them is the whole subject of this guide.

![Image](https://pbs.twimg.com/media/HMogIFHWgAEh_1V?format=jpg&name=large)

Chat to builder to agent. The jump that matters is the last one.

# What actually makes it an agent

Not every Claude conversation is an agent. A long prompt is still a prompt. Three things separate a real agent from a fancy autocomplete.

**It follows a process, not a reply.** A chatbot gives one answer per message. An agent moves through stages. It gathers context, forms a plan, executes step by step, checks the output, and adjusts when something is off.

**It decides under uncertainty.** A chatbot guesses when it does not understand you. An agent stops and asks, then adapts based on what it finds instead of charging ahead on a bad assumption.

**It clarifies before it acts.** Most bad AI output comes from the model guessing your audience, format, scope, or tone. A well-built agent treats your first request as the start of a short conversation, not a full spec to run this second. That one habit is where most of the quality lives.

![Image](https://pbs.twimg.com/media/HMoglndXQAAURLG?format=jpg&name=large)

Three tests. If it does not do these, it is a prompt wearing a costume.

# Every agent is four pieces

Strip away the jargon and every agent is built from four parts. That is the whole model.

**Role.** One specific job, not "an AI that does stuff." A research agent finds and organizes. A writer turns ideas into drafts. The narrower the role, the better it performs.

**Instructions.** How it does the job. Not "research this topic" but "find five sources, summarize each in three sentences, flag the contradictions, end with your recommendation." Instructions carry the process, the standard, and the output format.

**Tools.** What it can touch. Search the web, read your files, organize folders, write documents. Tools decide what it can actually do beyond generating text.

**Memory.** What it remembers. Past work, your preferences, yesterday's decisions. Memory is what turns a one-time tool into a standing assistant.

Role, instructions, tools, memory. Get these four right and the rest is detail.

![Image](https://pbs.twimg.com/media/HMoguzKWQAA3PgC?format=jpg&name=large)

Role, instructions, tools, memory. Every agent you will ever build is these four.

# The one file that runs everything

Open the Claude desktop app and go to the code workspace. Create a project folder and name it anything. That folder is your agent's office. Everything it makes, organizes, and references lives there.

Then create the most important file in the whole setup. It is called **CLAUDE.md**. Most people skip it, launch an elaborate workflow with no context about who they are or how they work, then wonder why the output feels generic. The workflow was never the problem. The missing context was.

You do not open a text editor. You type create a file called CLAUDE.md in the root of this project and Claude spins it up. Then you fill it in. It is plain markdown, and Claude reads it automatically every time it starts working in that project. Think of it as an onboarding doc you write once and it reads every session.

```text
## Project context
This workspace is for AI-assisted research, content, and workflow automation.
Outputs are for a non-technical audience that wants practical, actionable info.

## About me
I create practical AI content for everyday users.
I prefer concise, direct explanations over academic or jargon-heavy language.
Every output should read like advice from a knowledgeable friend, not a corporate report.

## Rules
- Ask at least three clarifying questions before starting any complex task.
- Always show your plan before you execute it.
- Keep every output at or under the requested length. Never pad.
- Save files with lowercase, hyphenated names.

## Folders
- /workflows for instruction files
- /output for finished work
- /resources for reference material
```

Once you save it, Claude stops working from scratch every session. It has context, rules, and a structure to operate in. That one file done well beats most of the prompt-engineering tricks you will find online.

![Image](https://pbs.twimg.com/media/HMog3YfXYAAFDtc?format=jpg&name=large)

One file. Context, who you are, your rules. Read on every session automatically.

# Planning mode: never let it run blind

One habit makes or breaks agent work. You never let the agent execute immediately.

When an agent starts running on its own, it commits. It creates files, structures content, makes assumptions. If any of those early assumptions are wrong, and they are wrong more often than you would expect, you are cleaning up a half-finished project instead of steering a clean one.

Planning mode means you ask Claude to show the plan before it touches anything. How it read your goal. The steps it will take. The files it will create. The questions it still has. The review takes maybe two minutes and routinely saves ten minutes of cleanup.

Bake it in with one line in your CLAUDE.md rules: always present a written plan and wait for approval before starting any multi-step task. After that, Claude shows its thinking before it acts by default. You review, you adjust, you approve, then it runs.

![Image](https://pbs.twimg.com/media/HMog-DLWUAAXvUE?format=jpg&name=large)

Plan, review, approve, execute. Two minutes up front, ten minutes saved.

# The architecture underneath

Understanding the structure makes you better at designing your own. Most agent systems have three components.

**The workflow file.** A markdown document that describes the whole process for one type of task. The goal, the steps, the rules, the output format, what to do when something breaks. A standard operating procedure written in plain English. No code.

**The agent.** Claude itself. It reads the workflow file, understands the objective, and coordinates. It decides what to do at each step, when to proceed, and when to pause for input. A project manager who read the SOP and is now running it.

**The tools.** What Claude can use inside the workspace. Reading and creating files, organizing folders, searching documents, editing text. For most workflows these built-in capabilities are more than enough. No external APIs required.

The most important component is the workflow file, not the tools. That runs counter to what most people expect. A well-designed workflow with basic tools beats a sloppy workflow with sophisticated integrations every time. The intelligence lives in the instructions, and instructions are something anyone can write.

![Image](https://pbs.twimg.com/media/HMohFbAXYAAsddQ?format=jpg&name=large)

Workflow file, agent, tools. The instructions carry the intelligence, not the tech.

# Your first agent: the research agent

Time to build something real. A system where you hand Claude a topic and it runs the whole research-and-report process start to finish.

Open a new conversation in the workspace. Do not give it a topic yet. Instead, describe the system you want to build.

```text
I want to design a research workflow.

When I give you a topic, first ask me clarifying questions
about scope, audience, and depth.

Then form a written plan and wait for my approval.

Once I approve, research the topic thoroughly, organize the
findings into clear sections, and save a structured report
to the /output folder.

Before we build this, show me your plan for the workflow itself.
```

Notice the move. You are not doing the task, you are designing the system that handles the task. That extra step turns a one-time answer into a workflow you run again and again with different topics.

Claude comes back with a structure. A clarification phase, a research phase split into subtopics, a synthesis step, a review before saving. Approve it and it writes the actual file, something like research-agent.md in your workflows folder. Open it and you are reading your agent's operating instructions in plain language, fully editable, reusable forever.

Now run it. New session, same workspace: run the research workflow on the current state of AI agents in 2026. What is working in practice, what is overhyped, where is it heading. If it is set up right, Claude does not start writing. It asks questions first. Answer them specifically. Then it plans, you approve, and it executes. It researches, synthesizes, writes, and saves the finished report to your output folder. You managed none of those steps. That moment is when it stops feeling like a chat and starts feeling like something that works for you.

And because the workspace holds context, refining is fast. Trim the executive summary to three points. It updates that section and leaves the rest alone.

![Image](https://pbs.twimg.com/media/HMohUGAXoAAAvUo?format=jpg&name=large)

One topic in. Clarify, plan, research, and a structured report saved for you.

# Your second agent: the repurposing machine

The research agent is useful. This one saves you time every single week. You feed it one long script and it returns three short scripts and a full social pack, each as a separate file, ready to publish.

You drop your main script in an input folder. You give one instruction. It reads the whole thing, picks the three strongest moments, and turns each into its own 60-second short with a fresh hook. Then it writes the social pack, an X thread, a LinkedIn post, an Instagram caption, and drops everything in the output folder.

```text
Role: you are a content repurposing specialist.
Input: a single long-form script in the /input folder.

Steps:
1. Read the script completely.
2. Identify three standalone moments that work as shorts.
3. Write each as a 60-second script with its own hook and payoff.
4. Draft platform posts (X thread, LinkedIn, Instagram caption)
   that match my voice.

Output: four markdown files saved to /output.
```

One prompt, and the files appear one after another. Three short scripts and a social pack from a single source in under two minutes. Point the output of your research agent at the input of this one and you no longer have two tools. You have a line.

![Image](https://pbs.twimg.com/media/HMohfBJX0AAkAjZ?format=jpg&name=large)

One script in. Three shorts and a full social pack out, in under two minutes.

# Five mistakes that kill agent builds

Most failures come from the same handful of mistakes. Skip the frustrating part.

**1\. Skipping CLAUDE.md.** Without it every session starts from zero, quality is inconsistent, and you spend more time fixing output than you save. Write the file before anything else.

**2\. Vague goals.** "Do some research on AI" gets you a Wikipedia article. "Research how non-technical marketers use AI agents for content, focus on tools with free tiers" gets you something you can use. The specificity of the goal sets the quality of the output, and it matters most here because the agent runs multiple steps off that one goal.

**3\. Skipping the plan review.** It feels like an extra step, so people let it run and fix things after. But a half-finished multi-stage workflow is far harder to correct than a plan. Two minutes up front, ten minutes saved.

**4\. Not requiring clarifying questions.** If the workflow does not tell Claude to ask, it will assume, and assumptions are where most mediocre output comes from. Build the clarification step into every workflow.

**5\. Building everything at once.** People get excited and start a research system, a content planner, a CRM flow, and an email responder in the same week. The result is five half-working systems nobody trusts. Start with one. Run it until it is reliable, then build the next.

![Image](https://pbs.twimg.com/media/HMohnNuXUAA8O52?format=jpg&name=large)

The five that catch almost everyone. Every one is avoidable.

## What to build next

Agent capability is not something you unlock all at once. You build it one reliable workflow at a time.

**Start with simple, self-contained tasks.** Clear input, clear output. A research report, a content outline, a document summary. Low stakes, fast feedback, cheap to get wrong.

**Then move to iterative workflows.** The agent produces a first draft and refines it across rounds on your feedback. Script writing and editing passes live here.

**The advanced level is multi-workflow systems,** where one workflow feeds the next. A research agent produces a findings report, and a content-planning agent reads that report and generates ideas from it. That is a real pipeline, and it is not as hard to build as it sounds once the individual workflows are solid.

![Image](https://pbs.twimg.com/media/HMohscSW4AEYM3I?format=jpg&name=large)

Simple task, then iterative, then a pipeline. One reliable layer at a time.

# The shift underneath it

The people winning with AI right now are not the smartest in the room. They stopped prompting one thing at a time and started building systems that run on their own.

Build one agent this week. Run it until it is boring. You set the goal, Claude writes the instructions, the workflow does the work. That is the whole model, and you will be operating on a different level inside a month. **Follow me** [@jeyxbt](https://x.com/@jeyxbt) **for more AI builds, workflows, and systems that actually ship. No fluff. Just what works.**

![Image](https://pbs.twimg.com/media/HMoiC2IWgAAxHBk?format=png&name=large)

Claude improvements