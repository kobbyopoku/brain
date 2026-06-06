---
type: entity
title: PostgreSQL
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [PostgreSQL, Postgres]
tags: [database, relational, sql]
---

# PostgreSQL

> Open-source relational database; in this wiki it appears as a direct query target for a Database MCP and as the relational substrate that the pgGraph extension turns into a graph database.

## Profile

PostgreSQL ("Postgres") is a relational database. In this wiki it surfaces in two roles: as a database that a Claude Code Database MCP can query directly, and — more substantively — as the relational engine that the **pgGraph** extension augments with graph-traversal capabilities. The pgGraph source argues that a typical SaaS Postgres schema already encodes a graph, even though SQL itself was designed for pairwise table joins rather than walking a network of relationships.

## Key facts

- Listed among the databases a Database MCP can query directly — [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]].
- A typical SaaS Postgres schema already encodes a graph (orgs → users → tickets → comments → users) — [[wiki/sources/daleverett-postgres-as-graph-pggraph]].
- SQL was designed to join two tables at a time, not to walk a network of relationships — [[wiki/sources/daleverett-postgres-as-graph-pggraph]].
- Postgres extensions (recursive CTEs, pgRouting, pgGraph) execute within the Postgres process and share its memory and CPU constraints — [[wiki/sources/daleverett-postgres-as-graph-pggraph]].
- Recursive CTEs are standard SQL and the recommended starting point for small graph queries in Postgres — [[wiki/sources/daleverett-postgres-as-graph-pggraph]].
- Listed as a structured store (exact lookup) for external agentic memory, queried by key/ID/SQL; described as fast, predictable, and good for user profiles, preferences, and structured data — [[wiki/sources/techwith-ram-agentic-memory-breakdown]].
- Recommended as the primary OLTP store at 1M-user scale, paired with Citus for horizontal sharding; read replicas sit behind PgBouncer for connection pooling — [[wiki/sources/akintola-steve-backend-1-million-users]].

## Positions and claims

- **A SaaS Postgres schema is already a graph** — the pgGraph framing in [[wiki/sources/daleverett-postgres-as-graph-pggraph]] argues the relational data already forms a network; the gap is traversal ergonomics, not the underlying shape.

## Mentioned in

- [[wiki/sources/suryanshti777-9-claude-code-plugins-senior-engineer]] — named target database for Database MCP.
- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — the relational database pgGraph extends; source argues a typical SaaS Postgres schema already encodes a graph.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — structured store for exact-lookup external memory.
- [[wiki/sources/akintola-steve-backend-1-million-users]] — recommended primary OLTP database, paired with Citus for horizontal sharding.

## Related entities

- [[wiki/entities/supabase]] — Postgres-backed backend platform.

## Related concepts

*(none yet.)*
