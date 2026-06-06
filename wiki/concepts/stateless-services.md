---
type: concept
title: Stateless Services
created: 2026-06-06
updated: 2026-06-06
aliases: [stateless service, stateless application layer, externalized sessions]
tags: [backend, scalability, architecture, distributed-systems]
---

# Stateless Services

> An architecture rule that application services hold no per-user state in memory, so any instance can serve any request and the death of a server kills no user session.

## Definition

A stateless service keeps no session or request-specific state in its own process memory. State that must persist across requests — notably user sessions — is externalized to a shared store. [[wiki/sources/akintola-steve-backend-1-million-users]] states the rule as: every application service must be stateless, with sessions living in Redis or Dragonfly rather than app memory, so that no user session dies when a server dies.

## Why it matters

If a service holds session state in memory, losing that instance logs users out and prevents requests from being freely load-balanced across instances. Statelessness is what lets a fleet scale horizontally and tolerate instance failure transparently — which is why the source lists it as the first of its four non-negotiable app-layer rules. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as the first of four non-negotiable app-layer rules: every application service must be stateless, with sessions in Redis/Dragonfly and never in app memory, so no user session dies when a server dies.

## Sub-claims and details

- Every application service must be stateless. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Sessions live in Redis or Dragonfly, never in application memory. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Consequence: no user session dies when a server dies. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- It is the first of the source's four non-negotiable app-layer rules. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/idempotency-keys]] — sibling app-layer reliability primitive from the same source.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
