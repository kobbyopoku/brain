---
type: concept
title: Human-in-the-loop
created: 2026-06-06
updated: 2026-06-06
aliases: [human-in-the-loop, HITL, review gate, approval gate]
tags: [ai-agents, agent-design, governance, feedback-loops]
---

# Human-in-the-loop

> A design pattern in which an AI agent does not act fully autonomously but routes its output through a human checkpoint — a review gate, approval step, or feedback interface — before the result is committed or shipped.

## Definition

**Human-in-the-loop** (HITL) keeps a human at a deliberate point in an otherwise automated agent workflow. Across the ingested sources the loop is treated less as a safety afterthought than as a first-class design surface: the agent handles the repeatable bulk of the work, and the human is inserted precisely where judgement, taste, or relationship-risk lives. The design problem is making the human's participation *cheap enough that they keep doing it* — a high-friction gate (a meeting, an assigned task) gets abandoned, while a one-click gate survives.

## Why it matters

For Godwin's product surfaces (Vedge clinical workflows, Kivora/GRC, Clarvyn HR) the question of *where* to keep a human in the loop is load-bearing: it is the difference between an agent that drafts and one that acts irreversibly. The sources converge on a split — agentize the repeatable ~80%, keep the edge/judgement ~20% human — and on a participation-cost discipline that determines whether the loop actually holds in practice.

## Treatment across sources

- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it as a participation-cost design problem: the Slack emoji reaction makes the feedback interface as small as possible ("one click is enough signal"), and every reply is still human-authored. Loops that demand meetings or assigned tasks fail because people stop participating.
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]] frames it as the source's strongest prohibition: "Never auto-post without a review gate." Even Blueprint 03's autonomous stack advises a monthly voice-drift review; Blueprint 02 makes the gate one-tap Telegram approval. Framed as the defense against gradual AI-tone homogenization.
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]] frames it via the Reply Manager, which drafts and waits for operator approval; copy strategy, offer-pivot decisions, and client relationship stay permanently human (the repeatable 80% is agent-ized, the 20% edge/judgement is not).

## Sub-claims and details

- **Participation cost determines survival.** A feedback gate only works if the human's per-event cost is near-zero — a single emoji or one-tap approval, not a meeting or a ticket ([[wiki/sources/petradonka-agents-need-feedback-loops]]).
- **The gate is a defense against homogenization.** Auto-posting without review lets agent output drift toward generic AI tone; a periodic human review (monthly voice-drift check) counters this ([[wiki/sources/doublenickk-personal-x-agent-algorithm]]).
- **80/20 split.** The repeatable bulk is automated; judgement, strategy, and relationship-bearing decisions stay human ([[wiki/sources/itsalexvacca-3-phases-ai-layer]]).
- **Draft-and-wait is the common shape.** Across sources the agent produces a draft and pauses for approval rather than committing — Reply Manager, one-tap Telegram approval, daily PR review.

## Open questions and contradictions

- **Autonomy creep**: Blueprint 03 ([[wiki/sources/doublenickk-personal-x-agent-algorithm]]) loosens the gate to a *monthly* review while still claiming HITL. How thin can the loop get before it stops being human-in-the-loop in any meaningful sense?
- **Where the line sits is domain-specific**: the "keep the 20% human" rule is asserted, not derived. No source gives a method for deciding which 20%.

## Related concepts

- [[self-annealing]] — HITL is the review-gated variant: corrections feed the directive, but a human approves the commit.
- [[compounding-judgement]] — the goal HITL serves: human judgement compounds into the agent rather than being removed.
- [[scheduled-automation]] — tension: scheduled runs default to no gate; some should produce a draft for review instead.
- [[markdown-as-agent-contract]] — the contract can encode where the gate sits.

## Related entities

- [[wiki/entities/claude-code]] — the platform several of these gated workflows run on.

## Mentioned in

- [[wiki/sources/petradonka-agents-need-feedback-loops]]
- [[wiki/sources/doublenickk-personal-x-agent-algorithm]]
- [[wiki/sources/itsalexvacca-3-phases-ai-layer]]
