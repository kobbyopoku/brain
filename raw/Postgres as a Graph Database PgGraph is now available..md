---
title: "Postgres as a Graph Database: PgGraph is now available."
source: "https://x.com/daleverett/status/2056406175282033090"
author:
  - "[[@daleverett]]"
published: 2026-05-18
created: 2026-05-21
description: "If you've been searching  for \"Postgres as a graph database\" you have probably found advice ranging from recursive CTEs to full graph databa..."
tags:
  - "postgres"
  - "pg"
  - "pggraph"
---
![Image](https://pbs.twimg.com/media/HInQvJxbkAA3VDy?format=jpg&name=large)

If you've been searching for "Postgres as a graph database" you have probably found advice ranging from recursive CTEs to full graph database migrations. pgGraph has just been released which allows you to access this natively via a pgrx extension which you can find [here](https://github.com/Evokoa/pgGraph).

This post compares pgGraph to the other main approach to graph querying in Postgres, explains when each one works, and shows where each one breaks.

## Your Postgres Schema is Already a Graph

Before we compare approaches, it is worth understanding what you already have. A typical SaaS schema actually already encodes a graph.

Organizations connect to users. Users connect to tickets as creators and assignees. Tickets connect to comments. Comments connect back to users. You can draw this as a network diagram and it makes immediate sense.

The problem is that SQL was not designed to walk this network. It was designed to join two tables at a time. When you need to answer "show me every entity within five hops of this user," SQL starts fighting you.

## pgRouting

pgRouting is a PostGIS extension that provides graph algorithms like Dijkstra shortest path and A\* search. It was built for geospatial routing (finding the fastest path between two GPS coordinates) but can be repurposed for non-spatial graph problems.

**When pgRouting works**

- You need shortest path or minimum cost algorithms specifically
- Your graph is relatively small (thousands to low millions of edges)
- You are already using PostGIS
- Your use case maps cleanly to weighted edges with a cost function

**When pgRouting breaks**

pgRouting was designed for road networks, not arbitrary entity graphs. It expects a specific edge table format with source, target, and cost columns. Modeling complex enterprise relationships (where a single join table connects six entities simultaneously) requires decomposing those relationships into pairwise edges, which inflates the graph and distorts path semantics.

Performance is acceptable for GIS-scale problems but degrades on large, dense graphs. pgRouting still executes within the Postgres process, so it shares the same memory and CPU constraints as the database itself. There is no dedicated graph index structure. Deep traversals on million-edge graphs will hit the same planner bottlenecks as recursive CTEs, just with better algorithm implementations on top.

## In-Memory Graph Layer (pgGraph)

This is the approach we built. [pgGraph](https://github.com/evokoa/pggraph) is an open-source Postgres extension that compiles your existing foreign key relationships into a Compressed Sparse Row (CSR) array held entirely in memory.

The key insight: separate topology from data. Postgres stores and serves rows. pgGraph stores and traverses relationships. When a traversal query arrives, pgGraph walks the in-memory integer array (not the Postgres tables) to find matching paths. Only after the path is resolved does it go back to Postgres to hydrate the actual row data.

How it works

1. **Schema scan.** pgGraph reads your Postgres schema and identifies foreign key relationships automatically.
2. **Graph compilation.** It builds a CSR array from those relationships. This is a flat integer array where finding a node's neighbors requires a single array offset calculation. No B-tree index lookups. No pointer chasing.
3. **In-memory traversal.** When a query asks for paths, neighbors, or connected components, pgGraph walks the CSR array in a tight Rust loop. No garbage collection. No query planner overhead.
4. **Hydration.** The traversal returns a set of node IDs. pgGraph fetches the corresponding rows from Postgres in a single batch query.

**Benchmarks**

On the LDBC Social Network Benchmark (3.1 million nodes, 34.5 million edges):

- **Person search:** 9.8ms (hot)
- **Friend traversal:** 34.1ms (hot)
- **Post-to-tag path:** 6.5ms (hot)

The memory footprint is roughly 34x smaller than loading the same dataset into Neo4j, because pgGraph stores only topology (integer IDs and edge types), not row payloads.

**When pgGraph works**

- You need traversals deeper than 5 hops
- Your dataset has millions of edges
- Your application (or AI agent) needs sub-50ms response times
- You want graph capabilities without migrating data out of Postgres
- You are building agentic workflows that require real-time structural context

**When pgGraph is not the right fit**

- You need openCypher compatibility (for now, coming soon)
- Your use case is strictly shortest-path on a road network (use pgRouting)
- Your graph is tiny and a recursive CTE is fast enough

## Getting Started

pgGraph is free, open source, and licensed under Apache 2.0. There is no paid tier, no usage cap, and no vendor lock-in. It is a Postgres extension you install and own.

If you are just exploring graph queries in Postgres and your dataset is small, start with recursive CTEs. They require nothing beyond standard SQL and will teach you how your data connects.

If you are hitting performance limits or building applications that need real-time traversal at depth, try pgGraph. [You can view the repo here.](https://github.com/Evokoa/pgGraph) Do give us a star!

[#postgres](https://x.com/search?q=%23postgres&src=hashtag_click) [#rust](https://x.com/search?q=%23rust&src=hashtag_click)