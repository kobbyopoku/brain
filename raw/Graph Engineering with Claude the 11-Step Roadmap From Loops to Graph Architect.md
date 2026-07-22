---
title: "Graph Engineering with Claude: the 11-Step Roadmap From Loops to Graph Architect"
source: "https://x.com/0xRafy/status/2079542513317118268"
author:
  - "[[@0xRafy]]"
published: 2026-07-21
created: 2026-07-22
description: "Most people who try to build an AI agent end up with a single while-loop calling Claude with a growing prompt until it hits the context ceil..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "graph-engineering"
  - "claude-code"
---
![Image](https://pbs.twimg.com/media/HNv8MD0XgAAQ4Q4?format=jpg&name=large)

Most people who try to build an AI agent end up with a single while-loop calling Claude with a growing prompt until it hits the context ceiling and starts hallucinating. 9 out of 10 never split the work across specialized agents.

**They don't route.** **They don't branch.** **They don't parallelize.** They run one loop, pray it works, and debug it for weeks when it doesn't.

This is the 11-step roadmap that turns that single loop into a graph that fans out, verifies itself, and converges on a real output.

> Follow my Substack to get fresh AI alpha: [movez.substack.com](https://movez.substack.com/)

Loop engineering was a real step forward. Instead of prompting Claude once and copying the output, you built a system that retried, verified, and improved with each pass. That was era three.

![Image](https://pbs.twimg.com/media/HNwEgbtXcAAp0QA?format=jpg&name=large)

But a loop is still one agent doing one job. When the task gets complex, one loop drowns in context, mixes concerns, and tries to be everything at once. Graph engineering is the next layer: you design the flow.

Which agent runs. What happens when it fails. Where results go next. When a human steps in. This article is the complete playbook.

A loop is one agent getting smarter. A graph is many agents getting coordinated.

# 01\. Why one loop is not enough

A loop gives one agent autonomy. It retries, it learns from failures, it improves with each pass. For single-purpose tasks - fix this bug, summarize this doc, clean this dataset - a loop is all you need. You define the goal, attach a verifier, set a stop condition, and let it run.

![Image](https://pbs.twimg.com/media/HNv_dHMWYAAbWPn?format=jpg&name=large)

The problem starts when the task has **multiple concerns**. Research + analysis + code + review. One agent trying to do all four fills its context window with mixed information, loses track of earlier steps, and produces work that looks complete but falls apart under inspection.

The research bleeds into the analysis. The code ignores the review. The agent is doing four jobs and has the context budget of one.

This is not a model limitation. Sonnet and Opus are more than capable of each individual task. The limitation is **architectural**. You are asking one worker to be the researcher, the analyst, the builder, and the reviewer simultaneously, all in one conversation.

The fix is not a bigger context window. The fix is splitting the work across agents that each do one thing well, and wiring them together so the output of one becomes the input of the next.

![Image](https://pbs.twimg.com/media/HNv75B9XkAAPzzT?format=png&name=large)

> The shift from loop to graph is the same shift a solo developer makes when they join a team. One person doing everything is fast until the project gets complex. Then you need roles, handoffs, and reviews.

# 02\. The four building blocks

Every graph, no matter how complex, is assembled from four primitives. You do not need a framework. You need functions, a dictionary, and if-statements.

![Image](https://pbs.twimg.com/media/HNwDSV8XsAETBNN?format=jpg&name=large)

- **Node.** A function that does one thing. A Claude call, a tool execution, a database query, a file write. It takes state in and returns state out. The node does not know what came before it or what comes after. It only knows its own job.
- **Edge.** A connection between two nodes. "After Research, run Analysis." Edges can be unconditional (always) or conditional (only if state\["status"\] == "needs\_more\_data"). Conditional edges are how graphs make decisions.
- **Router.** A special node that inspects the current state and picks which path to take. It does not do work itself. It classifies the input and sends it to the right specialist. Think of it as a dispatcher, not a worker.
- **State.** A dictionary that flows through the entire graph. Every node reads from it and writes to it. State is the graph's memory. Without it, each node starts from scratch and the graph has no idea what already happened.

![Image](https://pbs.twimg.com/media/HNv8Ud_W4AAIqOg?format=png&name=large)

```python
# The entire graph abstraction in 20 lines

def node(func):
    """A node is just a function that takes state and returns state."""
    def wrapper(state):
        return func(state)
    return wrapper

def edge(state, next_node):
    """An edge passes state to the next node."""
    return next_node(state)

def router(state, condition, if_true, if_false):
    """A router picks a path based on state."""
    if condition(state):
        return if_true(state)
    return if_false(state)
```

# 03\. The four eras

Each era of AI engineering absorbed the one before it. Prompt engineering taught us to write good instructions. Context engineering taught us to feed the right data. Loop engineering taught us to build one autonomous agent.

Graph engineering teaches us to wire many agents into a coordinated system.

![Image](https://pbs.twimg.com/media/HNwAF6MWoAAf5zV?format=jpg&name=large)

Most people are still in era one or two. They write a prompt, maybe attach some context, and expect a single Claude call to do the whole job. The builders who are shipping real products right now are in era three or four. They are not writing better prompts. They are designing better flows.

![Image](https://pbs.twimg.com/media/HNv8hghWAAAhred?format=png&name=large)

# 04\. Pattern: Sequential chain

The simplest graph. Node A runs, passes its output to Node B, which passes to Node C. No branching, no routing. Most "AI pipelines" are this.

![Image](https://pbs.twimg.com/media/HNwAYrVXMAAbNxu?format=jpg&name=large)

Sequential works when every step always succeeds and the order never changes. Data extraction, format conversion, translate-then-summarize. The moment any step can fail or the path can vary, you need one of the other four patterns.

The biggest risk with sequential chains is **error propagation**. If Node A produces bad output, Node B builds on that bad output, and Node C builds on that. By the end, the error has compounded through three layers.

This is why even simple sequential graphs benefit from a verification node at the end.

```python
def run_sequential(task):
    state = {"task": task}
    state = research_node(state)     # reads task, writes research
    state = analyze_node(state)      # reads research, writes analysis
    state = write_node(state)        # reads analysis, writes report
    state = verify_node(state)       # reads report, writes passed/failed
    return state
```

# 05\. Pattern: Router

A router inspects the input and picks one of several paths. Not every node runs. The router selects the right specialist for the job. This is how you build a system that handles multiple types of tasks without loading every tool into one agent.

![Image](https://pbs.twimg.com/media/HNwAukjWwAAIYtT?format=png&name=large)

The key insight: **routing is a classification task, not a reasoning task.** You do not need Sonnet to decide whether a ticket is about billing or a bug. Haiku handles it in milliseconds for a fraction of the cost. Save the expensive model for the actual work inside the specialist.

Each specialist should have its own system prompt and its own tool set. A code agent needs run\_tests and write\_file. A research agent needs web\_search and read\_doc. Giving every agent every tool means wrong tool calls, wasted tokens, and confused output.

![Image](https://pbs.twimg.com/media/HNv822jXwAArsqj?format=png&name=large)

```python
def router(state):
    # Cheap model for classification
    category = call_claude(
        model="claude-haiku-4-5",
        system="Classify this task. One word: code, research, or writing.",
        prompt=state["task"]
    )
    routes = {
        "code": code_agent,       # own prompt, own tools
        "research": research_agent, # own prompt, own tools
        "writing": writing_agent,   # own prompt, own tools
    }
    agent = routes.get(category.strip(), research_agent)
    return agent(state)
```

> **Pro nuance:** if your router makes wrong calls, the fix is usually a better system prompt, not a bigger model.

> Write 5-6 real examples of each category into the router's prompt. Few-shot classification on Haiku outperforms zero-shot on Sonnet for routing tasks.

# 06\. Pattern: parallel fan-out

Multiple nodes run at the same time on the same input. A collector waits for all of them and merges the results. Three agents running in parallel means your total time is the time of the slowest agent, not the sum of all three.

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNwCtXoXwAAx0a0.jpg" src="https://video.twimg.com/tweet_video/HNwCtXoXwAAx0a0.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNwCtXoXwAAx0a0.jpg?name=large)

GIF

The constraint is independence. If Agent B needs Agent A's output, you cannot parallelize them. If both work on the same input and produce separate outputs, you can. Competitive analysis is the clean example: one agent per competitor, all running simultaneously, results merge at the end.

The merge node is where most people underinvest. Merging three JSON blobs is easy. Merging three research reports into a coherent synthesis requires its own prompt and its own quality bar. **Treat the merge node like a real agent, not a string concatenation.**

![Image](https://pbs.twimg.com/media/HNv9F9-WYAA3kOy?format=png&name=large)

```python
import asyncio

async def fan_out(task):
    results = await asyncio.gather(
        research_competitor(task, "Acme"),
        research_competitor(task, "Globex"),
        research_competitor(task, "Initech"),
    )
    # Merge is its own Claude call with a synthesis prompt
    merged = call_claude(
        system="Synthesize these 3 competitor reports into a comparison matrix.",
        prompt=json.dumps(results)
    )
    return merged
```

# 07\. Pattern: loop with gate

The builder agent does the work. A separate reviewer agent checks it. If the review fails, the builder retries with the failure reason appended to state. This is the pattern behind every self-correcting agent system.

![Image](https://pbs.twimg.com/media/HNwBMhZWUAAUxeA?format=png&name=large)

The critical rule: **the builder and the reviewer must be different agents.** Different system prompts, often different model tiers. The builder's job is to produce. The reviewer's job is to reject. If the same agent reviews its own work, it approves its own mistakes, because the same reasoning that produced the flaw is the same reasoning evaluating it.

The reviewer's prompt should be adversarial. Not "is this good?" but "find every flaw, inconsistency, and missing edge case. If you find nothing wrong, respond with {passed: true}. If you are unsure, fail it." A strict reviewer catches real bugs. A polite reviewer waves everything through.

![Image](https://pbs.twimg.com/media/HNv9QkFWoAIXhV9?format=png&name=large)

```python
def loop_with_gate(task, max_tries=5):
    state = {"task": task, "history": []}

    for i in range(max_tries):
        result = builder_agent(state)      # Sonnet, creative
        check = reviewer_agent(result)     # Sonnet, adversarial

        if check["passed"]:
            return result

        state["history"].append({
            "attempt": i + 1,
            "issues": check["issues"]
        })

    return {"status": "max_retries", "last_result": result}
```

# 08\. Pattern: human-in-the-loop

The graph pauses at a specific node and waits for human approval before continuing. The agent does the research and drafts the action. The human reviews the critical decision. The agent executes after approval.

![Image](https://pbs.twimg.com/media/HNwBapxXEAAAwlM?format=jpg&name=large)

This pattern is mandatory for anything expensive, irreversible, or high-stakes. Sending emails to customers, deploying to production, executing financial transactions, deleting data. The graph handles the work. The human handles the judgment call.

The approval node should show the human exactly what will happen and what it will cost. Not "do you approve?" but "this action will send 2,400 emails to the billing segment with this subject line and this body. Estimated cost: $12. Approve?"

Specific enough that the human can make a real decision in 5 seconds.

```python
def human_gate(state):
    # Show exactly what will happen
    print(f"Action: {state['action']}")
    print(f"Scope:  {state['scope']}")
    print(f"Cost:   {state['est_cost']}")

    approval = input("Approve? [y/n]: ")
    if approval == "y":
        state["approved"] = True
    else:
        state["approved"] = False
        state["human_feedback"] = input("Reason: ")
    return state
```

# 09\. State flow and model tiering

State is a flat dictionary that every node reads from and writes to. Keep it explicit: every node should declare what keys it reads and what keys it writes. When a graph breaks, the first thing you check is state. If you cannot trace which node wrote which key, you cannot debug anything.

![Image](https://pbs.twimg.com/media/HNwBs0nXEAAt9Ex?format=jpg&name=large)

Model tiering is the second production concern. Not every node needs the same model. A router classifies: Haiku. A builder reasons: Sonnet. A final quality gate on high-stakes output: Opus. Using Sonnet for routing is like hiring a senior engineer to sort mail. It works, but you are burning budget on the wrong task.

```python
# Match the model to the job
TIERS = {
    "router":    "claude-haiku-4-5",     # fast, cheap, classify
    "builder":   "claude-sonnet-4-6",    # reasoning, tools
    "reviewer":  "claude-sonnet-4-6",    # strict, adversarial
    "final_qa":  "claude-opus-4-6",     # highest bar, rare
}

# State contract for every node
# research_node:  reads ["task"]           writes ["research"]
# analysis_node:  reads ["research"]       writes ["analysis"]
# writer_node:    reads ["analysis"]       writes ["draft"]
# reviewer_node:  reads ["draft"]          writes ["review"]
```

# 10\. Fallback paths and error handling

The happy path works. Any unexpected error crashes the whole graph. Production graphs need a fallback edge for every node that can fail.

![Image](https://pbs.twimg.com/media/HNwCG9LXYAANdtO?format=jpg&name=large)

A fallback is not "ignore the error." It is a separate path in the graph that handles the failure gracefully. If the research agent times out, return a partial result and flag it. If the reviewer crashes, skip automatic review and route to human review. If the whole graph fails after max retries, save state to disk and send an alert. The user gets something useful instead of a stack trace.

![Image](https://pbs.twimg.com/media/HNv9wxJWkAAeTEj?format=png&name=large)

```python
def safe_node(func, state, fallback_key="error"):
    try:
        return func(state)
    except Exception as e:
        state[fallback_key] = str(e)
        state["needs_human"] = True
        return state

# In the graph
state = safe_node(research_node, state, "research_error")
if state.get("needs_human"):
    notify_human(state)
else:
    state = analyze_node(state)
```

# 11\. Full working example

Here is a complete graph that handles customer support tickets. It classifies the ticket with Haiku, routes to a specialist with Sonnet, the specialist drafts a response, a reviewer checks it, and if approved the response ships.

If rejected, the specialist retries with the reviewer's feedback. All five patterns in one graph.

```python
import anthropic, json

client = anthropic.Anthropic()

def classify(state):
    r = client.messages.create(
        model="claude-haiku-4-5", max_tokens=50,
        system="Classify: billing, technical, general. One word.",
        messages=[{"role": "user", "content": state["ticket"]}]
    )
    state["category"] = r.content[0].text.strip().lower()
    return state

def draft(state):
    prompts = {
        "billing": "Handle billing. Precise on refund policy.",
        "technical": "Handle tech. Ask for logs first.",
        "general": "Handle general inquiries. Brief.",
    }
    r = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=1024,
        system=prompts.get(state["category"], prompts["general"]),
        messages=[{"role": "user", "content": state["ticket"]}]
    )
    state["draft"] = r.content[0].text
    return state

def review(state):
    r = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=200,
        system="Find flaws in this support response. JSON: {\"passed\": bool, \"issues\": [str]}",
        messages=[{"role": "user", "content": state["draft"]}]
    )
    state["review"] = json.loads(r.content[0].text)
    return state

def run(ticket, max_retries=3):
    state = {"ticket": ticket, "attempts": 0}

    state = classify(state)          # Haiku router

    for _ in range(max_retries):
        state = draft(state)         # Sonnet specialist
        state = review(state)        # Sonnet reviewer
        state["attempts"] += 1

        if state["review"]["passed"]:
            send_response(state["draft"])
            return state

    # Fallback: max retries hit, route to human
    state["needs_human"] = True
    return state
```

Classify (Haiku) -> Route -> Draft (Sonnet) -> Review (Sonnet) -> Ship or retry. Fallback to human after max retries. Under 60 lines. No framework.

![Image](https://pbs.twimg.com/media/HNv-C5rWwAEFaul?format=png&name=large)

# 6 graphs to build with Claude this week

- **Ticket triage:** Claude classifies incoming tickets by category and urgency. **Routes each to a specialist agent** with domain-specific instructions. Reviewer checks before sending.
- **Competitive analysis:** Claude spawns one sub-agent per competitor. **All agents research in parallel.** A merge node synthesizes findings into a single report.
- **PR review pipeline:** Claude reads the diff, runs tests, writes review comments. **A second agent reviews the review** for false positives before posting.
- **Blog post pipeline:** Research agent gathers sources. Writer agent drafts. **Editor agent checks facts and tone.** Loop retries until editor passes.
- **ETL with validation:** Claude extracts data from PDFs, transforms schema, loads to database. **Validator agent samples rows** and flags anomalies before commit.
- **Incident response:** Alert triggers the graph. Claude reads logs, identifies root cause, **drafts a fix and a postmortem**. Human approves the fix before deploy.

# Five ways people break their first graph

- **× Giant monolith node.** One node doing everything. If it fails, everything fails. Break it into smaller nodes with single responsibilities.
- **×** **No state between nodes.** Each node starts from scratch. No shared dictionary, no context passed forward. The graph forgets what the previous node learned.
- **×** **No fallback path.** The happy path works. Any error crashes the whole graph. Always build a fallback edge.
- **×** **Sonnet for routing.** Routing is classification. Haiku does it faster and cheaper. Use Sonnet where it matters: building and reviewing.
- **×** **Skipping the gate.** No review node. The first wrong answer sent to a customer is the last time anyone trusts the system.

# Conclusion:

**A loop is an agent. A graph is a** **team****.**

Loop engineering was the breakthrough that turned prompting into building. You learned to make one agent that retries, verifies, and improves. That was a real skill. It still is.

But every team outperforms every solo operator once the work gets complex. A graph is how you build a team of agents: **a researcher who gathers, an analyst who reasons, a writer who drafts, a reviewer who rejects.** Each agent is simple. The graph makes them powerful.

The code in this article has no framework dependency. Functions, dictionaries, if-statements. That is a graph. You do not need LangGraph. You do not need CrewAI. You need to understand the five patterns and wire them together for your use case.

> Two kinds of builders in 2026. Ones still running one loop for everything. Ones designing the flow. The model is the same. The architecture is not.