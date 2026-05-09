---
type: synthesis
title: Helm Commercialization Paths — Strategic Decision (Internal-Only for v1)
created: 2026-05-09
updated: 2026-05-09
aliases: [helm-strategy, helm-commercialization, helm-marketplace-decision]
tags: [synthesis, helm, strategic-decision, commercialization, decision-record]
---

# Helm Commercialization Paths — Strategic Decision Record

> **Decision (2026-05-09)**: [[wiki/projects/helm|Helm]] proceeds as a **ROAM Labs internal OS** for v1. The "agent marketplace" shape ([[wiki/projects/helm|Helm]] as multi-tenant productized SaaS) is **explicitly deferred**. Re-evaluate after 3-5 paying customers are operating real volumes through Helm via the services-as-software path. **Decision-maker**: [[wiki/entities/godwin-opoku-duah|Godwin Opoku Duah]]. **Decision-trigger**: user's brainstorming question on 2026-05-09 about pivoting Helm to a multi-tenant agent marketplace; wiki-evidence-driven recommendation favored Shape A.

## What was considered

Three real shapes the question "agent marketplace where companies rent agents to manage their business affairs" could take:

| Shape | Description | Risk | Ceiling | Time-to-first-$ | Status |
|---|---|---|---|---|---|
| **A** | Helm internal + offer as services-as-software engagement to high-trust existing relationships | Low | $1-7M ARR | ~3 months after Helm v1 ships | ✅ **Chosen** |
| **B** | Productized multi-tenant SMB-targeting agent platform (the "marketplace" framing) | High | $50M+ if it works | 12-18 months | ❌ Deferred |
| **C** | Open-source agent stack patterns + commercial hosted layer | Medium | Depends on community | 6-12 months | ❌ Deferred |

## Why Shape A wins (wiki evidence)

The brain has **5+ independent practitioners** documenting that the services-as-software shape is what actually scales for solo-founder agent businesses:

- [[wiki/sources/khairallah-ai-automations-10k-month]] — 6-phase $10K/month playbook is *exactly* this shape. $13,750/mo target = 5 retainer × $750 + 2 builds × $5K.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — **the scaled version**. ColdIQ hit $7M ARR doing this. Includes [[wiki/concepts/churn-at-scale|churn-at-scale]] math that pure-services hits without the software-margin accelerator layer.
- [[wiki/sources/heynavtoor-10k-claude-automation-business-90-days]] — derivative confirming the same pricing math.
- [[wiki/sources/realbrianmoran-making-money-online-2026]] — names AI services for businesses as 1 of the 10 working 2026 models.
- [[wiki/sources/saraev-agentic-workflows-2026]] — [[wiki/concepts/horizontal-leverage|horizontal-leverage]] thesis: wealth concentrates in agentic services.
- [[wiki/sources/exploraX_-google-maps-leadgen]] — gives the *acquisition layer* under this. Lead-gen playbook documented and ready to deploy.

The cumulative wiki signal: *Shape A has 5+ documented playbooks; Shape B has 0; Shape C has open-source-precedent (Hermes Agent, marketingskills-repo, Open Design) but no documented commercial-success path at solo-founder stage.*

## Why Shape B was deferred

The agent-marketplace framing fails three checks:

1. **Contradicts user's stated Q6 (a) decision** to be internal-only (recorded 2026-05-09 in [[wiki/projects/helm|Helm project page]]). Pivoting to multi-tenant adds back what was deliberately cut: RBAC, multi-tenant data scoping, billing infrastructure, self-service onboarding, productization polish. Estimate: 3-6 months of retrofit.
2. **Wiki has zero evidence of a productized multi-tenant agent platform working at small founder-scale.** CyrilXBT runs *one* business. nateherk runs *one* AI OS. Vacca runs an *agency* (services-mode). Closest competitor is [[wiki/entities/hermes-agent|Hermes Agent]] itself with 23k+ stars and MIT licensing — beating it requires more than "we did it for ROAM Labs internal."
3. **Distribution surface doesn't exist.** Shape B requires inbound content marketing + paid acquisition + partnerships — none of which are existing ROAM Labs strengths. Shape A leverages existing relationships (Brolly companies / Asanti / CBwBS / StaceSprouts / CPC if awarded) that already trust Godwin.

[[wiki/sources/Mnilax-430-hours-claude-code-waste]] adds an operational dimension: production AI cost discipline is brutal even for *single-tenant* deployments. Multi-tenant means *every customer's overhead patterns become Helm's problem* — a debugging surface that scales sub-linearly.

## Why Shape C was deferred

Open-source-core + commercial layer is a real shape ([[wiki/entities/hermes-agent]], [[wiki/entities/marketingskills-repo]], [[wiki/entities/open-design]] are precedents). But:

- **Time-to-first-dollar is 6-12 months minimum.** Open-source community building requires content cadence ROAM Labs doesn't currently have.
- **Helm's value isn't primarily in the runtime.** The agent runtime is [[wiki/entities/hermes-agent|Hermes Agent]] (already open-source). Helm's value is *the orchestration layer + voice profiles + master CLAUDE.md template + the operational discipline accumulated in this brain*. Open-sourcing that *gives away the proprietary advantage* without a clear monetization path.
- **Better paths to OSS contribution exist**. If Godwin wants community visibility, he can *contribute to* Hermes Agent or release smaller artifacts (the [[wiki/syntheses/multi-agent-ops-platform-blueprint|multi-agent-ops-platform-blueprint]] could become a public blog post / GitHub gist) without building a full OSS project.

