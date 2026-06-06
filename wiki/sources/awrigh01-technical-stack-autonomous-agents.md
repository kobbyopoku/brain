---
type: source
title: awrigh01 — The Technical Stack for Autonomous Agents (3 Planes, 10 Layers)
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/awrigh01/status/2056841869594918918
source_type: x-thread
author: awrigh01
source_date: 2026-05-19
raw_path: raw/The Technical Stack for Autonomous Agents..md
content_status: substantive-verbatim
tags: [autonomous-agents, agent-economy, agentic-capital-markets, erc-8004, agent-identity, agent-reputation, agent-settlement, agent-governance, ai-compliance, agent-orchestration, infrastructure-thesis, crypto, payments]
---

# awrigh01 — The Technical Stack for Autonomous Agents (3 Planes, 10 Layers)

> A market-infrastructure thesis: for autonomous agents to become a real asset class they must *transact*, not just generate output — which requires a 3-plane, 10-layer stack (trust / market / control) that does not yet compose into a coherent marketplace.

## TL;DR

awrigh01 argues that conversations about agents focus on models, copilots, and workflows, but markets do not run on intelligence — they run on identity, trust, pricing, contracts, settlement, enforcement, and policy. The piece decomposes the missing infrastructure into **three planes and ten layers**: the *trust plane* (identity, discovery, reputation), the *market plane* (quoting, contracting, settlement, dispute resolution), and the *control plane* (governance, compliance, orchestration/runtime). Pieces already exist as fragments — [[wiki/entities/erc-8004|ERC-8004]] as a shared trust substrate, payment primitives, observability and identity tools, policy "control planes" — but nothing composes them yet. The strategic claim: **whoever owns identity, settlement, and governance owns the marketplace** for machine labor, and they will look "less like OpenAI and more like Visa, Moody's, Stripe, Nasdaq, and ServiceNow fused."

## Key takeaways

