---
type: synthesis
title: Refero vs Open Design vs Claude Design — three strategic bets in AI design tooling
created: 2026-05-05
updated: 2026-05-05
question: How do the three major AI-design-tooling products in the wiki compare across positioning, architecture, and adoption fit?
tags: [synthesis, design-systems, ai-design, comparison, strategy]
---

# Refero vs Open Design vs Claude Design — three strategic bets in AI design tooling

> Three products solve "AI agents need design taste" with three distinct strategies: **Refero** sells curated taste as a SaaS catalog with an MCP server; **Open Design** ships an open-source full-stack platform that runs locally; **Claude Design** embeds the workflow inside Anthropic's proprietary product surface. Each bet is internally coherent and the right answer for a different user.

## TL;DR

- **[[wiki/entities/refero|Refero]]** wins on **curation density and zero infrastructure** — drop the MCP into Cursor / Claude / Windsurf and your agent has design taste. Best for solo builders who want fast results and don't care about lock-in.
- **[[wiki/entities/open-design|Open Design]]** wins on **architectural completeness and OSS freedom** — full application stack with 138 design systems, 64 SKILL.md bundles, 15 agent CLIs, BYOK proxy, anti-AI-slop machinery. Best for teams wanting local-first workflows or building a custom design pipeline.
- **[[wiki/entities/claude-design|Claude Design]]** wins on **integration tightness** — first-party experience inside Claude.ai with the deepest Anthropic-stack alignment. Best for users already deep in the Anthropic ecosystem who value polish over portability.

The three positions are **not directly comparable on a single axis** because they're optimizing for different things. The right tool depends on the user's stance on lock-in, customization needs, and whether the design pipeline is a feature of their broader AI workflow or a standalone problem.

## Context

The wiki has accumulated three substantial sources on AI design tooling: [[wiki/sources/refero-design-systems-for-ai-agents]] (2026-05-02), [[wiki/sources/nexu-io-open-design]] (2026-05-05), and Claude Design (referenced indirectly through Open Design's lineage as the proprietary antecedent — no primary source from Anthropic ingested yet). Plus 33 brand-specific Refero DESIGN.md ingests.

The question for any builder evaluating this space — including for [[wiki/projects/vedge|Vedge]]'s `vedge_landing` work — is: *which one to adopt?* The synthesis aims to make the comparison explicit.

## Argument / analysis

### Strand 1: Positioning — different products solving different problems

The three products are often described as competitors but they solve substantially different problems.

**Refero** is positioned as *"design taste, extracted"* — the value proposition is the *curation*. Refero's contribution is the act of capturing real product brands' visual decisions in a clean, agent-readable format. The product is the catalog. ([[wiki/sources/refero-design-systems-for-ai-agents]])

**Open Design** is positioned as *"local-first, open-source alternative to Claude Design"* — the value proposition is *architectural ownership*. Open Design's contribution is the full application stack: frontend + daemon + multi-agent runtime + media generation + MCP server. The product is the platform. ([[wiki/sources/nexu-io-open-design]])

**Claude Design** is positioned as *"design inside Anthropic's product surface"* — the value proposition is *integration tightness*. Claude Design's contribution is the artifact-first workflow embedded in Claude.ai with first-party model access. The product is the workflow. ([[wiki/entities/claude-design]])

The framing matters. A user picking "the AI design tool" without distinguishing these positions ends up frustrated when one tool doesn't solve a problem the other was built for.

### Strand 2: Architecture — three different scopes

| Layer | Refero | Open Design | Claude Design |
|---|---|---|---|
| **Catalog** | ✅ Curated SaaS catalog (32 brands in our wiki) | ✅ 138 design systems shipped in repo | ❓ Likely some brand library; unsourced |
| **DESIGN.md format** | 5-section schema | **9-section schema** (richer) | Unknown / proprietary |
| **MCP server** | ✅ Refero MCP (consumes from Cursor/Claude/Windsurf) | ✅ Local MCP for cross-repo queries | ❓ Probably internal to Claude.ai |
| **Skill bundles** | None — DESIGN.md only | ✅ 64 SKILL.md bundles | ❓ Likely some internal skills |
| **Multi-agent runtime** | None — agents call MCP | ✅ Auto-detects 15 CLIs on PATH | ❌ Claude only |
| **BYOK / multi-provider** | N/A | ✅ Proxy for Anthropic/OpenAI/Azure/Google | ❌ Anthropic only |
| **Sandboxed preview** | Web catalog only | ✅ srcdoc iframe in Next.js | ✅ In Claude.ai |
| **Export formats** | Tailwind v4 / CSS vars / design tokens | ✅ HTML / PDF / PPTX / ZIP / Markdown | ✅ Various (ZIP confirmed) |
| **Local persistence** | None — SaaS | ✅ SQLite at `.od/app.sqlite` | ❌ Cloud |
| **Anti-AI-slop machinery** | None codified | ✅ 5-mechanism stack | ❓ Possibly some |
| **Question Form First** | None | ✅ Turn-1 mandatory form | ❓ Unknown |
| **Visual Directions** | None | ✅ 5 OKLch presets | ❓ Unknown |
| **Source code** | Closed | Apache-2.0 | Proprietary |

Open Design is **architecturally a superset** of Refero in capability — it ships everything Refero does plus full application infrastructure. Claude Design is **architecturally a complement** — its strength is being part of the Claude.ai surface, not standing alone.

### Strand 3: Schema sophistication — the DESIGN.md evolution

The wiki has documented two distinct DESIGN.md schemas. ([[wiki/concepts/design-md]])

**Refero's 5-section schema**:
1. Color palette (brand / gradients / neutrals)
2. Typography (family + scale)
3. Spacing & shapes
4. Components (token-referenced)
5. Design philosophy

**Open Design's 9-section schema** (Refero's 5 + 4 new):
6. **Depth & Elevation** — multi-level shadow philosophy
7. **Do's and Don'ts** — explicit Do/Don't rules
8. **Responsive Behavior** — breakpoints, touch targets, collapsing
9. **Agent Prompt Guide** — quick color reference + example prompts + iteration guide

