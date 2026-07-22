---
title: "Post by @Mnilax on X"
source: "https://x.com/Mnilax/status/2079632365002117542/photo/2"
author:
  - "[[@Mnilax]]"
published: 2026-06-07
created: 2026-07-22
description: "everyone's self-improving agent is deleting its most useful data. Stanford just dropped a paper that keeps the part everyone throws away: t"
tags:
  - "clippings"
  - "llm-research"
  - "agent-memory"
---
everyone's self-improving agent is deleting its most useful data.

Stanford just dropped a paper that keeps the part everyone throws away: the agent's own failures.

fail a task -> diagnose why it failed -> write a code patch -> fold it back in -> retry

the standard loop only trains on successful runs and discards the failed ones, but failures are exactly where the model's weaknesses show.

so they flip it: an LLM reads the failed trajectory, names the failure mode, and generates an inference-time patch that upgrades the agent.

no retraining, just a quick human check.

the agent gets better from the runs everyone else deletes.

start with the paper, the article below shows how to wire it.

> **Mnimiy @Mnilax** · 2026-06-07
> 
> ![Article cover image](https://pbs.twimg.com/media/HKOnPerWsAAgxaR?format=jpg&name=large)

---

## Comments

> **Zoe MLL @the\_zmll** · [2026-07-22](https://x.com/the_zmll/status/2079859183961195006)
> 
> It seems we've all been converging towards an instance of this, none really cracking it long term. Do we understand the capability gaps enough?

> **OuWei @OuWei52613** · [2026-07-22](https://x.com/OuWei52613/status/2079787973588205609)
> 
> 請確認補丁是不是解決了真問題

> **midnight @midsusnight** · [2026-07-21](https://x.com/midsusnight/status/2079635209914626226)
> 
> how often do the patches break something else?

> **dunik @dunik\_7** · [2026-07-21](https://x.com/dunik_7/status/2079636942333886572)
> 
> it's the best guide what i watched, thank you mate

> **Ankush Singal @andysingal** · [2026-07-22](https://x.com/andysingal/status/2079803501476241485)
> 
> added here: Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents....
> 
> [medium.com Learning from Failure: Inference-Time Self-Improvement for Computer-Use Agents](https://t.co/pkBxey2Y3K)

> **Harry Tandy @HarryTandy** · [2026-07-21](https://x.com/HarryTandy/status/2079632884219122006)
> 
> what kind of human check does the patch need before it goes in?
> 
> does the agent ever push a fix that makes things worse?