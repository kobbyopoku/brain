---
type: concept
title: Graph traversal
created: 2026-06-06
updated: 2026-06-06
aliases: [graph traversal, path query, multi-hop query, graph walk]
tags: [graph-database, query-pattern, postgres, data-engineering]
---

# Graph traversal

> Walking the edges of a network of related entities — resolving paths, neighbors, and connected components across multiple hops — as a query operation distinct from the row-and-column matching of relational SQL.

## Definition

Graph traversal is the operation of following relationships through a graph: finding paths between nodes, enumerating a node's neighbors, or computing connected components, often across many hops. It is contrasted with relational joins, which are well-suited to combining tables but ill-suited to walking a network of arbitrary depth (e.g. "every entity within five hops"). One implementation approach resolves the topology in memory before hydrating rows from the underlying store.

## Why it matters

Many real datasets are graphs in disguise — entities connected by foreign keys form a network — yet querying them as paths in SQL grows unwieldy as hop count rises. Making traversal a first-class, fast operation unlocks relationship-centric queries (reachability, shortest path, neighborhoods) without abandoning the system of record. It also offers an alternative source of context for agentic workflows: structural context retrieved by walking relationships rather than by embedding similarity.

## Treatment across sources

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] frames it as the central capability of pgGraph: multi-hop path, neighbor, and connected-component queries over relationships. The source argues SQL joins are ill-suited to walking a network ("every entity within five hops") and that pgGraph performs traversal via in-memory CSR (compressed sparse row), resolving paths before hydrating rows.

## Sub-claims and details

- Graph traversal covers multi-hop path queries, neighbor queries, and connected-component queries. [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- SQL joins are framed as poorly suited to walking a network, especially at depth (e.g. "every entity within five hops"). [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- pgGraph performs traversal in memory using a CSR (compressed sparse row) representation, resolving the path/topology first and then hydrating the matching rows. [[wiki/sources/daleverett-postgres-as-graph-pggraph]]

## Open questions and contradictions

- The performance ceiling of in-memory CSR traversal at large graph sizes is not addressed by the source.

## Related concepts

- [[postgres-as-platform]] — the "add traversal to Postgres" framing that this capability instantiates.
- [[retrieval-augmented-generation]] — graph traversal as a structural-context alternative/complement to embedding retrieval.
- [[vector-database]] — sibling Postgres-extension capability (pgvector) contrasted in the same source's lineage.

## Related entities

- [[wiki/entities/pggraph]]
- [[wiki/entities/postgres]]

## Mentioned in

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
