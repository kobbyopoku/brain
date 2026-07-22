---
title: "Wtf is graph engineering and why is it going viral?"
source: "https://x.com/LoopOnChain/status/2079227569598300273"
author:
  - "[[@LoopOnChain]]"
published: 2026-07-20
created: 2026-07-22
description: "By the end of this you'll actually understand what a \"graph\" is, why everyone on your timeline suddenly won't shut up about them, and you'll..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "graph-engineering"
---
![Image](https://pbs.twimg.com/media/HNhQ-blWAAEGIGO?format=jpg&name=large)

By the end of this you'll actually understand what a "graph" is, why everyone on your timeline suddenly won't shut up about them, and you'll have the code to build your first one, so stick around! Ok so here's what happened. Back in June, a guy named Peter Steinberger ([@steipete](https://x.com/@steipete), built OpenClaw, now at OpenAI, basically AI-agent famous) posted two sentences that did 8.4 million views:

> "Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."

And everyone lost it. Addy Osmani over at Google wrote a whole essay calling it "Loop Engineering" the same day. Boris Cherny, the guy who literally built Claude Code, said basically "I don't prompt Claude anymore, I have loops running, they're the ones prompting Claude." So for a month, LOOPS were the thing. Everyone was building loops. Then last night Peter posts this:

> "Are we still talking loops or did we shift to graphs yet?"

And now everyone's quietly panicking about graphs. **Here's the honest part: that tweet is half a joke.** He's poking fun at how fast our little corner of the internet sprints from one buzzword to the next. But he's also not wrong. Graphs really are the next step up. And almost nobody is explaining them in plain english, so you get this low background dread that you're already behind. You're not. This one is genuinely simple. Let me show you.

## First, what a loop even is.

A loop is the simplest possible agent. It goes: think, do something, look at what happened, think again. Over and over until the job's done. Reason, act, observe, repeat. You've felt this. It's Claude Code chugging away, running a command, reading the output, running the next one, until your feature is built. One agent, going in circles until it's finished. Loops are great. But they hit a ceiling. Because real work isn't one clean circle. Sometimes you need "if the tests pass, ship it, but if they fail, go fix them and come back." Sometimes you want three agents working at once and one boss agent pulling it together. Sometimes you need to stop and ask a human before doing something scary. A plain loop can't do that stuff cleanly. It all ends up buried in tangled if-statements inside your code that you can't actually see. That's where a graph comes in.

## What a graph actually is (the whole thing, in one picture)

Draw a flowchart. Boxes connected by arrows. That's a graph. Seriously, that's the whole concept. Except this flowchart runs. The boxes do real work, and the arrows decide what happens next. There are exactly 3 pieces. Get these 3 and you get graphs, forever: **1\. Nodes (the boxes).** A node is one unit of work. "Call the LLM." "Run this tool." "Search the web." Each box does its one job and nothing else. **2\. Edges (the arrows).** An arrow points from one box to the next and decides where the work goes. And here's the good part: an arrow can point BACKWARD. Box B can hand the work back to Box A. That's a loop. A loop is literally just a graph with an arrow that curls back on itself. Arrows can also split. "If this, go here. If that, go there." That's a conditional edge, and it's the agent making a decision about its own next move. That split is the thing loops couldn't do cleanly. **3\. State (the clipboard).** There's one shared clipboard every box reads from and writes to. The conversation so far, which tools got called, whatever matters. Each box picks up the clipboard, does its thing, writes down what it learned, passes it on. That's it. Boxes, arrows, clipboard. Nodes, edges, state. Ok Alex, so what's actually different from a loop? A loop IS a graph. The simplest one. One box that keeps handing the clipboard back to itself. "Graph engineering" is just the name for what you do when your agent gets complicated enough that one box isn't enough, so you start drawing the real boxes and arrows instead of cramming everything into a while-loop you can't read. Branching. Multiple agents. A human checkpoint in the middle. All of it visible, all of it something you can point at when it breaks. That's the whole shift. Loops said "stop being the thing that prompts." Graphs say "draw the map before the whole thing turns to spaghetti."

## How to build your first graph (today, for real)

The tool everyone uses is called LangGraph. It's free, it's got over 37,000 stars on GitHub, and your first graph is well under 50 lines of python. The classic first graph is the simplest useful agent there is: it thinks, and if it needs a tool it grabs one, then thinks again, until it's done. The famous "ReAct" pattern, except now you can see it as a graph instead of a black box. Here's the shape: • State: just the running list of messages. • Node 1, "reason": call the model. • The decision (conditional edge): did the model ask to use a tool? If yes, go to the tools node. If no, we're done. END. • Node 2, "tools": run whatever tool it asked for, then hand the clipboard back to "reason." That backward arrow from tools to reason? That's your loop. Living inside your graph. You just drew it instead of hiding it. The full copy-paste code is at the bottom. It runs. You'll have a working agent-graph in about ten minutes.

## The one honest catch.

You don't need a graph for everything. If your agent is genuinely just one loop doing one thing until it's done, a graph is overkill and you should just write the loop. Don't graph-engineer your grocery list because Twitter told you to. You reach for a graph the moment you catch yourself writing "ok but if THIS happens do THAT instead, unless the other thing, in which case go back and..." That tangle in your head is a graph asking to be drawn. So here's what I'd actually do: • Play with a plain loop first. Really get it. (If loops don't click yet, that's your homework before this.) • Then build the little graph below. Change one node. Add one arrow. Watch it route. • The moment a loop starts getting tangled, that's your signal to graduate. Loops taught us to stop being the thing in the middle. Graphs teach us to draw the map before the map draws itself. Go build one.

## Here's the version to steal

```plaintext
Help me build my first graph, by teaching me to become a graph engineer with this first project:

# Your first graph: a ReAct agent.
# It thinks, uses a tool if it needs one, thinks again, until it's done.
# pip install langgraph langchain-anthropic

from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool

# 1. STATE: the shared clipboard. Here it's just the running list of messages.
class State(TypedDict):
    messages: Annotated[list, add_messages]

# A tool the agent is allowed to reach for.
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tools = [multiply]
model = ChatAnthropic(model="claude-opus-4-8").bind_tools(tools)

# 2a. NODE "reason": call the model with everything so far.
def reason(state: State):
    return {"messages": [model.invoke(state["messages"])]}

# Build the graph.
graph = StateGraph(State)
graph.add_node("reason", reason)
graph.add_node("tools", ToolNode(tools))   # 2b. NODE "tools": runs whatever tool was asked for

# 3. EDGES (the arrows):
graph.add_edge(START, "reason")                          # start by reasoning
graph.add_conditional_edges("reason", tools_condition)   # tool asked? -> "tools", else -> END
graph.add_edge("tools", "reason")                        # the backward arrow = your loop

app = graph.compile()

# Run it.
for step in app.stream({"messages": [("user", "What's 12 times 7? Use your tool.")]}):
    print(step)
```

And if you don't want to read code, here's the prompt. Paste it into Claude and it'll build this WITH you and explain every line:

```plaintext
Build me my first LangGraph agent from scratch in Python. Use the three primitives: a State that holds the message list, a 'reason' node that calls the model, a conditional edge that routes to a 'tools' node if the model asked for a tool (otherwise END), and a 'tools' node that runs the tool and loops back to reason. Keep it under 50 lines, put a one-line plain-english comment on every node and edge so I understand each piece, then show me how I'd add a second tool and a human-approval checkpoint before a tool runs.
```

**Follow me for more of this. I take the AI stuff everyone's panicking about and turn it into things you can actually build, minus the hype.** If this made graphs finally click, hit like so it reaches the next person who's quietly confused. And send it to the one friend who keeps saying "graphs" in meetings and clearly doesn't know what they are. You know who. **The best way to support me is with a comment below!** ❤️