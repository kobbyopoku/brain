---
type: source
title: "daleverett — Postgres as a Graph Database: pgGraph is now available"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/daleverett/status/2056406175282033090
source_type: x-thread
author: daleverett (@daleverett)
source_date: 2026-05-18
raw_path: raw/Postgres as a Graph Database PgGraph is now available..md
content_status: substantive-verbatim
tags: [postgres, graph-database, pggraph, rust, pgrx, csr, graph-traversal, agentic-context, open-source, apache-2]
---

# daleverett — Postgres as a Graph Database: pgGraph is now available

> Launch + comparison post for **pgGraph**, an Apache-2.0 Postgres extension (pgrx/Rust) that compiles existing foreign-key relationships into an in-memory Compressed Sparse Row array so applications and AI agents can run deep graph traversals natively in Postgres without migrating to a dedicated graph database.

## TL;DR

pgGraph is an open-source Postgres extension that gives Postgres native graph-traversal capabilities by separating **topology** from **data**: it auto-scans the schema's foreign keys, compiles them into a Compressed Sparse Row (CSR) integer array held entirely in memory, walks that array in a tight Rust loop on traversal queries, and only then hydrates matching rows from Postgres. The post positions pgGraph against the two existing approaches to graph queries in Postgres — recursive CTEs (good for small/exploratory) and pgRouting (good for shortest-path on road networks) — arguing each breaks on large, dense, deep enterprise graphs. On the LDBC Social Network Benchmark (3.1M nodes, 34.5M edges) it reports hot-path queries of 6.5-34.1ms and a ~34x smaller memory footprint than Neo4j because only topology is stored.

## Key takeaways

- **Your existing relational schema is already a graph.** A typical SaaS schema (orgs → users → tickets → comments → users) encodes a network; SQL was built to join two tables at a time, not to "walk" the network — queries like "every entity within five hops of this user" fight the planner.
- **pgGraph's core insight is to separate topology from data.** Postgres stores/serves rows; pgGraph stores/traverses relationships. Only after a path resolves does it return to Postgres to hydrate row data.
- **Four-step mechanism:** (1) schema scan auto-detects foreign-key relationships; (2) graph compilation builds a CSR array (flat integer array; neighbor lookup is a single array-offset calc, no B-tree lookups or pointer chasing); (3) in-memory traversal walks the CSR in a tight Rust loop (no GC, no query-planner overhead); (4) hydration fetches the resolved node IDs' rows from Postgres in a single batch query.
- **Delivered as a pgrx extension** (Rust framework for building Postgres extensions). Repo: `github.com/Evokoa/pgGraph`.
- **Benchmarks on LDBC Social Network Benchmark (3.1M nodes / 34.5M edges):** Person search 9.8ms (hot); Friend traversal 34.1ms (hot); Post-to-tag path 6.5ms (hot).
- **~34x smaller memory footprint than loading the same dataset into Neo4j**, because pgGraph stores only topology (integer IDs + edge types), not row payloads.
- **pgGraph fits when:** traversals are deeper than 5 hops; the dataset has millions of edges; the app or AI agent needs sub-50ms responses; you want graph capability without migrating data out of Postgres; you are building agentic workflows that need real-time structural context.
- **pgGraph does not fit when:** you need openCypher compatibility (described as "coming soon"); the use case is strictly shortest-path on a road network (use pgRouting); or the graph is tiny and a recursive CTE is fast enough.
- **pgRouting** is a PostGIS extension providing graph algorithms (Dijkstra shortest path, A*) built for geospatial routing; repurposable for non-spatial graphs but expects a `source/target/cost` edge-table format. Modeling enterprise relationships where one join table connects six entities forces decomposition into pairwise edges, inflating the graph and distorting path semantics.
- **pgRouting shares Postgres's process constraints** — same memory/CPU, no dedicated graph index, so deep traversals on million-edge graphs hit the same planner bottlenecks as recursive CTEs, just with better algorithm implementations on top.
- **Recursive CTEs** are the recommended starting point for small datasets and exploration — "nothing beyond standard SQL" — and teach how the data connects.
- **Licensing/positioning:** free, open source, Apache 2.0; "no paid tier, no usage cap, no vendor lock-in" — an extension you install and own.
- **Authored by daleverett**, hashtagged `#postgres #rust`; the maintainer org appears as "Evokoa" (repo `Evokoa/pgGraph`).

## Notable quotes

