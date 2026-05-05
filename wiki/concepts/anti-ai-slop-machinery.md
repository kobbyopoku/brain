---
type: concept
title: Anti-AI-Slop Machinery
created: 2026-05-05
updated: 2026-05-05
aliases: [anti-slop, design-discipline-machinery, ai-slop-prevention]
tags: [ai-design, output-discipline, agent-contract, quality-gates]
---

# Anti-AI-Slop Machinery

> A five-mechanism stack for preventing AI-generated design output from drifting into the recognizable "AI slop" aesthetic — purple gradients, generic icons, fabricated metrics, hedging copy. Codified by [[wiki/entities/open-design|Open Design]]: brand-spec extraction protocol, five-dimensional self-critique, P0/P1/P2 checklist, blacklist, and honest placeholders.

## Definition

**Anti-AI-slop machinery** is a structured set of pre-emit gates and output-discipline mechanisms that constrain an AI agent's design generation to specific, validated, brand-faithful output instead of the fast-degraded "AI slop" patterns that emerge from unconstrained generation. The mechanisms are *additive* — applied together they create overlapping discipline; missing any one weakens the whole.

The five mechanisms (per [[wiki/sources/nexu-io-open-design|Open Design]]):

1. **Brand-spec extraction protocol**: locate → download → grep hex → codify → vocalize. The agent must actually read brand assets (style pages, design files, logo files, marketing site) and extract concrete tokens; not infer.
2. **Five-dimensional self-critique** (pre-emit gate): Philosophy / Hierarchy / Execution / Specificity / Restraint. The agent grades its own output across these axes before emission and rewrites if any score is poor.
3. **P0/P1/P2 checklist enforcement**: priority gates on output. Critical issues (P0) block emission entirely; major issues (P1) require fix; minor issues (P2) are flagged but allowed.
4. **Blacklist**: explicit rejected patterns — purple gradients, generic icons (lightning bolts, abstract swirls), invented metrics ("3× faster", "boost productivity by 40%"), hedge phrases ("revolutionize", "seamless", "innovative"), AI-cliché color combinations.
5. **Honest placeholders**: em-dashes, grey blocks, *"[chart placeholder]"* over fabricated statistics. If the agent doesn't have a real number, it doesn't make one up.

## Why it matters

The AI-output-quality problem this concept addresses is well known: LLMs trained on web data have absorbed the visual / verbal conventions of low-effort marketing content and reproduce them by default. Without explicit discipline, agents generate landing pages with stock-photo placeholder + generic abstract logo + purple-blue gradient hero + fabricated "10× growth" stats + hedge copy ("innovative platform that revolutionizes the way teams work"). This is *AI slop* — recognizable, low-trust, indistinguishable from a thousand other AI-generated pages.

The machinery is interesting beyond design because:

1. **It's the most explicit articulation of "agent output discipline" in the wiki.** Most agent contracts ([[wiki/concepts/skill-md|SKILL.md]], [[wiki/concepts/CLAUDE|CLAUDE.md]], [[wiki/concepts/design-md|DESIGN.md]]) describe *what* the agent should do; this concept describes *how to gate the output before emission*.
2. **The mechanisms generalize beyond design.** The same five-dimensional self-critique pattern (whatever the dimensions) + P0/P1/P2 + blacklist + honest placeholders can apply to PRDs, marketing copy, runbooks, code reviews, clinical documentation, financial reports.
3. **It addresses a quality problem that generic prompt engineering cannot.** "Don't use purple gradients" in a prompt is brittle; embedding a blacklist as a pre-emit check is a structural fix.

## Treatment across sources

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source. Codifies all five mechanisms in the Open Design platform.
- *Adjacent treatments not yet ingested*: traditional brand-style-guide enforcement; Anthropic's published guidance on Claude system prompts; design-critique frameworks like Steve Krug's "Don't Make Me Think." Future ingests should connect this concept to those lineages.

## Sub-claims and details

### 1. Brand-spec extraction protocol

The agent's mandate, per Open Design: when given a brand brief, the agent must:

1. **Locate** — find the brand's official assets (style page, brandbook, marketing site).
2. **Download** — actually fetch the asset, not summarize from memory.
3. **Grep hex** — extract concrete color values from CSS, SVG, or Figma exports.
4. **Codify** — write the extracted values into a structured form (DESIGN.md tokens).
5. **Vocalize** — articulate the brand's design philosophy in one sentence (tone, archetype, restraint level).

This protocol exists because **agents asked to design "in Stripe's style" otherwise infer Stripe-likeness from training data**, which produces a *generic Stripe-flavor* rather than *the actual Stripe brand*. The protocol forces the agent to read the present-day brand, not the model's stale priors.

### 2. Five-dimensional self-critique

The five dimensions Open Design enforces:

- **Philosophy**: does the output express a coherent design intent (a brand mood, an aesthetic stance)?
- **Hierarchy**: is information ordered by importance? Are the most important elements visually dominant?
- **Execution**: are tokens applied consistently — colors, type sizes, spacing, components?
- **Specificity**: is the output tailored to *this* brand and *this* surface, or generic?
- **Restraint**: is the output free of decoration that doesn't serve communication?

The agent grades its own output against each dimension before emit; weak scores trigger rewrite. Conceptually similar to a self-critique loop in [[wiki/concepts/agent-workflow-patterns|evaluator-optimizer pattern]] — but specialized to design, with named axes.

