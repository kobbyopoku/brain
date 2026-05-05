---
type: concept
title: Question Form First
created: 2026-05-05
updated: 2026-05-05
aliases: [turn-1-form, mandatory-discovery-form, structured-intake]
tags: [agent-contract, ux-pattern, requirements-gathering, generation-discipline]
---

# Question Form First

> An agent-contract pattern in which the *first response* to a generation request is a **structured form** the user must complete before any output is generated. Locks surface, audience, tone, brand context, and scale upfront — preventing the "80% of redirects" that come from missing context. Codified by [[wiki/entities/open-design|Open Design]] for design generation.

## Definition

**Question Form First** is the discipline of treating Turn 1 of an agent interaction as a *mandatory structured-intake* phase rather than a generation phase. Instead of producing output from a one-line brief, the agent surfaces a form (typed fields, dropdowns, multi-select) that elicits the missing constraints — surface (web/mobile/desktop?), audience (developer / executive / consumer / clinical / etc.), tone (editorial / playful / corporate / brutalist), brand context (any existing brand assets / colors / voice), scale (one page / multi-page / full app), and any domain-specific dimensions. Only after the form is submitted does generation begin.

The pattern is **antagonistic to the natural-language-only ideal** — most agent interactions are framed as conversational, and inserting a form feels like a regression. But the discipline is justified by an empirical claim (per Open Design): unconstrained one-line briefs generate output that requires redirects 80% of the time; structured intake reduces this dramatically.

## Why it matters

The pattern matters in three ways:

1. **It addresses a fundamental information-asymmetry problem.** The user has the constraints in their head; the agent doesn't. Asking explicitly extracts them; assuming silently generates wrong output.
2. **It's domain-portable.** Design isn't unique — the same problem exists in PRD writing (who's the audience? what's the surface area? what's the deadline?), marketing copy (push/pull/habit/anxiety per [[switching-forces]]), clinical documentation (presenting complaint? medications? allergies?), code review (style guide? test coverage threshold? performance budget?). Every domain where output quality depends heavily on context benefits from structured intake.
3. **It moves the agent from "creative generator" to "specification compiler."** Once the form is filled, generation becomes more deterministic — the agent's job is to translate explicit constraints into output, not infer constraints from limited context.

## Treatment across sources

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source. Open Design enforces Turn-1 mandatory: a discovery form locks surface / audience / tone / brand context / scale before any design generation. Claim: prevents 80% of redirects.
- *Adjacent treatments not yet ingested*: Cal.com / Calendly booking forms (intake before consultation); medical clinic intake forms; loan application forms; many B2B SaaS onboarding flows. The pattern is universal in human-staffed services; Open Design is the first wiki source applying it explicitly to agent generation.

## Sub-claims and details

### Why "Turn 1 mandatory" rather than "ask if needed"

A subtler version of the pattern has the agent ask follow-up questions only when its initial generation would be too uncertain. This is weaker because:

- The agent doesn't always know what it's missing. Generation can produce confident-looking output despite missing context.
- Users learn to provide minimal briefs ("just generate something") and the agent learns not to interrupt — a co-evolved low-quality equilibrium.
- The cost of asking upfront is small (one extra turn); the cost of redirecting is large (multiple turns + emotional friction).

Mandatory Turn 1 form sidesteps these failure modes by removing the agent's discretion.

### Form field design (Open Design's approach)

Open Design's discovery form for design generation locks five dimensions:

| Dimension | Purpose | Example values |
|---|---|---|
| **Surface** | Where will this live? | Web landing / Mobile app / Desktop app / Slide deck / Document / Print |
| **Audience** | Who will see it? | Developers / Executives / Consumers / Clinicians / Investors / General-purpose |
| **Tone** | What mood? | Editorial / Playful / Corporate / Minimal / Brutalist / Warm |
| **Brand context** | Existing assets? | None / Brand kit URL / Specific brand reference / Custom palette |
| **Scale** | How big? | Single screen / Multi-page / Full prototype / Series |

The fields are *finite* (most are dropdowns) and *orthogonal* (each captures a distinct constraint). Adding more dimensions is allowed but the form should stay short — the goal is constraint capture, not exhaustive interrogation.

### Cross-domain field design

| Domain | Likely Turn-1 form fields |
|---|---|
| **PRD writing** | Audience (eng / pm / exec) / Surface (1-pager / full doc / RFC) / Stakeholders / Deadline / Existing context |
| **Marketing copy** | Audience (per ICP) / Channel (email / landing / social / ad) / Stage (awareness / consideration / decision) / Switching forces (per [[switching-forces]]) / Brand voice |
| **Clinical documentation** | Visit type (initial / follow-up / urgent) / Presenting complaint / Relevant history flags / Documentation template (SOAP / problem-oriented) |
| **Code review** | Diff scope / Style guide / Test coverage threshold / Performance budget / Security sensitivity |
| **Runbook writing** | Incident class / Severity / On-call audience / Existing related runbooks / Tooling assumed |

Each domain has its own 4-6 fields; the structure is invariant.

### Anti-pattern: forms that are too long

The discipline only works if the form is *short enough that users actually fill it out*. Open Design's 5-field form takes ~30 seconds; a 20-field form would be skipped. The art of the pattern is identifying the *minimal sufficient* set of fields.

### Composability with [[anti-ai-slop-machinery]]

Question Form First and Anti-AI-Slop Machinery are complementary:

- **Question Form First** captures *what* the user wants — the explicit constraints.
- **Anti-AI-Slop Machinery** disciplines *how* the agent produces it — the output gates.

Together they bound generation: explicit input + disciplined output. Either alone leaves a degree of freedom for slop.

## Open questions and contradictions

- **The 80% redirect-prevention claim is the project's prior, not measured.** A useful study: A/B test with vs without Turn-1 form, measuring revision count.
- **Form design itself can become slop.** A poorly-designed form with too many fields, ambiguous options, or missing categories pushes users toward "Other / skip" and re-introduces the unconstrained-brief problem.
- **The pattern feels paternalistic to power users.** Experienced users know exactly what they want; a mandatory form adds friction. Open Design's form has an implicit "skip" option (advanced users can override) but the design tension is real.
- **Translating the pattern to chat interfaces** (vs form-rendering UIs) requires the agent to ask the form questions one-at-a-time as natural language — slower but possible.
- **In multi-turn workflows, when does the form re-engage?** Open Design's pattern is Turn-1-only; iterations after the initial generation skip the form. But what if the user pivots ("actually make it for executives instead")? The form may need to re-engage on detected scope changes.

## Related concepts

- [[anti-ai-slop-machinery]] — composable; together they bound generation input + output.
- [[markdown-as-agent-contract]] — the form output is a structured agent contract.
- [[switching-forces]] — domain-specific intake fields for marketing copy.
- [[design-md]] — the form output flows into DESIGN.md selection.
- [[context-file]] — adjacent: per-client business voice/standards file.
- [[skill-md]] — adjacent: skills can embed Turn-1-form specifications.

## Related entities

- [[wiki/entities/open-design]] — codifies the pattern for design generation.
- [[wiki/entities/claude-design]] — the proprietary product likely also implements something similar.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]]
