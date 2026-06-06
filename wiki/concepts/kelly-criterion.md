---
type: concept
title: Kelly Criterion
created: 2026-06-06
updated: 2026-06-06
aliases: [Kelly criterion, Kelly formula, optimal bet sizing]
tags: [trading, finance, probability, strategy, stub]
---

# Kelly Criterion

> A position-sizing rule giving the optimal fraction of capital to wager as f* = (p·b − q)/b, where p is win probability, q = 1 − p, and b the payoff odds.

## Why it matters

Appears in this wiki via [[wiki/sources/retrochainer-claude-700k-musk-tweets]] as the math governing position sizing across both legs of a barbell trading strategy.

## Treatment across sources

- [[wiki/sources/retrochainer-claude-700k-musk-tweets]] frames it as the position-sizing math governing both barbell layers; the formula is given as f* = (p·b − q)/b with q = 1 − p. Market making (high p, small b) implies trade often, size small; lottery tickets (tiny p, huge b) imply bet almost nothing but bet.

## Sub-claims and details

- Formula: f* = (p·b − q)/b, with q = 1 − p. ([[wiki/sources/retrochainer-claude-700k-musk-tweets]])
- High p / small b (market making) → trade often, size small. ([[wiki/sources/retrochainer-claude-700k-musk-tweets]])
- Tiny p / huge b (lottery tickets) → bet almost nothing, but bet. ([[wiki/sources/retrochainer-claude-700k-musk-tweets]])

## Open questions and contradictions

## Related concepts

- [[wiki/concepts/barbell-strategy]] — Kelly sizes positions within both barbell legs.
- [[wiki/concepts/market-making]] — the high-p / small-b application of the formula.

## Related entities

## Mentioned in

- [[wiki/sources/retrochainer-claude-700k-musk-tweets]]
