---
type: entity
title: Redis
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [Redis]
tags: [database, key-value, cache, agentic-memory, stub]
---

# Redis

> In-memory key-value store. Appears in this wiki via [[wiki/sources/techwith-ram-agentic-memory-breakdown]].

## Key facts

- Listed as a structured store (exact lookup) for external agentic memory — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Recommended for sessions ("Sessions belong in Redis or Dragonfly, never in application memory") — [[wiki/sources/akintola-steve-backend-1-million-users]].
- Redis Cluster recommended for caching and real-time data — [[wiki/sources/akintola-steve-backend-1-million-users]].
- The Layer 2 application cache holds computed results, session data, and hot records — [[wiki/sources/akintola-steve-backend-1-million-users]].
- Used as a session store alongside Cognee in a hackathon where users built 21 LLM Knowledge Wikis in 3 hours — [[wiki/sources/tricalt-memory-skills-same-harness]].

## Mentioned in

- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — structured key-value store for exact-lookup external memory.
- [[wiki/sources/akintola-steve-backend-1-million-users]] — session store and application-level (Layer 2) cache; deployed as Redis Cluster.
- [[wiki/sources/tricalt-memory-skills-same-harness]] — used as the session store in the Cognee hackathon that built 21 LLM Knowledge Wikis in 3 hours.

## Related entities

- [[wiki/entities/postgres]] — relational store paired with Redis in the 1M-user backend stack.

## Related concepts

*(none yet.)*
