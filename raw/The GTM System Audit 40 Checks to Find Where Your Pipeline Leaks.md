---
title: "The GTM System Audit: 40 Checks to Find Where Your Pipeline Leaks"
source: "https://x.com/itsalexvacca/status/2079611804179955843"
author:
  - "[[@itsalexvacca]]"
published: 2026-07-21
created: 2026-07-22
description: "When a cold email system stalls, the reply rate is the number everyone stares at. It is also the least useful place to look.A reply rate is ..."
tags:
  - "clippings"
  - "gtm"
---
![Image](https://pbs.twimg.com/media/HNwuMQFacAEvSgI?format=jpg&name=large)

When a cold email system stalls, the reply rate is the number everyone stares at. It is also the least useful place to look.

A reply rate is a summary of five separate systems stacked on top of each other. List, deliverability, targeting, messaging, follow-up. Any one of them can be the thing holding the number down, and the average hides which one.

This audit breaks those five systems into 40 yes/no checks.

You run it in an hour, count the failures by stage, and start with the stage that fails the most. Everything here comes from what we have measured across 23M+ cold emails and 400+ B2B companies at ColdIQ.

![Image](https://pbs.twimg.com/media/HNvuWrpboAAoQDH?format=jpg&name=large)

The five leak points

# How to run it

Score each check **yes** or **no**. Yes means that piece is working, and no means it leaks.

Do not try to fix everything. Tally the no's per stage, because the stage with the most no's is your bottleneck, and it is almost always one stage carrying the damage for the other four.

Fix that stage, ship the next campaign, then re-audit. Run the whole thing once a quarter, because systems drift.

![Image](https://pbs.twimg.com/media/HNvuoLWaYAEkOJd?format=jpg&name=large)

Score it: count the no's by stage

# Stage 1 - List quality

The list decides more of your reply rate than your copy does. Most of what looks like a messaging problem starts here.

> A campaign built on a bad list has a ceiling, and no rewrite of the email raises it.

**1\. Is every address verified in the hours before send?** B2B lists decay 2–3% a month as people change jobs and old inboxes get retired, so an address you checked three weeks ago may already bounce. Run verification as the last step before a send and pull anything that comes back risky or unknown. One clean send protects the reputation of every send after it.

**2\. Are catch-all and role addresses (info@, sales@) stripped out?** Catch-all domains accept everything at the server and tell you nothing about whether a real person reads that inbox, and role addresses route to no one who can reply. Both inflate your list size and quietly drag deliverability down. Filter them out by rule before the campaign ever loads.

**3\. Do you send in batches of 500–1,000, not 10,000?** Blasting 10,000 scraped contacts trains mailbox providers to treat your domain as bulk mail, and placement collapses across the whole program. A tighter send of 500 to 1,000 well-researched contacts holds sender reputation and lands in far more primary inboxes. Cap the batch size and raise the bar on who earns a place on the list.

**4\. Is your bounce rate under 2–3% per campaign?** Once bounces cross roughly 2–3%, providers read it as evidence you buy or scrape lists and start throttling the whole domain. Watch the rate per segment, because when one vertical bounces several times higher than the rest, the defect lives in how you sourced that vertical. Fix the source and the rate settles on its own.

**5\. Does bounce and reply data feed back into the next list build?** Most teams let bounces and replies sit in their sending tool and never flow back to targeting, which locks the reply rate at a ceiling that has nothing to do with copy. Pipe every outcome - bounced, replied, booked, ghosted back into the model that builds the next list. The following campaign then starts from evidence instead of a fresh guess.

**6\. Is every contact matched to the right company, not just a name and an email?** A correct person attached to the wrong account produces an email that makes no sense to the reader and reads as spam. Enrich at the company level first, confirm the person actually works there today, then layer on the personal details. Getting the account right is what makes the personalization land.

**7\. Are you enriching for signals, not only firmographics?** Name, title and headcount describe a company but never tell you whether this is the week to reach out. Add live fields to every row - recent funding, open roles, a new tool in the stack, leadership changes - so timing becomes part of the list itself. A firmographic match with a fresh signal is worth ten matches without one.

**8\. Do you know your real total addressable market, or are you guessing?** Teams routinely overstate their market, work the obvious accounts too fast, and burn the best names in a month. Score the full addressable market once so you know its true size, then work it in fit order rather than at random. A ranked market lasts far longer than a rough guess.

**9\. Is the list deduplicated across campaigns and domains?** When the same prospect gets hit from three of your inboxes in one window, it reads as a coordinated pattern and trips spam filters for the whole thread. Deduplicate at both the person and the account level before every send, and keep a suppression list of anyone contacted recently. One clean touch beats three overlapping ones.

**10\. Does each list get refreshed, or rebuilt from scratch every Monday?** Rebuilding the list from zero each week throws away every reply, bounce and meeting outcome the last campaign earned. Carry those outcomes forward as the seed for the next build so the list compounds instead of resetting. By the fifth cycle the model already knows which accounts are worth a credit.

# Stage 2 - Deliverability

None of the other four stages matter if the email lands in spam. This is the gate, and in 2026 it stopped being a copy decision and turned into a compliance one.

![Image](https://pbs.twimg.com/media/HNvvJ4qaAAAyQwb?format=jpg&name=large)

The deliverability gate

**11\. Are you sending from multiple domains?** Running the whole program from one domain makes it a single point of failure, and one bad week can take the entire operation offline. Spread volume across several sending domains and multiple inboxes on each, and keep a few in reserve so you can rotate if one dips. Redundancy at the domain level is what keeps a program alive.

**12\. Are SPF, DKIM and DMARC set up and verified on every domain?** These three records tell providers the mail genuinely came from you, and a gap in any one is read as a forgery signal. Verify all three on every domain when you set it up, then re-check them, because a migration or a DNS change can silently break the alignment. Treat it as a standing check, not a one-time task.

**13\. Is each inbox capped at 30–50 emails a day?** Sending 100 an hour from a single account is the loudest red flag a filter looks for, and volume per inbox is what gets you flagged, not total volume. Cap each inbox at 30 to 50 sends a day and grow by adding inboxes rather than pushing any one harder. Volume per inbox is the number filters punish.

**14\. Did every domain warm up for at least 30 days before its first campaign?** A brand-new domain that suddenly sends real campaign volume looks exactly like a spammer and gets flagged on day one. Warm each domain for a minimum of 30 days, ramping volume gradually and generating genuine replies before any cold campaign touches it. The warm-up is the cost of entry, and skipping it burns the domain.

**15\. Is your spam-complaint rate under 0.1%?** This is the hard gate of 2026: cross a 0.1% complaint rate and providers throttle the domain no matter how good the copy is. Watch the rate per campaign and pull any list or angle that spikes it the moment you see it, because the penalty follows the domain, not the campaign. Deliverability now sits closer to compliance than to copywriting.

**16\. Are you rotating senders across ESPs?** Pushing all your mail through one provider makes the pattern trivial to detect, and one policy change can end the program overnight. Rotate across several ESPs and identities so no single provider or inbox carries the load. We send 500K+ a month across four ESPs at once for exactly this reason.

**17\. Is your identity hygiene clean, with real names, profiles and signatures?** An inbox with no photo, no signature and a half-built profile reads as automated traffic before a filter even reaches the body. Give every sending identity a full name, a real profile, and a clean signature so it looks like a person a colleague would recognize. The identity is part of deliverability, not decoration.

**18\. Do you monitor inbox placement, or only opens?** Open tracking can look healthy while half your volume quietly lands in spam, since an email in the junk folder still records an open on some clients. Run seed-inbox placement tests across the major providers so you see where mail actually lands: primary, promotions, or spam. Placement is the number that tells the truth.

# Stage 3 - Targeting and signal

Targeting decides whether the meeting you book is real. Most of the gap between meetings booked and pipeline created is settled here, before a word gets written.

> One Fortune-500 subsidiary closed a €200K+ contract off a single intent signal that triggered a 73-second personalized Loom.

**19\. Does every account on the list carry at least one buying signal?** A list with no signal is a list of strangers you are interrupting at random, and it converts like one. Require at least one reason-to-reach-out per account before it qualifies: fresh funding, a relevant hire, a tech change, or an intent spike. The signal is what turns a cold email into a timely one.

**20\. Are you acting on recent signals?** A funding round from 18 months ago tells you nothing about this quarter, and stale triggers produce outreach that lands flat. Window every signal to roughly the last 90 days so you reach accounts while the moment is still live. Freshness is most of what makes a signal worth anything.

**21\. Is your ICP split into subsegments that buy differently?** A 50-person startup and a 500-person enterprise can both match your ICP on paper and still buy for completely different reasons. Break the ICP into subsegments that each get their own angle; we run a 6-list, 2-persona, 3-variation frame on every client so no group hears a message built for someone else. Segmentation is where reply rate and pipeline quality separate.

**22\. Do you segment before you write?** Writing one email and slicing the list afterward produces copy that fits the average and speaks to no one in particular. Define the segments first, then write purpose-built copy for each so every reader feels addressed directly. Segments shape the message, and no message rescues bad segments.

**23\. Are high-signal accounts routed to a heavier touch?** Your strongest intent signals deserve more than the templated email everyone else receives. Route your top signals to a personal touch - a 60-to-90-second Loom, a hand-written note, a tailored teardown - and reserve that effort for accounts that have earned it. One signal-triggered Loom once turned into a €200K+ contract for a Fortune-500 subsidiary.

**24\. Do you know the contract value each segment produces?** Without contract value attached to each segment, you spend identical effort on a €5K account and a €150K one and cannot tell where the return sits. Tag average contract value per segment and weight your time and personalization toward the high end. Our signal-triggered campaigns now average past €150K because the effort follows the value.

**25\. Is fit scored before a Clay credit or a send is spent?** Enriching and emailing low-fit accounts burns both budget and sender reputation at once, and the meetings you book from them rarely convert. Score fit first and only enrich and contact the accounts that clear the bar, so every credit and every send goes to a name worth reaching. Cheap discipline up front saves expensive cleanup later.

**26\. Does the person you email actually own the problem you solve?** Right company, wrong role is one of the quietest reply killers, because the email reaches someone who has no reason to care. Map the specific buying role for each segment and target that title directly instead of whoever the tool surfaced first. The best-written email still fails when it lands on the wrong desk.

# Stage 4 - Messaging

When opens are healthy and replies stay flat, look at the shape of the ask before you touch the words. This is where most teams waste their optimization hours.

![Image](https://pbs.twimg.com/media/HNvviseaEAAahAi?format=jpg&name=large)

Same list, different ask

**27\. Does the email offer something usable without a call?** An email whose only move is to ask for 15 minutes transfers nothing the reader can act on, and it stays in the 1–2% reply band. Value-first emails on the very same lists clear 12% because they hand over something useful a teardown, a benchmark, a specific idea before asking for anything. Lead with what the reader can use today and let the meeting be the follow-on.

**28\. Can the reader verify one proof point inside the email?** A cold recipient with no prior exposure to you has no reason to take a claim on faith. Embed one concrete, checkable proof point right in the body a named result, a real number, a client they would recognize so belief happens inside the email without a click. Verifiable beats impressive every time.

**29\. Is there exactly one ask?** When an email carries two or three asks, the reader has to choose which to engage with, and the usual choice is none. Strip the email down to a single, small ask that is obvious in one read. One clear next step is what earns the reply.

**30\. Is the ask priced to the relationship?** "Hop on a 30-minute call this week" is expensive coming from a stranger, and the price is wrong for the trust a first email has earned. Lower it to something cheap to say yes to a short Loom, a resource, a simple yes/no question and let the relationship earn the bigger ask later. Match the size of the request to the size of the relationship.

**31\. Is personalization built on research?** "I saw your LinkedIn post" is surface-level, mail-merge personalization that every inbox now receives ten times a day. Build the personal line on a real signal the account actually shows a hire, a launch, a specific line from their site so it reads as attention rather than a token. Real research is the only personalization that still moves a reply rate.

**32\. Have you retired subject-line A/B tests as your main lever?** Subject-line testing is 2019 advice running on 2026 inboxes, where the reply floor has moved up more than 3x and the subject line is no longer the constraint. Spend those optimization hours on the offer and the shape of the ask, which is where the real lift now lives. Test the things that actually decide the reply.

**33\. Does email 1 earn email 2?** A weak first email makes the entire sequence dead weight, because no follow-up rescues an opener nobody engaged with. Make email 1 a genuinely personalized opener paired with a real value offer, then space follow-ups 3–5 days apart. The opener carries the sequence, and the follow-ups only compound what it started.

**34\. Are you building recognition before the cold email lands?** Prospects who have seen your brand three or more times before the first email convert at 2–3x cold-cold traffic on identical copy. Run light content and engagement against your target accounts ahead of the send, so the name is already familiar when the email arrives. The cheapest way to lift a reply rate is to stop being a stranger.

Run these three in order on any campaign with healthy opens and a flat reply rate. Fixing the offer on an email with no offer beats tightening an ask that was never the problem.

![Image](https://pbs.twimg.com/media/HNvvtkkaUAARJJO?format=jpg&name=large)

The three-question diagnostic

## Stage 5 - Follow-up and measurement

The last stage is where most programs stop measuring, which is why they never learn whether the first four worked.

> Meeting count is the metric that lies. A calendar can look full while pipeline stays flat.

**35\. Is your sequence four touches, spaced 3–5 days apart?** A single email leaves most of the available reply rate on the table, since plenty of replies come from the second, third, or fourth touch. Run a four-step sequence a personalized opener with value, a short follow-up, a fresh angle, then a clean breakup with 3-5 days between each. The spacing keeps you present without tipping into pressure.

**36\. Does each follow-up add a new angle?** A follow-up that just says "bumping this up" repeats the original ask and trains the reader to keep ignoring you. Give every touch its own reason to exist: a new proof point, a different use case, a fresh piece of value. Each email should earn its place in the inbox on its own.

**37\. Do you track whether a booked meeting became an opportunity within 45 days?** Meeting count is the metric that lies, and an AI-booked calendar can look full while the board deck reads "missed by 40%." Add a single CRM stage that marks whether a meeting turned into a real opportunity within 45 days, and manage to that number instead of the raw booking count. It is the one outbound KPI that stays honest.

**38\. Does a human own the 60 seconds before the meeting lands?** The handoff between a meeting booked and a meeting kept is where automation is weakest and where good pipeline quietly leaks. Put a person on the confirmation and the pre-call context a short note, a reason the call matters, a nudge the day before so the meeting actually happens. Those 60 seconds decide whether the booking becomes revenue.

**39\. Is the reason-for-loss captured and fed back to targeting?** "We are already using a competitor" and "we passed on you in Q1" are the most valuable and most wasted data in outbound. Log the reason on every lost meeting and route it straight back into how the next list is built and scored. Yesterday's losses are the sharpest input you have for tomorrow's targeting.

**40\. Does every campaign seed the next one?** A program that treats each campaign as history instead of training data resets its reply rate to zero every time it starts over. Close the loop so every outcome feeds back in and each build starts sharper than the last. Run it this way and the system compounds; skip it and you rerun the same average forever.

![Image](https://pbs.twimg.com/media/HNvwM5WagAANg7q?format=jpg&name=large)

The 45-day loop

# Run it as a skill

If you want the audit to run itself against every campaign, drop it into Claude Code as a skill. The checklist becomes the rubric, and the skill scores a campaign export, then hands back the stage with the most failures and the fix for each one.

```markdown
# gtm-audit.md
name: GTM System Audit
trigger: "audit this campaign" + a CSV or export path

steps:
  1. Load the campaign export — list, deliverability config, copy, sequence, outcomes.
  2. Score all 40 checks as pass/fail across the five stages.
  3. Tally the failures per stage.
  4. Return the stage with the most failures, the failed checks, and each fix.

output:
  stage_scores: { list, deliverability, targeting, messaging, followup }
  biggest_leak: <stage>
  actions: [ { check, fix } ]
```

Point it at one export and it tells you where to spend the week.