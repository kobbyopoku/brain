---
title: "Turn Hermes into a Superagent with these 12 integrations."
source: "https://x.com/itsolelehmann/status/2056343273023688989"
author:
  - "[[@itsolelehmann]]"
published: 2026-05-18
created: 2026-05-21
description: "You open Hermes for the first time. After 20 minutes you close it and think \"wait, this is just Claude or ChatGPT inside Telegram, what’s th..."
tags:
  - "ai"
  - "agents"
  - "agent"
  - "superagent"
  - "harness"
  - "integration"
  - "hermes"
---
![Image](https://pbs.twimg.com/media/HImXi-yWcAAyHwc?format=jpg&name=large)

You open Hermes for the first time. After 20 minutes you close it and think "wait, this is just Claude or ChatGPT inside Telegram, what’s the f\*cking difference??"

That was me a few weeks ago.

But the reason it felt that way wasn't Hermes' fault. It felt underwhelming because I hadn't plugged anything into Hermes yet.

Think of an agent like a brain floating in a jar.

It's smart, fast, happy to talk for hours, but completely cut off from your actual life. It can't really **do** much. All talk, no walk.

Integrations are the senses and limbs you bolt onto that brain.

The more senses you plug in, the more it can actually do for you.

Firecrawl gives it enhanced eyesight on the web, Reddit becomes its ear to the streets, Bland gives it a voice that can pick up a phone, Stripe puts eyes on your business, Obsidian holds its long-term memory, and so on and so forth.

Connect 2 and you've got a chatbot with context on all your Gmails.

Connect 12 and the first thing you'll see when you unlock your phone in the morning is a list of complex workflows Hermes already ran for you overnight (broke my brain the first time I saw it).

This article will give you my top 12 integrations to turn Hermes from a basic chatbot into a **superagent.**

If you want highly practical AI workflows like this delivered directly to your inbox, I send them to 37k readers every single week. Join here for free: [aisolo.beehiiv.com/subscribe](https://aisolo.beehiiv.com/subscribe)

# The 4 jobs every useful agent setup covers

Every Hermes setup that actually works ends up doing 4 things for you: research, action, workspace, and memory.

Miss one and the agent goes blind in that direction. Cover all four and you've got something that feels like a coworker.

Here's what I run in each bucket and why.

## Job 1: Research (eyes and ears on the world)

So Hermes can find things out on its own without you having to spoon-feed it the context.

**Firecrawl is web search built specifically for agents.**

You get cleaner data and faster responses than the native Hermes search, and it burns way fewer tokens doing it. I keep it on by default.

**Reddit gives you the best read you can find on what people actually think about a product, niche, or problem.**

I run it whenever I'm scoping a new idea (you find out in about 5 minutes if people are quietly furious about something in that space).

**YouTube transcripts pulls captions from any video, so long podcasts, tutorials, and conference talks become searchable notes in seconds.**

Very high-leverage integration and almost nobody plugs it in.

## Job 2: Action (hands and voice in the world)

This is the bucket that lets Hermes do stuff in the world instead of just describing what it would do.

**Browserbase is actual browser access, which means logging in, clicking buttons, and navigating sites that block scrapers.**

If you plug both Firecrawl and Browserbase in, Hermes picks between them automatically depending on the task.

**Bland (or Twilio) gives Hermes a phone voice so it can place live calls for things.**

You can literally have your agent call and book a reservation for you, so you don’t have to be on the call yourself. I love listening to the recordings haha.

**Stripe handles payments, customers, failed charges, and refunds.**

Which means you can ask Hermes "why did this customer churn" and get a straight answer with the receipts attached.

Also Stripe is rolling out agentic payments, so soon Hermes will be able to actually book things with your card. Hyped for this!

## Job 3: Workspace (where you actually live)

This is the bucket that lets Hermes operate inside your business. Without it, the agent can talk about your work, but it can't touch it or understand it fully.

**Google Workspace covers Gmail, Calendar, Drive, Docs, and Sheets in one connector.**

Absolutely essential. If your agent can't read your inbox or write to your docs, it can't really work for you, so plug this in before anything else.

**Discord is huge for me because I host my whole business there.**

I plug Hermes into different channels and have it run different workflows in each.

For example, my customer support channel has Hermes scan email every morning, pull out support tickets, and drop them in organized with priority tagged.

**GitHub covers code, issues, and PRs, which turns Hermes into an engineering teammate that can open a PR, review code, and triage issues.**

Non-negotiable if you ship code.

## Job 4: Memory (the long-term brain)

So Hermes never forgets the things you've already read, learned, said, or written down.

**Readwise pulls every highlight you've ever saved from books, articles, tweets, and podcasts into one queryable place.**

Solves the "dead knowledge" problem, which is when you highlight something brilliant once and never see it again because it's buried in 47 PDFs you'll never reopen.

**Granola gives you searchable transcripts of every meeting you've had.**

So Hermes can answer "what did that client say about pricing last month" instantly.

**Obsidian is for Karpathy-style LLM wiki second-brain maxxing.**

If you keep notes in Obsidian, Hermes can read across your whole vault and connect ideas you forgot you had.

Where all of this gets really awesome: chaining them together.

Plugged in alone, each of these integrations is useful.

But when you stack them together, they start to do things you probably didn't realize were possible.

A few of my actual workflows:

- **The sponsor filter.** When someone DMs on X or emails me about sponsorships, Hermes auto-reads it, scrapes their site through Firecrawl, scans Reddit and YouTube for any real chatter about the company, and drops a one-pager in Discord with a fit-rating for my audience.
- **The customer support agent.** Every morning Hermes scans Gmail for incoming support emails, categorizes each one by issue type, and logs them in my Discord support channel with priority tagged. Once a week it drops a summary in Obsidian with the 5 recurring problems I should actually fix at the root.
- **The Monday business dashboard.** Every Monday at 8am, Hermes pulls revenue, new subs, refunds, and churn from Stripe, grabs my follower growth and post views from X and LinkedIn through Browserbase, and posts a week-vs-last-week breakdown in Discord. 10 seconds to read instead of an hour of dashboard hopping.

Each of these takes 3 or 4 integrations talking to each other. None of them are possible with one plugged in.

## How to plug them in (10 minutes)

**Step 1: Open Hermes and ask it "how do I connect \[tool\]?"**

Just type:

"Hey Hermes, I want to connect my Gmail. What do I need?"

It tells you how and walks you through it (OAuth, API key, MCP, whatever) all in the same conversation.

**Step 2: Test it before moving on.**

Ask something that requires the tool to be connected to give a real answer:

- "What's on my calendar today?"
- "Find the last email from that client about the contract."
- "Pull the last 5 failed Stripe charges."

If you get a clean answer from the tool, it's live.

**Step 3: Stack them.**

Two tools are useful. Twelve tools are where the workflows above start working.

So go pick your favorites and connect them inside Hermes. Then go ask it to do one thing it couldn't do an hour ago.

**The first time it just does the thing, the chatbot dies and the superagent shows up.**

I'm building new Hermes automations every day, and always on the hunt for new inspiration, so if you have any loved workflows you've built, drop them below!

P.S. If you want highly practical AI workflows that help you get more customers and more views...

I send them to 37k readers every single week. Join here for free: [aisolo.beehiiv.com/subscribe](https://aisolo.beehiiv.com/subscribe)