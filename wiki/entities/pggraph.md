---
type: entity
title: pgGraph
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [pgGraph]
tags: [postgres, graph-database, rust, extension, open-source]
---

# pgGraph

> An open-source PostgreSQL extension that compiles a database's foreign-key relationships into an in-memory graph for fast traversal, keeping topology separate from row data.

## Profile

pgGraph is an open-source PostgreSQL extension that turns the foreign-key structure already present in a relational schema into a fast, in-memory graph-traversal layer. Delivered via pgrx (Rust), it compiles existing foreign-key relationships into a Compressed Sparse Row (CSR) integer array held entirely in memory, separating topology (held by pgGraph) from data (held by Postgres) and hydrating rows from Postgres only after a path resolves ([[wiki/sources/daleverett-postgres-as-graph-pggraph]]). It targets deep traversals (beyond 5 hops), million-edge datasets, sub-50ms response times, and agentic workflows needing real-time structural context. The project is free, Apache 2.0 licensed, with no paid tier, usage cap, or vendor lock-in, and is hosted at github.com/Evokoa/pgGraph.

## Key facts

- **Type**: open-source PostgreSQL extension, delivered via pgrx (Rust) (cited to [[wiki/sources/daleverett-postgres-as-graph-pggraph]])
- **Core mechanism**: compiles existing foreign-key relationships into a Compressed Sparse Row (CSR) integer array held entirely in memory
- **Architecture**: separates topology (held by pgGraph) from data (held by Postgres); hydrates rows from Postgres only after a path resolves
- **Pipeline (four steps)**: schema scan (auto-detect FKs) → graph compilation (CSR) → in-memory traversal (tight Rust loop) → hydration (single batch query)
- **LDBC benchmark (3.1M nodes / 34.5M edges)**: Person search 9.8ms hot; Friend traversal 34.1ms hot; Post-to-tag path 6.5ms hot
- **Memory footprint**: roughly 34x smaller than loading the same dataset into [[wiki/entities/neo4j|Neo4j]], because it stores only topology (integer IDs + edge types), not row payloads
- **License**: Apache 2.0; free, open source; no paid tier, no usage cap, no vendor lock-in
- **Repo**: github.com/Evokoa/pgGraph
- **openCypher compatibility**: described as "coming soon" / not yet available
- **Target use cases**: traversals deeper than 5 hops, million-edge datasets, sub-50ms responses, agentic workflows needing real-time structural context

## Positions and claims

- A relational database's existing foreign keys already encode a graph; pgGraph compiles that graph into memory rather than requiring a separate graph database — argued in [[wiki/sources/daleverett-postgres-as-graph-pggraph]].
- Storing only topology (not row payloads) yields a far smaller memory footprint than a dedicated graph database loading the same dataset (~34x vs. [[wiki/entities/neo4j|Neo4j]]) — see [[wiki/sources/daleverett-postgres-as-graph-pggraph]].

## Mentioned in

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — the launched open-source Postgres extension; the in-memory CSR graph-traversal layer that is the subject of the post.

## Related entities

- [[wiki/entities/daleverett]] — author of the announcement; associated with the project ("we built").
- [[wiki/entities/evokoa]] — GitHub owner hosting the pgGraph repository.
- [[wiki/entities/postgres]] — the database pgGraph extends.
- [[wiki/entities/rust-language]] — implementation language (via pgrx).
- [[wiki/entities/neo4j]] — dedicated graph database used as the memory-footprint comparison baseline.
- [[wiki/entities/pgrouting]] — PostGIS graph-algorithms extension presented as a compared alternative.

## Related concepts

- (none yet)
