---
type: concept
title: Database Sharding
created: 2026-06-06
updated: 2026-06-06
aliases: [Database Sharding, sharding, horizontal partitioning]
tags: [backend, database, scalability, system-design]
---

# Database Sharding

> Horizontally partitioning a database across multiple nodes so that each holds a subset of the data, chosen by a shard key.

## Definition

Database Sharding splits data across nodes by a shard key chosen on day one. As framed in [[wiki/sources/akintola-steve-backend-1-million-users]], sharding by `user_id` via modulo gives even distribution; all writes route through a query router (Vitess or Citus), and read replicas sit behind PgBouncer. Re-sharding after production data exists is framed as among the most painful migrations.

## Why it matters

The shard key is a decision whose cost compounds: choose it on day one and distribution stays even; choose it late and re-sharding live data becomes one of the most painful migrations. It is the database-tier instance of the [[scale-cube]]'s Z axis.

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as: shard key chosen on day one; shard by `user_id` via modulo for even distribution; all writes routed through a query router (Vitess/Citus); read replicas behind PgBouncer; re-sharding after production data exists framed as among the most painful migrations.

## Sub-claims and details

- Shard key must be chosen on day one. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Shard by `user_id` via modulo for even distribution. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- All writes routed through a query router (Vitess or Citus). ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Read replicas placed behind PgBouncer. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Re-sharding after production data exists is among the most painful migrations. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- Sourced from a single page; no independent corroboration in the wiki yet.

## Related concepts

- [[scale-cube]] — sharding is the concrete form of the Z axis (data partitioning).
- [[backend-scalability-blueprint]] — the database section of the blueprint.
- [[multi-layer-caching]] — cache layers reduce read load reaching the shards.

## Related entities

- [[wiki/entities/akintola-steve]] — author of the source.

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
