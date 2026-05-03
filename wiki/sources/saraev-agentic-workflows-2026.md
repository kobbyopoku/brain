---
type: source
title: "AGENTIC WORKFLOWS: Build & Sell AI Automations (2026) — Nick Saraev"
created: 2026-05-03
updated: 2026-05-03
source_url: https://www.youtube.com/watch?v=MxyRjL7NG18
source_type: video
author: Nick Saraev
source_date: 2026
raw_path: raw/saraev-agentic-workflows-2026.md
tags: [agentic-workflows, ai-automation, do-framework, horizontal-leverage, video, foundational]
---

# AGENTIC WORKFLOWS: Build & Sell AI Automations (2026) — Nick Saraev

> A 5h 41min definitive course on agentic workflows for business. Coins the **[[do-framework|DO framework]]** (Directives + Executions) as a deterministic architecture for AI workflows. Argues agentic workflows are *"one of the largest wealth transfers in human history"* enabled by **[[horizontal-leverage]]**. Provides the mathematical case (**[[reliability-decay-math]]**) for why raw LLMs fail at multi-step business processes.

## TL;DR

Saraev makes a structured economic + technical case that LLM-driven agentic workflows are about to compress the labor cost of standardized business processes by 90%+ — **but only for operators who solve the reliability problem.** Raw LLMs are probabilistic; chained 90%-success steps decay to 59% at depth 5. His answer is the **DO framework**: separate **Directives** (the *what*, declarative markdown specifications) from **Executions** (the *how*, deterministic Python scripts), with the LLM acting as orchestrator between them. This achieves 2-3% error rates on real business functions. The course covers the full toolchain: workspace setup, IDE choice (Cursor / Claude Code / Google's anti-gravity), MCP servers and their token cost, real workflow examples (lead scraping, email enrichment), workflow chaining, error recovery loops, human-in-loop decisions, and cloud/webhook deployment. The core economic claim is **horizontal leverage**: automating 90% of 10,000 people's roles is 9,000× more valuable than automating 100% of one person's role.

## Key takeaways

### The economic thesis
- **Horizontal leverage > vertical leverage.** *"Automating 100% of one person's role is equivalent to providing one unit of economic value. Whereas if you automate 90% of 10,000 people's, you're providing 9,000 units."* See [[horizontal-leverage]].
- **The wealth transfer is real and asymmetric.** Operators who can build reliable agentic workflows capture this; everyone else gets disrupted.
- **The bottleneck is not capability but reliability.** Models can do almost any single business task; getting them to do many tasks reliably-in-sequence is the hard problem.

### The reliability problem
- **Chained probability decays multiplicatively.** 5 sequential steps at 90% success each = 59% total success rate. 10 steps = 35%. See [[reliability-decay-math]].
- **LLMs are probabilistic, not deterministic.** Even with the same prompt, outputs diverge run-to-run.
- **Stochasticity / drift**: models pulled into long autonomous runs accumulate small deviations until they're solving a different problem than the one given.
- **LLMs are bad at deterministic operations.** Math, sorting, parsing, structured extraction — *"that's something you could build a Python script to do in 0.1 seconds."* See [[reasoning-execution-split]] for the wiki's existing concept on this.

### The DO framework (the headline contribution)
- **Directives** — declarative markdown files in `directives/`, one per workflow or capability (`scrape_leads.md`, `send_onboarding_email.md`). YAML frontmatter for metadata; markdown body for the *what*.
- **Executions** — Python scripts in `executions/`, deterministic and modular. The *how*. The programming language is incidental — what matters is determinism.
- **The LLM orchestrates between them.** Reads the directive, calls the right execution scripts, handles outputs, retries on errors.
- **Result: 2-3% error rates on real business functions.** Cited in the dental-marketing example.
- **Why it works**: separation of concerns. Probabilistic reasoning is bounded to "which directive applies" and "did this execution succeed?" Deterministic operations are off-loaded to code. See [[do-framework]] for full details.

### Workflow chaining and error recovery
- **Chain workflows by directive composition.** A "new client onboarding" workflow calls scrape_leads → enrich → draft_email → send_email. Each lives as a separate directive.
- **Error recovery is a 4-step loop.** Run → diagnose → fix → update. Loops until success or unfixable wall.
- **Plan for graceful recovery, not perfect prevention.** *"This thing is just going to occur and there's nothing you can do about it."*
- **Self-annealing**: workflows that improve through error feedback. *"Make this thing better. Make this thing better."* — repeated invocations with the previous output as input.

### IDE and toolchain choices
- **Anti-gravity** — Google's new agentic development platform. (Saraev demos this; verifying as a shipping product is a wiki TODO.)
- **Cursor** — already in this wiki via Brian Moran + Refero. Saraev names it as one of three primary choices.
- **Claude Code** — already substantively in the wiki via [[wiki/sources/regent0x-claude-code-247-dev-team|regent0x_]] and others.
- **VS Code** — used in the demo "just to show you can use whatever."

### MCP server economics
- **Saraev independently identifies the MCP overhead pattern** that [[wiki/sources/Mnilax-430-hours-claude-code-waste|Mnilax]] measured: *"This thing has basically filled up about half of my entire context window. And really I just have like a bunch of really simple tools."* MCP tool schemas eat ~8% of context per server.
- **Recommended discipline**: load only the MCPs the directive needs.

### Cloud workflows and webhooks
- **Web hooks as the universal trigger.** *"A web hook is literally just a URL that triggers your workflow when something hits it."*
- **Cloud-vs-local tradeoff**: cloud workflows can run while laptop is closed; local workflows preserve agentic self-annealing because the IDE-side errors are visible to the agent in real-time.
- **Distributed agent ecosystem (early stages)**: agents talking to other agents, querying each other for information, even introducing payments. *"Early versions of this do exist."*

### Human-in-the-loop heuristic
- **When to keep a human in the loop**: *"What is the magnitude of the outcome and what is the sensitivity to quality?"*
- **High magnitude or high quality-sensitivity → human in the loop.** Examples Saraev refuses to automate: client calls, contract negotiation.
- **Low magnitude + low quality-sensitivity → fully autonomous.** Lead enrichment, outbound email drafting (with review), report generation.

## Notable quotes

> "Agentic workflows have the potential to bring about what I think is one of the largest wealth transfers in human history. But very few people are currently talking about how to practically use them to improve their financial means."

> "Automating 100% of one person's role is equivalent to basically providing one unit of economic value. Whereas, if you automate 90% of 10,000 people's, you're providing 9,000 units."

> "If you have 90% success for step 1 times 90% for step 2 ... you don't end up with a 90% success rate across the entire process. You end up with a 59% success rate."

> "All DO does is reduce this so the range of possible outcomes is a lot more narrow. ... This lets me get to 2 to 3% error rates on a lot of business functions."

> "I plan for graceful recovery, not perfect prevention. And I'd recommend you do too."

## Notes

- **This is the fourth major source in the brain on AI automation services**, after [[wiki/sources/khairallah-ai-automations-10k-month|Khairallah]] (early-stage playbook), [[wiki/sources/itsalexvacca-services-as-software-7m-agency|Vacca]] ($7M ARR scaled playbook), and [[wiki/sources/realbrianmoran-making-money-online-2026|Brian Moran]] (10-models 2026 catalog). Saraev's contribution is **architectural** where the others are operational/economic — he tells you *how* to build the workflows the others tell you to sell.
- **The DO framework is the clearest "make AI workflows deterministic" pattern** ingested in the wiki to date. Cleaner than nateherk's AI OS template (which packs multiple concerns into one folder). Worth borrowing for any future Vedge automation work.
- **Cross-source agreement on MCP token cost** (Mnilax measured + Saraev observed + nateherk's "prefer API endpoints saved as markdown") is now triple-cited. This is becoming a load-bearing wiki claim.
- **Cross-source agreement on stochasticity** (hooeem's workflows-vs-agents framing + Saraev's drift framing) is double-cited. Reliability is the consistent enemy.
- **"Anti-gravity"**: Saraev demos a tool he calls Google's anti-gravity. Worth verifying — it may be a real shipping product (Google has been working on agentic IDEs) or a name Saraev uses informally. Flagging as unverified.
- **The course is **packaged as a comprehensive guide.** It's structured in named modules: idees, workspace setup, first flow, the DO framework, directives, executions, skills, MCP, cloud workflows, webhooks. Useful as a reference index when designing your own course-shaped material.
- **Quotability is high.** Several lines (the wealth-transfer thesis, the 9,000× horizontal-leverage line, the 59% chained-probability line, the "graceful recovery not perfect prevention" line) are directly usable as anchors in future work.
- **What's NOT in the course**: pricing for client engagements (Khairallah and Vacca cover this), team scaling and hiring (Vacca), broader monetization strategy (Brian Moran). Saraev is the architectural specialist; he leaves the business-side detail to others.

## Mentioned entities

### People
- [[wiki/entities/nick-saraev]] — author.

### Products and tools
- [[wiki/entities/cursor]] — already in wiki; named as one of three primary IDE choices.
- [[wiki/entities/claude-code]] — already in wiki; same.
- [[wiki/entities/anymailfinder]] — email enrichment tool referenced in lead-scraping demo.

## Related concepts

- [[do-framework]] — canonical wiki source for this concept.
- [[horizontal-leverage]] — canonical wiki source for the economic thesis.
- [[reliability-decay-math]] — canonical wiki source for the chained-probability problem.
- [[ai-automation-services]] — Saraev is the fourth major source treating this concept.
- [[services-as-software]] — Saraev's framing fits this pattern.
- [[reasoning-execution-split]] — strongly aligns with Saraev's DO framework (LLM reasons; deterministic code executes).
- [[agent-workflow-patterns]] — Saraev's workflow-vs-agent tradeoff aligns with hooeem's framing.
- [[claude-code-overhead-patterns]] — Saraev independently observes MCP overhead.
- [[ai-os-pattern]] — Saraev's directives/executions pattern parallels nateherk's contexts/skills.

## Related sources

- [[wiki/sources/khairallah-ai-automations-10k-month]] — early-stage services playbook.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — scaled-agency playbook.
- [[wiki/sources/realbrianmoran-making-money-online-2026]] — names AI services as one of 10 models.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — sibling on agent-building fundamentals.
- [[wiki/sources/Mnilax-430-hours-claude-code-waste]] — quantitative MCP-overhead source Saraev independently corroborates.
- [[wiki/sources/nateherk-claude-code-os-3m-business]] — sibling AI-OS framework with similar architectural moves.
