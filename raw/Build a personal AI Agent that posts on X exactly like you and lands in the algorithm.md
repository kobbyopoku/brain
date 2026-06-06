---
title: "Build a personal AI Agent that posts on X exactly like you and lands in the algorithm"
source: "https://x.com/doublenickk/status/2055719881493123275"
author:
  - "[[@doublenickk]]"
published: 2026-05-16
created: 2026-05-21
description: "X just open-sourced the algorithm that powers the For You feedI read every line of it, then built an agent with Claude Code that generates..."
tags:
  - "agent"
  - "agents"
  - "personal-os"
  - "x"
  - "personal-ai"
---
![Image](https://pbs.twimg.com/media/HIdUnDWXEAA9ak6?format=jpg&name=large)

X just open-sourced the algorithm that powers the For You feed I read every line of it, then built an agent with Claude Code that generates posts in my voice, optimized for every signal the algorithm actually measures > Here's how you do the same:

![Image](https://pbs.twimg.com/media/HIcbIUCXwAAUY83?format=jpg&name=large)

Most content advice about X is fiction: - post consistently - engage with your niche - use hashtags None of it is based on how the algorithm actually works, because until recently, nobody knew.

That changed when xAI open-sourced the entire For You feed recommendation system at → [github.com/xai-org/x-algorithm](https://github.com/xai-org/x-algorithm). • not a blog post about the algorithm • the actual source code The exact pipeline that decides which posts get shown to people who don't follow you and which ones disappear into the void.

I spent a week reading it. Then I built a Claude Code agent that uses what I learned to generate posts in my voice, optimized for the specific engagement signals the algorithm measures. > This article is everything I know about how to do the same!

## The Code Nobody Read

The X algorithm repository contains four main components: → Home Mixer (the orchestration layer) → Thunder (in-network post retrieval) → Phoenix (the ML ranking model) → Candidate Pipeline framework Together they form a recommendation system that predicts the probability of fourteen different user actions for every post it considers showing you.

Here is the critical insight buried in the scoring code:

> **\> From phoenix/scoring the actual weighted score formula** Final Score = Σ (weight\_i × P(action\_i)) The algorithm predicts probabilities for 14 actions, then multiplies each by a weight and sums them Positive actions push your post up. Negative actions push it down. The weights are not public, but the actions are

This matters because it completely changes how you should think about content strategy. The algorithm is not looking for (engagement) as a single number. It is predicting fourteen specific behaviors and scoring each one differently. **The 14 signals → what they mean for your content >** Reply ( ↑ **High Weight** )

Replies signal genuine interest. Content that provokes thought, disagreement, or questions drives replies. Open-ended posts outperform declarative ones. > Repost ( ↑ **High Weight** )

Reposts signal "I want my audience to see this." Useful, novel, or validating content drives reposts more than personal updates. > Favorite ( ↑ **Medium Weight** )

Likes are the lowest-friction signal. They matter, but they are weighted below replies and reposts in the scoring model. > Follow\_author ( ↑ **Very High Weight** )

A post that makes someone follow you is the highest positive signal. Content that clearly demonstrates a unique perspective or valuable expertise drives this. > Click ( ↑ **Medium Weight** )

Profile clicks suggest curiosity about the author. Strong voice and consistent positioning drive this signal over time. > Dwell ( ↑ **Medium Weight** )

Time spent reading the post without interaction. Long-form threads and posts that reward reading score well here. > Not\_interested ( ↓ **High Penalty** )

The "Not interested" tap is a strong negative signal. - bait-and-switch content - off-topic posts - low-quality reposts trigger this > Mute\_author ( ↓ **High Penalty** )

Mutes suggest the content is annoying but not worth reporting. - repetitive - low-value - over-promotional content drives this > Block\_author ( ↓ **Very High Penalty** )

The strongest negative signal short of a report. Aggressive, spammy, or deeply off-putting content triggers this. > Report ( ↓ **Severe Penalty** )

A report is the nuclear option. Even a small number of reports tanks distribution immediately and triggers visibility filtering.

> **KEY INSIGHT FROM THE SOURCE CODE** The algorithm has eliminated every hand-engineered feature The Grok-based transformer learns relevance entirely from your engagement history: • what you liked • replied to • shared • dwelled on This means: **CONSISTENCY OF TOPIC AND STYLE** trains the algorithm to show your content to people with matching engagement histories Inconsistency confuses the model

There is one more critical mechanic from the code: the Author Diversity Scorer. It attenuates your score each time the algorithm has already shown one of your posts to the same user in the current session. This means posting frequency matters, but flooding your audience with content in a short window actively hurts your distribution per post.

## The Problem With Manual Posting

you know your voice... you know your audience... you know roughly what performs... The problem is time, consistency, and the cognitive load of simultaneously being creative and analytical about every post you write. > A personal AI agent that knows your style solves this differently than a generic AI writing tool. The difference is memory and pattern: a generic tool produces content. • A personal agent produces your content calibrated to the specific signals the algorithm rewards, in the voice your existing audience has come to recognize.

Before building anything, you need to answer one question: > what does your pattern actually look like?

**YOUR PATTERN ANALYSIS PROMPT** → **RUN THIS IN CLAUDE CODE FIRST**

![Image](https://pbs.twimg.com/media/HIbv4dGXEAAUSr0?format=jpg&name=large)

Run this before building anything. The Voice Style Guide this produces is the most important document your agent will use. Everything else is scaffolding around it.

## Pick the Architecture That Fits Your Workflow

There is no single \[ correct \] personal X agent. The right architecture depends on how much control you want to retain, how technically comfortable you are, and how automated you want the pipeline to be. Here are three complete blueprints, from most accessible to most powerful. > **BLUEPRINT 01**

The Session Agent → Claude Code + MEMORY.md

The simplest architecture that actually works. • You run Claude Code in a terminal with a pre-configured MEMORY.md file containing your Voice Style Guide and algorithm context. Each session, Claude reads your memory and generates posts without you re-explaining anything. **\> WHAT YOU BUILD**

A CLAUDE.md project file that loads your voice, your topic positioning, and the algorithm's scoring priorities every time you open a Claude Code session in that directory. - Zero infrastructure - No API keys beyond Claude itself

![Image](https://pbs.twimg.com/media/HIbwT0ZW4AA_DrV?format=jpg&name=large)

**THE DAILY WORKFLOW**

Open Claude Code in your project directory. Type your idea or topic in one sentence. Get three post variants with a thread and single-post version of each. Pick the one that feels right, edit it to match your current voice, and post it manually. Total time: 8 minutes per post instead of 45.

![Image](https://pbs.twimg.com/media/HIdVrELXsAEgC7I?format=jpg&name=large)

\+ Zero infrastructure required + Full control, you approve every post + Voice quality is highest with human review - Manual posting — no scheduling - Requires you to open Claude Code each time **\> BLUEPRINT 02**

The Approval Pipeline → Claude Code + Queue + Telegram

A semi-automated system that generates batches of posts, sends them to you for approval via Telegram, and publishes approved content on schedule via the X API. You stay in the loop on every post but stop spending time on generation entirely. **\> ARCHITECTURE OVERVIEW**

Three components work together: 1. Claude Code agent that generates weekly post batches every Sunday evening 2. Telegram bot that delivers drafts to your phone for one-tap approval or rejection 3. Scheduler that posts approved content at algorithm-optimal times

![Image](https://pbs.twimg.com/media/HIbw3L6XwAAUfjT?format=jpg&name=large)

![Image](https://pbs.twimg.com/media/HIbw-TsXsAEOusp?format=jpg&name=large)

**OPTIMAL POSTING TIMES → ALGORITHM CONTEXT**

The algorithm's Thunder component retrieves posts from followed accounts in real-time. Your post's first hour of engagement is the primary signal that determines whether it gets served out-of-network. Schedule posts when your most engaged followers are active, check your X Analytics for your specific audience's peak hours. > Generally: Tuesday–Thursday, 8–10 AM or 6–8 PM in your audience's primary timezone. + You approve every post, quality stays high + Scheduling handles algorithm timing automatically + Weekly batch generation, 30 minutes of your time per week - Requires Telegram bot setup and X API access - X API has posting limits on free tier **\> BLUEPRINT 03**

The Autonomous Stack → Multi-Agent with Feedback Loop

A fully autonomous system with three specialized agents: a Content Agent that generates posts, an Analytics Agent that reads your X performance data and identifies what's working, and an Optimization Agent that continuously updates your Voice Style Guide based on real engagement results. The system learns and improves every week without manual intervention!

**THE THREE-AGENT ARCHITECTURE**

![Image](https://pbs.twimg.com/media/HIbxMnGXcAAvWlv?format=jpg&name=large)

**THE FEEDBACK LOOP → WHAT MAKES THIS DIFFERENT**

Most content systems optimize for what feels good to write. This system optimizes for what the algorithm actually rewards, measured weekly against real data. The Optimization Agent reads your engagement metrics and updates the Voice Style Guide with specific, evidence-based changes: \[ Posts ending with a direct question received 3.2x more replies than posts ending with a statement \] > Update guide: add question to 70% of posts

![Image](https://pbs.twimg.com/media/HIbxVSLWAAAwXut?format=jpg&name=large)

\+ Fully autonomous, zero daily effort once running + Self-improving, gets better every week from real data + Scales to any volume without additional time investment - Requires X API elevated access for analytics data - Risk of voice drift if not reviewed monthly - Significant initial build time, 1 full week minimum

## What to tell your agent and what to never let it do

Understanding the algorithm source code reveals specific rules that most content advice gets completely wrong. Build these directly into your agent's instructions. **\> RULES YOUR AGENT MUST FOLLOW 1. No hashtags** The algorithm's Phoenix model learns relevance from your engagement history and content semantics, not from hashtags. Hashtags are a signal of low-effort content and do not improve distribution. - Remove them from your agent's output entirely. 2. **Topic consistency is algorithm training** The Grok transformer learns your content type and matches it to users with compatible engagement histories. Posting off-topic content confuses this matching. Your agent should refuse to generate posts outside your defined topic scope.

**3\. Replies window matters** The algorithm's in-network component (Thunder) surfaces posts to your followers in near-real-time. But out-of-network distribution (Phoenix) depends on your in-network engagement rate in the first hour. Post when your most engaged followers are active, not when it's convenient for you.

**4\. Dwell time is a measured signal** P(dwell) is explicitly in the scoring model. Posts that reward reading, with a non-obvious payoff, a narrative structure, or layered information, score better than posts you can absorb in two seconds.

**5\. The follow signal is the highest positive weight** Content that clearly demonstrates a unique point of view or a specific expertise that's hard to find elsewhere drives P(follow\_author). Your agent should optimize at least one post per day specifically for this signal. **\> WHAT TO NEVER LET YOUR AGENT DO 1. Never auto-post without a review gate** Even the best-configured agent will occasionally generate content that misses your voice. Always have a human in the approval loop, even if it's just a one-tap Telegram review.

**2\. Never generate engagement bait \[** Agree or disagree? \] and \[ What do you think? \] are low-signal prompts that generate low-quality replies. The algorithm can distinguish between substantive replies and one-word reactions.

**3\. Never let it drift from your voice** The most common failure mode of AI content agents is gradual voice homogenization, the output slowly converges toward a generic AI tone. Review your Voice Style Guide monthly and compare it against what the agent is actually producing.

**4\. Never optimize for a single signal** The algorithm uses a weighted sum of fourteen signals. Content that maximizes one \[ like controversy for replies \] at the expense of others \[ triggering not\_interested or report \] will be net-negative. - Your agent should optimize for a portfolio of positive signals.

> \> the algorithm doesn't care how hard you worked on a post > it measures fourteen specific behaviors and scores each one > your agent should know all fourteen

## Why Most AI Content Sounds Like AI Content

The failure mode everyone worries about \[ the content will sound like AI \] → is real. But it is not inevitable. It happens because of one specific mistake: - the agent is given a topic, not a pattern.

Telling an agent \[ write about AI tools \] produces generic AI content about AI tools. Telling an agent write about AI tools in the voice of someone who is fundamentally skeptical of hype, uses concrete examples exclusively and ends every post with a question that implies a contrarian answer produces something that sounds like you.

The difference is specificity of constraint. The more precisely your Voice Style Guide captures your actual patterns, not just your topics, the more recognizable the output will be.

**THE VOICE PRESERVATION PROMPT → RUN WEEKLY**

![Image](https://pbs.twimg.com/media/HIbx1v6WEAEVcof?format=jpg&name=large)

Run this comparison every week for the first month. By week four, the gap between agent output and your natural voice will be narrow enough that your approval process becomes fast and the edits become minimal.

## The Metrics That Actually Matter

Most people measure follower growth and total impressions. Neither of these tells you whether your agent is hitting the algorithm signals that drive out-of-network distribution. **\> Here are the metrics worth tracking:**

\[ weekly agent performance review \] Track these numbers every Monday before your agent generates the next batch: 1. Reply rate (replies ÷ impressions) → target: above your baseline before agent 2. Follow rate (new follows from non-followers per post) → the highest-value signal 3. Out-of-network impression ratio (% of impressions from non-followers) → measures For You feed penetration 4. Profile click rate → signals content creating curiosity about you specifically 5. Not interested / mute rate → if this rises, your agent is drifting toward generic content Feed these numbers into your Analytics Agent every week. They are the signal that drives the optimization loop.

One number deserves special attention: the out-of-network impression ratio. This is the clearest signal that the Phoenix retrieval system \[ the ML model that discovers posts from the global corpus \] is serving your content to people who don't follow you. A ratio above 40% means the algorithm is actively distributing your posts to new audiences. • Below 20% means you are almost entirely dependent on your existing following for reach.

Your agent's algorithm optimization, the reply hooks, the follow-driving posts, the dwell-time-rewarding content, is specifically designed to push this ratio up. > Track it weekly If it's not moving, the agent's output needs recalibration against the Voice Style Guide and algorithm context.

\> Thanks for reading!