- **The thesis: agents must transact to be an asset class.** Generating output is not enough — agents must "find counterparties, make commitments, move money, build a track record, survive disputes, and stay inside the bounds of what its principal actually authorized." Strip away identity/trust/pricing/contracts/settlement/enforcement/policy and "you do not have an economy. You have a demo."
- **The framework: 3 planes, 10 layers.** Trust plane (who the agent is and what it has done), market plane (how value clears between agents), control plane (what the agent is allowed to do, what regulators require, and how multi-agent work coordinates at runtime).
- **The 10 layers compose sequentially.** Identity → reputation → pricing → contracting → settlement; settlement + governance → enforceable disputes. Each is a real product; several are "real companies that don't yet exist."
- **Layer 1 — Identity (Know-Your-Agent).** Current state is "identifiers without identity": an agent claims to be `gpt-4.1-claims-processor-v3` and you cannot verify weights, system prompt, or tool access. Needs model-lineage attestations, signed tool-permission manifests, and persistent agent DIDs ([[wiki/entities/cheqd|Cheqd]], [[wiki/entities/sphereon|Sphereon]] are early).
- **Layer 2 — Discovery / Capability Registry.** Today is "a flat list on a webpage with no machine-readable capability surface." Needs structured capability declarations (typed inputs/outputs/latency-SLA/jurisdiction), semantic search over them, and live availability + pricing. [[wiki/entities/model-context-protocol|MCP]] and [[wiki/entities/a2a-protocol|Google's A2A]] are interop foundations, not marketplaces.
- **Layer 3 — Reputation.** Agent work is not commoditized, so markets clear on reputation. Needs cryptographically attested outcome track records, cross-marketplace portability (today blocked because "reputation is the moat"), and Sybil resistance (staked collateral / behavioral fingerprinting). The boring enterprise opening: "Moody's for Machines" — a rating agency consuming the reputation registry — does not exist yet.
- **Layer 4 — Quoting / Price Discovery (the most undervalued layer).** "Does not exist anywhere today and is the most economically interesting." Inference is cheap; the interesting price is "per result of acceptable quality." Needs real-time RFQ ("Tradeweb for cognitive work"), outcome contracts with verifiable completion, and auction mechanics (ad-tech / programmatic-exchange blueprint). TAM "measured in low-trillions of dollars of cognitive labor."
- **Layer 5 — Contracting.** Turns a quote into an obligation; "not settlement." Needs machine-readable MSAs ([[wiki/entities/eip-712|EIP-712]] typed data is the cryptographic primitive; the legal layer is unbuilt), encoded SLAs with signed eval prompts, proof of authority (consumed from governance/Layer 8), termination conditions, and state transitions. A real contract looks "less like a PDF and more like a hybrid object: part legal agreement, part workflow schema, part policy bundle" — a portable execution wrapper for the job.
- **Layer 6 — Settlement.** Money moves on agent timescales (per-call/per-result/per-second), not Net-30. Three rails: stablecoins ([[wiki/entities/coinbase|Coinbase]] x402, [[wiki/entities/stripe|Stripe]]'s Bridge acquisition, [[wiki/entities/circle|Circle]] CCTP), agent-issued cards ([[wiki/entities/visa|Visa]] Intelligent Commerce, [[wiki/entities/mastercard|Mastercard]] Agent Pay, Stripe Issuing), and ACH/direct-debit ([[wiki/entities/mercury|Mercury]], [[wiki/entities/brex|Brex]], [[wiki/entities/column-bank|Column Bank]]). "No single rail wins"; whoever builds the abstraction layer — `pay(amount, currency, counterparty, settlement_window)` picking the cheapest rail — wins the developer surface.
- **Layer 7 — Dispute Resolution.** Needs escrow-as-default, automated remediation paths (quality-below-threshold → automatic refund), and validators/arbitration agents. [[wiki/entities/erc-8004|ERC-8004]]'s Validation Registry is the standardized hook, "deliberately unopinionated" about validation method (stake-secured re-execution, zkML proofs, TEE attestations, or human-in-the-loop). [[wiki/entities/kleros|Kleros]]-style crypto dispute markets "were too early and built for the wrong customer."
- **Layer 8 — Governance and Authority.** Once a prompting problem ("write a better system prompt"); that framing "has collapsed." Now a runtime authorization + legal authority problem. Needs inline policy engines that block before execution, spending limits / delegated authority (mostly shipped first on the crypto side — [[wiki/entities/safe-wallet|Safe]] modules, Zodiac roles, ERC-4337 session keys, MPC wallets from [[wiki/entities/turnkey|Turnkey]] / [[wiki/entities/privy|Privy]] / [[wiki/entities/fireblocks|Fireblocks]]), approval chains / human-in-the-loop gates, kill switches/rollback, and proof of authority downstream layers consume.
- **Layer 9 — Compliance.** Splitting out from governance as its own vendor category, driven by the [[wiki/entities/eu-ai-act|EU AI Act]] high-risk obligations (effective August 2, 2026; Article 99 penalties up to €35M or 7% of global turnover). Governance asks "what is the org willing to let the agent do?"; compliance asks "what must the org prove to a regulator after the fact?" Same observability stream, different buyer (general counsel vs CISO).
- **Layer 10 — Orchestration and Runtime (split, not one layer).** Runtime ([[wiki/entities/modal|Modal]], [[wiki/entities/e2b|E2B]], [[wiki/entities/daytona|Daytona]], OpenAI Agents SDK), Memory ([[wiki/entities/mem0|Mem0]], [[wiki/entities/letta|Letta]], [[wiki/entities/zep|Zep]]), Observability ([[wiki/entities/langfuse|Langfuse]], [[wiki/entities/helicone|Helicone]], [[wiki/entities/arize|Arize]], [[wiki/entities/braintrust|Braintrust]], [[wiki/entities/langsmith|LangSmith]]), and Orchestration ([[wiki/entities/langgraph|LangGraph]], [[wiki/entities/crewai|CrewAI]], [[wiki/entities/autogen|AutoGen]], OpenAI Swarm, [[wiki/entities/google-adk|Google ADK]], Anthropic Skills, Semantic Kernel). "OpenTelemetry-for-agents is the missing standard."
- **ERC-8004 is the connective thread.** A draft Ethereum standard (published August 2025) with authors from [[wiki/entities/metamask|MetaMask]], the [[wiki/entities/ethereum-foundation|Ethereum Foundation]], [[wiki/entities/google|Google]], and [[wiki/entities/coinbase|Coinbase]] — an author list spanning crypto-native and enterprise-native camps. Defines an Identity Registry (ERC-721 NFT per agent), Reputation Registry, and Validation Registry; sits on top of MCP and A2A. AgentProof reports 128,000+ agents registered across 24 chains as of early 2026.
- **Strategic claim — the platform play now requires three layers, not two.** "A year ago I would have said whoever owns identity and settlement wins." Now governance has earned a seat because enterprises cannot deploy without it and the legal-authority primitive must live somewhere. New claim: **whoever owns identity, settlement, and governance owns the marketplace.**
- **Crypto-native and enterprise-native stacks converge at the trust plane, diverge at the control plane.** ERC-8004 is the convergence story (Coinbase + Google co-authoring). Governance is the divergence: crypto = Safe modules / on-chain timelocks / session keys; enterprise = [[wiki/entities/cordum|Cordum]] / [[wiki/entities/galileo-ai|Galileo]] / Microsoft's toolkit / [[wiki/entities/airia|Airia]]. For the next five years more dollars flow through the enterprise side, "but the second is now reading from the first's identity and reputation layer."

## Notable quotes

> "They run on identity, trust, pricing, contracts, settlement, enforcement, and policy. Strip those away and you do not have an economy. You have a demo."

> "Whoever assembles them first will not just build a useful product. They will own the transaction rails of machine labor."

> "SaaS prices the tool, agents price the outcome."

> "Machines will execute exactly what is encoded and nothing that is merely implied."

> "Without that, every agent-signed contract is one ultra vires claim away from worthless."

> "The prize is not another app store for prompts. It is the transaction layer for machine labor."

> "The company that wins it ... will look like a market operator: part exchange, part payments network, part identity provider, part trust infrastructure, part governance platform. In other words, less like OpenAI and more like Visa, Moody's, Stripe, Nasdaq, and ServiceNow fused into a single system for software actors."

## Notes

- **Genre.** This is an infrastructure-thesis / market-map essay, not a how-to. It is the most macro, market-structure-oriented agent source in the wiki so far — where most agent content here is operational (Claude Code agents, Hermes, multi-agent ops platforms), this one asks what *rails* let one software actor reliably transact with another. It sits one abstraction level above [[wiki/concepts/multi-agent-orchestration]] and the [[wiki/concepts/do-framework|DOE framework]]: those describe how to *build* an agent system; this describes the *market* such systems would transact inside.
- **Relevance to Godwin's interests.** Strong fit with the wiki owner's clusters: agentic architecture, multi-tenant SaaS, GRC/compliance, and infrastructure. Layers 8-9 (governance + compliance) map directly onto [[wiki/projects/kivora|Kivora]] (ROAM GRC) — the "audit-grade logging" and "EU AI Act runtime enforcement" framing is the same problem space Kivora addresses, extended to agent actors. Layer 10's observability/runtime split is relevant to [[wiki/projects/helm|Helm]]'s runtime choices.
- **Self-aware about uncertainty.** The author explicitly flags this is "not the final architecture" — boundaries between layers are soft and names will shift. The completionist entity coverage below treats named vendors as citable mentions, not endorsements; many are positioned as "stealthed," "early," or "does not yet exist as a category-defining product."
- **ERC-8004 is the load-bearing standard.** It is named as the thread running through the trust plane (identity / discovery / reputation) and into the market plane (validation/disputes). The wiki should track whether inference providers (Anthropic/OpenAI) sign attestations *into* the registry directly — the author calls today's operator self-attestation "the soft underbelly of the whole stack."
- **Layer 4 (quoting) is the author's explicit highest-conviction undervalued bet** — analogized to programmatic ad exchanges that "built three of the largest companies of the last twenty years."
- **Legal-authority thread.** Cites the Air Canada Civil Resolution Tribunal ruling (Feb 2024) holding the airline liable for its chatbot's promise, and the Arbel/Goldstein/Salib paper "How to Count AIs: Individuation and Liability for AI Agents" (2026), plus law firms Venable, DLA Piper, Frankfurt Kurnit publishing on agentic-AI liability. Worth a concept page ([[wiki/concepts/proof-of-authority]] / ultra-vires) — genuinely unsolved per the author.
- **Many named vendors are thin mentions** and should become stubs (Cheqd, Sphereon, Cordum, Aegis AI, Assury Enforce, ComplyEdge, etc.). Some overlap with existing wiki entities ([[wiki/entities/coinbase|Coinbase]], [[wiki/entities/stripe|Stripe]], [[wiki/entities/mastercard|Mastercard]], [[wiki/entities/google|Google]], [[wiki/entities/langgraph|LangGraph]], [[wiki/entities/crewai|CrewAI]], [[wiki/entities/model-context-protocol|MCP]]).

## Mentioned entities

### Standards / protocols
- [[wiki/entities/erc-8004]] — the connective trust substrate (Identity / Reputation / Validation registries); the source's load-bearing standard.
- [[wiki/entities/model-context-protocol]] — interop foundation for discovery (existing wiki entity).
- [[wiki/entities/a2a-protocol]] — Google's agent-to-agent interop protocol; discovery foundation alongside MCP.
- [[wiki/entities/eip-712]] — Ethereum typed-data primitive named as the basis for machine-readable MSAs.
- [[wiki/entities/eu-ai-act]] — regulatory driver splitting compliance into its own layer.

### Payments / settlement
- [[wiki/entities/coinbase]] — x402 stablecoin protocol; ERC-8004 co-author (existing wiki entity).
- [[wiki/entities/stripe]] — Bridge acquisition + Stripe Issuing virtual cards (existing wiki entity).
- [[wiki/entities/circle]] — CCTP stablecoin rail.
- [[wiki/entities/visa]] — Visa Intelligent Commerce agent cards.
- [[wiki/entities/mastercard]] — Mastercard Agent Pay (existing wiki entity).
- [[wiki/entities/mercury]] — direct-debit/ACH rail (distinct from the Mercury design brand).
- [[wiki/entities/brex]] — direct-debit/ACH rail.
- [[wiki/entities/column-bank]] — direct-debit/ACH rail.

### Identity / DID
- [[wiki/entities/cheqd]] — early persistent agent-DID provider.
- [[wiki/entities/sphereon]] — early persistent agent-DID provider.
- [[wiki/entities/metamask]] — ERC-8004 co-author.
- [[wiki/entities/ethereum-foundation]] — ERC-8004 co-author.
- [[wiki/entities/google]] — ERC-8004 co-author; A2A and ADK author (existing wiki entity).
- [[wiki/entities/agentproof]] — reports 128k+ agents registered on ERC-8004; building on its reputation primitives.

### Governance (crypto-native)
- [[wiki/entities/safe-wallet]] — Safe allowance/Zodiac modules; 2-of-4 multisig for agent treasuries.
- [[wiki/entities/turnkey]] — MPC wallet provider for agent governance.
- [[wiki/entities/privy]] — MPC wallet provider.
- [[wiki/entities/fireblocks]] — MPC wallet provider.

### Governance / compliance (enterprise-native)
- [[wiki/entities/cordum]] — agent "control plane" / policy engine vendor.
- [[wiki/entities/aegis-ai]] — policy engine vendor.
- [[wiki/entities/assury-enforce]] — policy engine vendor.
- [[wiki/entities/galileo-ai]] — Galileo Agent Control; control-plane vendor.
- [[wiki/entities/airia]] — enterprise agent-governance vendor.
- [[wiki/entities/policylayer]] — inline policy engine.
- [[wiki/entities/complyedge]] — open-source EU AI Act runtime enforcement layer.

### Runtime / memory / observability / orchestration (Layer 10)
- [[wiki/entities/modal]] — agent runtime.
- [[wiki/entities/e2b]] — agent runtime sandbox.
- [[wiki/entities/daytona]] — agent runtime.
- [[wiki/entities/mem0]] — agent memory layer.
- [[wiki/entities/letta]] — agent memory layer (née MemGPT).
- [[wiki/entities/zep]] — agent memory layer.
- [[wiki/entities/langfuse]] — agent observability.
- [[wiki/entities/helicone]] — agent observability.
- [[wiki/entities/arize]] — agent observability.
- [[wiki/entities/braintrust]] — agent observability/eval.
- [[wiki/entities/langsmith]] — agent observability.
- [[wiki/entities/langgraph]] — orchestration framework (existing wiki entity).
- [[wiki/entities/crewai]] — orchestration framework (existing wiki entity).
- [[wiki/entities/autogen]] — orchestration framework.
- [[wiki/entities/google-adk]] — Google Agent Development Kit; orchestration.
- [[wiki/entities/kleros]] — crypto-native dispute-resolution market; cited as "too early."

### Author / people
- [[wiki/entities/awrigh01]] — author of the technical-stack thesis.

## Related concepts

- [[wiki/concepts/agentic-capital-markets]] — *(new)* the market-infrastructure framing this source defines; agents as autonomous economic counterparties.
- [[wiki/concepts/agent-identity]] — *(new)* Know-Your-Agent: model-lineage attestations, tool-permission manifests, persistent DIDs (Layer 1).
- [[wiki/concepts/agent-reputation]] — *(new)* attested outcome track records, cross-marketplace portability, Sybil resistance (Layer 3).
- [[wiki/concepts/agent-settlement]] — *(new)* multi-rail payment abstraction for agent-to-agent value transfer (Layer 6).
- [[wiki/concepts/agent-governance]] — *(new)* runtime authorization + legal authority; inline policy engines, spending limits, kill switches (Layer 8).
- [[wiki/concepts/proof-of-authority]] — *(new)* machine-readable signed declaration of what an agent may bind its principal to; ultra-vires risk (Layers 5/8).
- [[wiki/concepts/ai-compliance]] — *(new)* what an org must prove to a regulator after the fact; EU AI Act runtime enforcement (Layer 9).
- [[wiki/concepts/multi-agent-orchestration]] — the source's Layer 10 orchestration split refines this existing concept (runtime vs orchestration as separate procurement).
- [[wiki/concepts/mcp-server]] — MCP/A2A as interop foundations for the discovery layer.
- [[wiki/concepts/reasoning-execution-split]] — the contracting/settlement separation echoes the broader reason-vs-execute discipline.

## Related sources

- [[wiki/sources/nousresearch-hermes-agent]] — Hermes is an agent *runtime* (Layer 10); this source is the market the runtime would transact inside.
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — tool-layer reliability ("model as reasoning engine, not execution engine"); the micro to this source's macro.
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — agent-vs-automation judgment framing; complements this source's "autonomous counterparty" thesis.
- [[wiki/sources/saraev-agentic-workflows-2026]] — DOE framework + reliability-decay math; the build-side companion to this market-side map.