The new sections aren't decorative — they materially improve agent output:

- **Depth & Elevation** prevents agents from inventing shadows that fight the brand's elevation philosophy.
- **Do's and Don'ts** are *blocking* rules ("don't use weight 700") that prevent specific failure modes.
- **Responsive Behavior** ensures agents handle mobile breakpoints with the brand's specific collapsing strategy, not a generic mobile-first.
- **Agent Prompt Guide** makes the DESIGN.md self-contained — no external prompt engineering needed.

Open Design's schema is **the more mature form**. Refero's pages have the substantive core; Open Design's pages have the substantive core plus the boundary conditions. Same Linear DESIGN.md is ~144 lines on Refero, ~370 lines on Open Design.

### Strand 4: Adoption-fit decision matrix

The right tool depends on user constraints:

| User constraint | Refero | Open Design | Claude Design |
|---|---|---|---|
| **Don't want to install or run a daemon** | ✅ Best | ❌ Worst | ✅ Best |
| **Want local-first / offline / BYOK** | ❌ | ✅ Best | ❌ |
| **Already heavy in Claude.ai workflow** | Neutral | Neutral | ✅ Best |
| **Want OSS / no vendor lock-in** | ❌ | ✅ Best | ❌ |
| **Want lowest setup time** | ✅ Best | ❌ | ✅ Best |
| **Want maximum DESIGN.md fidelity** | ❌ | ✅ Best | ❓ |
| **Need multi-agent flexibility (Claude + GPT + Gemini)** | Neutral | ✅ Best | ❌ |
| **Need media generation (image / video)** | ❌ | ✅ Best (gpt-image-2 + Seedance + HyperFrames) | ❓ |
| **Need 64+ skill bundles for prototypes / decks / docs** | ❌ | ✅ Best | ❓ |
| **Need anti-slop discipline** | ❌ | ✅ Best | ❓ |
| **Want integrated chat + preview surface** | ❌ (catalog only) | ✅ | ✅ Best (in Claude.ai) |
| **Compliance / data residency requirements** | ❌ (SaaS) | ✅ Best (local) | ❌ (SaaS) |

For Vedge specifically: Open Design wins. Vedge has compliance constraints (PHI in a healthcare EHR), values local-first / BYOK, and already has multi-agent workflow exposure (Claude Code primarily). The daemon dependency is a real cost but worth paying for the architectural fit.

### Strand 5: Lineage and ecosystem

Open Design explicitly traces lineage to four upstream OSS projects:
- [[wiki/entities/huashu-design]] — design philosophy + brand protocol.
- [[wiki/entities/guizang-ppt-skill]] — magazine-style deck framework.
- [[wiki/entities/open-codesign]] — streaming artifacts + sandboxed preview + exports.
- [[wiki/entities/multica]] — daemon architecture + PATH-scan multi-agent detection.

This explicit attribution implies an active **AI design tooling OSS ecosystem** that Refero and Claude Design don't engage with. For users who care about the upstream community (more contributors, more eyes on bugs, more interoperability), Open Design's ecosystem position matters.

### Strand 6: The "anti-AI-slop machinery" differentiator

Only Open Design codifies output discipline as named mechanisms ([[wiki/concepts/anti-ai-slop-machinery]]):

1. Brand-spec extraction protocol
2. Five-dimensional self-critique pre-emit gate
3. P0/P1/P2 checklist enforcement
4. Blacklist (purple gradients, generic icons, fabricated metrics)
5. Honest placeholders (em-dashes, grey blocks)

Refero ships brand tokens but doesn't enforce critique. Claude Design likely has *some* output discipline but it's not externally documented or extractable. This is meaningful: if the user wants to know *why* their AI design output is mediocre, Open Design gives them a vocabulary and gates to fix it. The other two don't.

