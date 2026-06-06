---
type: source
title: "Alex Vacca — The 3 Phases of the AI Layer Most Services-as-Software Founders Get Wrong"
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/itsalexvacca/status/2056419277520224620
source_type: x-thread
author: Alex Vacca (@itsalexvacca)
source_date: 2026-05-18
raw_path: raw/The 3 Phases of the AI Layer Most Services-as-Software Founders Get Wrong.md
content_status: substantive-verbatim
tags: [services-as-software, ai-fulfillment-layer, agents, data-flywheel, human-in-the-loop, coldiq, build-order, outbound]
---

# Alex Vacca — The 3 Phases of the AI Layer Most Services-as-Software Founders Get Wrong

> [[wiki/entities/alex-vacca|Alex Vacca]]'s sequencing thesis for the AI fulfilment layer of a services-as-software business: **spine first, then agents, then the loop** — built in any other order, the system can't compound. The follow-up to his $7M [[wiki/entities/coldiq|ColdIQ]] playbook, this post isolates *which layer you build first* from the five-layer shape he described before.

## TL;DR

A services-as-software fulfilment layer must be built in a specific order or it stops compounding: **(1) the spine** (a single canonical data layer — one CRM, multi-domain sender infrastructure, one enrichment table that is "the agency's memory"); **(2) the agents** (two pay back first — a Reply Manager and an Enrichment Waterfall — built on top of the spine); **(3) the loop** (wiring every campaign's outputs back into the next campaign's inputs, where the [[wiki/concepts/data-flywheel|data flywheel]] finally turns). The agents are the layer founders want to build first because they look impressive on a screen recording, but they pay back *last*. The spine — the part that "doesn't look like AI" and ships no campaign the day it goes in — is what actually compresses the work. Three things stay permanently human: the strategic call on what the campaign is selling, the decision to pivot a broken offer, and the client relationship.

## Key takeaways

