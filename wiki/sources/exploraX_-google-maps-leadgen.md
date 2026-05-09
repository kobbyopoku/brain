---
type: source
title: m0h (exploraX_) — Google Maps lead-gen for AI services (5-step concrete playbook)
created: 2026-05-09
updated: 2026-05-09
source_url: https://x.com/exploraX_/status/2052774623473803483
source_type: x-thread
author: m0h (exploraX_)
source_date: 2026-05-08
raw_path: raw/How to Use Google Maps to Find Paying Clients For Free..md
content_status: substantive-verbatim
tags: [ai-automation-services, lead-generation, cold-outreach, claude-code, instant-data-scraper, sales]
---

# m0h (exploraX_) — Google Maps lead-gen for AI services (5-step concrete playbook)

> Concrete 5-step lead-generation playbook for AI-services builders. **Fills the wiki's biggest gap in [[ai-automation-services]] coverage**: how to find first customers. Existing sources (Khairallah, Vacca, heynavtoor) cover *what to deliver* and *how to scale*; this one covers *how to find paying small-businesses today*. 4 prospect signals (low reviews / no website / no review-responses / missing basics) → Instant Data Scraper Chrome extension → Claude Code filters and writes outreach → call top 20 prospects → 3-objection-handler script → meeting-close framework with 3 paid-deliverable options.

## TL;DR

Five steps, runnable today:

1. **Identify prospects via 4 signals** on Google Maps:
   - Review count under 30
   - No website linked
   - No responses to existing reviews
   - Missing basics (photos, hours, description)
   - **2 or more signals = qualified prospect.**
2. **Scrape the list** with [Instant Data Scraper](https://chromewebstore.google.com/) (free Chrome extension): Google Maps → search "[service] in [city]" → scroll list bottom → click extension → CSV download. ~100-120 businesses in 90 seconds.
3. **Feed CSV to Claude Code** in two stages:
   - **Stage 1 — filter**: score 0-4 on signals, output `prospects.csv` with `signal_score` + `signal_notes` columns.
   - **Stage 2 — outreach (call first, email second)**: cold-call the top 20 (10% meeting-book rate vs 1-2% email reply rate), generate per-prospect email fallback for unreached.
4. **Handle 3 objections** (the only ones that matter):
   - *"I'm not interested"* → agree, then bring back to specific observation.
   - *"Just send me an email"* → agree, but get small commitment first.
   - *"How much?"* → don't answer; offer 15-min walkthrough this week.
5. **Close the meeting** with 1 of 3 productized offers based on the gap they admitted: one-page website / review automation / AI receptionist or missed-call text-back.

Whole flow runs in ~2 hours. Manual equivalent = entire week.

## Key takeaways

### The mental model: every business is a leaky bucket

> *"Every local business is a bucket. They pour money in ads, signs, referrals trying to fill it with customers. But most of these buckets have holes: leads come in and fall right through. Your job isn't to pour more water in. Your job is to find the holes and plug them."*

This is a cleaner version of [[wiki/concepts/switching-forces|switching-forces]] applied to *prospect identification*: the 4 signals are observable indicators that the *push* and *anxiety* forces are already active in the prospect's mind. The owner already knows something is broken; the cold call just makes the gap visible.

### Cold call > cold email for high-intent prospects

> *"Cold emails get a 1-2% reply rate. Cold calls to qualified prospects book meetings at closer to 10%. It's not even close."*

Important counterweight to the wiki's existing cold-acquisition canon ([[wiki/sources/itsalexvacca-services-as-software-7m-agency|ColdIQ]] is email-centric). For local-services + AI-services intersection (where qualification is observable from the listing), **call beats email by ~10×**. Worth flagging as a niche rule.

### The 10-second opening (memorize, don't read)

> *"You want to know your opening 10 seconds by heart, and then trust yourself for the rest. The goal in those first 10 seconds isn't to pitch. It isn't to book a meeting. It's to give the owner one reason to stay on the call instead of hanging up."*

Three-part 10-second template:

1. **Say their name.** *"Hey, is this John?"* → tiny conformity thread.
2. **Lead with the observation, not the offer.** *"I was looking at your Google listing this morning and noticed you don't have a website linked."* → no agenda, just a fact.
3. **End with a question, not a pitch.** *"Is that something you've been meaning to fix, or is it just not a priority right now?"* → hands them control.

The pattern: **specificity > script**. Pulled directly from `signal_notes` column for that row.

### 3 productized offers (the close)

| Gap admitted | Offer |
|---|---|
| No website | One-page website (phone / services / hours / quote form). Afternoon's work, no-code tool. |
| < 30 reviews | Review automation (text every customer review link after job; doubles count in 60 days). |
| Phone unanswered (~62% of calls miss) | AI receptionist or missed-call text-back. |

**One gap, one fix. Don't pitch all three.** This composes with [[wiki/sources/saraev-agentic-workflows-2026|Saraev's]] [[horizontal-leverage]] thesis — small-business AI automation is the lowest-friction wedge for $3-15K builds.

