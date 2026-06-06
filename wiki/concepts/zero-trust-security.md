---
type: concept
title: Zero-Trust Security
created: 2026-06-06
updated: 2026-06-06
aliases: [zero trust, mtls between services, never trust always verify]
tags: [backend, security, distributed-systems, architecture]
---

# Zero-Trust Security

> An internal-network security model in which no service trusts another by default, regardless of origin, and all traffic is mutually authenticated and encrypted.

## Definition

Zero-trust security assumes the internal network is hostile: a service must not be trusted simply because it sits inside the perimeter. [[wiki/sources/akintola-steve-backend-1-million-users]] applies this as mTLS between all internal services, no service trusting another by default regardless of origin, and encryption both at rest and in transit everywhere.

## Why it matters

Perimeter-based security treats anything inside the network as trusted, so a single breached service can move laterally unchallenged. Zero-trust removes that implicit trust, requiring every internal call to authenticate, which contains the blast radius of any compromise. The source presents this as its internal-network security model. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Treatment across sources

- [[wiki/sources/akintola-steve-backend-1-million-users]] frames it as the internal-network security model: mTLS between all internal services, no service trusting another by default regardless of origin, and encryption at rest and in transit everywhere.

## Sub-claims and details

- mTLS is used between all internal services. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- No service trusts another by default, regardless of origin. ([[wiki/sources/akintola-steve-backend-1-million-users]])
- Encryption applies both at rest and in transit, everywhere. ([[wiki/sources/akintola-steve-backend-1-million-users]])

## Open questions and contradictions

- None surfaced in the wiki yet — single-source coverage.

## Related concepts

- [[wiki/concepts/stateless-services]] — sibling architectural rule from the same source.

## Related entities

- (none yet)

## Mentioned in

- [[wiki/sources/akintola-steve-backend-1-million-users]]