- **The order is the only part that matters.** Vacca's central claim: tools, agents, and stack are commodity; the *sequence* in which they go in is what he took two years to understand. "Build any other order and the system can't compound."
- **The AI fulfilment layer is the line item that decides a services business's ceiling.** Get it right → take on a new client without a new hire; margins stay near software margins. Get it wrong → "you become a body shop with a logo" and stall at the fifth hire.
- **Phase 1 — the spine — is the data layer that doesn't look like AI.** It sits between the universe of prospects and every downstream action, giving agents a place to read from and write to. Three requirements, in order: (a) **one CRM, not three** (ColdIQ runs [[wiki/entities/attio|Attio]]); (b) **multi-domain sender infrastructure from day one** (ColdIQ sends across 4 ESPs simultaneously; two-ESP redundancy is "the floor, not the ceiling"); (c) **one canonical data layer** (ColdIQ runs [[wiki/entities/clay-com|Clay]] as the single table every campaign reads from and writes to — enrichment, tier assignments, negative-signal columns, reply tags — "that table is the agency's memory").
- **The spine ships no campaign the day it goes in — which is exactly why founders skip it, and exactly why those who skip it stall.** The common failure: a single Apollo CSV → sequencer → chase first reply; campaign two starts from zero because campaign one's data is nowhere.
- **Phase 2 — the agents — is the layer that looks like the product the customer thinks they're buying, and the second-most-common reason the sequence collapses** (founders ship it first).
- **Agent one: the Reply Manager.** Every cold reply is a routing decision (positive signal → calendar link / bounce → feed data layer / wrong-contact → re-route / polite no → no manual response). Runs on [[wiki/entities/n8n|n8n]]; pulls prospect history from the spine + campaign context; drafts in [[wiki/entities/slack|Slack]] and waits for operator approval. A [[wiki/concepts/human-in-the-loop|human-in-the-loop]] approval gate.
- **Agent two: the Enrichment Waterfall.** [[wiki/entities/wiza|Wiza]] first against LinkedIn → [[wiki/entities/fullenrich|FullEnrich]] second (cascades 20+ providers) → [[wiki/entities/prospeo|Prospeo]] to clean residual at 98%+ verified accuracy. Full waterfall lands email coverage at 90%+ on harder ICPs.
- **What you do NOT agent-ize yet: copy strategy, the client relationship, and edge cases.** "Agents work inside the 80% of the work that's repeatable. The other 20% stays human." The agent that tries to handle every edge case is the agent that drifts.
- **"Two agents on top of a clean spine outperform six agents on top of nothing. Every quarter."** The accelerator anti-pattern: operators shipping a Lead Researcher + Campaign Strategist + Booking Coordinator in week one with no spine and no loop.
- **Phase 3 — the loop — is the part most operators never build, which is why most fulfilment layers stop compounding the second the agents go live.** The loop wires every campaign's outputs back into the next campaign's inputs.
- **Concrete feedback edges:** engagement signals from LinkedIn → data layer; buying triggers from [[wiki/entities/predictleads|PredictLeads]] + [[wiki/entities/common-room|Common Room]] → scoring model; reply intelligence from [[wiki/entities/instantly|Instantly]] → negative-signal column in Clay; disco-call notes → ICP definition; lost-deal reasons → copy framework's "do-not-promise-this" constraint.
- **Cost per delivered client flattens at the loop — not at agent one, not at agent five.** "By campaign 20, the system is making decisions on patterns that took a senior operator three years to learn manually. By campaign 200, the system has seen patterns no human operator could have seen at all." This is the [[wiki/concepts/data-flywheel|data flywheel]] / [[wiki/concepts/data-moat|data moat]] that a SaaS pure-play "can't copy off the shelf."
- **Three things stay human regardless of agent quality:** (1) the strategic call on what the campaign is actually selling (offer vs angle vs trigger event); (2) the decision to pivot when the data says the *offer itself* is broken — "most agencies respond by rewriting the copy; the senior operator responds by rewriting the offer"; (3) the client relationship — "the agents are not yet allowed in that room."
- **The agents didn't compress the work — the spine did.** In Vacca's "4 agents, one session, end-to-end campaign" video, the agents only worked because the ICP framework (trained on 2,200 prior campaigns), the list builder (an internal Clay product), and the copy patterns (the emails that generated $10M+ for clients) were "built years before the agents existed." The agents "made the compression visible on a screen recording."
- **Diagnostic for a half-built stack:** "you don't need more agents. You need to install the spine, deploy two agents on top of it, and start saving every output as an input to the next campaign. In that order." Most services-as-software builds collapse from "the right tool installed at the wrong time (read: too early)."

## Notable quotes

> "There is a sequence to the build: spine first, then agents, then the loop on top. Build any other order and the system can't compound."

> "The agents didn't compress the work. The spine compressed the work. The agents made the compression visible on a screen recording."

> "The spine doesn't ship a campaign on the day it goes in. That's the reason most founders skip it. It's also the reason the founders who skip it stall at the fifth hire."

> "Two agents on top of a clean spine outperform six agents on top of nothing. Every quarter."

> "By campaign 20, the system is making decisions on patterns that took a senior operator three years to learn manually. By campaign 200, the system has seen patterns no human operator could have seen at all."

> "A services-as-software company isn't an unattended SaaS product. The client is paying for an outcome, and the outcome lives where judgement still matters."

## Notes

