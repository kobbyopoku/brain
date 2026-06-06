---
type: source
title: av1dlive — How to Build a Voice Agent using AI (Full Guide)
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/Av1dlive/status/2056412170402091070
source_type: x-thread
author: av1dlive (@Av1dlive)
source_date: 2026-05-18
raw_path: raw/How to Build a Voice Agent using AI (Full Guide).md
content_status: substantive-verbatim
tags: [voice-agent, real-time, latency-budget, rag, conversation-design, function-calling, state-machine, guardrails, evaluation, stt, tts]
---

# av1dlive — How to Build a Voice Agent using AI (Full Guide)

> ~6,000-word build log distilling three months and four rewrites of production voice agents into a system thesis: a voice agent is a **real-time audio system** (five components inside a sub-700ms budget), not a chatbot with a microphone — and the hard parts are *wiring* and *conversation design*, not model quality.

## TL;DR

av1dlive argues voice agents "don't need the best model" — they need a real-time pipeline with a hard latency budget, five components wired in the right order, RAG grounding strong enough to keep the model honest, and a weekly review loop that compounds. The piece walks the five-component chained pipeline (STT → RAG → LLM → TTS → functions), a 700ms latency budget split per component, the Salesforce VoiceAgentRAG dual-agent cache pattern, conversation-design rules for writing-for-ears, two-checkpoint safety guards, and a four-layer evaluation framework. The author ships a companion Claude skill file at `github.com/codejunkie99/voice-agent-builder`. The article was edited by Minimax M2.7 and Claude Opus 4.7.

## Key takeaways

