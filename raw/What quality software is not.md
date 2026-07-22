---
title: "What quality software is not"
source: "https://x.com/saameeey/status/2079647206865248709"
author:
  - "[[@saameeey]]"
published: 2026-07-21
created: 2026-07-22
description: "I read @almonk’s article, Quality Software, and agreed with all of it. He describes what quality software looks like. I kept thinking about ..."
tags:
  - "clippings"
  - "software-craft"
---
I read [@almonk’s](https://x.com/@almonk) article, [Quality Software](https://x.com/almonk/status/2079461952577802549), and agreed with all of it. He describes what quality software looks like. I kept thinking about the inverse: what quality software is not.

LLMs and coding agents have changed how software gets made. You can describe an app, watch the files appear, and have a working version before lunch. I use these tools every day, and I am glad more people can now build software.

I learned to build software before LLMs started writing code. And please, do not let anyone rewrite history: I wrote bad code. I built broken interfaces and chose abstractions I would not use today. Writing every line myself did not give me taste.

What helped was everything surrounding the code.

I had to understand what the user needed before I started building. I tested my assumptions and reviewed changes before release. When something failed, I had to find the cause. After release, I maintained what I shipped.

That is where taste came from for me.

You stay with software long enough to see what happens after release. Over time, you begin to notice weak requirements, fragile code, and risky changes before they reach users.

A [study comparing novice and expert programmers](https://www.sciencedirect.com/science/article/abs/pii/S0020737383710849) found that experts connected code to program goals and recognized recurring patterns more clearly than novices.

AI can now handle much of the implementation. The discipline surrounding that implementation still has to be practised.

So, what is quality software not?

**Quality software is not software that works once.**

An app opening on your laptop proves that one case worked. Users will click things in another order, submit invalid information, retry requests, or lose their connection halfway through. The software must tell them what happened and help them continue.

**Quality software is not a good demo.**

A demo uses data you prepared and services you expect to respond. Production has old records, duplicate requests, missing permissions, and dependencies that time out. Quality software handles those cases without losing data or leaving the user confused.

**Quality software is not sophisticated code.**

An advanced pattern still has to earn its place. It should solve the requirement and leave the code understandable for the next developer. Taste is knowing when another layer removes a real problem and when it only creates more work.

**Quality software is not a passing test suite.**

Tests tell you whether the behaviour you checked still works. They do not tell you whether you understood the requirement or tested the failure the user will encounter. A green test suite is evidence. It is not permission to stop thinking.

**Shipping quickly does not prove quality.**

Speed tells you how quickly the change reached users. The team still has to review it before release, monitor it afterwards, and keep a reliable way to reverse it when it fails.

Define the requirement. Use AI for the implementation. Test the expected behaviour and likely failures. Review what changed. Monitor the product after release. Keep a rollback available.

Doing that repeatedly develops the judgement to know whether the software is ready for someone else to depend on.