> "The key insight: separate topology from data. Postgres stores and serves rows. pgGraph stores and traverses relationships."

> "pgGraph walks the in-memory integer array (not the Postgres tables) to find matching paths. Only after the path is resolved does it go back to Postgres to hydrate the actual row data."

> "The memory footprint is roughly 34x smaller than loading the same dataset into Neo4j, because pgGraph stores only topology (integer IDs and edge types), not row payloads."

> "If you are just exploring graph queries in Postgres and your dataset is small, start with recursive CTEs... If you are hitting performance limits or building applications that need real-time traversal at depth, try pgGraph."

## Notes

- **Direct relevance to Godwin's stack.** Multiple ROAM Labs products run Postgres + pgvector ([[wiki/projects/helm|Helm]], [[wiki/projects/kivora|Kivora]], [[wiki/projects/clarvyn|Clarvyn]]). pgGraph is a complementary "Postgres-native" capability in the same spirit as pgvector — adding a workload (graph traversal) to Postgres rather than standing up a separate datastore (Neo4j). For multi-tenant SaaS schemas that are already FK-dense, the "your schema is already a graph" framing maps cleanly.
- **The explicit agentic-workflows hook is the most wiki-salient claim**: "You are building agentic workflows that require real-time structural context." Sub-50ms structural traversal as live context for an agent is adjacent to the wiki's [[retrieval-augmented-generation]] thread — graph-traversal-as-context is a structural sibling to vector-retrieval-as-context. Uncertain whether pgGraph markets itself as a RAG component or the author is gesturing at it generically; the source only asserts the agentic use case, not an implementation pattern.
- **Benchmark caveats (analytical, not in source):** numbers are author-reported "hot" timings on a single standard benchmark (LDBC SNB); no cold-path figures, no hardware spec, no comparison methodology for the Neo4j memory claim. Treat the 34x and sub-50ms figures as vendor benchmarks pending independent replication.
- **"Evokoa" vs the lowercase repo URLs.** The body links both `github.com/Evokoa/pgGraph` and `github.com/evokoa/pggraph` (GitHub is case-insensitive on the owner/repo path). Recorded the maintainer as **Evokoa**; flagged as a thin stub — the source says nothing about who/what Evokoa is beyond owning the repo.
- **openCypher "coming soon"** implies a roadmap toward the de-facto graph query language standard; if delivered, it lowers switching cost from Neo4j-style stacks. Worth tracking for any future graph need in ROAM products.
- The post is a launch announcement framed as a comparison essay; tone is technical-promotional ("Do give us a star!").

## Mentioned entities

- [[wiki/entities/daleverett]] — author of the post; associated with the pgGraph project.
- [[wiki/entities/pggraph]] — the launched extension; in-memory CSR graph layer for Postgres.
- [[wiki/entities/evokoa]] — GitHub org/maintainer hosting the pgGraph repo.
- [[wiki/entities/postgres]] — the database pgGraph extends; "your schema is already a graph."
- [[wiki/entities/pgrouting]] — PostGIS graph-algorithms extension; the compared alternative for shortest-path/road-network use.
- [[wiki/entities/postgis]] — geospatial Postgres extension that pgRouting ships under.
- [[wiki/entities/neo4j]] — dedicated graph database; the memory-footprint comparison baseline.
- [[wiki/entities/pgrx]] — Rust framework for building Postgres extensions; pgGraph's build tooling.
- [[wiki/entities/rust-language]] — implementation language; CSR traversal runs in a "tight Rust loop."
- [[wiki/entities/ldbc-social-network-benchmark]] — the graph benchmark used for the reported numbers.

## Related concepts

- [[wiki/concepts/graph-traversal]] — the central capability; multi-hop path/neighbor/connected-component queries over relationships.
- [[wiki/concepts/postgres-as-platform]] — "do it in Postgres" pattern (sibling to pgvector); add workloads to Postgres instead of new datastores.
- [[wiki/concepts/retrieval-augmented-generation]] — graph-traversal-as-agent-context is a structural sibling to vector-retrieval-as-context; the source pitches "real-time structural context" for agents.
- [[wiki/concepts/reasoning-execution-split]] — traversal (execution over topology) separated from row hydration (data fetch); separation-of-concerns echo.

## Related sources

- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — RAG-retrieval-quality thread; both concern how an agent gets the right context, one via better chunking, one via structural traversal.
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — agentic memory over Postgres + pgvector; pgGraph is an adjacent Postgres-native context source.
