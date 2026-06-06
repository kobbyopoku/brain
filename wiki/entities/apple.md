---
type: entity
title: Apple
entity_type: organization
created: 2026-05-02
updated: 2026-06-06
website: https://apple.com
aliases: []
tags: [refero-catalog, design-md-ingested]
---

# Apple

> Featured brand in the [[wiki/entities/refero|Refero]] design-reference catalog; full DESIGN.md ingested into the brain. See [[wiki/sources/apple-design-md]].

## Profile

Apple appears in this wiki via [[wiki/sources/refero-design-systems-for-ai-agents|Refero's catalog]] and via the dedicated DESIGN.md ingest at [[wiki/sources/apple-design-md]]. The brain has captured Apple's **design tokens** (colors, typography, spacing, components, philosophy) but no primary source yet on what Apple *builds* — product, business model, history are still un-sourced. The treatment here is design-aesthetic only.

## Key facts

- **Website**: https://apple.com
- **Refero style page**: https://styles.refero.design/style/c9cabb96-32fa-4896-837a-f2497ce1c856
- **Refero mood descriptor**: "Gallery wall at natural light —…" *(truncated in source)*
- **Apple Silicon — unified memory**: Apple Silicon gives the CPU and GPU direct access to the same memory pool (unified memory), cited in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **M3 Ultra memory bandwidth**: up to 819 GB/s unified-memory bandwidth, cited in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].
- **MLX**: Apple created the MLX array framework for Apple Silicon, cited in [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]].

## Design system summary

Apple has **two distinct DESIGN.md surfaces** in the catalog as of 2026-05-04:

- **MacBook Neo product page** ([[wiki/sources/apple-design-md]]) — *"Gallery wall at natural light — enormous type casts shadows on a white surface, color enters only as product."* One Azure `#0071e3` for the Buy CTA, one Cobalt `#0066cc` for inline links — no other non-neutral fills. SF Pro Display + SF Pro Text. **28px card radius is the page's geometric signature.** Letter-spacing scales aggressively with size (-2.11px at 96px display). Zero box-shadows. Theatrical product gradients for each MacBook Neo color finish (citrus / blush / indigo).

- **General Apple presentation surface** ([[wiki/sources/apple-design-md-alt]]) — *"Precise Canvas, Vivid Product. A stark white presentation surface designed to make premium product imagery pop with singular focus."* Includes additional accent colors (Sky Teal `#00a1b3`, Royal Violet `#8668ff`) for product feature highlights — not present on the MacBook Neo page. SF Pro Display + SF Pro Text + Arial fallback. Different rounding scale + 8/12/14/17/18/20/24/34/44 px type scale (vs MacBook Neo's 80-96px display).

The two surfaces share the **single-CTA-blue + monochrome-neutrals + carved-typography** core but diverge on accent palette breadth and type scale extremes. An agent generating Apple-voice UI should pick one surface and stay consistent — they don't compose without conflict.

## Positions and claims

- **Design discipline matters as identity** — Apple's DESIGN.md captures explicit Do/Don't rules that constrain how the brand can ever appear in UI. *(See [[wiki/sources/apple-design-md]] for the full ruleset.)*

## Mentioned in

- [[wiki/sources/refero-design-systems-for-ai-agents]] — initial catalog reference.
- [[wiki/sources/apple-design-md]] — MacBook Neo DESIGN.md ingested 2026-05-02; raw refreshed with official Copy.md 2026-05-04.
- [[wiki/sources/apple-design-md-alt]] — alternate Apple surface DESIGN.md ingested 2026-05-04.
- [[wiki/sources/theahmadosman-inference-engines-local-ai-hardware]] — maker of Apple Silicon unified-memory hardware and the MLX framework.

## Related entities

- [[wiki/entities/refero]] — publishes the catalog this entity appears in.

## Related concepts

- [[wiki/concepts/design-md]]
- [[wiki/concepts/markdown-as-agent-contract]]
