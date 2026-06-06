---
type: concept
title: Recommendation algorithm (X For You feed 14-signal scoring)
created: 2026-06-06
updated: 2026-06-06
aliases: [recommendation algorithm, X algorithm, For You feed, X For You algorithm, 14-signal scoring]
tags: [recommendation-systems, social-media, x-twitter, ranking, content-strategy]
---

# Recommendation algorithm (X For You feed 14-signal scoring)

> The ranking model behind X's "For You" feed: it predicts probabilities for a set of user actions on each candidate post, weights each by importance, and sums them into a final score that determines feed placement.

## Definition

As described in [[wiki/sources/doublenickk-personal-x-agent-algorithm]], the X For You feed scores each candidate post by predicting the probability of 14 distinct user actions, multiplying each probability by a private weight, and summing the results:

```
Final Score = Σ weight_i × P(action_i)
```

Positive signals push a post up the feed; negative signals push it down. The action *probabilities* are derived from public behaviour, but the *weights* are private.

## Why it matters

For Godwin's content-strategy and personal-brand surfaces, the algorithm is the object an AI posting agent is optimizing against. Understanding which signals carry the most weight (and which are penalized) is what lets a Voice-Style-Guide-driven agent shape posts toward feed distribution rather than guessing.

## Treatment across sources

- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] frames it as the source's core object — the system a personal X agent must "land in." It enumerates the signal set, the scoring formula, and the named pipeline components, and uses them to derive concrete posting tactics.

## Sub-claims and details

- **Scoring formula**: `Final Score = Σ weight_i × P(action_i)` over 14 predicted user actions ([[wiki/sources/doublenickk-personal-x-agent-algorithm]]).
- **Positive signals**: reply, repost, favorite, follow_author (highest-weighted positive), click, dwell.
- **Negative signals**: not_interested, mute, block, report — these push a post down.
- **Public vs private**: the actions are public (observable behaviour); the weights are private.
- **Named pipeline components**: Home Mixer, Thunder, Phoenix, and a Candidate Pipeline.
- **Author Diversity Scorer**: penalizes flooding (posting too much from one author in a short window).

## Open questions and contradictions

- The exact weight values are private; the source asserts the relative ordering (e.g. follow_author highest) but cannot give numeric weights.
- Whether the named components (Home Mixer / Thunder / Phoenix) and the 14-action set reflect the current production system or a prior open-sourced snapshot is not established by the single source.

## Related concepts

- [[voice-style-guide]] — the artifact the posting agent uses to shape posts toward these signals.
- [[scheduled-automation]] — algorithm-optimal posting times are scheduled against this model.
- [[self-annealing]] — the Optimization Agent rewrites the Voice Style Guide from observed engagement against this algorithm.

## Mentioned in

- [[wiki/sources/doublenickk-personal-x-agent-algorithm]]
