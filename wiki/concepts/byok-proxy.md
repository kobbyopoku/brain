---
type: concept
title: BYOK Proxy
created: 2026-05-05
updated: 2026-05-05
aliases: [byok-multi-provider-proxy, multi-provider-llm-proxy, sse-normalizing-proxy]
tags: [llm-infrastructure, byok, multi-provider, sse, security, proxy-pattern]
---

# BYOK Proxy

> A multi-provider LLM proxy pattern: a single normalized API endpoint that fronts multiple upstream providers (Anthropic, OpenAI-compatible, Azure OpenAI, Google Gemini), normalizes Server-Sent Events (SSE) chunks across them, and supports user-supplied API keys (BYOK = Bring Your Own Key). Codified by [[wiki/entities/open-design|Open Design]] with security-first design including SSRF blocking. Architectural sibling of LiteLLM and Portkey.

## Definition

A **BYOK proxy** sits between an application's frontend and multiple LLM providers. It exposes a single normalized API surface to the application, accepts user-supplied API keys, routes requests to the chosen upstream provider, and *normalizes the SSE stream format* so the application sees identical chunk shapes regardless of which provider answered.

[[wiki/entities/open-design|Open Design]]'s implementation, per [[wiki/sources/nexu-io-open-design]]:

- **Endpoints**: `/api/proxy/{anthropic,openai,azure,google}/stream`
- **SSE chunk normalization**: each upstream's chunk format is translated to a unified shape downstream consumers expect.
- **SSRF blocking**: requests to loopback (127.0.0.0/8, ::1), link-local (169.254.0.0/16), and RFC1918 private addresses (10/8, 172.16/12, 192.168/16) are rejected to prevent SSRF attacks via user-supplied URLs.
- **BYOK**: API keys are user-supplied, not server-stored — the proxy is stateless w.r.t. credentials.

## Why it matters

Multi-provider LLM applications face a real architectural problem: every provider has its own API shape, its own SSE chunk format, its own streaming semantics. Building "supports Anthropic, OpenAI, Azure, and Gemini" naively means four code paths everywhere streams are consumed. A proxy with chunk normalization collapses that into one path.

Why this is worth a wiki concept (vs just an implementation detail):

1. **It's an emerging standard pattern.** [LiteLLM](https://github.com/BerriAI/litellm), [Portkey](https://portkey.ai), [OpenRouter](https://openrouter.ai), [Helicone](https://helicone.ai), and now Open Design all converge on the same shape: unified endpoint + per-provider routing + chunk normalization. The pattern is mature enough to name.
2. **The BYOK component has real privacy implications.** When an application doesn't store user API keys server-side, the trust model shifts — even an application breach doesn't compromise user keys. This matters for personal-knowledge tools (like this wiki) and clinical/compliance contexts.
3. **The SSRF blocking matters operationally.** A naive proxy would let an attacker supply `http://169.254.169.254/...` (AWS metadata endpoint) or `http://127.0.0.1:6379/` (local Redis) and have the proxy fetch it. Open Design's documented loopback/link-local/RFC1918 blocking is the right defense.

## Treatment across sources

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source. Open Design's BYOK proxy at `/api/proxy/{anthropic,openai,azure,google}/stream` with SSE normalization + SSRF blocking is the most explicit codification in the wiki to date.
- [[wiki/sources/nousresearch-hermes-agent]] — *2026-05-05*. **The proxy pattern collapsed into the agent itself**: [[wiki/entities/hermes-agent|Hermes Agent]] is model-agnostic by core architecture, not via an external proxy layer. Instead of "agent → BYOK proxy → providers," Hermes is "agent (with built-in provider abstraction) → providers." `/model` switches mid-conversation across Nous Portal / [[wiki/entities/openrouter|OpenRouter]] / NVIDIA NIM / Xiaomi MiMo / Kimi / MiniMax / Hugging Face / OpenAI / Anthropic / AWS Bedrock / custom endpoints. Cross-cite: Hermes also integrates with [[wiki/entities/openrouter|OpenRouter]], which is itself the *platform-scale* version of the BYOK proxy pattern — single endpoint fronting 200+ models. This gives a three-tier hierarchy: *application-level proxy* (Open Design) → *agent-level abstraction* (Hermes) → *platform-level aggregator* (OpenRouter / LiteLLM / Portkey / Helicone). Each layer solves the multi-provider problem at a different granularity.
- *Adjacent treatments not yet ingested as primary sources*: LiteLLM (Python proxy library), Portkey (commercial proxy SaaS), Helicone (proxy + observability). [[wiki/entities/openrouter|OpenRouter]] is now in the wiki as a stub.

## Sub-claims and details

### SSE chunk normalization

Each provider has a slightly different SSE chunk shape:

