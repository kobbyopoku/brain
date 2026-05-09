---
type: entity
title: Algebraic Architecture Theory (AAT)
entity_type: product
created: 2026-05-09
updated: 2026-05-09
website: https://github.com/iroha1203/AlgebraicArchitectureTheoryV2
aliases: [AAT, AlgebraicArchitectureTheoryV2]
tags: [open-source, lean, software-architecture, formal-methods, theory, stub]
---

# Algebraic Architecture Theory (AAT)

> Lean library by [[wiki/entities/iroha1203|Hiroyuki Nakahata]] formalizing software-architecture operations (compose / refine / abstract / replace / split / merge / isolate / protect / migrate / reverse / contract / repair / synthesize) as theorem packages with proof obligations. Repository: [`iroha1203/AlgebraicArchitectureTheoryV2`](https://github.com/iroha1203/AlgebraicArchitectureTheoryV2). The theoretical scaffolding under [[attractor-engineering]].

## Profile

This page is a **stub**. AAT appears in the wiki only via Hiroyuki Nakahata's [[wiki/sources/iroha1203-attractor-engineering|Attractor Engineering article]]. The Lean implementation lives at the linked GitHub repo; the wiki has not ingested the source itself, only the dev.to article that summarizes the formalism.

## Key facts

- **Author**: [[wiki/entities/iroha1203|Hiroyuki Nakahata]].
- **Implementation**: Lean.
- **Repo**: `iroha1203/AlgebraicArchitectureTheoryV2`.
- **Vocabulary contributed to wiki**: `ArchitectureCore`, `OperationProofObligation`, `ArchSig` (Architecture Signature), `RequiredDiagram`, trajectory shapes (Stable Orbit / Drift / Spiral Debt / Sudden Phase Shift / Oscillation / Basin Capture).
- **Specific Lean theorem absorbed**: *endpoint-safe + zero-net-delta does not imply path-safe* (the `0 → 2 → 0` excursion case).

## Mentioned in

- [[wiki/sources/iroha1203-attractor-engineering]] — sole canonical source.

## Related entities

- [[wiki/entities/iroha1203]] — author.

## Related concepts

- [[attractor-engineering]] — theory implemented in AAT.
- [[reliability-decay-math]] — adjacent (architecture-decay framing).
- [[lint]] — the wiki-level analogue of the trajectory observation AAT formalizes.