### The two Claude Code prompts (verbatim)

The article ships two complete prompts as agent contracts:

**Stage 1 (filter)** — pasteable in Claude Code session:
```
Read the file `hvac-phoenix.csv`. Each row is a local business from Google Maps.
For each row, score it from 0 to 4 based on how many of these signals it has:
 1. Review count is under 30
 2. No website listed
 3. Star rating is below 4.0 (suggests poor review management)
 4. Missing key fields (no phone, no address, etc.)
Then visit the website (if one exists) and check whether they respond to reviews.
If they don't, add 1 to the score.
Output a new file called `prospects.csv` containing only the rows with a score of 2 or higher.
Add two new columns: `signal_score` and `signal_notes` (a short list of which specific holes you found).
Sort by signal_score descending — best prospects on top.
```

**Stage 2 (email fallback)**:
```
Read `prospects.csv`. For each row, write a short cold email tailored to that specific business based on its `signal_notes`.
Rules:
- Lowercase, friendly, no corporate filler
- Lead with one specific observation about THEIR listing
- Mention one thing they're doing well
- Offer to share a free breakdown — never ask for a call
- Maximum 4 short paragraphs
Output everything into a new file `outreach.csv` with columns: business_name, phone, email, signal_notes, email_subject, email_body.
```

These are clean instances of [[markdown-as-agent-contract]] at the *task scope* — input source + processing + output specified explicitly.

## Notable quotes

> "Almost none of them tell you the part that actually matters: how do you find clients who are ready to pay for any of this?"

> "Two or more of these signals = prospect. The businesses that hit this profile aren't skeptical when you reach out. They already know something is broken. They just don't know who to call. That's the whole game."

> "The only reason that works is genuine specificity. You're not 'an agency' calling about 'their digital presence' — you're a human who actually looked at their listing and noticed something real."

> "If they engage past 60 seconds, they're asking questions, they're agreeing the gap is real, they're not trying to get off the call — book the meeting. Don't drag it out."

## How this composes with the wiki

- [[wiki/concepts/ai-automation-services]] — **fills the lead-generation gap**. Wiki's previous coverage was strong on *what to deliver* (Khairallah's 6-phase playbook, Vacca's $7M scaled version) and *what to charge* ($3-15K). This source adds *how to find first 20 prospects today*. Material upgrade.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — pairs as the consumer-acquisition layer to Khairallah's service-design layer.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — different scale (Vacca: enterprise email-centric). exploraX_ is local-business call-centric. Both compose; not opposed.
- [[wiki/sources/ig_claims-x-meta-retargeting]] — covers *retargeting* (warm audience). exploraX_ covers *cold lead-gen*. Together: cold prospect identified → call → meeting → if ghosts → retarget. Full funnel now in the wiki.
- [[markdown-as-agent-contract]] — two verbatim Claude Code prompts as task-scope contracts.
- [[switching-forces]] — 4 signals are observable indicators of push + anxiety forces.

## Mentioned entities

- [[wiki/entities/exploraX_]] — *(new)* author (signs as "m0h").
- [[wiki/entities/instant-data-scraper]] — *(stub candidate)* free Chrome extension.
- [[wiki/entities/google-maps]] — *(stub candidate)* prospect surface.
- [[wiki/entities/claude-code]] — agent runtime.

## Related concepts

- [[ai-automation-services]] — fills the lead-gen gap.
- [[markdown-as-agent-contract]] — two verbatim task-scope contracts.
- [[switching-forces]] — push+anxiety as observable signals.
- [[landing-page-patterns]] — adjacent (one-page website is one of the 3 productized offers).
- [[ai-seo]] — adjacent (review-automation is partly an AI-SEO play).

## Related sources

- [[wiki/sources/khairallah-ai-automations-10k-month]] — service-design layer; complementary.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — scaled sibling; different acquisition channel.
- [[wiki/sources/ig_claims-x-meta-retargeting]] — retargeting layer; full funnel composition.
