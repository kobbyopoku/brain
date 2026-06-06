---
type: entity
title: Anthropic
entity_type: organization
created: 2026-05-02
updated: 2026-06-06
website: https://anthropic.com
aliases: []
tags: [ai-research, claude-code-ecosystem, refero-catalog, design-md-ingested]
---

# Anthropic

> AI research and safety company; maintainer of Claude and [[wiki/entities/claude-code|Claude Code]]; publisher of the official [[wiki/entities/anthropic-skills|skill collection]] and the Claude Code plugin marketplace. Operator of the agent that maintains this wiki.

## Profile

Anthropic is the AI research company that builds the Claude family of models and operates [[wiki/entities/claude-code|Claude Code]] — the platform on which this wiki is maintained and which is the central subject of multiple ingested sources. Anthropic also publishes the official open-source [[wiki/entities/anthropic-skills|skills]] repository (canonical reference for Claude Code skill authoring) and operates the plugin marketplace through which third-party plugins like [[wiki/entities/superpowers]] are distributed. Anthropic also appears in the [[wiki/entities/refero|Refero]] design-reference catalog ("Research journal printed on warm…"), which is the original reason an entity page existed before substantive sources were ingested.

## Key facts

- **Website**: https://anthropic.com
- **Operates**: [[wiki/entities/claude-code]] (CLI), Claude API, Claude.ai web/desktop apps, IDE extensions.
- **Publishes**: [[wiki/entities/anthropic-skills]] (`github.com/anthropics/skills`) — official skill collection covering PDF, DOCX, XLSX generation, data analysis.
- **Operates**: the Claude Code plugin marketplace (e.g. `claude-plugins-official` namespace).
- **Refero style page**: https://styles.refero.design/style/d469cba4-c448-4a43-a033-883f8bfcdc42
- **Refero mood descriptor**: "Research journal printed on warm stone."
- **Claude Design release**: released [[wiki/entities/claude-design|Claude Design]] on April 17, 2026 (cited to [[wiki/sources/nateherk-claude-design-tally-brand]]). Claude Design lives inside an existing Claude subscription and requires at least a Pro plan (cited to [[wiki/sources/prajwaltomar-claude-design-workflow]]).
- **Mike Krieger as CPO**: joined as CPO right before the Claude Design announcement (cited to [[wiki/sources/nateherk-claude-design-tally-brand]]).
- **Model API**: the Anthropic API / Claude Messages API is named as a model API to learn to call from code (cited to [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]]); Anthropic Messages API compatibility is supported by [[wiki/entities/llama-cpp|llama.cpp]]'s llama-server and by vLLM (cited to [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]]).
- **Model tiers**: provides the Claude tiers Haiku, Sonnet, and Opus, routed between for cost and speed control (cited to [[wiki/sources/zephyr-hg-7-setups-claude-fluency]]). Opus 4.7 named (cited to [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]); Opus referenced as the model to reserve for reasoning subtasks only (cited to [[wiki/sources/vasuman-forward-deployed-engineering-101]]).
- **Cloud for Claude Routines**: Claude Routines run on Anthropic's cloud (cited to [[wiki/sources/charliejhills-full-agent-system-6-steps]]).
- **Model provider behind enterprise proxies**: one of the model providers (with [[wiki/entities/openai|OpenAI]] and [[wiki/entities/google|Google]]) behind Shopify's LLM proxy (cited to [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]]).
- **Anthropic Academy**: delivers the "AI Fluency" course (anthropic.skilljar.com), MCP courses, and prompt-engineering docs framed as "prompting like an engineering discipline rather than magic words" (cited to [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]]).
- **Agent-harness docs**: Anthropic docs describe the SDK as "the agent harness that powers Claude Code," a runtime framed as a "dumb loop" where all intelligence lives in the model (cited to [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]]).

## Design system summary

From [[wiki/sources/anthropic-design-md]]: *"Research journal printed on warm stone — authoritative typographic composition where word-level underlines replace color as the primary emphasis mechanism."*

- **Three custom typefaces**: Anthropic Sans (UI/body), Anthropic Serif (display/editorial), Anthropic Mono (technical labels). Most brands use one custom typeface; Anthropic has three.
- **Six accent colors as thematic tags** (Clay, Ember, Olive, Sky, Fig, Cactus) — rotated by section/category, not used for hierarchy.
- **Warm-stone neutrals** — Ivory `#faf9f5` page ground, Oat `#e3dacc` tertiary, Cloud `#87867f` secondary text. Genuinely warm vs. typical cool-temperature design systems.
- **Asymmetric "Try Claude" button** — radius `0px 0px 8px 8px` (flat top, rounded bottom). Brand signature.
- **Underline-as-emphasis** replaces color highlighting. *"Headline emphasis via underline only, never color."*
- **Zero box-shadows. Hard-edged surface transitions.**

## Positions and claims

