---
title: "Stanford and Anthropic discovered a system more powerful than any AI model."
source: "https://x.com/0xNoryxx/status/2078379404988743956"
author:
  - "[[@0xNoryxx]]"
published: 2026-07-18
created: 2026-07-21
description: "Right now you can take regular Claude or GPT and make it 10x more productive. Not through a better model. Not through a more expensive plan...."
tags:
  - "clippings"
  - "agentic-engineering"
  - "llm-research"
---
![Image](https://pbs.twimg.com/media/HNfhugQW0AAKde9?format=jpg&name=large)

Right now you can take regular Claude or GPT and make it 10x more productive. Not through a better model. Not through a more expensive plan. Through the right system around the model.

Stanford spent years researching this. Anthropic spent years building it in production. Both independently arrived at the same conclusion and published documents that most people will never read.

> Bookmark this and follow - I'm **Noryxx**, an Oxford student building AI systems and automation pipelines. I share projects, experiments, and practical ways to turn technology into real value. DMs open.

You're reading them now - as concrete principles you can apply today.

**Why the model stopped being the main question**

Until 2023 everyone argued about one thing: GPT-4 or Claude, OpenAI or Anthropic, which model is smarter.

That was the wrong question.

```text
2022  |  which model is smartest
2023  |  which prompt gives the best result
2024  |  what context to give the model
2025  |  how to build a pipeline around the model
2026  |  how to build a system that optimizes itself
```

Anthropic engineers now merge 8x more code per day than a year ago. Same model. Same team. Different system around the model.

Here's what that system looks like.

**Document 1 - DSPy**

Stanford NLP Group, October 2023.

> [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

> [arxiv.org/abs/2310.03714](https://arxiv.org/abs/2310.03714)

![Image](https://pbs.twimg.com/media/HNfh_nWXsAAX4jc?format=jpg&name=large)

The most important paper of the last few years that most developers never read.

The core idea: the developer no longer writes prompts. They program a system.

```text
Without DSPy:
Question → Prompt → Model → Answer
developer guesses which prompt will work

With DSPy:
Question
↓
Retriever      - finds relevant information
↓
Reasoning      - processes and analyzes
↓
Verifier       - checks the result
↓
Answer
```

The model becomes one node in an execution graph. Not the center - a component. The same way a database is a component of a web app and not the app itself.

The most important part of DSPy is the compiler. It automatically optimizes the entire pipeline toward a metric you define. You say what you want to get and how to measure quality. The compiler finds the best instructions and sequence of steps on its own.

```text
Task definition
↓
Metric
↓
DSPy Compiler
↓
Optimized Pipeline
↓
Better result than any human would write manually
```

The prompt is no longer written by hand. An algorithm optimizes it. This is one of the core reasons why the same model gives dramatically better results inside the right system.

**Document 2 - STORM**

Stanford OVAL Group, February 2024.

[github.com/stanford-oval/storm](https://github.com/stanford-oval/storm) [arxiv.org/abs/2402.14207](https://arxiv.org/abs/2402.14207)

STORM demonstrates something most people miss: even a "simple" task like writing an article becomes dramatically better when broken into a system.

```text
Single prompt:
Question → Model → Article
average quality, no source verification

STORM:
Question
↓
Research         - agent investigates the topic
↓
Source Collection - gathers real sources
↓
Outline          - builds structure
↓
Writing          - writes section by section
↓
Verification     - checks facts
↓
Revision         - corrects and improves
↓
Final Article
```

Same model. Completely different result. Because it's a system not a prompt.

STORM looks more like a newsroom than a chatbot. Every step has a role. Every step checks the previous one. This is exactly how serious AI systems should be built for any complex task.

**Document 3 - MIPRO**

Stanford, June 2024.

[arxiv.org/abs/2406.11695](https://arxiv.org/abs/2406.11695)

![Image](https://pbs.twimg.com/media/HNfiM-LXcAAsdV1?format=jpg&name=large)

If DSPy optimizes the pipeline - MIPRO optimizes the instructions themselves.

The core idea: the prompt stops being a static object someone wrote once. It becomes a variable the system optimizes automatically.

```text
Task
↓
Evaluation     - measures current result
↓
Optimization   - algorithm generates new instructions
↓
New Prompt     - better than any human would write
↓
Better Result
```

Instead of you spending hours rewriting prompts after every mistake - the system does it itself. Automatically. The result: instructions that no human prompt engineer would write manually because the algorithm finds patterns humans miss.

**Document 4 - GEPA**

Stanford DSPy Research, July 2026.

[arxiv.org/abs/2507.19457](https://arxiv.org/abs/2507.19457)

The newest paper on this list and the most radical.

GEPA - Reflective Prompt Evolution. A system that reflects on its own results and improves the next run. Without reinforcement learning. Without fine-tuning. Just reflection.

```text
Execute        - performs the task
↓
Reflect        - analyzes what went wrong and why
↓
Improve        - generates a better approach based on analysis
↓
Execute Again  - repeats with improved instructions
↓
Repeat
```

Result: a system that gets better with every run without any human intervention. GEPA is already part of the official DSPy research roadmap - this is not an experiment, this is the direction the entire field is moving.

**Document 5 - Claude Code**

Anthropic, 2025-2026.

[docs.claude.com](https://docs.claude.com/) [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook)

While Stanford built the theory - Anthropic built the same thing in production.

Claude Code does not work like a chat. It works like an engineering agent with a system of steps that looks exactly like a DSPy pipeline.

```text
Chatbot approach:
Question → Claude → Answer
one response, no memory, no verification

Claude Code approach:
Repository
↓
Documentation  - reads AGENTS.md, all docs
↓
Tool Use       - uses real tools
↓
Execution      - executes and observes the result
↓
Verification   - checks whether the result is correct
↓
Iteration      - repeats until the goal is reached
```

AGENTS.md in Claude Code = Skills in DSPy. Stored instructions the system reads automatically every session.

/goal in Claude Code = Verifier in DSPy. An objective condition that defines when the task is complete.

Subagents in Claude Code = Multi-module pipeline in DSPy. Specialized agents each doing one job better than one agent doing everything.

Stanford and Anthropic use different terminology. But they're building the same thing.

**Document 6 - MCP**

Anthropic, November 2024.

[github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)

Anthropic took a step Stanford hasn't taken at this scale - they released a protocol that connects AI systems to the real world.

```text
Before MCP:
LLM → separate integration for every tool
GitHub API separate. Slack API separate. Database separate.

With MCP:
LLM
↓
MCP Protocol
↓
Filesystem  |  GitHub  |  Slack  |  Database  |  Browser
```

The model is no longer isolated. It becomes the center of a system that has access to everything it needs for real work.

Practical result: an agent that doesn't just say "here is the fix" but opens the PR, links the ticket, pings Slack and updates the documentation - by itself, without a human in the chair.

**What Stanford and Anthropic figured out together**

```text
DSPy          |  model is a node in a graph, not the center
STORM         |  complex tasks need a system of steps
MIPRO         |  prompts are optimized by algorithm, not humans
GEPA          |  system reflects and improves itself
Claude Code   |  same principles in production
MCP           |  system connected to the real world
```

The shared conclusion both arrived at independently:

Competitive advantage in AI is no longer determined by which model you use. It's determined by how well the system around the model is designed - its pipeline, optimization, reflection, tools and connection to the real environment.

**Five principles that change the result**

```text
Principle 1  |  Model is a component, not a product
             |  Same way a database is a component of an app

Principle 2  |  Each step in the system has a separate role
             |  Research, Planning, Execution, Verification - separate

Principle 3  |  Verification is mandatory and objective
             |  The model cannot verify itself

Principle 4  |  The system optimizes itself in the process
             |  MIPRO, GEPA, /goal - all about this

Principle 5  |  The system is connected to the real world
             |  MCP, Tools, Connectors - not an isolated chat
```

**Bad AI system:**

```text
Question → Model → Answer
```

**Good AI system:**

```text
Question
↓
Retriever      - finds relevant context
↓
Planner        - breaks task into steps
↓
Executor       - executes with real tools
↓
Verifier       - checks result objectively
↓
Reflector      - analyzes mistakes, improves approach
↓
Answer
```

The difference between them is not the model. The difference is the architecture.

**Where to start today**

Day 1 - read the DSPy README at [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy). Understand the difference between prompting and programming a system. Create AGENTS.md for your project.

Day 2 - look at how STORM breaks tasks into steps. Apply the same logic to your most frequent task. Break it into Research, Planning, Execution, Verification.

Day 3 - set up Claude Code with the full stack. AGENTS.md, skills files, one subagent for review. Connect one MCP connector - GitHub if nothing else.

Day 4 - run your first /goal. Give the system a task with an objective completion condition. Watch it work while you do something else.

These four days will give you more than a year of rewriting prompts. Because you're building a system not searching for magic words.

Anthropic engineers merge 8x more code per day. Stanford researchers publish results that beat state-of-the-art without changing the model. Both use the same principles from opposite directions.

Most people will keep rewriting prompts and waiting for better models. A few will build the right system and stop depending on who releases the next GPT or Claude.

![Image](https://pbs.twimg.com/media/HNfi6AiXoAAcrRx?format=jpg&name=large)

/ If this was useful - bookmark this and follow