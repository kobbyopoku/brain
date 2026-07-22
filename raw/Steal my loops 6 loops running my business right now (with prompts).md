---
title: "Steal my loops: 6 loops running my business right now (with prompts)"
source: "https://x.com/ericosiu/status/2079327410613317866"
author:
  - "[[@ericosiu]]"
published: 2026-07-20
created: 2026-07-22
description: "I don't run most of my business by prompting anymore. I run it on loops.A loop sets a target, checks reality against it, acts, remembers wha..."
tags:
  - "clippings"
---
![Image](https://pbs.twimg.com/media/HNsydOvXUAAO9cy?format=jpg&name=large)

I don't run most of my business by prompting anymore. I run it on loops.

A loop sets a target, checks reality against it, acts, remembers what happened, and comes back sharper next time. Once you have a few, they run parts of the company on their own, and you stop being the one sitting in every thread.

I built fifteen or twenty of them over a weekend on Fable 5, the strongest model I can point at this right now.

This is a look at the ones running right now. What each does, why I built it, and the prompt behind it. Steal whatever fits your business.

## A loop isn't a /goal command

Quick foundation, because this took me months to get right.

A /goal command is a one-off. You give it a goal, it works toward an outcome, and it gets there. Useful, and I use it all day.

But run the same /goal next week and it starts from scratch, with no memory of the last run.

A loop keeps the memory. It has a target and a current state, works the gap, records what it learned, and reads that back on the next run.

That learning store is why a loop gets sharper and a /goal command never does.

```text
target state (what good is)
       |
       v
observe (your own data)
       |
       v
evaluate (against a rubric)
       |
       v
act (draft, test, notify)
       |
       v
learn -> store what happened
       |
       v
decide: keep going, stop,
        change, or escalate
       |
       +--> loop back, sharper
```

## First, find what to loop

Before building anything, I ask the model what's worth looping. This is the prompt I start with. Screenshot it if you want.

> "Knowing what you know about how I work, my goals, and my repos, what are the best use cases for Fable 5 to maximize revenue? Rank them top to bottom. Include finishing my open projects, rebuilding them with a Fable 5 lens, and finding technical blockers. Ideally, only things other models can't do."

It ranked my list and put the boring, high-value stuff on top. Finish the half-built projects. Restart the revenue loops that had gone dormant. Sweep the repos for security holes.

One more trick from that session. When something is worth moving between tools, I have it write a handoff document first.

That way I can pick the work up in Codex, Claude Code, or Hermes without losing the context. A loop is only as good as the context you hand it.

## The sponsorship loop

This is my favorite, so I'll start here. People reach out constantly to sponsor the channel and the podcast. I don't want to handle it, and neither does my team.

I built it because the back and forth ate my time, and because a team that guards the calendar sends a better signal than me haggling in a DM.

So the loop answers every inbound on its own. Here's the reply it sends:

> Thanks for reaching out. Mr. Siu's queue is tight right now, so he's only taking fixed-fee sponsorships at $25,000 for one post. If that works, send the product, campaign timing, usage rights, talking points, platform, posting date, and disclosure requirements.

If someone counters with a smaller budget, it holds the line and asks whether the number works.

People do pay it. And even when the money is on the table, I still don't want to spend the hours, so the loop wins either way.

It also lifts the positioning. A firm number from Mr. Siu's team reads differently than me negotiating in my own inbox.

Then the part that got me. After a run, it reported "tuning applied." It had rewritten its own instructions, adding rate-card handling, audience-insight notes, creator-selection language, and dedicated video-bundle usage rights it decided it needed.

Nobody told it to. It read its own results and upgraded itself for the next batch.

It runs every day now. I glance at the queue when I feel like it, and the rest handles itself.

That is the template for everything you don't want to touch. Find the repetitive back and forth, write the loop, and let it hold the line for you.

![Image](https://pbs.twimg.com/media/HNs1SyyXYAAqNtW?format=jpg&name=large)

## The conversion loop

I built this one because [singlebrain.com](https://singlebrain.com/) drives leads, and I wanted the conversion rate climbing without me touching it every week.

I picked this site on purpose. A couple thousand visitors a month, steady lead flow, and low risk if a test flops. That's the right place to let a loop run with a light touch.

Here's the setup:

```text
Loop: weekly conversion optimizer
target: +30% conversion over 4 weeks
current: ~1.8% on singlebrain.com
observe: last week's test result
act: ship one new test per week
learn: log what moved the number
decide: keep, kill, or change the test
gate: I approve before anything ships
```

Every Monday it tells me what it changed, what happened, and what it plans to try next. I read it in about a minute.

Run as a plain /goal, it would start over every week with no memory of the last test. As a loop, four weeks of tests add up to a lift.

The gate is the part that's easy to skip. You decide the one place a human signs off, and the loop respects it.

Once a test wins, the same loop can widen it. It proves the winner on a small batch, then runs it at scale while it keeps measuring.

![Image](https://pbs.twimg.com/media/HNs1_U7XAAAWJKq?format=jpg&name=large)

## The content loop

I built this because my best material comes out of calls, not scripts, and it kept getting lost.

This loop ingests what I produce, my long-form videos, my Gong call recordings, even a talk like this one, and finds the moments worth posting.

The Gong calls are the source that matters. Gong records our sales and internal calls, and my sharpest lines almost always come out of a live conversation instead of something I sat down to write.

Then it drafts pieces around ideas that are early, like company brain, Single Brain, and AI agents that live in Slack. Low search volume today, and some of them will take off.

Being early on a term is most of the game, and this is how I stay ahead of it.

It chains a few tools to do the work. Ahrefs for the search data, the ClickFlow MCP to shape and publish, and our own analytics for context. The MCP is free, so the cost stays low.

I get the first version to about 70 percent and hand it to a ClickFlow engineer who takes it to a nine or ten. I'm the prototyper. You probably have a few of those on your team, whether you've named them or not.

The X long-form skill inside this is the one I lean on most. It helped take an account from 87,000 impressions a month to over three million.

![Image](https://pbs.twimg.com/media/HNs2duaWEAA1BdU?format=jpg&name=large)

## The LinkedIn loop

I built this one because someone posted about getting five million impressions a month on LinkedIn, and I wanted the play running on autopilot.

I asked the model to turn that post into a loop. It gave me a template:

> \[Give away something people usually pay for.\] Here's a simple AI revenue loop scorecard that finds the one workflow in your business worth automating. Comment "loop" and I'll send it over.

The play is specific. Post a resource people would normally pay for. Ask for a one-word comment to get it. Then reach out to the ICP-fit people who commented, which is exactly what the original poster's software was built to do.

The loop keeps a few post variants and tests the premise over and over, tuning which angle pulls the most comments. It runs off my content library, so the giveaways stay on brand.

This worked for me years ago, when a LinkedIn post of mine would pull fifty thousand views. I'm rebuilding that muscle, and the loop is how I do it without living on the platform.

I prototype it, hand it to the team, and we sharpen it from there.

![Image](https://pbs.twimg.com/media/HNs3U4xXYAAE5pt?format=jpg&name=large)

## The sweeps

A few of my loops exist to catch problems before they cost me.

Fable 5 is strong at code, so I point it at a repo and it finds security holes and fixes them. It caught three or four issues in one repo on the first pass.

One heads-up. When it senses anything security-related, it hands the session back to Opus 4.8, a safeguard from the stretch when access was restricted. Switch back to Fable 5 and keep going.

The bigger idea is to make the model verify, not only build. Point it at a system you assume already works, an attribution model or a lead score, and tell it to prove the numbers hold up.

I run a CRM sweep on the same principle. It keeps the data clean and flags the records that look off, with a human checking before anything changes. That used to be a full role.

I also run a sweep on [singlegrain.com](https://singlegrain.com/) every day that catches broken forms, dead links, and busted thank-you pages before a lead hits a wall.

And a last-mile sweep does the same for pipeline. Before I spend a dollar on more traffic, it looks for where activity dies: a reply nobody routes, a form fill that alerts no one.

When a client asks how we know a result is true, a daily sweep is the answer.

![Image](https://pbs.twimg.com/media/HNs4tmJW8AAVWRT?format=jpg&name=large)

## The revenue command center

I built this because I lose track of deals across too many tools.

```text
Loop: revenue command center
observe: CRM, calls, pipeline
surface: stale deals, deals I lost
act: draft the right follow-up for each
learn: track which follow-ups get replies
gate: I approve, then it sends
```

It runs daily and hands me a short list. Which deals went quiet, which ones I lost, and the follow-up to send each.

It also drafts the revival message for deals I lost a while back, so reopening old pipeline becomes a two-minute approval instead of a project.

On most mornings, I skim the list, approve the ones that look right, and it sends them. Over time it learns which messages get answered and leans into those.

## Loops run parts of the business

Once you have a few of these, it clicks. Agents help you with tasks. Loops run parts of the business on their own.

The bigger win is your team. Teach one person to build loops and they start scaling the way you do, without you sitting in every thread. They build the systems instead of waiting for the next instruction.

That's the whole reason we keep our skills in one place people can pull from. A loop one person builds becomes a loop the whole team can run.

## Steal these prompts:

```text
# Loop build prompts (copy, paste, fill in the brackets)

Six reusable prompts for building revenue loops. Swap every [BRACKET] for your own numbers, sites, and tools before you run them.

---

## Find what to loop (start here)

Knowing what you know about how I work, my goals, and
my repos, what are the best use cases for [MODEL] to
maximize revenue? Rank them top to bottom. Include
finishing my open projects, rebuilding them with a
fresh lens, and finding technical blockers. Ideally,
only things other models can't do.

---

## Inbound handler loop (sponsorships, DMs, quotes)

Build me a loop that handles inbound [OFFER TYPE, e.g.
sponsorship offers] for my [CHANNEL / BUSINESS]. When
one comes in, reply on my behalf: thank them, set the
terms, and hold a fixed price of [YOUR PRICE] for
[WHAT THEY GET]. If they counter lower, hold the line
and ask whether the number works. Store every exchange,
and after each batch, review your own results and tune
your own instructions for next time. Flag anything
unusual for me to approve.

---

## Conversion loop (any page you want to improve)

Build me a weekly loop to raise conversion on [YOUR
URL]. Target a [X]% lift over [N] weeks from a [CURRENT
%] baseline. Each week, observe last week's test
result, ship one new test, log what moved the number,
and decide whether to keep, kill, or change it. Store
the learnings so each test builds on the last. Report
what you changed and what you'll try next every [DAY].
Wait for my approval before anything ships.

---

## Content loop (turn your raw material into posts)

Build me a content loop. Ingest my [SOURCES, e.g.
long-form videos, call recordings, talks] and find the
strongest moments. Draft [FORMATS, e.g. posts and
articles] around ideas that are early and low on search
volume. Use [SEARCH TOOL] for the data and [PUBLISHING
TOOL] to shape and publish. Store what performed and
feed it into the next round. Hand me drafts at about
[%] done so I can finish or route them.

---

## Playbook loop (automate a play you found online)

Build me a [PLATFORM] loop from this play: [DESCRIBE
THE PLAY IN ONE OR TWO SENTENCES]. Pull from my
[CONTENT SOURCE], keep a few variants, and test which
angle performs best. Store the results and lean into
the winners over time.

---

## Verify loop (sweeps that catch problems)

Build me sweep loops that check my systems and catch
problems before they cost me. One: scan my [REPOS /
CODEBASE] for issues and fix them. Two: check [YOUR
URL] daily for broken forms, dead links, and broken
thank-you pages. Three: run a last-mile audit for where
activity dies, like a reply nobody routes or a form
fill that alerts no one. Log findings, fix or flag, and
keep a human gate on anything that touches production.

---

## Command center loop (see and act on your pipeline)

Build me a revenue command center loop. Every day, read
my [CRM], [CALLS], and [PIPELINE], and surface the
stale deals, the deals I lost, and the right follow-up
for each. Draft the messages, track which ones get
replies, and learn from that over time. Give me a short
list to approve, then send on my go.

---

Note: every loop needs a target state, a source it observes, a rubric, an action, a place to store what it learned, a stop rule, and a human gate. Keep those in when you adapt these.
```

## How to build your own

You don't need a terminal for any of this. Build it inside Codex, point it at a repo that stores the learnings, and set it to run on a schedule.

The test for whether you built a loop, and not a /goal command on a timer: ask if next week's run will be smarter than this week's.

So take the prompts and whatever you're working on, hand it to your model, and ask what you could turn into a loop based on how you work. Then build the version that remembers.

That's the one that keeps paying while you go build the next.

If you're a business that wants AI systems built for you, check out [https://www.singlebrain.com](https://www.singlebrain.com/)

For marketing help, go to [https://www.singlegrain.com](https://www.singlegrain.com/)

For more like this, level up your marketing with 14,000+ marketers and founders in my Leveling Up newsletter, free: [https://levelingup.beehiiv.com/subscribe](https://levelingup.beehiiv.com/subscribe)

If you want to join our team, beat AI first ;) [https://github.com/ericosiu/beat-claude](https://github.com/ericosiu/beat-claude)