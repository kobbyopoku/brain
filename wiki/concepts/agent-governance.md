---
type: concept
title: Agent Governance
created: 2026-06-06
updated: 2026-06-06
aliases: [agent runtime governance, agent authorization layer]
tags: [agentic-ai, governance, autonomous-agents, runtime-authorization, layer-8]
---

# Agent Governance

> The runtime layer that decides — and enforces — what an autonomous agent is permitted to do, reframed from a prompting problem into a runtime-authorization and legal-authority problem.

## Definition

Agent governance is the control layer (Layer 8 in the 10-layer stack) that constrains an autonomous agent's actions at runtime. [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] argues that the early framing of governance as a *prompting* problem (telling the model what not to do) has collapsed, and that governance is now properly understood as a runtime-authorization and legal-authority problem — enforcement that sits between the agent's intent and the action's execution.

## Why it matters

If agents act with real-world consequences (spending money, signing contracts, mutating systems), an org needs mechanisms that block disallowed actions *before* they execute, not after. The source ties this directly to project survival: ungovernable agentic systems get cancelled.

## Treatment across sources

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] frames it as Layer 8 of the autonomous-agent stack — a runtime authorization and legal-authority problem that replaced the failed "prompting problem" framing.

## Sub-claims and details

- The "governance as a prompting problem" framing collapsed; it is now treated as a runtime authorization + legal authority problem ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- Required mechanisms include: inline policy engines that block before execution; spending limits / delegated authority; approval chains / human-in-the-loop gates; kill switches / rollback ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- Gartner predicts that more than 40% of agentic-AI projects will be cancelled by the end of 2027, attributed to ungovernability ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).

## Open questions and contradictions

- The source distinguishes governance (Layer 8) from AI compliance (Layer 9) and from proof-of-authority (the legal-authority bridge); how cleanly these separate in practice is unsettled.

## Related concepts

- [[wiki/concepts/ai-compliance]] — Layer 9; splits out from governance as its own vendor category.
- [[wiki/concepts/proof-of-authority]] — bridges governance permissions to enforceable legal authority.
- [[wiki/concepts/agent-guardrails]] — narrower, model-side constraint mechanism.
- [[wiki/concepts/human-in-the-loop]] — approval/HITL gates are a governance mechanism.

## Related entities

## Mentioned in

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]
