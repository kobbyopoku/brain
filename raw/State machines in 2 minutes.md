---
title: "State machines in 2 minutes"
source: "https://x.com/DavidKPiano/status/2079209887158989231"
author:
  - "[[@DavidKPiano]]"
published: 2026-07-20
created: 2026-07-21
description: "First it was loops. Now it's graphs. Next month it'll be something else.Here's the thing: we're constantly rediscovering decades-old softwar..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "state-machines"
---
![Image](https://pbs.twimg.com/media/HNrWO-OWkAAe7mw?format=jpg&name=large)

First it was loops. Now it's graphs. Next month it'll be something else.

Here's the thing: we're constantly rediscovering decades-old software engineering patterns and repackaging them as innovations or whatever, instead of just applying what we've already known for a long time. Two patterns I keep seeing rediscovered over and over are the **actor model** and **state machines**. I already wrote a 2-minute explanation of the actor model ([https://x.com/DavidKPiano/status/2033132659795194367](https://x.com/DavidKPiano/status/2033132659795194367)), so now take 2 minutes to understand state machines, because that's really all you need (and what I've been talking about incessantly for 10+ years).

A state machine is very simple. It's a thing that answers one question:

> Given the current state, when an event occurs, what is the next state?

Or as a function:

> (state, event) → nextState

That's it. And that function describes every program, application, and algorithm ever written, because it's a fundamental truth of computer science: given some state, something happens that transitions it to the next state. We don't usually \*write\* our programs this way, but it's the underlying "physics" of how all code works, whether we realize it or not.

One thing I love about state machines is that you can visualize them. A finite state machine has a finite set of states and a finite set of events that cause transitions between those states. It's basically the same (state, event) → nextState function, just visualized as a graph: states are nodes, transitions are edges.

![Image](https://pbs.twimg.com/media/HNrRpuPWgAAxQ7A?format=jpg&name=large)

A simple state machine; if you can read words and follow arrows, you already know how to read it

Making this explicit gives you two guarantees for free:

1. You will always be in exactly one state\* (no more impossible states)
2. You can never transition anywhere except along a defined edge (no undefined behavior, by construction)

Ok, but what about loops and graphs?

Surprise... loops are graphs: directed, cyclic ones. A loop is also just about the most basic state machine there is: two states, "looping" and "done":

![Image](https://pbs.twimg.com/media/HNrSUsCXMAATeFe?format=jpg&name=large)

This is the silly thing you all hyped for weeks

And when we talk about "agent graphs," we're really describing how an agent moves through different "steps" to accomplish some task. But those steps aren't always sequential, and they aren't always acyclic either (sorry, DAG lovers): agents retry, backtrack, wait for humans, loop until verified. Map out an agent with realistically complex logic and it looks like this:

![Image](https://pbs.twimg.com/media/HNrTveHXsAA3J2M?format=jpg&name=large)

Contrived example, but you get the idea

That's a state machine. That's also a graph. **State machines are graphs.** The nodes and edges have precise meaning: which states exist (nodes), which events matter (edge labels), and where they lead (edges).

So loops, graphs, whatever comes next month: it's all the same underlying model. State machines and the actor model are the two concepts actually worth learning for building complex agent logic and multi-agent architectures. Nothing is new; don't fall for the hype. We're just reapplying well-known software patterns (and that's a very good thing IMO), just repackaged for whatever reason.

Also you don't need a library for this. A simple \`switch\` statement or an object/dict works in every programming language. But if you want to build more complex state machines and statecharts\*, I created XState to help you: [https://github.com/statelyai/xstate](https://github.com/statelyai/xstate)

Happy graphing! 🟡→🟢 \*I'll talk about statecharts in the next article. They bring state machines to the next level and make them much more useful to work with for complex logic, but are still technically state machines.