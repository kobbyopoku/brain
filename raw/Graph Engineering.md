---
title: "/Graph Engineering"
source: "https://x.com/humzaakhalid/status/2079532755499839772"
author:
  - "[[@humzaakhalid]]"
published: 2026-07-21
created: 2026-07-22
description: "On July 18, Peter Steinberger posted nine words.\"Are we still talking loops, or did we shift to graphs yet?\"Peter Steinberger @steipete·Jul ..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "graph-engineering"
---
![Image](https://pbs.twimg.com/media/HNv31qvaIAAgh-S?format=jpg&name=large)

On July 18, Peter Steinberger posted nine words.

"Are we still talking loops, or did we shift to graphs yet?"

> Jul 18
> 
> Are we still talking loops or did we shift to graphs yet?

**Over 2.7 million views.**

Within 72 hours, the timeline had a manifesto, a backlash, three eulogies for loop engineering, and someone predicting a 10,000-word slop article.

This isn't that article. Because here's what nobody said in those 72 hours.

Almost everyone who "switched to graphs" this week did not build a graph.

They built a straight line and drew boxes around it.

## The shape you're already running

Every improvement system is the same four moves

Strip any self-improving process down, and you find the same engine underneath. Pick something to control. Set a target. Measure the gap. Act to close it. Repeat.

That's a thermostat. Temperature, setpoint, difference, heat.

That's your agent. Reason, act, observe, reason again.

That's your weekly retro, your OKRs, your model training run, and the plan-do-check-act cycle they've been teaching in business schools for seventy years.

The loop earned its dominance honestly. You can teach it in one sentence. It's cheap to build. And almost anything you measure and iterate on gets better.

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNv66PZaIAAv3Pw.jpg" src="https://video.twimg.com/tweet_video/HNv66PZaIAAv3Pw.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNv66PZaIAAv3Pw.jpg?name=large)

GIF

At first.

That "at first" is where the support team lived for five months.

## A graph is two things and nothing else

**Nodes.** A unit of work. One agent, one bounded job, one input in, one output out.

**Edges.** A dependency. This node's output feeds that node's input.

That's the entire vocabulary. Everything else in this article is built from those two words. And one sentence will save you three weeks:

**An edge only exists when data actually moves across it.**

Take a real example. "Summarize this file and then check the weather."

There's no edge there. The weather doesn't consume the summary. Those are two independent jobs that your script chained together for no reason.

You typed "and then." Your code heard "wait."

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNv6h2hb0AARaBv.jpg" src="https://video.twimg.com/tweet_video/HNv6h2hb0AARaBv.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNv6h2hb0AARaBv.jpg?name=large)

GIF

## Your linear agent is already a graph. A bad one.

Write "do A, then B, then C, then D" and you've drawn a graph.

A single unbranching chain. One edge in, one edge out, all the way down. It runs correctly. It also runs slowly, and it's brutally fragile.

Because a chain has zero redundancy. If C stalls, D never happens. And A's finished work sits trapped upstream with nowhere to go. This is the shape most builders are actually running right now while telling people they've moved to graphs.

## Most of your arrows are fake

Open your agent. Look at every arrow in it.

Ask one question of each:

**Does the next step actually read the last step's output?**

If the answer is no, that arrow isn't real. You typed those steps in that order, and your code obeyed you.

Cut it.

Most chains have two or three fake arrows hiding in them. Cut those and the chain collapses into something wider, a few independent nodes that all run at once, feeding one node that needs them all.

That collapse is the entire unlock. Everything else in this article is a variation on it.

I watched a builder run this on a repo audit script last month. Nine steps, forty minutes, every night. Six of the nine arrows were fake. The nine steps were really three that mattered and six that were just sitting in a queue because that's the order he'd typed them.

Same script, four minutes.

He didn't add a framework. He deleted six waits.

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNv5ex5a8AAfZuV.jpg" src="https://video.twimg.com/tweet_video/HNv5ex5a8AAfZuV.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNv5ex5a8AAfZuV.jpg?name=large)

GIF

## The idea isn't new. The wiring got cheap.

Graph orchestration has been around. LangGraph, AutoGen, and Google ADK all predate the term by a year or more.

So what actually changed in **July?**

You can now describe an objective and have the model write the orchestration script itself. Plain code, spawning a coordinated fleet of subagents.

And the coordination costs zero model tokens. Because it's code, not a conversation.

That's the shift. Loops didn't die. The cost of wiring collapsed, and a cost collapse always reveals a shape that was too expensive to build before.

# PART TWO

## The patterns that actually pay

Every node needs a contract

A node you can't reason about is a node you can't parallelize. The fix is a contract. Bounded input. Bounded output. Exactly one job.

Input is whatever the node reads, passed in explicitly. Never assumed from a shared context window. Output is a defined shape. Validated. So the next node consumes it without guessing.

In practice that means a schema. Force the subagent to return structured data, and validate at the tool-call layer, so it retries on mismatch instead of handing you free text you have to parse and pray over.

This is the line between a node you can wire into a graph and a node that only works when a human squints at its output.

## The diamond is the only topology you need to memorize

Fan out. Fan in.

One node splits the job. Many nodes do the work in parallel. One node merges the results.

**Fan out → reduce → synthesize.**

Fan out for breadth. Reduce with plain code to compress it. Synthesize with a final agent to write the answer. That's a market scan. That's a dependency audit. That's a code review. That's a research report.

Swap the sources and the prompts. Same skeleton every time. Once you can see the diamond, you stop asking how to make your agent do more steps.

You start asking where the split is and where the merge is.

That second question is the one that scales.

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNv4yNKbIAAmVS5.jpg" src="https://video.twimg.com/tweet_video/HNv4yNKbIAAmVS5.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNv4yNKbIAAmVS5.jpg?name=large)

GIF

## Most of what you're paying for is plumbing

Here's a ridiculous amount of wasted money, and I see it constantly.

People spawn an agent to "combine the results."

If combining means flatten-and-dedupe, that's a flatMap and a Set. Deterministic. Instant. Free.

Save agents for judgment. Never for plumbing.

**A graph where every edge is an agent is a graph paying rent on its own wiring.**

## Barriers are where your speed goes to die

A barrier makes everything wait for the slowest node before the next stage starts.

Sometimes that's exactly right. A cross-set dedupe genuinely needs the whole set in one place. But most of the time you don't need a barrier. You need a pipeline, where each item streams through all the stages independently.

Item A can be sitting in stage three while item C is still in stage one. Fast items finish early instead of idling behind slow ones.

The smell test is brutal and simple. If you wrote parallel, then a transform, then parallel again, and that middle transform has no cross-item dependency, you built a barrier for nothing.

"It's cleaner code" is not a reason. "The stages feel separate" is not a reason.

Separate is not the same as synchronized.

<video preload="none" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/amplify_video_thumb/2079529762457006080/img/8Kj5YLNKRZKDozsB.jpg" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"><source type="video/mp4" src="blob:https://x.com/e70dc647-d783-47de-bd13-11845ac947ec"></video>

![](https://pbs.twimg.com/amplify_video_thumb/2079529762457006080/img/8Kj5YLNKRZKDozsB.jpg?name=large)

## Put a verifier on the edge

This is where people running graphs separate from people posting about graphs.

The leverage was never more agents. It's the structure you wrap around them to produce confidence. A verifier sits on the edge, before a result is allowed downstream. Its only job is to try to kill the finding.

Survives, it passes. Doesn't, it never reaches the answer.

Three patterns are worth having in your hands.

**Adversarial verify.** Spawn independent skeptics prompted to refute each finding. Keep it only if a majority survive.

**Perspective-diverse verify.** Give each verifier a distinct lens: correctness, security, does-it-reproduce. Diversity catches failure modes that identical checks never will.

**Judge panel.** Generate several attempts from different angles, score them with parallel judges, synthesize from the winner while grafting in the best of the runners-up.

Notice what all three share. They're structural. Not prompt tricks.

## Contain the failure

In a chain, failure cascades. C dies, D never runs, the whole thing halts at 3 am and you find out at 9.

In a graph, failure should die at its node.

A thunk that throws inside a parallel call should resolve to null, not reject the whole batch. Eight good agents still return while one bad one drops out. Then you filter the nulls.

**Design every fan-in to tolerate missing inputs rather than assume a full set.**

There's a subtler failure underneath that one. Nodes stepping on each other. Agents writing files in parallel collide. The fix is isolation: give each agent its own worktree, let it work in a sandbox, then merge cleanly.

But only reach for that when nodes actually write in parallel. It's a seatbelt for one topology, not a tax on every run.

## Cycles are fine. Cycles that don't converge are expensive.

Sometimes you don't know how big the job is until you're inside it.

Unknown-size discovery. A bug sweep where finding one bug reveals three more.

That needs a cycle. A controlled edge back to an earlier node.

The danger is obvious. A cycle that doesn't converge is an infinite loop spawning agents until your budget is gone. The pattern that converges is loop-until-dry. Keep spawning finders until a few consecutive rounds surface nothing new, then stop.

And here's the detail almost everyone gets wrong on the first attempt:

**Dedupe against everything seen, not just against confirmed results.**

Miss that, and rejected findings reappear every round. The loop never runs dry. And you've built a machine that pays real money to rediscover the same dead ends forever.

## Not every node deserves your best model

A graph makes something obvious that a single agent never could.

Some nodes are bounded and repetitive. Extract this field. Classify this ticket.

Some nodes carry the actual judgment. Synthesize the report. Adjudicate the finding. Run the boring nodes cheaply. Spend the expensive tokens where judgment actually lives.

By default, every subagent inherits your session model, so a wide fan-out bills entirely at your top tier. People discover this on the invoice.

Route the fan-out down. Keep the merge node up.

This is the lever that turns a token-hungry graph from expensive into economical without touching its shape.

# PART THREE

## The part nobody is saying

More loops is not the answer

Now go back to the support team.

Everything you just read would have saved them. Pair the resolution metric with a renewal metric. Add an audit loop. Add a meta-loop tuning the thresholds.

So picture a company that does all of it.

Paired metrics. Audit loops. Meta-loops. A genuinely beautiful graph, drawn by someone who understood every section above. And every single one of those loops consumes reports. The audit loop checks the operations numbers against the finance numbers. The finance numbers come from the same systems that operations feeds. The meta-loop tunes its thresholds using dashboards built on all of it.

Every loop watches another loop.

**And no loop touches the ground.**

That graph is circular. An elaborate network of mutual confirmation where everything is consistent and nothing is verified.

It fails the same way the single loop failed. Just later. More expensively. And with far more green lights on the way down.

The topology bought sophistication. It did not buy contact with reality.

## Your graph needs anchors

Some measurements in the network have to be the kind that can't be argued with.

Revenue that landed in the bank. Tests that actually executed. Customers who actually stayed. The physical count that matches or doesn't.

Some nodes have to be frozen. Rules the optimizing loops are never allowed to tune, precisely because they're the rules the optimizer would be most tempted to weaken.

The way a training loop must never see the held-out set. And one thing has to come from outside the graph entirely. The answer to what "better" means at the root.

**Loops optimize toward references.**

**Graphs manage and revise references.**

But the original judgment, which things are worth controlling at all, where the frozen rules sit, can't be generated by the machinery.

Because every loop in the graph already presumes it.

That judgment comes from people, through contact with real failures.

**The most sophisticated architectures are the ones honest enough to mark where their own authority ends.**

<video preload="auto" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/tweet_video_thumb/HNv7MPka0AAExuB.jpg" src="https://video.twimg.com/tweet_video/HNv7MPka0AAExuB.mp4" type="video/mp4" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"></video>

![](https://pbs.twimg.com/tweet_video_thumb/HNv7MPka0AAExuB.jpg?name=large)

GIF

## The honest hype check

Most tasks never need a graph.

The default is a loop. A single agent running discover, plan, execute, verify handles far more than builders expect, and it's cheaper to build and debug.

Escalate only when the problem genuinely stops being one job. The people calling this whole thing slop have a point, and you should keep it in your pocket the entire way through.

Because here's the trend nobody's pricing in. Graphs of loops will fail too. In their own characteristic way. Circularly, consistently, plausibly, wherever they're built without anchors. And the discourse will lurch again toward whatever comes next.

Which means the durable axis was never loops versus graphs.

**It's ungrounded versus grounded.**

Whether the machinery, whatever shape it takes, keeps touching the reality it claims to improve. Whether its numbers settle against the world. Whether its watchers are genuinely independent. Whether its frozen rules stay frozen under pressure.

And whether it admits its deepest targets were chosen, not computed.

## Six graphs to build this week

Pick one. Ship it before Friday.

**Security sweep.** One subagent per route file hunting missing auth checks, then a verifier pass confirming every finding. Breadth no single context could hold.

**Cited research report.** Decompose the question into distinct angles, run parallel searches, dedupe the sources, adversarially verify every claim before writing a word.

**Port a module file by file.** Fan out translation across files, run the test suite as a gate on each one, loop the failures back.

**Adversarial diff review.** Route on diff size. A small change gets one quick pass. A large one triggers a full parallel audit on distinct lenses, then a judge panel synthesizes.

**Ecosystem scan on a schedule.** Check many sources in parallel, rank by impact at a barrier, write the digest. Save it once, re-run it forever.

**Discovery of unknown size.** Finders in parallel, dedupe each new find against everything seen, verify the survivors, loop until two rounds turn up nothing new.

**A prompter asks a question. An architect draws a graph.**

The linear agent was never the ceiling. It was just the first shape, the one everyone reaches for because it matches how we type. One line, one head, one thing at a time.

Once you can see the nodes and the edges, you stop asking the agent to do more. You start asking the graph to do it wider. Fan out where the work is independent. Gate the edges where confidence matters. Tier the models where judgment doesn't.

Most people will keep queueing steps in a line. The ones who learn to draw the graph will run a fleet.

And they'll never notice the ceiling the rest are stuck under.

I write my exclusive content on [Newsletter](https://substack.com/@humzakhalid) so make sure to subscribe and get more daily content that 99% of people are missing.

Also follow [@humzaakhalid](https://x.com/@humzaakhalid) for more AI Content that helps.

Comment below if you want me to cover more topics in Graphs.

\_ Hamza 💙