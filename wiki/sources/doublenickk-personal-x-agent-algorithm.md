---
type: source
title: doublenickk — Build a personal AI Agent that posts on X exactly like you and lands in the algorithm
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/doublenickk/status/2055719881493123275
source_type: x-thread
author: doublenickk (@doublenickk)
source_date: 2026-05-16
raw_path: raw/Build a personal AI Agent that posts on X exactly like you and lands in the algorithm.md
content_status: substantive-verbatim
tags: [agent, personal-ai, content-os, x-algorithm, recommendation-system, claude-code, multi-agent, human-in-the-loop, voice-cloning, telegram]
---

# doublenickk — Build a personal AI Agent that posts on X exactly like you and lands in the algorithm

> A long-form X thread that reverse-engineers xAI's open-sourced For You feed algorithm into concrete content rules, then gives three escalating Claude-Code blueprints for a personal agent that writes posts in your voice optimized for the 14 engagement signals the algorithm actually scores.

## TL;DR

doublenickk claims xAI open-sourced the full For You feed recommendation system at `github.com/xai-org/x-algorithm`, read the source for a week, and distilled it into a content strategy plus a buildable agent. The load-bearing finding: the algorithm doesn't score "engagement" as one number — it predicts probabilities for **14 distinct user actions**, weights each, and sums them (`Final Score = Σ (weight_i × P(action_i))`), so content should optimize for a *portfolio* of positive signals, not one. The thread then offers three Claude-Code agent architectures (Session Agent / Approval Pipeline / Autonomous Stack) that generate posts in the user's voice, calibrated to those signals, with a strong insistence on a human review gate and a weekly Voice Style Guide refresh.

## Key takeaways

- **xAI open-sourced the For You feed recommendation system** as actual source code (not a blog post) at `github.com/xai-org/x-algorithm`; the thread is built from reading that repo.
- The repo's **four main components**: Home Mixer (orchestration), Thunder (in-network / followed-account post retrieval), Phoenix (the Grok-based ML ranking model), and a Candidate Pipeline framework.
- **The scoring formula** is `Final Score = Σ (weight_i × P(action_i))` — the algorithm predicts probabilities for 14 actions and multiplies each by a weight; the **weights are not public, but the actions are**.
- **The 14 signals**, with the thread's claimed relative weighting: Reply (high+), Repost (high+), Favorite/like (medium+), Follow_author (very high+, the single highest positive), Click/profile-click (medium+), Dwell (medium+) — and negatives: Not_interested (high penalty), Mute_author (high penalty), Block_author (very high penalty), Report (severe penalty, triggers visibility filtering). (Thread enumerates 10 of the 14 explicitly.)
- **The Grok transformer has eliminated hand-engineered features** and learns relevance entirely from engagement history (likes / replies / shares / dwell), which means **topic and style consistency is literally algorithm training** — inconsistency confuses the matching model.
- **Author Diversity Scorer**: the algorithm attenuates a post's score each time it has already shown one of your posts to the same user in a session — so flooding your audience in a short window *hurts* per-post distribution.
- **First-hour in-network engagement (via Thunder) is the gate for out-of-network distribution (via Phoenix)** — timing of posts to when engaged followers are active is a primary lever; thread suggests Tue–Thu, 8–10 AM or 6–8 PM in the audience's timezone as a generic default.
- **A personal agent beats a generic AI writing tool** because of *memory + pattern*: a generic tool produces content; a personal agent produces *your* content calibrated to signals, in the recognized voice.
- **The pre-build step is a Pattern Analysis prompt** run in Claude Code that produces a **Voice Style Guide** — "the most important document your agent will use. Everything else is scaffolding around it." (The prompt itself is shown as an image in the thread, not transcribed.)
- **Three escalating blueprints**:
  - **Blueprint 01 — Session Agent**: Claude Code + a `MEMORY.md` / `CLAUDE.md` project file loading voice + topic positioning + algorithm scoring priorities. Zero infrastructure, manual posting, ~8 min/post vs 45.
  - **Blueprint 02 — Approval Pipeline**: Claude Code generates weekly batches → Telegram bot delivers drafts for one-tap approve/reject → scheduler posts approved content via the X API at optimal times. Requires Telegram bot + X API access (free tier has posting limits).
  - **Blueprint 03 — Autonomous Stack**: three agents (Content / Analytics / Optimization) with a weekly **feedback loop** — the Optimization Agent reads engagement metrics and rewrites the Voice Style Guide with evidence-based changes. Self-improving, requires X API elevated access, risk of voice drift.
