---
title: "My Claude Code OS Runs my $3M/yr Business. Steal This."
source: "https://x.com/nateherk/status/2050116705322512766"
author:
  - "[[@nateherk]]"
published: 2026-05-01
created: 2026-05-02
description: "Frameworks. Repo anatomy. Connections. Skills. Routines. Wikis. Mindset shifts. Every gotcha I hit along the way.By the end of this article,..."
tags:
  - "ai"
  - "ai-os"
  - "automation"
  - "claude"
  - "business"
---
![Image](https://pbs.twimg.com/media/HHN2NB2W4AAo089?format=jpg&name=large)

Frameworks. Repo anatomy. Connections. Skills. Routines. Wikis. Mindset shifts. Every gotcha I hit along the way.

By the end of this article, you'll know exactly how to build your own AI Operating System inside Claude Code, even if you've never opened it before.

## Why an AI OS in the First Place

An OS is the layer between you and your computer. macOS. Windows. iOS.

An AI OS is the same idea with intelligence on top.

It sees all your files. It touches your tools. It remembers better than you do. It can pull from the exact source faster than you can.

I'm not exaggerating when I say I could spend an entire workday with Claude Code open and still get more done than someone clicking through 30 different apps.

The reason this works is the four Cs sitting underneath it.

1. Context
2. Connections
3. Capabilities
4. Cadence

Once those four are in place, the OS runs in the background while your laptop is closed.

![Image](https://pbs.twimg.com/media/HHN489IXcAAQrGp?format=jpg&name=large)

Tools change every six months. Models get deprecated. SDKs get retired. The Three Ms and the Four Cs don't. That's the durable layer this whole article is about.

## The Three Ms of AI™

Three habits to internalize before you touch the repo.

1️⃣ The Default Shift

→ Before any task, ask "how could AI do this, or at least 30 percent of it?"

→ I had to update 300+ YouTube descriptions last month. Old me would have clicked through every video. New me brainstormed with Claude Code, found an API path, done in minutes.

2️⃣ The Function Breakdown

→ Your role is a tree of tasks. A YouTube video isn't one job. It's ideation, scripting, packaging, descriptions, comment replies, and more.

→ You don't automate a YouTube video. You automate one chunk at a time. Each chunk is reusable across other workflows.

3️⃣ The Curiosity Rule

→ Never accept AI output without asking why.

→ Treat AI as a mentor, not a vending machine. Mentors push back, ask questions, sharpen you. Vending machines just take a coin.

Here's the part nobody warns you about. Productivity drops before it climbs.

When you make a real change, expect a 20 percent dip for the first few days. The question isn't "will this be hard." It's "is the dip worth the 50 percent gain on the other side."

![Image](https://pbs.twimg.com/media/HHN3ZQaW0AAS48s?format=jpg&name=large)

Most people quit during the dip. Don't.

## The Four Cs of an AI OS™

This is the practical framework. The order matters.

→ Context: what AI knows about you, your team, your tools, your voice, your money

→ Connections: what data it can reach

→ Capabilities: what it can produce

→ Cadence: when it acts on its own while you sleep

You can't have cadence without connections. You can't have capability without context. Build them in order. One, two, three, four.

Easy test. Open a new Claude session. Ask it a real business question. Does it answer like a teammate or like a stranger who met you five seconds ago?

If it's the stranger, you have zero context. Start there.

## Map Your Tools Before You Touch the Repo

Before you open VS Code, sketch this on paper.

Seven tier-one domains:

→ Revenue

→ Customer

→ Calendar

→ Comms

→ Tasks

→ Meetings

→ Knowledge

For each one, write down where the data actually lives.

An example of what this could look like:

→ Revenue: Skool, Stripe, QuickBooks

→ Customer: Skool, YouTube

→ Calendar: Google Workspace

→ Comms: Google Workspace, ClickUp, Slack

→ Tasks: ClickUp, Notion

→ Meetings: Fireflies

→ Knowledge: YouTube transcripts, Google Workspace, local files

This sketch becomes your connections roadmap. Every tool here will eventually need an API key, an MCP, or a CLI bridge into Claude Code.

If you can't see all your business in one diagram, your AI OS won't either.

## Inside the Starter Repo

I built a Claude Code template that lives on GitHub. You clone it, open it in VS Code, and you're set up in five minutes.

[https://github.com/nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS)

Here's what's in it and why each folder matters.

![Image](https://pbs.twimg.com/media/HHN30qyWYAAfytY?format=png&name=large)

→ .claude/skills: where every reusable recipe lives. Ships with three skills out of the box: Audit, Level Up, and Onboard.

→ Archives: where Claude moves old documents you don't actively need. Don't delete, archive.

→ Contexts: where Claude builds out files like About Business, About Me, and Priorities. This is the Context C.

→ Decisions: an append-only log of meaningful decisions. When something matters, it gets a date, a reasoning, and a context entry.

→ References: external knowledge. The Three Ms doc lives here. Tool API references live here. SOPs live here.

→ claude.md: the master prompt for the entire project. It tells Claude who you are, how the folders work, when to invoke which skill, and where things live.

→ .env: your secret file. API keys go here, never in chat. Listed in .gitignore so it never gets pushed publicly.

The claude.md is the file that evolves the most. Mine gets updated two times a day. As you add new folders, new skills, new connections, this file gets the source-of-truth update so Claude actually knows your project.

## The Onboarding Skill (Day One)

You clone the repo, open it in VS Code, double-click Claude Code, and just say "I want to set up my AI operating system. Help me get onboarded."

It invokes the Onboard skill. Seven-question interview. By the end you have an About Me, About Business, Priorities, and a voice sample on disk.

Tip: don't type two-sentence answers. Use a voice tool like Glaido and dump three paragraphs into each answer. The richer the context, the better every future answer.

After onboarding, ask "what should I focus on this week?" and watch it pull from the three files it just wrote. That's your first proof the loop works.

## Connecting Tools the Right Way

Day two is connections. Here's the order I learned the hard way.

1️⃣ Make a separate account for your AI OS

→ Don't give Claude Code your personal API key with full permissions.

→ I made an account called Up at AI inside ClickUp and only gave that account's API key to Claude.

→ Same for Stripe, QuickBooks, anywhere it touches money.

→ Separate keys also let you see which automation is spending what.

2️⃣ Prefer API endpoints over MCP servers

→ MCPs load every endpoint and every function whether you need it or not. That eats tokens.

→ Tell Claude: "Use the API directly. Research the docs once, save them as a markdown reference, and pull from that file when you need an endpoint."

→ Markdown is cheap to read. API docs are expensive to crawl every time.

3️⃣ Store keys in .env, never in chat

→ Tell Claude to create the .env file with placeholders.

→ You paste the keys in the file and save. Never paste them into the chat history.

4️⃣ Default to bypass permissions only after you trust it

→ Plan mode is for brainstorming. Auto mode lets it do safe stuff and ask before risky stuff. Bypass lets it do everything.

→ I run on bypass. Has it deleted things? Yes. Only when I asked it to.

But here's the thing. The first time a connection fails, treat it as a gift.

Ask Claude to update the relevant API doc or skill so the same failure can never happen again. Every failure becomes permanent learning if you build the loop.

## Skills Are Where the Real Leverage Lives

Skills are reusable SOPs for your AI agents. Same way you'd train a human with an SOP, you train Claude with a skill.

A skill is just a folder. .claude/skills/skill-name/skill.md.

The skill.md has YAML front matter at the top with a name and description. Below it, the step-by-step instructions. That's it.

Anatomy of a skill:

→ Name and description: required, used by Claude to find the skill

→ Step-by-step rules: the actual SOP

→ Reference files: brand guidelines, tone, target avatars, anything heavy

→ Scripts: optional Python or JS that the skill can call

Reference files don't have to live nested under the skill folder. They can live in /references and the skill points to the path. Use whichever feels cleaner.

How Claude knows when to use a skill: progressive context loading.

→ Level 1: scan all skill front matter. Roughly 100 tokens per skill. Cheap.

→ Level 2: load the full skill.md if it picks one. Couple thousand tokens.

→ Level 3: only pull reference files when the task actually needs them.

That's why skill.md should stay under 500 lines and reference docs should be separate.

The six-step skill-building framework:

1️⃣ Name and trigger (slash command, natural language, or both)

2️⃣ Goal in one sentence (what's the output)

3️⃣ Step-by-step process (what you'd do manually, in order)

4️⃣ Reference files (what context does it need)

5️⃣ Rules and guardrails (what could go wrong)

6️⃣ The improvement loop (after you run it, update it)

Here's what stood out from my own skills.

The Pulse Check skill used to call the ClickUp MCP and search every list ID every time. Slow. Wasteful. So I hardcoded the list IDs into the skill.md itself. Now it knows them instantly.

It also delegates to a sub-agent called clickup-searcher so the heavy ClickUp data never blows the main context window.

That's the difference between a skill that runs and a skill that runs well. You watch it work the first few times. You patch the obvious waste. You move on.

The feedback cycle is the real unlock. Run it, watch it, give feedback, fix it, run it again. By the tenth run, the skill is sharp. By the thirtieth, it's part of how your business runs.

## Skills Live Two Places

Project-level: .claude/skills inside a specific repo. Only that project sees them.

Global: ~/.claude/skills in your home directory. Every Claude Code session can reach them.

I install front-end design as a global skill so it's there in any project. I keep business-specific skills in the Herk 2 repo so they only fire where they matter.

## Audit and Level Up: The Built-in Improvement Loop

The starter repo ships with three skills. Onboard you already met. The other two are how the OS keeps getting sharper without you having to think about what to build next.

1️⃣ Audit

→ Run /audit any time you feel stuck or want a checkup.

→ It scores your AI OS out of 100 across the four Cs: context, connections, capabilities, cadence.

→ Returns your top three gaps, ranked by leverage, not alphabetically.

→ Saves every audit so you can track your score climbing over time.

![Image](https://pbs.twimg.com/media/HHN40-GXEAALx0j?format=png&name=large)

The first time I ran it, I got 54.5 out of 100. One day in. That's the right kind of honest.

2️⃣ Level Up

→ Run /level-up after the audit when you want capability gaps, not structural ones.

→ It pulls from your priorities, your connections, and what's reachable right now, then asks five questions:

→ Walk me through this past week. What did you do three or more times?

→ Drudgery. Anything manual, boring, or copy-paste?

→ Smart intern test. Anything a smart intern could absolutely handle that you did yourself because explaining it would take longer?

→ Constraint. If 500 new community members showed up Monday, what would break first?

→ Growth lever. What would give you 500 more clients tomorrow if it ran on autopilot?

![Image](https://pbs.twimg.com/media/HHN45kcWEAABJq7?format=png&name=large)

Answer those five and there's no way you're stuck. Every answer surfaces a skill to build, an automation to run, or a connection to add.

The pair is the engine. Audit finds where the foundation is thin. Level Up finds where the next leverage point is hiding. Run them weekly and the OS improves on its own cadence.

## Cadence: Where It Becomes a 24/7 Employee

Capabilities make Claude useful when you ask. Cadence makes it useful when you don't.

Three options that matter.

1️⃣ Cloud Routines

→ Anthropic infrastructure. Your laptop can be off.

→ Triggered by schedule, API call, or GitHub event.

→ Pro plan: 5 runs a day. Max plan: 15. Team and Enterprise: 25.

2️⃣ Local Scheduled Tasks

→ Run on your machine, in the desktop app.

→ Catch up if you missed a run.

→ Need the app open and the computer awake.

3️⃣ Loop

→ One-off recurring runs inside a single session.

→ Three-day expiry, then auto-deletes.

→ Great for "every five minutes check if my deploy is done." Wrong for weekly recurring jobs.

Here's where Cloud Routines bite people. The gotcha list:

→ Routines run from a cloned GitHub repo. No local file access. If your skill needs a local file, the routine can't see it.

→ Your .env never gets pushed to GitHub (it's gitignored). So routines can't read your API keys from .env. You have to put them in the routine's cloud environment variables instead.

→ You also have to tell the prompt explicitly: "use the API key from the environment variable, don't look for a .env." Otherwise it'll try to read .env, fail, and stop.

→ Network access defaults to "trusted." That only allows known Anthropic-vetted domains. If you need ClickUp or anything else, switch the cloud environment to "full" access. There's a small risk if your inputs are untrusted, but for private repos with controlled inputs, it's fine.

→ Each run is stateless. The cloned repo gets destroyed after the run finishes. Anything that depends on cookies or local session state won't work.

→ Minimum interval is one hour. Loop and local tasks can go faster.

→ Don't push a massive 200MB repo into the cloud just to run a small routine. Spin up a smaller dedicated repo per routine if context is heavy.

Routines basically inject a prompt into a real Claude Code session. The same prompt you'd type yourself. So write specific, one-shot prompts. The routine isn't going to stop and ask clarifying questions for you.

## The LLM Wiki Layer (Karpathy's Idea)

This is the unlock most people miss.

Andrej Karpathy posted about using LLMs to maintain personal knowledge bases. No fancy RAG. No embeddings. No vector DB.

Just a folder with markdown files, an index file, and a log file.

The structure:

→ /raw: the source documents (transcripts, articles, meeting notes)

→ /wiki: the organized output (concepts, entities, sources, analysis)

→ /wiki/\_index.md: the master index

→ /wiki/\_log.md: append-only operation history

→ /wiki/\_hot.md: a 500-token cache of what was most recently active

You drop a file into /raw and tell Claude "ingest this." It reads the source, creates wiki pages, builds backlinks between concepts, updates the index, logs the operation. Done.

I have two of these vaults running right now.

→ One is my YouTube transcripts vault. 36+ video transcripts ingested. I can ask any question about my own content and it answers from the wiki, not from a vector search.

→ One is my Herk Brain vault. My personal second brain. Meeting notes, business decisions, priorities, the works.

Why this matters: one X user moved 383 scattered files and 100+ meeting transcripts into a wiki and dropped token usage by 95 percent on queries.

It also kills the "I forgot which Slack thread that was in" problem. The wiki has the source link, the date, the entity references, all in one place.

Pair it with Obsidian if you want a visual graph view. Obsidian is just a markdown viewer, it changes nothing about how Claude reads the files. But the visual layer helps you spot relationship clusters you didn't know were there.

The hot cache is the move I'd missed. A small 500-token file at the top of the wiki that captures the active state of your week. Claude reads it first, before crawling the bigger wiki. Saves a ton of tokens on repeat queries.

## Mindset Shifts You'll Need

Building the OS is half technical, half psychological. The technical part is easy. The mindset part is where most people stall.

→ Default Shift: assume AI does it first. Manually do it only as a last resort.

→ Function Breakdown: every job is a tree of tasks. Automate the leaves first, not the trunk.

→ Treat AI as a mentor: don't ask "do this for me." Ask "should I do this, what would you do differently."

→ Never binary: the question is never "can AI do this?" It's "to what percentage."

→ Productivity drops before it climbs: take the 20 percent dip seriously. The 50 percent gain is on the other side.

→ Failure is data: every broken run becomes a skill update or a reference doc update. Nothing breaks twice.

→ POC mindset: Proof of Concept first. Build the cheapest version. If it proves out, then dedicate real resources. I built dashboards as Claude Artifacts before ever investing time into a custom dashboard.

→ Per-account permissions: separate API keys per agent or per service. Restrict scope. Read-only where possible. Audit which automation is spending what.

→ Boring is beautiful: deterministic workflows beat AI agents nine times out of ten. Most business processes don't need autonomy. They need a Python script that runs on a cron.

## Daily and Weekly Loops

Daily:

→ Morning: ask Claude to plan your day. If the plan is bad, write down what context it was missing. Patch tomorrow.

→ End of day: which skills did you use, which prompts did you have to repeat, what did you have to correct.

Weekly:

→ Friday: run /audit, then /level-up. Pick one gap from each, build it next week.

→ Repeat.

That's the whole rhythm. The OS doesn't need a manager. It needs a loop.

## Success Criteria for an AI OS

Not KPIs. Subjective signals that it's working.

1️⃣ Your team would rather message your AI OS than message you (because it has better memory and never sleeps)

2️⃣ You stop opening browser tabs (because most of your work happens inside Claude Code)

3️⃣ Knowledge leaves your head (because it lives in the wiki, the contexts folder, and the skills)

If even two of three are true within a month, the system has taken.

## Wrap

The whole thing is just folders, markdown files, and a few API keys.

The frameworks make it durable. The repo gives you a starting point. The skills make it leverageable. The cadence makes it autonomous. The wiki makes it permanent.

Tools change. Models change. The Three Ms™ and the Four Cs™ don't.

I walk through every step of this build live in the full video. Link in the first reply.