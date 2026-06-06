---
type: concept
title: Saga Pattern
created: 2026-06-06
updated: 2026-06-06
aliases: [Saga Pattern, sagas]
tags: [backend, distributed-systems, consistency, system-design]
---

# Saga Pattern

> A pattern for managing transactions that span multiple services using a sequence of compensating actions instead of a distributed two-phase commit.

## Definition

The Saga Pattern handles transactions spanning multiple services as a sequence of steps, each with a defined rollback (compensating action) that fires if a downstream step fails. As framed in [[wiki/sources/akintola-steve-backend-1-million-users]], it replaces two-phase commit for cross-service transactions.

## Why it matters

Two-phase commit is impractical across independently deployed services; the Saga Pattern preserves consistency without it by making rollback explicit and per-step. It is the cross-service transaction approach within the consistency section of the [[backend-scalability-blueprint]].

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as: for transactions spanning multiple services, use a sequence of compensating actions instead of two-phase commit; each step has a defined rollback if a downstream step fails.

## Sub-claims and details

- Used for transactions that span multiple services. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Implemented as a sequence of compensating actions rather than two-phase commit. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Each step has a defined rollback that fires if a downstream step fails. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- Sourced from a single page; no independent corroboration in the wiki yet.

## Related concepts

- [[backend-scalability-blueprint]] — cross-service transaction approach within the consistency section.
- [[outbox-pattern]] — paired reliability primitive in the same section.

## Related entities

- [[wiki/entities/akintola-steve]] — author of the source.

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
