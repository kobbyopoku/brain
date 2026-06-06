---
type: concept
title: Function calling
created: 2026-06-06
updated: 2026-06-06
aliases: [tool calling, tool use, function-calling]
tags: [ai-agents, llm, tools, voice-agents]
---

# Function calling

> The mechanism by which an LLM matches a user's natural-language intent to a defined function and invokes it, rather than following a hardcoded conditional tree.

## Definition

**Function calling** lets an LLM map natural-language intent directly to a registered function and call it, with no conditional branching written by the developer. [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] characterizes it as a "define-describe-decide" flow: the developer defines the function, describes it, and the model decides when to call it.

## Why it matters

In voice agents, function calling is where reliability most often breaks: the model may *narrate* an action instead of *performing* it. Getting the invocation contract right — scoping which tools are available and handling errors — is what separates a demo from a deployable agent ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Treatment across sources

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]] frames it as define-describe-decide (the LLM matches intent to a function from natural language, with no conditional tree). It names the signature voice failure: the LLM narrates the action ("I've confirmed your booking") instead of calling the function. The fix is per-state tool scoping plus try/except handlers that always return a result.

## Sub-claims and details

- **Define-describe-decide**: the developer defines and describes a function; the model decides when to invoke it ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Signature failure mode**: the LLM narrates the action ("I've confirmed your booking") instead of actually calling the function ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Fix — per-state tool scoping**: limit which functions are callable in each state of the agent ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).
- **Fix — defensive handlers**: wrap tool calls in try/except handlers that always return a result ([[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]).

## Open questions and contradictions

- None recorded yet.

## Related concepts

- [[state-machine]] — per-state tool scoping uses the state machine to constrain which functions are callable.
- [[agent-guardrails]] — output guards catch over-promise narration that masks a missed function call.

## Mentioned in

- [[wiki/sources/av1dlive-build-a-voice-agent-full-guide]]
