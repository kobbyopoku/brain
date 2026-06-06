---
type: concept
title: Skills as code
created: 2026-06-06
updated: 2026-06-06
aliases: [agent instructions as code, skills in version control]
tags: [agents, agent-skills, governance]
---

# Skills as code

> The practice of keeping agent instructions that govern production behaviour in a code repository — with version history, review, and rollbacks — so that an agent's self-improvement ships as a reviewed pull request rather than an ungoverned self-edit.

## Definition

**Skills as code** is the governance pattern argued by [[wiki/sources/petradonka-agents-need-feedback-loops]]: agent instructions that determine production behaviour should live in a repo with version history, review, and rollbacks. Self-improvement is shipped as a reviewed pull request that shows the feedback, the proposed principle, and the exact diff. The source presents this as the answer to the objection *"do you want an agent rewriting its own instructions?"*

## Why it matters

It resolves the tension between letting an agent learn from feedback and keeping a human in control. By routing instruction changes through the same repo mechanics engineers already trust — diffs, review, rollback — self-improvement becomes auditable and reversible rather than opaque. It is the operational complement to the source's [[principles-over-rules]] and [[agent-feedback-loop]] arguments.

## Treatment across sources

- [[wiki/sources/petradonka-agents-need-feedback-loops]] frames it as: agent instructions that determine production behaviour should live in a repo with version history, review, and rollbacks; self-improvement is shipped as a reviewed PR showing feedback + proposed principle + exact diff — the governance answer to *"do you want an agent rewriting its own instructions?"*

## Sub-claims and details

- Production-governing agent instructions should live in a repo with version history, review, and rollbacks. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- Self-improvement ships as a reviewed pull request. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- The PR shows the feedback, the proposed principle, and the exact diff. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])
- It is positioned as the governance answer to the concern about an agent rewriting its own instructions. (per [[wiki/sources/petradonka-agents-need-feedback-loops]])

## Open questions and contradictions

- (none surfaced by current sources)

## Related concepts

- [[agent-feedback-loop]] — the loop produces the feedback that becomes a PR.
- [[principles-over-rules]] — what the PR proposes is a principle, not a new rule.

## Related entities

- [[wiki/entities/petra-donka]]

## Mentioned in

- [[wiki/sources/petradonka-agents-need-feedback-loops]]
