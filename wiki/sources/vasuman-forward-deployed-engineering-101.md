---
type: source
title: vasuman — Forward Deployed Engineering 101
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/vasuman/status/2057177266984226892
source_type: x-thread
author: vasuman (@vasuman)
source_date: 2026-05-20
raw_path: raw/Forward Deployed Engineering 101.md
content_status: substantive-verbatim
tags: [forward-deployed-engineering, fde, applied-ai, agent-deployment, evals, palantir, varick, ai-services, career]
---

# vasuman — Forward Deployed Engineering 101

> Definitive guide to the **Forward Deployed Engineer (FDE)** role — the author's framing of "the hottest role in tech right now" — covering why Applied AI companies need FDEs, the three-phase job (Audit / Evals / Deployment), and a 30-day roadmap to break in. Written by an FDE-turned-hirer at [[wiki/entities/varick|Varick]]; the role's lineage traces to [[wiki/entities/palantir|Palantir]].

## TL;DR

An FDE is a highly skilled engineer who deploys *on-site* with a customer, understands their workflows deeply, writes code into unfamiliar codebases, and communicates business impact to non-technical decision-makers. The thesis: if intelligence is commoditizing, the only competitive edge is *how and where* you apply it — and that placement work is the FDE's job. The role decomposes into three phases — **Audit** (map workflows, decide what to automate), **Evals** (prove the agent works to skeptical executives), and **Deployment** (build over existing data, sandbox, ship the smallest unit of autonomy first). The piece doubles as a recruiting funnel for Varick, an Applied AI company in SF.

## Key takeaways

- **The core thesis is "intelligence is commoditized, placement is the edge."** The author argues there is *no competitive advantage in intelligence alone* — the value is in determining how and where a company uses it, which is the FDE's role.
- **The FDE is "a million-dollar hire."** Defined as someone who can (1) understand a customer's problems deeply, (2) write code into a codebase they've never seen, and (3) communicate business impact to a non-technical decision-maker to close the deal.
- **On-site presence is non-negotiable.** Palantir's CTO is cited: *"you cannot build products for an environment without actually being in the environment itself."* Real efficiency gains require rebuilding a company around AI from the ground up, only possible by sitting with the customer.
- **The term FDE originated at Palantir.** Cited origin: in 2010 Palantir worked with Special Forces in Afghanistan — soldiers ran missions by day, routed feedback to FDEs who shipped code overnight.
- **The job has exactly three phases: Audit, Evals, Deployment.**
- **Audit = mapping workflows team-by-team** (e.g. two weeks with rev ops, one with procurement, a month with finance), learning each team's job, bottlenecks, and where agents could deliver value.
- **Three automation-decision rules** (from the Audit phase): (1) if a workflow distills to rules but inputs vary (email / PDF / scanned image) and involves tool calls → use an agent; (2) if rules *and* inputs are predictable → plain code is faster and cheaper; (3) if the decision needs pattern recognition + domain expertise → leave it manual.
- **Volume gate for ROI:** agents that run ~5 times a month don't pay off — look for lengthy, high-volume automations.
- **Don't over-use AI.** Most automation is a series of tool calls with *one* LLM call as an orchestrating layer; excess AI compounds token cost at scale and often lowers output quality. (This is [[wiki/concepts/reasoning-execution-split|reasoning-execution-split]] in prose.)
- **Evals must verify the agent thinks like a human, not just that the final answer is correct.** Two methods: (1) trace a human's multi-step process and grade the AI at each checkpoint; (2) start small with great gold-standard examples of the intended outcome, then measure everything against them.
- **Evals are the trust mechanism that proves ROI to skeptical executives.** "A good agent evaluation is what an executive needs to trust the agent will provide ROI."
- **Deployment: avoid large-scale data migrations.** Build APIs over the *existing* data layer (SharePoint, databases) and place a model on top as an orchestrator to query through it — clients have spent millions and years migrating to their latest ERP and won't rip it out again.
- **Build a sandbox execution environment in the company's infra** to run/test/debug the agent before production.
- **Ship the smallest unit of autonomy first, then layer capability.** Worked example: start with an agent that catches bugs, investigates, and writes a ticket; only once that works do you grant it write-code-and-push-PR ability.
- **Three backgrounds break in most easily: Consultants, PMs, and Software Engineers.** Consultants/PMs already translate data → ROI but lack engineering depth; SWEs have engineering depth but must master *communication* to non-technical VPs.
- **Portfolio + ability to articulate the business case are the deciding factors.** Four named portfolio projects: a production-ready AI agent (with API calls, autonomous logging, failure harness), a RAG pipeline on an industry dataset, a self-built eval framework scoring across correctness/format/cost/latency, and an MCP connecting an LLM to legacy software.
- **30-day roadmap with 4 checkpoints** (7/14/21/final days) covering: agent loops, tool calls, guardrails (input validation + max-step limit + output filtering), context-vs-external-memory, audit trails, structured JSON outputs, checkpointing, retry + exponential backoff (1s/2s/4s/8s cap 16s), cost optimization (cheaper models for cheap subtasks, Opus only for reasoning, prompt caching, max-token caps), golden datasets (20 real queries, hand-labeled), and multi-agent pipelines.
- **"Lack of communication ability is a deal-breaker for the FDE role."** If you can't explain what AI can and can't do to a non-technical decision-maker, there is no deployment.

