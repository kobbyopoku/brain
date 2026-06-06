---
type: concept
title: AI Compliance
created: 2026-06-06
updated: 2026-06-06
aliases: [ai compliance, agentic compliance, eu ai act compliance]
tags: [agentic-ai, compliance, governance, regulation, eu-ai-act, layer-9]
---

# AI Compliance

> The layer concerned with what an organization must prove to a regulator after the fact about its agents' behavior — distinct from governance, which decides what the org will let the agent do.

## Definition

AI compliance is Layer 9 of the autonomous-agent stack, splitting out from agent governance as its own vendor category. [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] distinguishes the two by question: governance asks *what the org will let the agent do*; compliance asks *what the org must prove to a regulator after the fact*.

## Why it matters

Regulation (specifically the EU AI Act, per the source) is creating a buyer and a market separate from runtime governance — evidentiary record-keeping aimed at regulators rather than real-time enforcement.

## Treatment across sources

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] frames it as Layer 9, a vendor category splitting from governance, driven by the EU AI Act, analogous to how Sarbanes-Oxley built the GRC industry.

## Sub-claims and details

- Compliance is splitting out from governance as its own vendor category, driven by the EU AI Act ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- Governance and compliance share the same observability stream but differ on buyer (general counsel vs CISO) and SLA (evidentiary completeness vs real-time enforcement) ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- The source draws an analogy to how SOX (Sarbanes-Oxley) built the GRC industry ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).

## Open questions and contradictions

- Whether governance (Layer 8) and compliance (Layer 9) consolidate under one vendor or remain distinct categories with distinct buyers is unsettled.

## Related concepts

- [[wiki/concepts/agent-governance]] — Layer 8; the category compliance splits from.
- [[wiki/concepts/proof-of-authority]] — sibling legal-authority concern.
- [[wiki/concepts/observability]] — both governance and compliance draw on the same observability stream.

## Related entities

## Mentioned in

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]
