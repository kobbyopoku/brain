---
title: "Forward Deployed Engineer (FDE): Skills and Complete 90 Day Roadmap"
source: "https://x.com/pvergadia/status/2079351037966815593"
author:
  - "[[@pvergadia]]"
published: 2026-07-20
created: 2026-07-21
description: "Week three of an enterprise AI deployment. The CTO is skeptical. The customer’s engineers feel threatened. The VP’s timeline makes no sense...."
tags:
  - "clippings"
  - "ai-careers"
  - "fde"
---
![Image](https://pbs.twimg.com/media/HNtVHz5bsAAdrGq?format=jpg&name=large)

Week three of an enterprise AI deployment. The CTO is skeptical. The customer’s engineers feel threatened. The VP’s timeline makes no sense. Someone has to sit in that room, figure out the gap between what the customer thinks they need, what they actually need, and what’s technically possible, then build the thing and leave it working.

That someone is now called a Forward Deployed Engineer. Postings are up something like 800%. Anthropic, OpenAI, Databricks, Palantir, all hiring, with total comp at the AI labs running $350K to . And nobody in tech is telling you the most useful fact about this job: it isn’t new. I started my career doing exactly this work. It just had a worse name and no equity. Once you see that, everything about how to get the role becomes obvious.

> **We’ve Had This Job for Thirty Years**

Enterprise software has always needed a person who ships inside the customer’s mess. Around 2005 to 2015, that person showed up twice in the deal cycle.

Before the contract, they were a Solutions Architect. Free, because the vendor wants to win your business. Sitting with customers, sometimes for weeks, whiteboarding what the deal would actually take. That person was me. I have vivid memories of translating between a CTO who hadn’t said out loud that he didn’t believe any of it, and engineers who were quietly doing the math on their own jobs.

After the contract, they were Professional Services. Same work, except now it costs money. Embedded with the customer’s engineering team, on-site for months, moving fast through environments that were never as clean as the sales deck promised.

Both got measured on exactly one thing. Did the customer’s problem get solved in production? Not features. Not lines of code.

Embed. Build. Own the outcome. That’s the whole job, and it’s been the job since before some of the people now interviewing for it could drive.

![Image](https://pbs.twimg.com/media/HNtVpGBa8AACQ1t?format=jpg&name=large)

FDE History

## So What Changed? Three Things

AI collapsed implementation time. Six months became six weeks, sometimes days, because Claude Code and the modern stack write the scaffolding for you. The typing got easier. And the economics flipped with it: one FDE now covers what took a team of three a few years ago. That’s why AWS put a billion dollars into a dedicated FDE org, and why Databricks unified Pro Serv across 1,900+ customer engagements. The math finally works at AI speed.

The hard problems moved. Coding shrank; thinking got harder. Pro Serv never had to check for hallucinations. I never built an eval pipeline as an SA, not once. Your logs and metrics and traces will not catch LLM failures, which is a genuinely uncomfortable thing to explain to a customer who just spent two decades trusting their monitoring stack. Verification is the new discipline: rubric-graded test suites, LLM-as-judge, golden datasets.

And the role got a name that made VCs write checks. I know that sounds cynical. It’s also just true. “Solutions Architect” meant decades of work, no equity, less prestige. “Forward Deployed Engineer” commands attention and compensation for the same work plus an AI layer. The rebrand matters. Use it.

So what are the skills you need and how do you lands this FDE role anyway? Let’s look at that now and also a video detailing all this.

## The Skills You Need To Be FDE

![Image](https://pbs.twimg.com/media/HNtVzvcagAAmv82?format=jpg&name=large)

Skills you need to be FDE

Everyone asks for the tool list first. The tools are the easy half.

Half the job is communication, and I don’t mean the LinkedIn version of that word. When a customer says “reduce claims processing time,” the work is asking what that means. Current time? What breaks? What does compliance require? All before anyone writes code. Then you’re managing three audiences on one project: a technical workshop for the IT lead, a working session for finance ops, a check-in for the CIO. Same project, three views, and you’re shipping the whole time.

Reading the room is load-bearing. I keep coming back to this one because it’s the skill people dismiss. A threatened engineer and a CTO whose skepticism hasn’t surfaced yet will kill your deployment faster than any bug, and neither of them will tell you it’s happening.

Also: done means the business outcome is real, not that the demo worked. And write things down. Architecture decisions, deployment rationales, customer constraints. Your deliverable lives after you leave; build brilliant and leave nothing behind and you failed.

The other half is engineering, the new kind. RAG systems and where they fail. Agentic workflows, MCP, context engineering. System design with primitives that didn’t exist three years ago: token cost budgets, latency budgets, eval gates, prompt versioning. And eval engineering, which is the single sharpest filter in the hiring loop right now. Anthropic’s job specs require eval frameworks by name. If you’ve never built a rubric-graded suite, that is your first homework, this week. Regulatory fluency rounds it out because enterprise customers ask about the EU AI Act on day one, and “let me get back to you” is not a great look in that meeting.

![Image](https://pbs.twimg.com/media/HNtWHkqasAAZA_O?format=jpg&name=large)

FDE Resume Tips

The trade-off nobody likes hearing: you will not be the world’s best RAG engineer or the world’s best account manager. Communicators without the AI layer win trust and can’t ship. Engineers without customer skills ship things nobody adopts, then bomb the customer-empathy round, which exists specifically to test how you hold a room. Being credibly good at both is the rarity, and rarity is what they’re paying [$350K+](https://x.com/search?q=%24350K%2B&src=cashtag_click) for.

Check out my detailed live session on FDE here: [https://youtube.com/live/kyP0WZEgK8E](https://youtube.com/live/kyP0WZEgK8E)

![Image](https://pbs.twimg.com/media/HNtWnnIbYAAZY-4?format=jpg&name=large)

## The Roadmap You Need To Become FDE

From SA: your stakeholder skills transfer as-is. Your gap is the production AI layer, real coding in customer environments, RAG, agents, evals. 60 to 90 days on the AI stack.

From Pro Serv: you already deploy, embed, and own outcomes. Your gap is AI fluency, iteration speed, and exec presence. Also 60 to 90 days, focused on AI app development.

From SWE: coding depth and system design instincts, check. Your gap is everything customer-facing, and it’s the longer road: 90 to 120 days building communication and the AI stack at the same time.

Here’s the thing that cuts across all three, and I’d argue it’s the most underrated fact in this space: mid-career engineers beat juniors in FDE loops. The customer-empathy and system-design stages reward judgment, and judgment comes from shipping production systems through real constraints. You don’t need more experience. You need to point the experience you already have in the right direction. A lot of that is storytelling. Work on that.

Your Resume Is Written in the Wrong Language

“Designed multi-cloud architecture for enterprise clients.” A hiring manager learns nothing from that sentence.

“Designed hybrid cloud architecture for Chevron. Reduced time-to-production from 9 months to 11 weeks. Influenced $4.2M contract expansion.” Now they know the customer, the mess, what you built, and the number that changed.

Lead with impact, not task. Name the stakeholder complexity, yes, including the skeptical CTO. Show speed, because compression is FDE currency: “shipped in 6 weeks against a 5-month estimate.” Show what you left behind, did the team own it after you? And for any AI project, add the eval line. How did you verify it worked? If that question makes you flinch, see homework, above.

## Should You Go For It?

If you’ve done any version of embedded, outcome-owned customer work: yes, now. The market is paying a premium for a skill set you’re closer to than you think. If you’ve done none of it, build the missing half before you interview, not during. I’ve watched people try the “during” version. It doesn’t go well.

Where does that leave you? If you’re an SA or Pro Serv type with real customer scar tissue, go now, and build one eval pipeline this month while you apply. If you’re a SWE who’s shipped production but never sat across from a customer, you’re about four months out; start volunteering for customer-facing work today. If you’re junior, under three years, with no production ownership, not yet: go ship something real under real constraints first, the role will still be here. And if you’re a deep AI researcher who hates meetings, skip it entirely. The room is the job.