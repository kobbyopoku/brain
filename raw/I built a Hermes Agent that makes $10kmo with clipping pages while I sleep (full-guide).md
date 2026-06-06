---
title: "I built a Hermes Agent that makes $10k/mo with clipping pages while I sleep (full-guide)"
source: "https://x.com/VadimStrizheus/status/2056410757063950634"
author:
  - "[[@VadimStrizheus]]"
published: 2025-12-24
created: 2026-05-21
description: "Clippers are getting paid $1,000,000 a month right now.Not the streamers. The clippers.I built the agent stack to print clips while you slee..."
tags:
  - "hermes"
  - "hermes-agents"
  - "business"
  - "work"
  - "autonomy"
---
![Image](https://pbs.twimg.com/media/HInSmyoWcAAKHHM?format=jpg&name=large)

Clippers are getting paid $1,000,000 a month right now.

Not the streamers. The clippers.

I built the agent stack to print clips while you sleep. Clipping, captioning, scheduling, posting. All of it firing off one Telegram message. Here's the entire thing.

## This is already happening

Daniel Bitton paid out $50,000 to clippers in one week running Content Rewards.

> Dec 24, 2025
> 
> Update Over $1k an hour is being paid out to creators as we speak Nice way to start Christmas Plan is to get this to $100k + a day very soon All to capture organic mindshare for the biggest companies in the world with UGC & clipping Not slowing down

Musa Mustafa made $22,000 in one month from TikTok alone, without showing his face. He started by clipping Sneako for $3k/mo. Then he realized he could just do it for himself and keep all of it.

![Image](https://pbs.twimg.com/media/HIlO6DjXcAAB6lS?format=jpg&name=large)

MrBeast runs a clipper army of over 1,000 people. He pays $50 for every 100,000 views. Bloomberg covered it in October.

![Image](https://pbs.twimg.com/media/HIlPJ0xWEAAIRgr?format=jpg&name=large)

Adin Ross and N3on jointly burn around $1M a month on clipper payouts. One Adin Ross campaign hit 430 million views across 11,000 videos from 520 clippers.

Anthony Fujiwara runs [Clipping.net](https://clipping.net/). He says the average clipper on his platform makes $3,000/mo. He has 62,000 of them.

Whop has roughly 1 million people inside its free clipping community. They generate 3.5 billion clipped views per month.

A 14-year-old in Ohio turned a $200 laptop into $10,000 in two months slicing Twitch streams into 60-second clips.

The market is paying. The only question is whether you're going to do it manually like everyone else, or build an agent that does it for you while you sleep.

## What a clipping page actually is

It's very simple....

Take long videos from one creator or one niche. Cut them into 30 to 60 second clips.

Slap captions on and post them everywhere on IG, X, TT, and YT.

That's it.

The clips get views and then those views get paid.

Some platforms pay per view directly.

Some creators pay you to post their content.

Brands pay for UGC content, and the clipper sits in the middle of all these deals and collects.

The catch is volume.

To make real money you need 5 clips a day, 4 platforms, 3 accounts. That's 60 uploads a day, (p.s some kids average 120).

Nobody is doing that by hand. The people making $10k, $50k, $100k a month aren't faster editors. They built systems.

This is the system.

## The stack

Three AI tools, and the one agentic harness that ties them together.

**Vugola** clips your long video into bangers, picks the moments and adds captions.

**Postiz** schedules and posts the clips to every platform. X, TikTok, IG, YouTube, Threads, LinkedIn, Bluesky, and much more.

**Hermes Agent** from Nous Research is the brain and it runs the whole pipeline from one message.

That's the entire stack.

All you have to do is text Hermes from your phone:

"Clip the latest Joe Rogan episode and schedule the 5 best clips to TikTok, Reels, and Shorts at 9am, 12pm, and 6pm CDT for the next 3 days."

Hermes calls Vugola → Vugola clips → Hermes hands the clips to Postiz → Postiz posts them across all of your social media platforms.

<video preload="none" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/amplify_video_thumb/2056268160056082432/img/k9KR2GGJaeMTYP-q.jpg" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"><source type="video/mp4" src="blob:https://x.com/098c9a7d-2fa7-481a-bc30-9d3738e5e833"></video>

![](https://pbs.twimg.com/amplify_video_thumb/2056268160056082432/img/k9KR2GGJaeMTYP-q.jpg?name=large)

Now the Step-By-Step Guide

**Step 1. Pick your niche**

Pick one. Don't try to clip 5 creators on day one.

- **Streamer clips** pay the most ($1 to $5 RPM): Adin Ross, N3on, Sneako, Kai Cenat, Clavicular
- **Podcast clips** are evergreen: Rogan, Lex, Diary of a CEO, Theo Von, Shawn Ryan
- **Hustle and finance** has the highest brand-deal CPM ($1.50 to $8 on Content Rewards): Hormozi, Iman Gadzhi, Hamza
- **Reddit story and fake text** is the easiest to mass produce

Pick what you can watch 10 hours of without getting bored. You'll be near this content a lot.

**Step 2. Get your three API keys**

**Vugola.** Sign in at [vugolaai.com/dashboard/api-key](https://www.vugolaai.com/dashboard/api-key). Starter is $14/mo. Creator is $21/mo and gives you unlimited posting plus API access. Key looks like vug\_sk\_...

**Postiz.** Settings then Developers then Public API. Visit it here [Postiz](https://postiz.com/).

**Hermes Agent.** Free, MIT license, open source. [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

![Image](https://pbs.twimg.com/media/HIlZZ0lXAAAmTJz?format=jpg&name=large)

**Step 3. Install Hermes**

One line in your terminal.

curl -fsSL [https://hermes-agent.nousresearch.com/install.sh](https://hermes-agent.nousresearch.com/install.sh) | bash hermes setup

Pick a model provider on setup.

Why Hermes and not the other harnesses? Hermes ships with the harness already built in. Skills, memory, terminal, messaging gateways, all of it.

**Step 4. Wire Vugola into Hermes**

Open ~/.hermes/config.yaml and add this:

mcp\_servers: vugola: command: "npx" args: \["-y", "vugola-mcp@1.3.1"\] env: VUGOLA\_API\_KEY: "vug\_sk\_yourkey"

(or simply tell your Hermes agent here is the Vugola API key and pass it the md files)

Hermes can now call 8 Vugola tools: clip\_video, get\_clip\_status, caption\_video, schedule\_post, list\_scheduled\_posts, cancel\_scheduled\_post, download\_clip, get\_credits.

**Step 5. Wire Postiz into Hermes**

In the same config.yaml:

postiz: command: "postiz-mcp" env: POSTIZ\_URL: "[https://api.postiz.com](https://api.postiz.com/)" POSTIZ\_API\_KEY: "your-postiz-key" POSTIZ\_ENABLE\_WRITE: "true"

![Image](https://pbs.twimg.com/media/HIlSPtCW0AA_wuc?format=jpg&name=large)

**Step 6. Add the Postiz skill**

This is the one Nevo built for agentic workflows. It gives your agent a clean CLI that outputs structured JSON, designed for LLMs to parse.

npx skills add gitroomhq/postiz-agent export POSTIZ\_API\_KEY=your\_api\_key postiz integrations:list

If you see your connected socials listed, you're wired. Hermes can now run postiz posts:create, schedule across every platform, and pull analytics back.

**Step 7. Connect Hermes to Telegram**

hermes gateway add telegram

Follow the bot setup. Takes 60 seconds. You can also use Discord, Slack, WhatsApp, Signal, iMessage, or email. Hermes supports 14+ gateways. Telegram is the fastest.

**Step 8. Now send one message to fire the whole pipeline**

Open Telegram. Text your Hermes bot:

"Clip the latest Lex Fridman podcast. Pull the 5 best moments. Schedule them across TikTok, Reels, YouTube Shorts, and X at 9am, 12pm, and 6pm CDT, spread across the next 3 days."

Hermes plans. Calls Vugola. Polls until the clips are ready. Downloads them. Hands them to Postiz. Postiz schedules everything.

You get a Telegram confirmation when it's done. Usually 15 to 25 minutes for the whole flow.

![Image](https://pbs.twimg.com/media/HIlUJo7WoAAVzJ-?format=jpg&name=large)

## The first 30-day playbook

This is what separates the people who make $4k their first month from the people who make $40.

**Week 1. Test signal.** Run 3 clips/day across TikTok, Reels, and Shorts. Same content. Don't change the captions yet. You're looking at which platform your niche will gain traction.

**Week 2. Double down.** Whichever platform is winning, push to 5 clips/day there. Add account #2 in the same niche. Different angle. Different posting times.

**Week 3. Add the payout layer.** Sign up for Whop Content Rewards. Browse campaigns. Filter by your niche. Some campaigns are paying $2 CPM right now with zero follower minimum.

Sign up for Vyro (MrBeast's marketplace) and [Clipping.net](https://clipping.net/) while you're at it.

(maximize your chances of getting paid by entering multiple clipping campaign networks)

**Week 4. Scale or pivot.** If you're seeing real view counts, push to 3 accounts × 5 clips × 4 platforms = 60 posts/day. That's only possible because Hermes is doing it.

If you're not seeing views by week 4, your niche or your hook style is wrong.

Switch niches

## Things I'd tell my friend

The agent doesn't replace taste. It replaces labor.

You still pick the niche. You still write the hook style. You still decide which voice to clip. The agent just does the 4 hours of clicking that used to follow that decision.

The clipping economy is loud right now. Bloomberg covered it. The Verge covered it. TBPN just sold to OpenAI partly because of its clips. Everyone is about to flood in.

The window for the people who can run this stack is roughly 12 to 18 months before the platforms catch up or the payouts compress.

Don't try to clip 4 niches at once.

Pick one, grind on it for 30 days and then scale those social media accounts.

## The bigger lesson

The smartest move in the whole creator economy right now isn't building a brand from scratch.

It's clipping the creators who already have one. And building the agent that does it while you sleep.

Most clippers will keep doing it by hand. They'll edit one clip at a time. They'll cap out at $2k to $3k a month and burn out.

The ones who run agents will be doing the same volume in 20 minutes a day and stacking the payouts across 12 campaigns at once.

That's the game.

## Build the stack

**Vugola** → [vugolaai.com](https://www.vugolaai.com/)

The clipping agent. Drop in a long video, get 10 clips back with captions already baked in. Starter is $14/mo. Creator is $21/mo and gives you the API. This is the part that replaces your editor.

**Postiz** → [postiz.com](https://postiz.com/)

If you're serious about scaling, this is the one I'd bet on. Postiz is the scheduler the open source world is moving to. 25+ platforms from one dashboard. Public API. MCP server. Nevo built it for people who post like it's their job. Self-host it for free or grab the hosted plan and skip the setup. Get your API key today and your agent can keep posting for you forever.

→ [Get Postiz](https://postiz.com/). The only scheduler with a real agent skill built in.

**Hermes Agent** → [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)

The brain. Free, open source, MIT. 57K GitHub stars in 6 weeks. Ties Vugola and Postiz together so one Telegram message runs the whole thing.

## Don't want to wire it up yourself?

Vugola ships the agent stack inside the app. Plug your Postiz key in, point it at a long video, you're posting in 4 minutes. No config files. No terminal.

→ [Start at vugolaai.com](https://www.vugolaai.com/) Follow me for breakdowns like this.

[@VadimStrizheus](https://x.com/@VadimStrizheus)