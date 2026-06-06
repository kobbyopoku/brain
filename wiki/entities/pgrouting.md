---
type: entity
title: pgRouting
entity_type: product
created: 2026-06-06
updated: 2026-06-06
aliases: [pgRouting]
tags: [postgres, postgis, graph, routing, extension]
---

# pgRouting

> A PostGIS extension providing graph algorithms (Dijkstra, A*) for geospatial routing, presented in this wiki as a compared alternative to [[wiki/entities/pggraph|pgGraph]].

## Profile

pgRouting is a [[wiki/entities/postgis|PostGIS]] extension that provides graph algorithms such as Dijkstra shortest path and A* search. It is built for geospatial routing — finding the fastest path between GPS coordinates — but is repurposable for non-spatial graph problems. It expects a specific edge-table format with source, target, and cost columns. In the [[wiki/entities/pggraph|pgGraph]] announcement it is presented as the main compared alternative for shortest-path / road-network use ([[wiki/sources/daleverett-postgres-as-graph-pggraph]]).

## Key facts

- **Type**: a [[wiki/entities/postgis|PostGIS]] extension providing graph algorithms like Dijkstra shortest path and A* search (cited to [[wiki/sources/daleverett-postgres-as-graph-pggraph]])
- **Primary purpose**: built for geospatial routing (fastest path between GPS coordinates) but repurposable for non-spatial graph problems
- **Input format**: expects a specific edge-table format with source, target, and cost columns
- **Best fit**: shortest-path / minimum-cost problems, relatively small graphs (thousands to low millions of edges), existing PostGIS users, and use cases mapping to weighted edges
- **Limitation**: executes within the Postgres process and has no dedicated graph index, so deep traversals on million-edge graphs hit the same planner bottlenecks as recursive CTEs

## Positions and claims

- Well-suited to weighted shortest-path / minimum-cost problems on relatively small graphs, but its lack of a dedicated graph index makes deep traversals on million-edge graphs hit recursive-CTE-style planner bottlenecks — argued in [[wiki/sources/daleverett-postgres-as-graph-pggraph]].

## Mentioned in

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] — PostGIS graph-algorithms extension presented as the main compared alternative to pgGraph for shortest-path / road-network use.

## Related entities

- [[wiki/entities/postgis]] — the geospatial Postgres extension pgRouting is built on / ships under.
- [[wiki/entities/pggraph]] — the in-memory graph-traversal extension it is compared against.
- [[wiki/entities/postgres]] — the database both run within.

## Related concepts

- (none yet)