The mechanisms also generalize beyond design — to PRDs, marketing copy, runbooks, code review, clinical documentation. Open Design is the only product whose architecture meaningfully exports beyond its category.

## Evidence summary

| Claim | Supporting | Contradicting |
|---|---|---|
| Open Design is architecturally a superset of Refero | [[wiki/sources/nexu-io-open-design]] | None |
| Open Design's 9-section DESIGN.md is richer than Refero's 5-section | [[wiki/sources/nexu-io-open-design]], live sample of Linear DESIGN.md | None |
| Refero is best for fast setup with no infrastructure | [[wiki/sources/refero-design-systems-for-ai-agents]] | None |
| Claude Design is the proprietary antecedent | [[wiki/sources/nexu-io-open-design]] (Open Design's stated mission) | No direct Anthropic source — inferred only |
| Open Design ships anti-slop machinery as named mechanisms | [[wiki/sources/nexu-io-open-design]] | None |
| 138 design systems > 33 brain-ingested Refero brands | [[wiki/sources/nexu-io-open-design]] live count | Refero may have more brands not in our 33 ingests |
| Open Design includes 64 SKILL.md bundles | [[wiki/sources/nexu-io-open-design]] live count | README claims 31; live shows 64 |
| The three products are not directly comparable on one axis | This synthesis | None |
| For Vedge specifically, Open Design wins | This synthesis (compliance + local-first + multi-agent) | Daemon dependency is a real cost |

## Open questions

- **What does Claude Design actually look like?** No primary Anthropic source ingested. The "?" cells in the architecture matrix above are inferences. A direct Claude Design walkthrough would let us verify or refute.
- **Refero's actual catalog size**: our wiki has 33 ingests, but Refero's full catalog may be larger. Worth a follow-up source-page that's a fresh re-clipping of styles.refero.design/.
- **Is Anthropic likely to merge Claude Design with Claude Skills?** Strategic question — both ship as Anthropic primitives. Convergence would change the competitive landscape.
- **Does Claude Design have anything analogous to anti-AI-slop machinery?** Probably yes (Anthropic ships strong output discipline elsewhere) but it's not externally extractable. If made extractable, it would be a strong asset.
- **Adoption data**: how many users / agencies / enterprises are using each? No data ingested. Adoption signals would shift the recommendations.
- **Cross-product portability**: can a Refero DESIGN.md be imported into Open Design? Open Design has `import/claude-design`; a `import/refero` endpoint would be useful and is currently absent.

## Implications for Vedge

For [[wiki/projects/vedge|Vedge]]'s `vedge_landing` work:

1. **Adopt Open Design as the design pipeline.** Local-first + BYOK align with PHI-compliance posture. The `saas-landing` skill is directly applicable. Use the **Linear** or **Stripe** DESIGN.md (clean SaaS feel) or **Notion** (warm-clinical) depending on brand decision.
2. **Apply anti-AI-slop machinery** as a discipline for *all* Vedge content generation, not just landing. Particularly relevant for clinical documentation where fabricated metrics are a real failure mode.
3. **Use question-form-first** for Vedge's intake forms — patient intake, clinic onboarding, even internal PRD drafting. The pattern is domain-portable.
4. **Don't lock in to Refero MCP** for Vedge specifically. The catalog is good but the SaaS dependency is the wrong shape for a healthcare product.

## Related

- [[wiki/concepts/design-md]] — the file format all three products use (with schema variants).
- [[wiki/concepts/anti-ai-slop-machinery]] — Open Design's discipline architecture.
- [[wiki/concepts/artifact-first-workflow]] — pattern originating in Claude Design, replicated in Open Design.
- [[wiki/concepts/byok-proxy]] — Open Design's multi-provider abstraction.
- [[wiki/concepts/question-form-first]] — Open Design's Turn-1 discovery pattern.
- [[wiki/concepts/visual-directions]] — Open Design's deterministic preset alternative to brand DESIGN.md.
- [[wiki/concepts/markdown-as-agent-contract]] — meta-pattern all three products instantiate at different layers.
- [[wiki/concepts/claude-code-skills]] — Open Design's skill mechanism.
- [[wiki/concepts/mcp-server]] — distribution mechanism used by Refero (consumed) and Open Design (exposed).
- [[wiki/projects/vedge]] — adoption recommendation lives here.

## Source pages

- [[wiki/sources/refero-design-systems-for-ai-agents]] — Refero canonical source.
- [[wiki/sources/nexu-io-open-design]] — Open Design canonical source.
- [[wiki/entities/claude-design]] — Claude Design entity (no direct source ingested).

## Entity pages

- [[wiki/entities/refero]]
- [[wiki/entities/open-design]]
- [[wiki/entities/claude-design]]
- [[wiki/entities/anthropic]] — publisher of Claude Design.
- [[wiki/entities/nexu-io]] — maintainer of Open Design.
