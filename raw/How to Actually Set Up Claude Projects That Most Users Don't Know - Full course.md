---
title: "How to Actually Set Up Claude Projects That Most Users Don't Know - Full course"
source: "https://x.com/cyrilXBT/status/2074669139730284735"
author:
  - "[[@cyrilXBT]]"
published: 2026-07-08
created: 2026-07-22
description: "Most people use Claude like a search bar.Every session starts the same way. You are a marketing copywriter. My business is this. My audience..."
tags:
  - "clippings"
  - "claude-code"
---
![Image](https://pbs.twimg.com/media/HMpuXhtXEAAVUO3?format=jpg&name=large)

Most people use Claude like a search bar.

Every session starts the same way. You are a marketing copywriter. My business is this. My audience is that. Now write me the thing. Then you close the tab, and tomorrow you do the entire briefing over again from scratch, training the same employee every single morning and letting them forget everything by night.

That is not a workflow. That is starting from zero, forever.

Claude Projects fix this, and almost nobody sets them up correctly. Most people create a project, paste one line of instructions, drop in a random PDF, and wonder why it does not feel dramatically better than a normal chat. The power is real, but it lives in the details that the setup screen does not explain.

This is the full course on setting up Claude Projects the way people who actually rely on them do it. Every feature here is real and current. By the end you will have a project that loads full context into every conversation automatically, never needs re briefing, and produces output that sounds like you instead of like a generic assistant.

## What A Project Actually Is

Strip away the marketing and a Claude Project is three things bundled into one persistent workspace.

Custom instructions. A system level prompt that applies to every conversation inside the project automatically. This is the standing brief that shapes how Claude behaves, who it thinks it is talking to, and what rules it follows, without you typing any of it into the chat.

A knowledge base. Files and documents Claude can reference in every conversation, always available, never needing re upload. Style guides, specs, past work, reference material.

Scoped conversations. All chats inside the project are grouped together and inherit the same instructions and knowledge.

One important thing to understand up front, because it trips people up constantly. Conversations inside a project do NOT share message history with each other. The shared state is the instructions and the files, not the chats. Each new conversation starts fresh with only those two things loaded. This matters for how you design everything below.

Projects are available on every Claude plan, including free, though free users are capped at five projects and project instructions specifically are a paid feature. On Pro, Max, and Team you get the full setup.

## The Mistake Almost Everyone Makes

Before the setup, understand the single biggest error, because avoiding it is most of the battle.

People treat the knowledge base like a storage locker. They dump everything in. The entire brand manual. Six months of meeting notes. A forty page strategy deck. The logic seems sound. More context equals better output.

It does not work that way, and here is why. Project knowledge does not get fully loaded into every response. Claude pulls the most relevant content per query through retrieval. When you overload the knowledge base with loosely related material, you dilute Claude's ability to find the signal that actually matters, and you risk filling the context window with files, leaving less room for the actual conversation.

The rule that produces dramatically better output is the opposite of what people expect. Keep each knowledge document tight and specific, roughly one to three pages. A three page brand voice guide beats a forty page brand manual every single time, because the useful signal is denser and the noise is lower. Precision beats volume in the knowledge base, always.

## Step 1: Create The Project With Real Intent

Open Claude, click Projects in the sidebar, click New project.

The name matters more than it looks. Name it specifically. "Newsletter" or "Client Proposals" or "API Documentation," not "Work" or "Stuff." The reason is that you will end up with multiple projects, and the entire point is separation. A vague name leads to a vague project that slowly accumulates unrelated junk, which is exactly the dilution problem above.

This leads to the first principle most people miss. One project per concern. Do not put your backend code and your marketing content in the same project. Do not mix client A and client B. Separate projects mean cleaner, more focused context, and focused context is the whole reason projects work. The instinct to have one mega project for everything is the instinct to recreate the generic chatbot you were trying to escape.

## Step 2: Write Instructions Like A Standing Brief, Not A Prompt

This is the highest leverage part of the entire setup, and it is where the gap between a weak project and a great one is widest.

A weak instruction block says "You are a helpful assistant that writes marketing content." That gives Claude nothing it did not already have.

A strong instruction block is a complete standing brief written for someone who knows nothing about you yet, because that is exactly the situation at the start of every new conversation in the project. It should cover who you are and what you do, the primary tasks this project exists for, your tone and style preferences, your required output format, the domain knowledge Claude should assume, and critically, the things Claude should never do.

Here is a template structure that works across almost any project type:

ROLE You are \[specific role\] working on \[specific domain\]. You are writing for \[specific audience who knows nothing about them\]. WHAT THIS PROJECT IS FOR The main tasks here are \[task 1\], \[task 2\], \[task 3\]. Assume every request relates to one of these unless told otherwise. HOW TO RESPOND Tone: \[specific\]. Format: \[specific\]. Length: \[specific\]. Do not ask clarifying questions unless genuinely blocked. Make a reasonable assumption, state it, and proceed. WHAT TO ASSUME \[Domain facts, product details, positioning that should be treated as given in every response.\] NEVER \[Specific things Claude should never do in this project: AI cliches, certain claims, certain formats, whatever your hard rules are.\]

That one instruction about not asking clarifying questions is worth calling out. By default, Claude often opens with a round of "before I start, can you tell me more about..." For a project you use daily, that preamble is pure friction. Telling it to make a reasonable assumption, state it, and proceed removes the back and forth and speeds up every single session immediately.

Write these instructions for the reader who has zero history with you, because every new conversation genuinely starts there. The instructions and the files are the only things that carry forward. The memory of your last conversation does not.

## Step 3: Build The Knowledge Base With Precision

Now the files. Remember the rule. Tight, specific, one to three pages each. Here is what actually belongs in a well built knowledge base, using a content project as the example.

A voice and style guide. How you write. Sentence rhythm, words you use, words you ban, the feel of your output.

An audience document. Who you are writing for, what they care about, what they already know, what they are skeptical of.

A pillars or scope document. The specific topics or categories this project covers, so Claude stays in lane.

A small set of best examples. Three to five pieces of your actual best work. This teaches by demonstration far more effectively than description. Claude learns your patterns from real examples better than from any amount of instruction.

Reference material specific to the work. SEO notes, product specs, technical constraints, whatever the domain requires.

Name each file descriptively. "Brand Voice Guide v3," "Q2 Product Roadmap," "API Documentation Payments Module," not "notes" or "stuff." Descriptive names help retrieval surface the right document for the right query, which is the whole mechanism you are relying on.

The limits worth knowing. On Pro, Max, and Team you get up to 20 files per project, 30MB per file, supporting PDF, text, markdown, code files, CSV, and images. That is plenty if you follow the precision rule. If you are hitting the ceiling, the problem is almost always that you are uploading volume instead of signal.

## Step 4: Test Retrieval Before You Trust It

Here is a step almost nobody does, and it separates people who think their project works from people who know it does.

After you upload your knowledge, open a conversation in the project and explicitly test whether Claude can retrieve each document. Ask directly:

Based on the Brand Voice Guide in the project knowledge, how should I approach the opening line of a post? Quote the specific guidance you are using.

If Claude accurately references the document, retrieval is working. If it gives a generic answer or cannot find the guidance, something is wrong. Maybe the file did not process, maybe the naming is too vague, maybe the document is buried under too many others. Better to find that out in a test than to discover three weeks later that Claude was never actually reading your most important file.

Run this test for each critical document. It takes five minutes and it is the difference between a project you hope works and one you know works.

## Step 5: Pick The Right Model Per Conversation

A detail most people miss entirely. Inside a project, you can choose which Claude model to use for each conversation independently. The project does not lock you into one model.

This matters for cost and quality. Use a faster model for routine drafting inside the project, and switch to a more capable model for the conversations that need deep reasoning or complex synthesis. Same project, same instructions, same knowledge, different engine depending on what the specific task needs. Most people never realize they can do this and either overpay by running everything on the top model or underperform by running everything on a fast one.

## Step 6: Use Conversations As Thinking, Not Just Tasks

Here is a habit that quietly makes projects far more powerful over time.

Do not only use project conversations for finished tasks. Use them to think out loud. Work through a problem, explain your reasoning, talk through why you are making a decision. Because the project is scoped and consistent, these thinking conversations help Claude understand your reasoning patterns, not just your output patterns.

The result is that over weeks, Claude inside a well used project starts matching not just your format but your judgment. It suggests approaches that fit how you actually think, because it has seen how you think inside that scoped context, not just what you produce.

## Step 7: Maintain It, Because A Project Is Only As Current As Its Files

A project is not set and forget. It is only as accurate as what is inside it, and outdated knowledge produces confidently wrong context, which is worse than no context.

Build a maintenance habit. When your positioning changes, update the voice guide. When a spec is revised, replace the old one. When a strategy shifts, update the scope document. Review your project instructions quarterly, because instructions written six months ago may now actively contradict what you are doing, and Claude will faithfully follow the outdated rule.

The projects that stay valuable are the ones people keep current. The ones that quietly become useless are the ones that were set up once and never touched again while the real work moved on around them.

## The New Layer: Cowork Projects

Worth knowing, because it extends everything above significantly. As of the 2026 updates, Projects also live inside Claude Cowork, the desktop agentic app, and this version adds capabilities the chat based projects do not have.

Cowork projects add scoped memory that persists between sessions, so you can say "build on last week's report" and Claude knows exactly what that was, without leaking that context into your other work. They add dedicated local folders, so the project reads and writes real files on your machine. And they add scheduled tasks, so a project can run recurring work automatically on a cadence you set.

The setup logic is the same as everything above. Clear instructions, tight relevant files, one project per concern. But the ceiling is higher, because a Cowork project does not just inform conversations, it executes work against real files and can run on a schedule without you. A good first move is pointing it at a folder and saying:

Read every file in this folder. Then summarize what you know about this workspace: what is here, what I probably use it for, and what instructions you will follow. If anything is unclear, ask before assuming.

That single command makes Claude learn the project on day one, and from there it remembers.

## Four Project Templates You Can Build Today

The theory is only useful once it is concrete. Here are four project setups that map directly onto the most common use cases, each with what goes in instructions versus knowledge, so you can copy the structure.

**The Content Project.** Instructions define your role as a writer for a specific audience, your tone, your formatting rules, and your hard bans. Knowledge holds a voice guide, an audience persona, a pillars document, and three to five of your best performing pieces. This is the project that makes everything you publish sound consistently like you instead of like a different writer each time. The best examples in the knowledge base do more work here than any instruction, because voice is caught, not taught.

**The Code Project.** Instructions define your stack, your conventions, your preferred patterns, and the things you never want done. Knowledge holds an architecture document, your key source files, your coding standards, and API documentation for anything the project touches. Point Claude at this and it stops suggesting code that fights your existing patterns and starts matching them. One project per codebase, never a shared one, because mixing two codebases is the fastest way to get suggestions that fit neither.

**The Client Project.** One project per client. Instructions define who the client is, their brand, their preferences, and the scope of your work with them. Knowledge holds their brand guidelines, past deliverables, meeting notes distilled to essentials, and any constraints specific to them. This is how a solo operator or agency keeps every client's context perfectly separated, so client A's voice never bleeds into client B's work.

**The Research Project.** Instructions define what question or domain you are investigating and how you want findings structured. Knowledge holds your source material, your prior notes, and your working thesis. As you feed it more, it builds a picture across everything, and because it is scoped, it does not confuse this research with anything else you are working on. This is the closest a chat based project gets to the second brain concept, a body of knowledge you can interrogate that stays coherent because it is walled off from everything unrelated.

Notice the pattern across all four. Instructions carry the standing rules and the behavior. Knowledge carries the reference material and the examples. The separation is deliberate, and getting the right content into the right layer is most of what makes a project work. A rule about how to behave belongs in instructions. A document Claude needs to reference belongs in knowledge. Mixing those up, putting behavioral rules in a knowledge file or pasting reference docs into the instruction box, is a quiet way to make a project underperform without an obvious reason why.

## The Layered Personalization Most People Miss

One more thing worth knowing, because it stacks on top of everything above. Project instructions are not the only personalization layer Claude has, and understanding how they combine gives you finer control.

There are three layers, and they all apply at once on every response. Account wide instructions, set in your profile settings, apply to every chat everywhere regardless of project. Project instructions apply only inside a specific project. And styles, set per chat, tune tone and format for that one conversation.

The practical move is to use each for what it is best at. Put the rules that apply to everything you do with Claude, like your general communication preferences, in the account wide profile instructions, so you do not repeat them in every project. Put project specific context and rules in the project instructions. Use styles for one off adjustments when a particular conversation needs a different tone than the project default.

Most people cram everything into one layer and lose this control. When you separate them correctly, you stop repeating your universal preferences in every single project, and each project's instructions stay focused purely on what makes that project different. That focus is, once again, the entire theme of setting projects up well.

## The Setup That Actually Compounds

Put the whole thing together and here is what a properly built project gives you that a normal chat never will.

Every conversation starts with full context already loaded. Your voice, your audience, your rules, your reference material, all present before you type a word. You stop re briefing. You stop starting from zero. You stop training the same employee every morning.

The output stops sounding generic and starts sounding like you, because Claude is working from your actual examples and your actual standards, not a blank slate plus a rushed one line prompt.

And it compounds. Week one needs small corrections as Claude learns your patterns from the files. By week three, it is matching your approach closely enough that you stop explaining things you used to explain every time. The thirty minutes of setup pays back over months.

Here is the honest bottom line. Most people never get this benefit, not because the feature is hard, but because they set it up in ninety seconds and never did the parts that actually matter. The precise knowledge base. The real standing brief. The retrieval test. The maintenance habit.

Do those four things and Claude Projects stop being a folder for your chats and become the difference between using Claude as a search bar and running it as a system that already knows exactly who you are and what you need.

Set up one project properly this week. Pick the work you do most. Write the real instructions. Upload three tight documents. Test retrieval. Then watch how different the next conversation feels.

Follow [@cyrilXBT](https://x.com/@cyrilXBT) for the full builds, the exact instruction templates, and the project setups I use every day.