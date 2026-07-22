---
title: "Mnimiy on X: \"everyone's self-improving agent is deleting its most useful data.Stanford just dropped a paper that keeps the part everyone throws away: the agent's own failures.fail a task -> diagnose why it failed -> write a code patch -> fold it back in -> retrythe standard loop only https://t.co/RALDXDc9J5\""
source: "https://x.com/Mnilax/status/2079632365002117542"
author:
published: 2026-06-07
created: 2026-07-22
description:
tags:
  - "clippings"
  - "llm-research"
  - "agent-memory"
---
## Post

## Conversation[Mnimiy](https://x.com/Mnilax)[@Mnilax](https://x.com/Mnilax)

everyone's self-improving agent is deleting its most useful data. Stanford just dropped a paper that keeps the part everyone throws away: the agent's own failures. fail a task -> diagnose why it failed -> write a code patch -> fold it back in -> retry the standard loop only trains on successful runs and discards the failed ones, but failures are exactly where the model's weaknesses show. so they flip it: an LLM reads the failed trajectory, names the failure mode, and generates an inference-time patch that upgrades the agent. no retraining, just a quick human check. the agent gets better from the runs everyone else deletes. start with the paper, the article below shows how to wire it.

[![Image](https://pbs.twimg.com/media/HNxWk4hWEAAsYxA?format=png&name=small)](https://x.com/Mnilax/status/2079632365002117542/photo/1)Quote

Mnimiy

@Mnilax

Jun 7

17 prompts that make Hermes run while you sleep (copy-paste inside)

In February 2026, Nous Research released Hermes Agent: an open-source, self-hosted agent that doesn't live inside an IDE and doesn't forget when the tab closes. It runs as a daemon on your own box,...

Post your reply[Zoe MLL](https://x.com/the_zmll)[@the\_zmll](https://x.com/the_zmll)

[3m](https://x.com/the_zmll/status/2079859183961195006)

It seems we've all been converging towards an instance of this, none really cracking it long term. Do we understand the capability gaps enough?[OuWei](https://x.com/OuWei52613)[@OuWei52613](https://x.com/OuWei52613)

[4h](https://x.com/OuWei52613/status/2079787973588205609)

請確認補丁是不是解決了真問題[30](https://x.com/OuWei52613/status/2079787973588205609/analytics)[midnight](https://x.com/midsusnight)[@midsusnight](https://x.com/midsusnight)

[14h](https://x.com/midsusnight/status/2079635209914626226)

how often do the patches break something else?[98](https://x.com/midsusnight/status/2079635209914626226/analytics)[dunik](https://x.com/dunik_7)[@dunik\_7](https://x.com/dunik_7)

[14h](https://x.com/dunik_7/status/2079636942333886572)

it's the best guide what i watched, thank you mate[85](https://x.com/dunik_7/status/2079636942333886572/analytics)[Ankush Singal](https://x.com/andysingal)[@andysingal](https://x.com/andysingal)

[3h](https://x.com/andysingal/status/2079803501476241485)

added here: Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents....[21](https://x.com/andysingal/status/2079803501476241485/analytics)[Harry Tandy](https://x.com/HarryTandy)[@HarryTandy](https://x.com/HarryTandy)

[15h](https://x.com/HarryTandy/status/2079632884219122006)

what kind of human check does the patch need before it goes in? does the agent ever push a fix that makes things worse?[137](https://x.com/HarryTandy/status/2079632884219122006/analytics)

## Discover more

Sourced from across X[Ridark](https://x.com/ridark_eth)[@ridark\_eth](https://x.com/ridark_eth)

[10h](https://x.com/ridark_eth/status/2079697417625063655)

SIX SEVEN just killed its flagship mode MOG Arena right before the main event everything’s been building toward.. But not because it flopped, something way bigger is taking its place: SIXSEVEN PRIME This is the final on-ramp before TMA Greatness Day. The play is stupidly

[![Image](https://pbs.twimg.com/media/HNyPpKyXsAExQZk?format=png&name=360x360)](https://x.com/ridark_eth/status/2079697417625063655/photo/1)

<video aria-label="Embedded video" controls=""><source type="video/mp4" src="blob:https://x.com/0ad8605a-c0f1-400e-a6d9-010d0c7dba51"></video> ![](https://pbs.twimg.com/amplify_video_thumb/2079695097302577152/img/vxrTVLzcGLAEaXla.jpg)

0:31

Quote

Six Seven Club

@sixsevenapp

Jul 21

![Embedded video](https://pbs.twimg.com/ext_tw_video_thumb/2079487010985648128/pu/img/PnWgw3FI9UoT-BUd?format=jpg&name=240x240)

0:03

MEET SIXSEVEN PRIME! As promised, MOG Arena is now over TMA Greatness Day is getting closer, so this is your last chance to board the 67 train invite a new user through your PRIME link & you’ll both get an extra 67 points[1.6K](https://x.com/ridark_eth/status/2079697417625063655/analytics)