## Notable quotes

> "If you believe intelligence is becoming commoditized, it then follows that the only competitive edge is how and where you use it. In fact, I will go so far as to say that there is no competitive advantage in intelligence alone."

> "The FDE is a highly skilled engineer who can understand the customer's problems very deeply, write code into a code base they've potentially never seen before, and communicate the business impact to a non-technical decision maker to close the deal. This is a million-dollar hire."

> "Palantir's CTO says that you cannot build products for an environment without actually being in the environment itself."

> "Most automation tasks can be done with a series of tool calls and just one call to an LLM as an orchestrating layer. Too much AI leads to unneeded token costs (which compound at scale) and often a lower-quality output."

> "Start with the smallest unit of autonomy; only then give it the capability to take action."

> "Reliable agents treat the model as a reasoning engine — not an execution engine." *(paraphrasing the same idea as [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap|Nainsi's tool-calling roadmap]]; the FDE piece states it as "just one call to an LLM as an orchestrating layer".)*

## Notes

- **This is the wiki's first source on the FDE role as a distinct job archetype.** Prior business-model sources cover the *firm* side of AI services ([[wiki/concepts/ai-automation-services|ai-automation-services]], [[wiki/concepts/services-as-software|services-as-software]]); this is the first to profile the *individual engineer* inside an Applied AI firm. It complements rather than competes — the FDE is the human unit that delivers the services-as-software motion.
- **The Audit/Evals/Deployment triad is a clean engagement lifecycle.** It maps directly onto Godwin's own client-work motion ([[wiki/projects/coffee-break-with-big-sis|Coffee Break]], [[wiki/projects/stacesprouts|StaceSprouts]], the [[wiki/projects/cpc-rtbvd|CPC RTBVD]] subcontract) and onto [[wiki/projects/helm|Helm]]'s internal agent-build process — Helm's Audit-equivalent is choosing which of the 6 agents to build, its Evals-equivalent is unmeasured today (flagged below).
- **The automation-decision rules are the most reusable artifact.** "Rules-but-variable-inputs-plus-tool-calls → agent / predictable-both → code / pattern-recognition-plus-expertise → manual" is a crisp triage heuristic worth promoting to a concept if it recurs. It generalizes the *when NOT to use AI* discipline that [[wiki/sources/cyrilxbt-claude-agent-manages-business|CyrilXBT's agent-vs-automation post]] frames philosophically.
- **The "build over existing data, don't migrate" deployment principle is load-bearing for Godwin's portfolio** — his clients (per the CPC RTBVD brief) have ERP/SharePoint/legacy systems they will not replace. The orchestrator-over-existing-data-layer pattern is exactly the [[wiki/concepts/mcp-server|MCP-over-legacy]] play.
- **The evals guidance is thinner than the wiki's other eval-adjacent content** but is the only source so far to frame evals explicitly as an *executive-trust / sales* instrument rather than purely an engineering QA tool. That framing is the novel contribution.
- **Recruiting-funnel framing (mild promotional weight).** The piece closes with a Varick careers CTA and the detail that Varick is "led by a former COO of Citadel Securities." The advice is substantive and not gated, but the source's purpose is partly lead-gen for Varick FDE hires — worth noting, not disqualifying.
- **Uncertainty:** the Palantir-Afghanistan-2010 origin story and the "Palantir's CTO says…" quote are presented without citation; treated here as the author's claims, not independently verified. The "65→94% accuracy" style metrics seen elsewhere in the wiki do *not* appear here — this piece makes no quantified efficacy claims, which is itself notable for a career-advice thread.
- **Two prerequisite sources are referenced but not in the wiki:** the author's own *Agents 101* (how to build an agent) and *Agents 102* (demo → production), both X threads by @vasuman. Candidates for future ingest if the FDE cluster grows.

## Mentioned entities

- [[wiki/entities/vasuman]] — author; former FDE, now builds the FDE motion at Varick.
- [[wiki/entities/varick]] — the author's Applied AI company; deploys FDEs to clients; hiring FDEs in SF.
- [[wiki/entities/palantir]] — credited origin of the FDE role and on-site-deployment philosophy.
- [[wiki/entities/anthropic]] — named (alongside OpenAI, Google) as an AI company hiring FDEs; *Building Effective Agents* + *Demystifying evals for AI agents* cited as study material.
- [[wiki/entities/openai]] — named as an AI company hiring FDEs; tool-use + structured-outputs docs cited.
- [[wiki/entities/google]] — named as an AI company hiring FDEs.
- [[wiki/entities/citadel-securities]] — Varick's leadership pedigree (former COO leads Varick).

## Related concepts

- [[wiki/concepts/forward-deployed-engineering]] — the source's central subject; this is its canonical introduction to the wiki.
- [[wiki/concepts/agent-evals]] — the Evals phase; trace-human-steps + gold-standard-examples; evals as executive-trust instrument.
- [[wiki/concepts/reasoning-execution-split]] — "one LLM call as orchestrating layer, rest is tool calls"; over-using AI is an anti-pattern.
- [[wiki/concepts/ai-automation-services]] — the firm-level model the FDE delivers inside.
- [[wiki/concepts/services-as-software]] — Applied AI companies (Varick) are the services-as-software shape; FDE is its delivery unit.
- [[wiki/concepts/mcp-server]] — "build APIs over existing data + model as orchestrator" and the MCP-over-legacy-software portfolio project.
- [[wiki/concepts/retrieval-augmented-generation]] — RAG pipeline named as a core portfolio project.
- [[wiki/concepts/agentic-loop]] — Checkpoint-1 "prompt → model → response → next step" loop.
- [[wiki/concepts/multi-agent-orchestration]] — Checkpoint-3 multi-agent pipelines (one plans, others execute, one synthesizes).
- [[wiki/concepts/scheduled-automation]] — high-volume / lengthy automations as the ROI gate for agent deployment.

## Related sources

- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — shares the model-as-reasoning-engine-not-execution-engine principle; the engineering deep-dive to this piece's manager-level framing.
- [[wiki/sources/cyrilxbt-claude-agent-manages-business]] — agent-vs-automation judgment framing; complements the FDE's "what to automate vs not" Audit rules.
- [[wiki/sources/khairallah-ai-automations-10k-month]] — firm-side AI-automation-services playbook; FDE is the in-house engineer version of the same motion.
- [[wiki/sources/itsalexvacca-services-as-software-7m-agency]] — services-as-software agency math; Varick is a same-category company, FDE is its delivery role.
- [[wiki/sources/saraev-agentic-workflows-2026]] — DOE framework + reliability-decay-math underpinning the "minimize LLM calls" discipline the FDE piece prescribes.