- **Hard rules to build into the agent**: no hashtags (a low-effort signal that doesn't aid distribution); enforce topic consistency (agent should *refuse* off-topic posts); post in the engaged-follower window; optimize for dwell time; dedicate ≥1 post/day specifically to the follow_author signal.
- **Hard prohibitions**: never auto-post without a human review gate; never generate engagement bait ("Agree or disagree?", "What do you think?"); never let voice drift toward generic AI tone; never optimize for a single signal at the expense of triggering negatives.
- **Metrics that matter** (track weekly, before the next batch): reply rate, follow rate, **out-of-network impression ratio**, profile-click rate, not-interested/mute rate. The out-of-network ratio is the headline metric — **>40% means the algorithm is actively distributing to new audiences; <20% means reach is almost entirely from existing followers**.

## Notable quotes

> "The algorithm predicts probabilities for 14 actions, then multiplies each by a weight and sums them. Positive actions push your post up. Negative actions push it down. The weights are not public, but the actions are."

> "The Grok-based transformer learns relevance entirely from your engagement history... This means CONSISTENCY OF TOPIC AND STYLE trains the algorithm to show your content to people with matching engagement histories. Inconsistency confuses the model."

> "the algorithm doesn't care how hard you worked on a post / it measures fourteen specific behaviors and scores each one / your agent should know all fourteen"

> "the agent is given a topic, not a pattern." — the thread's diagnosis of *why most AI content sounds like AI content*

> "A personal agent produces your content calibrated to the specific signals the algorithm rewards, in the voice your existing audience has come to recognize."

## Notes

- **Verification caveat (important).** The thread's central empirical claim — that xAI open-sourced the *full* For You feed system at `github.com/xai-org/x-algorithm`, including a "Phoenix" Grok-based ranker, "Thunder" retrieval, and a 14-action scorer — is *not independently verified here*. The historically known public X release was the March 2023 `the-algorithm` repo, which was a partial snapshot, not the live ranking model, and used heavyweight features rather than a pure transformer. The component names (Home Mixer / Thunder / Phoenix / Candidate Pipeline) and the "hand-engineered features eliminated, Grok learns everything" framing may be accurate, embellished, or fabricated. **Treat the specific repo contents as claimed-not-confirmed** until the repo itself is checked. The *content-strategy advice*, by contrast, is largely consistent with widely-reported X-algorithm behavior (replies/reposts/follows weighted above likes; negative signals heavily penalized; first-hour engagement gates reach; hashtags discouraged).
- This is a **Content-OS-shaped source** in the wiki's terms — it sits alongside [[wiki/sources/shannholmberg-content-os]] (Content OS framework) and [[wiki/sources/shannholmberg-hermes-agent-operator]]. Where Shann's stack is platform-agnostic and publish-layer-centric (Postiz), this thread is X-specific and *algorithm-reverse-engineering*-centric. The Voice Style Guide here is the analogue of Shann's brand-foundation document.
- The **three blueprints map cleanly onto the wiki's existing agent-architecture vocabulary**: Blueprint 01 is the [[wiki/concepts/markdown-as-agent-contract]] / `CLAUDE.md`-as-voice-loader pattern; Blueprint 02 adds a Telegram approval gate + [[wiki/concepts/scheduled-automation]]; Blueprint 03 is [[wiki/concepts/multi-agent-orchestration]] with a [[wiki/concepts/self-annealing]]-style feedback loop (Optimization Agent rewrites the directive from observed metrics). The escalation ladder (manual → semi-auto → autonomous) is the same shape as the fleet-level model in [[wiki/sources/shannholmberg-hermes-agent-operator]] and the 14-hour fleet ladder elsewhere.
- The **human-review-gate insistence** is notable and aligns with the wiki's recurring caution: even Blueprint 03 advises a monthly voice-drift review. This is a content-domain instance of human-in-the-loop.
- **Relevance to [[wiki/projects/helm|Helm]]**: Helm's Marketing agent has exactly this problem (generate brand-voiced posts across ROAM products). The 14-signal portfolio framing and the "optimize for a portfolio, never one signal" rule are directly transferable to Helm's voice-profile + posting logic. See [[wiki/syntheses/helm-voice-profiles]].
- The runtime stack named is **Claude Code** (not Hermes), distinguishing this from the Hermes-cluster sources — it's a lighter, terminal-first build rather than a VPS-hosted multi-platform agent.
- The four named optimal-time windows and the ">40% out-of-network ratio = good" threshold are presented as rules of thumb, not derived from the source code; treat as heuristics.

## Mentioned entities

- [[wiki/entities/doublenickk]] — author of the thread; reverse-engineered the X algorithm and built the agent.
- [[wiki/entities/x-ai]] — claimed open-sourcer of the For You feed recommendation system.
- [[wiki/entities/x-corp]] — the platform the agent targets (For You feed, X API, X Analytics).
- [[wiki/entities/grok]] — the transformer model underlying the Phoenix ranker per the thread.
- [[wiki/entities/x-algorithm-repo]] — the claimed open-source repo (`github.com/xai-org/x-algorithm`) with Home Mixer / Thunder / Phoenix / Candidate Pipeline.
- [[wiki/entities/claude-code]] — the runtime for all three blueprints.
- [[wiki/entities/telegram]] — approval-gate delivery channel in Blueprint 02.
- [[wiki/entities/x-api]] — posting + analytics interface in Blueprints 02 and 03.
- [[wiki/entities/github]] — host of the claimed algorithm repo.

## Related concepts

- [[wiki/concepts/recommendation-algorithm]] — the 14-action weighted-sum scoring model is the core object the source explains.
- [[wiki/concepts/voice-style-guide]] — the central artifact the agent runs on; produced by a Pattern Analysis prompt, refreshed weekly.
- [[wiki/concepts/content-os]] — this is an X-specific, algorithm-tuned instance of the Content OS pattern.
- [[wiki/concepts/multi-agent-orchestration]] — Blueprint 03's Content/Analytics/Optimization three-agent system.
- [[wiki/concepts/scheduled-automation]] — Blueprint 02/03 batch generation + scheduled posting at optimal times.
- [[wiki/concepts/self-annealing]] — the Optimization Agent rewriting the Voice Style Guide from real metrics is a content-domain self-annealing loop.
- [[wiki/concepts/markdown-as-agent-contract]] — Blueprint 01's `CLAUDE.md`/`MEMORY.md` loads voice + algorithm context as the agent's contract.
- [[wiki/concepts/human-in-the-loop]] — the non-negotiable review gate before any post is published.

## Related sources

- [[wiki/sources/shannholmberg-content-os]] — sibling Content OS framework; platform-agnostic + Postiz publish layer vs this thread's X-specific algorithm tuning.
- [[wiki/sources/shannholmberg-hermes-agent-operator]] — the escalating manual→semi-auto→autonomous fleet ladder mirrors this thread's three blueprints.
- [[wiki/sources/VadimStrizheus-hermes-10k-clipping]] — commercial content-agent pipeline (generate → Telegram → publish), the Hermes-runtime analogue of Blueprint 02.
- [[wiki/sources/zodchiii-10-claude-code-agents]] — the *job description + trigger + output* agent framing; Content Repurposer is a sibling content agent.
