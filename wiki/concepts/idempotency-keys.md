---
type: concept
title: Idempotency Keys
created: 2026-06-06
updated: 2026-06-06
aliases: [idempotency key, request id deduplication, idempotent retries]
tags: [backend, reliability, distributed-systems, api-design]
---

# Idempotency Keys

> A unique identifier attached to a mutating request so that retrying it produces the same result exactly once, rather than applying the change multiple times.

## Definition

An idempotency key is a client-supplied unique request ID carried on every mutating operation. The server records the key together with the outcome of the operation; if a request bearing a key it has already processed arrives again, the server returns the original result instead of re-executing the mutation. This makes retries safe over networks where a request may succeed but its acknowledgement may be lost. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Why it matters

On unreliable networks a client cannot tell the difference between "the request failed" and "the request succeeded but the response was lost," so it retries — and naive retries double-apply side effects (double charges, duplicate orders). [[wiki/sources/akintola-steve-backend-1-million-users]] frames idempotency keys as "the only safe way to handle retries on unreliable networks," making them a precondition for any at-least-once delivery system that touches state.

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as the only safe way to handle retries on unreliable networks: every mutating operation accepts a unique request ID, and a duplicate request returns the original result rather than re-applying the change.

## Sub-claims and details

- Every mutating operation accepts a unique request ID. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- A duplicate request (same ID) returns the original result rather than re-executing the mutation. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Positioned as the safe mechanism for retries specifically on unreliable networks. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/dual-write-rollout]] — relies on idempotency so a replayed or retried write is safe to repeat.
- [[wiki/concepts/stateless-services]] — sibling app-layer reliability primitive from the same source.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
