---
type: source
title: Vadim Strizheus — $10k/mo Hermes clipping-pages agent (full guide)
created: 2026-05-21
updated: 2026-05-21
source_url: https://x.com/VadimStrizheus/status/2056410757063950634
source_type: x-thread
author: Vadim Strizheus (VadimStrizheus)
source_date: 2025-12-24
raw_path: raw/I built a Hermes Agent that makes $10kmo with clipping pages while I sleep (full-guide).md
content_status: substantive-verbatim
tags: [hermes-agent, clipping-pages, ai-automation-services, vugola, postiz, content-business, mcp-server]
---

# Vadim Strizheus — $10k/mo Hermes clipping-pages agent (full guide)

> Operational playbook for a **commercial Hermes Agent use case**: automated clipping pages. Hermes orchestrates **Vugola** (clip-extraction + captioning) and **Postiz** (multi-platform scheduling) via MCP. End user texts Hermes one message; Hermes calls Vugola → Vugola clips → Hermes hands clips to Postiz → Postiz posts across X/TikTok/IG/YouTube/Threads/LinkedIn/Bluesky. Market signal: clippers paid $1K/hr in late 2025 per Daniel Bitton; MrBeast pays $50 per 100K views to >1,000 clippers; Whop's clipping community has ~1M people generating 3.5B views/mo.

## TL;DR — the stack

| Component | Role | Cost |
|---|---|---|
| **[[wiki/entities/vugola|Vugola]]** | Clips long video into 30-60s clips; picks moments; adds captions. 8 MCP tools (clip_video / caption_video / schedule_post / etc.) | $14-21/mo |
| **[[wiki/entities/postiz|Postiz]]** | Schedules + posts clips to X / TikTok / IG / YouTube / Threads / LinkedIn / Bluesky / Reddit | Open-source self-hostable |
| **[[wiki/entities/hermes-agent|Hermes Agent]]** | Orchestrates the whole pipeline from one Telegram message | Free / MIT |

**One Telegram message →** *"Clip the latest Joe Rogan episode and schedule the 5 best clips to TikTok, Reels, and Shorts at 9am, 12pm, and 6pm CDT for the next 3 days."* → Hermes runs the whole flow.

## Market context (the *why now*)

- **Daniel Bitton's Content Rewards**: paid $50K to clippers in one week (Dec 2025); $1K/hr at peak; plan to hit $100K+/day.
- **Musa Mustafa**: $22K/mo from TikTok alone clipping Sneako (started at $3K/mo doing it for the creator).
- **MrBeast**: clipper army of >1,000 people; pays $50 per 100K views.
- **Adin Ross + N3on**: ~$1M/mo combined clipper payouts; one Adin Ross campaign hit 430M views across 11K videos from 520 clippers.
- **Anthony Fujiwara's Clipping.net**: 62K clippers; average $3K/mo.
- **Whop**: ~1M people in its free clipping community; 3.5B clipped views/mo.

## Volume is the catch

> *"To make real money you need 5 clips a day, 4 platforms, 3 accounts. That's 60 uploads a day, (some kids average 120). Nobody is doing that by hand. The people making $10k, $50k, $100k a month aren't faster editors. They built systems."*

This is the [[wiki/concepts/ai-automation-services|AI-automation-services]] thesis applied at the *consumer-content scale*, not B2B.

## Niche framing

- **Streamer clips** ($1-5 RPM): Adin Ross / N3on / Sneako / Kai Cenat / Clavicular.
- **Podcast clips** (evergreen): Rogan / Lex / Diary of a CEO / Theo Von / Shawn Ryan.
- **Hustle + finance** ($1.50-8 CPM on Content Rewards): Hormozi / Iman Gadzhi / Hamza.
- **Reddit story + fake text**: easiest to mass-produce.

Rule: *"Pick what you can watch 10 hours of without getting bored. You'll be near this content a lot."*

## Configuration (verbatim)

`~/.hermes/config.yaml`:

```yaml
mcp_servers:
  vugola:
    command: "npx"
    args: ["-y", "vugola-mcp@1.3.1"]
    env:
      VUGOLA_API_KEY: "vug_sk_yourkey"
  postiz:
    command: "postiz-mcp"
    env:
      POSTIZ_URL: "https://api.postiz.com"
      POSTIZ_API_KEY: "your-postiz-key"
      POSTIZ_ENABLE_WRITE: "true"
```

Vugola's 8 MCP tools: `clip_video / get_clip_status / caption_video / schedule_post / list_scheduled_posts / cancel_scheduled_post / download_clip / get_credits`.

Hermes install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash hermes setup`. *"Hermes ships with the harness already built in. Skills, memory, terminal, messaging gateways, all of it."*

## Notable quotes

> *"The market is paying. The only question is whether you're going to do it manually like everyone else, or build an agent that does it for you while you sleep."*

> *"Why Hermes and not the other harnesses? Hermes ships with the harness already built in."*

## How this composes with the wiki

- [[wiki/entities/vugola]] — *(new entity required)* clip-extraction + captioning AI. Pricing $14-21/mo; offers MCP server.
- [[wiki/entities/postiz]] — adds new evidence: Hermes-compatible MCP via `postiz-mcp`. Already in wiki as Marketing agent publish layer in Helm.
- [[wiki/entities/hermes-agent]] — third major source confirming Hermes's *commercial* viability beyond personal-productivity scope.
- [[wiki/concepts/ai-automation-services]] — adds the **consumer-content scale** (clipping pages, $10K/mo) alongside existing B2B-services coverage. Different unit economics (per-view vs per-retainer) but same systematic-leverage thesis.
- [[wiki/concepts/mcp-server]] — concrete Vugola MCP integration with 8 named tools; adds a Postiz MCP configuration example.

## Ethical note

The clipping economy itself is **ethically gray** in places — much of the value extraction is creator-paid (per-view rewards by streamers/podcasters who control the IP) but some is parasitic (unauthorized clips monetized by intermediaries). The wiki ingests the workflow because it's a real Hermes use case; **does not endorse** the business model in cases where IP rights aren't established. No `ethical_flag` set because Vadim's framing emphasizes the *authorized* / *creator-paid* market (Content Rewards, brand UGC deals). Worth a 1-line scope note if a future ingest extends this into clearer rights-violation territory.

## Mentioned entities

- [[wiki/entities/VadimStrizheus]] — *(new)* author.
- [[wiki/entities/vugola]] — *(new)* clip-extraction AI; offers MCP server.
- [[wiki/entities/postiz]] — already in wiki.
- [[wiki/entities/hermes-agent]] — already in wiki.
- [[wiki/entities/daniel-bitton]] — *(stub candidate)* Content Rewards founder.
- [[wiki/entities/mrbeast]] — *(stub candidate)* clipper-army operator.
- [[wiki/entities/whop]] — *(stub candidate)* free clipping community / 1M users.

## Related concepts

- [[ai-automation-services]] — consumer-content scale variant.
- [[mcp-server]] — Vugola MCP + Postiz MCP integrations.
- [[scheduled-automation]] — one-message Telegram trigger orchestrating multi-platform posting.

## Related sources

- [[wiki/sources/shannholmberg-hermes-agent-operator]] — operator framework Vadim's stack instantiates.
- [[wiki/sources/itsolelehmann-hermes-12-integrations]] — Postiz overlap; both endorse Postiz as the publish layer.
- [[wiki/sources/cyrilxbt-x-2052570518667378918]] — similar agent-orchestrated business pattern at B2B scale ($105/mo replacing $350K/yr).