- **A voice agent is a real-time audio system, not a TTS-wrapped chatbot.** Five components coordinate inside a 300-800ms window; building it the "chatbot way" (STT completes → LLM → TTS → play) "felt awful, like talking to a kiosk." Humans converse in overlapping streams, not turns.
- **Three architectures, pick by control needed.** *Chained pipeline* (separate STT/LLM/TTS, ~600-700ms, most controllable/debuggable) → *half-cascade* (audio into multimodal model, TTS still specialized, 300-500ms) → *native speech-to-speech* (one model audio-in/audio-out, 200-300ms). Recommendation: **start chained**, move to speech-to-speech once the product is proven.
- **Speech-to-speech fails on complex state.** It excelled at booking flows but "fell apart on a 12-step intake form" by turn nine from context bloat; moving to a chained pipeline with a real state-machine layer lifted completion from 61% to 89% in three days. **Tool scoping per state was the entire fix.**
- **The five components**: the *ears* (streaming STT), the *brain* (LLM), the *knowledge* (RAG), the *mouth* (TTS), the *hands* (functions/integrations).
- **STT is the most consequential component** — a transcription error cascades through everything below. Target 6-8% WER on production audio (past 12% frustrates); **built-in end-of-turn detection is "the single biggest UX upgrade of 2026"** (semantic, not acoustic-silence; drops the pre-speech pause 200-400ms per turn).
- **Use the small fast model, not the flagship.** Frontier reasoning models take ~1500ms to first word = dead air; escalate to the big model only for specific complex tool calls. **Cap the system prompt at 800 tokens** — it reloads every turn.
- **The signature production failure: the LLM narrates an action instead of calling the function.** "I've confirmed your booking" — nothing was called. Fix: **scope tools to the current state; the state machine is the safety rail, not the system prompt.**
- **The latency budget is ~700ms total**, split per-component (transport / STT / end-of-turn / RAG / LLM TTFT / TTS time-to-first-audio / network). Fast lane ≈ 440ms, slow lane ≈ 700-900ms. The two biggest 2026 unlocks: model-integrated end-of-turn detection and speculative-prefetch dual-agent cache.
- **Dual-agent RAG cache** (from Salesforce AI Research's *VoiceAgentRAG* paper, March 2026): a background "Slow Thinker" predicts 3-5 likely follow-up questions and pre-fetches chunks *while the user listens*; a foreground "Fast Talker" checks the in-memory cache first (sub-ms vs ~110ms vector DB call). Paper benchmark: **75% cache hit rate, 316× retrieval speedup on hits, 16s saved across 200 queries.** Principle: *"use the user's listening time as your computation time."*
- **Conversation design is writing for ears, not eyes**: short sentences (8-10s attention span), never two questions per turn, acknowledgment phrases to fill silence, mirror the caller's exact words, no markdown in prompts, spell out numbers ("nine four one zero seven"). Three-act structure: acknowledgment/orientation → resolution → confirmation/close.
- **Safety is two checkpoints, not one.** *Input guard* (prompt injection, PII redaction, topic blocklist) before the LLM; *output guard* (over-promise language, factual claims not in retrieved context, moderation) before TTS speaks. There is no "read before sending" moment in voice. The hallucination check catches ~70% of confabulated answers in the author's deployment.
- **One hardcoded escalation phrase**, ALL CAPS in the system prompt: *"I want to make sure I give you accurate information. Let me connect you with someone who can help."* Never let the LLM improvise the refusal.
- **Four-layer evaluation framework**: infrastructure (WER, p50/p95/p99 latency) → execution (task success, tool-call accuracy, groundedness; LLM-as-judge on a small model, four yes/no questions) → user behavior (barge-in recovery, reprompt rate) → business outcome (containment rate is the primary optimization target). Build a 50-conversation test set before launch (40% happy / 30% edge / 15% error / 10% adversarial / 5% acoustic).
- **The weekly review loop**: every Monday, 30 min — pull metrics, sample 20 calls (7 escalated / 7 resolved / 6 random), read transcripts, name the single most common failure, make **one** change, A/B test 48h, ship the winner.
- **Grounding is a trust system, not just an accuracy feature.** A confident wrong answer makes a caller feel deceived. Four parts: source-of-truth ("ANSWER ONLY FROM THE CONTEXT PROVIDED" in caps), graceful refusal (one hardcoded phrase), confidence-aware response (BM25 score thresholds: >0.6 confident, 0.3-0.6 hedge with "I think", <0.3 transfer), knowledge-base hygiene (Friday audit of the bottom 5% confidence responses).
- **Six named failure modes**: VAD in the pipeline instead of the transport; tools available in the wrong state; function handlers that throw without calling the result callback; validating user data in the prompt instead of in code ("the LLM is not a parser. Python is a parser."); unbounded context growth over a long call; TTS reading codes/IDs literally (fix: NATO phonetic + SSML break tags).
- **Pipeline timeline**: first agent took a weekend; the production system took ten weeks and four rewrites; "it has been getting better every day since, without me touching it."

## Notable quotes

> "A voice agent that cannot be interrupted is not a voice agent. It is voicemail."

> "use the user's listening time as your computation time. The moment they start hearing the current response is the moment you start preparing for their next question."

> "The state machine is the safety rail, not the system prompt."

> "The LLM is not a parser. Python is a parser. Use Python."

> "Voice agents look like AI. They run like real-time systems. Teams that ship treat them that way. Teams that ship six months late think a better prompt fixes a system problem."

## Notes

- **This is the wiki's first end-to-end voice-agent build source.** It complements the wiki's text-agent material ([[wiki/concepts/agentic-loop]], [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]]) by adding the *real-time/latency-constrained* dimension absent from text-agent sources. The latency budget and "use listening time as computation time" framing have no prior analogue in the wiki.
- **Strong convergence with [[wiki/sources/akshay_pachaar-x-rag-wrong]] and [[wiki/concepts/retrieval-augmented-generation]]** on grounding-as-trust. Both treat RAG not as a retrieval-tuning problem but as a correctness/trust discipline. The dual-agent cache (VoiceAgentRAG) is a *latency*-motivated RAG variant; Blockify is a *chunk-quality*-motivated one — orthogonal but compatible.
- **"Scope tools per state" restates [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]]'s "model as reasoning engine, not execution engine"** in voice terms. The narrate-instead-of-call failure is a concrete instance of the tool-reliability gap that source theorizes. The state machine here functions as a tool-scoping mechanism.
- **The "use the small fast model, not the flagship" rule is voice-specific cost/latency discipline** that echoes the cost-discipline aesthetic in [[wiki/sources/zodchiii-x-claude-code-settings]] and [[wiki/sources/Mnilax-430-hours-claude-code-waste]] (small prompts, scoped tools, explicit budgets) — here driven by time-to-first-token rather than token cost.
- **The weekly review loop + turn-log replay** is a [[wiki/concepts/self-annealing]]-adjacent compounding pattern: a structured log replayed against current config, one change per week, A/B tested. It is self-improvement via human-in-the-loop discipline rather than agent-internal state.
- **Relevance to the wiki owner**: voice agents are directly buildable as [[wiki/concepts/ai-automation-services]] deliverables (the booking/intake/CRM use cases named are SMB-shaped) and intersect [[wiki/projects/vedge|Vedge]]'s healthcare domain (the 12-step *intake form* and *patient* examples are clinical-adjacent). The two-checkpoint safety model and PII-redaction input guard are notably relevant to PHI-bearing voice deployments.
- **Uncertainty / verify-before-citing**: several factual claims are time-stamped and specific but unverified by the wiki — *GPT-Realtime-2 shipped May 7 2026*, *Salesforce AI Research VoiceAgentRAG paper March 1 2026*, *Deepgram Flux GA same week*, and the *316× / 75% / 16s* benchmark numbers. These are the author's claims, not independently confirmed. The author discloses the piece was research-assisted (Perplexity, Claude, ChatGPT) and AI-edited (Minimax M2.7, Claude Opus 4.7), so figures should be treated as cited-from-source, not established fact.
- **Companion artifact**: the author ships a Claude skill file at `github.com/codejunkie99/voice-agent-builder` to paste the full article to an agent — an instance of the [[wiki/concepts/markdown-as-agent-contract]] / skill-pack pattern (article-as-skill).

