---
type: concept
title: Forward Deployed Engineering
created: 2026-06-06
updated: 2026-06-06
aliases: [FDE, forward deployed engineer]
tags: [ai-services, engineering-role, deployment, palantir]
---

# Forward Deployed Engineering

> A delivery role in which a highly skilled engineer is placed on-site with a customer to understand their problems deeply, write code into the customer's unfamiliar codebase, and communicate business impact to non-technical decision-makers.

## Definition

**Forward Deployed Engineering (FDE)** names both a role and a delivery model. The forward deployed engineer is deployed on-site with a customer, learns that customer's workflows and pain in depth, builds directly into an unfamiliar codebase, and translates technical work into business impact for skeptical, non-technical buyers. [[wiki/sources/vasuman-forward-deployed-engineering-101]] calls the role *"a million-dollar hire"* and traces its origin to [[wiki/entities/palantir|Palantir]].

The job decomposes into three phases:

1. **Audit** — map the customer's workflows and decide what to automate (the source gives three rules for the decision).
2. **Evals** — prove the agent works to skeptical executives (see [[agent-evals]]).
3. **Deployment** — build over existing data, sandbox first, and ship the smallest unit of autonomy.

## Why it matters

The source's thesis is that **intelligence is commoditizing**, so *placement* — being deployed where the problem lives, with the access and trust to solve it — becomes the only durable edge. For a builder selling AI work, FDE reframes the value-add away from model access and toward proximity, customer understanding, and the ability to prove ROI to a buyer. This is the wiki's canonical introduction to the concept.

## Treatment across sources

- [[wiki/sources/vasuman-forward-deployed-engineering-101]] frames it as the central subject and the wiki's canonical introduction: FDE = a highly skilled engineer deployed on-site with a customer who understands their problems deeply, writes code into unfamiliar codebases, and communicates business impact to non-technical decision-makers (*"a million-dollar hire"*). Originated at Palantir. Three-phase job: Audit (map workflows, decide what to automate via 3 rules), Evals (prove the agent works to skeptical executives), Deployment (build over existing data, sandbox, ship smallest unit of autonomy first). Thesis: intelligence is commoditizing, so placement is the only edge.

## Sub-claims and details

- **Origin**: the role originated at [[wiki/entities/palantir|Palantir]] ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Audit phase** decides what to automate using three rules ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Deployment discipline**: build over existing data, sandbox, and ship the smallest unit of autonomy first ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Strategic thesis**: intelligence is commoditizing, so placement is the only edge ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).

## Open questions and contradictions

- The source profiles the individual-engineer role; how FDE scales into a firm-level offering is left to the [[ai-automation-services]] frame.

## Related concepts

- [[agent-evals]] — phase 2 of the FDE job; proving the agent works to executives.
- [[ai-automation-services]] — the firm-level model; FDE is its individual-engineer delivery unit.
- [[multi-agent-orchestration]] — the source's Checkpoint-3 covers multi-agent pipelines an FDE may deploy.

## Related entities

- [[wiki/entities/palantir]] — where the role originated.

## Mentioned in

- [[wiki/sources/vasuman-forward-deployed-engineering-101]]