- This is the **build-order companion** to Vacca's [[wiki/sources/itsalexvacca-services-as-software-7m-agency|$7M services-as-software agency playbook]]. The prior post argued *what shape* the fulfilment layer takes (Data, outreach, orchestration, reporting, knowledge — five layers); this post argues *which layer you build first*. Vacca explicitly cross-references his own "services don't scale" argument and a separate piece on "the four feedback edges."
- The spine → agents → loop sequence is a **three-phase reframing of the same DOE-shaped split** the wiki tracks elsewhere: the spine is durable shared state (data layer), the agents are scoped [[wiki/concepts/reasoning-execution-split|reasoning-execution]] units, and the loop is the compounding feedback mechanism. It rhymes strongly with [[wiki/concepts/data-flywheel|the data flywheel]] and with [[wiki/concepts/markdown-as-agent-contract|durable shared memory]] patterns — "that table is the agency's memory" is the same idea as a canonical context store the agents read from and write to.
- **The "two agents that pay back first" claim is specific and falsifiable** — Reply Manager + Enrichment Waterfall — and worth filing as a concrete instantiation of [[wiki/concepts/human-in-the-loop|human-in-the-loop]] (the Reply Manager drafts and waits for operator approval) and the 80/20 boundary (agents own the repeatable 80%, humans own the 20% edge cases + judgment).
- **Terminology caution / possible duplicate:** Vacca's "Clay" is **Clay.com** — the outbound data-enrichment / list-building platform. The wiki already has a `clay` entity, but that is the *claymorphism* design-system brand from the Open Design catalog, a completely different thing. This source's tool is filed as a distinct entity (`clay-com`) to avoid collision. Flagged for the entity phase.
- Metrics restated from the prior ColdIQ post and consistent with it: $7M+ ARR, 400+ B2B clients, 30+ team across 10 countries, 3+ years operating, 2,200 cold email campaigns shipped, $10M+ generated for clients. Treat as self-reported.
- The closing diagnostic ("install the spine, deploy two agents, save every output as an input — in that order") is the most directly actionable takeaway for any [[wiki/concepts/ai-automation-services|AI-automation-services]] builder reading from this wiki — including, plausibly, ROAM Labs client-work engagements.

## Mentioned entities

- [[wiki/entities/alex-vacca]] — author; founder/operator of ColdIQ; states the spine → agents → loop thesis.
- [[wiki/entities/coldiq]] — Vacca's $7M ARR services-as-software agency; the source of every worked example.
- [[wiki/entities/attio]] — the single CRM ColdIQ standardizes the spine on ("one CRM, not three").
- [[wiki/entities/clay-com]] — Clay.com; the canonical data table every campaign reads from and writes to ("the agency's memory"). NOT the claymorphism design brand at [[wiki/entities/clay]].
- [[wiki/entities/wiza]] — first stage of the Enrichment Waterfall (runs against LinkedIn profiles).
- [[wiki/entities/fullenrich]] — second stage; cascades through 20+ providers.
- [[wiki/entities/prospeo]] — third stage; cleans residual at 98%+ verified accuracy.
- [[wiki/entities/instantly]] — reply-intelligence source feeding the negative-signal column.
- [[wiki/entities/predictleads]] — buying-trigger source feeding the scoring model.
- [[wiki/entities/common-room]] — buying-trigger source feeding the scoring model.
- [[wiki/entities/apollo]] — named as the lead source in the failure anti-pattern ("a single Apollo CSV").
- [[wiki/entities/n8n]] — runtime for the Reply Manager agent.
- [[wiki/entities/slack]] — surface where the Reply Manager drafts replies for operator approval.

## Related concepts

- [[wiki/concepts/services-as-software]] — the business model this whole sequence serves; this post is its build-order manual.
- [[wiki/concepts/ai-fulfillment-layer]] — the named subject; the line item that decides a services business's ceiling.
- [[wiki/concepts/data-flywheel]] — what the loop turns into; "where the data flywheel finally turns into something that compounds."
- [[wiki/concepts/data-moat]] — the loop builds the data moat a SaaS pure-play "can't copy off the shelf."
- [[wiki/concepts/human-in-the-loop]] — the Reply Manager's draft-then-operator-approve gate; the 20% that stays human.
- [[wiki/concepts/ai-automation-services]] — the broader services-build cluster this diagnoses ("if you're staring at a half-built stack").
- [[wiki/concepts/reasoning-execution-split]] — agents as scoped reasoning units reading/writing the spine.

## Related sources

- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — same author; the five-layer shape this post sequences. Direct predecessor.
- [[wiki/sources/itsalexvacca-x-2052740083820958072]] — same author; earlier queued follow-up.
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — the agent-vs-automation mental model; complements Vacca's "agents handle the repeatable 80%, judgment stays human."
- [[wiki/sources/saraev-agentic-workflows-2026]] — DOE framework + reliability-decay math; the architectural companion to Vacca's economic build-order argument.