### 3. P0/P1/P2 checklist enforcement

Standard severity-priority labels applied to design issues:

- **P0** (block emission): missing required elements, off-brand colors, invented data, accessibility failures.
- **P1** (require fix before final): minor brand inconsistencies, suboptimal hierarchy, weak typography choices.
- **P2** (flagged but allowed): nice-to-have improvements, minor refinements.

The discipline: the agent doesn't emit P0 violations; it self-flags P1 for explicit user review; P2 surfaces as suggestions. This separates *blocking* from *advisory* gates — a meaningful distinction missing from generic "be careful" prompts.

### 4. Blacklist

Open Design's documented blacklist (subset):

- Purple gradients (the AI-cliché hero treatment)
- Generic abstract logos (swooshes, geometric squiggles)
- Invented metrics ("Increase productivity 3×", "Save 8 hours per week")
- Hedge / buzzword phrases ("revolutionize", "seamless", "innovative platform")
- Stock-photo placeholders that look like AI-generated business meetings
- Decorative icons that don't carry meaning

Each blacklist entry is paired with a *positive* alternative: "if tempted to use a purple gradient, use a single-color flat hero with one product screenshot."

### 5. Honest placeholders

The principle: if the agent doesn't have real content, it shows that explicitly rather than fabricating. Specifically:

- **Em-dashes** for missing copy: *"Built on — for the —."*
- **Grey blocks** for missing images: a `<div>` with `background: #e5e5e5` instead of a stock photo.
- **Bracketed placeholders** for missing data: *"[chart: customer growth Q3 2026]"* instead of a fake chart.
- **TBD / TK conventions** for unknown metadata: *"Pricing: TK"* instead of "$X/month".

This is a discipline carry-over from journalism (TK = "to come" in editorial workflow). Refusing to fabricate is an interesting agent-contract primitive — most agents fabricate by default because their training rewards completeness over honesty.

## Cross-domain applications

The mechanisms generalize:

| Domain | Brand-spec extraction | 5-dim self-critique | P0/P1/P2 | Blacklist | Honest placeholders |
|---|---|---|---|---|---|
| **Design** (canonical) | Brand assets → tokens | Philosophy/Hierarchy/Execution/Specificity/Restraint | Blocking/Major/Minor | Purple gradients, generic icons, invented metrics | Em-dashes, grey blocks |
| **PRDs** | User research → personas | Problem/Solution/Risks/Metrics/Tradeoffs | Same | Buzzwords ("synergize"), unverified user quotes | "TBD" / "[research pending]" |
| **Marketing copy** | Customer interviews → ICP language | Push/Pull/Habit/Anxiety/Specificity | Same | Hedge phrases, fake testimonials | "[real customer quote pending]" |
| **Clinical docs** | Patient record → facts | Subjective/Objective/Assessment/Plan/Discharge | Same | Unsupported diagnoses | "[lab result pending]" |
| **Code review** | Diff → understanding | Correctness/Security/Performance/Readability/Tests | Same | Made-up vulnerabilities, hallucinated APIs | "Not reviewed: [section]" |
| **Runbooks** | Incident history → patterns | Trigger/Diagnosis/Action/Verification/Rollback | Same | Mock metrics, untested commands | "[command not yet validated]" |

The pattern transfers cleanly. The specific dimensions / blacklist entries change per domain, but the *structure* (extraction protocol + self-critique + severity gates + blacklist + honest placeholders) is invariant.

## Open questions and contradictions

- **Effectiveness is unmeasured.** Open Design's claim is that the machinery prevents slop; this isn't measured against a control. A useful follow-up: ablation study showing which mechanisms most reduce slop.
- **Maintaining the blacklist is itself work.** As AI design conventions evolve, today's blacklist becomes tomorrow's stale rule. The machinery requires ongoing curation.
- **Self-critique requires the agent to recognize its own slop.** If the agent's training distribution is heavy with slop, the agent's "critique" may praise the very patterns the blacklist rejects. The mechanism is only as strong as the agent's calibration.
- **The five dimensions are domain-specific.** Different domains need different axes — adopting this concept beyond design requires designing per-domain dimension lists.
- **Honest placeholders break some workflows.** A demo client expecting a finished page may be more disturbed by visible em-dashes than by fake copy. The discipline favors honesty over polish, which is a legitimate tradeoff but not always the right call.

## Related concepts

- [[markdown-as-agent-contract]] — anti-slop machinery is a particularly explicit instance of the meta-pattern.
- [[design-md]] — the format anti-slop machinery operates on.
- [[claude-code-skills]] — adjacent: skills can embed anti-slop rules.
- [[agent-workflow-patterns]] — five-dim self-critique is the evaluator-optimizer pattern specialized.
- [[reasoning-execution-split]] — anti-slop machinery is the deterministic-execution wrapper around the LLM's reasoning.
- [[switching-forces]] — adjacent: marketing copy applying push/pull/habit/anxiety as a 4-dim self-critique.

## Related entities

- [[wiki/entities/open-design]] — codifies the machinery.
- [[wiki/entities/claude-design]] — the proprietary product the machinery is built against.
- [[wiki/entities/refero]] — adjacent: ships brand tokens, doesn't enforce critique.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]]
