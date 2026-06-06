---
type: concept
title: Scale Cube
created: 2026-06-06
updated: 2026-06-06
aliases: [Scale Cube, AKF Scale Cube]
tags: [backend, architecture, scalability, system-design]
---

# Scale Cube

> A three-axis mental model for scaling a system, where each axis represents an orthogonal way to add capacity.

## Definition

The Scale Cube describes three orthogonal scaling axes: **X** — horizontal duplication (more identical servers); **Y** — functional decomposition (split into focused services); and **Z** — data partitioning (shard by user ID or region). As framed in [[wiki/sources/akintola-steve-backend-1-million-users]], it is the mental model that prevents "90% of scaling disasters."

## Why it matters

It separates three distinct scaling moves that are easy to conflate, making it possible to reason about which axis a given bottleneck actually requires. The model underpins the database and application-layer sections of the [[backend-scalability-blueprint]].

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as three orthogonal scaling axes — X (horizontal duplication / more identical servers), Y (functional decomposition / split into focused services), Z (data partitioning / shard by user ID or region) — presented as the mental model that prevents "90% of scaling disasters."

## Sub-claims and details

- **X axis** — horizontal duplication: add more identical servers. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- **Y axis** — functional decomposition: split the system into focused services. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- **Z axis** — data partitioning: shard by user ID or region. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- The model is credited with preventing "90% of scaling disasters." ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- Sourced from a single page; no independent corroboration in the wiki yet.

## Related concepts

- [[backend-scalability-blueprint]] — the blueprint that uses the Scale Cube as its reasoning model.
- [[database-sharding]] — a concrete instance of the Z axis (data partitioning).

## Related entities

- [[wiki/entities/akintola-steve]] — author of the source.

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
