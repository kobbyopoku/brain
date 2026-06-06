---
type: concept
title: Postgres as platform
created: 2026-06-06
updated: 2026-06-06
aliases: [Postgres as platform, do it in Postgres, just use Postgres, Postgres extensions]
tags: [postgres, data-architecture, extensions, platform-strategy]
---

# Postgres as platform

> The "do it in Postgres" pattern — adding a new workload to PostgreSQL via an extension instead of migrating data out to a purpose-built datastore.

## Definition

Postgres-as-platform is the architectural stance that PostgreSQL is an extensible base on which specialized workloads can be added in place, rather than a relational store you outgrow and migrate away from. When a new need arises — vector search, graph traversal — the pattern says reach for a Postgres extension that brings the capability to your existing data, instead of standing up and syncing to a dedicated system. The thesis is that capabilities should arrive "without migrating data out of Postgres."

## Why it matters

Migrating data to a dedicated datastore (e.g. a graph database) adds an operational system, a sync pipeline, and a consistency problem. Keeping the workload in Postgres preserves the system of record, transactions, and tooling while adding the new capability. For a builder, the payoff is fewer moving parts and one source of truth; the pattern reframes "which database do I need" into "which extension do I add."

## Treatment across sources

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]] frames it as the "do it in Postgres" pattern applied to graph traversal: rather than migrate to a dedicated graph database (Neo4j), add traversal to Postgres via the pgGraph extension. Its core arguments are "your schema is already a graph" and gaining graph "capabilities without migrating data out of Postgres" — explicitly positioned as a sibling to pgvector.

## Sub-claims and details

- The pattern adds a workload to Postgres via an extension rather than migrating to a dedicated datastore. [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- For graph traversal, the alternative being rejected is a dedicated graph database such as Neo4j. [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- Supporting claim: "your schema is already a graph" — relational data is already a network, so no model change is required. [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- Stated benefit: graph capabilities "without migrating data out of Postgres." [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
- pgGraph is positioned as a sibling to pgvector (the extension that added vector search to Postgres). [[wiki/sources/daleverett-postgres-as-graph-pggraph]]

## Open questions and contradictions

- The source does not address where the pattern breaks down — i.e., at what scale or workload a dedicated datastore beats a Postgres extension.

## Related concepts

- [[graph-traversal]] — the specific capability added to Postgres in the anchor source.
- [[vector-database]] — pgvector as the prior instance of the same pattern.
- [[ai-as-infrastructure]] — adjacent "consolidate capability into a base layer" framing.

## Related entities

- [[wiki/entities/postgres]]
- [[wiki/entities/pggraph]]

## Mentioned in

- [[wiki/sources/daleverett-postgres-as-graph-pggraph]]
