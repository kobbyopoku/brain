---
title: "How to add infinite context to your AI Agent"
source: "https://x.com/daleverett/status/2079188156973498414"
author:
  - "[[@daleverett]]"
published: 2026-07-20
created: 2026-07-21
description: "An AI agent can appear brilliant: right up until the information it needs falls out of the prompt. The first few interactions work perfectly..."
tags:
  - "clippings"
  - "agent-memory"
---
![Image](https://pbs.twimg.com/media/HNrCk4ga4AA23yc?format=jpg&name=large)

An AI agent can appear brilliant: right up until the information it needs falls out of the prompt. The first few interactions work perfectly. Then the conversation grows. Tool outputs accumulate. Customer history, earlier decisions, support tickets, policies, and product data compete for the same limited number of tokens, all jostling to get to the front of the queue.

Eventually, something important gets truncated, summarized beyond recognition, or buried beneath thousands of less relevant words. (Oh boy, does a tiny context window suck)

The obvious solution is to use a model with a larger context window. But a larger window only moves the boundary.

> Research into long-context language models has also found that models do not always use every part of a long prompt equally well. Performance can fall when the relevant information appears in the middle of a large input—the aptly named “lost in the middle” problem.

## Infinite context does not mean an infinite prompt.

Let’s clarify the word **infinite**.

> No production system has literally infinite storage, compute, or tokens.

[@polygres](https://x.com/@polygres) does not change the maximum input size of an LLM. Instead, it gives your agent **unbounded effective context**: information can remain in the database and become working memory whenever the agent needs it.

Rather than stuffing an entire knowledge base into every request, the agent queries its memory and retrieves a focused, token-ready slice.

In other words: **The prompt remains finite, but the addressable memory becomes database-scale.**

The goal is to retrieve the **smallest context that contains everything required to make the right decision**.

The result is an agent that does not need to carry its entire universe inside every prompt. It only needs a reliable way to navigate that universe.

You can try Polygres for free at [polygres.com](https://polygres.com/).

## Why context should live in a database

A context window is temporary. A database is persistent. That difference changes how you design an agent.

When the prompt is the agent’s only memory, every interaction becomes an exercise in compression. You continually decide which messages to keep, which documents to summarize, and which facts to discard. (leads to hallucination)

When Postgres becomes the data/memory layer, the prompt becomes a workspace rather than a warehouse.

Polygres brings four retrieval capabilities to the same operational data:

- **Graph retrieval** follows relationships between records. It can move from a customer to their account, tickets, messages, incidents, orders, or deployments.
- **Vector retrieval** finds records with similar meaning using embeddings stored in a vector(n) column.
- **Text retrieval** supports language-aware full-text search with TSVector and typo-tolerant matching with PostgreSQL trigram search.
- **Hybrid retrieval** combines graph relationships with vector similarity, allowing the agent to find information that is both semantically relevant and connected to the current entity.

Postgres remains the source of truth. Your application can continue using standard SQL for ordinary reads and writes while Polygres handles richer retrieval over those same records.

That eliminates an architectural question that appears in many agent projects:

> Which version of the data is the real one: the application database, the vector store, the graph database, or the search index?

With Polygres, they can all operate over the same underlying project data. There is only **ONE** source of truth.

## To infinity and beyond the context window

The future of AI agents will not be built by endlessly widening prompts.

It will be built by separating **memory** from **attention**. (I guess attention isn't all you need hmm?)

Memory belongs in a durable, structured, queryable system. Attention belongs in the model’s current context. Polygres connects the two by turning Postgres records, relationships, text indexes, and embeddings into retrievable working memory.

Your agent no longer needs to know everything at once.

It needs to know that everything it may need is reachable.

Stop stuffing prompts. Start querying.

- Try Polygres Today: [http://polygres.com](https://t.co/jhryKmThjh)
- Dev Discord (1k+ devs): [https://discord.gg/RFSHD5DgKP](https://t.co/8OTkEwRo7z)