---
title: "The 3 Phases of the AI Layer Most Services-as-Software Founders Get Wrong"
source: "https://x.com/itsalexvacca/status/2056419277520224620"
author:
  - "[[@itsalexvacca]]"
published: 2026-05-18
created: 2026-05-21
description: "Building a cold email campaign at ColdIQ used to take me an entire afternoon. Now it takes 15 minutes. The compression came from building th..."
tags:
  - "services-as-software"
  - "ai"
  - "agents"
  - "autonomy"
---
![Image](https://pbs.twimg.com/media/HIm4ynpbkAA13a2?format=jpg&name=large)

Building a cold email campaign at ColdIQ used to take me an entire afternoon. Now it takes 15 minutes.

The compression came from building them in a specific order that we've been running ColdIQ as a services-as-software company for over 3 years. [$7M+](https://x.com/search?q=%247M%2B&src=cashtag_click) ARR, 400+ B2B clients served, and a team of 30+ across 10 countries. The thing that took me longest to understand wasn't the tools, the agents, or the stack we sit on. It was the order in which all of it goes in.

There is a sequence to the build: spine first, then agents, then the loop on top. Build any other order and the system can't compound.

This article breaks down exactly what the sequence looks like, why the order is the only part that matters, and what to do if you're working with a half-built stack right now.

# Why your AI fulfilment layer is important

If you're building a services business in 2026, the AI fulfilment layer is the single line item that decides your ceiling.

Get the layer right and you take on a new client without a new hire. Margins stay near software margins instead of agency margins. Every model release lowers your cost of delivery while the price to the client holds. Case studies stack up faster than competitors can copy them, because the data flywheel under the layer compounds with every campaign you ship.

Get it wrong and you become a body shop with a logo. You hire a fifth person to deliver what the layer should have absorbed. Then a sixth. Margins drift where margins always drift in agencies, and the story ends at a ceiling you can't break without rebuilding from the bottom.

The shape of the layer is something I've described before (["services don't scale"](https://twitter.com/itsalexvacca/status/2044543861616492732) is the version of this argument I keep coming back to). **Data, outreach, orchestration, reporting, knowledge. Five layers.** That's a different argument. This one is about which layer you build first. The layers compose, and the order they compose in is non-obvious. Most founders reverse it.

## What I missed for two years

A few weeks ago I shot [a video called I Tried Building a Cold Email Campaign ONLY Using AI Agents](https://youtu.be/M6gBVUw85Uo). Four agents. One session. End-to-end campaign ready to send in under an hour.

The video looks like the agents are doing the work.

They aren't.

The four agents in that video work because everything underneath them was built years before the agents existed.

- The ICP framework was trained on 2,200 cold email campaigns we'd already shipped.
- The list builder was an internal product we shipped inside Clay over many cycles.
- The copy patterns came from the [same emails that generated $10M+ for clients](https://twitter.com/itsalexvacca/status/2044421372764647844).

Hand the same four agents to a founder with no spine underneath, and they produce the same campaign 90% of people building outbound businesses ship in their first quarter: wrong ICP, no signal density, no reply.

The agents didn't compress the work. The spine compressed the work. The agents made the compression visible on a screen recording.

That's the thing I missed for two years, and the thing most founders still miss. The agents are the layer everyone wants to build first because they look impressive. They are the layer that pays back last.

## What do you think I'm seeing

The spine is the part of the fulfillment layer that doesn't look like AI. Because it's the data layer that sits between the universe of prospects and every downstream action your system will ever take. The spine gives the agents a place to read from and a place to write to. Skip it and the agents make decisions in isolation, which is how you get a Reply Manager drafting responses that contradict what the operator told the prospect last week.

What the spine has to do, in order:

- **One CRM, not three.** Pick the system every campaign's data flows through. We run Attio. You can run something else. What can't happen is the data sitting in three places with three sources of truth.
- **Multi-domain sender infrastructure from day one.** We send across 4 ESPs simultaneously, with sender domains spun up specifically for outbound. [The deliverability gatekeepers retrain spam classifiers constantly](https://twitter.com/itsalexvacca/status/2044877048217501748). The kind of change that breaks single-ESP setups quietly, until a week of campaigns has gone silent. Two-ESP redundancy is the floor, not the ceiling.
- **One canonical data layer.** We run Clay as the table every campaign reads from and writes back to. It carries the enrichment, the tier assignments, the negative-signal columns, the reply tags. One table. Every client. That table is the agency's memory.

The mistake every operator I've watched makes is treating the spine like plumbing they'll get to later. They build a single Apollo CSV, send it through a sequencer, and chase the first reply. Then the second campaign starts. The data from campaign one isn't anywhere. The list pull starts from zero. Six months in, the operator is hiring a delivery person to keep up with the mess, and the mess is what they spent six months not building.

**The spine doesn't ship a campaign on the day it goes in.** That's the reason most founders skip it. It's also the reason the founders who skip it stall at the fifth hire.

![Image](https://pbs.twimg.com/media/HImpz1ibkAAgbjR?format=png&name=large)

The Fulfillment Sequence

## Phase 2: The Agents

The agents are the layer that finally looks like the product the customer thinks they're buying. They're also the layer most founders try to ship first, which is the second-most-common reason the whole sequence collapses.

Two agents pay back first. The rest pay back later. Build them in the order and their ROI compounds.

## Agent one: the Reply Manager

Every cold reply is a routing decision.

- Is it a positive signal that needs a calendar link?
- A bounce that needs to feed back into the data layer?
- A wrong-contact that needs to be re-routed inside the prospect's company?
- A polite no that should never see a manual response?

The Reply Manager classifies the reply, drafts the response, and waits for an operator to approve before anything goes back out. We run it on n8n. The agent gets the reply, the prospect's history from the spine, the campaign context, and writes the draft in Slack. The operator reads three lines and approves or rewrites. The hours that used to disappear into triage compound back into pipeline work.

## Agent two: the Enrichment Waterfall

Clean lists compound every downstream metric.

- We run Wiza first against LinkedIn profiles
- FullEnrich second to cascade through 20+ providers under the hood
- Prospeo to clean up the residual at 98%+ verified accuracy

Run the full waterfall and email coverage lands at 90%+ on harder ICPs.

That coverage is the reason the agents downstream don't waste their token budget writing copy for prospects whose emails will bounce.

**What you don't agent-ize yet:**

1. **Copy strategy.** Personalization at scale is an agent job. Deciding what the campaign is actually selling stays with a senior operator who's run the offer through enough rebuilds to know which version converts.
2. **Client relationship.** The agents handle the work. The operator handles the call where the client is unhappy and the agency is one renewal away from a churn.
3. **Edge cases.** The agent that tries to handle every edge case is the agent that drifts. Agents work inside the 80% of the work that's repeatable. The other 20% stays human.

The mistake I see in the accelerator over and over is operators trying to ship a Lead Researcher agent, a Campaign Strategist agent, and a Booking Coordinator agent in week one. Three agents, no spine, no compounding loop, and a stack that takes more attention than the manual work it was supposed to replace. **Two agents on top of a clean spine outperform six agents on top of nothing. Every quarter.**

## Phase 3: The Loop

The loop is the part of the fulfillment layer most operators never build, which is why most fulfillment layers stop compounding the second the first set of agents goes live.

The loop wires the outputs of every campaign back into the inputs of the next one.

> Engagement signals from LinkedIn into the data layer. Buying triggers from PredictLeads and Common Room into the scoring model. Reply intelligence from Instantly into the negative-signal column in Clay. Disco call notes back into the ICP definition. Lost-deal reasons back into the copy framework's do-not-promise-this constraint.

I've written a separate piece on [the four feedback edges that connect the layers of the operating stack and exactly how each one wires up](https://x.com/itsalexvacca/status/2047046755896946798). Read that for the technical detail. The thing to understand here is that without the loop, every campaign starts from the same priors as the last one. Campaign two doesn't know what campaign one learned. The agents stay the same age forever. The system never compresses cost, never improves response rates, and never builds the data moat that turns a services-as-software agency into something a SaaS pure-play can't copy off the shelf.

The loop is the part where the data flywheel finally turns into something that compounds. Every reply, every meeting outcome, every engagement signal, every disco call note routes back into the spine. The spine carries it forward into the next list pull, the next copy pass, the next tier assignment. By campaign 20, the system is making decisions on patterns that took a senior operator three years to learn manually. By campaign 200, the system has seen patterns no human operator could have seen at all.

That is where cost per delivered client finally starts to flatten. Not at agent one, and not at agent five. It flattens at the loop, where every campaign starts paying down the cost of the next one.

# What stays human after the build

A services-as-software company isn't an unattended SaaS product. The client is paying for an outcome, and the outcome lives where judgement still matters.

Three things stay human at ColdIQ regardless of how good the agents get.

1. The strategic call on what the campaign is actually selling. Is it the offer, the angle, or the trigger event? The agents can write copy against any one of those, and the writing reads cleanly in all three directions. **The operator is the one who decides which one to point them at, because the wrong choice on a clean list still produces a campaign that doesn't reply.**
2. The decision to pivot when the data says the offer itself is broken.n Reply rates collapsing on a clean list with clean copy is the system telling you the offer is the problem. **Most agencies respond by rewriting the copy.** The senior operator responds by rewriting the offer. That call is not yet an agent's job and won't be for a while.
3. The client relationship, every account, every week, the same operator who owns the book. The agents write the dashboard updates. The operator does the call where the founder of the client company asks whether to keep going or shut it down. The agents are not yet allowed in that room.

![Image](https://pbs.twimg.com/media/HImtfz9bsAE4zYm?format=jpg&name=large)

What stays human after the build

## What this means for someone starting now

The cost of running an outbound stack collapsed in the last 18 months. The bottleneck isn't access to the tools anymore. The bottleneck is the operating system around them and the order the operator builds them in.

If you're staring at a half-built stack right now, you don't need more agents. You need to install the spine, deploy two agents on top of it, and start saving every output as an input to the next campaign. In that order.

Most services-as-software builds ironically collapse due to the right tool installed at the wrong time (read too early). Do it in the sequence above and scaling your operations will be a walk in the park.