- **OpenAI**: `data: {"id":"...","object":"chat.completion.chunk","choices":[{"delta":{"content":"..."}}]}\n\n` followed by `data: [DONE]\n\n`.
- **Anthropic**: `event: content_block_delta\ndata: {"type":"content_block_delta","delta":{"type":"text_delta","text":"..."}}\n\n` plus `message_start`, `content_block_start`, `message_delta`, `message_stop` events.
- **Azure OpenAI**: similar to OpenAI but with subtle field-name differences and Azure-specific headers.
- **Google Gemini**: `data: {"candidates":[{"content":{"parts":[{"text":"..."}]}}]}\n\n` — different field structure.

A proxy that normalizes downstream sees a uniform shape (typically OpenAI-flavored, since most consumers are written against that shape first):

```
data: {"choices":[{"delta":{"content":"..."}}]}\n\n
...
data: [DONE]\n\n
```

The normalization is *lossy* in ways worth understanding — Anthropic's tool-use blocks, Gemini's safety scores, OpenAI's logprobs all need careful per-provider handling.

### SSRF blocking

The Server-Side Request Forgery class of attacks works when an application makes a request to a URL the user supplies, and that URL points to a *trusted internal* destination (cloud metadata endpoints, internal APIs, localhost services). SSRF blocking enforces that the destination is *publicly reachable*:

- **Loopback**: `127.0.0.0/8`, `::1` — blocks `http://localhost`.
- **Link-local**: `169.254.0.0/16` — blocks AWS metadata at `169.254.169.254`.
- **Private RFC1918**: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` — blocks LAN addresses.

Resolved address checks must happen *after DNS resolution*, not just on the URL string — `http://my-evil-domain.com` may resolve to `127.0.0.1`. Some implementations also block IPv6 unique-local (fc00::/7) and CGNAT (100.64.0.0/10) addresses.

### BYOK trust model

Server-stored keys vs user-supplied keys is a real privacy distinction:

- **Server-stored**: simpler UX (user pastes key once), but the server now holds a credential capable of impersonating the user. Server breach = user keys leaked.
- **User-supplied (BYOK)**: user pastes key on every session OR the key lives client-side. Server breach can't leak server-held credentials *because the server doesn't hold them*.

Open Design's BYOK pattern is the latter — credentials flow through the proxy on each request but aren't persisted server-side. This is the right default for personal-knowledge tools and is increasingly expected for any tool that handles sensitive context.

### Cost-routing as a downstream pattern

Once the proxy is in place, additional value emerges:

- **Failover**: if Anthropic 5xx's, retry on OpenAI.
- **Cost-routing**: send simple requests to cheap models, complex to expensive.
- **Model-mixing**: use Claude for reasoning, GPT-4o for structured output, Gemini for vision.
- **Budget caps**: per-user / per-day spending limits.
- **Logging / observability**: capture all LLM traffic for analysis.

Open Design ships the proxy primitive; downstream consumers can layer these. LiteLLM and Portkey ship some of these features out of the box.

## Open questions and contradictions

- **Normalization is lossy.** Tool-use, safety blocks, structured-output schemas don't translate 1:1 across providers. A truly unified API loses some provider-specific features.
- **The SSE format itself is converging slowly.** As providers move toward standards (OpenAI's chat-completions format becoming a de facto standard), the value of normalization decreases over time.
- **Latency overhead.** A proxy adds at least one network hop. For high-throughput apps this matters; for personal tools it's irrelevant.
- **Authentication semantics differ.** OpenAI's bearer token, Anthropic's `x-api-key` header, Azure's deployment-bound auth, Google's API key — the proxy must abstract these. Some providers also require organization/project IDs.
- **Streaming back-pressure.** Not all clients can keep up with token streams; the proxy may need to buffer or throttle.
- **The pattern doesn't solve the abstraction problem above the API.** Even with a unified streaming API, application code still needs to handle that Claude returns different content for the same prompt than GPT-4. The proxy is plumbing, not semantic equivalence.

## Related concepts

- [[mcp-server]] — adjacent: MCP is the *tool* abstraction; BYOK proxy is the *model* abstraction. Both are agent-infrastructure plumbing.
- [[markdown-as-agent-contract]] — adjacent: SKILL.md and BYOK proxy are different layers of the same "agent infrastructure" stack.
- [[reasoning-execution-split]] — proxy is firmly on the deterministic-execution side.

## Related entities

- [[wiki/entities/open-design]] — codifies the BYOK proxy pattern with SSRF blocking (application-level).
- [[wiki/entities/hermes-agent]] — collapses the pattern into the agent itself (agent-level abstraction).
- [[wiki/entities/openrouter]] — platform-level aggregator: single endpoint, 200+ models.
- [[wiki/entities/anthropic]], [[wiki/entities/openai]] — upstream providers the proxy supports.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]]
- [[wiki/sources/nousresearch-hermes-agent]]
