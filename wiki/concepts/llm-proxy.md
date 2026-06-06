---
type: concept
title: LLM proxy
created: 2026-06-06
updated: 2026-06-06
aliases: [llm-gateway, ai-gateway, centralized-llm-gateway]
tags: [llm-infrastructure, gateway, cost-control, observability, enterprise, proxy-pattern]
---

# LLM proxy

> A centralized gateway that routes every AI request through one layer, enabling cost control, usage analytics, and model routing/swapping without changing the workflow of the engineers issuing the requests.

## Definition

An **LLM proxy** is a single intermediary layer that all of an organization's AI requests pass through. By sitting between request originators (engineers, applications) and upstream model providers, it becomes a control plane: it can meter and cap cost, aggregate usage analytics, and route or swap the underlying model — all transparently to the caller. Per [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]], Shopify's internal LLM proxy is the canonical worked example of this pattern at enterprise scale.

## Why it matters

At organizational scale, ungoverned direct-to-provider AI traffic offers no cost ceiling, no usage visibility, and no central point to change models. An LLM proxy converts a sprawl of independent calls into one governed surface — the same architectural move that BYOK proxies make for credentials, generalized into an org-wide control plane. It lets a central team change models or enforce budgets without touching individual engineers' workflows.

## Why it matters (relation to BYOK proxy)

This page generalizes [[byok-proxy]]. The BYOK proxy is the BYOK-specific instance (user-supplied keys, SSE normalization, SSRF blocking); the LLM proxy is the broader enterprise-control-plane framing where the central concerns are cost, analytics, and model-swapping rather than key passthrough.

## Treatment across sources

- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] frames it as a centralized gateway routing every AI request through one layer for cost control, usage analytics, and model routing/swapping without changing engineer workflow — the canonical worked example, generalizing the BYOK-proxy pattern to an enterprise control plane.

## Sub-claims and details

- Routes every AI request through a single layer. ([[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]])
- Purposes: cost control, usage analytics, and model routing/swapping. ([[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]])
- Model routing/swapping happens without changing the engineers' workflow. ([[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]])
- Presented as the enterprise-control-plane generalization of the BYOK-proxy pattern. ([[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]])

## Open questions and contradictions

- The source describes Shopify's proxy at the level of purpose and placement, not implementation — latency overhead, failover behavior, and auth handling are not specified here (some are treated generically on [[byok-proxy]]).

## Related concepts

- [[byok-proxy]] — narrower: the BYOK-specific instance of this pattern. LLM proxy is the enterprise-control-plane generalization.
- [[observability]] — usage analytics is observability applied to LLM traffic.
- [[llmops]] — the operational discipline an LLM proxy supports.
- [[claude-as-infrastructure]] — adjacent framing of LLM access as organizational infrastructure.

## Related entities

- (Shopify — referenced in source; not yet cited as a wiki entity here)

## Mentioned in

- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]
