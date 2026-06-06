---
title: "The anatomy of ~/.hermes folder."
source: "https://x.com/akshay_pachaar/status/2055629943891988719"
author:
  - "[[@akshay_pachaar]]"
published: 2026-05-13
created: 2026-05-21
description: "the anatomy of ~/.hermes folder. one folder controls everything your hermes agent knows, remembers, and can do. understanding its layout is"
tags:
  - "hermes"
---
the anatomy of ~/.hermes folder.

one folder controls everything your hermes agent knows, remembers, and can do. understanding its layout is the difference between treating hermes as a black box and actually customizing it.

here's what lives inside and why each piece matters.

𝗰𝗼𝗻𝗳𝗶𝗴𝘂𝗿𝗮𝘁𝗶𝗼𝗻

𝗰𝗼𝗻𝗳𝗶𝗴.𝘆𝗮𝗺𝗹 is the source of truth for everything non-secret: model choice, terminal backend, tool enablement, MCP servers. 𝗲𝗻𝘃 holds your API keys and bot tokens. 𝗮𝘂𝘁𝗵.𝗷𝘀𝗼𝗻 stores OAuth credentials.

then there's 𝗦𝗢𝗨𝗟.𝗺𝗱. it occupies slot #1 in the system prompt, before anything else loads. it defines who the agent is: personality, tone, communication style, hard limits. everything the agent writes, creates, and remembers passes through this identity layer.

𝗸𝗻𝗼𝘄𝗹𝗲𝗱𝗴𝗲

𝗺𝗲𝗺𝗼𝗿𝗶𝗲𝘀/ contains two tiny files. 𝗠𝗘𝗠𝗢𝗥𝗬.𝗺𝗱 (2,200 chars) holds project conventions, tool quirks, lessons learned. 𝗨𝗦𝗘𝗥.𝗺𝗱 (1,375 chars) holds your profile.

both get injected into the system prompt as frozen snapshots at session start. when they fill up, the agent consolidates: merges entries, drops redundancy, keeps only what's dense and useful.

𝗰𝗮𝗽𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀

𝘀𝗸𝗶𝗹𝗹𝘀/ is where the learning loop lives. each skill is a self-contained ability: a 𝗦𝗞𝗜𝗟𝗟.𝗺𝗱 (the procedure), a 𝗿𝗲𝗳𝗲𝗿𝗲𝗻𝗰𝗲𝘀/ folder (docs the agent reads), and 𝘀𝗰𝗿𝗶𝗽𝘁𝘀/ (executable helpers).

skills come from three sources: bundled with hermes, downloaded from the hub via 𝗵𝘂𝗯/, or created by the agent itself during your sessions. hermes ships with 687 skills across 18 categories, and you can add any GitHub repo as a custom tap.

𝗿𝘂𝗻𝘁𝗶𝗺𝗲 𝘀𝘁𝗮𝘁𝗲

𝘀𝗲𝘀𝘀𝗶𝗼𝗻𝘀/ stores per-platform session metadata. 𝘀𝘁𝗮𝘁𝗲.𝗱𝗯 is the SQLite database with FTS5 indexing that backs tier 2 memory. this is what makes "what did we discuss three weeks ago?" actually work across CLI and messaging.

𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗼𝗻

𝗰𝗿𝗼𝗻/ holds scheduled jobs in 𝗷𝗼𝗯𝘀.𝗷𝘀𝗼𝗻 and their outputs in 𝗼𝘂𝘁𝗽𝘂𝘁/. the gateway daemon ticks every 60 seconds and runs due jobs in isolated sessions. you describe schedules in plain English, hermes converts them.

𝗲𝘅𝘁𝗲𝗻𝘀𝗶𝗼𝗻 + 𝗼𝗯𝘀𝗲𝗿𝘃𝗮𝗯𝗶𝗹𝗶𝘁𝘆

𝗽𝗹𝘂𝗴𝗶𝗻𝘀/, 𝗵𝗼𝗼𝗸𝘀/, and 𝘀𝗸𝗶𝗻𝘀/ are the surface area for user customization. 𝗹𝗼𝗴𝘀/ gives you 𝗮𝗴𝗲𝗻𝘁.𝗹𝗼𝗴, 𝗴𝗮𝘁𝗲𝘄𝗮𝘆.𝗹𝗼𝗴, and 𝗲𝗿𝗿𝗼𝗿𝘀.𝗹𝗼𝗴 for debugging.

you won't manually edit most of these files. but knowing this layout means you understand exactly where identity, memory, skills, automation, and state live, and how they connect.

i wrote a full deep dive covering hermes agent's architecture, memory system, self-evolving skills, GEPA optimization, and setting up multiple specialized agents.

The article is quoted below.

> **Akshay @akshay\_pachaar** · 2026-05-13
> 
> ![Image](https://pbs.twimg.com/media/HIcQfYeaIAAo0dV?format=jpg&name=large) ![Article cover image](https://pbs.twimg.com/media/HIIq8UxbwAAb5ul?format=jpg&name=large)

---

## Comments

> **ody @odyzhou** · [2026-05-16](https://x.com/odyzhou/status/2055638847124652089)
> 
> finally stopped treating my agents like magic boxes. when you actually open the hood and see how the memory layers work you realize how much potential there is for custom workflows.
> 
> > **Akshay @akshay\_pachaar** · [2026-05-16](https://x.com/akshay_pachaar/status/2055707176098996301)
> > 
> > The three-tier split is what makes it click. Tier 1 for always-in-context facts, Tier 2 for searchable history, external providers for deeper persistence.

> **Mert · AI Architect @MertLovesAI** · [2026-05-16](https://x.com/MertLovesAI/status/2055684992848585056)
> 
> The agent eats the interface, but the real consolidation is one MCP wiring one bill.
> 
> Hermes gets this right with skills as self-contained units. the harness matters more than any single model behind it.
> 
> > **Mert · AI Architect @MertLovesAI** · 2026-05-14
> > 
> > Creative tools consolidate around agents, not platforms. Pika's bet is that the interface dies and the agent eats the subscription stack.
> > 
> > One MCP. One bill. No prompt engineering.
> > 
> > This is the shape consumer AI should have shipped in already. x.com/i/status/20549…
> 
> > **Akshay @akshay\_pachaar** · [2026-05-16](https://x.com/akshay_pachaar/status/2055705849964970371)
> > 
> > Exactly. Skills as self-contained units is the key design choice.
> > 
> > It means you can swap the model underneath without rewriting your capabilities. The harness becomes the durable layer, the model becomes interchangeable.