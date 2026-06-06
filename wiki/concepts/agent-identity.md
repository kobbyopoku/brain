---
type: concept
title: Agent Identity (Know-Your-Agent)
created: 2026-06-06
updated: 2026-06-06
aliases: [Know-Your-Agent, KYA, agent DID]
tags: [autonomous-agents, agent-economy, identity, trust-plane]
---

# Agent Identity (Know-Your-Agent)

> Layer 1 of the agentic capital markets stack: the problem of giving autonomous agents real, attestable identity rather than bare identifiers.

## Definition

Agent Identity, or Know-Your-Agent, is Layer 1 of the agentic capital markets stack in [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]. The current state is characterized as "identifiers without identity." A functioning layer needs model-lineage attestations, signed tool-permission manifests, and persistent agent DIDs. ERC-8004's Identity Registry (an ERC-721 NFT) is identified as the most concrete standardization attempt, while operator self-attestation today is called "the soft underbelly of the whole stack."

## Why it matters

Identity is the trust-plane foundation: without attestable identity, the higher layers (reputation, contracting, settlement) cannot reliably bind to a known counterparty. It is where the stack is weakest today, which makes it both a risk and an opening.

## Treatment across sources

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]] frames it as Layer 1; current state is "identifiers without identity"; needs model-lineage attestations, signed tool-permission manifests, and persistent agent DIDs; ERC-8004's Identity Registry (ERC-721 NFT) is the most concrete standardization attempt; operator self-attestation today is "the soft underbelly of the whole stack."

## Sub-claims and details

- Agent Identity is Layer 1 of the stack ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- Current state is "identifiers without identity" ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- A functioning layer needs model-lineage attestations, signed tool-permission manifests, and persistent agent DIDs ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- ERC-8004's Identity Registry uses an ERC-721 NFT and is the most concrete standardization attempt ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).
- Operator self-attestation today is "the soft underbelly of the whole stack" ([[wiki/sources/awrigh01-technical-stack-autonomous-agents]]).

## Open questions and contradictions

- Reliance on operator self-attestation is flagged as a structural weakness without a settled fix.

## Related concepts

- [[wiki/concepts/agentic-capital-markets]] — the parent stack (Layer 1).
- [[wiki/concepts/agent-reputation]] — Layer 3, which builds on identity.
- [[wiki/concepts/agent-settlement]] — Layer 6, which presupposes identified counterparties.
- [[wiki/concepts/zero-trust-security]] — adjacent trust framing.

## Related entities

## Mentioned in

- [[wiki/sources/awrigh01-technical-stack-autonomous-agents]]
