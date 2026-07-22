---
title: AI Skills To Measure Anything - Part 1
source: https://x.com/nurijanian/status/2039264573883072836
author:
  - "[[@nurijanian]]"
published: 2026-04-01
created: 2026-07-22
description: These are 2 brand new skills I built for an extension to my PM OS that uses the skills from “How To Measure Anything” - one of the best prac...
tags:
  - "clippings"
  - "product-management"
  - "agent-skills"
---
![Image](https://pbs.twimg.com/media/HEfIq_qboAAxBR4?format=jpg&name=large)

These are 2 brand new skills I built for an extension to my [PM OS](https://www.prodmgmt.world/products/pm-os?utm_source=x&utm_medium=social&utm_campaign=howtomeasureanythingskills-1) that uses the skills from “[How To Measure Anything](https://www.lesswrong.com/posts/ybYBCK9D7MZCcdArB/how-to-measure-anything)” - one of the best practical analytical books I’ve ever read.

- **Fermi estimation:** Break seemingly immeasurable quantities into estimable components using structured factor decomposition. Use when estimating unknown quantities, sizing markets, or turning vague problems into structured estimates.
- **Clarification chain:** Convert intangible, “immeasurable” concepts (quality, security, culture, risk) into observable, measurable quantities by walking through three links: detectability, observable amounts, and measurement method.

I'm working on more skills, so watch out for part 2 and maybe 3.

![Image](https://pbs.twimg.com/media/HEfJRhNa8AA9MHr?format=jpg&name=large)

# As always, you can find them in my AI Skills Library for PMs (190+ AI skills for product work) and in the AI PM OS

## Fermi estimation

```markdown
---
name: fermi-decomposition
description: Break seemingly immeasurable quantities into estimable components using structured factor decomposition. Use when estimating unknown quantities, sizing markets, or turning vague problems into structured estimates.
type: flexible
---

# Fermi Decomposition

Break "immeasurable" quantities into estimable components.

## When to Use

- User asks "How many X are there?" for unknown quantities
- User needs to estimate something seemingly immeasurable
- Strategic planning, market sizing, cost estimation
- Any vague problem needing structure

## Method

### Step 1: Identify the Target Quantity

Clarify exactly what needs estimating:

- "How many piano tuners in Chicago?" → piano tuners actively working
- "Cost of employee turnover?" → annual direct + indirect costs

### Step 2: Find a Decomposition Path

Break into factors that multiply (or add) to the target.

**Check domain knowledge first:** Before committing to a path, verify the user knows the key concepts. If not, offer an alternative.

- Path A (direct): Volume × Density × Conversion — requires knowing constants
- Path B (comparison): "About the same as X" — uses analogies to known quantities
- Path C (iterative): Break into ever-smaller pieces until estimable

**Examples:**

- **Piano Tuners:** Tuners = (Population / People per Piano) × (Pianos per Tuner per Year)
- **Employee Turnover:** Cost = Headcount × Turnover Rate × (Recruiting Cost + Training Cost + Productivity Loss)
- **Atoms in sand (if chemistry unknown):** Compare volume to known objects, then use "atoms per cm³" rule of thumb (~10²² atoms/cm³ for solids)

### Step 3: Estimate Each Component

For each factor, provide a range (90% confidence):

- Population of Chicago: 2.7M ± 200k
- People per piano: 50-200 (guess: 100)
- Pianos tuned per tuner per year: 500-1500

### Step 4: Combine with Uncertainty

Multiply point estimates for central guess.

**For each high-uncertainty component, suggest a remedy:**

- Too uncertain? → Look up: [specific source, e.g., census data, industry reports]
- Can't estimate? → Compare to: [known reference, e.g., "about the same as X"]
- Still stuck? → Use Rule of Five: sample 5 random instances

Track which components contribute most uncertainty — these are priority for actual measurement.

### Step 5: Sanity Check

- Does answer make order-of-magnitude sense?
- What would need to be true for this to be 10x higher or lower?

**If estimate feels wrong, check:**

1. Component ranges — any bounds too narrow or wide?
2. Formula logic — units consistent? division vs multiplication correct?
3. Missing factors — any key variables omitted?
4. Base rates — how does this compare to known similar quantities?

## Output Format

**Decomposition:**
[Equation showing factor breakdown]

**Component Estimates:**
- Factor A: [value] (90% CI: [low]-[high])
- Factor B: [value] (90% CI: [low]-[high])
...

**Combined Estimate:** [central estimate] (range: [low]-[high])

**Key Uncertainties:** [which factors most affect result, and how to reduce each]

**Alternative Paths:** [if user lacks domain knowledge for primary path]

## Examples

### Example 1: Piano Tuners in Chicago

**Target:** Active piano tuners in Chicago metro

**Decomposition:**

Tuners = Population / (Households per Piano) / (Tunings per Piano per Year) / (Pianos per Tuner per Year)

**Estimates:**

- Chicago population: 2.7M
- People per household: 2.5 → ~1.08M households
- Households with pianos: ~1 in 50 → ~22,000 pianos
- Tunings per piano per year: 1
- Pianos a tuner can service per year: ~800

**Result:** ~27 tuners (actual: ~290 — within 10x)

### Example 2: SaaS Market Size in Austin

**Target:** Annual addressable market for B2B productivity tool in Austin

**Decomposition:**

Market = Companies × Adoption Rate × Price × Retention

**Estimates:**

- Austin metro companies (10+ employees): ~15,000
- Adoption rate for productivity tools: 5-15%
- Annual price: $500-2000 per company
- Net retention: 80-95%

**Result:** $3.75M - $42.75M annual market (wide range signals need for better data)

### Example 3: Employee Turnover Cost

**Target:** Annual cost of employee turnover for a 500-person tech company

**Decomposition:**

Cost = Headcount × Turnover Rate × (Replacement Cost + Productivity Loss)

**Estimates:**

- Headcount: 500
- Annual turnover rate: 15-25% (tech industry average)
- Replacement cost per employee: $50,000-150,000 (recruiting + onboarding)
- Productivity loss (months to full ramp): 3-6 months salary (~$25K-50K)
- Total cost per departure: $75,000-200,000

**Result:** 75-125 departures/year × $75K-200K = $5.6M - $25M annual cost
(actual industry rule of thumb: 50-200% of salary — within range)
```

## Clarification chain

```markdown
---
name: clarification-chain
description: Convert intangible, "immeasurable" concepts (quality, security, culture, risk) into observable, measurable quantities by walking through three links: detectability, observable amounts, and measurement method.
type: flexible
---

# Clarification Chain

Convert "intangibles" into observable, measurable quantities.

## When to Use
- User claims something is "immeasurable" (quality, risk, security, public image)
- Vague goals need concrete definitions
- Strategic objectives lack clear metrics
- Any concept that "matters but can't be measured"

## The Chain

The Clarification Chain has three links. Walk through them in order:

### Link 1: If it matters, it's detectable
**Question:** If this thing changed, what would you observe?

If "quality" improved, what would you see?
- Fewer customer complaints?
- Higher return customer rate?
- Lower defect rates in production?

If you can't name a single observable difference, the concept may not actually matter.

### Link 2: If it's detectable, it can be detected as an amount
**Question:** Can we observe more of it or less of it?

- "Fewer complaints" → complaint count per 1000 orders
- "Higher return rate" → percentage of customers who purchase again
- "Lower defect rate" → defects per million opportunities (DPMO)

If you can observe it at all, you can observe degrees of it.

### Link 3: If it can be detected as an amount, it can be measured
**Question:** How do we track this amount over time?

- Surveys → scale of 1-10
- System logs → counts per time period
- Financial records → dollar amounts
- Direct observation → binary or frequency counts

## Method

### Step 1: Name the Intangible
What does the user claim can't be measured?
- "Employee engagement"
- "Brand reputation"
- "System security"
- "Innovation culture"

### Step 2: Find the Observable Consequences
For each stakeholder, ask: "If this improved, what would they notice?"

| Stakeholder | If [Intangible] Improved... |
|-------------|----------------------------|
| Customers | Would notice... |
| Employees | Would notice... |
| Managers | Would notice... |
| Systems | Would show... |

### Step 3: Quantify the Observables (Distinguish Inputs from Outputs)
Convert observations to countable amounts, but first classify:

**Input indicators** (state of the intangible itself):
- Observable: "Employees feel safe experimenting" → Survey: "I feel safe taking risks" (1-10)
- Observable: "Leadership supports innovation" → Metric: "% of managers who allocated time to experiments"

**Output indicators** (results of having the intangible):
- Observable: "Customers complain less" → Metric: "Complaints per 1000 orders"
- Observable: "Employees stay longer" → Metric: "Voluntary turnover rate"
- Observable: "Fewer security incidents" → Metric: "Reported breaches per quarter"

**Critical:** If user wants to improve culture/environment, input indicators are primary. Output indicators lag and can be gamed.

### Step 4: Validate the Chain
Check: Does measuring these observables actually capture the intangible?
- Would improving the metrics improve the underlying concept?
- Are there edge cases where metrics improve but the intangible doesn't?

## Output Format

**Intangible:** [Original vague concept]

**Clarification Chain:**

Link 1 — Detectable consequences:
- Stakeholder A would observe: [specific observation]
- Stakeholder B would observe: [specific observation]
...

Link 2 — Observable as amounts:

**Input indicators** (state of the intangible):
- [Observation 1] → [Count/metric]
- [Observation 2] → [Count/metric]

**Output indicators** (results of having the intangible):
- [Observation 3] → [Count/metric]
- [Observation 4] → [Count/metric]

Link 3 — Measurement method:
- [Metric 1]: [How to track]
- [Metric 2]: [How to track]
...

**Validation Check:**
- Does measuring these capture the intangible? [Yes/No + why]
- Potential blind spots: [What might the metrics miss?]

## Examples

### Example 1: Employee Engagement
**Intangible:** "Employee engagement is immeasurable"

**Link 1 — Detectable:**
- If engagement improved, employees would: stay longer, produce more, collaborate better
- Managers would observe: fewer complaints, proactive problem-solving, lower absenteeism

**Link 2 — Observable amounts:**

*Input indicators (engagement itself):*
- Feel valued → Survey: "I feel recognized for my work" (1-10 scale)
- Understand company goals → Survey: "I understand how my work contributes" (1-10)
- Have resources needed → Survey: "I have the tools to do my job" (1-10)

*Output indicators (results of engagement):*
- Stay longer → Voluntary turnover rate
- Produce more → Output per employee / revenue per head
- Proactive problem-solving → Suggestions submitted / implemented
- Absenteeism → Sick days per employee per year

**Link 3 — Measurement:**
- Turnover: HRIS exit interview data, monthly rate
- Output: Sales CRM, production logs, project completion rates
- Suggestions: HR tracking system, quarterly count
- Absenteeism: Time tracking system, monthly aggregation

**Validation:** 
- Yes — these metrics collectively capture engagement
- Blind spot: Some engaged employees don't submit suggestions; need multiple indicators

### Example 2: System Security
**Intangible:** "We can't measure how secure our system is"

**Link 1 — Detectable:**
- If security improved: fewer breaches, faster detection, less downtime
- Attackers would find: harder to penetrate, more monitoring, faster response

**Link 2 — Observable amounts:**
- Breaches → Incidents per quarter, time to detect
- Downtime → Availability percentage, MTTR
- Penetration difficulty → Time to compromise (pen test results)
- Response speed → MTTD (mean time to detect), MTTR (mean time to respond)

**Link 3 — Measurement:**
- Breaches: SIEM logs, incident response tickets
- Availability: Monitoring tools (Datadog, PagerDuty)
- Pen test results: Red team exercises, quarterly reports
- Response times: SOC metrics, incident post-mortems

**Validation:**
- Partial — measures symptoms of security, not prevention
- Add: Patch latency, vulnerability scan results, security training completion
```