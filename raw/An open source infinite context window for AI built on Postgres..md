---
title: "An open source infinite context window for AI built on Postgres."
source: "https://x.com/daleverett/status/2079793421515206862"
author:
  - "[[@daleverett]]"
published: 2026-07-22
created: 2026-07-22
description: "Your AI assistant was brilliant in the demo. Then it met reality. The model had not suddenly become less intelligent. It had simply reached ..."
tags:
  - "clippings"
  - "agent-memory"
  - "postgres"
---
![Image](https://pbs.twimg.com/media/HNzNwo9aUAEMidS?format=jpg&name=large)

Your AI assistant was brilliant in the demo. Then it met reality. The model had not suddenly become less intelligent. It had simply reached the edge of what it could see. This is the hidden constraint behind many AI products.

We talk obsessively about model intelligence, reasoning scores, and context-window sizes. But for most production applications, the harder problem is whether the system can find the right information, at the right moment, with the right permissions, before the model starts reasoning.

Meet pgContext. The open source panacea to all your retrieval problems.

[\[here’s the repo →\]](https://github.com/evokoa/pgContext)

## Postgres becomes the memory layer

pgContext is an open-source Postgres extension that adds dense vector search, metadata-filtered approximate nearest-neighbor search, and hybrid vector-plus-full-text retrieval directly inside Postgres.

Yes, fully **inside good ol' Postgres**.

A conventional RAG database often introduces another system beside the application database. Product data lives in Postgres, while embeddings and searchable copies are sent to a vector service.

Teams then build pipelines to move data between them and must keep everything synchronized. But every copy creates another place where reality can drift. (I like to call this the "thanos snap")

pgContext takes a different approach. Your ordinary PostgreSQL tables remain the authoritative source of truth. Its HNSW acceleration structures are treated as rebuildable indexes rather than as a separate copy of the application’s truth.

Which means AI-native search does not require another database, another ingestion service, another synchronization job, and another operational boundary.

It can just begin with:

> CREATE EXTENSION pgcontext;

## Wait, this changes everything.

The appeal is not merely technical elegance. It is the possibility of removing entire categories of product and infrastructure friction.

1. AI now works closer to live operational truth. When a source row changes, the retrieval system does not need to wait for a separate copy to catch up.
2. Governance becomes part of retrieval. Permissions can remain enforced by the database layer before context reaches the model.
3. The architecture becomes easier to reason about. Instead of debugging an answer across multiple databases and services, teams can keep the retrieval lifecycle within one transactional system.
4. Finally, better retrieval can make model choice less existential. A smaller or less expensive model supplied with precise, authoritative evidence can outperform a stronger model forced to reason through a noisy mountain of tokens.

## The context architecture becomes the moat.

The first wave of generative AI products was built around prompts. The next wave is being built around systems that decide what belongs in those prompts.

That includes retrieval, ranking, permissions, freshness, relationships, compression, provenance, and the ability to return to the source of truth when an answer matters.

In the world today, model intelligence is only one layer of the product. And sure, the context window remains finite.

But the product no longer has to think that way.

Because when every relevant row can be discovered, filtered, verified, and placed into working memory at the moment it is needed, the model gains something more useful than an infinite prompt.

It gains access to an effectively infinite memory. Unbounded effective context.

If it looks useful, please star the repo. If it doesn’t look useful yet, star it optimistically and then tell us why. ⭐

**GitHub** →[\[Click Here\]](https://github.com/evokoa/pgContext)

**Host it on Polygres →**[\[Click Here\]](https://polygres.com/) (Free for limited time)

**More Links Below!**