## Mentioned entities

- [[wiki/entities/av1dlive]] — author of the voice-agent build guide (@Av1dlive).
- [[wiki/entities/openai]] — shipped GPT-Realtime-2 (May 7 2026 per source); native speech-to-speech model lab.
- [[wiki/entities/gpt-realtime-2]] — OpenAI's native realtime voice model cited as a 2026 enabling release.
- [[wiki/entities/salesforce-ai-research]] — published the VoiceAgentRAG paper (March 2026); source of the dual-agent cache pattern.
- [[wiki/entities/voiceagentrag]] — Salesforce paper introducing speculative-prefetch dual-agent RAG cache; benchmark source.
- [[wiki/entities/deepgram]] — streaming STT provider; Deepgram Flux moved beta→GA (cited).
- [[wiki/entities/deepgram-flux]] — Deepgram's streaming STT with built-in end-of-turn detection.
- [[wiki/entities/bland]] — voice/phone-call API for agents; pipeline-host candidate (existing wiki stub).
- [[wiki/entities/twilio]] — voice + SMS transport layer; pipeline-host candidate (existing wiki stub).
- [[wiki/entities/minimax]] — Minimax M2.7 listed as a copy-editor of the article.
- [[wiki/entities/anthropic]] — Claude Opus 4.7 listed as a copy-editor; Claude used in research.
- [[wiki/entities/perplexity-ai]] — Perplexity used in the author's deep research.

## Related concepts

- [[wiki/concepts/voice-agent]] — this source is the wiki's canonical definition: real-time five-component audio system inside a latency budget.
- [[wiki/concepts/latency-budget]] — the ~700ms end-to-end budget split per component; the organizing constraint of voice agents.
- [[wiki/concepts/conversation-design]] — writing-for-ears discipline; three-act structure; mirroring; spell-out-numbers.
- [[wiki/concepts/retrieval-augmented-generation]] — treated as grounding-as-trust; dual-agent cache is a latency-motivated RAG variant.
- [[wiki/concepts/dual-agent-rag-cache]] — VoiceAgentRAG's Slow-Thinker/Fast-Talker speculative prefetch pattern.
- [[wiki/concepts/function-calling]] — define-describe-decide; the narrate-instead-of-call failure mode.
- [[wiki/concepts/state-machine]] — per-state tool scoping as the safety rail; "the state machine is the safety rail, not the system prompt."
- [[wiki/concepts/agent-guardrails]] — two-checkpoint safety (input guard + output guard); escalation phrase.
- [[wiki/concepts/agent-evals]] — four-layer framework + 50-conversation test set + weekly review loop + LLM-as-judge.
- [[wiki/concepts/reasoning-execution-split]] — "the LLM is not a parser; Python is"; validate in code, not the prompt.
- [[wiki/concepts/ai-automation-services]] — voice agents (booking/intake/CRM) as a sellable AI-services deliverable.

## Related sources

- [[wiki/sources/akshay_pachaar-x-rag-wrong]] — companion RAG-as-correctness thesis; chunk-quality variant vs this source's latency-cache variant.
- [[wiki/sources/NainsiDwiv50980-tool-calling-roadmap]] — tool-calling reliability roadmap; the narrate-instead-of-call failure is its theory made concrete in voice.
- [[wiki/sources/hooeem-build-an-ai-agent-today]] — foundational agent-build course; this source adds the real-time/latency dimension.
- [[wiki/sources/zodchiii-x-claude-code-settings]] — shared small-model/small-prompt cost-discipline aesthetic.