- **Skill files are the canonical mechanism for teaching agents domain-specific workflows.** *(Implicit by virtue of publishing and curating the official skill collection; explicit articulation would require an Anthropic-authored primary source.)*
- **Plugin marketplace distribution is the right channel** for third-party agent capabilities at scale. *(Implicit by operating the marketplace.)*
- **Used as study material and authority reference.** Anthropic's "Building Effective Agents" and "Demystifying evals for AI agents," plus its tool-use docs, are cited as study material for forward-deployed engineers ([[wiki/sources/vasuman-forward-deployed-engineering-101]]). Conversely, [[wiki/sources/shreyas-get-to-the-core-of-the-thing]] names the "Anthropic case study" reflex as an authority-citation crutch that substitutes for real product thinking.
- **Framed as one corner of the AI race.** Named as one of the three companies most people think the AI race is between (OpenAI vs Google vs Anthropic), a framing [[wiki/sources/shabnam-google-2026-roadmap-keynote]] argues misreads the real competition.
- **FDE-hiring AI company.** Named (with [[wiki/entities/openai|OpenAI]] and [[wiki/entities/google|Google]]) among AI companies looking for forward-deployed engineers ([[wiki/sources/vasuman-forward-deployed-engineering-101]]).

## Mentioned in

- [[wiki/sources/regent0x-claude-code-247-dev-team]] — repeatedly: as Claude Code maintainer, official skills publisher, and plugin marketplace operator.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — implicit Claude Code maintainer.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — featured brand in the Refero catalog.
- [[wiki/sources/anthropic-design-md]] — full DESIGN.md ingested 2026-05-02.
- [[wiki/sources/nexu-io-open-design]] — *2026-05-05*. References Anthropic's [[wiki/entities/claude-design|Claude Design]] product as the proprietary antecedent that Open Design replicates as Apache-2.0.
- [[wiki/sources/techwithtimm-ai-engineer-roadmap-2026]] — model API provider referenced for API calls and model choice (Claude).
- [[wiki/sources/techwith-ram-agentic-memory-breakdown]] — provider of the Claude models used for generation (Opus) and importance-scoring (Haiku) in the reference agent.
- [[wiki/sources/nateherk-claude-design-tally-brand]] — maker of Claude Design, Opus 4.7, and Claude Code.
- [[wiki/sources/vasuman-forward-deployed-engineering-101]] — named (with OpenAI and Google) as an AI company seeking FDEs; its docs cited as study material.
- [[wiki/sources/shreyas-get-to-the-core-of-the-thing]] — invoked via "Anthropic case study" as an authority-citation reflex.
- [[wiki/sources/shabnam-google-2026-roadmap-keynote]] — named in the OpenAI-vs-Google-vs-Anthropic framing the thread says misreads the real competition.
- [[wiki/sources/AnatoliKopadze-how-to-actually-use-claude-18-steps]] — maker of Claude, the consumer chat product the guide configures.
- [[wiki/sources/heynavtoor-personal-ai-system-claude]] — maker of Claude, the product the entire 7-layer personal-AI system is built on.
- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] — Claude Opus 4.7 listed as a co-editor of the article; Claude used in the author's research.
- [[wiki/sources/nateherk-claude-code-codex-same-project]] — vendor of Claude Code, the primary agent in the setup.
- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — Anthropic Messages API compatibility is supported by some engines.
- [[wiki/sources/0xDepressionn-karpathy-claude-md-82k-stars]] — maker of Claude / Claude Code (platform context).
- [[wiki/sources/charliejhills-full-agent-system-6-steps]] — provider of the cloud Claude Routines run on.
- [[wiki/sources/akshay_pachaar-x-anatomy-of-an-agent-harness]] — Claude Code / Claude Agent SDK presented as the canonical "dumb loop" harness.
- [[wiki/sources/zodchiii-shopify-23000-engineers-claude-code-setup]] — one of the model providers Shopify's LLM proxy routes to.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] — maker of Claude Design and the Claude subscription it lives inside (≥ Pro).
- [[wiki/sources/suryanshti777-stop-prompting-design-systems]] — implicit maker of Claude / Claude Code.
- [[wiki/sources/saboo-shubham-ultimate-guide-to-goal]] — publisher of Claude Code named as the reviewer tool.
- [[wiki/sources/zephyr-hg-7-setups-claude-fluency]] — maker of the Haiku/Sonnet/Opus tiers referenced by the model-routing setup.
- [[wiki/sources/Shruti_0810-zero-to-ai-engineer-roadmap]] — Anthropic Academy (AI Fluency), MCP courses, and prompt-engineering docs.

## Related entities

- [[wiki/entities/claude-code]] — Anthropic's coding-agent product.
- [[wiki/entities/claude-design]] — Anthropic's design-tooling product (artifact-first workflow).
- [[wiki/entities/anthropic-skills]] — Anthropic's official skill collection.
- [[wiki/entities/superpowers]] — third-party plugin distributed via the Anthropic plugin marketplace.
- [[wiki/entities/trail-of-bits-claude-code-skills]] — third-party skill collection complementing Anthropic's official one.
- [[wiki/entities/refero]] — design-reference catalog Anthropic appears in.
- [[wiki/entities/open-design]] — open-source alternative to Anthropic's Claude Design.

## Related concepts

- [[claude-code-skills]]
- [[markdown-as-agent-contract]]
- [[design-md]]
