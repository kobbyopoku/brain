---
title: "How to Build a Full AI Sales Team Inside Claude Code"
source: "https://x.com/itsalexvacca/status/2074481281640079737"
author:
  - "[[@itsalexvacca]]"
published: 2026-07-07
created: 2026-07-22
description: "You can build a full AI sales team inside Claude Code: a set of specialists that each own a job and work together the way a real revenue tea..."
tags:
  - "clippings"
  - "gtm"
  - "claude-code"
  - "agent-tooling"
---
![Image](https://pbs.twimg.com/media/HMn7OqabIAAM-b6?format=jpg&name=large)

You can build a full AI sales team inside Claude Code: a set of specialists that each own a job and work together the way a real revenue team does. We built exactly that, and it produced $7.83 million in qualified pipeline for one client with zero new hires.

At Frontal we build revenue systems for B2B companies in 90 days, and this is the same setup we run for real accounts right now.

Below is how it's put together and how you can run it yourself, from scanning your website to a live campaign with the content to match.

# Why one prompt never works

Most people picture one magic prompt. They open Claude Code, type something like "write cold emails to find clients," paste whatever comes out, and wait for replies that never come.

You would never hire one person to be your strategist, your data person, your copywriter, and your LinkedIn content person all at once. Good work gets split into roles, each with its own knowledge. The same is true for an AI team.

# B2B revenue really breaks into six jobs

![Image](https://pbs.twimg.com/media/HMn1dS5bkAAmfCS?format=jpg&name=large)

The six jobs: strategy, signals, data, copy, execution, and the system that connects them

**Strategy.** Figure out who you can actually sell to, what your prospects care about, and why they would pick you over the alternatives.

**Signals.** Track the best-fit companies and wait for a sign they are ready to buy: a fresh funding round, a new hire they just made, or research they are doing on your competitors.

**Data.** Pull the right contacts at those companies, with a real phone number and a real email.

**Copy.** Write outreach that reads like a person wrote it for that one specific company rather than a template blasted out to thousands.

**Execution.** Send the actual emails, the LinkedIn messages, and the follow-ups.

**The system.** Connect the other five so it runs as one motion instead of five tools that never talk to each other.

Every one of those is its own skill.

# Skills give each job its own brain

A skill is a plain text file.

It gives Claude deep knowledge for one job and nothing else, the same way you would hand an onboarding doc to a new hire on day one. Because it's just text, anyone on your team can open a skill and edit it like a Google doc, no code needed.

![Image](https://pbs.twimg.com/media/HMn1sh2awAAkRo9?format=jpg&name=large)

Two layers: master skills on top routing to reference files underneath, stacked like lego blocks

You build them across two layers.

On top sit the master skills, which take your request and route it to the right specialist underneath. Below them sit the reference files that hold everything your company knows: your cold email templates, how you score accounts, the signals you want to track. Each one is its own small file. You stack them like lego blocks, and when something changes you swap one skill for another.

> A skill is an onboarding doc for a new hire, written once and reused on every run.

# What's in the library

![Image](https://pbs.twimg.com/media/HMn17VwaEAAQYYD?format=jpg&name=large)

The library: an orchestrator plus 52 sub-skills across Clay, signals, cold email, LinkedIn, list building, n8n and more

We collected a set of GTM skills into one repo you can drop straight into Claude Code. There is an orchestrator on top, then 52 sub-skills grouped into categories: Clay (nine of them for automating work inside Clay), signals (nine covering the most common ones and how to track them), cold email, LinkedIn ads, LinkedIn content, list building, n8n automation, email copywriting, sales triggers, and SDR tool setup.

Adding them takes a minute. Copy the skills into Claude Code, or download the whole repo as a zip.

# Run it: one prompt, the whole motion

![Image](https://pbs.twimg.com/media/HMn2PpGbcAAcDCq?format=jpg&name=large)

A Claude Code run: reading the skills, scoring 100 accounts, tiering them, writing the sequence, drafting content

Open Claude Code inside the Claude app, in the Code tab. You can use Whisper Flow to talk instead of type, so you're not typing everything out by hand. Then point it at your website and give it the plan.

```javascript
Scan my website and figure out my ICP and the type of
companies I want to target. Build a list of actions, then
walk me through creating personalized outbound campaigns that
track the right signals. After that, give me content ideas we
can post on LinkedIn.
```

Because the repo is already in the conversation, the agent has all the GTM skills on hand and reaches for them as it works.

# The action plan it works through

![Image](https://pbs.twimg.com/media/HMn21klbAAA3SNm?format=jpg&name=large)

The seven-step plan from ICP and scoring through to LinkedIn content

The agent moves through the plan in order.

- It defines the ICP and builds a scoring model where every lead is scored out of 100. It pulls the target accounts and gives each a tier.
- It selects the signals to track, then builds a play for each signal.
- It personalizes, writes the sequence, and finishes with a set of LinkedIn content ideas.

# What comes back

**A tiered list.** Ask for 100 companies and it hands them back tiered. On one run it returned 26 that fit tier one, 7 that fit tier two, and 67 it excluded.

**The signals that mean someone is ready.** The ones worth watching came out as a fresh funding round, hiring an SDR or a GTM role, a new CRO or VP of Sales, or using a competitor's tool.

**Copy written for the signal.** Here is a first email it wrote for a Series B company that landed in tier one.

```javascript
Subject: after the Series B

Hey {first name}, a Series B usually comes with a board
mandate to grow pipeline fast, and the motion that worked
before the raise rarely scales to hit it. We help solve
exactly that with a system instead of a new headcount:
$7.83M in qualified pipeline in 10 months, zero SDRs.
Open to comparing notes on your next phase of growth?
```

There's no "congrats on your raise," which is what nearly everyone sends the week a company announces a round.

**The signal is the hook, and the offer sits right behind it.**

![Image](https://pbs.twimg.com/media/HMn3R7lbYAAoFEV?format=jpg&name=large)

Two email openers side by side: a generic one at about 3.43% reply and a signal-based one at 15 to 25%, a 5 to 7x lift

The numbers explain why it lands.

Around 91% of cold emails get zero replies, and the average reply rate sits near 3.43%. Writing off a real signal moves that to 15 to 25%, roughly a 5 to 7x lift in replies.

**Content to match.** Pick a content pillar and one idea, then have the agent research it with a tool like Exa or Linkup and draft a post backed by real numbers. It can call an infographic skill to generate the visual too, the kind that used to take a designer a few hours. You get a near-ready post and image, and you just add your own photo. You can even add a step so that once someone replies to the campaign, they get added on LinkedIn and start seeing more of your content.

# The part the skills don't do

Skills get you moving, and the real work is everything around them: nailing the strategy, choosing the right signals, getting clean data, and knowing what actually gets a B2B company to reply. Get those right and the skills carry the rest.

> The skills run the motion. You still own the strategy, the signals, and the offer.

## Start building your team

Drop the repo into Claude Code, point the prompt at your own website, and start with a single skill. Add the next one once it's pulling its weight, and keep stacking until the whole motion runs from one conversation.

You will have a scored, tiered list in minutes, signal-based copy soon after, and content ideas to go with it, all from the same run. If you'd rather have the whole system built for you, that's the work we do at Frontal.