Shape C remains a candidate for *Helm v2-or-later* if the OSS community angle becomes strategically relevant. **Not deferred forever; deferred for now.**

## The trap Shape B avoids

The most common failure mode for solo-founder multi-product companies is **adding strategic surface faster than existing surface ships**. Godwin currently has:

- 3 owned products at varying maturity (Vedge / Kivora / Clarvyn)
- 2 client engagements + 1 government bid (Coffee Break / StaceSprouts / CPC RTBVD)
- 1 internal tool not yet started (Helm)
- Brolly co-founder responsibilities + Brolly platform itself
- This brain that takes its own maintenance

Adding "productized multi-tenant agent marketplace" to that list before Helm v1 even exists is the trap. Per [[wiki/concepts/cognitive-debt|Rohit's cognitive-debt thesis]], the failure mode at the individual level is *AI-before-thinking*; the founder-equivalent is **strategy-before-evidence**. Shape A is evidence-generating; Shape B is evidence-presupposing.

## What this decision commits to

- Helm v1 ships **internal-only** for ROAM Labs. Single user (Godwin). No RBAC, no multi-tenant scoping, no billing surface, no self-service onboarding.
- The 6-week build order and stack ([[wiki/entities/hermes-agent]] + FastAPI on Railway + Next.js on Vercel + PostgreSQL + pgvector) **stays as designed**.
- The architectural foundation (especially the data model) is designed to *not foreclose* a multi-tenant pivot later: `tenant_id` columns added from day 1 even if UI doesn't surface them. Cost: ~10% upfront. Saves: ~6 months later if pivot is chosen.
- Voice profiles ([[wiki/syntheses/helm-voice-profiles]]) cover ROAM Labs' 4 product/corp voices. Multi-tenant version would need per-tenant voice profile collection mechanism — *not built now*.
- The acquisition story for v2 (services-as-software engagements with existing relationships) is documented in this synthesis but **not built yet**.

## What this decision does NOT commit to

- **Permanent internal-only**: this is a v1 decision, not a forever decision. The whole point of Shape A is that it's the *evidence-generating path*. After 3-5 paying customers, evaluate.
- **Permanent rejection of Shape B/C**: deferred, not killed. If post-v1 evidence supports either pivot, take it.
- **Specific monetization target**: Shape A's $1-7M ARR ceiling (per [[wiki/sources/itsalexvacca-services-as-software-7m-agency|Vacca]]) is a *reference range*, not a goal.

## Re-evaluation trigger

Revisit the Shape A vs B vs C question when **all three** are true:

1. **3-5 paying customers** are operating real volumes through Helm via the services-as-software path (= ~$15K-$30K MRR realistic — 3-5 retainers at $750-$2K/mo per [[wiki/sources/itsalexvacca-services-as-software-7m-agency|Vacca's]] range + ~1 build/mo at $5-15K per [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah's]] range. The higher end requires premium retainers + steady build cadence, not all customers will be at the top of the range).
2. **Concrete evidence on churn / implementation / distribution** has been collected:
   - Churn rate (per Vacca, ColdIQ runs at **10% monthly churn** — *"70 clients × 10% monthly churn = 7 replacements/month, a full-time closer's quota"*. The agency model dies at this rate without the software-margin accelerator layer.)
   - Implementation cost per customer in hours (per Khairallah's framework)
   - Distribution leverage (which channels are actually working for new customer acquisition?)
3. **A specific Shape B or C opportunity** surfaces — not a hypothetical "we should be a marketplace" but a concrete catalyst (e.g. a customer asking to white-label Helm for their own customers; or a partnership channel proposing distribution; or a Series-A-able demand signal).

Without all three, the answer remains Shape A. **Set a calendar reminder for ~Q4 2026 to re-evaluate.** By then, Helm v1 should have shipped and run for ~3-6 months in production.

## Related to the brain

- [[wiki/projects/helm]] — the project this strategic decision governs.
- [[wiki/syntheses/multi-agent-ops-platform-blueprint]] — the architectural reference Helm v1 implements.
- [[wiki/syntheses/godwin-portfolio]] — Helm sits in Bucket 5 (ROAM Labs internal tools); Shape A pivot would move it to a new Bucket (ROAM Labs commercial product).
- [[wiki/concepts/services-as-software]] — Shape A's economic model.
- [[wiki/concepts/churn-at-scale]] — the math Shape A's eventual scale will hit.
- [[wiki/concepts/ai-automation-services]] — the parent business model.
- [[wiki/concepts/horizontal-leverage]] — Saraev's wealth-concentration thesis under all 3 shapes.
- [[wiki/concepts/cognitive-debt]] — the strategy-before-evidence trap this decision avoids.

## Author's note for future Godwin

If you're reading this in 6 months and Helm v1 is shipped + working: **re-read this page before committing to a pivot.** The wiki evidence the present-Godwin used to make this decision is documented above. The re-evaluation trigger is concrete. The trap is named. The deferred shapes are *deferred*, not killed.

If you're reading this in 6 months and Helm v1 is *not* shipped: **finishing v1 takes priority over re-evaluating commercialization paths.** Strategy without execution is the trap. Read [[wiki/concepts/cognitive-debt]] again.
