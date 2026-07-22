---
title: "How to Run Clay From Claude Code: A 12-Skill GTM System"
source: "https://x.com/itsalexvacca/status/2079249286882287897"
author:
  - "[[@itsalexvacca]]"
published: 2026-07-20
created: 2026-07-21
description: "This is the exact setup we use at @Frontal_AI to run Clay from inside Claude Code.You give it a company name, and what comes back is a compa..."
tags:
  - "clippings"
  - "gtm"
  - "claude-code"
  - "agent-skills"
---
![Image](https://pbs.twimg.com/media/HNrouCxbAAAHGJZ?format=jpg&name=large)

This is the exact setup we use at [@Frontal\_AI](https://x.com/@Frontal_AI) to run Clay from inside Claude Code.

You give it a company name, and what comes back is a company that's already been researched and scored and written into ready outreach, with nobody touching a Clay table to get there.

We're one of four Clay Elite Studio Partners in the world, and we turned the way we run it into twelve GTM skills you can drop into a Claude Code project and run today.

Everything you need to build it and run it yourself is right here. The finished skill files are the one thing we hand over ourselves, and there's a link for that at the end.

> Clay knows what's true about a company. Claude Code knows what to do about it.

# How the system works

Two tools, split cleanly by job.

> **Clay is the data layer.** It reaches into more than a hundred providers and runs them in a waterfall, trying one after another until it lands what you asked for.

On a hard field like a verified work email, that usually gets you into th

e eighties or nineties, where a single source stalls in the fifties.

![Image](https://pbs.twimg.com/media/HNro5a3bkAAbslu?format=jpg&name=large)

Two panels: Clay as the data engine and Claude Code as the reasoning engine, joined by a plus

> **Claude Code is the control layer.** It reads your instruction, decides what data it needs, calls Clay through its API to get it, reasons over what comes back, and writes the output.

You describe the outcome in plain language, and the agent runs the tables underneath.

You wire it once. A Clay API key, the twelve skills in a project folder, and from then on the whole thing runs from a single prompt.

![Image](https://pbs.twimg.com/media/HNrpE6-asAAyrSZ?format=jpg&name=large)

Architecture: a prompt feeds Claude Code, which calls Clay for data and returns a finished opportunity

# Set up the project

The whole system lives in one Claude Code project. This is the shape of it.

```javascript
gtm/
  CLAUDE.md            # standing rules: your ICP, your voice, the run order
  .env                 # CLAY_API_KEY=...
  accounts.csv         # the companies you want to work
  skills/
    company-research.md
    account-brief.md
    competitor-analyzer.md
    news-signal-synth.md
    linkedin-profile.md
    job-posting.md
    icp-scorer.md
    buying-signal.md
    technographic.md
    personalization-writer.md
    objection-handler.md
    email-sequence.md
  output/              # where finished rows land
```

**Three files make it run.**

**CLAUDE.md** is the agent's standing context. It holds your ICP, your positioning, your writing voice, and the order the skills run in. The agent reads it before every run, so you set your rules once instead of repeating them in each prompt.

**.env** holds your Clay API key. Grab it from Clay under Settings, paste it in, and the agent can reach your enrichments without you touching a table.

**skills/** is the twelve skills, one file per job. Each file is a self-contained instruction set the agent loads when it needs that step. This is the part we hand over, so you never write one from scratch.

Once the folder exists and the key is in place, you open the project in Claude Code and you're ready to run.

# The twelve skills

Twelve skills, three jobs. Each one is a self-contained step with a clear input and a clear output, and that's what lets the agent run them in a chain.

Here's what each one actually does.

## Research and intelligence

**Company Research Agent.** Point it at a company and it does the reading you never find time for. Through Clay it pulls the website, the funding history, the product, recent press, and the leadership team, then works out what a seller would actually use out of all of it.

What comes back is short and pointed: what the company does in a line, where they sit in their growth, and the couple of specifics you can build a real opener around. An hour of tab-hopping becomes something you skim in thirty seconds, done the same way for every account on the list.

**Account Brief Generator.** It shapes that research into the one-pager a rep opens right before a call. You get who the company is, the problem they're most likely feeling, the angle worth leading with, and a few talking points that make you sound like you did your homework.

It reads like something a diligent SDR spent twenty minutes on, and it's ready the moment the account clears scoring, so nobody is scrambling five minutes before the meeting.

**Competitor Analyzer.** It works out who the company already buys from in your category and how deep they are into that setup. You walk in knowing the incumbent, the obvious gaps in what they have, and where you actually fit against it, rather than guessing on the call.

That context changes the whole conversation, because you can speak to what they already own instead of pitching into a vacuum.

**News and Signal Synthesizer.** It watches for the moves that give you a reason to reach out now: a funding round, a product launch, a push into a new market, a senior hire.

Out of everything it finds, it surfaces the one event genuinely worth mentioning and drafts a line around it, so your outreach lands while the news is still fresh instead of referencing something from last quarter.

**LinkedIn Profile Analyzer.** It reads a person's profile the way a thoughtful seller would, not just the title. It looks at their background, the path that got them into this role, and what they choose to post about, then tells you what they seem to care about and the most natural way to open with them.

On a founder it might flag a build-in-public streak; on a VP it might catch that they came up through the exact function you sell into.

**Job Posting Analyzer.** It reads what a company is hiring for, because open roles are the clearest tell of where the budget is heading. A wave of SDR openings means the outbound number just went up. A first RevOps hire means they're about to care a lot about the tooling underneath.

It hands you the roles that matter and a plain read on what each one signals, which is often a better buying trigger than anything in a firmographic filter.

# Scoring and qualification

**ICP Scorer.** It rates every account against your ideal customer using the research the earlier skills gathered, not a static filter you set months ago. Because the score comes from what's actually true about the company right now, the strongest fits rise to the top and your effort goes where it converts.

The weak fits get flagged and set aside before anyone spends a minute on them, which is usually where most of a rep's wasted time goes.

**Buying-Signal Detector.** It checks whether an account is in motion right now and tells you why. Maybe they just raised, maybe they're hiring into your buyer's team, maybe they tripped a signal you track.

Instead of working the whole list on a Monday, you reach the handful with a live reason to talk this week, with that reason attached so the outreach can point straight at it.

**Technographic Qualifier.** It checks the tools a company already runs, which often decides the whole conversation before it starts. Running the kind of stack you plug into makes them an easy yes and tells you exactly how you slot in.

Running a competitor's tool isn't a dead end either, because now you know the incumbent and can lead with the switch. Either way, you stop pitching blind and start from what they actually use.

# Writing and outreach

**Personalization Writer.** It writes the opening line and the angle straight from the research the other skills gathered, so the first sentence points at something true about that specific account rather than a first name dropped into a template.

It writes on your voice profile too, which means the phrasing and rhythm come out sounding like you wrote it, not like a model on its default setting. That's the difference the reader feels, and it's the whole reason a cold message earns a reply.

**Objection Handler.** It looks at the specific account and drafts answers to the pushback that account is most likely to raise. For a company already running a competitor it preps the switch conversation; for a team that just cut budget it preps the cost angle.

You get the two or three objections you're actually going to hear, with a real response to each, so you're not improvising the "we already have something for that" reply live on the call.

**Email Sequence Writer.** It builds the whole sequence off everything above, so the messages connect instead of standing alone. The first email opens on the research, each follow-up picks up where the last left off and adds a fresh reason to reply, and none of them read like the "just bumping this" notes most sequences turn into.

What you get is a full sequence you can drop straight into your sender, written around this account rather than a template with the company name swapped in.

Underneath, every one of them works the same way. Clay fetches the raw material, and Claude decides what it means and how to say it.

![Image](https://pbs.twimg.com/media/HNrpsTgbwAAnAT3?format=jpg&name=large)

The twelve skills grouped into three columns: research and intelligence, scoring and qualification, writing and outreach

# What a skill looks like inside

Open one up and the pattern is the same for all twelve. Take the Company Research Agent.

It starts with a company name.

- **Clay fetches the raw material:** the firmographics and size, any recent funding or news, the tech stack, and the open roles. On its own that's a pile of facts.
- **Then Claude reads it the way a seller would**. It weighs the fit against your ICP, works out the angle most likely to land, and judges whether the timing is right. Out comes a one-page brief in plain language.

That's the shape of every file in the skills folder. Clay brings the facts, and Claude brings the judgment. Chain twelve of them and you have the system.

![Image](https://pbs.twimg.com/media/HNrp6m4a4AAenrE?format=jpg&name=large)

Inside one skill: a company name goes in, Clay fetches the data, Claude reads it for judgment, a brief comes out

> Every skill is the same handshake. Clay brings the facts, and Claude decides what they mean.

# Run it

With the project open, you run everything in plain language. There are three ways to use it.

**Run one skill** when you want a fast answer on a single account.

```javascript
Run the company-research skill on Northwind and give me the brief.
```

**Run the full chain** by handing it a list and the outcome you want. It walks every account through the skills in order.

```javascript
Take the companies in accounts.csv. Research each one, score it
against our ICP, and flag anything showing a live buying signal.
For the accounts that pass, write a personalized opener and a
three-email sequence, then save the results to output/.
```

Behind that one line, the agent calls Clay for the data at each step, runs the research and scoring skills, sets the poor-fit accounts aside, and writes the outreach for the ones worth pursuing.

What lands in output/ is a clean row per account: the research, the score, the signal, the opener, and the sequence, with the reasoning attached so you can check its work.

![Image](https://pbs.twimg.com/media/HNrqSVha0AAMJvc?format=jpg&name=large)

Change the list, not the process. The same instruction covers one account before a call or a few thousand overnight.

**Change the list, not the process.**

The same instruction covers one account before a call or a few thousand overnight.

Doing that research, scoring, and first draft by hand runs close to an hour per account, and only ever one at a time. The agent does it in minutes, at any volume. You swap the CSV, and everything else stays the same.

![Image](https://pbs.twimg.com/media/HNrqcj1a0AAJvQZ?format=jpg&name=large)

By hand it is a long chain of manual steps at about 45 minutes per account; from one prompt the agent runs the whole thing in minutes at any volume

# Start with one skill

Start with one skill, not twelve.

Run company-research on ten accounts, read what comes back, and once you trust it, add icp-scorer, then personalization-writer.

Four or five of them chained together already save you an afternoon a week, and the rest is more of the same.

# Why the output doesn't read like AI

This is worth calling out, because it's where most AI outreach dies.

The Personalization Writer never writes from a blank slate. It writes from the research the earlier skills already gathered, so the opener points at something true and specific about the account instead of a first name dropped into a template.

It also runs on a voice profile, so the words carry your rhythm rather than the default model tone.

The result reads like a rep who did their homework, because the homework got done. The research skills just did it instead of a person.

![Image](https://pbs.twimg.com/media/HNrqtUYa4AATSNH?format=jpg&name=large)

A generic AI message next to a research-backed one, showing the difference between fluent and specific

> Personalization was never a merge tag. It's proof that someone actually looked.

# Get the full build

The twelve skill files, the prompts inside them, and the Clay setups that feed them are the part we hand over directly.

Comment under the post, or send me a message, and I'll get all twelve to you, ready to drop into the project you just set up. Nothing to buy, and no form to sit through. It's the same system we run for clients at Frontal.

Once the agent is driving Clay, every repetitive GTM job you still do by hand becomes the next one you hand over.