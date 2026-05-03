---
title: "AGENTIC WORKFLOWS: Build & Sell AI Automations (2026)"
source: https://www.youtube.com/watch?v=MxyRjL7NG18
author: Nick Saraev
channel: https://www.youtube.com/@nicksaraev
published: 2026
created: 2026-05-03
duration_minutes: 342
transcript_segments: 10974
description: "Definitive 5+ hour guide on agentic workflows for business. Coins the DO framework (Directives + Executions). Argues agentic workflows are 'one of the largest wealth transfers in human history' via horizontal leverage. Transcript captured via youtube-transcript-api on 2026-05-03."
tags: [clippings, video, youtube, agentic-workflows, ai-automation, do-framework]
---

# AGENTIC WORKFLOWS: Build & Sell AI Automations (2026)

By Nick Saraev. Source: https://www.youtube.com/watch?v=MxyRjL7NG18

Full transcript with timestamps below. 10,974 snippets, ~342 minutes.

---

[000:00] Hey, welcome to the definitive guide on
[000:01] agentic workflows for business. Now,
[000:03] agentic workflows have the potential to
[000:05] bring about what I think is one of the
[000:06] largest wealth transfers in human
[000:08] history. But very few people are
[000:09] currently talking about how to
[000:10] practically use them to improve their
[000:12] financial means. That's what this video
[000:14] is going to show you how to do. Here's
[000:15] what you're going to learn. What an
[000:16] agentic workflow really is. How agentic
[000:19] workflows function via loops. A few
[000:21] common problems with agentic workflows
[000:22] and how to fix them. How to actually
[000:24] build these things. So, idees, setting
[000:26] up your workspace, creating your first
[000:28] flow, the DO framework, directive
[000:30] orchestration and execution, claude
[000:32] skills, MCP and other frameworks, what
[000:35] each one does, when to use which and how
[000:36] they all fit together, how to test and
[000:38] validate agentic workflows, the best
[000:40] system prompts for agentic workflows,
[000:42] which I will give you, how to make your
[000:44] workflows self annealing, aka heal
[000:46] themselves when they air out, how to
[000:47] move out of the IDE and into the cloud.
[000:49] I'll teach you how to create web hooks,
[000:50] schedule triggers, and more. How to run
[000:52] multiple agents simultaneously. I'll
[000:54] show you a sub aents and advanced
[000:56] workflow parallelization. And finally,
[000:58] how to troubleshoot agentic workflows
[001:00] when things break. If you don't know who
[001:01] I am, I build two AI based service
[001:03] agencies to $160,000 a month in combined
[001:06] revenue. I've also consulted for a
[001:07] couple of billion-dollar businesses with
[001:09] AI. And I tell you this cuz I want to
[001:10] make it clear. Well, you guys are of
[001:12] course going to learn everything from
[001:13] the fundamentals all the way up to the
[001:14] advanced concepts today. This course has
[001:16] a business focus. My goal is to help
[001:18] prepare as many people as possible for
[001:19] what I consider to be the next stage of
[001:21] the economy. So what you will learn
[001:22] today is working right now. It is
[001:24] generating revenue right now and you can
[001:26] use it to improve your own and other
[001:28] people's businesses right now. Please
[001:29] bookmark this and use the chapter
[001:31] feature to come back to it or whenever
[001:32] you need anytime. And I hope you guys
[001:34] are excited as I am to get into Agentic
[001:36] Workflows. Let's get started. This is a
[001:38] practical course. The whole point of it
[001:40] is to build and then use Agentic
[001:43] Workflows in real business environments.
[001:46] And that's because building is the most
[001:47] effective way to learn anything. When
[001:49] you build with your hands and get them
[001:51] dirty, you're forced to deal with
[001:53] concepts in a way that you guys never
[001:54] would have if you just sat back and
[001:56] passively listened. That said, before we
[001:59] get into the building, and there will be
[002:01] a lot of building and a lot of demos in
[002:02] this course, there are some foundational
[002:04] things about agents and workflows that
[002:06] I'd highly recommend that you understand
[002:09] because if you don't understand them,
[002:10] you're going to commit many hours to
[002:11] this course and you'll only really be
[002:13] able to digest or extract a few
[002:15] percentage points of it. So what I want
[002:17] to do is I want to maximize the ability
[002:19] and efficiency of your time by helping
[002:21] you cover those concepts now. And by
[002:23] doing that, you'll be able to absorb the
[002:25] rest of the course a lot faster and a
[002:27] lot better. So what do I mean by
[002:29] concepts? AI is currently in an overhang
[002:32] state. Current AI capabilities are very
[002:35] far beyond what most people believe,
[002:37] expect, or know how to use. If you guys
[002:40] graft this, what we have down here is
[002:43] sort of like the general public's
[002:45] perception of AI, okay? And their
[002:47] ability to use it. And what we have
[002:50] above it is sort of like the reality,
[002:54] okay? You guys are going to see a lot of
[002:56] very crappily drawn lines in this
[002:58] course, so you might as well get used to
[002:59] them now. So this gap between the
[003:02] reality of the situation and then what
[003:04] people believe AI is capable of is
[003:07] called the overhang.
[003:10] The reason why this overhang exists and
[003:12] the reason why people are only squeezing
[003:13] out a very small percentage of the
[003:15] actual value of AI, large language
[003:17] models, agentic workflows and so on and
[003:19] so forth [snorts] is because right now
[003:21] most people are using them as glorified
[003:23] copy and paste tools. They are basically
[003:25] trying to drink through the Pacific or
[003:27] Atlantic Ocean with a tiny straw. You
[003:30] know, they ask these galaxy brain
[003:32] intelligences. Pretty dumb questions to
[003:34] begin with to be honest. They answer and
[003:36] then all they do is they copy it from
[003:38] one tab into another, which is obviously
[003:40] a very low bandwidth, really
[003:42] bottlenecked way of working. They are
[003:44] not integrating AI into their business
[003:46] like I'm about to show you how to do in
[003:48] this course. Instead, they're just
[003:50] dealing with it like a like an external
[003:52] sort of third party thing.
[003:54] Now, obviously, people are figuring out
[003:56] that AI is a lot more powerful than most
[003:58] people give it credit to, and courses
[004:00] like mine are helping them do so. But as
[004:02] they figure it out, the arbitrage window
[004:04] will close. And in case you guys didn't
[004:06] know, arbitrage is your ability to
[004:08] essentially produce some sort of
[004:10] beneficial outcome, revenue or profit,
[004:12] based off of a disparity in knowledge.
[004:15] And so, if you know, you know, this and
[004:18] the rest of the market knows this,
[004:21] obviously there's kind of a gap there,
[004:22] right? and the market is willing to pay
[004:24] you to be somebody that solves that
[004:26] little tiny gap. Well, that window is
[004:28] closing because people are learning
[004:30] about how this technology works. But
[004:32] right now, it's wide open and you can
[004:34] make a ton of money with it. So, just as
[004:35] a demonstration to show you how powerful
[004:37] these models are, I'm going to have one
[004:39] in particular called Claude Opus 4.5 do
[004:42] a pretty straightforward task for me.
[004:44] This task is to compile a list of five
[004:46] local meal preparation companies that
[004:47] deliver to around my area and then find
[004:49] their email addresses. I'm then going to
[004:51] send each of them emails with
[004:52] specifications from this email. I want
[004:54] uh you know 3500 calories a day, 200
[004:56] grams of protein a day. I'm doing some
[004:58] big bulk. Do this entirely autonomously
[005:00] requiring no input from me. If you
[005:01] cannot find the emails of at least five,
[005:03] then keep on searching until you do.
[005:05] Most people don't realize that models
[005:06] are entirely capable of doing this sort
[005:08] of thing for you and essentially acting
[005:09] as you know an extension of yourself. So
[005:11] it's starting off by searching for meal
[005:13] prep delivery companies downtown
[005:14] Vancouver BC 2025. If I were doing this
[005:16] on my own, this is probably something
[005:18] that I would do as well, right? like
[005:19] very straightforward and logical. You
[005:21] don't need to know how the IDE that I'm
[005:23] using uh works. You don't need to
[005:25] understand the interface or everything.
[005:26] I'm going to cover all this later on in
[005:28] the course. And as you can see, it's
[005:30] found me a bunch of meal preparation
[005:32] services. There's Fresh Prep, Two Guys
[005:34] with Knives, Crave Healthy, Fed, Fresh
[005:37] in Your Fridge, K-Bop, and then WellFed.
[005:39] Now, it's finding email addresses of
[005:41] each of these. So, as you can see, it's
[005:42] actually simultaneously running a bunch
[005:44] of searches on their websites to look
[005:46] for email addresses or contact methods.
[005:48] A few seconds later, it looks like it
[005:50] could only find one email out of the
[005:52] four or five searches that it ran. So,
[005:53] what is it doing instead? It's now
[005:55] broadening its search. It's going on
[005:56] contact pages. It's looking for
[005:58] alternative solutions. Okay, it's now
[006:00] accumulated the email addresses and like
[006:01] a temporary database. And it's just
[006:03] going through and sending emails. It
[006:05] does so through uh what's called an MCP,
[006:07] model contact protocol server that I've
[006:08] set up. I'll show that to you later. And
[006:10] boom. Now, it is done. So, we've sent
[006:12] five emails. Down here, you can see it
[006:14] said, "I asked each company about custom
[006:16] meal plans, pricing for higher volume
[006:18] orders, and their delivery schedule to
[006:19] downtown Vancouver." We also included
[006:21] the requirements. I went through and I
[006:23] actually found the email that it sent.
[006:24] It was something like this. Hey, company
[006:27] team, I'm looking for a meal prep
[006:29] service that delivers to downtown
[006:30] Vancouver and that contains the
[006:32] following requirements. Daily calories
[006:34] approximately 3500. Daily protein
[006:36] approximately this much. Focus on whole
[006:38] foods and healthy ingredients.
[006:39] Interested in learning more? Do you mind
[006:41] letting me know? you know, if you guys
[006:42] offer custom meal plans, um, what your
[006:45] pricing looks like and how your delivery
[006:47] schedule works. Looking forward to
[006:48] hearing from you. Thank you very much.
[006:50] So, I mean, like, this is something I
[006:51] realistically probably would have sent
[006:53] myself. Um, is it in my exact tone of
[006:55] voice, honestly? Like, it's really
[006:56] close. This is more or less everything
[006:58] that I would send. There's no AI isms.
[007:00] People on the other end of the line
[007:01] aren't going to know that I'm using AI
[007:02] to do this sort of thing. And it turned
[007:03] a process that realistically would have
[007:05] previously taken me maybe like 20
[007:06] minutes into something that took me
[007:08] literally less than 15 seconds. I mean,
[007:10] I wrote the thing, I pressed enter, and
[007:12] then I went. And what you'll see is with
[007:14] the use of other bandwidth improving
[007:16] tools like voice transcription and stuff
[007:17] like this, you can actually have agentic
[007:20] workflows become more or less your
[007:22] interface for the internet. And I should
[007:24] note that I didn't even use a defined
[007:25] agentic workflow for this. I literally
[007:26] just asked an agent to do something and
[007:28] it was super unstructured and it still
[007:29] did a great job. Imagine when we wrap
[007:31] this in the framework. I also want to
[007:33] cover this idea of a river of value. The
[007:35] way I see the global economy is as a
[007:38] giant river. Okay. Now, capital flows to
[007:42] whoever provides value. And essentially
[007:44] what occurs is for many centuries that
[007:46] value has come from human labor,
[007:48] primarily physical to start, although
[007:50] eventually cognitive. And then the more
[007:53] value that people could produce, the
[007:55] more downstream little tributaries of
[007:57] this river we found. And so this might
[007:59] be some person that's producing
[008:01] tremendous value, these might be other
[008:03] people and so on and so forth. The whole
[008:05] idea of capital is that as solutions
[008:08] arrive in the economy that are more and
[008:10] more effective, [gasps] they produce
[008:12] larger diversions of this stream. Okay?
[008:16] And so let's say this person Z is using
[008:19] agentic workflows. The idea is over the
[008:21] course of the next few years, he or she
[008:23] is going to consume more and more and
[008:25] more and more and more of that river
[008:27] until essentially he's getting all of
[008:30] it. Those who position themselves as
[008:32] people like Z in this case will capture
[008:35] massive flows from the future economy
[008:37] because agentic workflows aren't
[008:39] optional. There's something that are
[008:40] coming and being deployed right now. The
[008:43] last thing I want to talk about is
[008:44] automation in the terms of a Gentic
[008:47] workflow. Now, a lot of people that
[008:49] watch my channel and are probably here
[008:51] are familiar with the idea of
[008:52] automation. They're also familiar with
[008:54] the idea of roles and they've heard a
[008:57] lot of things about how AI agents are
[008:59] coming and their whole fleets of teams
[009:01] that are being replaced and so on and so
[009:03] forth. And this is kind of inaccurate.
[009:06] Rather than thinking about agentic
[009:07] workflows, which is what we're going to
[009:08] cover in this course, as being able to
[009:10] automate 100% of one role, I want you to
[009:14] think about it a little differently. I
[009:15] want you to think about agentic
[009:16] workflows as being capable of automating
[009:18] 90% of 10,000 roles. So as opposed to
[009:22] automating 100% okay of one, we're
[009:27] automating say 90% of 10,000 people in
[009:31] the organization. Now if you automate
[009:33] 100% of one role, that's actually pretty
[009:35] valuable. Don't get me wrong. If I could
[009:36] automate a software developer completely
[009:38] end to end, if I could automate a
[009:40] marketer end to end, obviously that
[009:41] produces some value in my organization.
[009:43] But agentic workflows, like a lot of
[009:45] technology, have gaps. And so, um, the
[009:48] main issue is human beings tend to
[009:49] always have a little bit more context
[009:51] than these things do, at least right
[009:53] now. And so, even the ability to
[009:55] automate 90% of 10,000, despite the fact
[009:57] that it's not 100, is still tremendously
[009:59] valuable. If you just do the math,
[010:01] automating 100% of one person's role is
[010:03] equivalent to basically providing one
[010:05] unit of economic value. Whereas, if you
[010:07] automate 90% of 10,000 people's, you're
[010:09] providing 9,000 units of economic value.
[010:12] As long as you structure your companies
[010:13] in a way to accommodate these things,
[010:15] these things are very powerful. Now, I
[010:17] call this horizontal leverage and it's
[010:19] very, very strong. Another way I want
[010:21] you to think about this is like the
[010:23] industrial revolution. Back in the good
[010:25] old days, well, I don't know if they
[010:27] were really good, but certainly back in
[010:28] the day, you had people like
[010:30] seamstresses who would, you know, knit
[010:32] various garments and stitch various
[010:34] things together. And maybe one of these
[010:36] seamstresses could produce, you know, 10
[010:38] pairs of a specific type of clothing per
[010:41] day. Well, after the industrial
[010:43] revolution, obviously we didn't do a lot
[010:44] of this stuff by hand anymore. We had
[010:46] machines that did this stuff instead. So
[010:48] maybe a loom. Before a single seamstress
[010:51] could produce maybe 10 garments a day.
[010:53] After one of these machines could maybe
[010:55] prepare 10,000 garments in a day. That
[010:58] said, it the machine didn't fully
[011:00] replace that seamstress because that
[011:02] seamstress just transitioned. Instead of
[011:04] being somebody that worked with their
[011:05] hands on building the garment directly,
[011:08] they instead became somebody that was
[011:10] supervising whole fleets of machines
[011:11] that did it. Now imagine if in this
[011:14] analogy, not only can we build and use a
[011:16] loom, we are capable of rebuilding that
[011:18] loom in any configuration in seconds. We
[011:21] don't have to, you know, smelt the metal
[011:23] and then hammer it and then construct it
[011:26] in a way and screw gears and all that
[011:28] stuff in order to build a machine. We
[011:30] could literally just use natural
[011:32] language. Obviously, that would be a lot
[011:34] more powerful, right? Well, that really
[011:35] is the idea of an agentic workflow. It
[011:38] is something that provides incredible
[011:39] horizontal leverage and we can
[011:41] reconfigure it in seconds to do more or
[011:43] less whatever we want. And it's not an
[011:45] exaggeration to tell you that this is a
[011:47] phase change essentially in a company's
[011:50] ability to automate things. So if you
[011:53] guys are familiar with automation
[011:54] platforms, in this case this is N8N,
[011:57] you'll know that most of the time the
[011:59] way that we are currently building
[012:00] automated systems is through drag and
[012:03] drop nodes or modules. And so on the
[012:05] left hand side here, I have a simple
[012:07] system set up. I'm not going to go
[012:08] through everything because it's
[012:09] pointless. The point is not to learn a
[012:11] specific automation platform. The point
[012:12] is to learn how to automate platforms in
[012:14] general, but I have a specific
[012:15] automation here that just responds to
[012:17] some emails coming in for a cold email
[012:19] campaign. And as you see here, we have
[012:21] these nodes and they do various things.
[012:23] Some of them do HTTP requests. Some of
[012:24] them do some data processing and and
[012:26] formatting. Some of them call a Google
[012:28] sheet. We have some AI functionality and
[012:30] so on and so forth. They're all
[012:31] connected with these lines, which is
[012:33] basically the the flow of logic through
[012:35] a system. And this is hunky dory. It
[012:37] works really well. Well, the new version
[012:40] of that workflow on the left, which
[012:42] obviously requires a lot of time,
[012:45] energy, and understanding in order to be
[012:46] able to to parse and then change is what
[012:49] we have on the right. Instead of dealing
[012:51] with nodes and specific software
[012:53] platforms, we use the universal
[012:56] translation, which is natural language,
[012:58] and then just write it out in bullet
[013:00] points. So on the right hand side I have
[013:02] the exact same workflow except I have it
[013:04] set for agentic uh systems and all it is
[013:08] is a list of bullet points. Hey when
[013:10] somebody replies to one of your cold
[013:11] outreach campaigns instantly should send
[013:12] a web hook. The system should look up
[013:14] the campaign in a Google sheet to find
[013:16] talking points and example replies. It
[013:18] should then research the person who
[013:19] replied. It should then generate a short
[013:21] friendly reply. If they said something
[013:23] negative like unsubscribe or remove me,
[013:24] we should skip them. If there's no
[013:26] knowledge base, we should skip them.
[013:27] Otherwise, we should send the reply
[013:29] automatically. I want you guys to see
[013:31] that on the left hand side, we had to
[013:33] spend months, maybe years, becoming
[013:34] skilled enough to use a platform to be
[013:36] able to build systems that did this. And
[013:38] on the right, a toddler who has a a
[013:41] rough idea in mind of what he or she
[013:43] wants to do can write it out in natural
[013:44] language. And not only can everybody
[013:46] else on a team interpret that, we can
[013:48] also change that at any point. If I
[013:50] wanted to add an additional step to my
[013:51] workflow, all I do is I click click on
[013:54] this, press enter, and then just write
[013:55] it out. and the agentic workflow builder
[013:57] and then eventually doer using a
[013:59] framework I'm going to run you guys
[014:00] through later on in this course will do
[014:02] it and it'll do it extraordinarily
[014:03] remarkably well. So that's a very
[014:05] fundamental change in how these things
[014:07] work and hopefully it's clear to
[014:08] everybody here that workflows are no
[014:10] longer drag and drop sort of builds in
[014:13] the concept that we see on the left hand
[014:15] side. They're very much so just like
[014:17] basic logic. So why is all of this stuff
[014:20] possible right now? It certainly wasn't
[014:22] just a little while ago. Well, there are
[014:24] three main reasons. intelligence, tools,
[014:27] and cost. On the intelligence side,
[014:30] model intelligence just crossed a
[014:32] threshold and became very, very good,
[014:34] seemingly overnight, but really we've
[014:36] been working up to it for quite a while.
[014:38] Frontier models like Anthropics Claude,
[014:40] OpenAs, Chat, GBT, Google's Gemini, and
[014:42] then a bunch of other ones have gotten
[014:44] really smart. They score around 80% on a
[014:48] benchmark called software engineering
[014:49] bench verified. And this measures real
[014:51] software engineering ability. This is
[014:53] not a crappy cherrypicked demo. It
[014:56] wasn't included in like the training
[014:58] data or anything like that. These are
[015:00] novel problems that are being solved in
[015:01] novel ways through models. And
[015:03] essentially, they are genuine
[015:04] professional grade work that are better
[015:07] than most software engineers. Now, I
[015:09] would have considered myself a software
[015:11] engineer a couple of years ago. I'd say
[015:12] my skills have definitely uh
[015:14] deteriorated a fair amount since because
[015:16] I've been focusing more on no code tools
[015:17] and and making money and stuff like
[015:18] that. But this stuff is so far beyond my
[015:21] own abilities as sort of like a
[015:23] mid-level dev u that it's not even
[015:25] funny. Most people that learn about this
[015:27] and they're going to be learning about
[015:28] it pretty soon will think that AI went
[015:30] from, you know, intern level to some
[015:32] sort of senior employee overnight. But
[015:34] this is just how knowledge works.
[015:37] Basically, anytime that you have a
[015:39] process and that process slowly gets
[015:41] better and better and better over time,
[015:42] most people don't see until we hit a
[015:45] certain threshold and then it almost
[015:47] looks like it went vertical. In reality,
[015:49] uh it's almost like the way that boiling
[015:51] water works, right? The temperature of
[015:53] water goes up and up and up and up and
[015:54] up and then eventually it boils and then
[015:56] it fundamentally changes state. You
[015:58] know, it goes from over here where it's
[016:00] like a liquid to over here where it's a
[016:02] a gas. And although we're supplying more
[016:05] and more energy to this thing, we're not
[016:07] really seeing it change until all of a
[016:08] sudden, boom, it's producing bubbles and
[016:10] getting all over the place. So, I see
[016:12] model intelligence a very, very similar
[016:14] way. So, a lot of people talk about
[016:16] benchmarks. Very few people actually
[016:18] show what the questions inside of a
[016:20] benchmark realistically ask. I think
[016:22] benchmarks are for the most part pretty
[016:23] artificial. A much better test of how
[016:26] good a model is is just how good you
[016:27] feel while using it. But it is important
[016:29] that at least we understand how
[016:31] benchmarks work in order for us to
[016:32] really put in context the capabilities
[016:34] of agents. So here's uh one from
[016:36] Astropi. It's a misleading exception
[016:39] message. And basically, these models are
[016:41] so good at coding. Like, like, I mean, I
[016:43] tried to look through and understand
[016:44] what any of these actual questions meant
[016:46] and how to fix them. I'd probably be
[016:48] staring at each of these for like a day
[016:50] before anything makes sense. Um, let
[016:52] alone before I get to the point where I
[016:53] could realistically solve it. These
[016:55] models can do this sort of thing in in
[016:56] seconds. So, issue problem statement.
[016:58] Hey, removing a required column from a
[017:00] time series raises a misleading error
[017:01] message. The error claims the time
[017:03] column is missing even when it's
[017:04] present. Instead, the error should list
[017:06] all missing required columns. Then it
[017:08] gives you a snippet of code with the
[017:09] actual class time series. Right? So
[017:11] looking at that, no idea what the hell
[017:13] that does. The bug, if flux is missing,
[017:15] error still complains about time. Error
[017:17] message is factually incorrect. You're
[017:18] fix detect which required columns are
[017:20] missing. Report them explicitly. So you
[017:22] actually have to go through and you have
[017:23] to do this with the code. Okay, here's
[017:25] one from sort of like a Panda style
[017:27] question. Load CSV silently coerces
[017:30] mixtype columns instead of failing
[017:31] quickly which leads to incorrect
[017:32] downstream computations and then it like
[017:34] provides a list. So, we now have models
[017:36] that are basically capable of looking at
[017:38] a thousand of these and solving more
[017:42] than 800 of them perfectly. I mean, if
[017:45] you gave me a thousand of these, not
[017:46] only would I take like a year, I would
[017:49] probably get at least, you know, 50% of
[017:51] these things wrong. And I'm somebody
[017:53] that has some exposure to this sort of
[017:54] stuff. Imagine the average person. And
[017:57] so what I mean to say is that we are
[017:58] essentially empowering every human being
[018:01] on earth or at least we have the
[018:03] potential to empower if we were to
[018:04] actually distribute this technology and
[018:06] if everybody were to know it to the
[018:08] level that you will know it by the end
[018:09] of this course with the powers of like a
[018:11] mid-level to even senior developer in
[018:14] many cases. Another important point is
[018:16] how fast these models can operate. I
[018:19] mean this is me asking chat GPT 5.2
[018:21] thinking to just reason a little bit
[018:22] about the meaning of life. Check out the
[018:24] stream of output that it's providing.
[018:26] But you can go way faster than that.
[018:28] This is an example of a diffusion LLM
[018:30] that it basically immediately processes
[018:32] and writes I don't know how many hundred
[018:34] words, but extraordinarily quickly. You
[018:36] see that we just click generate and then
[018:37] immediately after, you know, probably at
[018:40] least 300 words for instantiated. These
[018:42] models can run these reasoning loops
[018:44] extremely quickly behind closed doors.
[018:46] In addition, providers like uh Anthropic
[018:48] and OpenAI and Gemini and stuff have all
[018:50] the compute necessary to run these
[018:51] things like 10, 50, 100 times faster
[018:54] than you are yourself. So just imagine
[018:56] what's going to happen when that level
[018:58] of technology drips down to the rest of
[019:00] the economy. Like to be clear, these
[019:02] models, the ones that I'm using to build
[019:03] agentic workflows, are already extremely
[019:05] powerful and have automated the vast
[019:07] majority of my day-to-day work. They can
[019:09] automate the vast majority of your
[019:10] day-to-day work as well or any of the
[019:12] companies that you work with. But
[019:13] imagine the models in 3 months. Imagine
[019:15] the models in a year from now. That's
[019:17] why learning how to build these sorts of
[019:19] workflows today is probably one of the
[019:20] highest ROI skills that you can engage
[019:22] in. The second thing is tool integration
[019:25] is now standardized. So there's some
[019:26] protocols out there like model context
[019:28] protocol which standardizes how AI
[019:31] connects to external tools, databases,
[019:33] resources, and stuff like that. I'm
[019:34] going to be showing you guys how to use
[019:36] model context protocol in pretty
[019:37] advanced ways that I don't think a lot
[019:38] of other people have covered in this
[019:40] course. I'm also going to be talking
[019:41] about some of the downsides of model
[019:43] context protocol like how initially it
[019:45] totally blew but now it's uh actually
[019:47] pretty good and well supported so it's
[019:48] it's worth us diving in. In addition to
[019:51] you know those tools through MCP there
[019:53] also some frameworks that have recently
[019:55] come out. One is directive orchestration
[019:57] execution. This is the framework I'm
[019:59] going to be using to build and then use
[020:00] our agentic workflows throughout the
[020:02] course. There are also platform specific
[020:04] frameworks like cloud skills for the
[020:05] cloud family of models. these formalize
[020:08] tool calling and you know in case you
[020:10] have no idea what I'm talking about here
[020:11] LLM are really flexible okay which is a
[020:13] great thing conceptually it's great if
[020:15] you want to write poems and write do
[020:16] creative writing and help you respond to
[020:18] emails and stuff like that but a lot of
[020:20] business functions don't depend on
[020:22] flexibility what they depend on is the
[020:24] opposite they depend on reliability so
[020:27] in business we need to standardize and
[020:29] tools are basically just standardized
[020:31] little things that we can use in order
[020:32] to accomplish business tasks I like
[020:35] thinking of it like a caveman that you
[020:36] know, is hunting saber-tooth tigers or
[020:38] something. If you're a caveman and
[020:40] you're hunting saber-tooth tigers, and
[020:42] every time you go to a saber-tooth
[020:43] tiger, you're completely empty-handed,
[020:45] what are you going to do? The first
[020:46] thing you're going to do is you're going
[020:47] to be like, "Holy crap, is that a
[020:48] saber-tooth tiger?" You're going to
[020:49] scrge around on the ground to look for
[020:51] rocks and pointy stabby things and, you
[020:53] know, sticks and anything that can buy
[020:55] you some distance and then maybe some
[020:56] effectiveness. Contrast that with if
[020:59] before you had a little bit of foresight
[021:01] and you said, "Hm, I should probably
[021:02] build something that's kind of pointy
[021:04] and sharp." Huh? So, you you work all
[021:06] day and night and you put together a
[021:07] spear. Well, every time you encounter
[021:09] that problem of the saber-tooth tiger,
[021:11] okay, what are you going to do? You're
[021:12] just going to pick up your spear and
[021:13] deal with it. Just my really crappy
[021:16] drawn spear. That's sort of the same
[021:17] thing that LLMs use tools for. They
[021:20] encounter problems. When they encounter
[021:22] them a few times, they then develop
[021:24] tools that solve them or use
[021:25] pre-existing ones through MCP. And then
[021:27] in doing so, we can standardize the
[021:29] solving of business problems pretty
[021:30] easily.
[021:32] Okay. The last thing is just cost
[021:33] economics and they finally make sense.
[021:36] When Claude Opus 4.5 dropped, it went
[021:38] from a cost of about $15 or $75
[021:41] depending on input or output per 1
[021:43] million tokens to five or $25 depending
[021:46] on input or output for 1 million tokens.
[021:48] That's a 3x reduction. And newer models
[021:50] are even cheaper than that. The cost of
[021:52] intelligence per like effectiveness has
[021:54] plunged something like 40% in the last
[021:56] year. If I were to graph this, it would
[021:58] actually look like this. Now, I've been
[022:00] using models since GPT3, way back in
[022:02] 2020 when it was um initially released
[022:05] with a very small, you know, select
[022:07] group of people that could access it and
[022:08] so on and so forth. GPT3, which is, I
[022:12] mean, orders upon orders upon orders of
[022:14] magnitude dumber than this, costs more
[022:17] than this technology that we are dealing
[022:18] with right now. It is insane how quickly
[022:21] the price of knowledge work has
[022:22] plummeted. It's already gone down 40
[022:25] times in just the last year. I imagine
[022:26] it'll probably go down another 40 times
[022:28] over the course of the next year, maybe
[022:29] even more. What that means is we can
[022:32] actually send large volumes of tokens to
[022:33] these things to replace the work of like
[022:36] deterministic um old school automations
[022:38] like the NAN flow that I showed you
[022:40] without it running a business ragged
[022:41] into the ground. There are also tons of
[022:43] price wars that are occurring between
[022:45] major providers and there's a lot of
[022:46] like geopolitical incentives between,
[022:48] you know, places in the east and then
[022:49] places in the west um to basically make
[022:51] these things as accessible and easily to
[022:53] use as possible. So to make a long story
[022:55] short, this is new. Very few people
[022:58] understand the capabilities right now.
[023:00] So there are many billions of dollars
[023:02] that will shift as the market learns and
[023:03] adapts. It is much better to be an early
[023:06] mover than somebody that is affected by
[023:08] this technology uh without their consent
[023:10] or knowingness. What I mean is would you
[023:13] rather learn about this stuff now or
[023:14] would you rather learn about it in 2
[023:16] years when your boss or I don't know
[023:18] some some client base of yours turns to
[023:20] you and says hey we no longer need you
[023:21] because we have aic workflows to do it.
[023:23] I would much rather be the person that
[023:25] helps them build those agentic workflows
[023:27] than I'd be the person that's now
[023:28] sitting on my ass because I don't know
[023:30] anything about them. Hopefully, you are
[023:31] too. Okay, so now that that big
[023:33] preamble's out of the way, let's learn
[023:34] about chat bots, agents, agentic
[023:36] workflows, uh, knowledge tools, and then
[023:38] actually get our hands dirty with some
[023:40] demos. I like thinking about knowledge
[023:41] tools as evolving over the course of the
[023:44] last 30, 40 or 50 years. I always think
[023:47] about it sort of like the step ladder on
[023:49] the right where you have three rungs. At
[023:52] the bottom you have documents. In the
[023:54] middle you have chats and at the top you
[023:58] have agents. Over the course of the last
[024:00] 30 40 50 years we basically transition
[024:02] from knowledge in the form of docs to
[024:05] knowledge in the form of chats over the
[024:06] last 5 years to knowledge and action in
[024:08] the form of agents. And I'm going to run
[024:10] you through what each of these look like
[024:11] now before actually using them in a real
[024:13] workflow. So documents are static
[024:15] knowledge. Hopefully they're pretty
[024:16] straightforward. It's oneway information
[024:18] flow. All you do is you read the
[024:20] document, but it's not like the document
[024:22] can respond to you. We currently use
[024:24] documents everywhere in school and in
[024:25] business. We use them in legal
[024:26] agreements. We use them in training
[024:28] materials. Once you write a document, it
[024:29] obviously stays fixed. That's a feature,
[024:31] not a bug, because it's great for
[024:33] permanence. Like if you're writing
[024:34] contracts or standard operating
[024:36] procedures that are immutable, aka it
[024:38] should not change. You don't want your
[024:39] contract or your standard operating
[024:41] procedure rewriting itself unless you
[024:42] want it to, right? In most cases, you
[024:44] don't. So, u that's great. That's
[024:45] actually a feature, not a bug. Chat
[024:47] bots, on the other hand, are not static.
[024:48] They are dynamic. Chat bots were
[024:50] developed realistically way back in the
[024:52] 1970s, but we were only starting to use
[024:54] them for real knowledge purposes and
[024:56] maybe like the early 2020s. And they
[024:58] perform two-way interaction. You read
[025:00] the output, but you can also ask
[025:02] questions back. So, here's a crappy pass
[025:04] to GPT40 where I just said, "Hey, what's
[025:07] up? Hey, Nick. All good on my end. Quick
[025:08] check-in. Zero fluff. I'm ready to help
[025:10] if you want to chat. If you got a
[025:11] decision to make, whatever. What's on
[025:12] your mind?" This is now two-way
[025:14] knowledge interaction. the dreaded
[025:16] mdash. Um, this allows you to do things
[025:18] like clarify confusing points. You can
[025:20] ask for research. You can dig deeper
[025:22] into topics. You can also modify the
[025:24] knowledge. So, you could upload, you
[025:25] know, a PDF or you could make some
[025:26] statement and then the chatbot now has
[025:28] some additional context. Uh, I just
[025:30] think of it like really smart colleagues
[025:32] who read everything you give them, but
[025:33] then they're also confined to a chair.
[025:35] You know, they can't move and they can't
[025:36] do anything with it. So, essentially all
[025:37] you can do is is talk. This is how most
[025:40] people treat models today as chat bots.
[025:42] They're dynamic knowledge, but they're
[025:43] still subject to this little window.
[025:45] They can only be communicated with and
[025:47] copied and pasted through your chatgbt
[025:49] or through your cloud output. Now,
[025:50] contrast that with agents, which I
[025:52] consider to be dynamic action. To make a
[025:54] long story short, this is two-way
[025:56] interaction, just like chat bots, except
[025:57] this time it acts. On the right hand
[025:59] side here, you can see I have a flow
[026:01] that says run the thumbnail generator on
[026:02] a link. So, it's not just asking it a
[026:05] question about the thumbnail generator,
[026:06] and I'm actually having it do something.
[026:07] And this is a real agentic workflow that
[026:09] I developed to basically build YouTube
[026:10] thumbnails like what you guys saw on my
[026:12] channel. What we see here is a
[026:14] fundamentally different interface. On
[026:15] the left hand side, we have some of
[026:17] these nodes. Green ones here are actions
[026:19] that are being taken. These gray little
[026:21] sections over here are thinking nodes,
[026:23] which are where the model reasons um
[026:25] extemporaneously, basically temporarily,
[026:27] and then discards these reasoning
[026:28] tokens. You can see that it's actually
[026:30] calling a script. You don't need to know
[026:31] Python in order to like have the model
[026:33] do really cool things for you, but
[026:34] that's what's happening right here. And
[026:35] then down over here we have a bash
[026:36] output where it's actually ran. We have
[026:38] an output that we can then use and so on
[026:40] and so forth. So you're given visibility
[026:42] into the reasoning. You're also given
[026:43] visibility into the um planning tool
[026:46] memory reasoning and then observation
[026:48] loop. And I'm going to cover exactly
[026:50] what that looks like in a moment. You
[026:52] also have autonomy, long execution
[026:53] times. Agents can routinely run for 5 or
[026:55] 10 minutes. Now yesterday night I
[026:57] actually had an agent run for over 5
[026:58] hours uninterrupted to build me a really
[027:00] cool system. As of today I think of
[027:02] models like a mid-tier developer.
[027:04] They're 100K a year or so in terms of
[027:06] their like capability. But if you think
[027:07] about it, I'm spending 20 bucks a month
[027:10] for this, which is 240 bucks a year,
[027:12] which is over 400 times cheaper. And not
[027:14] only is it cheaper, this thing works 24
[027:16] hours a day, as I mentioned, or it can
[027:17] work 24 hours a day. You can do a lot of
[027:19] really cool things with models like
[027:20] this. So now is the time to jump on it.
[027:22] A point to understand is that an agent
[027:24] is not a chatbot, despite the fact that
[027:25] they look really similar, right? Now,
[027:27] the way I see chat bots is like a chat
[027:29] is just an interface, right? It's just
[027:31] some specific thing with messages that
[027:33] go back and forth and then a little
[027:34] window down here where you can enter in
[027:36] your own information. The chat is just
[027:38] like the app. The agent is what lives
[027:40] inside of the app. If you guys are
[027:42] familiar with crustaceians or crabs or
[027:44] um I don't know, like cute little things
[027:46] that crawl around on the ocean subfloor.
[027:48] They often will have fine shells and
[027:51] then um discard them when they no longer
[027:53] fit their purpose. Right? So, like a
[027:55] crustation that uses the shell of an
[027:57] older animal, an agent is just currently
[027:59] using the interface of an older type of
[028:01] knowledge tool, the chatbot. And I'm
[028:03] sure over the course of the next few
[028:04] years, it's going to discard this and
[028:05] we're going to have new interfaces that
[028:06] are even better. Okay, so let me show
[028:07] you guys just the difference between
[028:09] chat bots and then a really low-level
[028:10] agentic workflow that I put together
[028:12] that functions through an agent. Um,
[028:13] down over here is a chat GPT desktop
[028:15] app. This is really simple and easy. You
[028:17] can download it on chatbt's website.
[028:18] Super straightforward. I'm just going to
[028:20] say um hey, how can I scrape, you know,
[028:23] leads from LinkedIn Sales Navigator. So,
[028:27] when you're working with models like
[028:28] this, the input and output is pretty
[028:30] bounded, right? All you can really do is
[028:32] you could just see what this model tells
[028:34] us. Hey, you know, here's the direct
[028:36] high IQ zero fluff rundown. Use this,
[028:39] scrape this,
[028:42] use this. This is cool, right? I mean,
[028:44] it's nice that we're getting information
[028:45] on how to do this. And you know a few
[028:46] years ago this would have been
[028:47] revolutionary. Rather than just have a
[028:49] conversation with the model and ask it
[028:50] how to do things which is knowledge. I
[028:52] can actually force a model to action
[028:54] using agentic workflows. So in this case
[028:56] I'm saying scrape me 200 HVAC owners in
[028:58] the US. I want decision makers. It then
[029:01] checks to see if there are lead scraping
[029:02] directives and execution scripts. This
[029:04] is just part of the framework that helps
[029:06] constrain the model's output which I've
[029:08] run you guys through a little bit more
[029:09] later. It's then going through and
[029:11] actually pulling a script together to do
[029:13] this thing for me. It then comes up with
[029:15] this idea of a test scrape, 25 leads.
[029:17] It's then going to verify some industry
[029:19] match, run the full scrape, upload to
[029:21] Google sheet, and then even go through
[029:22] and enrich it for me. In this case, the
[029:24] model is performing a search. It's then
[029:26] comparing the results of the search with
[029:27] what it is that it thinks that I want.
[029:29] It's determining that there's a very low
[029:31] match rate. And so, it's now adjusting
[029:32] its filters on the fly completely on its
[029:35] own to find leads with zero input. All
[029:38] I'm doing here is texting a friend of
[029:39] mine on my phone.
[029:42] It's then verified, past threshold. Now
[029:44] it's running a full scrape. It then went
[029:46] and it actually got us a Google sheet
[029:47] with all that information. I mean, it's
[029:49] pretty cool in so far that it's totally
[029:50] autonomous. It probably would have taken
[029:52] me a fair amount of time to come up with
[029:53] the filters and so on and so forth
[029:54] myself. This thing just did it entirely
[029:55] on its own. If you guys check the bottom
[029:57] right, we actually ended up getting
[029:58] almost 200 emails directly from this. We
[030:00] also got a bunch of phone numbers and a
[030:01] bunch of other really personal
[030:02] information. So, what exactly is going
[030:04] on? There are five steps that an agent
[030:05] will follow every single time you send
[030:07] or receive a message. The first is
[030:09] planning. The next is tools. The third
[030:10] is memory. The fourth is reflection. And
[030:12] the fifth is orchestration. I think I
[030:14] called it observation before. My bad on
[030:16] that. But orchestration. I use a simple
[030:18] fiveletter acronym for this. Just pt
[030:20] mro. Helps me remember it. Hopefully
[030:21] it'll help you remember it as well. Now
[030:23] these five components are as follows.
[030:25] Planning is where you break down
[030:26] objectives into executable steps. Tools
[030:28] are the actions that an agent actually
[030:30] takes in the world. If you guys
[030:31] remember, it was calling various things
[030:33] to do what it needed to do. They then
[030:35] stored things into memory. So this is
[030:37] how agents retain and recall information
[030:39] across tasks. There different forms of
[030:41] memory. There's short-term, midterm,
[030:42] long-term, and there's different ways
[030:44] that that works within an agent these
[030:46] days. I'm I'm going to cover each of
[030:47] them. Uh reflection is where the agent
[030:49] evaluates and corrects its own work. So,
[030:51] as you saw there, we had an issue with
[030:52] one of the calls and it went through and
[030:54] it fixed the filter. And then finally,
[030:56] orchestration, which is where you
[030:57] coordinate multiple agents or complex
[030:59] workflows. We're going to talk about how
[031:00] to do that um later on in the program,
[031:02] too. Obviously, there's planning, and
[031:04] that's mostly goal decomposition. So,
[031:05] it's where a highle objective gets
[031:07] broken into subtasks. Um, for instance,
[031:09] if your highle task is to eat at White
[031:11] Castle, you know, it's not just eat at
[031:13] White Castle, right? That's not enough
[031:15] to go and actually do the thing. What
[031:17] you want to do is you want to break that
[031:18] down into various tasks. Like maybe step
[031:21] one is we have to um, I don't know, get
[031:23] in the car, right? Step two is, and
[031:26] maybe you do this while you're in the
[031:27] car, you do this before, you got to
[031:29] research the um, GPS location. You know,
[031:32] the third is you have to drive all the
[031:34] way over there.
[031:36] And then the fourth is you actually have
[031:37] to order. And the fifth is you have to
[031:40] make a movie about it. Just kidding. But
[031:42] um the point that I'm making is you know
[031:43] you take this high level task and you
[031:44] actually break it down. And that is
[031:46] occurring every single time within an
[031:47] agent. You don't always see it because
[031:49] it's typically buried within reasoning
[031:51] and most people don't expose reasoning.
[031:52] But this form of highle goal
[031:54] decomposition occurs all the time. And
[031:56] it's important that it does it right
[031:57] because if it screws up at the planning
[031:59] stages, probability of it being able to
[032:01] move and do the rest of the task is very
[032:03] low because it's making a foundational
[032:04] misassion. Now, an agent will identify
[032:06] dependencies within steps. It'll then
[032:08] sequence them logically, like I just
[032:09] gave you, five steps. Well, the agent
[032:11] will actually reverse those steps as
[032:12] necessary. And then good planning also
[032:14] means revising the plan when things
[032:15] change because there's obviously only so
[032:17] much information that we have ahead of
[032:18] time. There are limitations to this and
[032:20] Claude, GPT, Gemini, these have pretty
[032:23] imperfect planning capabilities. So, as
[032:25] part of the building of the workflows
[032:26] that I'm going to show you later, I
[032:28] actually recommend doing a fair amount
[032:29] of the planning yourself. The reason why
[032:31] is because it's sort of um like an
[032:33] analogy where if I'm on I don't know
[032:36] let's say the east coast of the United
[032:37] States and I want to go somewhere on the
[032:39] west coast of Africa or something like
[032:41] that. Okay, and I'm this ship over here
[032:43] and my goal is I want to make it to this
[032:45] port right over here. If I screw up at
[032:48] the very beginning, okay, even by a few
[032:51] percentage points, let's say, okay, and
[032:53] I give myself a range of possible
[032:55] outcomes here, this range, even if it's
[032:57] like a 1% problem with the planning or
[032:59] 1% error or something like that, these
[033:01] ranges have massive downstream impacts
[033:04] over the course of the entirety of the
[033:05] task. Like, if I'm really really bad, I
[033:08] could end up in the middle of freaking
[033:09] nowhere. Or if I'm really, really,
[033:10] really bad on this end, I could end up,
[033:12] you know, hundreds of kilometers, maybe
[033:13] thousands of kilometers away from where
[033:15] I wanted to go. So what planning really
[033:17] is if you think about it is effective
[033:19] planning just reduces those error bars.
[033:21] It just allows us to go a lot tighter
[033:23] and a lot narrower. So the probability
[033:25] of us actually achieving uh the thing we
[033:27] want aka going to where we want to go is
[033:29] a lot higher. If there was one place for
[033:31] you to exert your human intellect, it's
[033:33] at the planning stage. And I'll cover
[033:34] some practical ways to do that later. Um
[033:36] obviously there's DO which helps by
[033:38] providing structured directives. I'm
[033:40] going to show you guys how you can just
[033:41] dump your company SOPs into a model to
[033:42] guide its planning. If you guys don't
[033:44] have company SOPs, I'm going to show you
[033:45] how to reproduce them really simply and
[033:46] easily. Next are tools. Now, these turn
[033:48] LLMs into systems that are capable of
[033:50] real world action. Um, I think I covered
[033:52] the caveman analogy, ancient people
[033:54] building a spear or something like that,
[033:56] but you can also think of it as like an
[033:57] ancient person building a house. It's
[033:59] like they will build the house the first
[034:00] time and the house will be pretty cool,
[034:02] you know, might um have most the things
[034:03] that they want. I don't know, some sort
[034:05] of um straw roof or whatever. And then
[034:07] what's really cool is agents can then go
[034:09] back to the tools and then make them
[034:10] better. So maybe, you know, you want to
[034:11] build a window or something like that.
[034:13] So the first iteration of the house
[034:14] doesn't have a window. Second one has a
[034:15] window. The third one has like a door.
[034:17] The fourth one has like a cool barbed
[034:19] wire security system and so on and so
[034:21] forth. But just to break it down, tool
[034:22] use is where agents interact with
[034:24] systems and services. In our case,
[034:27] because we are dealing mostly with
[034:28] digital services, that means things like
[034:30] calling APIs. Okay, that's a big chunk
[034:32] of tool use to be honest. Then executing
[034:34] code. You don't need to know any of the
[034:35] code. It does the coding for you, but it
[034:37] is still executing the code. It also
[034:39] nowadays includes a lot of database
[034:40] stuff because you don't want to store
[034:42] all the information directly in the uh
[034:44] context of the model. Then it also means
[034:45] things like browsing the web. So if your
[034:48] computer was the entire world, right, in
[034:50] your case, the tool that you personally
[034:52] use to interact with your computer, if
[034:54] you think about it, is use your mouse
[034:55] and use the keyboard. And some people
[034:57] are now using voice transcription tools
[034:59] like myself. So that is our input method
[035:01] to our world of the computer, right?
[035:04] Well, it's the same thing with agents.
[035:05] Tools are their input methods to real
[035:08] life. They need tools in order to break
[035:10] out of that little chatbot, okay, and
[035:12] actually influence things that matter.
[035:14] So the entirety of the intelligence of
[035:16] models in the do directive orchestration
[035:19] execution framework in cloud skills in a
[035:22] bunch of these different ways of
[035:23] thinking about agentic workflows, the
[035:25] entire point of the intelligence is just
[035:26] to help it use and then build tools. And
[035:29] a good analogy is tools are like the
[035:31] agents hands. The LLM is the brain. If
[035:33] you're a brain and you're in a vat or in
[035:34] a jar somewhere, obviously your ability
[035:36] to influence the real world is pretty
[035:37] limited, right? But you give a brain
[035:39] some wires and neurons and some hands or
[035:41] whatever and now it can actually start
[035:42] doing things. Unfortunately, right now
[035:44] tool quality varies a ton. There is a
[035:46] lot of variance in like really good and
[035:48] really crappy tools. And just a few
[035:50] months ago is actually way larger.
[035:51] There's way more variance, but we're
[035:52] getting better. And I imagine future
[035:54] tool systems are going to be mostly
[035:56] pretty solid. There's going to be a lot
[035:57] less uh uh range between like a really
[035:59] good tool and a really bad tool.
[036:01] Essentially, um, this is for a variety
[036:04] of reasons. MCP came out pretty
[036:05] recently, and there are also a lot of
[036:07] people trying to capitalize short-term
[036:09] on MCP, so they're building a lot of
[036:11] really crappy tools. I'll show you guys
[036:12] how to avoid that, and also how to
[036:13] select like really high quality tools
[036:14] that matter, as well as how to build
[036:16] your own that are way better. The way I
[036:18] see bad tools is it's like if you give
[036:19] somebody a really crappy hammer and then
[036:21] you expect them to build you like a
[036:22] really nice uh cupboard or cabinet or
[036:24] something, probability is low, right? If
[036:26] you want to build something really cool,
[036:27] you need to have cool tools. If you want
[036:29] to do something really cool, you
[036:30] obviously need to make sure those tools
[036:31] are as high quality as humanly possible.
[036:34] So, here's one of the key insights of
[036:35] Agentic Workflows and one of the reasons
[036:36] why I think a lot of people don't
[036:37] understand how the stuff works. When you
[036:39] standardize tools, okay, and you turn
[036:41] them from vague ideas into actual
[036:44] concrete functions. You let anybody use
[036:48] them, regardless of the type of model
[036:50] that you're using, whether it's Claude
[036:51] or whether it's chat GBT or whether it's
[036:53] Gemini. All of these models are smart
[036:55] enough to know how to use the tool. You
[036:57] also ensure consistent inputs and
[036:58] outputs, which is really, really
[037:00] important for business. And the cool
[037:01] thing is you don't actually need to wait
[037:02] for other people to build them anymore.
[037:04] All of these models are hyper optimized
[037:06] for programming. So, we're just going to
[037:08] let the model build its own tools. LLMs
[037:11] are very probabilistic, right? Their
[037:13] decision-m process is pretty opaque to
[037:15] us. I heard a great quote the other day,
[037:17] uh, might have been from Dario Amod,
[037:18] might have been from somebody else, but
[037:19] it was that AI models are grown. They're
[037:22] not built. And I think about that pretty
[037:24] often. AI models are just intelligences
[037:26] that we are slowly figuring out how uh
[037:28] they work under the hood. We don't
[037:30] actually know. We don't have an an
[037:31] established consistent decision-making
[037:33] process that takes us from one to
[037:35] wherever we want to go. Business
[037:37] requires that you need interpretability.
[037:39] You need the ability to audit things and
[037:40] so on and so forth. Okay? So rather than
[037:42] have this big probabilistic galaxy brain
[037:44] which makes decisions in routes in ways
[037:46] that we have no idea how, okay, we just
[037:48] give it very very simple tools. And in
[037:53] that way, even if there's some
[037:54] deviation, maybe it gets all kind of uh
[037:57] loopy over here, we know that it called
[037:59] a tool. And because it called a tool, we
[038:01] can obviously interpret that um a lot a
[038:03] lot easier, right? We have a sequence of
[038:05] steps like 1 2 3 4 5 6. We go through
[038:09] the process. It's just way more
[038:10] straightforward. So, we just let an
[038:12] agent, which is optimized for coding,
[038:13] make its own tools. Then the agent will
[038:16] call the tools and then interact with
[038:17] life for us. I want to show you guys how
[038:19] easy it is to build your own tools. So
[038:21] here I have a simple query. Hey, how
[038:22] would you build a workflow that takes a
[038:24] video, cuts out the silences in said
[038:26] video, and stitches it all back together
[038:28] to deliver me the results. The cut
[038:29] should look natural like most YouTube
[038:31] junk cuts. Basically just try and stitch
[038:32] the empty space together. You know, this
[038:34] is a pretty complicated flow if you
[038:36] think about it. There are a lot of
[038:37] different ways you could build something
[038:38] like this and none of them are basically
[038:40] easy. So, what this is going to do is
[038:41] it's going to look for a couple of
[038:43] simple and easy ways to do this and then
[038:45] present them to me because I went down
[038:47] here and I selected plan mode, which is
[038:48] one of the different modes that you can
[038:49] use in um at least the Claude series of
[038:51] models. Keep in mind depending on the
[038:53] models that you're using may be a little
[038:54] bit different. So now once I have this
[038:56] plan in front of me, I'm then going to
[038:58] be able to decide on how to do the
[038:59] workflow and then I could act as more or
[039:01] less a highle director letting this
[039:03] thing know whether or not I want to do
[039:04] something. Okay, next up it's asking me
[039:06] are we doing this on short clips, long
[039:08] clips, any preference on the defaults
[039:10] and so on and so forth. I say short
[039:12] clips defaults sound fine. MP4 is great.
[039:17] Okay, I then have the plan in front of
[039:18] me and if I wanted to build this, all I
[039:20] would need to do is click yes and auto
[039:22] accept. And I think I will. That seems
[039:24] pretty straightforward. So, let's give
[039:25] it a try. While this is working, I'm
[039:28] just going to see if I could find an
[039:29] example of a video that I could feed
[039:31] into this. Um, I've done this a couple
[039:33] of times previously as you guys could
[039:35] see. So, let me just find some really
[039:37] simple video that's only a few seconds
[039:38] that we can test this on. Okay. And I
[039:41] found an example here. It's just a short
[039:43] one minute video clip of me doing a
[039:45] typical intro.
[039:47] Now that this thing is building, I'm
[039:48] just going to move this to bypass
[039:50] permissions mode. That'll just allow it
[039:51] to operate autonomously without me. And
[039:53] once it's there, it's actually created
[039:54] it. That's great. As you guys can see,
[039:56] that only took us maybe like 30 seconds
[039:58] or so. From here, I actually want to
[039:59] test this. Let's test using
[040:02] test_clipip.mpp4.
[040:07] Now, I'm not actually expecting this to
[040:09] work the first time around because most
[040:10] workflows don't actually work the first
[040:12] time around. It's all a process of
[040:13] progressive iteration. Essentially, if
[040:15] the workflow doesn't work, the error
[040:17] message is fed back into the agent and
[040:19] then the agent will progressively build
[040:21] the agentic workflow using the u the
[040:23] error messages to sort of guide it in
[040:24] the right direction.
[040:26] In situations like this, I honestly just
[040:28] alt tab and then do something else.
[040:30] Okay. And it actually looks like it did
[040:32] run through the entire test manually and
[040:34] was perfectly fine. That's crazy. What
[040:37] I'm going to do now is I'm just going to
[040:38] watch the test, see how it is, and then
[040:40] we'll just continue to go back and forth
[040:41] a few times until I have what I want.
[040:43] Oh, by the way, I don't even need to
[040:44] find this file. I could actually just
[040:45] say open it. Okay, so I'm noticing that
[040:48] the cuts are kind of abrupt. They're a
[040:49] little bit too fast for me. Um, what I
[040:51] mean by that is like instead of cutting
[040:53] at the point that I wanted it to cut,
[040:55] it's just cutting like a few seconds
[040:56] before. Multiple different ways around
[040:57] this. I could use a different approach
[040:59] to detect the cut points. I could have
[041:01] it manually move things over. I mean, if
[041:03] you think about it, like I could do
[041:04] whatever the heck I want here. Uh, this
[041:06] thing's operating at the speed of
[041:07] thought. So, I'm just going to give it
[041:08] some very high level instructions here,
[041:09] and we'll see what it thinks. It's
[041:11] giving me a bunch of different options
[041:12] here. One of them is voice activity
[041:14] detection. I like this. Let's do this
[041:17] one. Okay, it's now testing with this
[041:18] new approach.
[041:20] All right, let's take a look at round
[041:21] two.
[041:24] Okay, so it worked perfectly on the um
[041:27] one minute clip. So now I'm just going
[041:28] to run it on test three minutes.
[041:32] Okay, and it's just finished and then
[041:34] opened the next clip. Let's just see how
[041:36] that does. There is a cut point right
[041:39] here, I think. Let's see if that's good.
[041:44] Cool. Nice. Looks like it did that cut.
[041:45] That's cool. How about another one? H
[041:49] I think it was right here.
[041:54] Nice. It's solid.
[041:59] Last one right here.
[042:04] Cool. So, yeah, this one worked
[042:05] basically perfectly. Um the agentic
[042:07] workflow is for the most part now
[042:09] complete. So, you guys could see it took
[042:11] one back and forth. I just in a very
[042:12] high level um realistic way gave it a
[042:15] list of what I wanted. I didn't really
[042:16] know what I wanted to be honest, just
[042:18] like I think most people that have
[042:19] probably done any sort of like software
[042:20] engineering work know clients usually
[042:22] have no clue how to scope a project. So
[042:24] you can sort of only take them at face
[042:25] value there. I went back and forth a
[042:27] little bit. Um you know I was like okay
[042:28] this didn't work too well. Is there any
[042:30] other thing that we could do? It gave me
[042:31] some other thing. So I tried the other
[042:33] thing. Hopefully you guys could see that
[042:34] this sort of loop is very
[042:35] straightforward and realistically only
[042:37] takes a few moments of your time. The
[042:39] most important part I think of my entire
[042:41] day is now just providing some sort of
[042:43] highlevel nudge in one direction or
[042:44] another to a agents like this when
[042:46] designing my agenda workflows. Um, you
[042:49] know, like if you just remove me from
[042:50] the loop completely, the resulting agent
[042:52] workflow is probably going to suck, at
[042:53] least for now. But, uh, I'm just here to
[042:55] steer the ship, right? It's almost like
[042:57] as if I don't know, it's like an old
[042:59] school Viking boat where people have to
[043:00] like manually row, right? So, I'm just
[043:02] the person at the very front of the ship
[043:03] doing a little bit of steering. The
[043:04] agents are the minions doing my rowing.
[043:07] At this point, I'm briefly going to
[043:09] cover memory here. It's how agents
[043:10] maintain context. This isn't super
[043:12] important to know for building, but it's
[043:14] important to know if you want to
[043:15] understand how these things work under
[043:16] the hood. So, short-term working memory
[043:18] are basically reasoning tokens that are
[043:20] relevant to the current task. They're
[043:21] stored temporarily. If you guys have
[043:23] ever seen like a little thinking window
[043:25] or a thinking tab with like a little
[043:26] thing that you could click to open
[043:28] inside, it'll be like the user wants to
[043:30] do this. The user is thinking about
[043:31] doing this. This is your uh short-term
[043:33] memory sort of uh analog and like the
[043:35] way that our human brains work. Sort of
[043:37] your intermediate memory is your back
[043:38] and forth messages with the agent. So
[043:40] it's like the actual like message chain
[043:42] that you are having. Those aren't
[043:44] removed like reasoning tokens are. And
[043:45] so this is just always stored and sent
[043:47] with every API call. Long-term memory
[043:49] are things that persist across sessions.
[043:51] So they're variables that are stored in
[043:52] claude chat GBT etc. On the right hand
[043:54] side here, I have that same message that
[043:56] I sent earlier as part of our demo where
[043:58] I scrape 200 HVAC owners. If I show you
[044:00] guys how all of this memory works in
[044:01] context, basically this over here, okay,
[044:04] and then its replies are what are called
[044:06] intermediate messages. Anything inside
[044:08] of this thinking tab is like your
[044:10] short-term, okay? And then long-term are
[044:13] like things that are stored within my
[044:15] file space. So they're things like, you
[044:18] know, my agents MD. They're things like
[044:20] my Gmail accounts.json. They're things
[044:22] like my token leftclick. If this all
[044:25] seems like magic to you right now, don't
[044:26] worry. You're going to get to the point
[044:27] you can actually understand and
[044:28] interpret everything within an
[044:30] integrated development environment by
[044:31] the end of the program. But I just
[044:32] wanted you guys to be on the same page
[044:34] here that this over here is like an
[044:36] intermediate piece of memory. It's going
[044:38] to include all messages that are sent
[044:40] and received from you and the agent and
[044:41] then everything in between the reasoning
[044:43] loops and stuff for short-term whereas
[044:44] long-term tend to be files and then
[044:46] system prompts. Right now, one of the
[044:47] primary failure modes in Agentic systems
[044:50] right now is because of um context. And
[044:52] context, for those people that don't
[044:53] know, is just all of like the the
[044:55] letters and words and tokens that are
[044:57] being stored in a model at any given one
[044:58] point in time. Uh the way that agents
[045:00] manage context limitations right now is
[045:02] they are summarizing previous steps to
[045:04] save on tokens by compressing the full
[045:06] history into key takeaways. If you think
[045:08] about it, like the way that I write and
[045:10] the way that the model writes isn't
[045:11] actually like super token efficient.
[045:12] What it does is it makes a bunch of
[045:14] summaries of these constantly. So if you
[045:16] know this is my actual chat window if
[045:18] you think about it that's the message
[045:19] that the agent sent me and this is the
[045:21] message that I sent the agent this is
[045:22] the message that it sent me back and
[045:24] blah blah blah what it'll do
[045:25] periodically just to save on the token
[045:27] cost is it'll actually just summarize it
[045:29] in as high density a form as humanly
[045:31] possible so we take maybe like a 500word
[045:34] uh uh context and then chunk that down
[045:36] into like a a 100 or maybe a 50word
[045:39] context. It'll do so periodically
[045:41] without losing you the core details just
[045:43] by rewriting it in various ways that are
[045:44] just a lot simpler. For instance, I
[045:46] could say hello, how are you doing? My
[045:48] name is Nick Sarif. Or I could say, hi
[045:52] dash, how you do question mark, I'm Nick
[045:58] Sarif. And if you just like count up the
[046:00] total number of characters there, the
[046:01] latter one is obviously going to be a
[046:02] lot more efficient. They also don't
[046:04] store reasoning in the main loop. It
[046:06] generated temporary and then it
[046:07] disappears. It does store intermediate
[046:08] results externally by offloading the
[046:10] databases, files, and other vector
[046:11] stores. And then it'll now load the
[046:13] relevant context on demand to only pull
[046:15] in what is needed for the current step.
[046:17] Um, you know, you can build this in
[046:19] explicitly using something called a rag
[046:20] or retrieve augmented generation system,
[046:22] which I'll talk about later, or you can,
[046:24] uh, you know, just let the model do its
[046:25] own thing and it does a pretty good job
[046:26] of it. When we make it to reflection,
[046:28] this is where the agent self-evaluates.
[046:30] So that's where it examines its outputs
[046:31] to detect errors and then assess whether
[046:33] or not what it wanted to do actually
[046:35] worked. It identifies the approaches are
[046:36] failing. it knows when to pivot and it
[046:38] just selforrects. This is really like
[046:40] the intelligence of the model to be
[046:41] honest. Um, if you don't have this
[046:43] reflection loop, you will just have a
[046:44] script like a typical Python script or
[046:47] like an nadn or make.com or zapier or
[046:49] gum loop or lindy automation that just
[046:51] breaks at the first hiccup. And this is
[046:52] also really important in what's called
[046:54] self-annealing which I'm going to cover
[046:55] a little bit more of later. But it's
[046:56] essentially the way that an agentic
[046:58] workflow can run and then also just heal
[047:00] itself as it encounters errors and so
[047:02] on. Finally, we have what is called the
[047:03] orchestration or coordination layer. The
[047:05] way that I think of it as if you just
[047:07] get all of these steps, right? So
[047:08] planning, tool use, memory, then
[047:12] reflection. Okay, orchestration doesn't
[047:15] exist within the loop. It sort of exists
[047:16] outside of it or maybe inside of it. And
[047:18] then it's just responsible for shuttling
[047:20] the information around from step to
[047:22] step. And that's really cool, right? It
[047:24] looks at the results of the plan. It
[047:27] then feeds that into the right tools. It
[047:29] then enters what it needs to enter in
[047:31] memory. and then it looks at the results
[047:33] of the reflection and then changes the
[047:35] next loop of the planning and so on and
[047:37] so on and so forth infinitely. I think
[047:38] of it as like the brain that combines
[047:40] all the components that we just talked
[047:41] about similar to how your brain combines
[047:43] inputs from like your ears and your eyes
[047:45] and your nose and your skin and your
[047:47] mouth and your memory and it just like
[047:49] factors everything in and then this is
[047:51] what thinks and then ultimately comes up
[047:53] with decisions. Now there are a couple
[047:54] of different approaches uh right now for
[047:56] orchestration. uh there's an approach
[047:58] with crew AI right now that uses
[048:00] role-based team structures and so you
[048:02] know up at the top you have some sort of
[048:04] manager and then underneath you maybe
[048:06] have like a a marketer and then you have
[048:08] like a software engineer and you know
[048:10] the manager exists above the marketer
[048:12] and the software engineer and the
[048:13] marketer has like you know some interns
[048:15] and so on and so forth the software
[048:17] engineer has some juniors this is one
[048:19] way of doing it um and it's a way that
[048:21] you know crew AAI has done reasonably
[048:23] well with like the sort of framework
[048:25] role-based team structure I think It's
[048:27] kind of like an organization and I think
[048:28] that's just looking at things like a
[048:30] human being would. I think they're
[048:31] actually just much more efficient ways
[048:32] to organize. So I don't personally do
[048:34] this with the directive orchestration um
[048:36] execution framework and then cloud
[048:38] skills. Instead, what we do is we
[048:40] basically give AI access to um both
[048:43] highle instructions and then tools to
[048:47] have it execute. And then this AI over
[048:49] here, this is sort of like that
[048:50] orchestrator that we were talking about
[048:52] before. It just looks the high level
[048:53] instructions, looks at the tools,
[048:55] matches up the two, does stuff, stores
[048:57] things into a memory, and then it just
[048:58] loops over and over and over in that
[049:00] PTML loop. Claude skills is kind of
[049:02] similar. It just um organizes the
[049:04] instructions. If we visualize this for
[049:08] you guys, it basically just stores
[049:09] things into a folder. This folder
[049:13] contains both the highle instructions
[049:15] and the specific tool use and any
[049:18] additional resources. And then the model
[049:21] now just accesses a folder instead of
[049:23] accessing you know two different
[049:24] folders. And really the point I'm trying
[049:26] to make is no framework is perfect yet.
[049:28] I imagine the real best framework in the
[049:30] future is just going to be a combination
[049:31] of all these. You know taking the best
[049:33] parts and leaving the crappiest parts.
[049:34] Um but they are all improving rapidly as
[049:36] the space gets m more and more mature.
[049:38] So my recommendation is we're not going
[049:40] for perfection here. We just want what
[049:41] works. And in my case um I use dough
[049:43] because you know I came up with it and
[049:45] then it's a big part of all the content
[049:46] that I'm producing now. So I mean this
[049:48] works reasonably well right now. Sure,
[049:50] maybe there's another framework out
[049:51] there that'll get us from 97% accuracy
[049:53] to 98.5. I'll worry about that framework
[049:56] when it's here. For now, I'm going to do
[049:58] what I can with the 97. Okay, we're now
[050:00] talking text. This is the universal
[050:02] interface. When I want to talk to my
[050:05] model, I do so through text, right? When
[050:08] I want to talk to my model and I don't
[050:10] know, I try and give it a call or
[050:12] something like you can do on claw on
[050:13] chatbt and stuff like that. What's
[050:15] really occurring is I'm transcribing
[050:16] most of that into text. Now agents if
[050:19] you think about it are actually a step
[050:20] back in terms of our interfaces for now.
[050:23] Back in the day and when I say back in
[050:25] the day I mean like you know very very
[050:27] recently um most people use these drag
[050:29] and drop no code tools right and these
[050:31] are actually really pretty and they're
[050:32] very easily interpretable and you can
[050:34] see how the data flows and so now we
[050:36] basically said no screw that we just
[050:38] want a bunch of words on a screen right
[050:40] which obviously has a bunch of issues in
[050:41] terms of presentation our ability to
[050:43] visualize them and understand them.
[050:44] Right now we are taking a step back in
[050:46] terms of the interface. It's sort of
[050:49] like back in like the 70s, 80s and 90s
[050:51] when most people coded and then built
[050:53] things on computers through DOSs or
[050:55] Linux terminals, right? It was like text
[050:57] in you get results out. That's it.
[051:00] Everything is just like some sort of
[051:01] terminal or prompt. And in this way, I
[051:03] think it can be really intimidating for
[051:04] people because they just see a bunch of
[051:05] text and they're like, "Oh, I'm not a
[051:06] programmer. Oh, I'm not like a, you
[051:08] know, I don't learn through reading and
[051:09] writing. I learn through seeing." And I
[051:11] think that's fair and it's a totally
[051:13] okay criticism to make with these things
[051:14] right now. I imagine future systems are
[051:17] going to go back to a visual interface.
[051:19] It's just we don't have them yet. And as
[051:20] I mentioned earlier, my whole goal is
[051:22] just make do with what we can at the
[051:24] moment. I imagine over the course of the
[051:25] next couple years, somebody's going to
[051:26] build the most amazing visual interface
[051:28] probably in conjunction with one of
[051:30] these agents or agent agentic workflow
[051:32] builders and then we'll have something
[051:33] that combines the best of both worlds,
[051:35] natural language and visualization. But
[051:37] right now we use some tools. And those
[051:39] tools as of the time of this recording
[051:40] are cursor, VS code, and anti-gravity.
[051:43] And that's where most agent interaction
[051:45] happens today. That is the textheavy
[051:47] interface that you guys saw earlier as
[051:48] part of the demo where I just talk to
[051:50] the model through a chat box and see it
[051:51] update files and stuff like that. On the
[051:53] lefth hand side, I have some
[051:54] recommendations to make things feel a
[051:56] little bit more natural. I personally
[051:57] use speech to text tools like um Whisper
[051:59] Flow and Aqua. These are really simple,
[052:01] straightforward transcription tools.
[052:03] They allow you to feel like you're
[052:04] talking to an employee more than you are
[052:06] necessarily writing text or typing at
[052:09] your computer. I'm going to show you
[052:10] guys a bunch of practical examples of me
[052:12] using this. But for now, let me give you
[052:14] guys a demo. On the left hand side here,
[052:16] I'm just talking to my model. I
[052:17] basically converted a workspace from the
[052:19] directive orchestration execution
[052:21] framework to the cloud skill framework.
[052:22] And you guys are going to see both of
[052:23] those later. But for now, I just want to
[052:25] ask it how things are going and you
[052:26] know, if you can tell me something about
[052:27] it. So, I'm just going to hold down a
[052:28] key on my computer. Fn. Hey, can you
[052:31] tell me a little bit about the changes
[052:32] that we just made? I let go and then I
[052:34] press enter and now I'm basically
[052:36] talking to my model. Of course, I still
[052:37] have to press the enter key. Future
[052:39] iterations of this will probably change
[052:41] that, but in this way, I'm maximizing
[052:43] the bandwidth. Human beings can speak a
[052:45] lot faster than they can type, but they
[052:47] can also read a lot faster than they can
[052:48] listen. So, this is typically how you
[052:50] optimize both of those. All right, so
[052:51] what I have here are five cloud code
[052:53] instances. I'm running the latest model
[052:55] of Opus, Opus 4.5, at least as of the
[052:58] time of this recording. You guys may
[052:59] have some later versions, but just to
[053:01] show you as the variability of model
[053:02] outputs, I've set all these to plan
[053:03] mode. And what plan mode essentially
[053:05] means to make a long story short is they
[053:07] just don't they can't take actions
[053:09] without my express or explicit approval.
[053:11] They write a plan for me first, then I
[053:12] verify the plan. And so, just to show
[053:14] you guys how different um various forms
[053:16] of these plans are, I'm going to open up
[053:19] five tabs. I'm then going to um open up
[053:22] the reasoning and kind of thinking
[053:23] panels here. Then we're just going to
[053:25] evaluate how different all of these
[053:27] answers are to the same simple question.
[053:30] What are some ways to send automated
[053:31] proposals? So I sent that to all five.
[053:33] And you'll see that as we proceed
[053:35] through here, there are a variety of
[053:38] different routes that these models
[053:39] follow. After this does its research and
[053:41] and plans, you end up with five answers.
[053:44] And you'll notice that um all five of
[053:46] these answers are different, meaning
[053:47] that there is no like procedural
[053:50] simple step-by-step result here. the
[053:53] models are doing different things every
[053:54] single time. This first one here says,
[053:56] "What type of proposal?" So, it's asking
[053:58] me some questions. The second one here
[053:59] actually just went through and then
[054:00] wrote me a big list of different options
[054:02] I could take. This third one here wrote
[054:04] me sort of a combination, ask me some
[054:06] questions. And then it's giving me some
[054:08] common automation triggers alongside
[054:10] some more questions. This one here gives
[054:12] me these four options. And then this one
[054:14] here gives me like a little table. And
[054:16] this is okay. I mean, obviously I'm
[054:18] arriving at like the same sort of answer
[054:20] regardless, but I want you guys to know
[054:22] that like the way that businesses work
[054:24] is, you know, when somebody does
[054:25] something like they fill out a form or
[054:27] they require an invoice sent or
[054:30] something of that nature. This level of
[054:32] variability in and of itself is way too
[054:33] much. There's no way that we could
[054:35] really like meaningfully add value to a
[054:37] business, whether it's our own business
[054:38] or some other business with variability
[054:40] like this, with like 30 40 50% variance
[054:43] in answers. What we need is when we
[054:45] generate an invoice, the invoice needs
[054:47] to be basically the same every time.
[054:48] When we generate a receipt, the receipt
[054:50] needs to be the same every time. When we
[054:52] send an email, maybe an onboarding thing
[054:54] or whatever, these should be the same
[054:56] every time. When a new form comes into
[054:58] our system and we need to qualify them,
[055:00] we should use the exact same
[055:01] qualification framework every time. Any
[055:03] serious company at scale that has this
[055:05] level of variability in their processes
[055:07] won't be a serious company for long.
[055:09] which is why raw large language models
[055:11] are very difficult to use in u both
[055:14] mid-market and enterprise style
[055:15] applications. Now the reason for this is
[055:17] because LLMs are probabilistic not
[055:20] deterministic. I touched on this earlier
[055:22] on in the course but let me run you
[055:23] through how a large language model
[055:25] actually works under the hood. So a
[055:26] while back I actually built a large
[055:28] language model. Well I guess kind of a
[055:29] small language model. this guy Andre
[055:31] Cararpathy, he um built this big uh like
[055:34] GitHub repo showing people how to like
[055:36] train their own textbased mini GPT. I
[055:40] went through this whole thing and then I
[055:41] built my own mini GPT and it was really
[055:42] instructive and I've since learned a lot
[055:44] more about large language models and
[055:45] sort of what's going on under the hood.
[055:47] So let me just give you guys a very
[055:48] brief demonstration. If you guys
[055:50] understand this, you guys will go a lot
[055:51] further towards getting how these agents
[055:53] are working under the hood. What large
[055:55] language models are are they are
[055:57] basically machines and they are machines
[055:59] that operate off of a distribution of
[056:02] outcomes. What I mean by this is they
[056:05] are statistics sort of pattern matchers.
[056:07] What a lot of people think is that large
[056:09] language models will predict the single
[056:11] best next word but they don't do that.
[056:14] Instead they predict a statistical
[056:16] distribution of options that they could
[056:17] pick from. What I mean is if I say hi,
[056:21] how are and then I have a little space
[056:26] and if you feed this into a model, what
[056:28] you may think you're going to get is
[056:30] you're going to get the most likely next
[056:31] token, right? Which is sort of like
[056:32] universe A. You think you'll just get
[056:33] the word you and then maybe a question
[056:35] mark. But what you actually get is you
[056:37] get a whole graph
[056:39] of different outcomes and possible words
[056:42] that you could choose from. This one
[056:44] might be you. This one might be
[056:49] the word things, right? How are things?
[056:52] This one here might be your, for
[056:54] instance. And what happens is we use
[056:57] this concept of temperature and top P to
[057:02] basically randomize the process of
[057:04] choosing the next token. And so while U
[057:08] may statistically be the most likely
[057:10] next token, maybe U has like a 98%
[057:13] confidence score or something, despite
[057:15] the fact that U is the most likely next
[057:17] token, we're not always going to pick
[057:19] you. What we're going to do is we're
[057:20] going to have some cutoff, which is sort
[057:22] of like this um top P. And then we're
[057:25] going to pick from one of these three or
[057:26] four options. And we're going to do so
[057:28] with a level of what's called
[057:29] stochasticity or randomness. That means
[057:32] that you can't actually predict what the
[057:33] large language model is going to do
[057:35] every time. Now, this isn't a bad thing.
[057:37] This is actually a good thing because
[057:39] think about it. If we could predict what
[057:40] every large language model was going to
[057:42] do, there would be no reason to have a
[057:43] large language model. If you just
[057:44] trained things and always outputed the
[057:46] exact same thing every time, there would
[057:47] be no way for the model to reason
[057:49] flexibly about things. It would
[057:50] essentially just be a giant series of
[057:52] dominoes that just, you know, knock over
[057:54] one to the other. Those are some really
[057:55] crappy looking dominoes to the other to
[057:57] the other. And then, you know, we'd be
[057:58] able to predict everything that's going
[057:59] on. Anyway, models um randomness and
[058:02] stochasticity is actually a big chunk of
[058:04] how they are capable of solving problems
[058:05] and reasoning for us. But what I'm
[058:07] trying to say is there's a level of
[058:09] randomness added to every step of the
[058:10] process. Right? So the first thing is
[058:12] they predict a distribution of options.
[058:14] What that means is there is some
[058:15] randomness. There is some statistical uh
[058:18] error here or or inaccuracy. Next, we
[058:21] can set the temperature and top P. These
[058:22] are settings that you'll find in
[058:23] parameters for most large language
[058:25] models nowadays. Those settings also
[058:27] introduce some randomness to the
[058:28] process. You now have um architectures
[058:31] like the mixture of experts architecture
[058:33] which is basically where they don't just
[058:35] have one large language model do this.
[058:36] They test this simultaneously across
[058:38] four or five large language models and
[058:40] then they pick the most commonly voted
[058:42] task. Believe it or not this introduces
[058:44] some additional variance. Then even at
[058:46] temperature zero tiny input variations
[058:48] can produce wildly different outputs
[058:49] because of randomness. Obviously there
[058:51] is um sort of like probabilities here at
[058:53] every step. Now in math these are
[058:56] basically called compound probabilities.
[058:59] And I don't mean to make this a math
[059:00] thing, but if you're working with AI,
[059:02] you might as well um learn at least a
[059:04] little bit of the math underneath it
[059:05] because it'll help you understand how
[059:07] all these things work. Essentially,
[059:08] these compound probabilities make it
[059:10] very unlikely that you'll be able to
[059:12] achieve the exact same outcome every
[059:13] time on the large language models own.
[059:15] And so what happens is you have these
[059:16] error rates that compound
[059:18] catastrophically. I'll give you a quick
[059:20] example. Let's say you have five steps
[059:22] in a process. You want the large
[059:24] language model to, I don't know, go out
[059:26] into your email inbox, pick the best
[059:28] email, then you want it to summarize
[059:30] that email, then you want to feed that
[059:32] summary into some other model, then you
[059:34] want that other model to take that
[059:35] summary and then combine it with a bunch
[059:37] of other summaries to give you a big
[059:38] digest of the day. So if you have five
[059:41] steps and each of them are 90%
[059:44] successful, the way that math works
[059:46] really is although every individual step
[059:49] may be 90% successful, if you math it
[059:52] out and actually multiply out 90%
[059:54] success for step one time 90% success
[059:56] for step two times 90% success for step
[059:58] three times 90% success for step four
[060:01] times 90% success for step five, you end
[060:04] up not with a 90% success rate across
[060:07] the entire process. you end up with a
[060:08] 59% success rate across the entire
[060:10] process. Essentially what occurs is
[060:12] although the first step might be 90%.
[060:15] The second step when multiply makes it
[060:17] 081 and then you have 64 or 74 or 63 and
[060:21] so on and so forth until eventually your
[060:23] actual total error rate is significantly
[060:25] higher. Your success rate on the other
[060:27] hand is significantly lower. And so when
[060:29] you add more and more steps to this
[060:31] process, you know, if you get to 10,
[060:32] it's 35% success rate. If you're at 20,
[060:34] it's 12% success rate. This applies even
[060:37] if models are 95% successful at specific
[060:39] tasks. What ends up happening is
[060:41] basically at every step of the task. A
[060:44] good way to consider it is the total
[060:47] range and outcomes gets bigger and
[060:49] bigger and bigger and bigger. There are
[060:51] super successful outcomes, sort of quasy
[060:53] successful outcomes. They're not
[060:55] successful outcomes and they're like
[060:56] catastrophic outcomes, right? And this
[060:58] range in business is nowhere near tight
[061:02] enough for most companies to trust
[061:03] systems like this. Now, because most
[061:05] business workflows are multi-step and
[061:07] because people have typically tried
[061:09] doing things like this with dumber,
[061:10] simpler models with no frameworks, you
[061:12] know, most raw LLMs are actually just
[061:14] not usable in business, aside from copy
[061:16] paste outputs, which is why people tend
[061:17] to do that. Just as an aside, imagine if
[061:20] you were a business that made $100,000 a
[061:22] month and you sent a wrong invoice 5% of
[061:24] the time. What sort of impact do you
[061:26] think you that would have to your
[061:27] business? Do you think that would have a
[061:28] 5% impact to your business? No, that
[061:30] would have like a 95% impact on your
[061:32] business. If I'm one of your clients and
[061:33] you send me the wrong invoice even one
[061:35] out of 20 times, I don't think I'm going
[061:37] to work with you the 21st time. So, the
[061:39] root cause here is we're asking
[061:40] probabilistic systems to do
[061:42] deterministic work. Probabilistic is
[061:44] that big sort of uninterpretable
[061:47] thought process that cloud that I showed
[061:49] you guys earlier. Whereas deterministic
[061:51] is what businesses use where you have
[061:53] one step going into the second step
[061:55] going into the third step going into the
[061:56] fourth step and so on and so on and so
[061:58] on and so forth. This over here is what
[062:01] business is and the best businesses, you
[062:04] know, productize and standardize
[062:05] everything. And then this over here um
[062:08] operates in the realm of probabilities
[062:10] which ultimately we can't use. What is
[062:12] the solution here? Well, it's not
[062:13] necessarily just making LLM smarter.
[062:15] Although keep in mind, the smarter the
[062:17] models get typically the less error and
[062:18] variance they do have. That's great. But
[062:21] the actual solution is we don't have to
[062:22] wait for model intelligence to get smart
[062:24] in an unspecified amount of time. We
[062:26] just build a framework around those
[062:29] models that turns these really rickety
[062:31] outputs into something that we could
[062:33] still use anyway despite the fact that
[062:35] there's variability in the process. We
[062:38] give them defined nodes and steps
[062:40] between each important thing that we
[062:43] want. And in that way, because we're
[062:45] shortening the total gap, models are
[062:47] capable of performing economically
[062:48] valuable work. So what we're going to do
[062:50] is wrap this super galaxy brain
[062:52] intelligence in a framework. And this
[062:55] framework is going to allow us to
[062:57] control it for beneficial purposes for
[062:59] ultimately business ends. Okay. So how
[063:01] do you actually do that? Well, this is
[063:02] now where you get into DO or the
[063:04] directive orchestration and execution
[063:06] framework. What we do is we separate
[063:09] concerns. Directives up at the very top
[063:11] provide very clear unambiguous
[063:14] instructions to the system. These are
[063:16] documents which if you guys remember
[063:18] were sort of the first rung on that
[063:20] knowledge ladder. Orchestration, if you
[063:22] think about the PTMRO loop, is where the
[063:24] large language model does its thing. It
[063:27] chooses what to do and in what order.
[063:30] And then execution scripts are the
[063:32] actual heavy lifting. And we don't do
[063:34] that with the model itself. What we do
[063:37] that are with little snippets of code
[063:39] that the model has built, then test, and
[063:41] then retested over and over and over
[063:43] again. Okay? I typically do this in
[063:46] Python right now, but I want you guys to
[063:48] know you can do this with whatever
[063:50] programming language you want. The
[063:51] models tend to be pretty good at I want
[063:53] to say most of them equally. The reason
[063:55] why this works so well is because of
[063:56] this concept of separation of concerns.
[063:59] Essentially, anything that is
[064:00] deterministic aka something that like a
[064:02] business would use. So maybe an API
[064:04] call, some sort of data transformation,
[064:06] some sort of file ops actually go into
[064:09] code. Code is always the same every
[064:11] single time. If you give it input A,
[064:13] it'll always give you output B. There's
[064:15] never any variability unless you
[064:17] specifically program that in. So, it's
[064:19] really, really interpretable. It's very,
[064:20] very clear how it works. And you never
[064:22] really need to wonder, hm, is that doing
[064:24] what I wanted it to do? Because it's
[064:26] only going to do what you told it to do.
[064:28] And then what we do is we leverage the
[064:30] really flexible, cool parts of AI to
[064:32] make judgments, to make routing
[064:34] decisions, and so on and so forth. Code
[064:37] is really reliable. It's also super fast
[064:39] and precise. LLMs are flexible,
[064:41] adaptive, and then also handle ambiguity
[064:43] really well. So, what we're doing is
[064:45] we're combining the best of both parts.
[064:47] We combine AI's incredible ability to
[064:49] route and be flexible and so on and so
[064:52] forth with deterministic code's
[064:54] extraordinarily ability to run really
[064:57] quickly, really precisely, and really,
[064:59] really repeatably. When you do this, you
[065:01] get the best of both worlds, and you can
[065:02] make a ton of money with it. That's how
[065:04] Agentic workflows work in a nutshell.
[065:05] What's interesting is you probably would
[065:07] not have understood any of this had you
[065:08] not watched the last hour to hour and a
[065:10] half of content all about the basis and
[065:12] the foundations. Some other reasons LLMs
[065:15] are really really bad at basic
[065:16] operations. When I say basic operations,
[065:18] I mean math. Up until quite recently, um
[065:21] LLM couldn't even count the number of
[065:22] letters in a word. That's something that
[065:24] you could build a Python script to do in
[065:25] like 0.1 seconds. You know, if you have
[065:27] a big list of numbers or something, you
[065:29] use LLM to sort those numbers. It's kind
[065:31] of like hiring a PhD intelligence to
[065:33] count some inventory. It's just not the
[065:35] best cost basis on your end. You're
[065:36] going to spend way too much money and
[065:38] get way too little of a result. Hence
[065:39] why we pushed the deterministic tasks to
[065:42] scripts and then reserve the LLM
[065:43] processing with the tokens for actual
[065:45] thinking. Also makes everything cheaper.
[065:47] Just for the purposes of demonstration,
[065:49] if I gave an LLM a really simple task
[065:51] and I said, "Hey, I have all of these um
[065:54] letters, okay, and they're all arranged,
[065:57] you know, in this list." And let's say
[065:59] this list hypothetically isn't just, you
[066:01] know, six letters long. It's like a 100
[066:04] thousand or 10,000 items long or
[066:06] something. It's just like really really
[066:07] long. Okay, so just pretend that I put
[066:08] this thing together and I give it to an
[066:10] LM. If I had the large language model
[066:12] sort this thing, it would have to run
[066:14] billions upon billions upon billions of
[066:17] mathematical operations to sort this
[066:18] list. If I gave this to a Python script,
[066:22] it could literally do this entire thing
[066:24] in one function call. I could probably
[066:26] do it in like 5 seconds on my own, not
[066:28] even with a large language model. And it
[066:30] would take milliseconds. If you look at
[066:32] the actual mathematical time and then
[066:34] the resource usage when you use uh
[066:35] deterministic scripts to do things like
[066:37] this, these mathematical simple
[066:38] operations like sort a big list, you
[066:40] could do it 10,000 to 100,000 times
[066:42] faster with deterministic code. And then
[066:45] it's also for the most part free because
[066:47] it's operating on your CPU or
[066:49] extraordinarily low cost cuz it's
[066:50] operating on some cloud CPU or GPU um
[066:52] that's very very uh affordable. This
[066:55] gets more and more and more difficult
[066:56] the more you do. Instead of having the
[066:58] large language model do math for us,
[067:00] what we do is we build a calculator tool
[067:02] and then we say, "Hey, can you call the
[067:03] calculator tool to do the math for us?"
[067:05] In this way, obviously, we're maximizing
[067:07] the best of all possible worlds. So now
[067:09] I want to show you the difference
[067:10] between using a large language model's
[067:12] native intelligence to do something that
[067:14] I think most would consider very simple,
[067:16] which is just sorting a list, and then
[067:18] using a Python script to do it instead.
[067:20] And I'm showing you this because there
[067:22] are so many advantages to using
[067:23] procedural deterministic tools like
[067:25] Python scripts. It's hard for me to know
[067:27] where to begin, but I just wanted to
[067:28] give this to you guys sort of as a
[067:29] representative example. So, what I've
[067:31] done up here is I've just had AI or an
[067:33] agent assist me with the creation of a
[067:35] brief demo list that I'm going to sort.
[067:37] The first thing I'm going to do is I'm
[067:38] going to tell it to sort the list on its
[067:40] own. Sort the list using only your
[067:42] native LLM intelligence. Do not make use
[067:44] of any tools. Time yourself and at the
[067:47] end, let me know how long it took.
[067:50] What I'm going to do now is let it run.
[067:53] And you'll see that when its native LLM
[067:55] intelligence does the sorting, it takes
[067:57] significantly longer in order to do so.
[067:59] We can see the time that it's taking by
[068:01] expanding this reasoning tab.
[068:04] Scroll all the way down here. You can
[068:06] see it's actually manually outputting
[068:07] every token. Here we go. And now it's
[068:10] actually gone through and sorted the
[068:11] list alphabetically by name. Okay.
[068:13] Anyway, it told us it didn't have its
[068:14] own internal clock or whatever, but
[068:16] realistically, as you guys could see and
[068:18] probably timestamped the video, this
[068:19] took what, 30 seconds or something like
[068:20] that from start to finish. Now, I want
[068:22] you to see how quickly it is when we
[068:24] just run a script to do it instead. Now,
[068:26] run the script.
[068:30] So, what it's going to do is instead
[068:32] it's just going to call said script,
[068:34] then it'll immediately sort this with
[068:36] significantly higher levels of accuracy
[068:37] on the right hand side. Now, I should
[068:39] note that the amount of time it took me
[068:41] to call the large language model and
[068:42] actually have it do the thing, that's a
[068:44] bunch of latency here that we're not
[068:45] actually taking into account.
[068:47] Realistically, this took 53
[068:48] milliseconds. The LLM, I mean, it's
[068:50] saying 3 to 5 seconds, but as you can
[068:51] tell, it doesn't really understand its
[068:52] own internal processing. So, it's closer
[068:54] to, you know, 15 to 30. That is um
[068:56] several hundred times faster. And not
[068:58] only is it several hundred times faster,
[069:00] a point that I'm going to make
[069:01] repeatedly throughout this course is
[069:02] also several hundred times freer because
[069:04] running a Python script to sort of list
[069:06] on your own CPU or even on cloud CPU
[069:09] when we get into uh posting web hooks
[069:11] and actually hosting these things on
[069:12] servers that aren't ours is like is
[069:15] essentially free. I mean it's it's
[069:16] occurring in the space of I don't know a
[069:18] neuron in your brain firing. This
[069:19] thing's doing a whole whole buttload of
[069:21] work. And you can see even down here it
[069:23] said this is the core argument for
[069:24] pushing deterministic work into tools.
[069:26] The LLM handles decision-making whereas
[069:27] the script handles execution. That's a
[069:29] major part of how we are going to be
[069:31] talking about how to use these and build
[069:32] these agentic workflows later on. So in
[069:34] a nutshell, my whole point is reserve
[069:36] your large language model calls for
[069:37] judgment. Let code handle the rest. By
[069:40] doing so, things will be significantly
[069:42] faster, things will be significantly
[069:43] more reliable and things will also be
[069:45] significantly cheaper. This is where the
[069:47] DO directive orchestration execution
[069:49] framework comes into play and it's how
[069:51] we're going to be building out the rest
[069:52] of the workflows in this course. Let's
[069:54] talk a little bit more about how to
[069:56] actually do this. Now, okay, so
[069:57] unsurprisingly, right now everything to
[070:00] do with the Gentic Workflows happens in
[070:01] what's called an IDE. If you guys are
[070:04] unfamiliar with IDE, that stands for
[070:06] integrated development environment. Now,
[070:09] idees look like this, and you've seen
[070:12] them already multiple times throughout
[070:14] this course. What they are is they are
[070:16] basically programming environments. Now,
[070:20] agentic workflows are not idees. To be
[070:24] clear here, this is just a way that
[070:25] we're communicating with them. If you
[070:27] guys remember way back in the beginning
[070:28] of this course, I talked about how chats
[070:31] were sort of like an interface and then
[070:33] agents were like things that lived
[070:35] inside of the interface almost the way
[070:36] that a crustation has shells and it can
[070:38] change shells at will. Well, right now,
[070:41] because programmers usually build stuff
[070:43] and because agentic workflows are
[070:45] composed of the same thing that
[070:46] programmers used to build, we just
[070:48] happen to do them in an IDE. But I want
[070:50] you to know that this is most likely to
[070:52] change. Now, I don't like IDEIDes
[070:54] because they just are really overly
[070:55] technical for a lot of newbies, people
[070:57] that don't understand this stuff, and
[070:58] they look at it and they look at all the
[071:00] lines on the page and all the different
[071:01] partitions and sections and then they
[071:02] go, "Holy crap, Nick. This is way too
[071:04] complicated. I'm not a technical person.
[071:05] I don't want to deal with it." But what
[071:07] I want to do in this course is I want to
[071:09] avail you of the notion that you have to
[071:10] be technical in order to understand
[071:11] what's going on. What this is is this is
[071:13] just the same thing as like a bunch of
[071:15] instrumentation panels on a car or
[071:17] something. You know, the very first time
[071:18] you step into a car, you don't know how
[071:19] the odometer works. You don't have any
[071:21] idea what the gear shift is, how the
[071:23] radio works, and all that stuff. This is
[071:24] the exact same thing. I'm currently
[071:26] taking my pilot's license right now, and
[071:27] let me tell you, the damn
[071:29] instrumentation panels on even the
[071:30] oldest and and cheapest of aircraft are
[071:33] sort of the way that I imagine IDs are
[071:35] to people that have never touched these
[071:36] things. So I entirely empathize with you
[071:38] and I'm going to walk you through it all
[071:39] in a moment. So as mentioned IDE stands
[071:42] for integrated development environment.
[071:45] I think of it as basically Microsoft
[071:47] Word just for code instead of you know
[071:49] natural text documents. They're composed
[071:52] of workspaces and this is the same
[071:54] language that basically any IDE will use
[071:56] where you basically just write organize
[071:58] run and then manage everything in one
[071:59] place. And it's important for me to note
[072:01] like how this works in a historical
[072:02] basis cuz otherwise you'll be like why
[072:04] the hell did we choose this? Well, the
[072:06] reason why is because back in the day,
[072:07] we actually used to have like five or
[072:08] six different tools. Uh, programmers
[072:10] would use tool number one to like write
[072:12] their code. Then they'd use tool number
[072:15] two to test their code. Then they jump
[072:17] over into tool number three to, I don't
[072:19] know, run their code, tool number four
[072:21] to host their code, tool number five to
[072:24] commit their code into a a repository so
[072:27] they could save it, and tool number six
[072:29] to do something else. And so there was
[072:31] just so much switching going on, right?
[072:32] We had to jump from tool number one to
[072:33] tool number two, whatever. And then
[072:35] somebody was just like, "Wait a second.
[072:36] Why don't we just combine all of these
[072:37] into one unified tool? Sure, the
[072:39] interface will probably be an absolute
[072:41] cluster, but you know, this is more than
[072:43] enough and it'll probably simplify and
[072:44] and alleviate some of the context
[072:46] switching." And that's basically what
[072:47] happened here. We basically just stuck
[072:49] them all into this one tool. And this
[072:50] tool is really like 20 or 30 tools
[072:52] simultaneously, which is why it looks so
[072:54] complicated. Now, over the course of
[072:55] just the last year or so, ids have
[072:57] gotten way smarter. And I mean smarter
[072:59] here as in like AI. So, in the last
[073:02] year, basically every IDE has added some
[073:05] form of AI chat capability. Old school
[073:08] ones like VS Code, and I'm going to
[073:09] cover what all these are in a minute,
[073:11] added built-in AI assistance quite
[073:13] recently. And then newer tools like
[073:14] anti-gravity, big one that Google just
[073:16] released, are now less like coding
[073:18] workspace, and they've just eliminated
[073:20] and streamlined most of the UX. So, it's
[073:22] almost all just like AI based agent
[073:23] stuff. Basically, the line between
[073:25] writing code and then just directing AI
[073:27] to do it all for you through natural
[073:29] language is blurring really quickly. And
[073:30] that's um one of the motivations behind
[073:32] our course actually. So this over here
[073:34] is VS Codes logo. This over here is um
[073:37] anti-gravities. And this over here is
[073:39] cursor. These are three relatively
[073:41] popular tools that I'm going to touch on
[073:42] in a little bit more detail. And then
[073:44] I'm actually going to walk through VS
[073:45] Code and anti-gravity just so you guys
[073:47] could see how all this stuff really
[073:48] plays out. In a nutshell, if you guys
[073:49] are going to be comfortable with agents,
[073:51] you need to be comfortable in an IDE.
[073:53] That's just the whole goal of today's
[073:54] module. So three areas of your IDE.
[073:58] There's a file explorer on the left.
[073:59] There's an editor panel in the center
[074:01] and then there's an agent chat panel on
[074:03] the right. Let's cover all of them in
[074:04] detail. On the lefth hand side, we have
[074:07] the file explorer. The file explorer
[074:09] almost always looks something like this.
[074:11] All this is is it's just another way
[074:13] that you guys can explore files. Just
[074:15] like on a Mac or a PC, you have the
[074:17] native file explorer. Here, your files
[074:19] are just arranged vertically as follows.
[074:22] This little tab just means that this is
[074:24] a folder. And if you click on one of
[074:25] these, obviously, this will open and
[074:27] expand. and then you'll be able to see
[074:28] all the files within. So just as like a
[074:30] sanity test, this um first kind of line
[074:34] here, this first folder is period cla
[074:37] and there are a bunch of other files
[074:38] inside of period claude. Same thing
[074:40] here. Period dev container period
[074:43] prompts period tmp period venv. You
[074:47] might be wondering, Nick, what the hell
[074:48] do any of these things mean? I'll be
[074:49] honest, I have AI do most of that. I
[074:51] don't even know, nor do I really care.
[074:52] The whole job of coding is not the point
[074:54] of gentic workflow building. All I'm
[074:57] doing is I'm just giving highle
[074:58] instructions and I have the AI deal with
[074:59] the how. Next up, we have a directives
[075:02] folder as you guys see here, an
[075:03] execution folder as we guys see here. Uh
[075:06] I also have a folder called for_youtube
[075:08] in my workspace. This is where I store
[075:10] things like this course node modules
[075:13] prompts trigger, right? What you'll
[075:14] notice is eventually we run out of
[075:16] folders, these little things with the
[075:17] tabs, and then everything else is just a
[075:18] file. So I have this file here, this
[075:20] file here, this file here. We we got a
[075:22] ton of files in the workspace. But
[075:24] hopefully now you guys have like looked
[075:25] at it and squinted hard enough at it
[075:27] that you guys at least understand that
[075:28] there's nothing magical going on here.
[075:29] This is just a file explorer. So just
[075:32] like with any other file explorer, you
[075:33] can create files, you can rename files,
[075:35] you can delete files, and you can
[075:36] organize everything you want from here.
[075:38] For Aentic work, at least in our case,
[075:40] the DO framework. This is also where the
[075:43] directives and executions folders live.
[075:45] As we saw earlier, I had the directives
[075:47] folder here and then the execution
[075:48] folder. I'm going to dive into those and
[075:49] actually show you what these look like
[075:50] in a moment. And really just the way to
[075:52] think about this whole thing is as a
[075:56] filing cabinet. Okay, that does not look
[075:59] like an F, but we're going to roll with
[076:00] it regardless. This is just your filing
[076:02] cabinet for your agent. And so that is
[076:03] how I want you to think about this
[076:05] moving forward. In the middle of the
[076:06] page, you have the editor panel. Now,
[076:08] this is typically in the center,
[076:10] although some idees will vary. That's
[076:12] okay. I'll cover two instances today.
[076:14] When you click on a file, this is where
[076:16] they open. And so for instance, as we
[076:18] see here in this middle panel, I have a
[076:19] file open called capitalized agents.mmd.
[076:23] Now we get into system prompts and how
[076:25] to actually control these u models
[076:27] through long-term context later on. But
[076:29] this is basically just like a file that
[076:31] you will add to any workspace and it'll
[076:33] just be injected at the very top of your
[076:35] agent. So the agent will just always see
[076:37] this in its context 24/7. And in my
[076:40] case, what I do is I just give it some
[076:41] highle instructions describing my
[076:43] framework. Hey, you operate within a
[076:45] three-layer architecture that separates
[076:46] concerns to maximize reliability because
[076:49] of the same things that I just taught to
[076:50] you. LLMs are probabilistic. Most
[076:52] business logic deterministic so on and
[076:54] so on and so forth. Okay? So, we'll
[076:56] cover this file later, but for now, I
[076:57] just want you to know that you can
[076:58] actually open multiple files and tabs
[076:59] just like a browser. You guys see here
[077:01] how this is sort of like a tab. Well,
[077:03] you can actually have multiple other
[077:04] ones open, too. I could have, you know,
[077:05] another file here, and then another file
[077:07] here, and another file here. You'll
[077:09] notice that some of these letters are
[077:10] different colors. You see how this one's
[077:11] blue and then this uh little um you know
[077:14] right arrow is green and then this text
[077:16] is white and then this is uh sort of
[077:18] orangey. Well, the reason why is just
[077:20] because um this this is a natural
[077:22] language file. This is markdown it's
[077:24] called which is a specific format. But
[077:26] like when you're dealing with code like
[077:27] Python and JavaScript and Node and so on
[077:30] and so forth, there's just so many
[077:31] different types of text that coloring it
[077:33] just makes it a little bit easier on the
[077:34] eyes and you can just tell what's going
[077:36] on faster. So in the case of markdown,
[077:38] which is the format that my natural
[077:40] language or almost plain text files are
[077:41] in, um if something is in blue, it's a
[077:44] header. So you know that this is like a
[077:45] header of some kind, right? Same thing
[077:47] over here, right? This is a header or
[077:48] it's like bolded, right? So that's what
[077:50] that is. If something is in orange, you
[077:52] know it's written in like code format.
[077:53] So anytime you write something in code
[077:55] format, it's done with these little back
[077:57] texts. Something is in white, odds are
[077:58] it's just like normal text. Something's
[078:00] in green, it's like a comment or
[078:01] something like that, right? This depends
[078:03] on the format. Typically, we only use
[078:05] two or three formats in Aentic Workflow.
[078:07] So, you're just going to figure this out
[078:08] really quick. Nor does it really matter
[078:09] to be honest because you you never
[078:11] actually read files. And that actually
[078:12] takes me to a great point. Um, you can
[078:14] look at files in the editor panel, but
[078:16] you'd almost never actually manually
[078:17] edit them. My rule of thumb is if I'm
[078:20] manually editing a file, I am doing
[078:22] something horrifically wrong because
[078:24] there's no real reason why I should be
[078:25] manually editing a file. I just
[078:27] communicate with my agent and then it
[078:28] does it for me. Even if I want to change
[078:30] a specific file, I won't go into that
[078:32] file. I'll just say hey change specific
[078:34] file to do this and then typically I'll
[078:36] just give it a oneline description of
[078:38] what I want it to do and it'll go
[078:39] through and it'll do it in the most
[078:40] efficient way. In this way I'm almost
[078:42] like the CEO of my own company. I mean I
[078:44] am the CEO of my own company but I am
[078:47] like the CEO of my own agent company. I
[078:49] just give very highle instructions and
[078:51] then it's the agent that interprets
[078:52] those highle instructions and does
[078:53] things. So that's two out of the three
[078:55] sections. The third is the agent chat
[078:57] panel that exists all the way on the
[078:59] right. So the agent chat panel is
[079:00] hopefully very familiar to you guys.
[079:02] Same sort of thing as just any chat over
[079:04] the last four or five years. In this
[079:06] case, I just said, "Hey, what's up?" It
[079:07] then read through agents.mmd. As I told
[079:09] you, it always reads through this at the
[079:11] very beginning of every run. And then it
[079:12] says, "Hey, not much. Just ready to
[079:14] help. What are you working on?" So, this
[079:15] is your primary interface. This is
[079:17] really where you're going to live. And
[079:19] uh it's such a primary interface that
[079:20] the modern idees like anti-gravity and
[079:22] stuff have basically done away with
[079:24] everything else except for this. And you
[079:25] just talk to this all day. So, you'll
[079:27] type your instructions here. Agent will
[079:29] respond. You can even see the thinking
[079:31] tab over here with the reasoning
[079:32] processes is deciding what actions to
[079:34] take. That's really cool for
[079:35] interpretability reasons. And it's also
[079:37] just one of my favorite things to watch
[079:38] because you're seeing the AI's internal
[079:40] monologue. It's also good and and useful
[079:42] when you're building aic workflows,
[079:44] which obviously we're going to cover uh
[079:45] quite shortly so that you could stop it
[079:47] if it makes some mistake. Um you could
[079:50] see where maybe an error is, do your
[079:51] debugging and so on and so forth.
[079:53] Finally, just an obligatory section on
[079:55] code. I know code is really intimidating
[079:57] for a lot of people. I want you to know
[079:59] that all scripts are is they're just
[080:01] text written in a hyperspecific way.
[080:04] This over here is what's called Python.
[080:07] Do I know what's going on over here? I
[080:09] mean, yeah. I've done some coding in
[080:10] Python, so I can look at this. I can
[080:12] kind of interpret it, but I I I can't do
[080:14] so very quickly, and I don't know what's
[080:16] going on for the most part. You don't
[080:18] actually need to have any clue what's
[080:20] going on in the code these days in order
[080:21] to do really powerful, effective things
[080:23] with them because, as I mentioned
[080:24] earlier, AI is just a way better coder
[080:26] than you. So, if you find yourself
[080:28] opening coding scripts and stuff, you're
[080:30] probably doing something wrong. I never
[080:31] actually have a page open like this
[080:33] because it just means no difference to
[080:34] me. Now, if you do find yourself opening
[080:37] this for whatever reason, I want you to
[080:38] know that a Python script or whatever
[080:40] language you're using, Python's just one
[080:41] of the many. It's just a set of
[080:43] instructions for the computer to follow.
[080:44] It's the same sort of thing as like the
[080:46] the the bullet points that I was showing
[080:48] you guys at the beginning of the course
[080:49] where I was describing an instantly auto
[080:51] reply bot. This is just a set of
[080:53] instructions written in a way that this
[080:54] computer understands, but it's literally
[080:56] just text sitting in a file. It doesn't
[080:57] do anything on its own. What you have to
[080:59] do in order to turn this into some sort
[081:01] of function, turn this into some sort of
[081:03] execution script, is you have to run it.
[081:04] And that just means telling the computer
[081:06] to run the instructions. And typically
[081:08] the way you do this is you do this
[081:09] through the terminal yourself. You'd
[081:11] find the file, you'd see it's called
[081:12] Python script. py. Then you'd actually
[081:15] go into the terminal and very
[081:16] intimidatingly, you know, if you even
[081:18] script one character, it's not going to
[081:19] work. You actually have to type all that
[081:20] yourself. Well, guess what? you no
[081:22] longer have to do that. The agent just
[081:24] does all the coding for you and then it
[081:25] also runs the code for you. That's what
[081:27] makes it such a powerful um orchestrator
[081:30] and that's why I live entirely in the
[081:32] editor. Agents just run all the code. I
[081:35] just say, "Hey, run my Upwork scraper."
[081:37] Do I have to know the format to to
[081:38] execute it? No, I don't. What I do is I
[081:41] just say, "Do the thing I want." It'll
[081:43] then do some thinking. It'll find the
[081:45] specific file that I'm referencing and
[081:46] then it'll go and it'll run it. And so
[081:48] now this is actually running. It handles
[081:50] the entire execution loop autonomously.
[081:52] That's the whole point of agentic
[081:53] workflows. So don't worry about being
[081:55] hyper precise. If you spend too much
[081:57] time being hyper precise, you're kind of
[081:58] wasting it because models, as I
[082:00] mentioned, are just millions of times
[082:01] faster than us. They think just
[082:02] extraordinarily quickly. This is really
[082:04] just the domain of the model.
[082:06] Communicate with it almost like you'd be
[082:07] communicating with an employee or staff
[082:09] member. Obviously, you wouldn't say,
[082:10] "Hey, Pete, run the Upwork scraper. Give
[082:12] me the results. Uh, post it to Slack and
[082:14] then give me the Google sheet URL. Hey,
[082:16] could you send Sandy an email about X,
[082:18] Y, and Z? Use the email template. Just
[082:20] speak to it like you'd speak with an
[082:22] employee. Don't speak with it like you'd
[082:23] speak with a programmer, and you're
[082:24] going to do a lot better. When you do
[082:26] this, your IDE becomes essentially a
[082:28] visual chatbot where you can just watch
[082:30] the agent work 24/7. And that's where
[082:32] things get really cool and really
[082:33] powerful. So, back in the day when we
[082:36] didn't have agents, we had to create a
[082:37] lot of this stuff manually. What I have
[082:39] open here on the right is the terminal.
[082:42] And the terminal is essentially the
[082:44] command line interface way that you
[082:47] would communicate with your computer in
[082:48] order to get valuable knowledge work
[082:50] done. Usually programming work. And so
[082:53] before you know I couldn't just say hey
[082:55] write me a script that does XYZ. Why? It
[082:59] would say command not found. This only
[083:02] works in the context of specific
[083:04] commands. You know instead I would have
[083:06] to use Python 3 for instance. I'd
[083:08] actually have to open it up and then I'd
[083:10] have to, I don't know, create a
[083:11] function. So, let's just do x= 5, y =
[083:15] 10, um, x + y equals what? 15. As I'm
[083:20] sure you guys could tell, this is pretty
[083:21] laborious. And obviously, this is like a
[083:23] highly specialized domain of knowledge
[083:25] that you have to learn in order to be
[083:26] able to communicate with things in this
[083:28] way. Well, if I clear all that out of
[083:30] the way, with our previous example, we
[083:32] had um a list, right? That list looked
[083:35] kind of like this. It was a big list and
[083:38] items with water filter, compass watch,
[083:40] matches, so on and so forth. So back in
[083:43] the day, if I wanted to build a script
[083:45] to do this, I needed a tremendous amount
[083:47] of domain specific knowledge to be able
[083:49] to put together scripts like this. What
[083:51] this does here is this. This actually
[083:53] sorts the list. It's Python 3 C import
[083:57] JSON, D equals JSON.load, open
[084:00] item.json, D items equals sort key
[084:03] equals lambda. I mean, this is like this
[084:04] is a whole another language you have to
[084:06] learn. You know, it's like me trying to
[084:07] write an essay in Portuguese or
[084:09] something. You know, the amount of time
[084:10] and energy it would take for me to be
[084:12] able to know just how to do this one
[084:14] thing would be immense. And you know, I
[084:16] can do it and then my list gets nice and
[084:17] sorted. But the amount of work that I
[084:19] had to do in order to get that done is
[084:20] tremendous. Contrast that with our
[084:22] agent. All I'm going to say is write me
[084:24] a simple function to sort this file
[084:26] alphabetically, then execute it. It's
[084:28] going to do some thinking to begin. So
[084:30] first it's going to read the file then
[084:32] it's going to see the structure and it's
[084:34] going to write the script and then
[084:35] execute it basically immediately. The
[084:37] amount of time that it previously would
[084:38] have taken me somebody with no knowledge
[084:40] how to do this probably is on the orders
[084:42] of like a day at least just to be able
[084:45] to write that script let alone all other
[084:46] ones and this thing can now do it in you
[084:48] know just a few moments. You offload the
[084:50] coding to the model have it actually put
[084:52] together these deterministic scripts
[084:54] which are a lot more reliable and then
[084:55] what you do is you just sort of sit back
[084:57] and orchestrate. Okay, so IDEs, as I
[084:59] mentioned, were kind of like code
[085:00] editors, right? And they've been around
[085:02] for quite a while, at least 15 years.
[085:04] They weren't designed with AI agents in
[085:05] mind, but the new breed of IDs just give
[085:08] agents access to everything. They have
[085:09] your editor access, they have terminal
[085:11] access, they even have browser access.
[085:13] Now, so there are three main options I
[085:15] want to talk about today. Each of them
[085:16] have different trade-offs, and your
[085:17] choice depends on how much flexibility
[085:19] versus simplicity you want.
[085:22] The first is anti-gravity. I'm actually
[085:24] going to be opening this in a moment and
[085:25] then running through this in a lot more
[085:26] detail. But basically, this is Google's
[085:28] brand new agentic development platform
[085:31] launched super recently and it's very,
[085:32] very good. It's designed primarily for
[085:34] their Gemini class of models, but it
[085:36] supports other providers as well. It's
[085:38] the cleanest and simplest interface in
[085:40] the bunch, has by far the lowest
[085:41] learning curve, and it looks something
[085:43] like this. On the lefth hand side, it
[085:45] has the file explorer. On the right hand
[085:47] side, you have your agent. And you'll
[085:48] notice in the middle, it's actually
[085:50] empty. And there's the ability to open
[085:51] up agent managers, code with the agent
[085:53] or edit the code inline. For the most
[085:55] part, this thing is really simplified
[085:57] and it knows that you don't really give
[085:58] a crap about what the files look like.
[086:00] Obviously, if you open a file, it'll
[086:01] open up in the middle, but for the most
[086:03] part, it abstracts away all that for you
[086:04] and you just communicate with the model
[086:06] and it does what you want it to do. Next
[086:07] is VS Code. That stands for Visual
[086:09] Studio Code. This is a lot older of a
[086:11] platform. It's actually the platform
[086:12] that all other platforms are kind of
[086:13] based on nowadays. It was built by
[086:15] Microsoft. It's their free co-et code
[086:17] editor and it's very, very popular. The
[086:19] big draw to Visual Studio Code is its
[086:23] extensibility. You can't really see this
[086:25] that well, but over on the right there's
[086:26] this little extensions tab. And VS Code
[086:28] just has like a massive supported
[086:29] library of all the different extensions
[086:30] you could want. These extensions are
[086:32] pretty cool. Now, for the most part
[086:34] nowadays, we just use like the Cloud
[086:35] Code extension, GitHub Copilot, right?
[086:38] These like AI model extensions that add
[086:40] AI functionality into your code. But
[086:42] there are some cool things that you can
[086:43] build in with extensions that just allow
[086:45] you to use whatever the heck you want
[086:46] with it. So, I see this as less of like
[086:48] a specific AI editor and more as just
[086:50] like a really general editor that a lot
[086:52] of people are used to. They just import
[086:53] extensions to turn their editor into,
[086:56] you know, a hyperoptimized AI one. I'm
[086:58] going to be showing you this one as
[087:00] well, just because it's very popular.
[087:01] Finally, I want to chat a little bit
[087:03] about Kurser. Kurser is actually one of
[087:04] the first like AI editors on the market,
[087:07] like an an editor that was built
[087:08] specifically for AI in mind. I don't
[087:10] really like using Kurser these days
[087:12] myself. Um, obviously it's baked in
[087:14] directly to every part of the platform.
[087:17] But for the most part, I just find
[087:18] anti-gravity is better in every way,
[087:20] shape, and form. Um, very similar
[087:22] interface to what you guys are used to.
[087:23] So, there's a file explorer, there's an
[087:25] editor, and so on and so forth. The file
[087:26] explorer, which you can't actually see
[087:28] in this screenshot, is usually just on
[087:29] the left hand side. Then in the middle
[087:31] here, you have like the big code editor,
[087:32] and then on the right hand side, you
[087:34] have both a chat and a composer. Same
[087:36] sort of vibe to anti-gravity. Aside from
[087:37] that, it just has access to everything.
[087:40] I'm not going to cover this one just
[087:41] because while it's somewhat popular,
[087:42] it's not as popular as the other two
[087:43] options and I want to be mindful of
[087:45] everybody's time. Okay, so let's start
[087:46] with anti-gravity. Pretty
[087:48] straightforward stuff. On the lefth hand
[087:49] side, we have that file explorer, which
[087:50] I talked about to you guys earlier. In
[087:52] the middle, we have obviously the
[087:54] editor, which is where you can open
[087:55] specific files and then change things.
[087:57] And on the right hand side, you have the
[087:58] agent window, which is where you can
[088:00] talk with agents. So, just to be clear,
[088:02] I sent this agent a message saying,
[088:03] "Hey, what's up?" And then it tells me,
[088:04] "Hey, I'm ready to help. I see you've
[088:06] been working on a variety of workflows
[088:07] recently from YouTube transcript
[088:08] analysis and panda dooc proposals to
[088:10] lead scraping. What would you like to
[088:11] tackle today? To cover the middle
[088:13] section here as I talked about earlier
[088:15] uh markdown.md is the file format that
[088:17] we put a lot of instructions in. And
[088:19] you'll notice that we have a blue sort
[088:21] of headers over here you know orange
[088:23] text over here and then the rest of it
[088:24] is uh is white. And so what I've opened
[088:26] up is I've opened up a simple directive
[088:28] called the Upwork scrape apply system
[088:31] which just scrapes Upwork jobs matching
[088:32] AI automation keywords, generates
[088:34] personalized cover letters and proposals
[088:36] and outputs to a Google sheet with a
[088:37] one-click apply link. The whole idea
[088:39] behind the system, and I'm going to show
[088:40] you how to build ones just like this in
[088:41] a moment, is you can automate the
[088:44] process for the most part of applying to
[088:45] an Upwork job. Upwork being a freelance
[088:47] platform. This sort of stuff is going to
[088:49] very quickly become an integral part of
[088:51] most people's workflows. So as you can
[088:53] see here, we define some inputs. So, we
[088:55] give it some tools. We give it a filter.
[088:57] You may be thinking like, good lord,
[088:58] Nick, did you write all this? No, of
[089:00] course not. I had AI, write all of this
[089:01] for me based off some simple bullet
[089:03] points. It's very meta. You use AI to
[089:04] come up with the instructions for
[089:05] another AI model. Um, in a way, in that
[089:08] way, you are literally just some person
[089:09] that is giving some minor instructions.
[089:11] You're acting more as like the motivator
[089:13] than anything else. Okay, I remember I
[089:16] talked about on the left hand side how
[089:17] there'd be a couple of different folders
[089:19] here, directives and then executions.
[089:21] I'm just going to open up directives and
[089:22] show you guys around a little bit. So,
[089:24] as you can see here, I have a bunch of
[089:25] these different flows set up. One of
[089:27] them was Upwork, scrape, apply, but
[089:28] there's, I don't know, another 15 or so.
[089:30] Create proposal MD, cross niche
[089:32] outliers, deep research, pitch, and so
[089:34] on and so forth. Let's say I'm in the
[089:36] building process of an agentic workflow.
[089:38] What I'm going to do is I'm going to ask
[089:39] this to help me out. Hey, is there
[089:41] anything that I could do to the create
[089:43] proposal directive to improve it?
[089:46] Suggest some alternative approaches.
[089:49] Going to enter that in. And now the
[089:51] model is going to come up with some ways
[089:52] that we can make things better. It's
[089:54] going to do so with the directive
[089:55] structure. Um we injected a prompt into
[089:58] its uh agents MD, claude MD, Gemini MD,
[090:01] multiple different ways to initialize
[090:02] system prompts, but it has all the
[090:03] context about what I mean. And this is
[090:04] how Gemini's UX works. You know, analyze
[090:07] and improve, create proposal directive.
[090:09] Gives me the reasoning loop over here,
[090:11] progress updates, it gives me a big
[090:13] plan, and then I get some
[090:14] interpretability, some access to its
[090:16] thoughts. At the end of it, we end up
[090:18] with, "Hey, you should add a human in
[090:20] the loop review step. Hey, you should
[090:21] try a web enrichment option. Hey, you
[090:23] should handle variable token counts.
[090:25] Hey, you should do robust JSON handling.
[090:26] Hey, you should do a dynamic follow-up
[090:28] email." That's pretty cool. I like the
[090:30] idea of number two. Number two sounds
[090:32] great. Why don't we give that a try? All
[090:35] I'm doing is asking it for its opinion.
[090:37] I went through. I didn't like four out
[090:38] of the five, but I did like the second.
[090:40] So, now I'm just going to have this
[090:41] model go to the directive and then
[090:43] update it to include a web enrichment
[090:45] step. It's then built me a plan that
[090:46] looks pretty straightforward and easy.
[090:48] I'm then going to okay this. What I
[090:50] really like about Gemini is it just
[090:51] shows you sort of like the tracked
[090:53] changes really easy. And you can see
[090:55] here that it's now provided an
[090:56] additional step called research client.
[090:58] Understand the client's brand voice and
[090:59] current context. So on and so forth. If
[091:01] a website URL is provided or can be
[091:03] inferred from the email domain, then use
[091:05] this thing to fetch the client's landing
[091:07] page. Analyze all this information and
[091:09] output a brief summary. So I like this.
[091:11] I'm going to accept it. And then I'm
[091:12] going to say, "Yeah, sounds great. Let's
[091:14] give this a try.
[091:16] As part of this specific workflow, um, I
[091:18] have the model ask me a bunch of
[091:20] questions about the client. To be
[091:21] really, really straightforward here, I'm
[091:23] actually just going to open up chat GBT
[091:25] and then going to take a screenshot of
[091:27] this. I'll feed this in and I say, I'd
[091:30] like you to give me a bunch of example
[091:32] data here. I'm feeding this into a model
[091:34] for a demo, for a YouTube video.
[091:38] I'm then going to have Chat GPT
[091:39] construct a big list of demo
[091:41] information, and then I'm going to feed
[091:43] that in in a second.
[091:45] Okay, as you guys can see here, I have a
[091:46] bunch of data sets here. Um, they fed me
[091:49] in 10. I'm just going to use one, use
[091:52] this information for the demo.
[091:55] Cool. And now I'm sort of orchestrating
[091:56] multiple AI models. I am certainly using
[091:59] chatbt as a copy paste sort of thing,
[092:01] but I just wanted to show you guys that
[092:02] like this is data that is in a way real.
[092:06] It's data that is supplied outside of
[092:07] the system that I'm feeding into this
[092:09] workflow. I'm not having um Gemini
[092:10] itself within its own context come up
[092:12] with it. I'm giving it a bunch of
[092:14] information outside of things. Okay. And
[092:16] at the end of it, I actually have a
[092:17] fully functional proposal over here for
[092:19] bright path learning with an AI powered
[092:21] student success predictor. How cool is
[092:23] that? We have all of the problem
[092:24] statements, the solution statements.
[092:26] It's really clean. It's pretty nicely uh
[092:28] well done. Uh even includes some
[092:30] information here about pricing and so on
[092:32] and so forth. So, these are actual
[092:33] proposals that I sent to actual clients.
[092:34] As you guys see, we just generated a
[092:36] bunch of demo information for a
[092:38] hypothetical demo client that actually
[092:39] meaningfully altered a workflow in
[092:41] something like 30 seconds of actual
[092:43] work. Everything else is me just waiting
[092:44] for the model. Okay, so that was
[092:46] anti-gravity. Now, I just want to show
[092:47] you guys VS Code. And one of the reasons
[092:49] I want to show you guys this is because
[092:51] I want to show you that you can open up
[092:52] the same workspace on multiple different
[092:55] IDEs. You could actually create a
[092:57] workspace and then you could run it in
[092:58] anti-gravity, you could run it in VS
[093:00] Code, you could send it to your buddy
[093:02] who operates in cursor. There's so much
[093:04] that you could do here. It's fully
[093:05] interoperable. The only thing that
[093:07] really matters is the agent itself and
[093:10] then the workspace. You could swap out
[093:11] Gemini for GPT 5.2. You could swap that
[093:14] out for Claude Opus. I mean there
[093:15] there's just so many different options
[093:17] here obviously, but just want to give
[093:18] you guys um sort of a view into the fact
[093:20] that all the stuff is interoperable. It
[093:21] doesn't actually really matter what you
[093:22] use. So just pick whatever makes sense
[093:24] to you, what you enjoy. Okay. So VS Code
[093:26] works very similarly because the two are
[093:28] very heavily inspired by each other. Um
[093:30] on the lefth hand side we have the file
[093:31] editor. So right now I have the
[093:32] agents.mmd file open. Okay. So if I go
[093:35] over here you can see it's actually in
[093:36] the root directory. So I'm going to give
[093:37] that a click. That opens up the
[093:39] instruction file. Obviously I'm then
[093:42] feeding in um you know some very simple
[093:44] information here just saying run my
[093:45] Upwork scraper. It's actually gone
[093:46] through generated proposals pushed to a
[093:48] Google sheet. Same sort of idea. If I
[093:50] open up this Google sheet I have
[093:51] information about specific Upwork jobs.
[093:53] This took a few moments which is why I
[093:55] didn't do this in real time. Um in my
[093:57] case I was running a really simple
[093:58] workflow. I didn't want to edit a
[093:59] workflow here. or I actually just wanted
[094:00] to use one. And you'll see that there is
[094:02] a distinction between the building of
[094:03] the workflows and then the using of the
[094:04] workflows. In my case, I'm now using a
[094:06] workflow, not building it. Um, which is
[094:08] why I just had it say, "Hey, let's run
[094:10] this thing." The color scheme is
[094:12] slightly different. It looks slightly
[094:13] different. I'd say VS Code looks a
[094:15] little bit older, of course. But the
[094:16] most important thing that I'll show you
[094:17] that sort of distinguishes VS Code from
[094:19] a lot of things is just how big their
[094:21] extension library is. They really do
[094:22] support a tremendous number of
[094:24] extensions. If I just type the letter A,
[094:26] you'll see here that there are like
[094:27] hundreds of extensions that it opened.
[094:29] This is the search bar for all of the
[094:30] extensions. I could scroll down this
[094:32] thing for hours and probably never run
[094:34] out of things. Hell, I could probably do
[094:36] this for like the next two months or
[094:37] whatever and then I'd never run out of
[094:38] extensions. So, that's pretty cool.
[094:40] There's just a ton of different things
[094:41] you could do depending on what you're
[094:42] doing. There's code formatterers to
[094:43] change like the colors and stuff like
[094:45] that. Uh, you can kind of think of this
[094:46] as like I don't know who here plays
[094:48] video games, but it's kind of like
[094:49] Skyrim mods, Oblivion mods, you know,
[094:51] like you can just modify it to do
[094:53] whatever the heck you want, which is
[094:54] really awesome. Okay, you guys have now
[094:55] seen anti-gravity and VS Code in action.
[094:57] Let's talk a little bit more about the
[094:59] workspace itself. I've shown you guys
[095:00] how to operate within a workspace, but
[095:02] how do you actually set it up? Well,
[095:03] first thing is you have to obviously
[095:04] create a workspace. That's really easy.
[095:06] Anytime you open one of these IDs for
[095:07] the first time, the first thing it'll
[095:08] say is, "Hey, you should create a
[095:10] workspace." So, assuming you've done
[095:11] that, now you're inside of the
[095:12] workspace. What we have to do now is we
[095:14] have to set up the folder structure that
[095:16] our agent can understand and then
[095:17] navigate. We also need to give it some
[095:19] instructions that it knows how we
[095:21] structure the folder and why. And if you
[095:23] think about what I'm doing with you guys
[095:24] and then what I did with the agent with
[095:26] the agents.mmd file, I'm basically
[095:28] giving it a whole education as to why we
[095:31] are in the do framework, why we're using
[095:32] this to begin with. And I find that sort
[095:34] of context is really important. It's
[095:36] like a training uh session for your
[095:38] agent. Get them up to speed. Have them
[095:39] understand the methodology and the
[095:41] philosophy behind why you're using them
[095:43] in that way. And they'll typically work
[095:44] a lot better than if you just tried to
[095:46] raw dog it. So I think about this the
[095:47] same as like setting up a desk for an
[095:49] employee at your organization. They need
[095:51] to know where everything goes. They need
[095:52] to have like the base sort of things set
[095:54] up. They need to have the base folders
[095:56] and so on and so forth. Then once you've
[095:58] given them that structure, they can
[095:59] obviously excel within it. So I'm going
[096:00] to cover a lot more about this in the do
[096:02] section, but uh for now just know that a
[096:04] well organized workspace I would
[096:05] consider essential. So what is the
[096:07] actual project structure? Well, let me
[096:09] show it to you. We start off with the
[096:11] workspace itself. And you can name the
[096:14] workspace whatever you want. Now
[096:15] underneath the workspace, you then have
[096:17] two major folders. You have directives
[096:20] over here. Then right over here, you
[096:22] also have execution.
[096:25] Now, inside of directives, let me show
[096:27] you guys what that would look like. You
[096:29] have a bunch of files. So, you would
[096:31] have, for instance, scrape_leads.md.
[096:37] You might have another one, upwork
[096:41] applybot.md.
[096:44] These are your highlevel instructions
[096:45] where all of the top information goes.
[096:48] you know like hey start the scraping
[096:49] leads thing by asking the user what
[096:51] leads they want to scrape right once
[096:53] they've supplied those leads uh the
[096:54] directions to you then ask them what
[096:56] platform they want to use just some very
[096:58] highle stuff now underneath that as I
[097:00] mentioned we have the executions and
[097:02] then we have the actual like um Python
[097:04] scripts that correspond to the
[097:05] directives so over here for instance
[097:07] we'd have and let me just make this
[097:08] really really simple to see we'd have
[097:11] things like uh appify which is a
[097:14] platform scraper
[097:16] py I underneath that we'd have I don't
[097:19] know Upwork
[097:22] scraper
[097:24] py maybe underneath that we have upwork
[097:28] applier or something like that
[097:31] py and what essentially occurs in your
[097:33] directives is you just say somewhere
[097:35] within it hey step three I want you to
[097:37] call ampify scraper py it reads that in
[097:40] the directive and then it just knows
[097:42] which execution to call I have some
[097:44] recommendations here of course um use
[097:45] subfolders for inputs outputs, prompts,
[097:47] and reference materials. So that is sort
[097:49] of what the directives and the
[097:50] executions are. But if you, let's say,
[097:51] have a bunch of files that you feed in
[097:53] routinely as resources, you can
[097:55] absolutely add a resources folder. The
[097:58] only two folders that I would consider
[097:59] required in the DO framework anyway are
[098:01] just directives and executions. And
[098:03] depending on the framework, you know,
[098:04] people have different ideas about this,
[098:05] but you can add in whatever other
[098:07] folders you want. You could add a
[098:08] resources folder. A common folder to add
[098:09] is a TMP folder. That just stands for
[098:11] temporary. So sometimes agents um need
[098:14] to create files temporarily to do
[098:16] things. They use files like as like
[098:17] scratch pads. Uh my friend Gio yesterday
[098:20] was telling me about an experiment that
[098:21] somebody did where he had like a chat
[098:23] room for agents.mmd
[098:26] where basically he had multiple agents
[098:28] run simultaneously and then add things
[098:30] to a chat room. I mean obviously the
[098:31] world is your oyster here and I'm not
[098:32] going to try and force you in a specific
[098:34] way of being, but there are a variety of
[098:35] other folders that I would probably
[098:36] include as well. I'd include some clear
[098:39] naming conventions so the agent knows
[098:40] what lives where. For instance, if uh my
[098:42] thing scrapes leads, I would call it
[098:43] scrape underscore leads. I wouldn't call
[098:45] it like s_l with some naming convention.
[098:47] I mean, these character tokens are
[098:49] cheap, right? Be very descriptive with
[098:50] the titles of your files. And then if
[098:52] you have any documentation like the
[098:53] highle context and then you know like
[098:55] your agents
[098:57] MD and so on and so forth, make sure to
[098:58] include that as well. Talked about the
[099:00] directives and execution folders. So I'm
[099:02] going to leave that. Um directives
[099:04] generally holds things in markdown.
[099:06] That's important to understand, which is
[099:07] just a way to, you know, um mark up text
[099:09] a little bit. An execution is typically
[099:10] in Python, although that depends. And
[099:12] this is just that simple separation
[099:14] between what you do and then how you do
[099:16] it. So the directives are what you do
[099:18] and then the execution scripts are how
[099:19] the thing actually happens. I don't want
[099:21] to beat a dead horse here. Um the number
[099:23] one other thing that you guys really
[099:25] need to understand is this idea of an
[099:26] env file. So when you're working in any
[099:29] sort of programming environment,
[099:31] typically you don't want to store like
[099:33] passwords and secrets and API keys in
[099:35] the code itself. you want to store it in
[099:37] a separate area which um programmers
[099:39] have created a convention around called
[099:41] your env. That's just sort of like where
[099:43] you store all of your API keys, all of
[099:45] your credentials and so on and so forth.
[099:46] And the idea is instead of saying, "Hey,
[099:49] use this API key in your directive," you
[099:52] just say, "Hey, grab all your API keys
[099:54] from your env." That way, logically, if
[099:57] you ever wanted to share your directives
[099:58] later on, you could do so really easy.
[099:59] You would just copy and paste them. And
[100:01] I'm going to cover how to share and set
[100:02] up cloud-based instances later on. A lot
[100:04] of people ask me why these naming
[100:06] conventions exist, why an env.
[100:09] Some things in technology just are. You
[100:11] ever ask yourself why um JPEG files are
[100:14] called JPEG files? Well, it's because
[100:16] this is actually like an organization. I
[100:18] forget what the name of the organization
[100:20] is. It was like the journal for blah
[100:21] blah blah blah blah blah executive
[100:23] group, right? This is just a thing that
[100:26] has occurred 50 years ago that we all
[100:28] just must follow now. And if we change
[100:30] the name, then other people won't
[100:31] understand what they are. So it's just
[100:32] easier to stick with the name is widely
[100:35] recognized by basically everybody. So we
[100:37] just call these things and that's okay.
[100:39] Likewise there are some conventions
[100:41] right now between the models themselves.
[100:43] So for instance um I talked about system
[100:45] prompts things that you inject at the
[100:46] very top of any model conversation and
[100:49] there's a b a bunch of different ones
[100:51] right now. Claude.md corresponds to
[100:53] claude. Gemini.mmd is for gemini.
[100:56] Curser.md is for curser. agents.m MD is
[101:00] sort of like a general one that is
[101:02] supposed to be a fallback in case you
[101:03] don't have this specific one. And you
[101:05] know what I do? I just throw all of
[101:07] these in my main project route so that
[101:09] whatever model I use, I have the exact
[101:11] same sort of thing. So I will copy the
[101:13] same thing from agents MD to cloud MD to
[101:15] Gemini. MD to cursor MD. This
[101:17] interoperability is really really easy.
[101:19] And obviously these names matter. Just
[101:21] because somebody said, well, we should
[101:22] probably have some configuration file.
[101:24] Why don't we just call it claude MD? We
[101:26] use capitals because that'll stand out
[101:27] and make it like hypersp specific and
[101:29] differentiable and then other people
[101:31] sort of went on that bandwagon and
[101:32] that's how it is. If you upload a
[101:33] gemini.mmd to claude then claude isn't
[101:36] going to understand what that is.
[101:37] They're not going to automatically
[101:38] insert it. But if you upload a claude.md
[101:40] to claude it will. If you upload uh you
[101:42] know agents.mmd or codecs or cursor or
[101:44] whatever to your various models of
[101:45] choice it'll understand what's going on.
[101:47] The really cool thing is you just create
[101:49] the structure one time and then the
[101:51] agent just works with it for every
[101:52] project going forward. Which is one of
[101:54] the reasons why I love this. The
[101:56] initialization is so easy that I now
[101:58] don't even tell people to initialize it
[101:59] themselves. I just give the agents item
[102:02] D file to anybody I want to set up and
[102:04] then I just say hey have your model do
[102:06] it. Then they just go to their agent and
[102:07] they say hey can you set up my workspace
[102:09] according to this file and then it does
[102:11] so automatically. How cool. I want you
[102:12] guys to know that as you get better and
[102:14] better with IDE, this feeling of
[102:16] overwhelm will decrease. But at the
[102:18] beginning, it is totally normal to feel
[102:20] overwhelmed with the menus and the
[102:21] panels and the buttons and all the
[102:23] keyboard shortcuts. Um, it's just like a
[102:25] beginner pilot looking at cockpit
[102:27] instrumentation right now. I think I
[102:28] told you guys that I was taking my
[102:29] pilot's license and it is it is really
[102:31] intimidating. This is the exact same way
[102:33] that I tried to put myself in your guys'
[102:35] shoes when explaining this. I wish
[102:36] somebody explained pilot instrumentation
[102:38] to me the same way I'm explaining ID
[102:40] instrumentation to you. But you don't
[102:41] need to learn everything at once. And
[102:43] hopefully it's clear, as long as you
[102:44] understand those three things, the file
[102:46] explorer on the lefth hand side, the
[102:47] editor in the middle, and then the agent
[102:49] chat on the right hand side, you're
[102:51] already 80% of the way there, and you
[102:52] can build and use Agentic Workflows for
[102:54] your own business. The goal isn't to
[102:56] master every feature here. It's just to
[102:57] be comfortable enough that the ID
[102:59] doesn't like slow you down. Okay, so let
[103:01] me show you how you can easily build
[103:02] proposals and high-quality PDFs and
[103:04] visual assets with Agentic Workflows.
[103:07] This is an example of a workflow that I
[103:08] use all the time in my day-to-day
[103:09] business. So immediately underneath this
[103:11] I have a sales call transcript.
[103:13] Essentially what we do is we feed in
[103:14] these sales call transcripts and we just
[103:16] tell the model hey I want you to
[103:17] generate a proposal with it. So what am
[103:19] I going to do? I will literally just say
[103:21] generate a proposal using the below
[103:22] transcript. Then I'm going to press
[103:25] enter. What's going to happen is this
[103:27] model is going to immediately start
[103:29] looking through the existing directives
[103:32] which I'll talk a little bit about more
[103:33] later in the course. It'll find contact
[103:36] details and everything that we need in
[103:37] order to actually send the proposal
[103:39] because I removed the email from this
[103:41] specific one. I am going to supply just
[103:43] a demo email. What its reasoning is
[103:45] doing is it's extracting the main
[103:46] problem areas, the main solution areas,
[103:48] the things that we talked about and also
[103:50] the pricing. Immediately afterwards,
[103:51] it's going to ask me for the email
[103:53] address. This is a demo, so just use
[103:57] and I'm going to provide my own.
[104:01] And once it has this information, it can
[104:03] proceed and actually go through with the
[104:04] generation of the asset. So it's not
[104:06] formatting this in the way that I want
[104:07] the proposals to look like. Keep in mind
[104:09] that I had no real work here aside from
[104:11] copying my transcript over. And even
[104:13] that is unnecessary. I could have just
[104:14] used it directly from the transcript
[104:16] provider Fireflies, but I wanted to show
[104:17] you guys how malleable this sort of
[104:19] thing is. Whether you copy and paste it
[104:21] in, whether you put an API call to like
[104:23] some transcript endpoint in, uh, you
[104:24] know, it works the same regardless.
[104:26] Great. And it's finished. Now it's going
[104:28] to do is send a quick follow-up email.
[104:30] And the email was sent successfully just
[104:32] using an MCP server that I set up. And
[104:34] now we get a summary as well as a link
[104:37] so we can view it directly.
[104:40] When I open this up, you can see the
[104:41] proposal document right here. It
[104:43] includes um you know your problem areas.
[104:46] Number one, your revenue is
[104:47] unpredictable because you're relying on
[104:48] referrals and sporadic outreach. One
[104:50] month may bring three clients, the next
[104:51] month brings zero. The feast or famine
[104:53] cycle makes it impossible to plan
[104:54] hiring, delivery capacity, or growth
[104:55] investments with any confidence. This is
[104:57] all stuff that the AI came up with. You
[104:59] know, I chatted about this briefly on
[105:00] the transcript, of course, but um
[105:02] everything else here, the tone of voice
[105:04] and everything like that was just a very
[105:06] simple highle prompt instruction as well
[105:08] as a brief example. The actual workflow
[105:10] here took me maybe 15 minutes to set up
[105:12] and to end. And as you can see now with
[105:14] just a prompt, uh I can generate
[105:15] high-quality sales proposals within
[105:17] seconds. So, this is what you are going
[105:19] to learn how to do. You're going to
[105:20] learn how to set up workflows, not only
[105:22] to do things like generate proposals,
[105:24] although I absolutely recommend you do
[105:25] if you're in any sort of service
[105:27] business where you have sales calls, but
[105:28] we can do more or less anything. I've
[105:30] set up dozens of workflows to automate
[105:32] many of the mundane routine business
[105:34] tasks that I have. Things that just a
[105:36] few years ago, people probably would
[105:37] have raised an eyebrow at you and
[105:38] thought you were crazy for suggesting
[105:40] you can automate something like this.
[105:42] All right, it's now time to talk about
[105:43] DO directive orchestration and
[105:45] execution. So up at the very top of
[105:47] this, you can see that I've written
[105:48] three layer software architecture.
[105:51] That's because that's what DO is. It is
[105:52] a three layer system that we're wrapping
[105:55] around an AI agent in order to help
[105:58] constrain its outputs and take it from
[106:01] like a probabilistic thing which is all
[106:02] over the place to something very
[106:04] standard, consistent, and deterministic.
[106:07] So at the very top of this system is
[106:09] your directive layer. Of course, this is
[106:11] going to include workflows and SOPs. And
[106:14] by the way, if you don't know what SOP
[106:15] means, that stands for standard
[106:18] operating procedure. And standard
[106:21] operating procedures are very common in
[106:23] any sort of business, which is one of
[106:24] the reasons why I like Do so much
[106:27] because all you really do is just import
[106:28] your standard operating procedures in
[106:30] whatever business you are working with,
[106:31] whether it's your own or business you're
[106:32] helping. Then you just say, "Hey, turn
[106:34] this into a directive as per do." And
[106:36] boom, you're done. You now have like an
[106:37] AI agent that just does tasks that your
[106:39] company needs to do. So up at the very
[106:42] top kind of the first layer is this
[106:43] directive. Now underneath you have the
[106:46] orchestration layer. Your orchestration
[106:48] layer is your AI agent or AI employee in
[106:51] a way. And you'll also see that like not
[106:54] only did I put a little robot face here,
[106:55] but I also put a person. And the reason
[106:57] why is because it's actually pretty
[106:58] similar to how most organizations work.
[107:00] You have some highle directives. Those
[107:01] directives are read by employees or you
[107:04] know other people in the business. And
[107:06] then what they do is they just make
[107:07] decisions surrounding how to accomplish
[107:09] the highle uh directives. This is where
[107:12] they perform coordination, task
[107:13] management, and stuff like that. And
[107:15] what they do with those decisions is
[107:17] they call or use tools. Now, if you're
[107:20] an AI agent, you're going to be using
[107:22] mostly software tools as expected. Hell,
[107:24] if you're an employee, for the most
[107:25] part, you're going to be using software
[107:26] tools. Now, think of the tools that an
[107:28] average employee uses in any
[107:29] organization. We're using Google Sheets,
[107:31] Excel. We're using Microsoft Word, Docs,
[107:33] right? All of those things are actually
[107:35] analogous to tools that we use within an
[107:38] organization to accomplish things. It's
[107:40] the same thing that our AI does with
[107:42] tools that it creates. Okay. So down at
[107:44] the very bottom here, you have the
[107:45] execution layer and this contains tools.
[107:48] It contains Python scripts and so on and
[107:49] so forth. It's primarily responsible for
[107:51] action and output. I don't want people
[107:54] here to be really scared or worried
[107:56] about DO. It's a lot simpler than you
[107:58] may think. The thing is we just need to
[107:59] frame it as like a three- layer software
[108:01] architecture in order for the rest of
[108:02] the course to make sense. So to be
[108:04] clear, do is literally just a folder
[108:06] structure plus a system prompt. And
[108:09] pretty much all frameworks out there
[108:10] right now for aentic workflows are all
[108:13] we do is we just set up a folder called
[108:15] directives and a folder called
[108:17] execution. Then we add some files like
[108:19] an agents MD, cloud MD or Gemini MD as
[108:22] our prompt and then you know we might
[108:23] add avi keys etc. Again, the API uh env
[108:28] is literally just a convention that, you
[108:30] know, some programmers made forever ago.
[108:32] So, it's great for beginners primarily
[108:34] because it's intuitive and it's really
[108:35] easy to understand. And it's also really
[108:37] cool for businesses because we can just
[108:38] copy and paste SOPs directly in like um
[108:41] a company that I'm currently working
[108:42] with right now does marketing
[108:43] specifically for dental practices and
[108:45] they do about $2 million a year. And
[108:47] when I introduced agentic workflows to
[108:49] them, you know, I'm kind of like in a
[108:51] meeting I met with the director and I
[108:52] started discussing how, hey, you know, I
[108:53] think we could probably automate a
[108:54] couple of the previously non-automatable
[108:55] tasks with aentic workflows, he's like,
[108:58] okay, so how do we start? And I was just
[108:59] like, well, you guys got a knowledge
[109:00] base. Why don't I just feed the entire
[109:01] knowledge base in and see what happens?
[109:03] And within 15 minutes or so, we had
[109:05] actually like procedurally turned most
[109:07] of those things into agentic workflows.
[109:10] We had all of the the API keys. We had
[109:12] everything that we needed preset which
[109:13] was lucky cuz a lot of the time you have
[109:15] to jump around and you know finagle
[109:17] various services. Um but yeah within 15
[109:19] minutes we had turned this into dough
[109:21] and we now have a workspace that you
[109:22] know the director managers and myself
[109:24] can use to do like 90% of the
[109:26] economically valuable work. Is that
[109:28] going to lead to some headcount
[109:28] reduction? Probably. I mean when you
[109:31] automate 90% of 10,000 people's roles
[109:33] obviously you need to take a step back
[109:34] and start doing more management style
[109:36] stuff than actually getting your hands
[109:37] dirty. Uh but yeah, that's just a very
[109:39] simple and straightforward example of
[109:40] something that I have actually just just
[109:41] now done. The reason why dough works
[109:44] really is because of the whole
[109:45] stochasticity idea. And stochasticity
[109:47] just for anybody that's like why the
[109:48] heck is Nick using all of these crazy
[109:50] words. It's just the way to formalize
[109:52] randomness I would say. I mean it's a
[109:54] little bit different but for for our
[109:55] purposes you could use that. So it just
[109:56] takes this big like if this is like the
[109:59] total range of possible outcomes. Okay?
[110:01] You know you could do uh this outcome
[110:03] you could do outcome somewhere here. You
[110:04] could do this outcome you could do
[110:06] outcome somewhere here. All DO does is
[110:08] it just reduces this so that the range
[110:09] of possible outcomes is a lot more
[110:11] narrow. And so, you know, for the most
[110:13] part, we're operating within a very
[110:15] tightly bounded range of possible
[110:16] outcomes for our system. It can do this
[110:18] or it could do that. And it's very, very
[110:20] similar uh because we do this through
[110:22] the separation of concerns. It's just a
[110:24] lot more reliable. This lets me get to 2
[110:26] to 3% error rates on a lot of business
[110:28] functions. That dental uh marketing
[110:30] business that I was talking about
[110:31] earlier is a great example of that. It's
[110:33] really not more complicated than that. I
[110:35] also like to think of it as I don't know
[110:36] if you guys have ever gone bowling or
[110:37] something, but uh this is going to be my
[110:39] crappy
[110:41] bowling pin thing. Um you know,
[110:44] typically the way that bowling works is
[110:45] you have gutters on the side and you
[110:47] know if your bowling ball is not very
[110:48] good or if you are not very good at
[110:50] bowling I should say. Um you know like a
[110:53] lot of the time it's going to veer off
[110:54] into the gutter and then you're screwed,
[110:55] right? So as a total newbie, one thing
[110:58] that I really like doing is I like
[110:59] asking them to set up the guardrails. So
[111:01] I say, "Hey, do you mind setting up the
[111:02] guardrails for me?" Then they set up
[111:04] these little guardrails that basically
[111:06] prevent the ball from um landing. And so
[111:09] what ends up happening is I basically
[111:11] will bump off of a wall and then I still
[111:13] get to hit some pins. That's all dough
[111:15] is for agents. It just constrains it. We
[111:17] just give it some guardrails and then we
[111:18] significantly improve the probability
[111:19] that it does something that we want. So
[111:21] I'm going to go very into detail here
[111:23] and be very comprehensive because this
[111:24] is the framework we're using for the
[111:25] rest of the program. You've already seen
[111:27] me use this a bunch through the various
[111:28] demos that I've I've created. Now I just
[111:30] want to provide context for everything.
[111:31] If some of this stuff is repetitive or
[111:33] if you think you already know this
[111:34] stuff, that's okay. I would recommend
[111:35] just watching it regardless. Try and
[111:37] internalize as much of this as possible
[111:39] because this is the same idea that any
[111:40] framework uh is going to use. So the
[111:43] directives obviously are SOPs written in
[111:45] natural language as markdown files.
[111:47] Markdown is very important. File ending
[111:50] all will end in MD. That's obviously
[111:53] stands for markdown. Uh and generally
[111:55] speaking, this is just a sort of like
[111:57] markup language.
[111:59] A markup language just formats text. So
[112:03] this is plain text for instance, right?
[112:04] First SOPs are written in natural
[112:05] languages as markdown files. Uh uh uh
[112:08] you know marked up version of this might
[112:09] be first. Let me make sure I got this
[112:12] right. You had some stars. SOPs and now
[112:14] this is bolded text are written in you
[112:17] know natural language. And so now it's
[112:19] like quoted text as markdown files. What
[112:21] we're doing is we're taking text and
[112:22] then we're just marking it up. We're
[112:23] adding some structure to it basically.
[112:25] Um markdown is just one way to do so.
[112:27] So, for instance, this on a page is
[112:28] actually markdown underneath it. Um, I
[112:30] used markdown to help uh I used AI
[112:32] actually to help me convert a big
[112:33] 17,000word document into um a slideshow.
[112:36] And so, this was actually a heading. And
[112:38] the way you demonstrate or the way you
[112:40] use headings in markdown is you use
[112:41] little number signs. So, for instance,
[112:43] if I wanted to write this big heading, I
[112:44] actually would have written this layer
[112:47] one, you know, directives.
[112:50] Underneath that, you have bullet points.
[112:51] Bullet points in markdown are little
[112:53] stars. So star first, you know, s os are
[112:58] written, right? So all of these little
[113:00] characters are just a ways that you add
[113:02] formatting to text. And the reason why
[113:03] we do this for our AI agent for
[113:05] directives is because formatting allows
[113:07] us to add a lot moreformational content
[113:09] to the text. It also allows us to
[113:11] structure things. So it's not just one
[113:12] giant massive text dump. We add we get
[113:14] to add new lines. We get to add various
[113:15] tabs for indentation. Basically, we just
[113:17] add a bunch of structure to things as
[113:20] opposed to it just being this, right? we
[113:22] basically convert it into something that
[113:24] is a lot more interesting. We have
[113:26] spaces and we have little bullet points
[113:28] and you know the structure of the text
[113:30] kind of looks like a face funnily enough
[113:31] you know allows us to impart a lot more
[113:33] information per token and then it's also
[113:35] token efficient. There are other
[113:36] markdown languages as well. One that
[113:38] you've probably heard of before is or
[113:40] markup languages as well. One that
[113:42] you've probably heard before is called
[113:43] HTML. With HTML the way you mark things
[113:45] up is you use a variety of tags. And so
[113:48] tags are these little number sign
[113:49] things. If I were to try and write the
[113:51] same thing in tags, it would be
[113:53] significantly less token efficient and
[113:55] so I'd actually have written way more um
[113:58] total tokens, which obviously would have
[114:00] consumed a lot of my context. So instead
[114:02] of that, okay, instead of the HTML body,
[114:06] H1 layer 1 directives, H1, whatever, all
[114:08] we're doing to to accomplish the same
[114:10] thing is I literally just do a number
[114:11] sign. Obviously, this is one character.
[114:12] That's like, I don't know, however many
[114:13] characters, way more, obviously, to just
[114:15] um demonstrate some some structure
[114:17] there. Okay, so that's markdown. Now,
[114:20] these define your goals. They define
[114:22] your inputs. They define your tools,
[114:23] your expected outputs, edge cases, and
[114:26] ultimately a lot of other things that
[114:27] you can define. I don't proclaim to have
[114:29] the perfect directive creation
[114:30] structure. I'm going to show you my own
[114:31] directive creation structures, and that
[114:33] tends to include all these things, but
[114:34] um in general, you just want to provide
[114:36] highle overviews. Now, the way I write
[114:38] these or the way I have AI write these
[114:40] is I write them like I'd instruct a
[114:42] competent employee. I would make them
[114:43] clear, but I would not micromanage. And
[114:45] really, AI does this for you. All I do
[114:47] is I describe the what and the highle
[114:49] hows of my task in markdown and then I
[114:51] just trust the agent to figure out the
[114:52] rest. I'm going to remember to drink
[114:53] this tea cuz it is going to get cooled.
[114:59] Damn, that stuff's good. Holy.
[115:02] So directives obviously live in the
[115:04] directives folder in our workspace. The
[115:06] way I separate each directive is as a
[115:08] separate markdown file that covers one
[115:10] workflow or one capability. For
[115:13] instance, I would have a scrape_leads.
[115:18] MD file, but I wouldn't have a run
[115:23] business MD file just because, and maybe
[115:26] we'll get to this point later, I don't
[115:27] know, but um just because this is a lot
[115:29] that we're asking from the model. And so
[115:30] the model typically starts looping over
[115:31] and and doesn't really understand
[115:33] various edge cases and stuff like that.
[115:35] I constrain these into sort of like
[115:38] modular directives. And then later on I
[115:40] can actually group them with umbrella
[115:42] directives. Not umbrella to the point
[115:44] where it's literally like hey run my own
[115:45] business but umbrella to the point where
[115:47] it's like hey you know run onboarding
[115:49] flow or something like that. So some
[115:51] examples lead scraping MD proposal
[115:53] generation MD email_enrichment MD and so
[115:56] on and so forth. I highly recommend
[115:58] making the names descriptive. Logically
[116:00] speaking these are the only things that
[116:03] uh descriptives descriptive um this is
[116:05] the only way that like the model can
[116:06] tell kind of what's going on here. You
[116:08] can of course add um some other forms of
[116:11] structure to the text. You could add
[116:12] what's called YAML front matter, which
[116:13] I'll talk about a little bit more later
[116:15] on. But for the most part, like the
[116:16] model just consumes the name and then
[116:18] uses that name to determine which
[116:19] workflows it's going to use. If I say,
[116:20] "Hey, I want you to scrape some leads,"
[116:22] obviously it's going to do the lead
[116:22] scraping one, right? But if I just
[116:24] called that L_S with some
[116:26] naming convention, it would have no idea
[116:27] what it's doing. So very important here
[116:29] to just like be descriptive. Don't use
[116:30] acronyms. Don't use anything that like
[116:32] complexifies the names of the directives
[116:35] if you want the agent to be able to use
[116:36] it as best it can.
[116:40] Very important point is that directives
[116:42] contain no code at all. There is zero
[116:44] code within a directive. All directives
[116:46] are are natural language instructions.
[116:49] We don't have any code, no executables.
[116:51] And really there's there's very little
[116:52] technical here. You know, I may [snorts]
[116:53] include some URLs. I say, "Hey, go to
[116:55] this URL in order to get information
[116:57] about this." But I'll never actually
[116:58] include any sort of code or executable.
[117:02] The reason why is because we want these
[117:03] directives to remain readable by all
[117:05] humans within the organization. And they
[117:07] should just make sense to all people
[117:08] within the company. If your directives
[117:10] are to the point where they're so
[117:12] technical and confusing that like any,
[117:14] you know, average low-level staff member
[117:16] within the business could not read it
[117:17] and understand what's going on, you've
[117:18] screwed up. The whole idea is that you
[117:21] want to lower the barriers to entry so
[117:22] that anybody in your company that is
[117:24] system-minded, they don't have to be
[117:25] technical, but they have to know systems
[117:27] can actually just improve things. You be
[117:29] like, "Oh, um, yeah, take a look at that
[117:30] directive and let me know if there's
[117:31] anything that you think I'm missing."
[117:32] And then they just read it natural
[117:33] language and they go, "Oh, you know, uh,
[117:35] sometimes customers ask for X, Y, and Z.
[117:37] We should probably add some logic
[117:38] there." Right? You want that person to
[117:40] actually be able to substantially
[117:41] improve the organization. You don't just
[117:42] want it to be like a black box. Because
[117:44] that's one of the main benefits of this,
[117:46] right? We're making this really, really
[117:47] interpretable. removing bottlenecks
[117:48] across the organization to have people
[117:50] see and understand how uh the systems in
[117:52] the business work. Okay, so next up
[117:54] we're going to talk about layer two
[117:55] which is orchestration. This is kind of
[117:57] like the who. Um orchestration is
[117:59] basically a competent project manager.
[118:01] So a good project manager in business
[118:02] rarely actually does the hands-on work
[118:04] themselves. They're basically just like
[118:06] a nexus and that nexus takes information
[118:08] in and then it kind of puts information
[118:10] out. And you know this might be person
[118:13] one, person two, person three. They're
[118:15] going to take inputs from these three
[118:16] sources. They're going to do some
[118:18] thinking and then they're ultimately
[118:19] going to go and delegate some additional
[118:20] work to person 1 2 and 3. So they make
[118:22] routing decisions at the end of the day
[118:24] and they take advantage of available
[118:25] tools. If you think about old school no
[118:27] code flows like NAD and stuff like that,
[118:29] this job was basically done by you and
[118:31] you would orchestrate it once when you
[118:33] built the flow. You'd say this node goes
[118:35] to this node, this node goes to that
[118:37] node, that node goes to that node, that
[118:40] node goes to that node. Maybe this thing
[118:42] loops around a little bit and then
[118:44] eventually we, you know, do this node or
[118:46] something like that. This is a decision
[118:48] that you would make once when you built
[118:50] the flow. What's really cool is the
[118:52] orchestrator basically just does all of
[118:54] that on its own. So if I just show you
[118:56] guys as like a practical example here,
[118:58] the orchestrator
[119:02] instead just compiles all the tools and
[119:05] then at runtime it decides, hey, you
[119:08] know, I actually want to do this and
[119:09] then this is actually going to go over
[119:10] here. After that's done, it's going to
[119:12] go over here. That's going to go over
[119:13] here. We're going to loop back three
[119:15] times over there, start over here, and
[119:16] then we'll finish over here. And because
[119:19] it's flexible, it can adapt to any
[119:21] situation at the time that you are
[119:23] asking it to do things. You just give it
[119:24] tools and then it just does all the
[119:26] routing and stuff like that for you.
[119:27] Obviously, we want to provide at least
[119:28] some structure, right? We don't want to
[119:30] just give it a bunch of tools and say,
[119:31] "Hey, figure it out." That's what our
[119:32] directives are for. So, it does ensure
[119:34] work gets completed according to those.
[119:36] But the flexibility here allows it to
[119:38] deal with situations like when something
[119:40] breaks, how to diagnose the problem
[119:41] rather than just crash and and you know,
[119:43] 404. And then later on if you use sub
[119:45] aents like I recommend throughout the
[119:47] program um we're going to have like a
[119:48] document flow that not only will go
[119:51] through see uh workflow end to end if
[119:54] there's any problems it'll diagnose it
[119:55] and so on and so forth it'll actually go
[119:57] back and it'll document for the purposes
[119:59] or rather the benefits of future
[120:00] instances of the agent um you know
[120:02] changes that it made things that you
[120:04] know the agent needs to keep in mind
[120:06] logical errors that you know maybe
[120:08] agents typically make to avoid API
[120:11] exceptions that don't really make sense
[120:12] or work and so on and so forth.
[120:14] All right, layer three is execution,
[120:16] which is the how. So, logically
[120:18] speaking, execution is deterministic.
[120:20] It's very modular. It's very
[120:21] straightforward. Doesn't mean it's
[120:23] simple. The execution scripts are stored
[120:25] in the execution folder. I typically
[120:27] just use Python for this. Why? Cuz the
[120:29] programming language doesn't really
[120:30] matter to be honest. And when you have
[120:32] Python, like at any point in time, if
[120:34] you needed to, you could convert this
[120:36] into whatever the heck you want. You can
[120:37] convert Python into Rust, you can
[120:39] convert uh into Node, you could convert
[120:40] it into Java. I mean, like whatever
[120:42] language you want really. These things
[120:43] are all [snorts] essentially just
[120:45] conversions of natural language at this
[120:46] point. Anyway, each script handles just
[120:49] one thing. So, one job or one task. I'll
[120:51] give you an example just using what we
[120:53] talked about earlier. So, if I have like
[120:54] a scrape leads directive, this is like
[120:57] the highle kind of workflow. Right? Now,
[121:00] this workflow isn't just going to have
[121:01] one, you know, scrape_leads.py
[121:06] script. This might actually have
[121:08] multiple different scripts. This might
[121:09] have uh you know depending on whatever
[121:11] you're using might be like
[121:13] scrape_appify.py
[121:17] might have like a upload to gsh sheet.py
[121:23] hell might even have if you have to make
[121:25] some interface or something present
[121:28] to user.py.
[121:31] But the point is these things all just
[121:33] do one thing really well. So this one
[121:34] scrapes appy really well. This one
[121:36] uploads to a Google sheet really well.
[121:37] This one presents to a user really well.
[121:39] These are just like things that you know
[121:40] you like like tools that an agent can
[121:42] use in order to do some task. So what
[121:45] happens is because they're
[121:46] deterministic, they do the exact same
[121:48] thing every time when given the same
[121:50] inputs. So like if I were just to I
[121:52] don't know do this raw dog it and just
[121:54] feed in some prompt to my agent and say,
[121:56] "Hey, I want you to scrape aify for X,
[121:57] Y, and Z." And I had no tools and no
[121:59] directives, you know, it would
[122:01] eventually figure out what I wanted to
[122:02] do. But if I did it 10 times, you know,
[122:04] on route one, it would go from here
[122:07] to here and then on route two would feed
[122:09] back and route three, you know, we just
[122:12] have fundamentally different um
[122:13] executions every single time, right?
[122:15] When you have the exact same inputs
[122:17] provided to the exact same execution
[122:19] scripts and then you get the exact same
[122:20] outputs, it becomes very obvious like
[122:22] what the model needs to do and you
[122:23] heavily constrain the inputs and outputs
[122:25] uh and you essentially just provide a
[122:27] simple rule. Hey, you know, if I say,
[122:29] hey, scrape appy or whatever, uh, for
[122:32] Texas, uh, for 200 people, it'll
[122:34] actually feed that in as a parameter to
[122:35] the scrape appy. It'll actually like
[122:37] have dash dash, you know, location
[122:40] equals Texas, for instance, and then d-
[122:45] um, you know, amount equals 200 or
[122:47] something like that. And because we are
[122:49] being extraordinarily explicit here,
[122:50] there's never any misunderstanding. So,
[122:52] the agent just always knows what to
[122:53] expect. So, do you. Another example here
[122:55] would be a scrape_apollo. That would
[122:57] scrape leads from Apollo, but maybe you
[122:59] also enrich the leads. Well, now you
[123:01] have enrich_clearb. Maybe that enriches
[123:03] company data via that tool. Maybe you
[123:05] then have a send email that sends emails
[123:07] via specified service and then a create
[123:09] pandock which generates proposals. What
[123:11] you'll quickly realize is when you build
[123:12] a sufficient enough library of tools,
[123:14] you can have multiple directives
[123:16] reference the same tools. Like for
[123:17] instance the send email pi maybe as part
[123:20] of my scrape_leads.mmd
[123:24] directive I always send an email with a
[123:27] summary of the leads right so maybe you
[123:29] know somewhere here I say hey you know
[123:30] generate the the leads scrape it with
[123:31] apolla and then send an email well what
[123:33] about the create panadoc maybe in the
[123:35] create panadoc uh maybe I have like a
[123:37] generate proposal MD well the generate
[123:39] proposal MD um also needs to send an
[123:43] email what's really cool is when you
[123:45] define these atomic functions Both of
[123:47] these can call the same execution
[123:49] script. And because we've optimized the
[123:52] hell out of these execution scripts by
[123:54] rerunning and self- annealing and all
[123:55] this stuff, which we'll talk about
[123:56] later, um, this is really robust and it
[123:58] basically like works every time.
[123:59] Execution scripts are not AI for the
[124:01] most part. They don't hallucinate. They
[124:03] don't make things up. They basically
[124:04] either work correctly or they throw a
[124:05] clear error. So there's no ambiguity.
[124:06] There's a programming term here called
[124:08] unit testing, which basically means like
[124:10] you can like isolate this down to its
[124:12] barebones function, just its input and
[124:14] its output, and you can just test that.
[124:15] You can version control them. So you can
[124:17] have like a log of updates and you can
[124:19] optimize them independently. You could
[124:20] start with like um some sort of serial
[124:22] flow where it goes one and then it does
[124:24] two and then it does three and then
[124:26] after a few runs maybe it'll come up
[124:28] with a more efficient way to do things.
[124:29] For instance, maybe it'll split it and
[124:31] it'll parallelize one, two, and three
[124:33] and then recombine the inputs or
[124:35] something for some API call. Uh the
[124:37] options here are virtually limitless. Um
[124:38] but because they don't guess or
[124:40] hallucinate, you can just incrementally
[124:41] improve these things over time. I had
[124:42] this question come up the other day, so
[124:44] I figured I'd answer it in this course.
[124:45] Um, nothing says you can't actually use
[124:47] AI inside of your scripts. For instance,
[124:49] you might have a thing called process
[124:53] leads with,
[124:56] you know, claude. py that, uh, I don't
[124:59] know, it feeds in a bunch of leads or
[125:01] grabs the leads from like a Google doc
[125:02] or something or Google sheet and then it
[125:05] just like passes them all through Claude
[125:06] and has you tell something about each
[125:07] lead. I don't know, whatever the heck
[125:09] you want this to say. Well, you can
[125:10] still use AI to do that for you, right?
[125:12] It's still passing it into Claude. It's
[125:14] just doing so in a much more predictable
[125:16] way because you are defining it within a
[125:18] single workflow as opposed to just like
[125:19] giving it full orchestrator access. Like
[125:21] for instance, your process leaves with
[125:22] Claude would probably start by like
[125:24] reading the sheet, right? That's
[125:25] probably what's going to happen under
[125:27] the hood. After you read the sheet,
[125:28] it'll then um send each row to Claude.
[125:33] Uh when you do that, you'll have like a
[125:35] specific prompt that is like deter, it's
[125:37] not deterministic, but it's as
[125:38] deterministic as possible. You know, you
[125:40] set the temperature really low. It like
[125:41] expects the same outputs for the same
[125:42] inputs and so on and so forth. After
[125:44] you're done with that, maybe you like
[125:46] add update
[125:49] to sheet or something. Um so you can
[125:52] call, you know, open AI anthropic Google
[125:54] at your whims. I do it all the time
[125:56] within my flows and actually is a pretty
[125:57] big chunk of how I do things. I also
[125:59] call like neural networks and stuff like
[126:00] that. I use various libraries. Uh you
[126:02] don't have to just you know do it all
[126:04] with old school Python automation. I
[126:05] guess the point that I'm trying to make
[126:06] is just make these execution scripts
[126:07] very atomic. Make them do one thing and
[126:09] just make them as deterministic as
[126:11] possible. Um this will significantly
[126:12] improve the quality of your end result.
[126:14] So why does this do model work? It works
[126:15] because it plays to everybody's
[126:16] strengths. When you do not constrain the
[126:18] outputs of LLMs, they're really
[126:19] unpredictable, right? They'll try
[126:21] anything and when they fail, they fail
[126:23] spectacularly. And it might be like they
[126:24] work 80% of the time, but the 20% of the
[126:26] time they don't. They will like blow up
[126:27] a building or something. Uh, pre-built
[126:30] tools replace the construction of tools
[126:33] on the fly. Because the LLM is running
[126:35] pre-built tools, it doesn't have to make
[126:37] them from scratch every time, which
[126:38] reduces the total number of steps that
[126:39] you have to take to get there. A really
[126:41] simple analogy for this is imagine if
[126:43] you just gave somebody a recipe versus
[126:45] asking them to invent a new dish every
[126:46] time. Like if I just said, hey, can you
[126:48] make that paella recipe that you've been
[126:50] making me recently? The likelihood that
[126:51] I'm going to get the PA recipe I want is
[126:54] probably a lot higher than if I just
[126:56] have it, you know, go off the cuff every
[126:57] single time. it will know the flavoring,
[127:00] the ratio of ingredients I like, the
[127:02] various steps that it takes, how to put
[127:04] the muscles in, I don't know, just tons
[127:05] of stuff. Whereas, you know, every time
[127:07] it invents this new dish, this new pa of
[127:10] 3.0, obviously, it's just like going off
[127:11] of its own biases and randomness at that
[127:14] particular moment. So, in addition to
[127:16] directives and executions, we also have
[127:17] two essential configuration files. And
[127:19] it's actually in practice a little more
[127:20] than two, but I just call it two because
[127:22] it's a system prompt and then it's an
[127:23] env. um agents.mmd contain the
[127:26] instructions injected at the start of
[127:27] every conversation with the
[127:28] orchestrator. Now these are named
[127:30] according to your um ID environment. So
[127:32] this could be cloudMD, gemini.mmd or it
[127:34] could be whatever the heck it it asks
[127:36] for cursor.mmd whatnot. Um I would just
[127:38] always have like all of these
[127:39] simultaneously. The reason why is
[127:41] because if you just have all of them
[127:42] simultaneously you can just like move
[127:43] into any new IDE or any new agent or any
[127:46] new model and it'll just like
[127:47] immediately uh understand what you're
[127:49] saying. So in this way you could
[127:50] theoretically have like you know rate
[127:52] limits for your Gemini model um and then
[127:54] rate limits for your claude model and
[127:56] then rate limits for your open AI model
[127:58] and you just open all three of them in
[127:59] tabs and just have them all work on
[128:00] things to minimize the probability of
[128:02] you running over anything. Most models
[128:03] at this point are pretty similar. We've
[128:05] kind of converged to really really
[128:06] similar accuracy ratings and scores on
[128:08] stuff. So aside from preference and
[128:09] stuff, this is how you keep those costs
[128:11] low. In addition, your env file is where
[128:13] you store all your API keys and then
[128:14] your credentials. Um, what this ends up
[128:16] looking like for instance is just using
[128:18] that claude example earlier, uh, if we
[128:20] want AI to do something, we would
[128:21] actually have claude or rather anthropic
[128:24] API_key
[128:26] and then you just have like the the key
[128:28] itself right over here. Then over here
[128:30] you'd have like open AI
[128:33] API_key.
[128:36] Then you'd actually store that key over
[128:38] here as well. And you just like dump
[128:40] this. It would be a massive list of just
[128:41] all of like the credentials and keys
[128:42] that you'd ever want. your execution
[128:44] scripts instead of having to hardcode
[128:46] the key would just say, "Hey, go into
[128:47] ENV and then find it instead." And
[128:49] there's just like very simple programs
[128:51] that do that sort of thing for you. Just
[128:53] so we're all on the same page, what
[128:54] agents MD actually does is it acts as
[128:56] your persistent context. You inject this
[128:58] automatically every single time at the
[129:00] beginning of a session, so you just
[129:01] don't ever have to repeat yourself. It
[129:03] also explains the do framework structure
[129:05] to the orchestrator. So everything that
[129:06] I've done here, we are basically going
[129:08] to turn into an agents.mmd file and then
[129:10] just give to the orchestrator so it
[129:11] understands what is going on. we're
[129:13] going to give it to our agent and be
[129:14] like, "Hey, make sure to do it this way
[129:16] because it's reliable and because
[129:17] execution scripts are pretty
[129:18] deterministic and so on and so forth."
[129:20] So, it's really meta, right? Like
[129:21] everything I'm telling you right now,
[129:22] we're just going to tell to the agent.
[129:23] We're just going to do it in a very like
[129:24] context compressed way. This will also
[129:26] define the error handling behavior. The
[129:28] agent does not spiral when something
[129:29] breaks. And then obviously, what's
[129:30] really cool is you can actually just
[129:31] make your agents.mmd better and better
[129:32] and better. Like I find uh routine edge
[129:34] cases that I didn't handle for with my
[129:36] agents MD probably like once a week and
[129:38] then I just like add a line to it and
[129:39] then the next time like my model just
[129:40] doesn't make that mistake. I did not
[129:42] always self anneal for instance I just
[129:43] realized that huh there's some
[129:45] situations where my model solves the
[129:46] problem itself and then other situations
[129:48] where it comes to me for help why don't
[129:49] I just make it explicit hey man I want
[129:51] you to solve the problem for yourself
[129:52] that is what resulted in the self
[129:54] annealing concept all right so let's
[129:55] actually go and have AI set up directive
[129:57] orchestration execution for us I'll show
[129:59] you guys the system prompts
[130:00] agents.mmdenv
[130:02] and everything okay so let's actually
[130:04] build our very first real agentic
[130:06] workflow together the first thing you
[130:08] need to do is open up your IDE
[130:11] In my case, I'll be using Visual Studio
[130:13] Code for this demo. Not because I think
[130:15] it's better than anti-gravity or
[130:16] anything like that, but just because I
[130:17] want to show you guys you could use
[130:18] whatever the heck you want. You know,
[130:19] it's all interoperable these days.
[130:21] Anyway, the very first thing we need to
[130:23] do is we need to create a new workspace.
[130:25] So, I'm going to head over here to the
[130:26] top lefthand corner and then I'm going
[130:28] to say
[130:30] open folder. From here, I'm going to at
[130:33] least on a Mac, click the new folder
[130:35] button. Then I'm going to say YouTube
[130:38] workspace. do then going to create. Once
[130:42] I'm in it, I'll click open.
[130:44] Next up, what we have to do is we have
[130:46] to create our system prompt file. I get
[130:50] a lot more into detail about these
[130:51] later, but for now, what I'll do is I'll
[130:54] open up this file. I'm going to type
[130:56] claude.md.
[130:58] I'm going to paste in one of the
[131:00] examples that you can get in the top
[131:02] link in the description. So, that is
[131:04] this my system prompt. Then going to
[131:07] save. The next thing I'm going to do,
[131:10] I'm assuming you've already downloaded
[131:11] Claude Code. If not, you head over here
[131:13] to extensions, type, you know, in this
[131:15] case, Claude Code, but realistically,
[131:17] whatever model you want. Give that
[131:18] button a click, click install over here.
[131:21] You're going to need to sign in and all
[131:22] that stuff. But assuming you have your
[131:24] own key, and assuming you have your own
[131:26] um account set up on at least, you know,
[131:28] a $10 or $20 a month plan, you're good.
[131:30] I'm then going to go to the top right
[131:32] hand corner here, click this little
[131:33] claude code button, and now I'm just
[131:36] going to move back a bit and start
[131:38] asking it to help me. Now, what I want
[131:40] to do is I want to build a simple email
[131:42] onboarding flow. Essentially, when
[131:45] somebody joins my organization as a
[131:47] client, I want to send them a brief
[131:49] email saying, "Hey, thanks so much for
[131:51] joining. Really looking forward to
[131:53] having you." And you know, here's a link
[131:55] to a kickoff call that you can schedule.
[131:57] This is a super easy and straightforward
[131:59] thing to do. And you can of course set
[132:00] up systems to do this outside of Agentic
[132:03] workflows. I'm just showing you this
[132:04] because I think it's probably the most
[132:06] straightforward example to show you how
[132:08] to chain together three or four things
[132:09] that I can think of. We'll progressively
[132:12] design more and more complex workflows.
[132:14] But for now, what I need to do is I need
[132:16] to talk to this model. I need to have it
[132:17] do things. But if you notice on the
[132:20] lefth hand side, I don't actually have
[132:21] like the workspace itself set up. I just
[132:22] have this claw.md. So the very first
[132:24] thing I'm going to do is down here, I'm
[132:26] just going to go bypass permissions.
[132:28] Whatever model you're using probably has
[132:30] a bypass permissions mode nowadays. And
[132:32] I'm I'm just going to say set up my
[132:34] workspace in accordance with claw.md.
[132:38] I mean, I could have said whatever. I
[132:39] could have said just set my workspace up
[132:41] or something like that. What it's going
[132:43] to do is it's going to read through
[132:44] cloud.mmd. It's going to understand how
[132:46] this works and it's going to create a
[132:48] full directory structure based off that.
[132:50] now. Okay, it's adding a bunch of
[132:52] information web hook.m MDs talking about
[132:55] the deterministic and execution layers
[132:58] and so on and so forth. Now it's going
[133:00] to go through and verify the final
[133:01] setup. And now it's giving me a brief
[133:04] summary. Okay, great. Now that I have
[133:06] this set up, I want to show you guys how
[133:07] easy it is to actually build this
[133:08] workflow. All I'm going to do is I'm
[133:10] going to give it a very highle natural
[133:12] language instruction of what I want.
[133:14] Hey, I'd like to build a brief
[133:16] onboarding workflow. Basically, I want
[133:18] to be able to tell you onboard client
[133:21] email@acample.com
[133:23] and then have you send an email to that
[133:26] new client that introduces them to our
[133:28] company, gives them some background, and
[133:30] then invites them to a kickoff call
[133:32] using a calendar link.
[133:35] Then going to press enter. You'll notice
[133:37] that because I'm using my voice,
[133:38] sometimes this text is a little bit
[133:40] misformatted. That's okay. Doesn't need
[133:42] to be perfect. This model is smart
[133:44] enough to understand what's going on.
[133:46] >> [snorts]
[133:46] >> It's going to ask me some questions.
[133:47] What should I use to send emails? SMTP,
[133:50] resend, send grid, whatever. What's the
[133:52] company info? What's the URL? Now, I
[133:55] need to obviously go and I need to get
[133:56] this information, come back to it. But I
[133:58] should know that I don't even need to
[133:59] like know for sure. Hopefully, it's
[134:01] clear. I just want to like send through
[134:02] my own Gmail account. So, I'm just going
[134:04] to say, sorry, I don't know what any of
[134:06] that means. I just want to send a
[134:08] welcome email from my Gmail account.
[134:11] And I'm going to provide it my own.com.
[134:17] For company info, I'll just give you a
[134:19] brief list of bullet points whenever you
[134:22] send the email.
[134:26] And underneath for the calendar link,
[134:28] just use an example calendar link for
[134:30] now.
[134:32] Cool. I'm giving it some highle
[134:34] instructions here, and it's going to
[134:36] help and walk both of us through the
[134:38] finishing of this workflow.
[134:40] The first thing it will do is if we open
[134:42] up our directives folder, it'll build
[134:45] this onboard_client.mmd.
[134:50] If I go up here, you can see there's now
[134:51] an onboardclient.md
[134:53] with a bunch of highle directives with
[134:55] this information.
[134:57] Now, you'll see that it's installing
[134:59] dependencies and so on and so forth. It
[135:01] doesn't fully understand what to do
[135:03] here, but that's okay. Okay, what it's
[135:04] doing next is it's walking us through a
[135:07] one-time setup with our Google
[135:09] information. So, what I'm going to do is
[135:11] I'm just going to create a new app
[135:12] specific password. Let's just call it
[135:14] YouTube example. And then going to go
[135:17] over here. I'm going to paste this in.
[135:19] This is now going to take the app
[135:21] password and actually use it to update
[135:22] the env file.
[135:26] Says the app password saved. We're all
[135:27] set. First, I'm going to ask it what
[135:29] does the onboarding email look like.
[135:32] This looks pretty reasonable. I'm now
[135:34] going to go through and then edit this
[135:35] template so that we could send what I
[135:37] think is a higher quality template every
[135:38] time. Okay, just spend a few moments
[135:41] here putting together this onboarding
[135:43] email. It says, "Hi, name. Thanks for
[135:45] choosing to work with us. We're excited
[135:46] to have you on board." Here's what
[135:48] happens next. We hop on a quick kickoff
[135:49] call to align on goals. You meet the
[135:51] team and get synced with your project
[135:52] manager. From there, we'll map out a
[135:54] plan tailored to you and finally receive
[135:56] daily updates when the project is
[135:57] complete. Book your kickoff call here.
[136:00] Very straightforward template. I
[136:01] basically just want this to send every
[136:03] single time. So, it's just going to go
[136:04] and update the directive and presumably
[136:06] the execution to always reflect this
[136:08] information. And then finally, I'm just
[136:10] going to say onboard nick at
[136:13] nickleclick.ai.
[136:15] And at the end of it, you could see we
[136:17] now have a really well formatted and
[136:19] simple onboarding email. This whole
[136:22] workflow only took me a few seconds to
[136:24] put together. Hopefully you guys see the
[136:26] power for nontechnical people, even
[136:28] people that don't understand what app
[136:29] keys are or env tokens or anything like
[136:33] that to actually meaningfully integrate
[136:35] with software that we're using. All
[136:36] right, so now that we've seen a little
[136:37] bit about how to set things up, how do
[136:38] you actually go and create like really
[136:39] good directives? Well, you need four
[136:41] things. You need a clear objective
[136:42] statement, aka what this directive does.
[136:45] You need some form of input
[136:46] specification, so what data does the
[136:48] agent need to actually get started? You
[136:50] need a step-by-step process, which is a
[136:52] sequence of operations, scripts, and
[136:53] expected outputs in natural language.
[136:55] And then you also need a definition of
[136:57] done. So that's quality criteria. How do
[136:59] you know that the agent has actually
[137:00] succeeded? It needs to be able to grade
[137:02] itself based on its output. For
[137:03] instance, like you'll know you're
[137:05] successful when you have a Google Sheet
[137:06] link URL with at least 100 rows filled
[137:09] in, something like that. You should
[137:10] also, of course, include edge cases. So
[137:12] any known exceptions, if there are
[137:13] quirks with an API, if there are things
[137:15] that come out as error codes that should
[137:17] not come out as error codes, if they
[137:18] have common failure modes, you should
[137:20] actually include all of that in the
[137:21] directive. Uh you should also describe
[137:23] fallback behavior like, hey, if the
[137:25] Apollo scraper we're using fails, try
[137:27] the instantly lead uh enrichment tool
[137:29] instead. And unlike old automations, you
[137:32] don't have to like build this massive
[137:33] complicated error handling function.
[137:35] Unlike naden or make.com or any of these
[137:38] visual coding tools, you don't actually
[137:39] have to go through and like create these
[137:41] error handling flows. You you just add
[137:42] one line and you're like, "Hey, if this
[137:44] happens, then do this." And it's so much
[137:45] simpler. It also includes some sort of
[137:47] instructions saying what to return if
[137:49] everything fails gracefully. Like a lot
[137:51] of um systems do fail really gracefully.
[137:53] They don't even really tell you that
[137:54] they fail. If you expect a 100 leads to
[137:56] pop up or 100 YouTube videos to come
[137:57] from your YouTube video scraper or
[137:59] whatever, you know, like one will uh
[138:01] it'll technically have done so
[138:02] correctly, but you know, nothing will
[138:04] have errored out. So there's no real
[138:06] built-in way for the model to know
[138:07] unless you make it hyper explicit what
[138:09] happens if things go to plan. That's why
[138:12] you need a definition of done. And then
[138:13] you also need something to say like,
[138:15] hey, if this does fail gracefully, if
[138:16] we're under 100 records, let's say if
[138:18] that's our minimum, um, rerun it over
[138:20] and over and over again with wider
[138:22] filters until we get to 100. don't
[138:23] return this to the user until we have at
[138:25] least whatever he put in. All right, for
[138:27] my next system, I basically want to
[138:28] build a CRM manager for ClickUp. ClickUp
[138:32] is one of many CRM tools that you could
[138:34] use. I really like it because I think
[138:36] it's simple, it's fast, and then it
[138:37] includes a bunch of functionality that
[138:40] weaves together different tools like it
[138:42] has built-in messaging. Um, it obviously
[138:45] has documents. I could store my
[138:46] knowledge bases in here and so on and so
[138:48] forth. But I want you to know the
[138:50] specific tool doesn't really matter at
[138:51] all. You can build this sort of thing
[138:53] out in basically any CRM so long as it
[138:55] has the ability to connect via API and
[138:57] MCP and that sort of stuff. So basically
[139:00] what I have here is I have a really
[139:01] simple CRM setup called template
[139:03] creative agency. I'm going to pretend
[139:04] I'm a creative agency here. You can see
[139:06] there's a sales pipeline. Inside of the
[139:09] sales pipeline, I have people like Nick
[139:11] Sarif and Peter Jackson and Peter Smith,
[139:14] Peter Jackson, Sally Lozen, her last
[139:16] name's Lozen, Koth Arllan, and so on and
[139:18] so forth. Basically stored um on this
[139:20] cool little table. And what happens like
[139:22] any CRM is people come in through this
[139:24] intake stage like
[139:29] Bast Sarif and then um essentially they
[139:32] are assigned a status. Then as they are
[139:34] updated, I move them to things like
[139:36] meeting booked and then proposal sent
[139:38] and close lost or closed one. Uh
[139:40] depending on whether or not they accept
[139:41] the contract. However, I don't really
[139:43] want to interact with it manually
[139:45] anymore. I think it'd be really cool if
[139:46] I could weave this into other workflows
[139:49] like our onboarding workflow that we
[139:50] made earlier. So, how do I do this? I'm
[139:52] just going to ask it to build this for
[139:53] me. I'd like you to be a wrapper around
[139:56] my ClickUp CRM. I want to be able to ask
[139:58] you to do anything inside of ClickUp,
[140:00] then have you automate the process for
[140:02] me. This will also allow us to connect
[140:04] to other workflows that we build around
[140:06] my agency. All of the CRM information is
[140:10] stored inside of the
[140:13] and let me head back over here and let's
[140:16] see what it's called. Template creative
[140:17] agency space.
[140:22] Give me three ways we could do this.
[140:24] Okay, it's now going to create me
[140:26] everything that I need. The first option
[140:28] is a direct script library. It'll create
[140:31] a set of execution scripts for common
[140:33] ClickUp operations with a master
[140:34] directive that routes requests. That's
[140:36] pretty cool. I would have to invoke it
[140:38] every time. Then there's some sort of
[140:40] conversational idea. Then there's also a
[140:43] web hook bridge. I like the idea of
[140:46] number one. I want to see if there's a
[140:47] simpler way to do this. Is there any
[140:49] simpler way to do this? Like is there an
[140:51] MCP or just anything that wouldn't
[140:53] require us building a specific step for
[140:55] every request?
[140:57] It's going to go through and reason
[140:59] first. So, it's going to check to see
[141:00] whether or not there is anything out
[141:02] there that would allow us to do this
[141:03] more easily. What it's doing here is
[141:05] it's using a web search sub agent.
[141:07] Believe it or not, we're going to talk a
[141:08] lot more about sub agents later, but sub
[141:10] aents have pros and cons. When you use
[141:12] sub agents, things typically take a lot
[141:14] longer to finish, but the pro is you
[141:16] isolate the context. And um what that
[141:19] means is you just don't need to worry
[141:20] about inserting all this stuff into the
[141:22] main flow. Cool. So, this is sort of
[141:25] what I wanted to do initially. kind of
[141:27] cheating here, but I know MCP is just a
[141:29] simple and easy way that I could build
[141:31] something like this. And I'll show you
[141:32] guys more about this later. But as we
[141:34] see here, there's an official and then
[141:36] there's also a nonofficial one. What I'm
[141:38] going to do is I'll say, "Hey, let's do
[141:41] the official. How do I get my API
[141:43] token?"
[141:47] Okay, it's giving me some instructions
[141:49] here. So, I'm going to head over here. I
[141:51] just need to regenerate this API token.
[141:54] So, first I have to put my password in.
[141:55] Just bear with me.
[141:58] Next, I'm going to copy this token over.
[142:00] And then I'm just going to head over
[142:01] here and paste it. One thing that you'll
[142:03] find that models do pretty often is, and
[142:06] I don't know if this is because they
[142:07] want to conserve on their own token
[142:08] usage or something, instead of just
[142:10] doing the thing for you, often times
[142:12] they will say, "Hey, I'm going to find
[142:13] information on how you can do the
[142:14] thing." What is super super powerful is
[142:17] just to say, "Okay, great. Do it. Looks
[142:19] like we need some more information
[142:21] here." So, we need to go to ClickUp in
[142:23] our browser, look at the URL, and then
[142:24] get the team ID.
[142:28] I see it right over there. Let me just
[142:30] paste it in. Okay. And now all I need to
[142:33] do is just restart Claude Code. So, let
[142:34] me click this little X, head over here
[142:37] again. I double tap on the page in order
[142:39] to create that new file.
[142:42] Okay. And now I have an MCP. So, let me
[142:44] just give that a click. When you type
[142:46] back SLMCP, you can now see the MCP
[142:48] servers you have. and I'll say,
[142:51] "Awesome. Can you create a new record
[142:53] for me?"
[142:58] So, because this is an MCP, it's like a
[143:00] general solution. It's not a specific
[143:01] solution. We need to insert some
[143:03] information about this. So, what type of
[143:05] record? Where should it go? I'd like you
[143:07] to act essentially as my ClickUp
[143:10] wrapper.
[143:12] Keep in mind that this is a new
[143:13] instance. So, I need to provide it some
[143:14] highle instructions. again.
[143:22] So all conversations are going to be
[143:25] related to that space.
[143:28] I'd like you to store this information
[143:30] somewhere. That way the next time I ask
[143:31] you to do this, you'll do it the first
[143:33] time.
[143:35] Go and learn about the space first.
[143:39] New lead, Peter Rockwell.
[143:45] Okay. And now what it's doing when I say
[143:48] new lead Peter Rockwell, it is creating
[143:50] a lead in that space. Pretty
[143:52] straightforward. Let's go check and make
[143:53] sure that it's good. And as you can see
[143:55] here, we now have a meeting URL link as
[143:57] well as a status of meeting booked.
[143:59] Hopefully, it's clear. I could talk all
[144:01] day about this and give this all of the
[144:03] information that I want in order to have
[144:05] it, you know, manage my uh ClickUp CRM
[144:08] for me. So, that's one way to do so with
[144:09] an MCP, which is really straightforward
[144:11] and it's super simple. Let me show you
[144:13] another way we can do this just using
[144:14] like the ClickUp API instead. So I'm
[144:17] just going to exit out of this and then
[144:18] create a new cloud code instance. I'm
[144:21] going to say, hey, can you uninstall the
[144:23] ClickUp MCP and remove anything in our
[144:25] environment that has to do with ClickUp?
[144:27] I'm doing a demo.
[144:29] Then going to bypass permissions. So I
[144:31] just don't have to worry about it. It's
[144:32] just going to do it all for me. Hey, I'd
[144:34] like you to build a series of ClickUp
[144:36] directives so that I could automate the
[144:38] process of adding records, updating
[144:41] them, and so on and so forth. I
[144:43] basically want you to act as my ClickUp
[144:45] wrapper. I want to do this via API
[144:47] calls. We previously tried MCP, but I'm
[144:50] doing a demo and I just want to do this
[144:51] via API instead. Okay, it's now building
[144:54] this out systematically. So, it's going
[144:56] to start by building a base ClickUp API
[144:58] client. It's then going to create CRUD
[145:00] scripts to create, get, update, delete.
[145:03] So, I'm going to create directives for
[145:04] each operation. Then, finally, it's
[145:06] going to update my env template. It says
[145:08] with a ClickUp API key placeholder. Um,
[145:10] I did just remove it, so I'm going to
[145:11] have to add that in again most likely.
[145:13] What's really cool is I know nothing
[145:14] about any of this stuff, and it's just
[145:16] doing it all completely automatically
[145:17] right now. It's writing all the
[145:19] directives, all the executions,
[145:20] literally everything that I need. And
[145:21] so, the reason why I'm showing you
[145:23] multiple different ways to do things is
[145:24] because there almost always are multiple
[145:26] different ways to do things. And with AI
[145:28] and agentic workflow builders like this,
[145:31] it's not necessarily that one approach
[145:33] is better than the other. Sometimes I'll
[145:35] try an approach and for whatever reason,
[145:36] whether the API isn't cooperating or
[145:39] it's just not very logistically
[145:40] reasonable, I will abandon it halfway
[145:43] and then just do another one. There's no
[145:44] reason why I have to commit to something
[145:46] that isn't working. And I can always
[145:48] change things. Nowadays, the barrier
[145:50] isn't really whether or not it's
[145:51] possible. The barrier is basically just,
[145:53] hey, how much time do I want to spend
[145:55] guiding or steering the ship in order to
[145:57] get this thing done for me. Okay, it's
[145:59] now going through adding all the
[146:00] information that we need. I gave it the
[146:02] API key as you guys could see above.
[146:04] It's going to essentially loop over as
[146:06] many times as it takes because of what
[146:08] is in the cloud MD. Eventually, it will
[146:11] um, you know, solve its own problems
[146:13] through a process called self annealing.
[146:14] And then we'll be able to do things like
[146:16] create tasks, delete them, update them,
[146:18] and so on and so forth. So, it's just
[146:20] running through and testing all of the
[146:21] various scripts that it put together.
[146:23] The creating of a task, the deleting,
[146:26] the cleaning up, so on and so forth. So,
[146:28] let me give it some more highle
[146:30] instructions just to tell it I really
[146:31] wanted to work within that template
[146:33] creative agency uh uh space. I'd like
[146:36] you to do all of your tasks solely in
[146:39] the template creative agency space.
[146:44] Update everything to reflect this. Then
[146:50] whatever you need to in order to reflect
[146:53] this. Then create a new lead called Nick
[146:56] Sar.
[146:58] Cool. Looks like it already knows what
[147:00] it needs to do. So now it's going to
[147:02] create the lead. And you can see it's
[147:03] even given me a link to the lead so that
[147:05] I can pull it up and see it for myself,
[147:06] which is pretty cool. Awesome. Why don't
[147:09] we see if this has access to some other
[147:10] fields? Do you have access to custom
[147:12] fields? Okay. First, it's going to see
[147:15] the custom fields in this list. It's
[147:17] then going to see if we could set the
[147:18] appropriate one. Nice. That's pretty
[147:20] cool. So, whereas the other one could
[147:22] not set custom fields, um, this one can
[147:24] set custom fields, which is pretty
[147:25] sweet. As you guys could see, sometimes
[147:27] there's pros or cons to different
[147:28] approaches. This one was really awesome.
[147:30] So, to be honest, I now basically have
[147:32] like a whole CRM manager. Great. Delete
[147:35] the record. That was just for demo.
[147:39] I'd personally say having some sort of
[147:41] CRM wrapper like this now with the power
[147:43] of current technology is like a
[147:45] non-negotiable. This thing just makes
[147:46] our lives so much easier. And what's
[147:48] really cool is we could weave flows in
[147:50] together. So when somebody becomes a new
[147:52] client, for instance, we could then
[147:53] automatically send that onboarding flow,
[147:55] then maybe even reflect that by adding a
[147:57] comment or something like this. These
[147:59] things will supercharge any CRM very
[148:01] very quickly. Okay, I want to talk a
[148:03] little bit about cloud skills. Um, this
[148:04] is really similar to DO like we just ted
[148:06] chatted about, but it is specific to the
[148:08] cloud family of models. So you can't use
[148:10] the same cloud skills structure that I'm
[148:12] about to show you in like Gemini or
[148:14] OpenAI or or GPT 5.2 or whatever. It's
[148:17] very very specific to Claude. That said,
[148:19] you know, all of these model families
[148:21] now have their own versions of this. So
[148:22] I wanted to cover probably like the most
[148:24] popular one just so we're all on the
[148:25] same page. I care a lot about
[148:26] interpretability and modularity. So I
[148:29] want to be able to use the same workflow
[148:30] setup in, you know, model A versus model
[148:33] B versus model C. Um cloud skills are
[148:35] obviously hyperspecific to anthropics
[148:37] model. Now, this was their attempt to
[148:39] standardize Agentic workflows into
[148:41] reusable portable packages. And just
[148:43] like DO, it's a folder structure. It
[148:45] contains instructions, scripts, prompts,
[148:47] and resources that Claude will load
[148:48] every time you call something. So, it's
[148:51] just a slightly different folder
[148:52] structure that includes a file called a
[148:54] skill.md. And I'm going to run you
[148:55] through that in a moment. The way that
[148:56] skills work in a nutshell is just ignore
[148:58] the lefth hand side of this graph cuz I
[149:00] think this is a little more complicated
[149:01] than we probably need right now. But
[149:02] basically, you have your agent and your
[149:04] agent organizes things into these skills
[149:07] folders. And so, it's a skills folders
[149:09] slash whatever the the skill um that you
[149:11] want it to to know is. So, in this case,
[149:14] there's a skill called big query. Then,
[149:16] you'll see there's a capital skill.md
[149:18] with a data sources.md, a rules.md. Over
[149:21] here, there's an NDA review, which
[149:23] includes a skill.md. The skill.md is
[149:25] just your directive, right? And you'll
[149:26] notice that because it's in markdown.
[149:28] Everything else here is entirely up to
[149:30] you. And so it's sort of like a loose
[149:31] framework right now where people are
[149:32] just dumping in whatever the heck they
[149:34] want the agent to have access to. It's
[149:35] also just a form to uh a way that you
[149:37] can modularize things. And basically
[149:38] what you'll do is you'll just have like
[149:40] a big list a big directory called
[149:42] skills. Then underneath that you will
[149:44] have things like you know hey uh let's
[149:47] do big query. Let's do one called docx.
[149:50] Let's do one called pdf. Let's do one
[149:52] called I don't know scrape leads. And
[149:55] each of these are going to be folders um
[149:57] themselves. So very similar to do. just
[150:00] takes a slightly different approach.
[150:01] Instead of having like the executables
[150:03] and like the scripts and stuff like that
[150:05] stored in other folders like an
[150:07] execution scripts folder, um it just
[150:09] stores it all in the exact same one. The
[150:10] way I treat things is as an instruction
[150:12] manual that Claude reads first. There's
[150:15] one slight difference between the way
[150:16] that the markdown file is written in so
[150:18] far that um it uses what's called YAML
[150:20] front matter. YAML just stands for yet
[150:22] another markup language by the way,
[150:23] which is really funny. There's like a
[150:24] million different ways to do this.
[150:25] Basically what this is is this is like a
[150:27] short I don't know 100 character 200
[150:30] character description of what the skill
[150:32] does. Um so as opposed to with you know
[150:34] the directive orchestration execution
[150:36] framework you know I don't usually use
[150:37] YAML I just like have it whip it up
[150:39] although YAML I think would be an
[150:40] improvement. Um you know instead of just
[150:43] naming something really descriptively
[150:44] what this does is actually just provides
[150:45] some context. Hey this script does X Y
[150:48] and Z. Hey this uh skill asks for this
[150:51] thing. And then you know what'll happen
[150:53] is upon runtime claude will load the
[150:56] skill based on whatever task you're
[150:57] asking to perform just based off of the
[151:00] YAML front matter which just means it
[151:01] saves a lot of tokens. It doesn't have
[151:02] to read the whole thing. So this is just
[151:04] a small block of metadata at the top of
[151:06] the file. There's like a name field,
[151:08] there's a description field, and then
[151:11] there's a purpose field and I'll show
[151:12] you an actual concrete example in a
[151:14] second. And then it's like kind of
[151:16] separated like this. And then when the
[151:17] agent loads the file um to actually like
[151:19] search through your skills, you say,
[151:20] "Hey, you know, I want you to scrape
[151:21] some leads." It'll actually just load
[151:23] this. So, it's way way shorter. Small
[151:26] metadata allows it to, you know, only
[151:28] load a few hundred characters at a time
[151:29] as opposed to big chunks. It allows it
[151:31] to understand what the skill does
[151:32] without reading the whole thing. Now,
[151:33] there's also a big library of pre-built
[151:35] skills right now for common tasks,
[151:37] mostly relating to documents. Um, and
[151:38] these are just skills that have been
[151:40] like hyper optimized over the course of
[151:41] tens of thousands of runs. You can think
[151:43] of them as execution scripts and
[151:45] directives that are just really, really,
[151:46] really self- annealed and they're just
[151:47] really, really powerful. So, we can do
[151:49] PDF creation, do word documents easily,
[151:51] Excel spreadsheets, PowerPoint
[151:53] presentations. The quality is
[151:54] surprisingly good. And because so many
[151:56] people have run these things because
[151:57] they've optimized the hell out of it,
[151:59] they tend to execute super quickly and
[152:00] then they also tend to be like pretty
[152:02] reliable. All right, let me show you
[152:03] some cloud skills in action. Let's talk
[152:04] about how to build things in cloud
[152:06] skills format instead of do format. I
[152:09] want you guys to see it's more or less
[152:10] the same thing. This is just highly
[152:11] cloudspecific. So I have a simple task
[152:14] in front of me here. I want to create a
[152:15] new cloud skill called generate- report.
[152:18] And I want this to build a weekly
[152:19] weather report with publicly available
[152:21] information from some API. I just
[152:24] Googled weather API. Pasted this in
[152:26] there. I don't even know if it's going
[152:26] to work, but we'll figure it out
[152:27] alongside each other. I also said I want
[152:29] a Canada specific just because I'm
[152:31] Canadian. I.e. this report should be all
[152:32] about the weather across Canada. Now the
[152:34] last thing I need is I need some sort of
[152:36] template. So I'm just going to go and
[152:37] I'm going to see if I could download a
[152:39] free report template.
[152:41] Let's see. It's going to open up a bunch
[152:43] of tabs. What do we got here? 2035
[152:45] annual report. That looks ridiculous.
[152:47] [gasps] Um, okay. This one looks pretty
[152:49] cool. Can I just download this whole
[152:50] thing? Okay. Anyway, I'm just going to
[152:52] go over to Canva here. And then I'm just
[152:55] going to download this as uh what are we
[152:58] going to do? PDF. Let's just do PDF.
[153:01] We'll do all pages. I'll click download.
[153:04] Once I have this, I'm then going to
[153:06] provide this file to Cloud Code.
[153:09] I have a template file in I'll just drag
[153:13] this over tot
[153:18] and I'll just call it uh
[153:22] orange and black modern annual report
[153:24] that I want you to use. Go. Awesome.
[153:29] So it's then going to pull that file and
[153:31] then it's going to because it knows how
[153:33] to generate cloud skills sort of
[153:34] natively go through the whole process.
[153:36] Okay. It's going through and then
[153:37] creating the skill directory structure.
[153:40] Uh it's then writing the skill MD with
[153:42] instructions. It's doing a fair amount
[153:43] of stuff. So I'm just head over to here
[153:44] to skills and then I'll see where this
[153:46] would be. Okay. Generate report right
[153:48] over here.
[153:51] Okay. And inside there's a skill.md.
[153:53] Then there's also a scripts folder. This
[153:55] is where we're going to insert the
[153:57] scripts. It's now going to go fetch a
[153:59] bunch of weather data. The cool thing
[154:01] about Claude skills is there's this
[154:04] little YAML front matter. It's called Y
[154:07] A ML and then front matter is just
[154:10] everything that's between these three
[154:11] dashes. And here we have the name, a
[154:13] brief description, and then also some
[154:15] allowed tools, which is really cool. So
[154:17] you can get very granular with how you
[154:18] give your agent access to these
[154:21] workflows. And then what's cool is they
[154:23] only actually um load this into context
[154:26] before deciding on which skill to use.
[154:28] So that way you save a fair amount of
[154:30] tokens because it doesn't have to like
[154:31] read every single file, right? Okay, I'm
[154:34] then going to get an API key payment.
[154:37] Okay, it looks like open weather map is
[154:39] not free despite it saying that it is
[154:41] free. I need to sign up and then enter
[154:42] some payment information. So don't use
[154:44] that. U what I've done here is I've just
[154:46] said, hey, it's not free. So find a
[154:48] source that is free. So now it's going
[154:49] to go and it's going to find me
[154:50] something that is realistically. Looks
[154:52] like it found an alternative source
[154:53] called open- so it's just going to
[154:55] rewrite it with that information in
[154:57] mind. Now that it's done a little bit of
[154:59] work, what it's doing is just testing
[155:00] this skill. Okay, looks like it has now
[155:02] generated me a file. Let's just say open
[155:06] PDF.
[155:09] Cool. And now we have it. So, Canada
[155:11] weekly weather 2025, table of contents,
[155:14] national overview, weather highlights,
[155:16] west coast prairie, central Canada. So,
[155:19] you guys can see it is very, very easy
[155:21] to create a template using a PDF. Just
[155:24] drag and drop that puppy in. And then
[155:25] boom, you now have native intelligence
[155:27] that is capable of interacting with
[155:28] tools like this to generate honestly a
[155:31] very clean and very sexy proposal
[155:35] document. Pretty straightforward, huh?
[155:38] So, I mean like this is just one of many
[155:39] asset generation workflows that you
[155:41] could do. Um, hopefully you guys see you
[155:42] could now like generate proposals in a
[155:44] flash. You could generate any PDF in a
[155:46] flash, customized assets or slide decks
[155:48] or whatever the heck you want. um it
[155:49] really only takes a data source, the
[155:52] template itself and then you waiting
[155:54] around 5 minutes or so as it self
[155:55] anneals and then generates. Let's talk a
[155:57] little bit about model context protocol.
[155:59] So this is essentially a USB for AI. The
[156:03] idea is that it is a universal adapter
[156:05] that lets any assistant whatever model
[156:08] family connect to any data source
[156:11] interoperably. Now when I say USB um a
[156:14] while back you had so many different
[156:15] types of USBs. You had like a USB 1, you
[156:18] had a USB 2, you had a USBA,
[156:21] a USB. I don't actually know if this
[156:24] one's real, but you had like hundreds of
[156:25] different types of USB configurations,
[156:27] basically hundreds of different cables.
[156:29] And then um eventually somebody made a
[156:31] USBC and they realized that this is just
[156:33] like the superior format and then they
[156:35] made either regulations depending on
[156:37] where you live or just heavily
[156:38] incentivized the market to just produce
[156:40] USBC's because USBC's if we all just
[156:43] standardize to one adapter means that
[156:44] like I could just buy any device and
[156:46] then I could just slot that into any
[156:48] other device and it would just work. I
[156:49] don't have to carry around 20 different
[156:50] types of cables. I just know that this
[156:52] sort of adapter function is just going
[156:53] to make everything work and uh it's
[156:55] going to be super easy and more
[156:56] convenient. That's essentially just what
[156:58] MCP is. We're just doing that for our AI
[157:00] agents. This was introduced by Enthropic
[157:02] back in November 2024. It's a
[157:03] standardized way for AI assistants to
[157:05] connect to any external data and tools.
[157:07] And this isn't just Claude to be clear.
[157:08] Um they just made this for everybody. So
[157:10] this works with, you know, like the
[157:11] OpenAI family of models. This works with
[157:13] the Gemini family models. The whole idea
[157:15] is it just eliminates the need for those
[157:17] custom USBs for every connection. Just a
[157:19] universal translator. It's like imagine
[157:21] there was some language that you know
[157:23] anybody on planet earth could speak and
[157:25] you know when you meet a person who
[157:26] doesn't speak the other language that
[157:28] you speak you just all use the same
[157:29] language it's espironto or whatever but
[157:31] it's for um you know AI agents that's
[157:33] basically it there are two main pieces
[157:34] to understand there are MCP clients on
[157:36] one hand and then there are MCP servers
[157:38] on the other hand so you know these
[157:40] clients are basically our AI apps so
[157:43] these are our things like anti-gravity
[157:46] these are our VS codes and these are
[157:50] also are things like uh I don't know
[157:52] clawed desktop
[157:54] these are things like you know chat GPT
[157:58] and basically what these are is you
[158:00] remember how earlier in the course I
[158:01] said that chats are just like the
[158:02] interfaces that agents are using right
[158:04] now they're sort of borrowing them
[158:05] because we don't have a better interface
[158:07] well that's essentially all a client is
[158:09] it's just an interface so the client is
[158:10] the tool that houses the agent right
[158:12] it's the shell around it and what this
[158:15] does is it connects to servers and these
[158:18] servers are based on specific tools. So
[158:21] for instance, there is an Appify MCP
[158:23] server. In addition to an Appify MCP,
[158:26] there's like an Apollo MCP.
[158:29] There is a I don't know Google Drive
[158:31] MCP. There's a Sheets MCP.
[158:35] And the point is whatever client you're
[158:37] using at the time, so maybe anti-gravity
[158:39] in this case, just calls the specific
[158:42] MCP whose configuration files you
[158:44] include in your workspace. So in
[158:47] anti-gravity I might have you know an
[158:49] appy mcp drive mcp and sheets mcp and
[158:52] then what I do is I just say hey can you
[158:54] you know look at my drive for whatever
[158:56] file and then turn that into a big CSV
[158:58] and then can you feed that CSV into appy
[159:00] and you know assuming that these three
[159:02] MCPS are good because there's a lot of
[159:04] quality variance in MCPS right now um it
[159:06] can actually do what you want it to do
[159:08] you can also store highle directives
[159:10] that explain how to chain these together
[159:11] even more in-depthly and more reliably
[159:14] and then the MCPS are essentially ally
[159:16] just your execution scripts. Right now
[159:18] there are three main ways that MCP
[159:20] servers communicate with MCP clients.
[159:22] There are resources which are structured
[159:23] data like documents, code, database
[159:25] records and so on and so forth. Then
[159:27] there are tools which are functions that
[159:28] your agent can call. These are analogous
[159:30] to execution scripts on our end. And
[159:32] then there are prompts which are
[159:33] basically just like system prompts for
[159:35] specific things. They guide how the
[159:37] model should interact with specific
[159:38] server. Hey, you should use this uh
[159:40] execution script when you want to do
[159:42] this function. Hey, you should call this
[159:44] resource. You shouldn't pagionate all of
[159:46] them. You should only call the first 50
[159:48] lines. This just is like highle
[159:49] instructions that help the model do
[159:50] things more reliably. The whole idea of
[159:52] MCP is really just to make the entire
[159:55] internet web accessible to our agents.
[159:59] Every tool gets its own MCP server. What
[160:02] your agent does is it only loads the
[160:05] ones that you absolutely need. This
[160:08] means you never have to build custom
[160:10] tools from scratch. though I think it is
[160:13] pretty easy and pretty great to get
[160:14] yourself that functionality and you get
[160:17] to give your agent breadth out of the
[160:18] box with very little effort on your
[160:20] part. In addition, you can also build
[160:22] your own custom MCP servers. The value
[160:26] here is not only are you going to have
[160:28] your own agent use it, of course, you
[160:30] could share it with other people. And by
[160:32] sharing it with other people, you can
[160:34] either ask them to either pay you or
[160:35] something to build the MCP server or,
[160:38] you know, let's say you're an API that
[160:39] builds an MCP server around your
[160:41] function, you can make things more
[160:43] accessible and then increase your
[160:45] company revenues. So, it's very very
[160:47] easy to build these things with AI
[160:48] assistance. When MCP came out, it was
[160:50] very difficult, but now it's super easy.
[160:52] I actually built one in 10 minutes the
[160:54] other day. I never read any MCP
[160:56] documentation and it did something
[160:58] really cool for me, which I may talk
[161:00] about in a future video. This means you
[161:01] can create specialized tools for
[161:03] specific workflow needs anytime that you
[161:05] want. And then if other people within,
[161:07] let's say, your organization want to use
[161:08] this or whatever, you just share the MCP
[161:10] server. Uh it's always going to work the
[161:12] same out of the box because it's the
[161:14] same server now. There are multiple
[161:15] people that can iterate and improve it,
[161:17] not just you. So the main question I get
[161:18] at this point is why don't we just use
[161:20] MCP for everything? Sounds great, right?
[161:23] Maybe we should. Well, the reason why is
[161:26] because MCP takes a lot of tokens. And
[161:28] the more context a model deals with, the
[161:31] dumber it gets. If you fed in the exact
[161:35] same prompt to two models, except prompt
[161:38] one said what you wanted it to say in, I
[161:41] don't know, 10 words, and prompt two
[161:43] said the exact same thing, but it wrote
[161:45] it really inefficiently and made it
[161:46] really, really, really, really long. The
[161:49] model would almost always perform better
[161:50] here. Maybe this would have a 99%
[161:54] success rate, whereas this would have an
[161:56] 85% success rate or something. What I
[161:58] mean to say is there's a very strong
[162:00] relationship between token count in
[162:04] context and then performance
[162:08] and this is improving as models get more
[162:09] intelligent but essentially performance
[162:12] as tokens go longer and longer and
[162:13] longer in the context almost always
[162:15] necessarily will decline. It's not
[162:18] exactly like this because usually when
[162:20] you provide more context, it's actually
[162:21] a little like bump until you get to a
[162:24] certain point and then it starts
[162:25] declining because it's like here we
[162:26] didn't really provide enough information
[162:27] for the model to know what's going on.
[162:29] Whereas here, maybe we provided a bunch
[162:30] of examples or whatever, which is why it
[162:32] does better. But inevitably, the longer
[162:34] that you um add a bunch of information
[162:35] that isn't relevant to your task, the
[162:37] more tokens that you have in that
[162:38] prompt, the crappier your outputs are
[162:40] going to be. And the issue with MCP is
[162:42] it actually loads pretty much all of its
[162:45] available functions into your agents
[162:46] context window. Now there are some
[162:49] developments that are fixing this. These
[162:50] are like at runtime MCP servers where um
[162:54] your AI just makes an intelligent
[162:56] determination about which MCP servers to
[162:58] load and stuff like this. But MCP as a
[163:01] framework is still pretty new and a lot
[163:02] of the MCP servers out there are pretty
[163:04] crappy. So regardless, we're loading a
[163:06] ton of tokens into a context window.
[163:09] Every function will have a name. They'll
[163:11] have a description. There'll also be a
[163:12] schema. This will be a few hundred
[163:14] tokens usually. And what that means is
[163:16] if you connect five servers and every
[163:18] server has 10 tools. So like if you
[163:20] connected to the drive server and then
[163:22] the drive server had I don't know get
[163:24] file. Okay, this is one of the functions
[163:27] or execution scripts. I don't know it
[163:29] has read file. It has share file and so
[163:34] on and so forth. Right? Every single one
[163:36] of these would have a name, description,
[163:38] schema, name, description, schema, name,
[163:40] description, schema. We're getting
[163:42] really high up in the tokens already,
[163:44] right? If you have 300 tokens per
[163:45] definition, even five servers with 10
[163:47] tools each means 15,000 tokens. And
[163:50] that's before you've done anything. So,
[163:52] it's like you're already on that graph
[163:53] that I showed you guys earlier, you
[163:54] know, if this is your performance when
[163:56] your token count is really low, you're
[163:57] probably already like down over here.
[163:59] You have some loss in percentage, which
[164:02] is just ultimately not efficient for
[164:04] business purposes. And you're probably
[164:05] wondering like, well, Nick, how bad is
[164:06] it really? What I want to do here is I
[164:08] just want to show you a quick example on
[164:10] some older models. And obviously, keep
[164:12] in mind that in order for us to do
[164:13] research on things, they necessarily
[164:14] have had to been out for a while. Um,
[164:16] but older models and how their accuracy
[164:18] on tasks scales with the number of
[164:21] documents in the input context. So
[164:23] number of documents in the input context
[164:24] is basically equivalent to tokens in
[164:26] this way. So I don't know just call the
[164:29] the number you know one document in this
[164:31] case is probably equal to like 1,000
[164:33] tokens or something like that. So as we
[164:36] see here at the very beginning when the
[164:37] context is quite small and we only have
[164:39] five documents in the input context. You
[164:41] know this um model here GBT3.5 turbo 16k
[164:44] performs very well. It performs maybe
[164:46] somewhere around 75% or so. The second
[164:48] we double that accuracy is now to
[164:51] slightly over 65%. We double that again
[164:53] and now it's almost down to 60%. And
[164:55] then if we 1.5x that, now it's like
[164:57] somewhere between 50 and 60%. So
[164:59] performance here really drops off
[165:01] extraordinarily quickly. And so to make
[165:02] a long story short, the reason why this
[165:04] happens is really similar to what I
[165:05] showed you guys earlier on in a demo
[165:07] where like if you just have one token
[165:09] and then you have three potential tokens
[165:11] here, you know, basically every single
[165:14] time you are forced to compute like the
[165:16] next token in a sequence, the total
[165:19] variance of the things that you could be
[165:21] generating just kind of go through the
[165:22] roof. And so that's that's what's
[165:24] occurring here. In order for you know
[165:26] this model to somehow know that the
[165:28] right answer is over here obviously it
[165:30] needs to somehow maintain some degree of
[165:32] accuracy and coherence. And that just
[165:33] becomes less and less and less and less
[165:35] likely uh the more tokens that you
[165:37] generate. Now obviously it doesn't
[165:38] happen this quickly. It happens over the
[165:40] course of many thousands of tokens
[165:41] nowadays. But back in the day when I was
[165:43] working with um just the base vanilla
[165:44] GPT2 the output quality was super
[165:47] sensitive to the number of tokens the
[165:48] input prompt. Like if you added an
[165:49] additional five tokens and those tokens
[165:51] were not very high quality tokens, they
[165:53] didn't really add a lot of value. Like
[165:55] accuracy would plunge off a cliff. Screw
[165:57] documents here. Pretend like we're just
[165:58] talking number of tokens. At five it
[166:01] might be 70, but at 10 it would
[166:02] literally jump down and so on and so
[166:04] forth. So anytime you try and get to any
[166:05] reasonable answer, you're already
[166:07] working super super below um you know
[166:09] total accuracy limits. Here's another
[166:10] example of memory retrieval accuracy. So
[166:13] basically if there is some token buried
[166:15] super deep in the context of you know a
[166:18] model that's doing 2 million48,000
[166:21] context window um it forgets it you know
[166:24] when there are only 30,000 tokens in the
[166:26] prompt or whatever it sees and finds it
[166:28] like 100% of the time but if there are I
[166:30] don't know 2 million it'll actually
[166:32] forget about that a massive chunk of the
[166:34] time and it won't even realize like that
[166:35] there is a token within its context.
[166:37] basically its ability to retrieve things
[166:38] from its memory, intermediate memory in
[166:41] this case, which is just the chat and
[166:42] the prompt, um, plummets. Finally, you
[166:44] could see here a needle in the haystack
[166:46] sort of example. Um, very similar to
[166:48] what we were talking about earlier, but
[166:50] basically as the number of tokens goes
[166:52] up, you see a massive decrease in just
[166:54] the model's ability to meaningfully keep
[166:56] track of things. And this is just sort
[166:58] of the way that intelligence works,
[167:00] right? The more things we're trying to
[167:01] juggle and keep in our head
[167:02] simultaneously, the higher the
[167:04] likelihood that we're going to forget
[167:05] any one of them. So, as a demonstrative
[167:07] example, let's say I wanted my agent to
[167:09] write me an absolutely beautiful poem
[167:10] all about the meaning of life and our
[167:12] place in the universe. I say, "I'm a big
[167:14] fan of MayaangAngelou and Pablo Nuto is
[167:16] wonderful as well. Please make this um
[167:18] short but also punchy and very
[167:21] beautiful." If you think about it
[167:23] logically, like this prompt right here
[167:24] is a certain number of tokens and I can
[167:26] count that here. I'm using a service
[167:28] called wordcounter.net. It doesn't count
[167:30] tokens, it counts words. But if you want
[167:31] the number of tokens, you basically just
[167:33] grab the number of words, then you
[167:34] multiply it by, you know, uh, 1 divid
[167:37] 0.7 approximately. If I do that math,
[167:40] this is somewhere on the order of like
[167:42] 67 tokens. But I want you to look
[167:44] really, really closely at what I just
[167:46] wrote here. Are all of these words
[167:48] required in order to get the model to do
[167:50] something for us? Like what is the
[167:52] information density of this sentence?
[167:55] Hello. Is that required? Probably not,
[167:58] right? I could probably realistically
[168:00] remove that. could. It's kind of a long
[168:02] way to say can. Can can you is kind of a
[168:05] long way to just tell it to write
[168:06] something. So, write me an absolutely
[168:09] beautiful do I need that? No. Write me a
[168:12] beautiful poem all about no about the
[168:15] meaning of life and our place in the
[168:18] universe. I say
[168:23] emulate Maya Angelou
[168:27] Pablo Naruda.
[168:33] Short, punchy,
[168:38] and I don't actually need to say very
[168:40] beautiful because I just said so earlier
[168:43] up here. Now, if you compare what I just
[168:44] wrote um initially at 47 words to what I
[168:47] wrote here at 22 words, notice how I
[168:49] basically said the exact same thing I
[168:51] did in the first prompt just in terms of
[168:53] the actual like pure information
[168:54] density. I just did it in less than half
[168:57] of the words. So now instead of 67
[168:59] tokens, this is probably somewhere right
[169:00] around like, you know, 28 tokens or
[169:02] something like that. What that means,
[169:03] walking back to our example, is you can
[169:04] realistically significantly improve the
[169:07] ultimate quality of an output just by
[169:10] refactoring the sentences that you feed
[169:12] into a prompt. Instead of hello, could
[169:14] you write me an absolutely beautiful
[169:15] poem all about the meaning of life or
[169:16] whatever, I could create a new prompt
[169:19] instance and then I could just say the
[169:20] exact same thing. And instead of me
[169:22] doing this on, you know, two lines or
[169:23] something like that, I could do this on
[169:24] one line. And although it is very
[169:27] difficult to determine the quality of a
[169:29] poem quantitatively what is occurring
[169:31] statistically is the quality of this
[169:33] poem over here will be better than the
[169:35] quality of this poem over here. The
[169:37] reason why is I just wrote it in a
[169:39] shorter sort of punchier way. So as
[169:40] opposed to if you think about this graph
[169:42] um you know quality and then the prompt
[169:45] length
[169:48] as opposed to me being somewhere over
[169:50] here like in this example realistically
[169:52] this example I'm probably somewhere over
[169:54] here right so the reason I'm showing you
[169:56] this is because this is exactly what
[169:58] models are actually doing under the hood
[170:00] instead of writing in in like laborious
[170:02] long sort of ways what they are doing is
[170:04] they're actually compacting the words
[170:05] that you are saying into as high an
[170:08] information density summary of your
[170:10] prompt as humanly possible. And they
[170:11] have a couple of strategies to do this.
[170:13] I don't know if you guys have seen like
[170:14] reasoning tokens, but the way that
[170:16] reasoning occurs here is it's actually
[170:17] done like a very high information
[170:19] density way. They actually specifically
[170:22] have trained the model to write in a way
[170:24] that is shorter on tokens as opposed to
[170:26] longer. If you look at other models out
[170:28] there like GPTOSS 20 bill for instance
[170:31] or maybe 120 bill, um these are open
[170:33] source models that OpenAI released a
[170:34] little while ago. You'll notice when you
[170:36] expand the reasoning tokens a very
[170:38] peculiar thing. It writes super short.
[170:40] It says need to define X but also Y but
[170:44] maybe Z. And you're like what the heck's
[170:47] going on? This is like an alien really
[170:48] short form way of writing. Well, the
[170:50] reason why it's writing that way is
[170:51] because it's just much higher
[170:52] information density. And the higher
[170:53] theformational content in your prompt
[170:55] per token, the ultimate better response
[170:58] you are going to get. Another strategy
[171:00] that models will use is they will
[171:01] compact. Okay? And what I mean by this
[171:03] is basically every time you feed in any
[171:05] prompt to a model, what it's also doing
[171:07] is it's going back and feeding in every
[171:09] message that you and it have ever sent
[171:10] to each other in the same chain. So what
[171:12] compaction is is it basically is just
[171:14] you take the entire history of your
[171:17] prompt and then you just summarize it.
[171:18] Summarize everything we've talked about
[171:21] so far. So now I'm just going to have it
[171:23] summarize it all into a very succinct
[171:25] message. And then the way the compaction
[171:27] works is once we hit a certain token
[171:29] amount which uh could be you know 50% of
[171:31] the total number of tokens allotted or
[171:33] whatever this summary is then fed into
[171:35] the next instance of the model and so
[171:37] now you know a future instance of in
[171:39] this case claude code would have access
[171:40] to more or less the full summary. Sure
[171:42] we'll miss some details but a lot of
[171:44] those details aren't really that
[171:46] consequential or important anyway. Think
[171:47] of how many fewer tokens this is than
[171:49] literally my entire conversation history
[171:51] from start to finish. Another big issue
[171:53] is when your agent calls an MCP tool
[171:55] directly, the entire response goes into
[171:57] the context. So if I were wanted to pull
[172:00] a document from Google Drive, for
[172:01] instance, I would actually then have to
[172:03] store the entire thing in my context, at
[172:04] least the way models are right now. If I
[172:06] wanted to query a Google sheet for like
[172:08] 10 rows or something, let's say all 10
[172:10] rows had like 20 columns each. Well, now
[172:12] I have 200 additional cells within my
[172:14] context. Meaning that your agent can hit
[172:16] the context ceiling really fast. they
[172:18] can burn a ton of money and so on and so
[172:19] forth when you use generalized MCP
[172:21] tools, not tools that you build
[172:22] yourself, but ones that other people
[172:23] build for you without really optimizing
[172:25] the process.
[172:27] Last thing I'm going to note on this is
[172:29] not all MCP servers are created equal. A
[172:31] lot of servers are rushed to market to
[172:32] capitalize on the hype. I know a couple
[172:34] just off the top of my head that are
[172:35] just super poor. They don't return like
[172:37] any good error codes. They don't even
[172:39] interact with the APIs correctly and
[172:40] tons of people are unfortunately
[172:41] struggling because of that. Um, some
[172:43] good examples are perplexities and NAND
[172:45] servers. Uh, but some really bad
[172:47] examples of this, too. I'm not going to
[172:48] name the names, but some are a complete
[172:49] joke. In general, you will know when you
[172:51] start interacting with an MCP server.
[172:53] Just going to flag a bunch of errors.
[172:54] Your model's just going to be dumb as
[172:55] hell. You could tell pretty quick. All
[172:57] right, so let me show you how easy it is
[172:59] to connect the Google Drive MCP server.
[173:00] We've already done a little bit of MCP.
[173:02] I've obviously wanted to tease that
[173:04] throughout the course to keep you guys
[173:05] um interested and engaged, but this time
[173:07] I'm actually going to do a full
[173:08] comprehensive walkthrough on how to do
[173:09] it. We're going to connect this to our
[173:10] agent, and then we're going to use it to
[173:11] perform a really simple operation. I
[173:13] just want you to notice how how seamless
[173:14] the integration is. Once it's set up, I
[173:16] don't actually have to even like set up
[173:18] the directive or the script or anything.
[173:19] I can just like uh communicate with it
[173:21] in plain language and it can go in and
[173:22] call the appropriate tools for me. Let's
[173:24] talk MCPs. Now, as I've talked about,
[173:26] model context protocol servers differ in
[173:28] their quality. Some were made pretty
[173:30] hastily, others were made very um
[173:33] carefully and are very high quality. But
[173:35] because of this, you do have to be a
[173:36] little bit careful and be open to doing
[173:38] some trial and error when it comes to
[173:39] adding your own MCPs. Regardless, I'm
[173:41] going to show you guys how simple and
[173:42] easy it is to do. First of all, there
[173:44] are tools and websites out there like
[173:46] mcpmarket.com
[173:48] and mcpservers.org
[173:50] whose sole job it is to basically
[173:52] categorize and then list all of the good
[173:55] MCP features out there. So, as you can
[173:57] see, there's an MCP for Trigger Dev, MCP
[174:00] for OpenSpec, Fast API, Pipe Dream, PAL,
[174:04] and these on these tools anyway are
[174:06] basically rated uh based off of their
[174:08] quality. So, the higher up the better,
[174:10] right? So, if you want the ability to
[174:11] automate browser interactions for large
[174:13] language models using Playright, this is
[174:15] the MCP for you. You know, if you want
[174:16] Chrome DevTools, this is the MCP model
[174:19] for you. If you want to automate, I
[174:21] don't know, Sereno specifically, then
[174:23] this is the one for you, and so on and
[174:24] so on and so forth. What I want to do in
[174:26] this video is show you just how easy it
[174:27] is to set one up. Um, you guys have
[174:29] already seen me do this for ClickUp,
[174:31] although that wasn't the point of the
[174:32] tutorial. What I'm going to do in this
[174:33] demo is just be a lot more specific
[174:35] about it. So, simplest and easiest way
[174:37] to get up and running with an MCP is
[174:38] just to ask your agent. So, I'm just
[174:40] going to say, hey, I want to set up a
[174:41] Gmail MCP so that I can send emails on
[174:44] demand from my email address. And then
[174:47] I'm going to give it some details just
[174:49] that it knows that, you know, this is
[174:51] like a Google Workspace sort of address.
[174:53] And let's see what it does. First, it's
[174:56] going to look and see whether or not
[174:58] there's some email MCP already. It's
[175:00] probably not going to find it. It really
[175:02] does help to open up these thinking
[175:04] modules. So now it's going to say, "Hey,
[175:06] you know, I see you've already set up an
[175:07] SMTP email for this email address, but
[175:10] instead here are two approaches. First,
[175:12] you can do quick SMTP. Second, you can
[175:15] do the Gmail MCP." So obviously, I want
[175:17] to do Gmail MCP. Let's do the Gmail MCP.
[175:22] I want you to do everything you can for
[175:24] me. Typically, models will give you
[175:26] instructions and stuff like this, but
[175:28] it's much better just to have them do it
[175:29] all for you. So, anytime you don't
[175:31] really know what to do or it's laborious
[175:33] or involved, just see how much the model
[175:34] can do for you. And that's what it is
[175:36] currently doing. Okay, cool. And this
[175:38] actually ended up finding a previous
[175:39] OOTH instance somewhere on my computer.
[175:41] I should note it was not in this folder.
[175:43] I just asked it to get up and going.
[175:44] It's running into some issues here
[175:46] because I haven't actually done this for
[175:48] this MCP before, which is
[175:49] understandable. Now, it's going to add
[175:51] some to my cloud config. Okay, now it's
[175:53] asking me to sign in. So, I'm going to
[175:54] sign in right over here. Cool. Says the
[175:56] authentication successful. We can now
[175:58] close this window. Okay, so now I just
[175:59] need to restart cloud code. Okay,
[176:05] just going to go MCP or manage MCPS.
[176:09] See that I had have my Gmail MCP
[176:11] connected.
[176:12] And now I can just say, "Hey, send an
[176:15] email to Nicholas orgmail.com
[176:19] saying what's up." Boom. Just sent me
[176:20] the email. Fantastic. That was easy.
[176:23] Okay, that's cool. Um, now that we've
[176:25] sent the email, obviously we have to
[176:26] talk about how to set up your own MCP
[176:29] servers, which is way cooler. So, how do
[176:31] you actually go about this process?
[176:32] Well, I didn't actually know until quite
[176:34] recently. I just asked how would I
[176:35] create my own MCP server, and now it's
[176:37] giving me a bunch of knowledge. Here's
[176:39] how to create your own server using
[176:40] Python. So, hypothetically, just for the
[176:43] purpose of this demonstration, I want to
[176:44] set up a really simple MCP, one that um
[176:46] just does something really
[176:47] straightforward. Just reads my website.
[176:49] Maybe it has some information about my
[176:50] website, and then it just like returns
[176:51] information about it. So, I said,
[176:53] "Create a simple custom MCP server whose
[176:55] sole job it is is to interact with this
[176:57] website, www.leftclick.ai."
[177:00] Now, in case you guys didn't know,
[177:01] leftclick.ai is my business. Um, we are
[177:04] the definitive AI growth partner for
[177:05] fastmoving B2B companies. Uh,
[177:07] essentially what we do is we build
[177:09] outbound growth engines that supplement
[177:11] AI to do things like personalize the
[177:13] emails, find leads, and so on and so
[177:15] forth. I talk about it a lot on my
[177:16] channel. And so, literally all I want
[177:18] this MCP to do is basically just to be
[177:20] be a resource for this website. I want
[177:22] people to be able to download it and
[177:23] then just be like, "Hey, tell me about
[177:24] leftclick and I want it to call the
[177:26] MCP." Is that something you need? No,
[177:28] obviously not. But you don't need MCPs
[177:30] in general. MCPS are just convenient,
[177:32] nice little wrappers around functions.
[177:33] Moving back to Cloud Code here, you can
[177:35] see that it now created an MCP-servers
[177:38] folder. And what it's doing next is
[177:39] it'll write the server Python code. I
[177:42] have no idea what that Python code looks
[177:43] like. After that, it'll create some TOML
[177:46] for dependencies before providing some
[177:48] registration instructions for me. Okay,
[177:50] so it looks like it just finished.
[177:52] Creates a server that exposes five
[177:54] tools. Get company overview, get
[177:56] services, get booking link, get case
[177:58] studies, and search site. So that's
[178:00] pretty easy. It's saying, "Hey, do you
[178:01] want to register with cloud code?" I'll
[178:03] just say, "Great. Sounds good.
[178:04] Register."
[178:06] It'll go through the rest of that
[178:07] process for me. Okay. So now I'm going
[178:10] to do a new instance of Cloud Code.
[178:12] Again, going to go /mcp status. It's now
[178:15] loading my servers. And you can see now
[178:16] we have the leftclick st server
[178:18] available. So go to bypass permissions
[178:20] and then I'll say tell me about
[178:22] leftclick. Now what occurs when this
[178:24] happens is because we have access to the
[178:26] MCP data, it'll actually find that and
[178:28] then get me information about it. So
[178:30] that's what's happening right here. We
[178:32] called the MCP server as opposed to
[178:34] doing something else. Maybe I'll say
[178:36] what's the booking link. The reason I'm
[178:39] asking this is because I saw there was a
[178:40] booking link feature. So it's going to
[178:42] call the get booking link function. Here
[178:44] it is. Leftclick.ai I book a call to
[178:46] schedule a complimentary 30-inut
[178:48] discovery call. Now, in my case, I don't
[178:50] think I actually have a calendar, which
[178:51] is why it just gave me the thing and
[178:52] then it told me where to find it. But
[178:54] hopefully, it's clear. You can build
[178:55] your own MCP servers super easily. So,
[178:57] why build your own MCP servers to begin
[178:59] with? Well, generally speaking, like I
[179:01] probably wouldn't put together MCP
[179:03] servers for most things these days
[179:04] unless I wanted to share them with
[179:05] others. So, like a creator building an
[179:08] MCP server for all of his followers to
[179:10] use, that's a pretty good um option. And
[179:12] so maybe if there's something cool that
[179:14] you know I want to share with you guys,
[179:15] I might do that and then make it
[179:16] publicly available. But aside from that,
[179:18] like why would you build an MCB server
[179:20] instead of maybe using cloud skills or
[179:22] do I've had a lot of people ask me this,
[179:24] Nick, why don't you uh recommend MCP
[179:26] more often and so on and so forth. And
[179:28] the reason why is it's just not really
[179:29] required. MCP is positive in so far that
[179:32] it standardizes the ability to call
[179:34] tools and whatnot, but it's also
[179:35] negative in so far that it loads a ton
[179:37] into context. Like what you're not
[179:40] seeing here is how many tokens that I am
[179:41] essentially consuming by having this MCP
[179:44] server. If I go back slash and then
[179:45] write the word context, you'll see that
[179:47] it actually includes a bunch of
[179:48] information about my context usage. And
[179:50] so of the basically the entire
[179:52] conversation we've had so far, um I've
[179:55] used 1.4% in the system prompt, which is
[179:57] just the um you know, claude.mmd, 7.4%
[180:00] in my system tools, which is just
[180:02] something I don't have control over. And
[180:03] you'll see that there's 8.2% 2% of my
[180:06] entire context window dedicated just to
[180:07] MCP tools. The rest of the stuff, 0.6%
[180:10] 0.6% of my messages. And so what's
[180:12] really really kind of annoying is that
[180:14] this thing has basically filled up about
[180:16] half of my entire contact window. And
[180:18] really I just have like a bunch of
[180:19] really simple tools. Leftclick at
[180:20] company overview, uh, Gmail send email.
[180:23] You know, this is eating up a ton of my
[180:25] total token space if you think about it.
[180:27] The left click server itself is uh
[180:29] almost what I guess that's like 3,000 or
[180:31] so over 3,000 3,300 or something like
[180:34] that um of my tokens. And you know these
[180:36] tokens aren't free. I spend money to use
[180:38] these tokens. I also obviously every
[180:40] time I make a message and you know have
[180:43] some output um the number of tokens in
[180:45] my prompt it does affect the output
[180:47] quality which we're going to talk about
[180:48] later. So, for the most part, I don't
[180:50] actually recommend using MCPS unless
[180:52] it's something hyper standardized or
[180:53] unless it's like a one-click thing and
[180:55] uh unless, you know, you're building one
[180:57] that you want to, you know, share maybe
[180:58] with your team or maybe with like a
[181:00] group of people. All right, so now let's
[181:01] talk about building the workflows. I've
[181:03] built a bunch of workflows for you
[181:04] throughout various demos, but I now I
[181:06] want to provide you guys a systematic
[181:07] approach to be able to do so yourself
[181:09] really easily and really
[181:10] straightforwardly. First major
[181:12] principle, everything begins and ends
[181:15] with your system prompt. That system
[181:17] prompt, as we know, is typically called
[181:18] agents MD, claude MD, Gemini MD, or
[181:22] cursor MD. And there are many more
[181:24] naming conventions. I'm not going to
[181:25] cover them all. The [snorts] name
[181:26] basically just needs to match whatever
[181:27] your IDE or agent looks for. And the
[181:30] content should be identical regardless
[181:31] of how you call it. Now, for D
[181:33] specifically, I'll show you guys exactly
[181:34] what mine looks like in a sec. This
[181:36] system prompt or agents MD or cloud MD
[181:38] or whatever, it's basically just a
[181:40] supercharged prompt. When you
[181:41] communicate with chatbt in your window
[181:43] or in your browser and you say, "Hey, I
[181:44] want you to do whatever for me. That's a
[181:46] pretty short prompt. This one is
[181:47] basically a prompt that's inserted every
[181:49] time and it's just super super long,
[181:51] super intense, super comprehensive, and
[181:53] it covers more or less all of the edge
[181:55] cases and ideas that you want the model
[181:56] to have. It should explain your
[181:58] framework. It should also explain your
[182:00] thinking, what you want it to do at
[182:01] every step, and then more. This is how
[182:03] you customize your agent essentially, so
[182:05] it's not just a cookie cutter vanilla
[182:06] agent that functions the same for
[182:07] everybody else. The prompt right now is
[182:09] kind of the moat. Now, I do recommend
[182:10] you to copy and paste mine because it's
[182:12] just like out of the box pretty good.
[182:13] But there's some important things I'd
[182:14] like you guys to make sure to include
[182:16] regardless of whether you're using mine
[182:17] or whether you guys are using somebody
[182:19] else's. The first is you should explain
[182:21] the framework. So whatever framework
[182:24] you're using, whether you are using do
[182:25] or claude skills, you should actually
[182:26] explain that to the model. You should
[182:28] tell them where the resources are. You
[182:30] know, hey, directives are in the
[182:31] /directives folder. Hey, you should use
[182:33] TMP if you want to store temporary
[182:35] files. Make sure to delete temporary
[182:36] files after you're done. I also find a
[182:38] lot of success in explaining the
[182:39] rationale behind the framework. It
[182:41] reduces error rate significantly. So I
[182:42] don't just say hey you're using the do
[182:44] framework I say hey right now as a large
[182:46] language model the probability that you
[182:48] can do things completely on your own
[182:49] without any framework is pretty low
[182:51] because of that I'm using a framework
[182:52] called directive orchestration execution
[182:54] here's how it works directives store
[182:56] whatever orchestration is you execution
[182:59] does whatever by using this framework
[183:01] you significantly reduce your error
[183:02] rates and blah blah blah blah here's why
[183:04] you should do this right we actually
[183:05] convince the model you almost have to
[183:07] get like buyin from the model when you
[183:09] get buyin from the model the resulting
[183:10] outputs are a lot higher quality the
[183:12] second thing you should include is an
[183:13] explanation of self- annealing. Now, I'm
[183:15] kind of cheating here because I haven't
[183:16] actually got to this point, but bear
[183:17] with me. Self- annealing is the process
[183:19] of the model fixing its own mistakes
[183:20] without coming to you first. So, rather
[183:22] than just break like an old school
[183:24] automation, self- annealing means if
[183:26] there's an error, you then feed that
[183:28] error into the model, the model then
[183:30] reasons and then it solves and then
[183:32] finally updates so that it doesn't run
[183:33] into that problem the next time. In a
[183:35] nutshell, self annealing allows the
[183:37] models to become more resilient. Doesn't
[183:39] just get back to working. And every time
[183:41] something breaks, it's a feature, not a
[183:42] bug, because it reveals weak points in
[183:44] your flow that you didn't even know
[183:45] existed. I'm going to tell you all about
[183:47] self-nealing and go really in depth with
[183:49] like system prompts and stuff like that
[183:50] later on, but for now, it's sufficient
[183:51] that you just know what it is.
[183:54] The third thing you need to include is
[183:55] you need to include a sense of autonomy.
[183:59] What do I mean by this? Well, I let the
[184:01] model know that, hey, my goal is for you
[184:02] to run autonomously without me. You are
[184:04] an agentic workflow. I say you should
[184:07] test each system on its own. you should
[184:08] identify mistakes on your own and you
[184:10] should loop repeatedly until you make it
[184:12] work. I also say, "Hey, be careful when
[184:14] you're sending API calls or consuming my
[184:16] tokens for testing reasons." And then I
[184:19] say, "Hey man, this is really just a
[184:21] rule that says come to me only if you
[184:23] absolutely need to. I don't want you to
[184:24] come to me unless you are 100% confident
[184:27] that you cannot solve this thing without
[184:28] my human input." And that's very, very
[184:30] rare. When you do this, your model gets
[184:32] significantly more autonomous and you
[184:34] really change it from like this uh a
[184:36] co-builder programming thing into like a
[184:39] co-orker and a co-mp employee. At the
[184:41] end of the day, directives and execution
[184:43] scripts are basically living documents.
[184:44] So, if there's an error or a constraint
[184:46] that you guys find, you should instruct
[184:47] your agent to update them. Cool. So,
[184:49] talking a little bit more about
[184:50] building, if you have SOPs, you're
[184:51] actually already halfway to having
[184:53] strong agentic workflows. All you really
[184:54] do is you just open your IDE. You drag
[184:57] your existing SOP document from, you
[184:59] know, your knowledge base or your
[185:01] company PDF or your company uh one drive
[185:03] or Google Drive into your workspace. You
[185:06] just say, "Hey, I just uploaded a file
[185:08] into the workspace. Could you turn it
[185:10] into a directive and build the execution
[185:11] scripts to make it happen?" Now, if it's
[185:13] a really simple SOP, let's say something
[185:15] that doesn't even need an execution
[185:16] script necessarily. It's just like a an
[185:18] AI prompt thing, it it'll just do it and
[185:20] it'll do it like really quickly. If it's
[185:22] a complex one, it may ask you to verify
[185:23] its approach. Hey, you know, here's some
[185:25] ideas that I have. What do you think I
[185:26] should do? Okay. Yeah, let's pick the
[185:28] first one. Let's proceed. When the agent
[185:29] does this, it'll create the directive in
[185:31] /directives. It'll build whatever
[185:33] scripts are needed, then store them in
[185:34] executions, and then if it doesn't have
[185:36] API tokens or whatever, it'll just ask
[185:37] you to add them to an ENV. This works
[185:39] really well because SOPs are literally
[185:41] already directives. They contain
[185:42] everything the agent needs, the goals,
[185:44] the steps, the inputs, outputs, and edge
[185:46] cases. If yours are written correctly,
[185:48] all you're doing is you're just
[185:49] translating your human readable
[185:51] documents into another human readable
[185:53] document in the form of directives.
[185:54] You're not really getting the agent to
[185:56] like come up with anything new. It's
[185:57] just reformatting and translating into a
[185:59] more token efficient format. All you're
[186:00] really doing is converting a recipe into
[186:02] a format that some sort of robot chef
[186:03] can follow. You're basically like
[186:05] programming this thing. If your SOPs
[186:07] aren't very good, believe it or not,
[186:08] this is actually an opportunity to make
[186:10] them better because your agent, knowing
[186:12] that it does not have everything that it
[186:14] needs in order to do the task, will ask
[186:15] clarifying questions. This will force
[186:18] you as a systems engineer to resolve
[186:21] ambiguities that a human being might
[186:23] just figure it out without explicitly
[186:24] having to write. The resulting directive
[186:27] ends up being a lot better than the
[186:28] original SOP a lot of the time. And it
[186:31] means that your messy docs become an
[186:33] opportunity to actually clean up your
[186:34] processes and become a clearer company.
[186:37] I think that's really underrated, but
[186:39] companies in general tend to bury the
[186:42] lead. A lot of the time they don't
[186:43] actually make explicit or verbalize all
[186:46] of the knowledge within the business.
[186:47] It's like, oh, just ask Pete for
[186:49] whatever. Send an email to this person.
[186:51] I mean, your agent will say, well, like,
[186:52] who the heck is that and why does that
[186:53] matter? Right? Can we just include the
[186:55] information that we need in order to do
[186:56] it? Now, if you have a big weight step
[186:58] or something, it'll be like, "Okay, to
[187:00] be clear, why do you want me to wait?
[187:01] What is the purpose of this?" And so,
[187:03] the very building process itself can
[187:05] actually help significantly upgrade your
[187:07] business. Now, let's say you have no
[187:09] documentation. Well, if you don't have
[187:11] any pre-existing documentation or SOPs,
[187:13] no problem. We can still make this work.
[187:15] What you do is you begin with some very
[187:17] basic bullet points that describe your
[187:19] ideas surrounding the agent. I use
[187:21] really plain conversational language. I
[187:23] will literally write down what I want to
[187:25] do as if I'm explaining it to a
[187:27] colleague. I have a bunch of people in
[187:28] my team. A lot of the time this is
[187:29] messages that I would have sent to them.
[187:31] So sometimes I literally just go into
[187:32] Slack and I say, "Hey, I want you to do
[187:34] X, Y, and Z. It should be this. It
[187:36] should be that. It should be that."
[187:37] After I'm done explaining it like I'd
[187:38] explain it to a colleague. I then just
[187:40] copy and paste it in my agent. Do not
[187:42] overthink the structure. Don't overthink
[187:44] the format. Just get your ideas down.
[187:45] Agents are really good at formatting
[187:47] this. You can also use voice prompts
[187:48] like you've seen me do a bunch. And then
[187:49] you can refine and add detail later as
[187:51] you test and learn and try different
[187:52] approaches. The really cool thing is you
[187:54] don't actually need to know how to code
[187:55] at all. You just need to know how to
[187:57] explain what it is that you want, which
[187:58] I think is a far more achievable skill.
[188:00] This is a real prompt from a lead
[188:01] generation system that I just built. I
[188:03] said, "Hey, scrape leads from Appify
[188:04] based on the industry and location I
[188:06] specify. Then verify 80% match my target
[188:08] market before doing the full scrape.
[188:10] When you're done, enrich missing emails
[188:11] using a secondary service like any
[188:12] mailinder. Then add everything to a
[188:14] sharable Google sheet and send me the
[188:15] link." Pretty straightforward and pretty
[188:17] simple, huh? All right, let me show you
[188:18] a practical demo. All right, let's build
[188:20] another agentic workflow together. This
[188:22] one I want to be a lead generation or
[188:25] lead scraping workflow. You guys might
[188:27] have seen me build these sorts of things
[188:28] before on my channel. I love building
[188:30] them because they are so high leverage
[188:32] relative to what I used to have to do
[188:34] back in the day. So, I figured I'd just
[188:36] bring you guys alongside me for uh one
[188:38] of the new lead scraping workflows that
[188:40] I'm going to put together. So, the first
[188:41] thing I'm going to do, just like I
[188:42] always do, is I'm going to give it in
[188:44] natural language a set of instructions
[188:46] to club. I'm using a voice transcription
[188:48] tool. So, I'll say, "Hey, I'd like to
[188:50] build a lead generation workflow that
[188:53] scrapes publicly available information
[188:56] to get me a list of B2B leads. What are
[189:00] the three best approaches for this?"
[189:03] Now, I kind of know what I want to do
[189:05] here, but I want to show you guys how
[189:06] you can use an agent, not only as some
[189:09] builder, but also as something to assist
[189:11] you with the ideation. So what this is
[189:13] saying is we could start by using a
[189:14] LinkedIn sales navigator or similar
[189:16] tools to identify decision makers by
[189:19] title, industry, company size, then
[189:21] enrich with contact data via APIs. That
[189:24] sounds pretty good to me. So I'm going
[189:25] to need some additional tool. That's
[189:27] okay.
[189:29] Let's go with the first. I think I've
[189:31] heard of a few different tools we could
[189:33] use to do this. Phantom Buster is one.
[189:35] There's another one called Vain. Which
[189:37] do you think is best for our approach?
[189:39] How should we go about this exactly? So,
[189:41] it's now going through and it's
[189:42] performing a bunch of research on these
[189:44] tools. Okay, now it's gone through
[189:46] performed a bunch of research on all of
[189:48] the tools that we could use and it since
[189:50] recommended me a uh a pipeline. So, that
[189:52] sounds awesome. I really like this. Why
[189:54] don't I say let's do it. Yes, I already
[189:56] have a sales navigator subscription.
[189:59] Let's do it. Build out a pipeline. I
[190:02] also already have a pre-existing
[190:04] subscription to any MailFinder, which is
[190:06] an enrichment tool. So, why don't we use
[190:07] that as part of our flow? I want you to
[190:09] build this using the DO framework. Let
[190:12] me know if you need anything.
[190:15] So now what we've done is we've
[190:17] basically taken
[190:19] our demand or our request I should say
[190:22] and then we've paired it down into a
[190:24] much higher probability build path um
[190:27] just based off a couple of back and
[190:28] forth questions. If you think about it,
[190:30] the total amount of time that it takes
[190:32] an agent to build something is pretty
[190:34] short, all things considered, but it's
[190:36] still like five or 10 or 15 minutes. If
[190:39] you screw up and you go down the wrong
[190:41] path, in order for you to walk back and
[190:43] start fresh, you're probably going to
[190:44] have to spend another 10 or 15 minutes
[190:45] in order to have the agent rebuild the
[190:47] next thing. And so, at a very high
[190:49] level, giving it a tiny bit of input
[190:51] initially is super powerful, and it's
[190:53] also a big time saver. So, I usually
[190:55] recommend going back and forth at least
[190:56] a little bit while it does its searches.
[190:58] and you know use your own human
[191:00] knowledge really to pair down the total
[191:02] um possible number of paths. So it's
[191:05] going through building a Google Sheets
[191:07] LinkedIn lead genen lead enrichment
[191:09] pipeline and any mailfinder client
[191:11] pipeline. All right, once it's almost
[191:13] done all of the scripts, it's going to
[191:15] create a directive just to tie
[191:16] everything together. Do all this for me.
[191:20] Okay, I'm now having it wrap things up.
[191:23] We can now start giving it a test.
[191:25] Obviously, it is one thing if a model
[191:27] tells you that it is good to go. It's a
[191:29] complete other thing um whether or not
[191:31] the flow actually works. So, we always
[191:33] have to verify that the flow works with
[191:34] with a real test. Okay, it's now testing
[191:37] out any mailinder, testing out the
[191:39] Google Sheets connection.
[191:41] Looks like it found an issue with the
[191:43] way that it was going to do the
[191:44] connection. I added a credentials.json
[191:46] file here just from another workspace,
[191:48] which is basically like an ooth thing.
[191:50] Um I didn't generate this thing. I had
[191:52] the model generate it for me. It's now
[191:54] going to ask to authenticate for the
[191:57] first time. Anytime you connect to a new
[191:59] Google credential with OOTH, you're
[192:01] going to have to do this. Now I have the
[192:02] browser authentication. I'm just going
[192:04] to pump over here and connect this. This
[192:06] is a great opportunity for me to point
[192:08] out a common issue that people have with
[192:10] the Gentic workflows. It's where they um
[192:13] essentially have the model generate a
[192:14] test case for them. So in this case,
[192:16] that's what's occurring here.
[192:17] Test_leads.csv.
[192:19] It then uses the test data essentially
[192:21] to test end to end to see whether or not
[192:23] the flow works. That's not good enough
[192:26] because if you think about it, the model
[192:27] just created a bunch of scripts. So the
[192:29] test case that it will come up with is
[192:31] most likely going to be in the same
[192:33] format that all of the rest of the
[192:35] scripts and so on and so forth expect.
[192:37] What's way more informative is for us
[192:38] just to do this entirely based off new
[192:40] data. So that's what I'm going to do
[192:42] next. I don't really want to export the
[192:44] leads from Vain. I instead want you to
[192:46] do all that for me.
[192:50] Okay. And it looks like it now is ready
[192:51] for a test. So I just need to give it a
[192:53] sales marketing or a sales navigator URL
[192:55] anyway and it'll do everything or I
[192:57] could run it myself with one command.
[192:59] That's cool. Um what I'm going to do is
[193:01] I'll just go back to LinkedIn sales nav
[193:03] here and I have a link. Basically what
[193:04] what happens on LinkedIn when you want
[193:06] to find something like a list of people
[193:08] is you need to generate a search on the
[193:09] lefth hand side. Now you just need to
[193:11] copy over the URL and then just paste it
[193:12] in. So I'm just going to paste this in
[193:13] and I'm just going to see what happens.
[193:14] We'll just test it in 10. All right. And
[193:16] now it has found 231 prospects. So it's
[193:19] going to go through and scrape the 231
[193:21] profiles via vein. Then enrich with any
[193:23] mailinder before exporting to Google
[193:25] Sheets. Okay, it had some issues with a
[193:28] particular API call uh to Vain. It since
[193:31] self-annealed and automatically fixed it
[193:33] all. So it's just continuing down the
[193:35] building process on that first run. Once
[193:37] I have it finished this first run, I'm
[193:38] just going to ask it to do a second run.
[193:40] And I'm going to do it completely from
[193:41] scratch. So it's going to be like a cold
[193:43] start. I'm going to instantiate a fresh
[193:44] cloud instance, one that has no idea
[193:46] what the heck's going on. Then we'll see
[193:48] how it goes. Okay, one of the outputs
[193:50] was buffered. That just means that uh
[193:52] basically it was in a loop repeating. So
[193:54] I just paused it and said how are we
[193:56] doing? Looks like it's still running. So
[193:58] Python is buffering the output. We're
[194:00] just going to wait for the completion.
[194:01] Sometimes some of these tool calls can
[194:02] take a fair bit and that's what's
[194:03] happening with any mailfinder. The
[194:05] reason why this is actually good for us
[194:07] is because I get to show you guys later
[194:08] on what it looks like to optimize a
[194:10] workflow realistically. And I know this
[194:12] because I've done a fair amount of
[194:14] enrichment at this point. You do not
[194:16] need to take this long to enrich 200
[194:18] records. You could probably enrich 200
[194:20] records in maybe like 15 seconds or so
[194:23] through bulk requests. Um the first time
[194:26] that a agent ever builds a workflow,
[194:29] it's going to do so in as simple a way
[194:31] as humanly possible. Typically through
[194:33] serial requests, which just means that
[194:34] it's sending one request at a time,
[194:36] waiting until the request is done, then
[194:38] sending another request after that. But
[194:40] what you can do with a lot of workflows
[194:42] is you can parallelize them, which means
[194:43] you could actually send 200 requests
[194:45] simultaneously and then wait for the
[194:47] outputs of all 200 in the same time
[194:49] block as opposed to, you know,
[194:50] independently. So I'm still going to
[194:52] wait for this thing to finish because I
[194:53] want this test to be done end to end at
[194:56] least once. Um, after that, we're going
[194:57] to look into ways to make this faster
[194:59] through parallelization and so on and so
[195:01] forth. Okay, so I got a little bit bored
[195:02] and I just said, hey, could we make this
[195:04] way faster? It's since um offered to
[195:06] batch all of these requests. So that's
[195:08] what it's going to do next. and let's
[195:10] see how quickly it performs. While I'm
[195:12] doing that, let me just create a new
[195:14] search. Maybe instead of United States
[195:16] residents, um I want to search Canadian
[195:18] residents. [gasps] That way, we'll be
[195:21] able to split test this very quickly and
[195:22] easily. As you can see here, we have 31
[195:25] results. Uh maybe we'll also do posted
[195:27] on LinkedIn, so maybe 45 or something
[195:28] like that. Okay, no, it's just 20. If I
[195:32] deselect this, how many do we get? 683.
[195:35] Uh too many. Why don't we just do
[195:37] Vancouver instead? I I want like between
[195:39] 50 to 100.
[195:42] Okay, 66. That's perfect. So, this is
[195:44] going to be the URL I use to test the um
[195:46] totally fresh app. It's now just going
[195:48] to go through the process of self
[195:50] annealing, running, testing, and so on
[195:51] and so forth. Looks like it found 139
[195:54] valid emails of my 231 sent. Now, it's
[195:57] just going through and updating the
[195:59] script a couple more times. Cool. It's
[196:00] gone through and since found me a bunch
[196:02] of leads, I can open up the spreadsheet
[196:04] to get 159 rows. So, um, these are all
[196:08] of the the records with email addresses.
[196:11] Um, there were more records that didn't
[196:12] have email addresses, but we just left
[196:13] those out. Obviously, this is pretty
[196:15] solid, but, um, I want to number one,
[196:18] make sure that we're documenting this.
[196:19] So, I'm going to head back over here,
[196:21] and I'll say make sure to document all
[196:23] changes, both directives and executions.
[196:27] Once it's done with the documentation,
[196:29] I'm then going to open up a totally new
[196:30] fresh instance and then go through and
[196:33] then um, update and then test. Cool. And
[196:36] it looks like it did some updating.
[196:38] That's pretty solid. What I'm going to
[196:39] do next is I'm just going to open up a
[196:40] new instance of Cloud Code. Going to set
[196:43] it to bypass permissions and I'll say,
[196:45] "Hey, here's a search URL. Scrape these
[196:50] using our pipeline."
[196:52] All right. So now this is a totally new
[196:55] fresh cloud code instance. Let's see how
[196:57] it performs. It's going to start by
[196:59] thinking it's checking the directive for
[197:01] LinkedIn scraping, which is great.
[197:02] That's what we wanted. It's then going
[197:04] through here. URL is a sales navigator
[197:06] search has a bunch of information here.
[197:08] It's going to check how many leads are
[197:09] available. Cool. Found 66 prospects. It
[197:12] is now going to perform the full scrape.
[197:15] Okay. And it looks like we got uh 45 out
[197:18] of those 66. So, this did work on a
[197:21] totally fresh list. Um took me about 4
[197:24] minutes. I got a little bit overeager
[197:26] and I was like, "Hey, are you done yet?"
[197:27] But realistically, this uh this works
[197:30] pretty well. So, I mean, a couple of
[197:31] different approaches that I could take
[197:32] here. Obviously, I could make this
[197:34] better, could make this faster. I could
[197:36] set up approaches to dump all this into
[197:38] Google sheet instantly using bulk. I
[197:40] could do I could do a lot of stuff and
[197:42] uh that's what I want to talk about
[197:43] next. But for the purposes of this
[197:44] demonstration, this is good to go. We
[197:46] have essentially created a workflow to
[197:49] completely or almost completely automate
[197:51] the entire process of scraping LinkedIn.
[197:52] Obviously, there is still one manual
[197:54] step, which is we need to provide the
[197:55] LinkedIn sales navigator URL, but that's
[197:57] something that we could reasonably
[197:58] automate if we'd like to as well. So,
[198:00] here's what you don't need to specify.
[198:02] You don't need to know which APIs to use
[198:04] or how they authenticate. You also don't
[198:05] need to know how to structure the code
[198:07] or handle an error case yourself. And
[198:08] you don't even need to know any Python,
[198:10] any JavaScript, or any programming
[198:11] language. The agent's whole job is to
[198:13] abstract that complexity away from you
[198:14] and turn it into a natural language. A
[198:16] really cool hack that I'm using a lot
[198:17] more of now is I don't just have the
[198:19] agent solve it one approach. I actually
[198:21] have the agent produce three approaches
[198:22] simultaneously. Then I either pick one
[198:24] of the three, whichever one makes the
[198:26] most sense, or this is kind of neat,
[198:28] [clears throat] I have parallel
[198:29] instances of my agent generate all three
[198:32] directive and execution scripts based
[198:35] off of each approach. I then just test
[198:37] their outputs and I rate. I test them on
[198:39] things like how fast it is, test them on
[198:41] things like how reliable it is and how
[198:43] cheap it is, and then I just pick the
[198:45] best performing one, and then that's it.
[198:46] Why three approaches? Well, if you think
[198:48] about it, the cost of exploring multiple
[198:50] approaches is basically free. They're
[198:52] not it's not free free tokens are not
[198:54] free yet but they are very cheap
[198:55] compared to the cost of intelligence and
[198:57] it's also a big chunk of the search
[198:59] space. Uh basically if this is like the
[199:01] amount of space you have to search
[199:03] through in order to come up with your
[199:04] really really cool problem rather than
[199:06] have your agent just go like manually
[199:08] one by one by one by one and just kind
[199:10] of do this whole thing on its own. Um
[199:12] you can actually just like quarter this
[199:14] you know and in my case I said three but
[199:16] you could totally have it four and then
[199:17] just have like four agents independently
[199:19] simultaneously. I can't draw
[199:21] simultaneous executions here, but just
[199:23] assume that it is. Explore that search
[199:25] base in like a tenth of the time. When
[199:26] you do this, I recommend you have it run
[199:28] in a temporary folder. So, you say,
[199:30] "Hey, do this in a temporary folder.
[199:31] Don't do this in the main directive
[199:33] execution um framework." Cuz I'm
[199:34] actually giving this to a few of your
[199:35] brother and sister agents to run
[199:37] simultaneously to figure out the best
[199:38] approach. There are a couple of
[199:39] trade-offs with every single way that
[199:41] you build. The first is speed versus
[199:43] cost. So, do you need it fast or do you
[199:44] need it cheap? Obviously, we're looking
[199:45] for situations where we have both, but a
[199:47] lot of the time you have to make
[199:48] trade-offs. Next is reliability and
[199:50] complex complexity. The simple solutions
[199:52] do break less often. If you can store
[199:54] things in one execution script, it's way
[199:55] faster and better than if you store
[199:57] things in 10. The next is breadth versus
[199:59] depth. So if you cover more ground or go
[200:01] really, really, really deep on a few
[200:02] items, it's going to depend or it's
[200:04] going to change how your agent
[200:06] constructs things. And then finally,
[200:08] sometimes you just need human judgment
[200:09] to weigh these things. So I would
[200:10] recommend at least asking your agent,
[200:12] how would you do this stuff before you
[200:13] actually have it go and build uh every
[200:15] approach. If you think about it
[200:16] logically, this steering is the highest
[200:19] return on investment time that you will
[200:21] ever spend across your entire agentic
[200:23] workflow career. And the reason why is
[200:25] really some of what I talked about
[200:26] earlier. If you just look at any process
[200:28] that has variability in its outputs,
[200:29] okay, this variability grows over time
[200:33] as you proceed through the process just
[200:35] because there are more and more and more
[200:36] and more steps possible, right? And so
[200:38] right now, this is kind of like the
[200:40] range of all of the possible um
[200:42] decisions that the model could make.
[200:43] Well, if you think about it, the one
[200:45] thing that you have the power to do at
[200:46] the very very beginning is you have the
[200:48] power to steer what direction this thing
[200:50] goes. And so let's say hypothetically my
[200:53] goal is over here, right? Or maybe we
[200:55] should say my goal is over here. If at
[200:58] the very beginning, literally from the
[201:00] first step, the model is already in the
[201:02] wrong direction. It doesn't really
[201:03] matter how much time and energy it takes
[201:05] to build things, right? But if you could
[201:07] just reorient this approach down over
[201:09] here, then your solution is actually in
[201:11] the range of all possible outcomes. I
[201:13] call this steering just like steering a
[201:14] car. If you steer, let's say you're
[201:16] going like a real straight line track
[201:18] and your car at the very beginning of
[201:20] the track is already starting to veer
[201:22] off a little bit. Obviously, the most
[201:24] important thing you can do as a, you
[201:25] know, driver is you could just steer it
[201:27] so that it goes basically as as straight
[201:29] down the middle of this thing as humanly
[201:31] possible, right? And that's just
[201:32] ultimately something that really takes
[201:34] like a minute or two. I wouldn't
[201:35] recommend trying to outsource everything
[201:37] to the model, like the thinking itself.
[201:38] The first version of anything you build
[201:40] probably will not be perfect. And the
[201:42] first versions of a lot of the things
[201:43] that I build do suck, but that's okay.
[201:44] That's actually one of the points. Dough
[201:46] really depends on iteration. So just run
[201:48] the workflow a few times, watch what
[201:50] happens, open up the reasoning loop, and
[201:52] then just take some notes on what's
[201:53] slow. Hey, I don't really like this.
[201:55] Hey, this takes forever. Is that
[201:56] necessary? Hey, um, I don't like how
[201:58] this had to call this API. Hey, this is
[201:59] a little too expensive. How can we do it
[202:01] cheaper? Right? Actually, just tell the
[202:03] model what it is. Like, it's you're not
[202:04] going to hurt its feelings. It's a the
[202:06] form of intelligence that none of us can
[202:08] really quantify. Don't anthropomorphize
[202:10] the damn thing. What'll happen is the
[202:12] agent will diagnose the problem and then
[202:14] implement a fix. And ideally, assuming
[202:15] that you have it in your system prompt,
[202:17] it'll also update both the execution
[202:18] script and your directive, which means
[202:20] next time you run from a fresh instance,
[202:22] it will already know the solution. And
[202:23] that's typically what I recommend. I
[202:24] recommend running it, fixing it, getting
[202:26] in that testing loop over and over and
[202:28] over again. And when you really want to
[202:29] verify that this thing works, you just
[202:30] open it up in a new instance and then
[202:31] have it run. Every problem that you
[202:33] encounter will make your system stronger
[202:34] if you're smart. Edge cases will get
[202:36] handled that you never anticipated. uh
[202:38] and after a few iterations you will have
[202:40] a robust workflow uh that I've heard a
[202:42] lot of people say this term battle
[202:43] tested I think battle tested about is
[202:45] about as real and as accurate a way to
[202:47] describe it but you'll have something
[202:48] that is actually just kind of like been
[202:50] there done that it has seen all possible
[202:51] instances of the problem because it's
[202:53] run 10 or 20 times it sort of knows what
[202:55] to expect um you know you basically go
[202:57] from a workflow that the very first time
[202:59] it runs maybe is 80% reliable to one
[203:01] that's 90% reliable to one that's 95%
[203:03] reliable one that's 97% reliable one
[203:06] that's 98% reliable and so on and so on
[203:08] and so on and so forth until it's like
[203:09] 99.25% or something. And maybe this is
[203:12] the theoretical limit that you reach.
[203:13] All right, let's build a lead genen flow
[203:14] start to finish using everything that
[203:15] I've talked about so far. You remember
[203:17] how earlier we created a lead generation
[203:19] workflow? Well, what if instead of just
[203:22] using one cloud instance to generate it,
[203:24] we used multiple cloud instances to
[203:25] generate the lead generation workflow in
[203:27] parallel. not only would be able to
[203:29] generate higher quality lead generation
[203:30] workflows, we'd be able to create things
[203:32] that are most likely better because we
[203:34] are able to search more opportunities
[203:36] and options. If that doesn't make sense
[203:38] to you, I'm just going to copy and paste
[203:39] the same thing that I pasted in here.
[203:41] Instead of three best approaches, I'll
[203:44] say five best approaches, I'll say be
[203:47] comprehensive and give me all possible
[203:50] options. And then instead of publicly
[203:51] available information, I'll say HVAC
[203:54] companies in Texas
[203:57] to get me a list of B2B leads and their
[203:59] emails.
[204:00] Okay, great. Once I give this parent
[204:03] agent some room to think, what I'm going
[204:05] to do is I'm then going to open up a
[204:07] bunch of additional clawed code
[204:09] instances. So, new,
[204:11] new,
[204:13] new,
[204:15] new. So, we're going to have five in
[204:16] total. What I'm going to do is I'm just
[204:18] going to
[204:20] set things up so we could see them all.
[204:22] Next, I'm going to provide some
[204:23] scaffolding. So, I'm just going to say,
[204:25] "Hey, your task is to build a lead
[204:27] generation workflow according to the
[204:29] below details." I'm giving similar tasks
[204:31] to five other agents. Since you're
[204:33] operating the same workspace, uh to
[204:35] minimize the probability of a conflict,
[204:37] do all your work in a new tmp/ test3
[204:40] folder. And then what I'm going to do is
[204:41] I'm just going to feed in all of this.
[204:43] So, I'm going to say boom
[204:49] boom
[204:53] boom
[204:57] boom.
[205:03] And then boom. And now I'm actually just
[205:05] going to run all of these
[205:06] simultaneously.
[205:08] What's cool is this is going to create
[205:10] new folders inside of this TMP which are
[205:12] not going to interfere with our other
[205:14] directives, our execution scripts. I can
[205:15] now remove this top level script here
[205:17] for simplicity. And now it's going to go
[205:19] through and just create all of these.
[205:21] Not all of these are at the exact same
[205:22] level obviously, but um you know this
[205:24] test two directory structure and the
[205:26] test 4 uh when they get created they're
[205:28] going to just do their work in there. So
[205:30] in this way I'm capable of exploring a
[205:32] large number of options in a very short
[205:33] period of time. I mean obviously I can
[205:35] take a brief highle look at like one of
[205:36] these things and say okay this one is
[205:38] most likely uh the highest probability
[205:40] of working but it's much easier if I
[205:42] just explore them and then what I do is
[205:44] anytime I run into a hiccup with one of
[205:46] these flows I just take a look at what
[205:47] the hiccup is and if the hiccup is like
[205:49] so big that it would be a pain in my ass
[205:51] to deal with then I just drop that and
[205:52] then I don't continue. Then for the
[205:54] survivors, um, once I have like a pretty
[205:56] good-look workflow, I'll test them all
[205:58] side by side, ask them to go do a
[206:00] scrape, and then once I've done the
[206:01] scrape, I can just compare and contrast
[206:03] results. What's really sweet is when all
[206:05] these things are done, I can sometimes
[206:06] combine the best of each, and then I can
[206:09] say, "Hey, build a unified lead
[206:10] generation workflow that combines the
[206:12] best of X, Y, and Z." And then it'll,
[206:14] you know, find 30% of leads with one
[206:16] approach, 30% of leads with the other
[206:18] approach, 30% of the leads with a third
[206:20] approach, and so on and so forth.
[206:21] Anecdotally, it feels really cool to be
[206:23] able to manage and orchestrate this many
[206:25] simultaneous builders. I don't usually
[206:27] do five at a time, but I just wanted to
[206:29] demonstrate that you can explore a very
[206:31] large search space in a very short
[206:32] period of time. So, after a few minutes,
[206:34] these are now beginning to finish. The
[206:36] one on the left hand side has tested the
[206:38] pipeline with a full batch. Just going
[206:39] to take a peek. See, we've now generated
[206:41] four of these files. We then have our
[206:43] pipeline summary, and now we just need
[206:45] to enter some API keys essentially. Now,
[206:47] the issue is I've yet to give it a
[206:48] Google Places API key or a Hunter API
[206:50] key. So, I'll just say, "Could you set
[206:53] up the Google API key for me?" I don't
[206:56] have Hunter, but I do have an email
[206:59] finder. Please do this instead. Over
[207:02] here, Apollo.
[207:09] Okay. And then one of these wanted a
[207:10] sales navigator URL for HVAC companies.
[207:13] So, I'm just going to go HVAC. And then
[207:15] geography. Why don't we just go Texas
[207:17] because I think that's what that was.
[207:20] Rest of this looks pretty reasonable.
[207:21] It's 4,000 results. I just want a really
[207:23] really like simple one. So, I'm just
[207:24] going to go change jobs 54. That way, we
[207:27] should only get 54. Go back here and
[207:29] then I'll feed in the URL.
[207:32] I then see an Apollo API key. Yes,
[207:35] Apollo API key. It's then going to go
[207:38] through
[207:40] and give me instructions on one of my
[207:42] API keys. So, I'm going to head over
[207:43] here to Google Places API. What I want
[207:46] is the Places API new apparently. So,
[207:48] I'm going to enable this. And now it's
[207:50] just a process of getting API keys for
[207:52] everything really.
[207:54] Copying the API key. Just going to paste
[207:57] that in there. This is now testing. This
[207:59] is going to test. This is now testing.
[208:03] And then we just have these two over
[208:04] here which are in the process of
[208:06] building. This here ran into an issue
[208:08] with one of the scrapers. So, it's
[208:10] decided to pivot and then use an Appify
[208:11] API token. That's cool. I don't mind
[208:13] that. This here on the left is now doing
[208:15] some debugging and so on and so forth.
[208:17] That's okay. I don't need to be a part
[208:18] of this. All I'm doing is I'm just
[208:19] overseeing. And if any one of these
[208:21] workers needs me for anything, I'll
[208:23] provide it. All right. And we are just
[208:24] testing across the board. We got 50
[208:26] leads running for most of these tests.
[208:29] Some of them are 10. That's okay. I'm
[208:31] seeing this task over here is running
[208:34] into some issues. Namely, the Apollo API
[208:36] key that I provided earlier was for a
[208:37] totally free account. So, it doesn't
[208:38] look like I can it can actually go and
[208:40] enrich them. This one here on the left
[208:42] looks like it's pretty solid. So, it's
[208:44] since found a verified email address.
[208:46] That's pretty cool. I did uh no work
[208:48] here. I just let it run. This over here
[208:51] is doing a batch email scrape. And this
[208:53] right over here is now running a
[208:55] pipeline test with a fixed client. I've
[208:57] actually forgotten what's going on over
[208:58] here on the left. So I'll say describe
[209:00] what is occurring top to bottom. So this
[209:03] is scraping the Google Places API for
[209:05] terms like HVAC contractors, heating
[209:07] contractors. It's going across 50 Tex
[209:10] and cities. Then it gives me a big list
[209:12] of leads. It's then enriching with
[209:14] emails before exporting to Google
[209:15] Sheets. So, that's pretty cool. Let's
[209:17] run this on a test of 50. Meanwhile,
[209:20] over here on the right, we did run it on
[209:22] a test of 50, and it looks like we ended
[209:24] up with 26 email addresses. That's
[209:26] pretty badass. I should note that not
[209:28] all of these are valid. I'm seeing here
[209:30] one of them is for somebody that works
[209:31] at Neurolink. So, probability of that
[209:33] being a valid lead is kind of off. Um,
[209:35] I'm going to want to double check that.
[209:37] So, I'm going to go back here and I'll
[209:38] say, I noticed one of the leads was for
[209:40] Neurolink. How are these filters? Are
[209:42] they super accurate? Make sure to double
[209:44] check. Meanwhile, this one over here on
[209:46] the lefth hand side is doing some
[209:47] enrichment. This is now actually testing
[209:50] to see how many of these leads are HVAC
[209:53] related. So, we're seeing a bunch of
[209:54] these are HVAC related. A bunch of these
[209:56] are not HVAC related. So, uh the search
[209:58] that we're going to be providing here is
[210:00] presumably going to have to be a little
[210:01] bit more specific. I can't just like,
[210:03] you know, head over to LinkedIn Sales
[210:05] Nav, copy and paste something with a
[210:06] term HVAC, and then have it work 100% of
[210:08] the time. Okay. on the right hand side.
[210:10] This is now giving me some highlevel
[210:11] instructions on how I can uh you know do
[210:14] the search better. So that's nice. HVAC
[210:16] and refrigeration equipment
[210:17] manufacturing. Why don't I actually go
[210:18] ahead and just do this? So I'm going to
[210:19] remove this keyword HVAC. And what I
[210:21] want to do is click industry.
[210:24] Go down here.
[210:27] I see HVAC right over there. I'm going
[210:28] to include that. This is 341 results. So
[210:32] then I'm just going to copy this and
[210:33] paste this back in. Let's run a test on
[210:36] 50. Cool. Cool. Cool. Looks like this
[210:39] lead flow here worked really well. 18
[210:41] out of 20 businesses had websites. 13
[210:43] out of 20 had emails. Meanwhile, we
[210:45] happen to get Satia Nadella, the CEO of
[210:47] Microsoft's email over here. That's
[210:49] always fun. Okay, cool. And now we have
[210:51] a whole list of steps right over here in
[210:53] the middle. So, that's awesome. Gives me
[210:56] a brief description of what's going on.
[210:57] And yeah, I mean, I like this. So, why
[210:59] don't I actually see a result? Where are
[211:02] the leads? Looks like it's going to find
[211:04] me the leads. Text businesses with
[211:06] emails. Then it has them all over here.
[211:07] This is cool. So hopefully it's clear at
[211:09] this point. I mean I could do pretty
[211:10] much whatever I wanted, right? And like
[211:11] we've actually gone through and explored
[211:12] a tremendous amount of search space in a
[211:14] very short period of time. I could for
[211:15] instance just um send the same message
[211:17] to all five. Hey, show me the results in
[211:19] a Google sheet. You know, I could then
[211:21] standardize the test and just ask all of
[211:23] them to do 20 leads simultaneously and
[211:26] then I could just have them really
[211:27] quickly test to see which one delivers
[211:29] me the highest degree of accuracy on the
[211:31] leads. Um I could also disqualify a
[211:33] couple. Don't really like this one. I
[211:35] mean like it it's working. It just found
[211:36] me three. uh with verified emails, but
[211:38] I'm seeing that it's using an Apollo
[211:40] endpoint, which isn't 100% right. Um
[211:42] it's kind of crazy because we're not
[211:44] supposed to be able to use Apollo in
[211:45] this way. We should be having to pay a
[211:47] fair amount of money. And you know, I
[211:48] think there are a lot of things that
[211:49] realistically anybody could do. You
[211:50] could also just use all five of these,
[211:51] but yeah, I just wanted to show you guys
[211:53] what that looks like. So, what I'm going
[211:54] to do is I'm just going to pretend that
[211:56] I've now selected three and I'm going to
[211:57] say excellent. turn this into directives
[212:02] or merge these directives executions
[212:05] with the main branch your approach one
[212:09] then update everything to ensure that
[212:13] the file paths etc are correct that's
[212:16] actually really cool I wasn't expecting
[212:18] this to do anything with Apollo um I
[212:20] mean I fed it in my API key which is
[212:22] free but uh yeah normally they don't
[212:24] allow you to see any of that and finally
[212:26] it ended up finishing and it since
[212:28] merged my directives with the main
[212:30] directives folder. So I actually have
[212:32] the Texas SOS Legen directly here. What
[212:34] I could do now is I could test it. I
[212:36] could rerun it. I could optimize it by
[212:37] just asking it to do things faster and
[212:39] faster and faster. And yeah, I was able
[212:41] to accurately assess that this is the
[212:43] flow that I wanted in light of five
[212:45] other ones. Total cost to this was no
[212:48] more time than it would have taken me to
[212:49] do the first. Sure, I did spend some of
[212:52] my um in this case Claude Max plan
[212:54] usage, although keep in mind that we're
[212:56] talking cents on the dollar here. I also
[212:58] spent a few dollars on Google Places
[212:59] API. You know, I would have spent a few
[213:01] dollars over here. I spent a few HTTP
[213:04] calls over here and then, you know, some
[213:05] Ampify tokens over here. Realistically
[213:07] though, this allows you to do 5x the
[213:10] tests for like just a couple of dollars
[213:12] per workflow build. Way cheaper than
[213:14] anything um that N8, make.com or Zapier
[213:17] would have charged you just for like
[213:19] development and testing costs alone. And
[213:21] we get to do it through self annealing
[213:23] and have a very robust reliable workflow
[213:25] to boot. So, how do you actually improve
[213:27] these workflows over time? And when I
[213:28] say this, I mean practically. Like, how
[213:30] do you actually cut through the noise
[213:31] and then do this thing in a way that is
[213:32] consistent and reliable? Well, you just
[213:34] ask. I actually literally just say, can
[213:37] you make this faster? Can you make this
[213:39] cheaper? Over and over and over and over
[213:40] again, like 30 times. I say, list 10
[213:42] approaches to make this thing cheaper.
[213:44] List 20 approaches to make this thing
[213:45] faster. Most of the approaches will not
[213:47] work, but I will use my human judgment.
[213:49] And then after it opens up and gives me
[213:51] 20 possible opportunities, I then just
[213:53] pick one that I think makes the most
[213:55] sense. And then we proceed with that.
[213:56] Then I just repeat the process over and
[213:58] over and over again until my workflow is
[214:00] now significantly faster and
[214:02] significantly more optimized. That said,
[214:03] cuz I think a lot of people have
[214:04] probably stumbled on this, um, I do have
[214:06] a rule and my rule is the order of
[214:08] magnitude rule. I don't actually do this
[214:11] anymore unless I can get at least a 10
[214:14] times improvement in a key metric. For
[214:16] instance, time, cost, or accuracy
[214:18] because a workflow running in 3 minutes
[214:20] versus 2 minutes, well, technically it's
[214:22] a 33% improvement or whatever, it's not
[214:24] actually meaningfully better for me. and
[214:26] the amount of time that I take to
[214:28] implement it multiplied by the
[214:29] introduced error risk by doing what is
[214:32] typically an approach that trades off
[214:34] time, money or accuracy for speed
[214:38] against each other means that I'm
[214:41] usually losing. If you think about it,
[214:43] it's basically what's the metric we
[214:44] want? We want like time, right? And so
[214:46] the degree to which the time gets better
[214:48] is sort of related to the degree to
[214:51] which maybe the cost and the accuracy go
[214:54] down. And so the amount of time that I
[214:57] spend on this I in addition to like the
[214:59] introduced error rate and stuff like
[215:01] this means that this only really makes
[215:02] sense to do if there's a very clear path
[215:04] to making your flow 10 times better.
[215:06] What's an example of this? Um I used to
[215:08] scrape tons of leads using a serial
[215:11] approach and I found that it took
[215:12] forever. My serial approach was
[215:14] something like you know 20 minutes for
[215:16] 2k leads. If you do the math on that
[215:19] that's like I don't know 100 leads a
[215:21] minute or so. Um, I came through and I
[215:23] tried optimizing the hell out of the
[215:24] serial approach with like every way way,
[215:26] shape, and form that I could. I tried
[215:28] like changing the compute that I was
[215:29] using. I tried changing like the Ampify
[215:30] actors I was using. I tried changing
[215:32] like the API requests that I was making
[215:33] to Google Sheets and stuff like that.
[215:35] And I was only really able to get this
[215:36] down to maybe 15 minutes. That is like a
[215:39] 25% improvement in time of course, but a
[215:41] lot of the time this is even my
[215:42] bottleneck. Like it doesn't actually
[215:42] matter if it takes 15 minutes or 20
[215:44] minutes because I'm not utilizing the
[215:45] leads 100%. Anyway, what I ended up
[215:47] finding was I ended up finding an
[215:48] approach that batch parallelized them.
[215:50] So sent instead of um 2k leads for 20
[215:53] minutes, it basically sent 100 leads at
[215:55] a time 20 times and then it finished in
[215:58] approximately 1 minute. Um this for
[216:01] example is a 20 times improvement. This
[216:04] is something that I'd actually do. Um
[216:05] that actually worked. But this whole
[216:07] like I don't know this whole like uh
[216:09] detour or rabbit hole thing was just a
[216:11] total waste of my time because this
[216:12] turned the flow into an unreliable mess.
[216:14] So my rule is I basically just like I
[216:16] don't make small optimizations anymore
[216:18] because they reduce accuracy and
[216:19] reliability for marginal gains. I would
[216:21] only do this on something that I
[216:22] actually see there being an order of
[216:24] magnitude possible improvement. What are
[216:25] some examples? It's like moving from
[216:27] software encoding to hardware encoding.
[216:29] You don't need to know what that means.
[216:30] Just make sure that when you ask the
[216:31] model and you see words like that, it's
[216:33] like okay, I should probably use the
[216:34] hardware encoding. Parallelizing or
[216:36] using what's called like multiple
[216:37] threads or using multiple service
[216:38] workers simultaneously. These are things
[216:40] that usually do provide like an order of
[216:42] magnitude jump. Um, sometimes you can
[216:44] like fundamentally change the order of
[216:46] operations in a workflow. Uh, but in
[216:48] general, unless the model expects that
[216:49] this is going to provide at least a 10x
[216:51] boost, I don't really recommend doing
[216:53] it. What is really cool is that every
[216:54] workflow that you build does become a
[216:56] permanent asset in your library. And I
[216:58] mean this both in the way of directives
[217:00] and execution scripts as well. Your
[217:02] library ends up infinitely reusable. If
[217:04] you think about it, you could open up
[217:06] any workspace in any IDE or agent model.
[217:09] You could also copy directives and
[217:10] execution scripts over to anybody else's
[217:12] workspace like your friends or your
[217:13] colleagues. You could put it on GitHub
[217:15] with like GitHub code spaces, something
[217:17] I'm going to talk about soon. You could
[217:18] reuse automations the exact same way
[217:20] that you do them in, you know, drag and
[217:22] drop no code tools like naden, make.com,
[217:24] or gum loop, but you just do that with
[217:26] natural language instead. Your
[217:28] blueprints, if it makes sense now, is
[217:30] just like a bunch of words on a page,
[217:31] which are much, much more portable. And
[217:33] over time, your ID will become basically
[217:35] a giant treasure chest that you can
[217:37] deploy anytime you want, anywhere you
[217:39] want. So, for instance, what my library
[217:41] can do right now is it can do automated
[217:43] lead scraping, automated email
[217:44] enrichment, automated personal replies
[217:46] on campaigns that I run because we're
[217:47] predominantly like a cold email agency.
[217:49] I can initiate high quality voice agent
[217:51] calls. I literally just say, "Hey, call
[217:52] this person. Hey, I want you to call
[217:53] people on this list. Hey, I want you to
[217:55] split to like 20 20 uh threads and then
[217:57] call 20 people." I could do automated
[217:59] proposal generation. I could do slide
[218:01] deck creation that actually matches my
[218:02] tone of voice and it looks pretty good.
[218:04] Um, and all of it is customized to how I
[218:06] communicate. It is not generic AI slop.
[218:08] Um, so it's pretty cool. Obviously, I
[218:10] didn't build all this stuff overnight.
[218:11] It took me a fair amount of time, few
[218:12] days, well, a few weeks now to really uh
[218:15] put the finishing touches on all these.
[218:16] But yeah, I mean, at the end of the day,
[218:18] this thing can basically be your
[218:19] terminal for life. A real example from
[218:21] my actual day-to-day was automating my
[218:23] school posts. So, I kept forgetting to
[218:24] post a weekly community call thread. I
[218:26] did it three weeks in a row, which is
[218:27] really embarrassing, especially because
[218:28] I uh like to make it clear that if I
[218:30] don't do like the foundational
[218:32] fundamental things that I promise people
[218:34] I will do, then why why the hell am I
[218:36] entitled to their money? So, I gave a
[218:37] bunch of people refunds. Um, I asked my
[218:39] agent, Claude Opus 4.5, at the time if
[218:42] automating this was straightforward. I
[218:43] had never even really thought of this
[218:44] before, but I was basically just like,
[218:45] "Hey, I keep forgetting about this
[218:47] thing. Man, I really suck. Any ideas?"
[218:48] And then it's just like, "Oh, yeah, we
[218:50] could totally automate that." So, it
[218:51] went and found a reex uh pre-existing
[218:53] school system that I had built um which
[218:55] just handled like the authentication and
[218:56] the logging in. Then it built a simple
[218:58] scraping spec and it figured it out in
[218:59] like 3 minutes flat and I automated my
[219:02] school post in 3 minutes flat using a
[219:04] simple schedule timer which I'll talk
[219:05] about later. So now it just happens for
[219:07] me which is incredible and it's super
[219:08] easy and it's super straightforward. Um
[219:10] you can solve so many tiny little
[219:12] problems in your life using tools like
[219:14] this. So once you've built like
[219:16] individual workflows that work really
[219:17] well, then you eventually transition to
[219:19] what I call metadirectives. So at the
[219:21] end of this, what you will essentially
[219:23] have is you will essentially have okay
[219:26] giant families of workflows
[219:29] that do various things. For instance, I
[219:32] will have like a marketing workflow
[219:34] umbrella. And this is a family of
[219:36] workflows that does things like, you
[219:38] know, scrape leads, create ad copy, you
[219:42] know, do uh voicemail drops, I don't
[219:44] know, whatever the heck, right? And so
[219:46] what this umbrella workflow, this
[219:48] metadirective does is it just ties them
[219:50] together. So, for instance, if you have
[219:51] a bunch of separate workflows for, I
[219:53] don't know, a welcome email, the setup
[219:54] of a workspace, and the copyrighting of
[219:55] an email, this is sort of like an
[219:57] onboarding thing, right? So, you could
[219:58] just tile all these together with a new
[220:00] client workflow that just does all them
[220:01] in sequence. I recommend storing the
[220:03] directives separately in order to make
[220:04] this happen. I don't recommend just like
[220:06] having a giant new client workflow
[220:08] that's like four quadrillion lines
[220:10] because it's much easier and more
[220:11] maintainable for the model to load only
[220:12] what it needs in context at any one
[220:14] particular time. But this becomes really
[220:15] powerful because they just chain all of
[220:17] the existing capabilities together.
[220:18] Instead of you having to go like 1 2 3,
[220:21] you know, you have like four or five
[220:22] workflows. What you do is you just turn
[220:24] that into one workflow and then every
[220:25] time you want all of these done in
[220:26] sequence, you just call the big
[220:28] workflow, not individual workflows. It
[220:30] also means that when you prompt the
[220:32] model and use it as like an assistant or
[220:33] whatever, you could just say, "Hey, I
[220:34] want you to do X, Y, and Z onboarding
[220:36] workflow." And then you can just step
[220:37] away, have a freaking nice cup of tea or
[220:39] something like that and come back and
[220:40] everything's okay. You don't actually
[220:41] have to get like interrupted all the
[220:42] time. And yeah, when you combine that
[220:44] with the infinite reusability of these
[220:46] workflows, this becomes really, really
[220:47] powerful because then you can just send
[220:49] your new client workflow to the other
[220:51] three account managers on your team and
[220:52] then they can just run it every time
[220:53] they get a new client. or as I'm going
[220:55] to show you later, maybe you could
[220:56] attach that to a schedule trigger or
[220:57] some sort of web hook so that it just
[220:59] runs autonomously without you. Hopefully
[221:01] that makes sense. Now, we're starting
[221:02] one of my favorite topics in directive
[221:04] orchestration execution and just agentic
[221:05] workflows in general, and that's this
[221:07] idea of self annealing. First, let's
[221:09] talk about annealing in a general sense.
[221:11] Annealing is the process of heating a
[221:13] piece of metal and then slowly cooling
[221:15] it down. Basically what happens is
[221:17] previously the molecules in the metal
[221:19] are kind of all over the place. But what
[221:21] happens when you heat up a metal is they
[221:23] end up actually moving to like their
[221:25] highest or rather lowest energy state
[221:27] and they end up looking kind of like a
[221:29] crystal lattice which is really badass.
[221:31] And then what we do is we cool it down
[221:33] very quickly which then hardens this and
[221:35] sets it into you know some really strong
[221:38] robust piece of metal. Blacksmiths and
[221:40] so on have been doing this for many many
[221:41] generations. It removes a bunch of these
[221:43] internal weird misconfigurations of the
[221:45] atoms and it creates a really strong
[221:47] more stable structure. So people do this
[221:49] with swords and you know uh uh devices
[221:52] and and pieces of metals all the time in
[221:53] real life. It's cool as hell. And today
[221:55] I wanted to talk about a similar concept
[221:57] in agentic workflows. So what if we had
[221:59] the ability to stress test our workflows
[222:02] as well to make them significantly more
[222:04] resilient? Turns out we do. When we
[222:07] build instruction sets, prompts or
[222:09] directives for our agents. I want you to
[222:11] think of them as looking something like
[222:13] what we see on the left hand side here.
[222:15] In short, these are pretty rough. We
[222:17] have some idea of how we want the
[222:19] workflow to develop. Maybe we want it to
[222:22] start here and then go over here and go
[222:25] over here, here, and then here. But we
[222:28] don't really have uh uh you know a
[222:29] strong mechanism to do it. All we really
[222:31] have so far is just an outline. You
[222:33] know, when we when you say step one, do
[222:35] X, step two, do Y, and step three, do Z,
[222:38] all this really is is just a couple of
[222:40] bullet points on a piece of paper. And
[222:41] even if you have an agent like produce a
[222:42] workflow for you uh in a directive form,
[222:45] it's not super tight. What self-
[222:47] annealing does is basically every single
[222:49] time we run into some error or issue or
[222:52] opportunity for improvement, the system
[222:56] reinforces that flow. And so if this on
[222:59] the left hand side is what we kind of do
[223:00] on the first day, this on the right hand
[223:02] side is after maybe 60 days of you using
[223:04] an agentic workflow. Instead of it just
[223:07] being this small little piss ant line on
[223:09] the left, we have a super strong battle
[223:12] hardened protocol. You know, every one
[223:14] of these little shields is some form of
[223:16] retry logic. You know, uh it's so much
[223:18] beefier. There's like validation steps
[223:20] that that go into place. Maybe you have
[223:22] human in the loop at specific steps you
[223:24] didn't realize that you needed before
[223:25] and so on and so forth. And so you know
[223:27] if I'm somebody designing a workflow
[223:29] despite the fact that I start over here
[223:31] on the left hand side at the end of the
[223:32] self- annealing process my workflow
[223:34] actually becomes super super robust and
[223:35] very resilient as well. So that concept
[223:37] is self- annealing instead of brittle
[223:40] systems that break every time that you
[223:42] error out like with you know nadn or
[223:46] make or whatever. When you build these
[223:48] systems they just strengthen over time.
[223:51] The secret ingredient is adding a level
[223:54] of thoughtful error handling to your
[223:56] system prompt. And the whole idea is
[223:59] when you do this, it will learn and it
[224:00] will adapt. Problems essentially stop
[224:03] being like problems in the error sense
[224:05] and they start being opportunities for
[224:06] you and the model to build edge cases um
[224:09] error handling and sort of unexpected uh
[224:12] uh steps in that you just didn't really
[224:13] understand the first time because a lot
[224:15] of the time the only way to know is just
[224:17] by doing a bunch. So when you enter the
[224:19] self annealing loop essentially what
[224:21] happens is there will be some sort of
[224:23] error. Immediately after you will
[224:25] diagnose where the error is coming from
[224:28] then you will attempt some sort of fix.
[224:31] After the fix you will then update. So
[224:33] you'll actually update the workflow the
[224:36] execution script itself and then you'll
[224:37] just rotate over and over and over and
[224:39] over and over again. And then finally
[224:40] eventually this stops erroring out right
[224:42] and then it becomes successful. And when
[224:45] it becomes successful, all we do is we
[224:47] just do some sort of documentation
[224:49] upgrade. And so we let the directive
[224:51] know, hey, you know, this is a common
[224:53] issue that previously used to happen a
[224:54] lot. We've since reinforced against it,
[224:56] and it's a lot better. And then the next
[224:57] time the loop uh fixes, and let's say
[224:59] this eventually goes into some sort of
[225:01] error. Well, guess what happens? We just
[225:04] run the same thing. We go through an
[225:06] error, then we diagnose, then we fix, or
[225:08] attempt to fix, I should say, and then
[225:10] we update. And then we just loop over
[225:12] and over and over again until we can no
[225:14] longer loop. Okay, so this is really
[225:16] like that four-step process. The agent
[225:18] will continue until the operation
[225:19] succeeds or it hits like some super
[225:21] unfixable wall, just something that like
[225:22] actually requires a human being even
[225:23] when something is unfixable. You'll find
[225:25] that an agent often will find a creative
[225:27] workound. So like for instance, if one
[225:29] of the things that you asked for is like
[225:30] you asked for 50 leads or something or
[225:32] maybe I always use leads cuz you know
[225:34] I'm just super in that business. But
[225:36] let's just take a step back here and say
[225:38] you are looking for like 50 blog posts
[225:40] on a subject, right? And your whole job
[225:42] is you want to like take these blog
[225:44] posts and then use them to create
[225:45] something. Your definition of done is
[225:47] you get 50 blog posts from your scraper.
[225:49] Well, let's say the scraper only returns
[225:51] 40. This loop will start and continue.
[225:54] And maybe the reality is there just
[225:55] aren't any more blog posts on the
[225:57] internet about this. Well, your model
[225:58] finds a creative workaround by maybe
[226:00] changing one of the filters in how it
[226:02] pitched the first thing. and it lets you
[226:03] go from 40 to 50 technically
[226:06] accomplishing what you were looking for
[226:07] despite the fact that it is a
[226:08] fundamentally different process. Now
[226:10] you're using maybe a different set of
[226:11] filters and then although it didn't work
[226:13] 100% it worked 80% the model will then
[226:15] give you a notification or ping you or
[226:17] something to be like hey this mostly
[226:18] worked know if this filter is okay too.
[226:20] So then you provide some feedback or
[226:22] whatever and then it actually cements
[226:23] the fact that this filter is okay too
[226:24] preventing it from ever happening again.
[226:26] And in that way every cycle will leave
[226:28] the system a lot more robust and
[226:29] reliable than it was before. So, as a
[226:31] business owner, somebody that's been
[226:32] doing stuff like this for the better
[226:33] part of the last decade, I like thinking
[226:35] about agents and agentic workflows as
[226:37] basically many employees. And in
[226:40] business, when you hire a bunch of
[226:41] people, you quickly realize that you can
[226:43] bin human beings into two camps. You
[226:45] could have employee A, who I'm going to
[226:47] consider the blocker, and you can have
[226:48] employee B, who I'm going to consider
[226:50] pretty self-capable. So, in the
[226:51] situation of employee A, anytime that
[226:53] they have a problem, and I've hired a
[226:55] lot of people like this, that problem is
[226:57] now your problem. So, hey boss, I tried
[227:00] doing XYZ, couldn't make it happen.
[227:02] Could you help me with this? Meaning,
[227:05] this is the sort of person that cannot
[227:06] proceed without your intervention. Every
[227:08] time they run into an issue, well, now
[227:10] it's your issue as well. All work grinds
[227:12] to a halt, not just theirs. This is the
[227:14] sort of person that makes the same
[227:15] mistakes over and over and over again,
[227:16] doesn't seem to learn, and ultimately
[227:18] you become the bottleneck for their
[227:19] productivity. They almost require you to
[227:21] micromanage them in order to succeed.
[227:23] I'm sure there's some business owners
[227:24] here that are watching this video. This
[227:26] happens very often and this is one of
[227:27] like the easiest and simple tells that
[227:29] you probably shouldn't hire a person
[227:30] that you know runs into issues and can't
[227:32] actually self-mmitigate them. Employee B
[227:34] on the other hand is a star performer.
[227:36] They encounter the same problems but
[227:37] they have a simple SOP. The SOP is well
[227:40] even if I don't know how to solve the
[227:42] problem. I'm going to try on my own
[227:44] first and so they'll only escalate when
[227:46] it's absolutely necessary. They respect
[227:48] your time. They document solutions when
[227:50] they run into them that your team so
[227:52] that your team never ever hits the same
[227:53] issue twice. They make a a statement in
[227:55] your Slack. Hey guys, ran into XYZ
[227:57] problem. Just wanted you all to know
[227:58] that you could fix this by doing XYZ
[228:00] solution. Sometimes they even run a
[228:02] quick session to teach others what they
[228:03] learned. Now, if I gave you a choice
[228:04] between these two, which one would you
[228:06] choose? Obviously, you'd choose employee
[228:09] B. And I think most business owners
[228:11] would too. Well, self annealing agentic
[228:13] workflows behave like employee B. They
[228:16] don't behave like employee A. And so,
[228:18] we're giving them a level of autonomy
[228:20] that I think a lot of people previously
[228:21] would have considered insane.
[228:24] But I think the definition of insane is
[228:25] going to change pretty quickly as these
[228:27] models get more and more intelligent.
[228:28] How do you actually enable this cool
[228:30] process? It really just boils down to a
[228:32] small set of instructions and a prompt.
[228:34] You just add to your cloud MD, Gemini
[228:36] MD, agents MD, whatever a key thing that
[228:38] just changes its opinion uh essentially
[228:41] like the default mode of problem
[228:43] solving. And the default mode of problem
[228:44] solving with these programming agents is
[228:46] usually, hey, if I can't do something,
[228:47] return it to the user and ask them what
[228:49] they'd like me to do. which makes sense
[228:50] because for the most part this these
[228:52] sorts of models are used predominantly
[228:53] in like enterprise coding applications
[228:55] now where like a small change can
[228:56] actually result in a big downstream
[228:58] problem but like if we're building
[228:59] simple agentic workflows that are
[229:00] modular and like unit testable uh and
[229:02] then we're just using them in our IDE
[229:04] like that doesn't apply to us.
[229:08] So all we say is something along the
[229:09] lines of hey when you encounter an error
[229:11] first diagnose it then fix it then
[229:14] update your scripts and directives to
[229:15] handle similar errors in the future. Now
[229:17] I always add is something like try super
[229:19] duper hard before escalating to the
[229:21] user. What happens over time is the
[229:23] initial workflow will look very
[229:25] different on the initial implementation
[229:26] than it does you know several weeks
[229:28] later. Retry logic in instances where
[229:30] one-off failures occur will be added
[229:32] automatically. It'll do things like um
[229:35] self retry loops. It'll do things like
[229:38] um if you guys are in the programming
[229:40] space, you'll know there's stuff like
[229:41] exponential backoff.
[229:44] There's various forms of error handling
[229:45] like logging and so on and so forth. And
[229:48] because it is hyper optimized to program
[229:51] really well and understands these things
[229:52] outside of the box, it'll just do them
[229:53] for you. Which means edge cases that you
[229:55] never anticipated get handled as your
[229:56] agent encounters them. Efficiency
[229:58] improvements occur organically. You
[230:00] know, bulk endpoints, parallelization,
[230:02] multiple workers. If there's like a a
[230:04] request that you made initially in your
[230:05] directive, I want this to occur under 5
[230:06] minutes after you run this every single
[230:08] time. Just make sure to like see how
[230:09] long it took. If it takes more than 5
[230:10] minutes, IDate solutions. If you have
[230:12] simple little blockers in there or
[230:14] decision or router points uh in there,
[230:16] agents will naturally do a lot of this
[230:17] stuff for you, which is really cool. And
[230:18] then obviously you can also just ask,
[230:19] "Hey, make this thing better. Make this
[230:21] thing better. Make this thing better.
[230:22] Make this thing better." In this way,
[230:23] your system continuously optimizes
[230:25] itself without any form of ongoing
[230:27] intervention. Uh which is the coolest
[230:29] thing ever in practice. That said, when
[230:31] you guys start getting really deep into
[230:33] self- analing and you have workflows
[230:34] that do a lot of their work themselves,
[230:37] safety becomes a much bigger portion of
[230:39] the conversation than it ever was
[230:40] before. Like with N8N and Make.com
[230:42] workflows, the biggest potential issue
[230:44] was basically that you just like turned
[230:46] it on and you forgot to turn it off and
[230:47] then it just continued consuming your
[230:49] credits or operations or whatever longer
[230:51] than you realistically wanted it to,
[230:52] which charges costs and so on and so
[230:54] forth. But most APIs, most systems, and
[230:57] most automation platforms now have some
[230:59] sort of built-in detection for this, or
[231:00] at least thresholds that you could set.
[231:02] So, it's not that big of a deal. But
[231:03] with fully autonomous AI, especially AI
[231:05] that were proposing giving total
[231:07] bypassed permission access to a system,
[231:10] safety becomes much more important. I
[231:12] was just reading this thread the other
[231:13] day where somebody let Gemini basically
[231:15] run autonomously for I think it was like
[231:17] 2 days or something like that and you
[231:19] know it checked in and it had some cool
[231:20] little workflow loop where it did this
[231:21] but then when they went back to it they
[231:23] realized that they didn't put it in a
[231:24] container. They basically gave it full
[231:26] system access and then it like deleted
[231:27] their whole like C or D drive. Anybody
[231:30] that's in the know, you delete your
[231:31] whole CR D drive, your computer's
[231:32] basically screwed. You know, you have to
[231:34] do like a fresh install. So that's on
[231:36] your server, right? The thing is you're
[231:38] also giving this thing access to the
[231:40] internet. And so if you have cookies or
[231:41] API keys or whatever, I'm sure you can
[231:44] imagine even if there's like a 0.1%
[231:46] risk. If you just stack up that 0.1%
[231:49] over the course of a very long period of
[231:51] time, okay, this is just uh let's say
[231:54] you know 99.9 raised to the 1,000
[231:57] operations. At the end of this process,
[231:59] there is only a 36% chance that the
[232:02] model will actually do what you
[232:03] initially intended it to do. Despite the
[232:05] fact that on an individual basis, every
[232:07] step was 99.9% um secure and logical.
[232:10] The more steps you have, the basically
[232:12] the larger those error bars become like
[232:14] I've drawn a few times now. So, what
[232:15] this means is we really do have to add
[232:17] at least some sort of uh uh guard rail
[232:20] towards the model so that it doesn't
[232:21] screw things around completely. Now,
[232:23] there are a few simple ones that I do.
[232:24] My processes are never a thousand steps,
[232:26] right? I mean, I might be dealing with a
[232:27] five or 10step process. So, I typically
[232:29] don't have to go much further than this,
[232:30] but if you want really autonomous
[232:32] longunning agents, um you need to
[232:33] develop what are called harnesses for
[232:34] them, which I cover later. But
[232:36] basically, here are four things that I
[232:37] would always do. I would always ask the
[232:39] model to confirm beyond making API calls
[232:41] above a cost threshold. So, a lot of
[232:43] APIs have the ability to check usage.
[232:45] So, I'd actually add like a little step
[232:46] in there that says, "Hey, make sure to
[232:47] check the usage. If you've spent more
[232:49] than, you know, $5 in the last like few
[232:51] minutes, then you should not continue
[232:53] doing this. You should let me know, send
[232:54] me a notification, whatever. Hey, never
[232:57] modify credentials or API keys unless I
[232:59] explicitly tell you to." That's valuable
[233:01] because a lot of the time it'll do
[233:02] things like reformat your API key.
[233:04] Sometimes it'll delete API keys that it
[233:06] thinks it doesn't need anymore.
[233:07] Sometimes, you know, that'll be a big
[233:08] pain in your ass because you have to go
[233:10] back to the platform then reinstitute an
[233:11] API key. Never remove secrets out of ENV
[233:15] files or hardcode them into the
[233:16] codebase. Models are really good at this
[233:17] already, but I always just like having
[233:18] this explicit because if I try and share
[233:20] something with somebody at any point in
[233:21] time and it has like my enthropic API
[233:23] key or whatever, then these guys now own
[233:25] my ass. And finally, although this does
[233:27] eventually run into a limit, I have the
[233:28] model log all self modifications as a
[233:31] change log at the bottom of the
[233:32] directive. What this does is it
[233:33] basically allows me to take a look at
[233:34] any point in time be like, "Okay, so
[233:36] like what was the sequence of of events?
[233:37] What was the order of operations?"
[233:39] essentially. Um, I do this in like
[233:40] GitHub format. So, it's sort of like a
[233:42] commit if you guys know what that means.
[233:43] And it's a really simple just like one
[233:45] paragraph. Uh, well, a lot of the time
[233:47] it's just like a one sentence
[233:48] explanation of the changes that we made,
[233:50] how the changes worked and whatever. And
[233:52] the reason why this is valuable is
[233:53] because like if you're not using version
[233:54] control like a lot of people will not be
[233:56] using uh and I know that for a fact at
[233:58] least you have like a change log that
[233:59] the model can use to go through and see
[234:01] hm before this I was doing X and that
[234:03] was working okay. Then I tried doing Y
[234:04] and Y is working not so good. So let's
[234:06] move back to X. You should also just
[234:08] accept that some rules will occasionally
[234:10] be broken. That's just how these things
[234:11] are. We know that agents are
[234:13] probabilistic at this point. 100%
[234:15] compliance and everything is just not
[234:16] realistic and it's not achievable. So
[234:18] despite our best efforts, there will
[234:19] always be some sort of edge case
[234:22] failure. Although it is getting a lot
[234:24] better with time, obviously this is just
[234:26] a trade-off that we have to accept
[234:27] anytime we're using AI. I mean, AI
[234:29] multiplies our leverage by thousands
[234:31] upon thousands upon thousands of times,
[234:32] right? But in doing so, it also
[234:35] multiplies um accuracy or or reliability
[234:37] issues as well. Again, it's one of those
[234:40] like even if our human workflows are
[234:42] 99.9% accurate, obviously if you run
[234:44] them enough times, let's say a thousand
[234:46] times, these errors compound and then
[234:48] you end up with a total process that's
[234:49] only maybe 36% successful.
[234:51] [gasps and sighs] Well, a human being
[234:53] can typically spot that earlier. But
[234:54] also, a human being typically just
[234:56] doesn't do a thousand operations in a
[234:57] row, right? There'll usually be some
[234:59] sort of check mark or guardrail. With
[235:01] agents, you could do a thousand
[235:02] operations like this. So obviously
[235:03] despite the fact that like our accuracy
[235:05] levels are still really high because
[235:07] we're giving them so much autonomy and
[235:08] because at the end of the day they do
[235:10] lack some context that human beings have
[235:11] and you know a lot of people would argue
[235:13] they're not as intelligent as like the
[235:14] most intelligent human being. This thing
[235:15] is just going to occur and there's just
[235:17] nothing you can do about it. So I plan
[235:19] for graceful recovery not perfect
[235:21] prevention and I'd recommend you do too.
[235:23] Cool. Let's chat about using these
[235:24] workflows. And I just want to make this
[235:26] clear that this program is both about
[235:29] building workflows. Then it's also using
[235:31] said workflows. And the two are not the
[235:34] same. Building a workflow versus using a
[235:36] workflow are two very different things.
[235:38] When I build a workflow, I am having my
[235:40] agent essentially be a programmer for
[235:42] me. When I use my workflows, that's sort
[235:44] of DO, right? The directive
[235:46] orchestration execution idea. My agent
[235:48] is just executing a sequence of steps
[235:49] that a previous iteration of an agent
[235:51] built. So these agentic workflows are
[235:53] mostly about the using side of things,
[235:54] right? like building them while is
[235:56] important and stuff like that, it's just
[235:57] a very small part of actually living in
[235:59] your ID and getting things done. And to
[236:01] that point, I have an important thing to
[236:02] say. The interface to everything is now
[236:06] just a text box. So my actual day-to-day
[236:09] work occurs almost entirely now through
[236:11] a single text box. It occurs through,
[236:14] you know, anti-gravity or Visual Studio
[236:15] Code. And I just have the agent do
[236:17] everything that I have created
[236:19] painstakingly over the course of the
[236:20] last few weeks using the tools that I've
[236:22] I've set up. So, I'll have it do things
[236:24] like generate, you know, my YouTube
[236:25] thumbnails. I'll have it do things like
[236:27] uh generate scripts and stuff like that
[236:28] that I could send to people. I have it
[236:30] do things like generate pitch decks so
[236:31] that I could send to people that are
[236:32] interested in working with me, generate
[236:34] proposals. I do things like analyze my
[236:36] transcripts and stuff like that. But I
[236:37] don't do it in individual software
[236:39] applications, okay? I don't do it in
[236:41] Fireflies and Google Drive and Panda Doe
[236:45] and, you know, Quiller and all these
[236:47] other platforms. I literally just do it
[236:49] all through a single text interface. And
[236:51] this is just the way that high leverage
[236:53] work is now going to be done, at least
[236:55] until we come up with a better
[236:56] alternative, which may come in some
[236:58] time. But I wouldn't hold out on it. For
[237:00] a lot of people, a single text box feels
[237:02] like a downgrade. Cuz if you think about
[237:04] it, we've spent decades learning
[237:06] software through visual interfaces and
[237:08] menus. And GUIs, graphical user
[237:12] interfaces, are basically the current
[237:14] standard. If you contrast that to typing
[237:16] and stuff like that, a lot of people
[237:18] also consider it really slow and tough
[237:20] compared to, you know, clicking buttons
[237:21] and whatnot that they're used to, right?
[237:23] Sometimes people type at 50, 60, 70
[237:25] words per minute. I have some family
[237:26] members that can't type it more than 20
[237:28] words per minute. Obviously, that is
[237:29] very slow relative to dragging stuff
[237:31] around and clicking buttons and stuff
[237:32] like that. So, there is no obvious right
[237:34] way to do this. It's very open-ended and
[237:36] unfamiliar, and I'm sure eventually
[237:38] we'll converge on like a really cool
[237:40] visual thing that combines the best of
[237:41] both worlds. But there are ways to make
[237:44] doing a lot more natural and efficient,
[237:45] which I want to talk about. The first is
[237:47] just to switch to using voice
[237:48] transcription tools. In case you guys
[237:50] didn't know, you can now just say
[237:51] whatever you want to your computer, and
[237:52] there's like a 99.9% chance that it will
[237:54] understand that and be able to turn that
[237:56] into text. The reason why this is
[237:58] valuable is because the average typing
[237:59] speed is 50 to 70 words per minute,
[238:00] which is really slow bandwidth. The
[238:02] average speaking speed is 150 to 200
[238:04] words a minute, which is three to four
[238:06] times faster. You guys have been
[238:07] listening to me talk at between 150 to
[238:09] 200 words a minute on average. Sometimes
[238:11] I'm a little bit slower, maybe around
[238:13] like 130. Other times I'm a little bit
[238:15] faster, maybe around 220 or so. But in
[238:17] general, I'm speaking maybe three times
[238:20] faster than most human beings type,
[238:21] which is very, very important. Nowadays,
[238:23] models are pretty smart. So, you don't
[238:25] even need to really organize your
[238:26] thoughts in a hyperspecific way. Like
[238:27] back when I was using GPT3, okay, back
[238:29] in the uh the good old days, you had to
[238:31] be extraordinarily precise and concise
[238:33] with your prompts because even 10
[238:34] additional tokens could really really
[238:36] screw up the intelligence and the
[238:37] steerability of the model. Nowadays
[238:39] though, I could have prompts that are
[238:41] thousandword text dumps where I just I'm
[238:43] in my car driving somewhere. I click the
[238:44] voice transcribe tool and then I just
[238:46] talk. And it does a really good job at
[238:47] turning that into something useful. The
[238:48] highest bandwidth way of communicating
[238:50] with computers, at least right now, is
[238:51] the following. Nobody really talks about
[238:53] this, but you transcribe your text as
[238:55] input, which gets you to route 200 words
[238:57] a minute. So my input bandwidth is now
[238:59] 200 WPM. And then you don't like have it
[239:02] say stuff to you like you do with like I
[239:04] don't know the chatbt voice call or
[239:06] whatever. Instead, you just read as the
[239:08] output because most people can actually
[239:09] read between 300 to 500 words per minute
[239:11] if you skim. And most people will skim
[239:13] in some way, shape, or form. Some people
[239:14] can go much faster to like a thousand.
[239:16] And in that way, you have like 200 word
[239:18] per minute input, 1,000 word per minute
[239:21] output, you know, in terms of skimming
[239:22] to relevant materials. Um, the old way
[239:25] of doing this is like 50 to 70. And then
[239:27] if you're doing voice, it'll be, you
[239:29] know, like 200. So, what we're doing
[239:30] here is we're basically quadrupling our
[239:32] input um at at at both sides of this. So
[239:34] this is like a 3 to 5x and this is like
[239:36] a 5x at least. So maybe like a quadruple
[239:38] I would say. Um I would recommend just
[239:40] doing that moving forward. It's way
[239:41] simpler. The only situation which I
[239:43] actually type stuff now is if I like
[239:44] absolutely have to because there is some
[239:46] hypersp specific file that I need to
[239:48] reference on my computer somewhere. And
[239:49] even then I'll usually just like copy
[239:50] the name and paste it manually. From
[239:52] here on out when I say the word prompt
[239:53] assume I'm just generating all this with
[239:55] my voice. And then you guys have also
[239:56] seen me do this on multiple demos. But
[239:58] um I will proceed to assume that you
[239:59] guys know that. How do you actually use
[240:01] workflows? Well, it's really simple.
[240:02] Hopefully you guys have already seen. We
[240:04] just ask for it. There's no need to
[240:05] memorize the exact name of the
[240:07] directive. Agent typically knows the
[240:09] directives exist because we've included
[240:10] that in our system prompt and it'll scan
[240:12] for matches automatically. You do of
[240:14] course need to provide some data um
[240:16] specifically that your directives input
[240:17] schema requires. So if your directive
[240:20] says, hey, you know, I want you to
[240:21] include uh I don't know the name of a
[240:23] person or something like this and we
[240:25] need the name of the person in order to
[240:27] generate some form of proposal or
[240:28] something. And if you say, "Hey, just do
[240:30] the thing." It'll look at it and be
[240:31] like, "Hey, you're currently lacking
[240:32] this input." So, like, "What's the name
[240:33] of the person you wanted? Let me know
[240:34] and I'll I'll create that for you."
[240:37] Really, this is just like ordering food,
[240:38] right? Kitchen needs to know what dish
[240:39] any modifications or whatever. You can't
[240:41] just say, "Hey, get me food." You need
[240:42] to be like, "Hey, you know, can you can
[240:44] I have like the hamburger with a side of
[240:45] fries, please?" Like, there's a level of
[240:47] specificity here. You don't have to go
[240:48] super deep, but you also don't need to
[240:50] overthink it. I'm pretty specific with
[240:52] my requests that I know have specific
[240:54] input methods. So, like in the case of
[240:57] getting me some leads, I can absolutely
[240:58] just say, "Hey, get me some leads today,
[241:00] obviously, it's going to ask me a bunch
[241:01] of questions and then I'm going to have
[241:02] to like feed those questions in and then
[241:04] I can kind of mess about with my
[241:05] directive, right?" So, I much rather
[241:06] say, "Hey, scrape 200 HVAC companies in
[241:08] Texas, then verify the emails,
[241:10] personalize them, and then give me the
[241:11] Google sheet." This takes, you know, 2
[241:12] seconds longer than the first version,
[241:14] but because I'm at the helm of the ship,
[241:16] I'm able to steer it into a much uh more
[241:18] straight line direction to what it is
[241:20] that I want. The more steps you put in
[241:22] an AI's hands, the more chances for
[241:24] errors that it has. Remember that error
[241:25] rates multiply. If I had, you know, a
[241:27] 90% chance doing the first thing
[241:29] correctly and then a 90% chance doing
[241:30] the second thing correctly, um, you
[241:32] know, I would have a, I don't know, I
[241:34] guess a 081% total chance. Ideally,
[241:36] we're dealing with higher rates, but let
[241:37] me just show you how that transforms,
[241:39] right? If I give it everything I need
[241:40] immediately, I now have this is a 90%.
[241:44] Let's say, you know, in the first one, I
[241:46] say get me leads. Well, what happens? It
[241:50] interprets my request as saying, okay,
[241:51] we need to get some leads, so let's go
[241:52] to the directive or whatever. and then
[241:54] it says we don't have any leads. Hey
[241:55] Nick, can you send me some leads? And
[241:57] then I need to provide it leads and then
[241:58] it goes through another process and then
[242:00] gives me a total uh success rate of
[242:01] let's say 81%. Here if I just say you
[242:04] know hey scrape me 200 HVAC companies in
[242:06] Texas, verify their emails and so on and
[242:08] so forth. [gasps] It's only been one
[242:10] step. So I've significantly reduced
[242:12] what's called the compound probability
[242:13] of the error. When you're specific, you
[242:15] also reduce the back and forth. It
[242:17] lowers your overall failure risk and
[242:18] then it's just faster. So I just do it
[242:19] faster that way. If you're not sure
[242:21] what's available, you could just ask
[242:22] like, "Hey, what workflows do I have?"
[242:24] Um, you know, eventually after you
[242:25] design so many directives, it does start
[242:26] being a little bit overwhelming for both
[242:28] you and the model. And obviously, there
[242:29] are some strategies that you could use
[242:31] to help accommodate that, like sub
[242:32] agents, which we talk about later. But
[242:34] for now, just know that, you know, if
[242:35] you don't know what's available,
[242:36] absolutely just ask your model. You
[242:37] could ask the model to do things like
[242:39] refactor your directive base. Hey, are
[242:40] any directives that look really similar?
[242:41] Are there any executions that look
[242:42] really similar? I want you to run a
[242:43] comprehensive refactor and everything to
[242:45] like group them in ways that make sense.
[242:47] You obviously have a lot of freedom to
[242:48] do this in your own. Now, for really
[242:49] complex workflows, I'll usually just
[242:50] paste in the context rather than typing
[242:52] it all manually. Like um you know,
[242:54] rather than asking the model to do some
[242:56] sort of like Fireflies API request for
[242:57] me, I'll just like paste my call
[242:59] transcript directly in. Takes
[243:00] approximately the same amount of time.
[243:02] It's just this one is like exact and
[243:03] there's no room for error. Another
[243:05] really common request that I typically
[243:06] will do is I will like go to a website
[243:09] and I'll just like command all copy
[243:11] everything and then paste it in the
[243:12] model and be like, hey, you know, build
[243:13] me a proposal with this website or
[243:15] something. Obviously, I could have it,
[243:16] hey, HTTP request this link and then it
[243:18] goes through that. But, I mean, it's the
[243:19] same thing, right? It takes me the same
[243:20] amount of time to do that versus this.
[243:22] So, from the model's perspective,
[243:23] doesn't matter. Everything gets inserted
[243:24] in context the same way. Can be a big
[243:26] time saver since HTTP calls and then API
[243:28] requests and then accessing databases
[243:30] and stuff like that can take some time
[243:31] to set up. So, if you're using this as a
[243:34] user, right, you are executing your
[243:36] workflows using this orchestrator, you
[243:38] can absolutely just like co-create with
[243:40] it. You can go on websites yourself,
[243:41] copy paste stuff in, it's no big deal.
[243:43] The next thing I wanted to do is talk a
[243:45] little bit about how to peruse API
[243:47] documentation with Agentic workflows.
[243:49] So, as you guys remember in a previous
[243:51] demo, I built a workflow that took
[243:53] LinkedIn Sales Navigator URLs, fed them
[243:56] into the service vein, uh, you know, did
[243:58] a couple of other things, and then ended
[243:59] up giving me a big list of leads in a
[244:01] Google sheet. So, how exactly do we do
[244:03] this sort of thing in like a reasonable
[244:04] way? Well, obviously we could just, you
[244:06] know, tell the model, hey, I want you to
[244:08] build XYZ with Fain. But what you'll
[244:10] quickly realize is models will spend
[244:11] maybe 50% of their time just looking up
[244:13] API documentation and another 50% of the
[244:16] time like running into some sort of
[244:17] error. Like for instance, if I were to
[244:19] use this API documentation so let me
[244:21] just go over here then feed this into AI
[244:24] and say something like tell me about
[244:25] this API documentation.
[244:28] The first thing it'll do is it'll take
[244:30] the link and then it'll try accessing it
[244:31] using some sort of web search tool.
[244:33] That's what it'll do here. The thing is,
[244:35] not all API docs are created equal, and
[244:37] so some API documentation pages don't
[244:40] actually include um all of the
[244:42] information that we need in order to do
[244:43] what we need to do. Some of them don't
[244:45] return things the way that we need them
[244:47] to. So here it's saying the page is
[244:49] fairly lightweight on specifics. No
[244:50] detailed endpoint schemas, rate limits,
[244:52] or code examples. You need to log into
[244:53] their dashboard to add the full open API
[244:56] spec with the request and response
[244:57] schemas. But that's kind of weird
[244:59] because we have all the information
[245:00] right here, right? Well, that's the
[245:02] thing. Some of these API pages only load
[245:04] through JavaScript. So realistically,
[245:06] this isn't actually capable of accessing
[245:07] the API docs. If I said, hey, you know,
[245:10] could you find the endpoints or
[245:11] something? It could eventually do so,
[245:12] but it probably wouldn't do so very
[245:13] well.
[245:15] So I say, what are the API endpoints
[245:17] here? It's going to look for more
[245:19] information. So it's going to look for
[245:20] some spec to get more detailed
[245:21] information about the page. It's going
[245:23] to run through the same thing that it
[245:24] just did a moment ago, probably to no
[245:27] success. And here you see it uses
[245:29] JavaScript to render the UI, which means
[245:31] the endpoints aren't actual HTML. So now
[245:33] it's just starting to look and sort of
[245:35] guess at what the um JSON information is
[245:38] for the API. Sort of annoying, right?
[245:41] Doesn't actually provide that
[245:42] information. So what else is it going to
[245:43] do? Well, it's going to do more. It's
[245:44] going to start looking for other
[245:46] people's um API docs. It'll start
[245:47] looking for blog posts and stuff like
[245:49] that. And I mean like this information
[245:51] here, it's not terrible or anything, but
[245:52] if we're clear about how long this takes
[245:55] and then um what sort of resources it's
[245:57] requiring on our end, if I just type
[245:59] back slashcontext over here, you can see
[246:01] now that we've already started filling
[246:03] up our message um context, right? I
[246:06] mean, you know, MCP is still the
[246:07] prevailing one because this is using the
[246:09] same um series that we were using
[246:10] before. But yeah, I mean, like messages
[246:12] are already 1.4%. We haven't even done
[246:13] anything yet. Imagine if this continued
[246:15] operating on its own sort of like loop
[246:17] for another 30 seconds or so. Hell, we
[246:19] probably get up to like 3% 4% 5% or
[246:21] more. And so in order to prevent all of
[246:23] that from occurring, um, a lot of the
[246:25] time for APIs, I will actually just open
[246:27] the things that I want. So we wanted
[246:30] open, we wanted get, and then
[246:32] [gasps and sighs] what else did I do?
[246:33] There was like a URL check right over
[246:34] here. And I'll just copy all of it in
[246:36] directly.
[246:38] These are vehins API docs list endpoints
[246:42] for me. So now instead of having the
[246:45] model do all of that searching itself,
[246:47] which if you think about it is like
[246:48] that's an additional step which
[246:49] compounds error probabilities, I just
[246:51] copy and pasted everything in which
[246:53] means it's going to get everything right
[246:54] on the first try. It's not going to go
[246:56] back and forth or try and guess at
[246:57] various API endpoints or whatever. I
[246:59] basically have everything that I need.
[247:01] If I wanted to make a simple API call to
[247:04] the post endpoint, what would that look
[247:05] like in Python? Now it's actually going
[247:08] through and then giving me all the
[247:09] information that I need. That's pretty
[247:11] straightforward. Okay, great. Let's do
[247:12] it. Now, I should contrast that with a
[247:15] few other APIs out there that are
[247:17] actually optimized directly for AI and
[247:19] large language models and agentic
[247:20] workflows. So, one in particular is the
[247:23] Ampify API and these guys I want to say
[247:25] are like a leader, but um there are
[247:27] other services that are catching up and
[247:28] they're doing stuff like this as well.
[247:30] Like obviously I could feed all of this
[247:31] in to AI via plain text and you know it
[247:33] would do a good job, don't get me wrong,
[247:35] but what you'll see is that now there
[247:37] actually are copy for LLM buttons up at
[247:40] the top of the page. If I were to copy
[247:42] this for LLM, view it as markdown, open
[247:43] in chat, GBT, open in cloud, open in
[247:45] perplexity, it actually like includes
[247:47] information for
[247:50] AI models and I mean like this is just a
[247:52] markdown version of everything we saw on
[247:53] the page. Because it's marked down, it's
[247:55] actually already significantly more
[247:56] efficient and AI natively understands
[247:59] how to traverse this. So this is a brief
[248:01] example of like APIs accommodating to AI
[248:06] models and agentic workflows. APIs are
[248:09] sort of like anticipating that agentic
[248:10] workflows are going to quickly come and
[248:12] swallow up everything. So they're making
[248:14] all of their documentation totally
[248:16] available through like very token
[248:18] performant, token efficient markdown
[248:19] like this. So you know if I wanted to
[248:22] have it check the um documentation, I
[248:23] would actually just copy this
[248:27] and then I would just say
[248:30] tell me about this API. It would
[248:32] actually go when it would um first
[248:34] access the page itself to grab all the
[248:36] markdown data. And what's cool is
[248:37] despite the fact that it's a fair amount
[248:39] of text, this does so very quickly. Once
[248:41] it's done, it gives me a big overview.
[248:44] Then I can also ask follow-up questions.
[248:46] What kind of endpoints
[248:48] are most common?
[248:51] Okay. And as you can see, it's already
[248:52] providing me a bunch of information. So
[248:54] that's pretty sweet, right? You would
[248:56] not believe how much money on the
[248:57] internet is available for the taking if
[248:59] you just know how to connect APIs. And
[249:01] nowadays, to be honest, you don't even
[249:02] really have to know how to connect APIs.
[249:04] You just need to be able to communicate
[249:05] the fact that you want to connect to an
[249:07] API to a model. So if you could just
[249:08] say, "Hey, here's an API. Could you like
[249:10] really quickly connect to it and then
[249:11] send a quick test query like XYZ and
[249:14] then it does?" So, you know, you can
[249:15] actually swoop up a large chunk of like
[249:17] the economically valuable work on
[249:19] freelancing platforms, simple one-off
[249:21] queries that, you know, like businesses
[249:23] commonly require. Hey, I'm using
[249:25] Xplatform, but Xplatform doesn't have a
[249:27] a one-click Zapier integration. How do
[249:29] we connect to their API? It's so scary
[249:31] and intimidating. I mean like you can
[249:33] actually solve that really easily not
[249:34] just for yourself but for other people
[249:35] with a tool like this. In terms of how
[249:38] to actually do the stuff once a workflow
[249:40] starts for the first few times maybe
[249:42] first 10 or 15 times I actually
[249:43] recommend watching it work end to end.
[249:45] It seems like this is a big time
[249:46] investment keeping in mind that
[249:48] workflows can take you know 30 seconds
[249:49] to a minute to execute. Um, I don't
[249:51] think this is anywhere near that big of
[249:53] a deal because if you just watch the
[249:55] reasoning for a little bit for even like
[249:56] one or two executions, you typically
[249:58] learn more about what's the model is
[249:59] currently and actually doing under the
[250:00] hood than you would if you had like 3
[250:03] days of autonomous flows. Uh, and so in
[250:05] doing so, you're very very quickly able
[250:06] to iterate and make it very very good.
[250:08] You don't have to like stretch that
[250:09] iteration process out for like weeks or
[250:11] months. What's cool too is when you
[250:13] watch workflows, you get to develop a
[250:14] sense of intuition about the reasoning
[250:16] the model goes through. And I honestly
[250:17] think there's probably nothing more
[250:19] important, no better skill to develop
[250:20] than intuition surrounding how models
[250:22] think as of the current date. I mean,
[250:24] these models are going to run our
[250:25] economy very soon and they're already
[250:27] running our economy in many ways. So
[250:28] like if I am going to spend some time
[250:30] working, my whole time working should be
[250:32] spent developing an intuition for how
[250:34] these models actually function. I mean,
[250:35] it's also really satisfying. It's super
[250:37] cool just to see the model solve
[250:38] problems and, you know, make logical
[250:40] conclusions based off information that I
[250:42] provided it. And it's usually pretty
[250:43] easy to pinpoint when the reasoning goes
[250:45] sideways. the model will be like wait
[250:47] maybe I should use this approach and
[250:48] then you're looking at it you're like
[250:49] well that's not the approach to use
[250:50] which means you can actually
[250:51] significantly cut the amount of time it
[250:53] would take by just like pressing X and
[250:55] then pausing the run and then just
[250:56] saying hey sorry it's actually Y right
[250:58] way easier to do it that way and then
[251:00] co-creating with that model also again
[251:01] lets you build that good intuition for
[251:03] how your workflow is supposed to work
[251:04] now if I'm handling a really long
[251:06] workflow like I have a video editing
[251:07] workflow whose full execution due to you
[251:09] know the ffmpeg library can take like 45
[251:12] minutes or something I'm not going to
[251:14] just sit there and watch it obvious
[251:15] obviously because most of it is the
[251:16] script executing and then my hardware
[251:18] running and stuff, right? So, I'll just
[251:19] open an extra agent window and then I'll
[251:21] use what are called background tasks.
[251:22] Background tasks depend on the different
[251:24] model provider and interface that you're
[251:26] using. Claude introduced background
[251:27] tasks a while back and I've been using
[251:28] the Claude family of models um quite a
[251:30] bit recently. So, that's easy. What I'll
[251:32] then do is I'll set up some sort of hook
[251:34] in my IDE to play some sort of sound
[251:36] when the thing is done. Hooks connect to
[251:38] specific points in the workflow. Uh what
[251:40] that means is like if you know my
[251:42] workflow takes 30 minutes and it's a
[251:43] background task when it's done I can
[251:44] actually have my computer go duh ding
[251:46] and then you know tell me when the thing
[251:47] is completed. I'll show you guys an
[251:49] example of that later. Um there's also
[251:50] native system notifications. Obviously I
[251:52] just find the sounds more reliable for
[251:54] getting my attention. I get a lot of
[251:55] notes nowadays. To set up hooks
[251:57] depending on the platform you just
[251:58] create a mini workflow that triggers the
[252:00] sounds or the animation. So you can just
[252:01] like give it a cool sound that you want
[252:03] and then say, "Hey, set up this up so
[252:05] that when you finish operating um
[252:07] there's some hook and then it it
[252:08] triggers this sound and it just plays
[252:09] natively on my computer because that'll
[252:11] help me direct my attention back to you
[252:13] and then like help you with the next
[252:14] step." Claude has really good
[252:15] documentation on hooks. Most people that
[252:17] have built hooks have done so with
[252:18] Claude. You can check their hook docs
[252:20] for specifics. Um the common use case,
[252:22] as I mentioned, is to play sound when
[252:23] the workflow finishes just so you can
[252:25] check the output, verify things which
[252:26] you wanted. But you can also do things
[252:27] like play different sounds for human in
[252:29] the loop steps where it's like, hey,
[252:30] action required type stuff. Okay, brief
[252:32] example of me setting up a hook. Here's
[252:34] a practical guide on setting up hooks.
[252:36] So, first of all, what I'm going to do
[252:37] is I'll say, hey, how's it going? I'd
[252:39] like you to set me up a hook that plays
[252:41] a nice chime sound every time that one
[252:45] of my agents is done with a task. That
[252:48] way, I'll know to go back to the task
[252:50] because I normally have you alt tabbed
[252:51] while I'm doing other things.
[252:55] This already knows that it's a clawed
[252:57] code hook feature. There are shell
[252:58] commands that execute in response to
[252:59] events like tool calls. So now it's
[253:01] giving me all this information. First,
[253:03] it's going to do some research. Then
[253:06] it's going to actually write a script to
[253:07] run the claude code hook. All right. And
[253:10] it's now adding the hooks configuration
[253:12] with a little glass sound. I don't know
[253:13] if you guys heard that, but that's that.
[253:15] It just finished. So yeah, I did just
[253:17] finish. I'm going to pretend I'm alt
[253:18] tabbed somewhere, not paying attention,
[253:20] but I'm not hearing the chime.
[253:26] So, it looks like every time it plays it
[253:28] directly, I could hear it.
[253:33] Okay. So, I'm going to back slash check
[253:36] hooks.
[253:38] I'm just going to start a new Cloud Code
[253:40] instance like it's telling me to do.
[253:42] Hey, how's it going?
[253:47] Perfect. And now I hear the chime. So,
[253:49] it's that easy. You can now set let's
[253:51] say five of these simultaneously.
[253:54] One,
[253:57] two, three, four. Then I'll just open
[254:01] all these in separate tabs. Then I'm
[254:04] just going to send to all of them. Write
[254:07] me a funny poem.
[254:11] Now I will send to all. One, two, three,
[254:16] four, five.
[254:29] Nice. Now, this thing has gone through
[254:31] and written me funny poems, and I got a
[254:33] bunch of chimes, too. Hopefully, you
[254:35] guys could see how this thing could be
[254:37] helpful if you guys were working on a
[254:38] cloud code instance without
[254:40] notifications enabled or something like
[254:41] that, uh, and then you were on another
[254:43] tab. In practice, I find when you are
[254:45] juggling a bunch of things and trying to
[254:47] stay in context, but obviously also
[254:49] monitoring or orchestrating some sort of
[254:51] AI flow, um, a big chunk of the time you
[254:53] will spend is literally just completely
[254:55] wasted time where you haven't given AI
[254:56] the next instruction. So to really
[254:58] economize that time, simplest way to do
[255:00] it is just to like have some sort of
[255:01] notifying flow. Play a nice chime noise
[255:04] or I don't know, you could set it up so
[255:06] the claud window actually pops up every
[255:07] time it's done. That way, you'll very
[255:09] quickly go back to this, give it some
[255:11] additional instructions, and then be
[255:12] able to double up on the return on your
[255:14] time. Now, when any workflow completes,
[255:16] you're almost always going to get a
[255:17] deliverable. This is a link or a
[255:20] document or a summary or something.
[255:22] You'll also usually get some sort of
[255:24] report of what happened during the
[255:26] execution. My recommendation for you is
[255:29] to review the output, confirm that it
[255:31] meets your needs, and if it does, tell
[255:33] the model. Let them know. Say, "This
[255:36] worked great." If you've had to do some
[255:39] trials and some some iterations in order
[255:41] to get this, let the model know that
[255:43] like this is what you want and to update
[255:45] the directive in execution unless it's
[255:47] already done. So most of the time this
[255:49] will happen automatically, but it's
[255:51] cheap and almost free to say that every
[255:53] time you get like a really really good
[255:54] output. As I mentioned previously,
[255:56] individual workflows are really useful,
[255:58] but I actually think chaining them
[256:00] together is where the real magic
[256:01] happens. I always provide that umbrella
[256:04] analogy and I like how my umbrellas are
[256:06] getting better and more and more um
[256:08] sophisticated as this course goes on. I
[256:10] don't think I used to see that little
[256:11] thing up there. That's really badass. Um
[256:13] this is like your, you know, marketing
[256:16] umbrella, you know, your new new client
[256:18] onboarding umbrella or whatever. What
[256:20] you do is you get all the individual
[256:21] workflows that you've created, group
[256:23] them under this thing, and then next
[256:25] time you can just run all of them
[256:27] simultaneously by just saying, "Hey,
[256:29] trigger the new onboarded client
[256:31] automation." This solves the manual
[256:33] handoff process with the deliverable.
[256:35] Like you could build a lead scraper. You
[256:37] could build an enrichment workflow, but
[256:39] what that means is this workflow will
[256:41] start and then it'll finish and say,
[256:43] "Hey, we're done." And then you actually
[256:44] have to take that link and say, "Okay,
[256:46] now do the enrichment workflow. Oh,
[256:47] okay, now we're done." You have to take
[256:48] that and be like, "Okay, let's actually
[256:50] send the emails. Okay, now we're done."
[256:51] Like much better for me just to
[256:53] eliminate that process completely and
[256:55] then, you know, only check in once we've
[256:57] actually completed the entire thing,
[256:58] right? Assuming that I've verified that
[257:00] every individual step does what it is
[257:03] that I want it to do because otherwise,
[257:05] yeah, you're basically the bottleneck.
[257:07] And I can't tell you how many times I've
[257:09] just had 10 claw instances open or 10
[257:12] Gemini instances open and I just forget
[257:14] to proceed with one of the steps. It's
[257:16] like, "Would you like me to send the
[257:18] email?" And then I'm like, "Where the
[257:19] heck's this damn email?" And then I look
[257:21] back and I realize, "Oh, I didn't
[257:22] actually tell it to continue. I wasted
[257:23] like an hour." So, I've covered similar
[257:25] examples, but here's another one. Uh,
[257:27] lead scraping is really popular. So, you
[257:29] find potential customers, then you
[257:30] enrich their emails, then you
[257:32] personalize their first line generation.
[257:34] I do this using a casualization workflow
[257:36] I've shown you guys multiple times, but
[257:38] essentially this is all just batched
[257:39] under um you know like end toend
[257:44] new client workflow. So that when I get
[257:48] a new client, it actually goes through,
[257:50] analyzes the client niche, scrapes
[257:52] leads, enriches the emails, and then
[257:54] does personalized first lines before
[257:55] giving me a Google sheet. It's kind of
[257:57] cool because this is all stuff that I
[257:58] was doing manually step by step. As you
[258:00] get to higher levels of abstraction,
[258:01] eventually we'll have things that are
[258:03] basically like do all of the marketing
[258:05] for this campaign and it'll do a really
[258:06] good job. When does the agent actually
[258:08] require our help? Well, sometimes the
[258:11] agent genuinely cannot fix something
[258:12] automatically. And it's rare, but when
[258:15] this happens, it'll typically just ask
[258:16] you directly. Usually, it'll provide a
[258:18] fair amount of context, which is good.
[258:20] Now, the question is what it was trying
[258:22] to do, what went wrong, and then what
[258:24] options exist to fix it. Your job is
[258:26] literally just to look at that and say,
[258:28] "Okay, let's do this then or okay,
[258:31] update the directive to do this or are
[258:33] you sure you fully tried?" Or, "Have you
[258:35] research all of the solutions?" or
[258:36] something along those lines. And so, in
[258:38] this way, you're not only like uh, you
[258:41] know, like a decision maker at a high
[258:42] level. A lot of the time, you're also
[258:43] just a motivator. To be honest, I can't
[258:45] tell you how many times I've had one of
[258:46] these agents go on some loop for 10
[258:48] minutes and try and build something and,
[258:50] you know, they get really close, but
[258:52] then they just can't seem to get the API
[258:54] spec. And then I say, "Could you
[258:55] research the API spec?" And they go,
[258:57] "All right, yeah, I'll go research the
[258:59] API." And then they actually go do the
[259:01] thing and they get it right on the first
[259:02] try. It sounds weird, but a lot of the
[259:04] time agents don't just need the
[259:06] decisions made, they also need some
[259:08] level of motivation. I've also found
[259:11] that sometimes a gets stuck in a really
[259:13] silly loop. Sometimes it'll literally
[259:16] just like do the same thing over and
[259:17] over and over again and then it'll try
[259:19] the same next solution over and over and
[259:20] over again and then it'll just chain
[259:21] those two together and go back and forth
[259:23] and back and forth and back and forth.
[259:25] Who knows why this happens? I'm sure the
[259:26] smarter the models get, the less this
[259:28] will occur. But when this happens, you
[259:30] you just pause it. You look at the
[259:31] reasoning. You see what's going on. You
[259:32] say, "Hey, you've just been doing these
[259:34] two things for the last like 20 minutes.
[259:35] Could you please not do that anymore?
[259:36] Instead, do research on this best
[259:38] solution before proceeding." The reason
[259:40] why you do this is because iteration is
[259:41] actually just really cheap. So it's much
[259:43] better to do something than nothing.
[259:45] Like I mean the cost of you sending this
[259:47] one message or whatever is like cents on
[259:49] the dollar, right? And then the
[259:50] potential upside is is very very big.
[259:53] And typically when you have like a
[259:54] massive disparity between the cost and
[259:57] then the upside, it would take many many
[259:59] many runs of this thing completely
[260:02] failing without returning some sort of
[260:05] like ROI. And in my case, you know, I'm
[260:07] usually capable of doing on the first or
[260:08] the second try. So when should you jump
[260:11] in? When should you do let it run aka
[260:12] when is there human in the loop? The way
[260:14] that I determine when I should build a
[260:17] human in the loop flow or rather I
[260:19] should use human in the loop in a in a
[260:20] flow is what is the magnitude of the
[260:23] outcome and then what is the sensitivity
[260:25] to quality. So if the magnitude of the
[260:27] outcome is really big aka this single
[260:30] task matters a ton for my business then
[260:32] I'm going to step in. If it's very
[260:35] sensitive to quality, as in if there are
[260:36] very small errors that create
[260:38] disproportionately large problems, I
[260:40] also step in. And if they're high on
[260:41] both, you absolutely want a human in the
[260:44] loop. A really simple example of this is
[260:46] cold email templates and then outreach
[260:48] sequences. So I do a lot of these,
[260:50] right? It's part of my day-to-day as
[260:51] part of leftclick. I find that when you
[260:53] have an AI do 100% of this, performance
[260:55] is pretty trash. And the reason why is
[260:58] because I could actually graph this.
[260:59] There's basically like a really
[261:02] uncanny valley essentially where let me
[261:07] see
[261:09] if this is the let's just say quality
[261:14] and then this is the perception.
[261:18] If this is zero and then this is one.
[261:21] Notice how it doesn't really matter how
[261:23] much quality we put in
[261:26] until we reach some like phase change
[261:28] level and then all of a sudden it goes
[261:30] boom and then it becomes really really
[261:32] really good. So for my cold email if I
[261:35] have AI right AI it's gotten better over
[261:37] the years. Maybe it started over here
[261:38] and now it's over here and now it's over
[261:40] here and now it's over here here here.
[261:43] It doesn't really matter how good AI is
[261:46] at this process because the sensitivity
[261:50] of the perception of my email campaigns
[261:53] is very very high. And so there's this
[261:56] uncanny valley effect over here where
[261:58] like a tiny little improvement in
[261:59] quality massively improves the
[262:01] perception. And so in situations like
[262:03] this where the model just can't seem to
[262:04] get up this thing, obviously it makes
[262:06] sense for me to like review it really
[262:08] quickly, change up two or three words,
[262:09] and then boom, all a sudden the quality
[262:10] is up here, right? It's like, did I
[262:12] objectively change the quality a ton?
[262:14] No. But did the perception massively
[262:16] change? Yeah. And that might have taken
[262:17] me a few moments of work. So, I find
[262:19] stuff like that is really, really
[262:20] important on um, you know, cold email
[262:22] templates, outreach. I would always, you
[262:24] know, given the volume of the task, the
[262:26] fact that I'm sending this stuff out to
[262:27] tens of thousands of people, I would
[262:29] almost always at least have a person
[262:30] looking it over before it runs because
[262:32] it's like, well, what if I'm just like
[262:33] off by one degree here? I just wasted
[262:35] 10,000 emails. I might have as well like
[262:37] spent 2 seconds to fix that up and then
[262:39] sent to 10,000 and then gotten much
[262:41] better results, right? [gasps] Same
[262:43] thing with financial documents like
[262:44] invoices and even proposals. I mean, I
[262:46] automate the hell out of my proposals,
[262:47] don't get me wrong, but I have a human
[262:48] in the loop stop. I will take a look at
[262:50] the proposal before I send it out cuz
[262:52] imagine what if you accidentally added
[262:53] an extra zero or something. It's very,
[262:55] very unlikely, right? But even if that
[262:57] occurs like 01% of the time, you screw
[263:00] up on some number because your AI system
[263:02] just misinterpreted what you said or
[263:03] maybe your voice transcription tool was
[263:04] wrong or whatever. The point I'm making
[263:06] is like the time savings that you get by
[263:08] not looking it over are not at all
[263:10] equivalent with the negative impact to
[263:12] you, your reputation, and your business
[263:14] if you do not look it over. So anywhere
[263:17] where there's a few percentage points of
[263:18] quality making a massive difference to
[263:21] the impact, generally anytime the impact
[263:24] over here and then the quality over here
[263:28] has this sort of relationship. Pardon
[263:29] me, I didn't draw that cuz I think my
[263:31] tablet's malfunctioning. Um, you
[263:33] generally always want a human in the
[263:34] loop. On the other hand, there are a lot
[263:36] of tasks out there that are really low
[263:37] sensitivity. And when this happens, it's
[263:39] like the volume of this thing is a lot
[263:42] more important than being perfect. So,
[263:43] you might as well just let it run
[263:44] completely autonomously. Good example of
[263:46] that is web scraping. Like, this is not
[263:48] a really high sensitivity task. Models
[263:50] are pretty great at this. Creating
[263:52] multiple drafts or variations for later
[263:54] selection is a design pattern that I use
[263:55] all the time. And it's like I don't
[263:57] actually need to steer it that much cuz
[263:58] the whole idea is I just want it to like
[263:59] generate me a bunch, right? So, that's
[264:01] really simple. Generally anything that
[264:03] sales linearly with quality, right?
[264:06] Where it's like the amount of quality
[264:08] here and then the amount of impact sort
[264:11] of at like a onetoone relationship, I'm
[264:13] okay with it going autonomously because
[264:15] even if I'm up here, okay, and it's over
[264:17] here, the amount of time that I save
[264:20] having it automated, you know, at like
[264:22] 70% of the full thing versus 100% of the
[264:24] full thing is typically way better than
[264:26] whatever the the actual impact
[264:28] improvement is. Now, some things should
[264:30] not be automated at all. I don't
[264:32] actually think that you should have
[264:33] voice agents doing any sales calls for
[264:35] you. And this is something I see so many
[264:37] people do. Like if you're offering a
[264:39] call, you clearly care a lot about the
[264:41] outcome of the call, right? It is a
[264:44] hightouch sales conversation. And you
[264:47] know, if there's even a.1% chance that
[264:50] somebody thinks that there's not a real
[264:51] human being talking to them, it's like a
[264:52] robot. That's going to have a much
[264:54] bigger impact on the quality of that
[264:56] deal than 0.1%. Right? So it's not a
[264:58] linear relationship between that at all.
[265:00] And you know, some things I just don't
[265:01] automate. Like would I automate the
[265:03] calling of my client or something? No, I
[265:05] I wouldn't. At least not right now at
[265:06] current levels of tech. Maybe if um
[265:08] agentbased calling becomes better and
[265:10] like more socially acceptable later. But
[265:12] for now, no. What I would do is I would
[265:14] like automate the process of coming up
[265:16] with a bunch of information and context
[265:18] about the client. I would automate the
[265:20] process of doing research on the client.
[265:22] These are all things that scale pretty
[265:23] linearly as I was talking about, right?
[265:24] So, I'd have some big dossier of
[265:26] information in front of me to save me
[265:28] from having to manually go through hours
[265:30] and hours of LinkedIn research, but um I
[265:32] would actually just make sure that the
[265:33] actual calling part is me, right? It
[265:34] just doesn't make sense. It's too
[265:35] sensitive of a process. Research, on the
[265:38] other hand, a lot more linear. There's
[265:40] some situations that do require empathy,
[265:42] judgment, but you can convert situations
[265:44] that require empathy and judgment into
[265:46] situations that you just like
[265:47] automatically say yes or no to. A good
[265:49] example of this is um Amazon. Amazon has
[265:51] like basically automatic refund
[265:53] dispersement. If uh you have asked for I
[265:56] think less than like a 2% refund rate or
[265:58] something like that. So if there's an
[265:59] issue with your order and like for the
[266:01] most part you don't ask for refunds very
[266:02] often and you say, "Hey, there's some
[266:03] issue with this. Could you give me a
[266:04] refund?" Like they will automatically be
[266:06] like, "Yes, refund granted." And then
[266:08] you're like, "What the hell? I didn't
[266:09] even tell anybody about like I didn't
[266:10] even give a photo or anything. It's
[266:12] fully automatic." It's like, "Yeah, see
[266:14] how much time and energy they save by
[266:15] doing that." So you can just reconstruct
[266:18] um sensitive customer situations and
[266:20] like quantify them and then you can like
[266:21] totally automate them. But in situations
[266:23] where like you genuinely can't. Let's
[266:24] say this is somebody with sort of a
[266:26] shakier refund rate and stuff like yeah,
[266:28] you're going to need to find a way to
[266:28] pass that off to somebody that has
[266:30] empathy and judgement. So yeah, I mean I
[266:33] would not automate things just for the
[266:34] sake of automating them. I'd only ever
[266:36] automate something if like it actually
[266:37] made a bottom line difference to my
[266:38] business. And things like lead scraping
[266:40] for instance, research, accumulation of
[266:42] large data sets and stuff like Like all
[266:43] this stuff in videos make a large
[266:44] difference to my bottom line. So I'm
[266:46] happy to automate it. But the calls and
[266:47] whatnot, it's all just me, baby. At the
[266:49] end of the day, your goal is supervised
[266:51] autonomy. It is not babysitting. So I
[266:54] just talk to them like Slack messages. I
[266:56] do not use formal syntax or precise
[266:58] technical language. I just DM my
[267:00] colleagues and then just replace the
[267:02] colleagues with my agent. You know, uh I
[267:04] was running a YouTube workflow just the
[267:06] other day to edit one of my videos and I
[267:07] said, "Hey, could you run the YouTube
[267:08] editor for the new file? Make the cuts a
[267:10] little bit tighter." and it took the
[267:11] average cut distance and then it just
[267:13] like decreased it a little bit and then
[267:14] it just reran the YouTube editor and
[267:16] then I said I liked it so then it
[267:17] updated the flow so I would just use
[267:18] that the next time. Same thing with
[267:20] voice transcription in general. Just
[267:22] just speak naturally and then send it.
[267:23] It'll understand you. Okay. So manually
[267:25] triggering these workflows is actually
[267:27] just the beginning and that may be
[267:28] frustrating for you because there many
[267:29] hours through the course but that goes a
[267:31] lot deeper than this. Right now what
[267:33] we're doing is we're opening our IDE.
[267:35] We're talking to our agents and then
[267:36] we're starting the flows yourself, which
[267:38] is fine if you have like ad hoc tasks,
[267:39] one-off requests. It's fine when you
[267:41] work 8 hours a day and between, you
[267:42] know, 9 to5 or whatever when you're at
[267:44] your desk, you can you can get things
[267:45] done. But as I'm sure you'd imagine, the
[267:48] automatic part in the word automation,
[267:50] like the auto is pretty important,
[267:52] right? So, how do you actually have
[267:53] these things run automatically without
[267:54] your involvement? Well, these are called
[267:56] event- driven workflows. For instance,
[267:58] let's say a new lead fills out your
[267:59] website form. You want a workflow that
[268:01] automatically replies and books a
[268:02] meeting, right? But what if the new lead
[268:03] comes in at 5:30 and and you leave for
[268:05] home at 5? What if a customer sends a
[268:07] support email? Your agent does the
[268:09] triage, write the draft, and writes to
[268:10] the right person for sending. I mean,
[268:12] that's great and all, but like what are
[268:13] you going to do? Like wait until the
[268:14] next day, um, look at your inbox and
[268:16] then do the triage, then that defeats
[268:18] the purpose. So, how do we actually
[268:19] build these things? There's also
[268:21] schedule driven workflows. Maybe it's
[268:22] 9:00 a.m. on Monday and you want a
[268:24] weekly report to generate itself. So, do
[268:25] you really want to come in every Monday
[268:27] and then be like, "Hey, generate my
[268:29] weekly report." I mean, of course, you
[268:30] can, but it's nice if some of these
[268:31] things are done automatically for you.
[268:32] Maybe the weekly report is summarizes
[268:34] your work and then sends it to your boss
[268:36] or something or your client with your
[268:38] timetable, right? Same thing for these
[268:40] other things. These are uh specific
[268:42] schedules. Well, that's what we're going
[268:43] to learn about next. Web hooks and
[268:45] scheduling. Now that you know everything
[268:46] that you need to know about agentic
[268:48] workflows in order to build them and
[268:51] then use them, it's time to take these
[268:54] things which up until now have been
[268:55] constrained to your own device or your
[268:57] integrated development environments,
[268:59] then put them in the cloud where they
[269:00] can be triggered through means other
[269:02] than you actually prompting. So in order
[269:05] to do this successfully, which I'm going
[269:07] to call cloudifying my workflows, we
[269:11] don't actually upload the orchestrator
[269:13] itself. Remember in the loop where we
[269:16] have the directives, the orchestration
[269:17] layer and then the executions. What we
[269:19] don't upload is the orchestrator. All we
[269:22] really do is upload the execution
[269:24] scripts themselves which are the
[269:26] deterministic parts. You can also upload
[269:28] the directives too if you wanted to
[269:30] provide context to a a model later on in
[269:33] case it wanted to edit or or whatever.
[269:35] So for the most part just upload the
[269:38] execution scripts. I'm going to show you
[269:39] guys how to do that and some
[269:41] alternatives. The way that you can think
[269:43] of it is as creating many APIs that do
[269:46] one specific thing reliably. And the
[269:48] same concepts apply whether you're using
[269:49] DO or other frameworks like cloud skills
[269:52] or whatever. Now you may be wondering
[269:54] Nick what is fundamentally different
[269:55] about this versus what we were doing
[269:57] before. Well, what's fundamentally
[269:58] different about this versus what we're
[270:00] doing before is there is no LLM.
[270:01] Instead, all we're really doing is we're
[270:03] just creating our own API and we're
[270:05] using LLMs to do it really really
[270:06] quickly and easily with some sort of
[270:08] defined input and output. The reason why
[270:10] is because you need to remember
[270:11] stochasticity or sort of randomness. The
[270:14] tendency for models to eventually
[270:15] diverge from what it is that you wanted
[270:17] them to do over time given enough time
[270:19] steps. So because of this, LMS are very
[270:21] probabilistic and they sort of have
[270:22] randomness in every direction. When
[270:24] they're working in your IDE, for the
[270:26] most part, you're around, right? Whether
[270:27] you're not looking at it right this
[270:28] second, you'll probably look at it at
[270:30] some point over the course of the next
[270:31] hour. And because of that, if it has an
[270:33] issue, you're watching. You can course
[270:34] correct. But if it's 3:00 a.m., okay,
[270:36] and this is running unattended with full
[270:38] system permissions, this level of
[270:40] variability is a liability. And so we're
[270:42] taking the AI just out of the cloud loop
[270:45] entirely.
[270:47] Additionally, instead of having slightly
[270:48] different routing decisions like we see
[270:50] here, we're just going to force them
[270:52] into one routing decision every time
[270:54] using what's called server side logic.
[270:56] So because your execution scripts do the
[270:58] same thing every time, you never
[271:00] actually have to suffer this. Instead,
[271:01] it's always just, hey, we start by
[271:03] executing node one, then we move to
[271:05] executing node two, and then so on and
[271:07] so on and so forth to node n. And all
[271:11] we're doing is we're taking those
[271:12] execution scripts, deploying them as
[271:14] standalone cloud functions. No LLM in
[271:16] the loop, just an API on a schedule or
[271:18] responding to web hooks. The
[271:19] intelligence that we use during this
[271:21] process is just used to build the
[271:23] execution scripts, not to actually run
[271:24] them. In this way, you can consider this
[271:26] like basically deploying your own mini
[271:27] app. A good way to think about this is,
[271:29] you know, like your agent is the
[271:31] architect and your cloud workflow is the
[271:32] building. Architects design buildings
[271:34] all the time, but it's very rare that
[271:36] they actually live in the buildings they
[271:37] design, right? So, what our agent is
[271:38] doing in this point is just architecting
[271:40] our beautiful building and we're going
[271:42] to put execution scripts to live in
[271:44] there instead. This obviously loses a
[271:46] fair amount. I mean, this takes our
[271:47] agentic workflows and changes them back
[271:49] into traditional workflows or procedural
[271:51] workflows. It means that they can't
[271:53] adapt to unexpected situations on the
[271:55] fly. They also can't self-anneal or ask
[271:58] clarifying questions when things get
[271:59] weird. You know, you are going back to
[272:01] that old school traditional automation
[272:02] behavior and it just does exactly what
[272:04] you told it to do. Nothing more, nothing
[272:05] less. But if you think about it, by the
[272:08] time your workflows deploy, they should
[272:10] be pretty battle tested as I was
[272:12] mentioning earlier from having run
[272:14] dozens of times locally and you've
[272:15] probably already worked out all the
[272:17] kinks in your IDE locally where the
[272:18] debugging is easy. So if something
[272:20] breaks, you are still going to get error
[272:22] notifications. And the really cool thing
[272:23] is you can just fix it with your agent.
[272:24] If you're using a modern platform like
[272:26] modal, um models can read the errors
[272:28] from modal really easily. So you can
[272:29] actually just say, "Hey, this workflow I
[272:30] think is broken, fix it." And I can
[272:32] actually just do the debugging process
[272:33] for you. So you get all of like the
[272:35] ability to debug and stuff like that.
[272:37] It's just you're not doing it on like a
[272:39] live loop because if you were doing it
[272:40] on a live loop, results, assuming that
[272:42] it doesn't do what you wanted to do,
[272:44] could be catastrophic, go all over the
[272:45] place. And I mean like I could sit here
[272:47] and I could give you guys a way to do
[272:49] this that includes the orchestrator
[272:51] directly in the uh environment. I could
[272:54] have the agent actually like listening
[272:55] and constantly modifying things. But
[272:57] I've tried this now in a in a few actual
[272:59] businesses. And despite the fact that
[273:00] it's very shiny and it's very sexy and
[273:02] people like, "Wow, I can just query my
[273:03] LLM um you know on some cloud container
[273:06] somewhere and have it do whatever I want
[273:07] via web hook." Despite the fact that it
[273:09] seems really cool, we're just not there
[273:11] yet. I'm pretty sure we'll be there some
[273:13] point in the next couple of years, but
[273:14] for now we're just going to leave the
[273:15] orchestrator out of it completely and
[273:17] basically just use our agentic workflow
[273:19] building skills to build APIs really
[273:21] quickly that we can then call. So the
[273:23] platform that I use for all this is
[273:24] called modal. Modal is not the only
[273:27] platform out there. There are many
[273:29] others like trigger.dev etc. I'm not
[273:31] associated with any of these. Um but
[273:33] modal is just a good product.
[273:34] Trigger.dev is a good product. We've set
[273:36] up some workflows there and there are a
[273:37] couple of other builders too that like
[273:39] essentially do this function. But
[273:41] essentially the way that u modal works
[273:42] is it's really simple. You just take a
[273:44] Python script and then you turn it into
[273:46] a cloud function. It's also pay-per-use.
[273:48] So when your workflow isn't running,
[273:49] it'll spin down and it'll cost nothing.
[273:51] You'll get a web hook URL just like you
[273:52] would from make or nad. And it's also
[273:54] very cheap, especially for Python based
[273:56] execution scripts. They gave me $5 of
[273:58] credits the beginning of this month and
[273:59] I think so far I've used like 3 cents.
[274:01] So very very very affordable. The best
[274:03] part is you don't need to know anything
[274:04] about any of these platforms to be
[274:05] honest. They're built for agents and so
[274:08] agents know how to crawl them and
[274:09] traverse them and set things up really
[274:10] easily because their documentation is
[274:12] fantastic. All I really had to do in
[274:14] order to do this, which I'll show you in
[274:15] a moment, is say turn this into a cloud
[274:17] function. And then it did everything
[274:18] else. Now, the web hook URLs that modal
[274:20] gives you can be called from anywhere,
[274:21] including by other agents. And then it
[274:23] also allows people at regardless of
[274:25] whatever skill level you are to set up
[274:27] this sort of web hook or event- driven
[274:28] flow. It's sort of like nadn or make.com
[274:31] or you know gumloop or zapier any one of
[274:34] these platforms
[274:36] these will expose these little web hook
[274:38] urls right and you take these web hook
[274:41] urls and then you give them to services
[274:43] like I don't know um clickup or
[274:46] instantly or pandadoc or whatever the
[274:47] heck you want right well this is exactly
[274:49] what modal does it's just instead of
[274:51] giving it to you in sort of this visual
[274:52] way um we just do it through natural
[274:54] language we're like hey set this thing
[274:56] up and then give me a web hook URL so
[274:57] that I can call here's what the request
[274:59] body is going to look like. Cool. We
[275:00] done. Awesome. Thank you very much. That
[275:02] said, wanted to take a couple steps back
[275:03] here just in case people didn't know
[275:04] what web hooks are. If what I just said
[275:06] made no sense to you, that's okay. I'm
[275:07] going to cover it. First of all, a web
[275:08] hook is literally just a URL that
[275:10] triggers your workflow when something
[275:11] hits it. So, an external system like a
[275:13] CRM or website form or make or n can
[275:16] actually just call a URL like this
[275:17] automatically. It's just like a
[275:18] doorbell. When somebody presses it, your
[275:20] workflow will wake up and run. Um, you
[275:22] don't necessarily have to be there to do
[275:23] it. If you guys have ever done any home
[275:24] automation stuff, any sort of like, I
[275:26] don't know, switches or whatnot, it's
[275:28] the same it's the same idea. There's
[275:29] like some URL somewhere, some
[275:31] destination, it could even be your
[275:33] website, and when somebody visits it, it
[275:35] triggers something that does something
[275:36] else. Obviously, the something else in
[275:38] this case is going to be our automated
[275:39] workflow. If I had a URL like this,
[275:41] let's say it's my
[275:42] nick-thbot.webhook.com,
[275:45] I could do anything with this URL. Like
[275:46] I I could literally just like enter this
[275:47] into my browser and press enter, and it
[275:49] would trigger a flow. Or I could send an
[275:50] HTTP request which is um like a web
[275:53] request through make.com nada and any
[275:55] other noode builder. I could do it
[275:56] through my terminal. I could do it
[275:57] through an agent. But basically this is
[275:58] just a destination on the internet.
[276:00] Okay, that's like a node and when
[276:02] somebody accesses the node, this thing
[276:04] does some logic and depending on whether
[276:06] or not the node input fits its
[276:07] specifications, it'll continue and then
[276:09] call whatever the heck you want. So web
[276:10] hooks really are just like URL with some
[276:12] logic attached to them. That's more or
[276:13] less it and they're very very common in
[276:15] any sort of automated scenario. All
[276:17] right. So, what is the agent doing
[276:18] behind the scenes in order to set this
[276:20] up for you? Well, it'll review our
[276:21] agents.mmd and our claude MD and our
[276:23] gemini.mmd and so on and so forth. Just
[276:26] to understand the setup first, ideally
[276:27] somewhere in there, you would say, "Hey,
[276:29] you know, as part of your work, one of
[276:30] the things you do is you set up cloud
[276:32] web hooks or cloud scheduled workflows
[276:35] on modal. Here's how to do so." What it
[276:37] then does is it looks at your existing
[276:38] execution scripts for the workflow that
[276:40] you want to deploy. It'll wrap
[276:41] everything in a simple format that modal
[276:43] really likes proper decorators and
[276:45] whatnot and then if there are any
[276:47] prompts or API keys or whatever it'll
[276:49] actually like ask you for them although
[276:50] I find most of the time it's
[276:51] plug-and-play it's just like oh you know
[276:52] I have the keys let me convert them into
[276:54] modals format once deployed you get a
[276:56] simple URL this is the you know node
[276:58] that it calls um this is the phone
[277:00] number that other systems can give a
[277:01] ring in order to make something happen
[277:03] and then in whatever service you're
[277:05] using because this is obviously being
[277:06] triggered by some service by some
[277:08] notification from Slack or some some
[277:10] incoming web hook from instantly or
[277:12] whatever, you just give them the web
[277:14] hook URL. And a lot of the time there's
[277:15] like a field or something and it'll say,
[277:16] "Hey, what's the web hook URL you want
[277:18] us to send results to?" And then you
[277:19] just put it there. The request just
[277:21] needs to match the format that the agent
[277:23] expects. It's usually in what's called
[277:24] JSON or JavaScript object notation. You
[277:26] don't actually need to know JSON
[277:27] nowadays. Um, all you need to do is be
[277:28] able to recognize it. Typically starts
[277:30] with some curly braces and then when
[277:32] your agent sees this, um, you know, you
[277:33] can just copy and paste whatever you see
[277:35] in the web hook documentation. It'll go
[277:37] from a demo to actually doing stuff
[277:38] really, really quickly, which is
[277:39] fantastic. If you don't know how to
[277:40] connect stuff, you literally just ask,
[277:42] "Hey, how do I set up, you know, ClickUp
[277:43] to call this web hook when a new lead
[277:44] comes in agent or Claude or Gemini or
[277:47] whatever you're using, we'll actually
[277:48] walk you through all that step by step,
[277:50] especially if it's a platform specific
[277:51] UI thing. I find a lot of the time
[277:52] they'll just pick, oh, um, here's the
[277:53] link. Just go to this link and then
[277:55] you're done." You don't need to spend
[277:56] hours Googling stuff or chatbing stuff.
[277:58] This is exactly what the tools are good
[277:59] at. So, don't sweat it. And to take that
[278:01] one step further, if you wanted to,
[278:02] instead of making it web hook driven,
[278:04] have it schedule driven, you just use
[278:06] something called cron. Um, again, this
[278:08] is something that's very native that is
[278:09] supported by Modal and our agents out of
[278:11] the box. Instead, you just say, "Hey,
[278:13] can you run this thing at, you know,
[278:14] 5:00 p.m. every single day, and it'll do
[278:16] it. No complex configuration. You just
[278:18] describe when you want something to run.
[278:19] It'll handle all the syntax and
[278:20] deployment details." That's just kind of
[278:22] annoying for me because I spent a lot of
[278:23] time learning cron way back in the day
[278:25] when I wanted to schedule simple things.
[278:27] But, um, yeah, it's just like setting a
[278:28] recurring calendar reminder. You're just
[278:30] doing it for your workflows. So, God
[278:31] bless the fact that we are at this point
[278:32] where technology can do all that for us
[278:34] because good lord do I not want to have
[278:36] to learn another scheduling syntax
[278:37] again. Okay, so some example prompts.
[278:39] You just say, "I want my weekly workflow
[278:41] report to run automatically every Monday
[278:42] at 9:00 a.m. It'll actually set up the
[278:44] cron for you. Deploy it to modal and so
[278:45] on and so forth." You know, agent will
[278:47] figure out the rest. Whatever your
[278:49] timing is, whether it's every minute,
[278:50] every hour, every year, every 2,000
[278:53] years, whatever, like you can set this
[278:54] stuff up really, really easily. Don't
[278:56] sweat it. Um there is some like
[278:59] misunderstanding usually in modal about
[279:01] like API keys and tokens and credentials
[279:03] and stuff like that. Um inevitably you
[279:05] will need obviously to connect one
[279:06] platform to another and there is always
[279:08] going to be some inherent risk in
[279:09] uploading a secret to the server. So
[279:11] just keep that in mind. By making things
[279:13] cloud accessible you are introducing a
[279:14] little bit of risk. You're basically
[279:15] setting up a server on the internet
[279:16] right like anybody can theoretically
[279:18] access it if they know your credentials,
[279:19] password, whatever. So your agent will
[279:21] prompt you naturally. It'll say hey this
[279:23] script needs your Apollo API key. Should
[279:24] I use what's in your env? All you do is
[279:26] you just say yes. You just say no. You
[279:28] say hold on, use this one instead or or
[279:30] whatever. The way that modal works
[279:31] really is they will store these
[279:32] credentials as an encrypted secret which
[279:34] is separate from your code and then the
[279:36] credentials only actually run when
[279:38] somebody calls the the web hook. So it's
[279:40] never actually like in the codebase or
[279:42] whatever. It's kind of similar to how we
[279:43] separate our code from thev file in um
[279:46] you know our IDE. Very very common. It's
[279:49] not specific to Asian workflows, but
[279:50] yeah, it's the same way that
[279:51] professional engineering teams do this
[279:53] sort of thing. And then what happens to
[279:54] your IDE is it basically just becomes
[279:55] your command center. I mean I obviously
[279:57] do both um cloud workflows and then I
[280:00] also do local workflows. And I actually
[280:01] just like have all of them operate from
[280:03] my IDE. Like I will say hey run this
[280:05] workflow and it'll be like okay this is
[280:06] a cloud workflow so I'm going to call
[280:08] this web hook URL. Then it'll actually
[280:09] create its own request and then send it
[280:11] to my own server which is kind of cool.
[280:14] Um although keep in mind that when you
[280:15] do that as I mentioned earlier you will
[280:17] remove the agentic kind of part the
[280:19] self- annealing and so on and so forth.
[280:21] What's really cool though is your IDE
[280:22] helps you get this done too. And then
[280:24] what you end up with is you actually end
[280:25] up with specific agentic workflows made
[280:27] to automate the process of uploading
[280:28] things to modal which is pretty sweet.
[280:31] What are my recommendations around when
[280:32] to actually turn something into a cloud
[280:34] workflow? Um just scheduled workflows.
[280:36] If you guys have stuff that is like a
[280:38] daily report or a weekly summary or some
[280:39] sort of like recurring scrape or HTTP
[280:41] request, like you can do that in modal,
[280:43] no problem. If it's event triggered, aka
[280:45] um it's very timely, you need to do
[280:47] something within a few moments of some
[280:48] other requests coming in, then set up
[280:50] the web hook functionality like I talked
[280:51] about and then boom. But if it doesn't
[280:53] fit one of these two categories, believe
[280:55] it or not, probably is best to stay
[280:56] local. If it does not need to run when
[280:59] you're not around, it's probably better
[281:00] to like run it while you are around
[281:01] because as I mentioned, these agentic
[281:03] workflow things, they uh they multiply
[281:05] your leverage like crazy right now,
[281:06] right? But they also multiply the error
[281:08] bounds. So you should probably be around
[281:10] to see in case it does something you
[281:11] don't want it to do. Now, if you're just
[281:13] hanging around by your computer for 3 or
[281:15] 4 hours a day or whatever, keep in mind
[281:16] you are now doing like 3 or 4 hours a
[281:18] day of work, keep in mind that like you
[281:21] are now capable of doing 30 to 40 hours
[281:23] of work in the 3 or 4 hours with aentic
[281:25] workflows. Um, so it's not like you're
[281:26] really losing too much here. You're
[281:28] multiplying your leverage as all
[281:29] technology is done. But there are of
[281:31] course some instances and automations
[281:32] where you just always want to run the
[281:33] thing automatically and and that's
[281:34] that's what this is for.
[281:39] Last thing I really need to mention
[281:40] about this is logging and monitoring.
[281:43] Now, if something happens in your IDE,
[281:46] it's typically pretty easy to see where
[281:47] it went wrong. Why? Because you have
[281:49] little reasoning windows that you can
[281:50] pop open, right? It's very easy for you
[281:52] to like see and poke around and be like,
[281:53] "Okay, I could see that there was a
[281:55] problem here with this HTTP request and
[281:56] so on and so forth." But right out of
[281:58] the box, um, in the cloud, you don't
[282:00] have access to that and most of this
[282:02] logging functionality is not around. So,
[282:04] cloud deployments don't have that. What
[282:06] that means is your agent action needs to
[282:07] explicitly force the logging in the
[282:09] code. It won't always be able to do this
[282:11] and um when it can't do this, the debug
[282:13] process can take quite a while. That
[282:15] said, okay, if you learn how to build in
[282:17] some form of observability, that's what
[282:19] this is called in programming. I'm in
[282:21] from the start, it becomes a lot more
[282:23] straightforward. My own personal
[282:24] monitoring setup is I actually have a
[282:26] dedicated Slack channel called
[282:27] Agentic-Cloud-LOG
[282:29] for all cloud workflow updates. So every
[282:31] time a workflow runs, it'll actually
[282:33] automatically send an update to my own
[282:35] Slack channel letting me know if it was
[282:36] successful or not. I have like a pretty
[282:38] superficial highle version of
[282:40] interpretability now and observability.
[282:42] If something happens, I know that it
[282:44] worked. If something doesn't happen, I
[282:45] know that it didn't work. Uh it's not as
[282:46] like super in-depth as it could be, but
[282:48] it's simple enough that I could just
[282:50] look at that and then go to my agent and
[282:51] then say, "Hey, you know, I noticed this
[282:52] thing isn't working. Can you double
[282:53] check to see what's going on?" And then
[282:54] it can do its loop on its own. I don't
[282:56] need to be around. And then, you know, I
[282:57] can continue working on something else
[282:58] while it does that. But if I didn't have
[283:00] this, if I didn't know, then obviously
[283:02] that would be a problem. I've seen some
[283:04] ways that people have built automated
[283:06] systems where they will um automatically
[283:08] take an error notification and send it
[283:10] back to another cloud, a claude or
[283:12] Gemini or, you know, GPT 5.2 instance or
[283:16] something like that and basically say,
[283:17] hey, there was some error with this
[283:18] thing. Fix it. And it'll just like do it
[283:20] completely autonomously. I think that
[283:21] stuff can be kind of cool. Although,
[283:23] keep in mind like most people aren't
[283:25] building like 3,000 web hooks a day,
[283:26] right? So that's usually not the actual
[283:28] bottleneck. the bottleneck is more like,
[283:29] you know, why are you building this
[283:30] webbook in the first place? So, I don't
[283:32] really want to like mislead people here
[283:33] and have them build these cool automatic
[283:35] self-fixing loops when it doesn't really
[283:37] matter all that much in the first place.
[283:39] Not to mention like the probability of
[283:40] it actually entirely fixing itself
[283:42] without introducing more errors is
[283:43] pretty low. And you know, I hopefully
[283:45] you guys understand what I'm trying to
[283:46] say. Okay, so pretty easy to do that.
[283:47] You just say, "Hey, when you deploy to
[283:49] modal, make sure to add logging that
[283:50] sends me a Slack message every time it
[283:52] runs. Here's my Slack web hook URL." If
[283:54] you don't have that, you can ask it,
[283:55] hey, get me a Slack web hook URL. If
[283:57] you're using Discord or something, you
[283:58] do the same thing there. If you, I don't
[284:00] know, want a text message or an email
[284:01] address, you can obviously set that up
[284:02] on your end as well. Pretty
[284:03] straightforward. I also say stuff like,
[284:05] "Hey, could you give me a status check
[284:06] on all my modal deployments? How are
[284:07] they going?" It'll go through all of the
[284:09] modal deployments, run through their
[284:10] logs. Um, it has access to its API. As I
[284:13] mentioned, the docs are pretty
[284:14] straightforward. And so, you end up just
[284:16] getting everything that you need from a
[284:17] a check-in like this. So, you can do it
[284:19] manually, you can do it based off of
[284:20] like some Slack notification, you can do
[284:22] it based off the email notice that you
[284:24] get. There are a lot of um ways to error
[284:26] handle this. The reality is you just
[284:27] need to like know to do this. If you
[284:29] don't do this, you're going to have a
[284:30] bad time. In the future, we will have
[284:32] cloudnative agents, right? Instead of
[284:34] leaving the orchestrator out of this,
[284:36] we're going to actually be inserting the
[284:37] orchestrator in. And so, we're going to
[284:39] minimize that agent accuracy as models
[284:41] get more intelligent and people design
[284:43] better frameworks to deal with us. It'd
[284:44] be pretty cool, right? If you think
[284:45] about it, what you could do is you could
[284:47] just send a natural language query to,
[284:49] let's say, nyx-agent.com.
[284:51] This is my agent, with a question mark,
[284:53] which is a query parameter that says,
[284:54] "Run the lead scraper." It would then go
[284:56] through the agent PTM MRO loop. It would
[284:58] do planning. It would do tool use. It
[285:00] would check its memory. It would do some
[285:02] reasoning and reflection before finally
[285:04] doing the orchestration. But as I
[285:05] mentioned, now we're just at the point
[285:06] where the error bars are a little too
[285:08] high. It will be pretty cool though
[285:09] because once you're done with that,
[285:10] you'll be able to set up a whole
[285:12] ecosystem of just cloud agents that talk
[285:13] to each other and hang out. So, you
[285:15] know, you'll have one agent here, Nick's
[285:17] agent, then you'll have Peter's agent,
[285:18] and then Sam's agent. Then Peter's agent
[285:20] will say something Nick's agent, which
[285:22] will query Sam's agent for more
[285:24] information. and they'll decide on
[285:25] something together and then I don't
[285:26] know, you could even introduce payments
[285:27] into this sort of structure and more.
[285:29] So, early versions of this do exist
[285:31] today. I published some videos exploring
[285:33] some of them. Just check out my channel.
[285:34] They're just a little too high risk
[285:36] right now and it just doesn't really
[285:37] make too much sense to do that all
[285:38] yourself. Okay, so I'm going to walk you
[285:39] through actual modal web hook
[285:41] deployment. Now, I have a bunch of
[285:42] prompt templates and stuff like that.
[285:43] You can obviously get all of that stuff
[285:44] in the link at the very top of our
[285:46] description. Um, let's actually go
[285:48] through setting up uh web hooks in
[285:49] modal. All right, now let's talk about
[285:51] how to take your directives that are
[285:53] inside of your IDE and then put them on
[285:56] the cloud, specifically on a service
[285:58] called modal.com. Now, in case you guys
[286:00] were unaware, modal is basically what's
[286:02] called serverless infrastructure, which
[286:04] is where they have these virtual servers
[286:07] that they spin up on demand on the fly
[286:09] every time that you want them to do
[286:11] something. What's really cool is most
[286:13] the time these serverless
[286:15] infrastructures sort of bend into one of
[286:17] two camps. One is they're like online
[286:20] all the time and then they're always
[286:21] charging you some usage per minute,
[286:24] second, week, month, whatever. The
[286:26] second is they're offline, but then they
[286:28] have to start. This is termed a cold
[286:30] start. And cold starts typically just
[286:32] take a lot of time and energy. So that
[286:34] if you have a flow that requires like
[286:36] instant reaction like a lot of the uh
[286:38] you know executions that you
[286:40] realistically want to host in the cloud
[286:41] um you know it takes a fair amount of
[286:43] time and you don't actually get it
[286:44] instantly. You get it after like a
[286:45] minute or two. So, what's really cool is
[286:47] modal solves both both of these
[286:48] problems. And what you can do is you can
[286:50] just take the execution scripts that you
[286:52] developed and then put them on modal so
[286:53] long as you have the right system prompt
[286:55] uh and have it work essentially
[286:56] instantaneously. So, what you do is you
[286:59] create an account on this service and I
[287:00] should note that I'm not affiliated with
[287:01] them. Do whatever you want. There are
[287:03] variety of other ways to do this, but
[287:04] this is definitely the simplest one.
[287:05] They give you a bunch of free credits,
[287:07] at least as of the time of this
[287:08] recording. And it's worth me noting that
[287:09] I've used Modal now for like at least
[287:11] two weeks, maybe three, and I've used 4
[287:14] cents out of the $5 available. Like
[287:16] realistically, you're not going to run
[287:17] out of this credit usage. Um, just as a
[287:19] test. I can't imagine how much $30 in
[287:22] free credits would take you. If you're
[287:23] just using like a Gentic Workflow for
[287:25] yourself or for like a small to-size
[287:27] business, this will take you really far.
[287:28] So, it's I mean, not free, but it's
[287:30] virtually costless. Once you're done,
[287:32] because we added all the information
[287:34] into our um cloud MD and our agents MD
[287:37] and and so on and so forth. If we want
[287:38] to push one of our flows to Modal, it's
[287:40] actually really easy. All we need to do
[287:42] is just get some authentication going
[287:43] and then obviously find the specific
[287:44] flow that we want. So I want to do the
[287:46] create proposal. I'm going to speak to
[287:48] my agent. Hey, I'd like to create a
[287:51] modal web hook for create_proposal MD. I
[287:54] basically just want to be able to
[287:56] replicate the functionality of that and
[287:58] just do it on the cloud instead.
[288:01] Get me a web hook
[288:03] URL for this.
[288:05] So now it's going to go through read my
[288:08] pre-existing system prompt which will
[288:10] include a bunch of information all about
[288:11] this. All right, this is almost done
[288:13] working through the modal web hook. As
[288:15] part of the system prompt, we set up
[288:17] what's called a web hooks.json. This is
[288:19] just a giant list of all of the
[288:20] different web hooks we have. I should
[288:22] note that before it was empty, so all we
[288:24] did is we just populated it. Now getting
[288:26] some information about the web hook that
[288:27] we set up and it looks like it was
[288:29] deployed successfully. So, we actually
[288:31] have a web hook now available at this
[288:34] URL here, nick- 90891-cloud-
[288:38] orchestrator-
[288:40] directive and so on and so forth. It
[288:42] looks like this takes all of our
[288:44] information in as follows. So, I mean
[288:47] like we could hardcode all of these. We
[288:49] could also have AI generate them. So,
[288:51] what I'm going to do is I'm actually
[288:52] just going to have it run. Okay, great.
[288:54] Could you run a brief example then
[288:56] return the URL when it's done? Okay. And
[288:58] it looks like at the end of it, we got
[289:00] our proposal which is right over here.
[289:02] Let's take a look and see how it did.
[289:04] Demo Corp AI automation pilot has some
[289:07] brief problem areas, has some brief
[289:10] solution areas. You guys remember we um
[289:12] built this earlier on in the course. And
[289:14] uh yeah, we now have essentially an
[289:17] automated proposal generator. Obviously,
[289:19] I wouldn't just like send an HTTP
[289:21] request to this with this information.
[289:22] This is a little bit short. I'm not
[289:24] going to call something demo corp, nor
[289:25] am I going to call uh manual data entry
[289:27] taking 20 hours per week. I'm going to
[289:28] go in a lot more detail. So just for the
[289:30] purposes of this, I'll say great, please
[289:33] update the documentation. Every time I
[289:34] call this, I want to make sure that the
[289:36] demo that I'm providing is really
[289:38] complete. So lengthen the paragraphs for
[289:41] the benefits and the solution
[289:42] statements. Make things longer in
[289:44] general and significantly more
[289:46] realistic. Then rerun the test.
[289:50] And opening up the new proposal. Let's
[289:53] see what this one looks like. Cool. I
[289:55] mean, we did write uh I guess it took my
[289:58] description of long to mean that we
[290:00] should write the title long, too. But
[290:03] these look significantly better. Check
[290:05] this out. We now have way more
[290:06] customized information here. Yeah, this
[290:09] is uh much much better. Awesome. So,
[290:11] that's great. So, what did we learn
[290:12] today? We learned that it is actually
[290:14] really easy to set up a web hook. All we
[290:15] really need to do is we just take our
[290:17] flow which um you know in our case was
[290:19] the creation of a proposal and then send
[290:21] it to our agent alongside um some system
[290:24] prompts that describe how to upload
[290:27] agentic workflows to the cloud.
[290:29] Obviously we need to add our
[290:30] documentation and so on and so forth.
[290:32] Really cool thing about modal is it's
[290:34] just one click takes like two seconds.
[290:36] You just go get your modal API key and
[290:38] then post it in here. It'll ask you to
[290:39] do so. In terms of how to create the
[290:41] token, you just click on that new token.
[290:42] The token secret is on the right. So
[290:44] that's what you copy and then you just
[290:45] paste it directly in here uh when it
[290:47] asks you for the modal token and boom,
[290:48] you're done. And yeah, that's how to do
[290:50] it with web hooks. Okay, now that we've
[290:51] set that up, let's actually go through
[290:53] setting up scheduled um triggers in
[290:55] modal as well. This is different from
[290:57] web hooks obviously because now we
[290:58] wanted to do so on a schedule, not just
[291:00] like based off of some event that comes
[291:01] in. So last time we did this with web
[291:03] hooks. Let me show you instead how to do
[291:04] it with some sort of schedule trigger.
[291:05] Maybe instead of running this via web
[291:07] hook call, what I want to do is I want
[291:08] to run a really simple workflow,
[291:10] probably some lead scraper or something
[291:12] like that, uh, every 5 minutes. So, what
[291:14] I'm going to do is I'm just going to
[291:15] tell it which thing I want to run and
[291:17] then how often I want to run it. And
[291:19] then everything baked into the system
[291:20] prompt is super easy and it'll just tell
[291:22] Modal to run this using what's called
[291:23] cron. Hey, could you send a welcome
[291:25] email to nickleclick.ai
[291:28] every 5 minutes and I want you to set up
[291:30] a modal cloud scheduled trigger to do
[291:33] this for me automatically.
[291:35] Cool. So now it's setting up the modal
[291:36] scheduled function to send the welcome
[291:38] email every 5 minutes. First it's going
[291:41] to check the existing schedule function
[291:42] pattern. Realizes that there is no
[291:45] schedule function pattern. So now it's
[291:46] just going to add some scheduled welcome
[291:47] emails. Cool. And now we have it.
[291:49] Scheduled welcome email is live.
[291:51] Schedule every 5 minutes. So that's what
[291:53] that looks like in cron. What we're
[291:55] going to do now is we're going to send.
[291:58] What's really cool is when you add them,
[292:00] you can actually see the the various
[292:02] schedule triggers. So, there's one here
[292:03] with a little clock icon that says every
[292:05] 5 minutes UTC. If I click on this,
[292:07] you'll see that there are no scheduled
[292:09] calls um that have gone out yet, but
[292:11] there is one in 1 minute and 9 seconds.
[292:13] And modal's cool because it actually
[292:15] allows you to run in between a schedule.
[292:17] So, you can just click on that little
[292:18] run now button, and when you click the
[292:20] run now button, it'll actually do the
[292:22] thing. You can see here that it took 3
[292:24] seconds to start up the server and 1.47
[292:27] seconds to actually send. Finally, if I
[292:30] go to the email address that I
[292:31] specified, you can see that it's
[292:32] actually sent the email. I mean, in this
[292:35] case, I just used a basic kind of
[292:36] onboarding email template, or rather, it
[292:38] created an basic onboarding email
[292:40] template. If I wanted to update this, I
[292:42] just tell my agent, hey, you know,
[292:44] change this so that it's like a welcome
[292:45] email from whatever to whatever. I could
[292:47] even give it a template. I could give
[292:49] whatever I wanted to.
[292:51] And just so that you guys could see it
[292:52] actually run, I'm just going to wait
[292:54] until this counter goes down to zero so
[292:55] you guys see what occurs when you set up
[292:57] a schedule. It's pretty straightforward.
[292:59] I mean, at the end of the day, since
[293:00] we're no longer using directives in our
[293:02] cloud um, you know, servers, all we're
[293:05] really doing here is we're just running
[293:06] a Python script, right? Because it's a
[293:08] Python script, these things execute
[293:09] nearly instantly. And that's really,
[293:10] really helpful rather than, you know,
[293:12] have to wonder about whether or not this
[293:14] thing is sent, rather than have to wait
[293:15] a really long startup time or send and
[293:18] receive things to or from Anthropic, we
[293:20] execute pretty quick. And as you see,
[293:22] because we just finished the previous
[293:24] query, I think within like 3 or 4
[293:25] minutes or something like that, we
[293:26] didn't even have to wind down the
[293:27] server. So, this one took 0 milliseconds
[293:28] and this execution time um was under 1
[293:31] second. So, I mean, we just did this
[293:33] whole thing in like less than a second
[293:34] flat, which is really cool. Heading back
[293:36] over here, you see that we now have the
[293:38] same email. This is your scheduled
[293:39] welcome email. And then we also have
[293:40] that 5-minute block that we talked
[293:42] about. Uh it's almost 1000 p.m. UTC,
[293:44] which is why that time says that. Cool.
[293:46] So, hopefully I've convinced you guys
[293:48] that setting up these sorts of web hook
[293:50] based triggers and schedule based
[293:51] triggers is actually really easy. That
[293:53] definitely isn't the bottleneck here.
[293:55] Before with uh no code platforms like
[293:57] Zapier and NADN and make.com and stuff
[293:59] like that, you had to be a lot more
[294:00] precise. Now you just get the URL and
[294:02] what can we do with the you know web
[294:03] hook URL? Well, now I can just connect
[294:05] it to whatever service I want. I could
[294:06] very easily set it up so that let's say
[294:08] when one of my prospects moves to the
[294:11] send proposal stage in my ClickUp CRM
[294:13] for instance, which by the way I can
[294:15] control completely um agentically using
[294:17] the agentic workflow that I set up
[294:19] previously as an example. uh you know we
[294:21] then trigger the web hook and maybe that
[294:24] occurs automatically as well. And so in
[294:26] this way we build a full endto-end
[294:27] completely automatic flow with web hook
[294:29] URLs that I could share within my
[294:30] organization or give to other people.
[294:32] And that's it. You now know how to build
[294:33] workflows that essentially run without
[294:35] you. The next step is to take this to
[294:37] the next level. Right now we've been
[294:38] running agents sequentially which just
[294:40] means one at a time. But imagine a
[294:42] future where you could actually run
[294:43] multiple agents simultaneously. That's
[294:45] what this next chapter is going to be
[294:46] about. It's going to be about
[294:47] parallelizing your work to multiply your
[294:49] output. Essentially, you're going to go
[294:50] from one employee to a whole team.
[294:52] Instead of doing things like this where
[294:54] you finish task one and then you do task
[294:56] two and then you do task three, we're
[294:58] actually going to in one fell swoop
[295:00] actually do tasks one, two, and three.
[295:02] Then we're just going to recombine the
[295:04] outputs. And we can um do this
[295:06] arbitrarily basically all the way to n
[295:08] service workers or threads or or or
[295:10] instances of an agent so long as you set
[295:12] up the environment right. Okay. Okay, so
[295:14] how do you set up multiple agents
[295:15] simultaneously? Well, spoiler alert, all
[295:18] you're really doing is just opening
[295:19] multiple terminal instances. Nothing
[295:21] super magical here. In VS Code or
[295:23] anti-gravity or any terminal based
[295:25] workflow, they all provide you the
[295:26] ability to open multiple panes, which
[295:28] allows you to run Gemini, GPT, Cloud
[295:30] Code, whatever the heck you want in
[295:32] different terminal windows. My favorite
[295:34] way to do this right now, and sort of my
[295:36] optimal, is three. I don't really work
[295:38] with more than three simultaneously
[295:39] unless we're doing long background tasks
[295:41] just because I find that my attention
[295:43] starts wavering and I start losing
[295:44] effectiveness at like remembering what
[295:46] the heck I'm doing. I always just do
[295:47] this vertically, left, middle, and
[295:48] right. I'll show you guys examples of
[295:50] all that stuff in a minute. So instead
[295:51] of just doing all of this within a
[295:53] single IDE, you can also be kind of
[295:54] smart about it. Uh most models are
[295:56] basically at approximately the same
[295:58] level right now. Like if this is three
[295:59] different models, they're basically all
[296:01] capping out at similar levels of
[296:02] intelligence. There are model
[296:03] differences between them, but most of
[296:04] them are trained in the same data,
[296:06] trained in similar ways, and so they're
[296:07] all kind of like reaching same levels
[296:09] right now. So if you find yourself with
[296:11] an IDE or a model, I should say like um
[296:13] Gemini within anti-gravity that is
[296:15] stricter rate limits or higher costs,
[296:17] instead of running like three instances
[296:19] of let's say Claude against each other,
[296:20] you could run one instance of Claude,
[296:22] then you could run one instance of
[296:23] Gemini, and you could run one instance
[296:24] of like GPT 5.2 or something. By doing
[296:27] all this stuff simultaneously, the
[296:29] frontier models will remain at a similar
[296:31] intelligence level. You're also going to
[296:32] get some slightly different ways to do
[296:34] work which can be beneficial for you if
[296:36] you're still in the building stage or
[296:37] the doing stage not necessarily running
[296:39] this sort of stuff um really high scale
[296:41] and then because we have the same
[296:42] initialization files agents MD cloud MD
[296:45] Gemini MD etc there's no functional
[296:47] difference for the model as a result
[296:49] instead of let's say like this is the
[296:51] the the threshold here where you know
[296:53] you pay $200 a month for the plan of
[296:57] claude I think this is like a the claude
[296:58] max plan or something like that and then
[296:59] you have to pay another I don't know
[297:01] $100 in credits after you hit this
[297:02] threshold, right? So, instead of being
[297:04] like this, what we basically do is we
[297:06] get to use three models instead and keep
[297:08] them below that threshold the entire
[297:09] time. I'm going to show you guys this
[297:10] and a bunch of others um in anti-gravity
[297:12] and then uh you know, have you guys run
[297:14] through practical ways to do this. Um,
[297:16] another thing I wanted to mention was
[297:17] practical limits on parallel agents. So,
[297:19] I find that in practice, two
[297:21] simultaneous agents is probably the
[297:23] average baseline that I like sticking
[297:25] at. Four agents is what I consider to be
[297:27] my soft max before things start getting
[297:28] counterproductive. Like it seems really
[297:30] cool when you have a million tabs open
[297:31] and all these agents are working on
[297:33] things. You feel like a superpower,
[297:34] right? But you're not actually being
[297:36] productive. You're just feeling
[297:37] productive. So instead of like being in
[297:39] a situation like that where most of the
[297:40] agent time will actually be spent
[297:42] waiting for you to like see the tab and
[297:43] like do something with it. I want you
[297:44] guys to know that feeling busy is not
[297:46] the same thing as actually being busy.
[297:48] Feeling productive is not the same thing
[297:49] as being productive. So this is a good
[297:51] way to just like help monitor that. I
[297:53] stick to three to four. Any more than
[297:55] that, you're probably just shooting
[297:56] yourself in the foot. Okay. Okay, so
[297:57] I've talked a little bit about this
[297:58] before, but you know, when you don't
[298:00] know how to build a workflow, you have a
[298:02] couple of approaches here. You can
[298:03] obviously just say, "Hey, can you build
[298:04] a workflow for me that does this?" And
[298:06] it's like a first pass. That's fine. But
[298:08] an advanced way to do it is actually
[298:09] say, "Hey, can you give me three
[298:10] approaches to build this thing?" What
[298:13] you do is you take those three
[298:14] approaches and you give them to either
[298:17] separate models or separate instances.
[298:20] Then what you do is once they're all
[298:21] done, you test to see which one scores
[298:23] the best. So maybe this one here scores
[298:25] 75%, this one here scores 84%, this one
[298:28] here scores 99%. What are you going to
[298:30] do? Obviously you're going to use this
[298:31] one, right? This one's the best
[298:33] combination of speed, cost, accuracy,
[298:34] and so on and so forth. In doing this,
[298:36] rather than having to um, you know, get
[298:38] a subpar solution and then slowly like
[298:41] make a bunch of changes to get to this
[298:42] point. You can actually just run these
[298:43] three agents in parallel and get three
[298:45] times the total search space instead of
[298:48] like manually going through this process
[298:50] one by one by one. I want you to imagine
[298:52] dividing this into three sections,
[298:53] having three of these little snakes go
[298:55] at the same time, which is just much,
[298:56] much faster, and then ultimately build
[298:58] something that is way better and way
[298:59] more scalable. How do you do this?
[299:01] Really straightforward. Just send that
[299:02] brief list of bullet points describing
[299:03] what you want to build to one agent.
[299:05] Then say, can you generate three
[299:06] distinct approaches with in-depth steps
[299:08] for each because I'm going to send this
[299:09] over to another model. Also, give me
[299:11] some pros and cons so I can understand
[299:12] the trade-offs up front. And you know,
[299:14] this will take you a few minutes up
[299:15] front, but it'll also save you a lot of
[299:16] time because if you go with a subpar
[299:18] solution initially, two or three hours
[299:20] down the line, you may still be working
[299:21] out some bugs or kinks or ways to make
[299:23] things faster. Whereas, if you just
[299:24] started with the right architecture
[299:25] right off the bat, you would have had
[299:26] all that stuff solved. Once you're done
[299:28] with that, it's pretty easy. Just open
[299:29] three separate instances of your agent,
[299:31] one for every approach. Give each agent
[299:33] a dedicated working folder. I like doing
[299:35] this in TMP. So I do like uh temporary
[299:37] folder SL1 temporary folder SL2
[299:39] temporary folder SL3 and actually just
[299:41] copy a prompt and I'll say hey you're
[299:43] currently working in this folder. The
[299:44] reason why is because we're creating
[299:46] three copies of a similar build with
[299:48] three different approaches. I want to do
[299:49] it here so that we're not, you know,
[299:51] crisscrossing files and so on and so
[299:52] forth. I'll show you guys a brief
[299:54] example what that looks like in a
[299:55] moment. Once you're done, you just
[299:56] review all three outputs side by side.
[299:58] Pick your favorite approach based off
[299:59] the actual results and the theoretical
[300:00] assumptions. Then you move the winning
[300:02] solution into DO or whatever it is that
[300:04] you're using, cloud skills and so on and
[300:06] so forth. Once it's moved over, you
[300:07] obviously also have to retest
[300:09] everything. And the reason why is
[300:10] because if you don't retest everything
[300:12] when the files are moved over, there may
[300:13] just be some issues with file references
[300:15] and that sort of thing. So this lets you
[300:18] do three builds in the same amount of
[300:19] time. Best one wins. You can obviously
[300:21] do exactly what I'm talking about, not
[300:22] just for the building, but also for the
[300:24] doing. You can run dozens of agents. And
[300:26] there are also things like background
[300:27] tasks which allow you to run agents sort
[300:29] of like in the background so that you
[300:31] could still do something else in
[300:32] parallel on top of it within a single
[300:34] thread. So I've talked a lot about
[300:36] building agentic workflows until now.
[300:38] But what I wanted to do here is just
[300:40] give you guys a brief demonstration of
[300:41] what using agentic workflows looks like
[300:43] in my day-to-day. So to be clear, I
[300:46] personally do a few things with my
[300:48] day-to-day. Number one is I run
[300:51] leftclick which is a growth/outbound
[300:53] AI enabled agency. We basically help you
[300:56] go to market for a product or service or
[300:59] scale up an existing product's outreach
[301:02] using AI and lead scraping mechanisms
[301:04] like you see here. We let you build
[301:06] completely autonomous outbound pipelines
[301:09] that don't rely on you or your team. You
[301:11] just end up with a bunch of booked
[301:13] meetings to sell your service in you or
[301:15] your salesperson's calendar. The other
[301:17] main thing I do is I create content like
[301:19] this. So I make YouTube videos. I write
[301:21] big long guides on how to, you know,
[301:23] build with agentic workflows and stuff
[301:25] like that. And so I'm constantly
[301:27] juggling between these two things. The
[301:29] third thing is I run a school community,
[301:32] actually a series of school communities.
[301:33] One called Maker School over here and
[301:35] one called Make Money with Make over
[301:37] here. And so I have a fair amount that I
[301:39] have to do on a daily basis as I'm sure
[301:41] you can imagine. You know, I have to do
[301:43] things for Leftclick that are kind of
[301:44] older school agency things. I need to
[301:47] create proposals and, you know, I need
[301:48] to scrape leads from my clients and
[301:50] onboard them and stuff like that. Then I
[301:51] have to do things for school like I have
[301:53] to manage replies. I have to, you know,
[301:55] send and receive DMs. I have to answer
[301:57] people's questions and so on and so
[301:59] forth. Plus, I have to do things for
[302:00] YouTube, like I have to create scripts
[302:02] and monitor YouTube for competitors and
[302:04] stuff like that. So, let me just give
[302:05] you a brief example of what me doing all
[302:07] three of these things simultaneously
[302:08] would look like in an Agentic workflow.
[302:10] So, the first thing I'm going to do is
[302:11] I'm going to have this run through
[302:13] basically my end to-end agency flow
[302:15] using a demo kickoff call transcript
[302:18] that uh I'm pulling up from my TMP
[302:20] folder. This is just plain text. Um, you
[302:22] know, I could pull this up from like
[302:23] Fireflies or any other like
[302:25] transcription tool if I wanted. I've
[302:27] just stored this plain text inside of
[302:28] TMP for simplicity. So, I'll say run the
[302:31] post kickoff flow for demo kickoff call
[302:34] transcript
[302:36] over here. you know, maybe I'm just
[302:38] getting started for the day and I want
[302:39] to see what sorts of YouTube outliers
[302:41] there are. Uh, with those YouTube
[302:42] outliers, I'm going to be able to
[302:44] ideulate a new video or something like
[302:45] that, come up with an outline and so on
[302:47] and so forth. So, I'll say run the
[302:49] YouTube outlier workflow and find me
[302:51] between 10 to 20 outliers for agentic
[302:54] workflows.
[302:56] This is what I'm going to be doing a
[302:59] fair amount today because, as you guys
[303:00] could see, I'm recording a video on
[303:02] agentic workflows and, you know, it's
[303:03] sort of like the hot topic now. And over
[303:05] here on the right, I'm obviously
[303:06] managing my school community. And so I
[303:08] built up some agentic workflows to help
[303:10] me pull relevant questions and comments
[303:12] and stuff like that from school. Pull
[303:15] the top 10 most recent school posts from
[303:18] Maker School. And so now I have these
[303:20] three clawed code instances basically
[303:23] running in the background for me. And
[303:24] all I'm going to do as somebody that is,
[303:26] you know, attempting to be economically
[303:28] productive is I'm just going to sit here
[303:29] and then watch over these and then, you
[303:32] know, add and chime in where necessary.
[303:34] So over here on the left hand side, it's
[303:36] asking me some simple questions. I'm
[303:38] just because I'm doing a demo here, say
[303:40] Nick at left
[303:43] uh leftclick.ai AI
[303:46] do the lead genen with modified query
[303:51] and then everything else too. Cool. Over
[303:55] here on the right hand side I see that
[303:56] we're done with my school post. So now I
[303:58] have a bunch of information about this.
[304:01] Looks like Suam recently posted a cold
[304:03] email guide. So I'm going to say Suam's
[304:05] cold email guide. Run me through his
[304:07] step by step. This over here in the
[304:10] middle is using the tube labab API which
[304:12] is part of one of the agentic workflows
[304:13] that I put together to go and then
[304:15] scrape me a bunch of um outliers. So one
[304:17] of our members was kind enough to share
[304:20] with us how he made $500,000 in about 6
[304:23] months or so using instantly which is a
[304:25] cold email tool and then a lot of the
[304:27] same um you know principles that we talk
[304:29] about here. So he ran through and
[304:30] actually provided a ton of info and I
[304:32] mean I'm just curious what that looks
[304:33] like. I could of course use the school
[304:35] UI. I could log into school and then
[304:37] scroll through the post myself and stuff
[304:38] like that. But I set up an agentic
[304:40] workflow to do this. Why? Because it
[304:42] becomes really easy to do really cool
[304:44] things with agentic workflows inside of
[304:46] school. Like hypothetically, I get a lot
[304:48] of questions, right? And what I did was
[304:50] I built a rag or retrieval augmented
[304:53] generation uh tool that essentially
[304:55] looks every time somebody asks a
[304:56] question to see if something similar has
[304:58] been answered in the community before.
[305:00] If so, it actually goes and it gives me
[305:01] the link. Then what I can do is as I
[305:03] respond to them, I could just copy the
[305:05] link over and say, "By the way, if you
[305:06] want a much more detailed explanation,
[305:08] check out this post or so on and so
[305:10] forth." So, what I'm seeing here on the
[305:11] cross niche outlier sheet is it's
[305:13] looking like we're not including all um
[305:16] AI based uh results. And that's probably
[305:19] because realistically there just aren't
[305:21] any competitors for agentic workflows
[305:24] yet because I've kind of coined the
[305:25] term. So, that's great for me. What I'm
[305:27] going to do now is I'm just going to
[305:28] have it run some sort of outlier scraper
[305:30] for terms like AI agents instead. That
[305:32] should give me a fair amount of stuff to
[305:34] work with. Anyway, on the right hand
[305:36] side here, now we're done with this.
[305:38] This is great.
[305:40] Fantastic.
[305:42] Comment extremely valuable guide. So,
[305:46] what I'm going to do is use my school
[305:48] system to go through this, get all of
[305:51] the post ID and stuff like that, and
[305:53] then actually send a comment on that
[305:55] saying, you know, excellent or extremely
[305:58] valuable guide. If I open this up and
[305:59] then scroll all the way down to the
[306:00] bottom, you can see that I just left a
[306:02] comment here saying super valuable
[306:03] guide. And so, I basically get to
[306:05] communicate with school, which is a
[306:06] service that previously required a
[306:07] graphical user interface, just entirely
[306:09] through an agentic workflow instead,
[306:11] which is fantastic. I'm sure future
[306:14] versions of Aentic Workflows will be
[306:15] able to recreate the UX any flavor or
[306:18] way that I want, but for now, this is
[306:20] pretty cool for me. I don't mind. Over
[306:21] on the left hand side, you can see we
[306:23] came up with 15 leads. The reason why I
[306:25] did 15 and not say 1,500 just because it
[306:28] was trying to be mindful of my token
[306:29] costs, knew that I was doing this as
[306:31] part of a demo. Um, we've actually
[306:33] already gone through and and got what I
[306:35] think is nine emails, which is cool. And
[306:37] then after that, if we scroll a little
[306:39] bit further down, this actually went
[306:40] through and uploaded leads to the
[306:42] campaign, which is pretty sweet. It then
[306:44] even added things to a knowledge base
[306:45] and then even went as far as to send a
[306:47] summary email to my client, which in
[306:49] this case I just used my own email for
[306:51] um basically telling them, hey, you
[306:52] know, we're done with the campaign and
[306:53] so on and so forth. What's really cool
[306:54] is it also gave me three links. So, I'm
[306:56] just going to open up these three links,
[306:58] which take me directly to my cold email
[307:00] tool um where I can actually see the um
[307:02] campaigns that it came up with. So, this
[307:05] might sound crazy, but hear me out. I
[307:06] want to generate 50,000 in revenue for
[307:07] company name in the next 90 days. If I
[307:09] don't hit that number, I'll work for
[307:10] free until I do. How? LinkedIn thought
[307:12] leadership. I run a company. We spent
[307:14] six years helping 200 partners at
[307:15] professional services firms turn
[307:17] LinkedIn into a revenue channel.
[307:18] Counting firms, consultancies, financial
[307:20] adviserss, executive coaches. Our
[307:22] clients regularly close 50K deals
[307:23] directly from LinkedIn. Some see 3 to
[307:25] 10x follower growth and most start
[307:27] getting two to three inbound leads per
[307:28] month once the content machine is
[307:29] running. I know this is bold, but I'm
[307:31] confident we could do something similar
[307:32] for you when you open to a quick chat.
[307:33] No pressure, just a conversation. I
[307:35] mean, this is just one of three
[307:36] campaigns with two split tests each.
[307:39] Obviously, while this copy is uh I would
[307:41] consider very punchy and probably
[307:43] [snorts] higher quality than like 80 85%
[307:45] of all of the copy that other people are
[307:47] running for campaigns like this. I'm
[307:48] going to like take a look at the copy,
[307:49] maybe make some minor changes before I
[307:51] actually go through the process. Um, but
[307:52] it's still pretty great, right? I did
[307:54] notice that there was an issue here
[307:55] where the Gmail MCP was not
[307:57] authenticated. So, um, because I was
[307:59] showing you guys how to authenticate
[308:00] MCPS in another video here, it was a
[308:03] demo that I did a few hours ago. um it
[308:05] unauthenticated my MCP. Obviously, if
[308:07] this occurs, you need to reauthenticate,
[308:09] right? So, what I would do in this case
[308:11] would be reauthenticate MCP and then it
[308:13] would just go through that process
[308:14] together. On the right hand side here,
[308:15] I'm going to say something like, hey,
[308:18] what sorts of questions have been asked
[308:20] in the last 24 hours that I can answer.
[308:23] So now I'm going to get a list of
[308:24] questions the right hand side here.
[308:26] That's pretty straightforward. While I'm
[308:27] doing this, I'm reauthenticating my
[308:29] Gmail MCP. That's going to trigger OOTH,
[308:31] which is pretty cool. in the middle
[308:32] here. We're still scraping more
[308:34] outliers.
[308:35] Would you give me the highest priority
[308:37] ones
[308:40] over here? We now need to restart the
[308:42] Gmail MCP server. So, I'm just going to
[308:44] restart cloud code. The new O flow
[308:46] should capture a refresh token. Let me
[308:47] know once you've completed the browser
[308:48] authentication and then I will start
[308:50] again. Cool. So, I'm going to do is I'll
[308:51] go new. Just going to go /mcp.
[308:58] We'll say off
[309:01] my MCP, off my Gmail MCP.
[309:05] Over here on the right hand side, you
[309:07] see some people have asked some
[309:08] questions. So, Emil's asked some
[309:09] questions about client delivery when
[309:11] you're offering a lead genen system. For
[309:12] how long should you sign up the client
[309:13] for and how long can you keep on
[309:15] providing new leads for the company? For
[309:16] how long are you guys typically running
[309:17] campaigns for clients? On average, I run
[309:20] campaigns for a minimum of 90 days. I
[309:22] didn't used to do this, but I found that
[309:24] 90 days was sort of the sweet spot as it
[309:26] typically takes some stopping and
[309:28] starting before you figure out the right
[309:30] offer combination and the right lead
[309:32] targeting. When I started, I went
[309:34] month-to-month entirely. I'd probably
[309:35] recommend that in your case just to keep
[309:37] friction low, but hopefully this helps
[309:39] give you an understanding of the various
[309:41] ways that you could put something like
[309:43] this together. And we have another
[309:44] question here about 400 bucks. Well,
[309:47] first off, nice job on the 400 bucks.
[309:49] the JSS score tanking is hard to hear.
[309:53] My recommendation would be to send him a
[309:55] message
[309:57] letting him know that immediately after
[310:00] you finished your contract, you had a
[310:01] massive JSS dump. This is something
[310:03] about Upwork. And softly implying that
[310:06] this will unfortunately have serious
[310:08] consequences as to your ability to get
[310:10] future work. I would also ask him if
[310:12] there's something or anything that you
[310:13] can do to improve that job success
[310:16] score, whether it's going back and
[310:17] providing free or additional work etc.
[310:20] It looks like on the third he put some
[310:22] copy together. So I'm just going to say
[310:23] show me the copy.
[310:26] Cool. And now this is going to go
[310:27] through top to bottom and then send that
[310:28] info. What's cool is this also formats
[310:30] my text for me. So I can just dump all
[310:32] this in. It's now going to authenticate.
[310:35] So I'm just going to head over to my
[310:36] email. Looks like it's successful. So I
[310:39] can go back here. This looks pretty
[310:41] solid. I would probably
[310:43] remove the
[310:54] just because this doesn't offer a lot of
[310:55] value. If you work with
[311:00] somebody in your niche, I would
[311:03] recommend that.
[311:11] This is usually considered positive
[311:14] social proof. The would you be open to a
[311:16] 15-minute call about this as the last
[311:19] question is a little weak. I would
[311:22] probably be hyper specific with the
[311:25] times that I'm asking for. I.e. could
[311:28] you do?
[311:36] Okay, over here on the left hand side we
[311:37] have the Gmail MCP. So I'll just say
[311:40] send me
[311:42] a hello email to nicholas@gmail.com.
[311:47] Over here we have the output of our
[311:49] agent. So let's take a look at this.
[311:52] Looks like it's saying that a lot of
[311:53] these are related to ICE agents, which
[311:57] is sort of a political thing that's
[311:58] going on right now, which is why we're
[312:00] getting these outliers. Obviously,
[312:02] that's not, you know, that's not what
[312:03] I'm going to be doing. I really care
[312:04] about looking for those outliers, but I
[312:06] do see some of these are more agent
[312:08] related. So, a agents that actually work
[312:09] the pattern anthropic just revealed. We
[312:11] have the thumbnail right over here.
[312:14] That's cool. Google Workspace Studio
[312:16] between these two. Sam Alman looking
[312:18] quite menacing.
[312:20] These are pretty funny, honestly. Uh,
[312:22] cool. Yeah. So, I have some reasonable
[312:23] outliers here, which is nice. Um, you
[312:25] know, I'm probably not going to be able
[312:26] to do the political ones, and I'm not
[312:27] really making content like that or
[312:29] talking head, so I can avoid those. But
[312:30] hopefully you guys see that, you know,
[312:31] now I have some outliers that I could
[312:33] work with that have just been released
[312:34] in the last few days. Um, but, you know,
[312:36] maybe I could start modeling my content
[312:37] around or something like that.
[312:38] Meanwhile, the MCP now works. So, we did
[312:40] fix that. And then I've also sent three
[312:43] um messages within school. So, I'm just
[312:44] going to take a little peek at that.
[312:47] Cool. also just sent that just sent that
[312:51] and then right over here just said that
[312:54] and you can see it's also formatted my
[312:55] text for me and stuff like that. Okay,
[312:57] so I don't do this because I think any
[312:59] of these three particular ones that I'm
[313:00] running are super powerful or super
[313:02] incredible or whatever, but these are
[313:03] just things that I had to do today, you
[313:04] know, and I just figured I would run
[313:06] through them with you guys. Um, this is
[313:08] like a practical look at this the
[313:09] day-to-day work that I do within my
[313:10] Agentic Workflow IDE. Um, and hopefully
[313:13] you guys see how this is a very simple
[313:15] and easy way to like multiply your
[313:16] leverage, right? I mean, I just did like
[313:18] a whole endto-end workflow for uh,
[313:20] admittedly a demo client, but a demo
[313:22] client nonetheless on the lefth hand
[313:24] side. In the middle, I ran like outlier
[313:26] detector and on the right hand side, I
[313:28] even interacted and engaged with school
[313:30] posts much faster than I could do
[313:32] manually. Um, that auto automatically
[313:34] formatted my text, found like good
[313:36] questions for me to answer and so on and
[313:38] so forth. You guys can use Agentic
[313:40] Workflows in your ID in the exact same
[313:42] way for whatever the knowledge work is
[313:44] that you need to do. Whether you're
[313:45] copyrighting campaigns, whether you're
[313:47] scraping leads, whether you're just like
[313:49] organizing your CRM or adding things to
[313:50] a record, like it is now entirely
[313:52] possible. And I hope you guys also see
[313:54] that there is a split between the
[313:56] building of a workflow and then the
[313:58] using of the workflow. The building is
[314:00] something you do once and then the using
[314:01] is an opportunity to make a return on
[314:03] investment on the building time over and
[314:05] over and over and over again basically
[314:06] every day. I don't really think it's a
[314:08] far cry to say that most people could
[314:10] probably automate 50% or more of their
[314:12] day-to-day work using flows like this
[314:14] and at minimum at least make it 50% more
[314:17] enjoyable or easier to do. So, next I
[314:19] want to talk a little bit about sub
[314:20] agents. Why sub agents? Because context
[314:23] windows fill up really, really quickly.
[314:26] Most people don't realize this, but
[314:28] current models have a context window of
[314:30] around 200,000 to around 1 million
[314:32] tokens in certain instances. And that
[314:35] sounds like a lot, but when you add
[314:36] tools, all of this context disappears
[314:39] much faster than you would think.
[314:41] Specifically, detail oriented tasks burn
[314:44] through context really quickly because
[314:45] of that loop that I was telling you
[314:47] about. Debugging burns through context
[314:49] very quickly because of the loop I was
[314:51] talking to you about. Any sort of MCPs
[314:53] burn through context really quickly. And
[314:55] before you know it, half of your whole
[314:57] context window of let's say 500,000
[314:59] tokens or something is filled with
[315:01] intermediate garbage that significantly
[315:02] reduces the probability of a successful
[315:05] output. Now, this phenomenon where
[315:07] there's a bunch of garbage in your
[315:08] context window and that leads to poor
[315:10] quality outputs is called context
[315:12] pollution. And pollution is essentially
[315:15] where that intermediate memory, that
[315:16] sort of midterm memory that I talked
[315:18] about way back at the beginning of the
[315:19] course, gets cluttered with a bunch of
[315:21] irrelevant noise. Now, scientists have
[315:24] been working with these models for quite
[315:26] a while. As I may have mentioned to you
[315:28] at some point in the past, AI models
[315:29] these days are more grown than they are
[315:31] built. And so, it's very much like a
[315:33] natural phenomenon that we are testing.
[315:35] And what they've found is consecutively
[315:37] across thousands and thousands and
[315:39] thousands of tests, the more tokens in a
[315:41] context window, typically the poorer the
[315:45] quality is. And the relationship looks
[315:47] something like this.
[315:49] And the reason it looks like this is
[315:51] because over here on the very left hand
[315:53] side, you probably have zero tokens,
[315:54] right? And so if it's fresh and you ask
[315:57] it to do something with no context or
[315:58] whatever, it'll do an okay job. If you
[316:00] add a bunch of context and you tell it,
[316:03] hey, you know, I'd like you to do this.
[316:04] Here are a couple of examples of past
[316:06] instances of this run correctly. Uh
[316:08] here's a bunch of context. Here's a
[316:09] bunch of links and whatever. Performance
[316:11] actually goes up in the short term. What
[316:13] you'll notice is as you go on and on and
[316:15] on and you start filling it with more,
[316:17] you know, irrelevant garbage and
[316:18] whatnot, performance and quality and
[316:20] outputs go down a lot. Now, back in the
[316:22] day with GPT2 and GPT3 when I was
[316:24] starting 1 second copy in my content
[316:26] writing business, you know, this was
[316:28] super super important and it was so
[316:30] important that I actually trained all of
[316:31] my writers not to use more than 256
[316:34] tokens at a time. So, imagine that we
[316:36] had to stick under 256 tokens with our
[316:39] prompt. Essentially, if we went any over
[316:41] that, we found um quality went off a
[316:43] cliff. In our case, now we can use
[316:44] significantly more than 256 tokens.
[316:46] Obviously, this point here is probably
[316:48] somewhere closer to like 10k or so, not
[316:50] 256. So, we're sort of blessed in that
[316:52] way. But still, there is that
[316:54] relationship between more stuff in the
[316:55] context window and then poor quality.
[316:57] So, we need to make sure that uh you
[317:00] know, if all else is held equal, we try
[317:01] and minimize the amount of tokens in our
[317:03] context as much as possible. Now that we
[317:04] understand that, onto sub aents. The way
[317:06] that sub agents solve this is through
[317:08] isolation of context. Now the idea is in
[317:12] order for something to be a sub aent and
[317:14] not a part of the main agent, it gets
[317:16] its own fresh clean context window to
[317:19] work in. So all you do with a sub agent
[317:22] is basically you give it a task. You let
[317:25] it do all the messy work in its own
[317:27] space and then you return only the
[317:29] relevant findings. So just as a quick
[317:32] little demonstration here, let's say
[317:34] this is a chat back and forth with you
[317:37] and you know your agent. So this is you
[317:41] over here. This is your agent over here.
[317:45] Any every time you ask it something, it
[317:47] sends something back and so on and so
[317:48] forth. Imagine what happens every time
[317:51] you send a call. Essentially what is
[317:53] occurring is we stack up all of these.
[317:56] And so our total context, if you think
[317:57] about it, is that block up there plus
[318:00] this block over here plus that block
[318:02] over here plus that block over here plus
[318:04] that block over here. So how many blocks
[318:06] is this? We're just counting. That's
[318:08] five blocks. And let's say everyone's a
[318:10] thousand words. You're actually sending
[318:11] like a,000 words. So what that means is
[318:13] on the next query, what we're doing is
[318:14] we're sending a total of five blocks of
[318:17] context plus the thing that we asked. So
[318:19] maybe 6,000 in total. What sub aents
[318:21] allow you to do is instead of doing this
[318:24] um you know having this 1,000 here,
[318:26] let's pretend that this over here is
[318:27] actually a sub aent loop. What we do is
[318:29] we actually just eliminate this
[318:30] completely. Okay, and then we eliminate
[318:33] that completely. And so what ends up
[318:34] happening is basically the model instead
[318:37] of storing the results directly in the
[318:39] context, okay, only stores the outputs
[318:42] of that response. So all we're really
[318:45] doing to make a long story short is we
[318:46] ask the sub agent to do something. It
[318:48] deals with all of that stuff sort of
[318:50] internally in its own head and then just
[318:52] spits us out a brief summary plus the
[318:54] results that we asked for. If you guys
[318:56] are keen, you'll notice that this is
[318:57] very similar to how reasoning tokens get
[318:59] discarded after use to keep the total
[319:01] token countdown. Remember how there's
[319:03] that sort of like thinking tab and you
[319:06] can open up the thinking tab if you want
[319:07] to see what's kind of going on under the
[319:09] hood. Well, those tokens aren't actually
[319:10] added to what I talked about here. Those
[319:12] tokens disappear. So, it's the exact
[319:13] same thing. Whether it's reasoning,
[319:15] whether it's sub aents, both of these
[319:16] strategies are meant to reduce the total
[319:18] amount of stuff and garbage polluting
[319:20] the context window. And the data backs
[319:22] this up. Anthropic, a company that sort
[319:24] of not coined sub aents, but is
[319:26] definitely the leading force behind them
[319:28] with clawed code. Um, it ran a test
[319:30] where opus was the lead and then opus
[319:32] essentially controlled a bunch of sub
[319:34] aents and had those sub aents do a
[319:36] variety of smaller tasks before
[319:38] reporting back their findings. And it
[319:39] found that it outperformed single agent
[319:41] opus by over 90% on research. based
[319:44] tasks. Now, I should note that's
[319:46] research, right? Not all tasks are
[319:48] research related. Obviously, research
[319:50] involves a ton of tokens. And so, sub
[319:52] agents here obviously did way better
[319:54] than they probably do on most other
[319:55] tasks relative to, you know, the
[319:57] standard. But, there are some
[319:58] circumstances where sub agents do
[320:00] perform significantly better even in
[320:02] day-to-day use. And that's why I'm
[320:03] talking about it. You'll know that I uh
[320:06] I really haven't really given a crap
[320:07] about sub agents or anything like that.
[320:09] This is a very recent phenomenon for me.
[320:10] People have been talking about sub
[320:11] agents for the better part of the last
[320:12] two years. And every time they are like,
[320:14] "Nick, why aren't you using sub aents or
[320:15] whatever?" I'm always like, "Because
[320:16] it's pointless." Like sub agents as an
[320:18] architectural addition just complicate
[320:21] things. They don't actually make things
[320:22] easier. Models for the most part can
[320:24] handle tasks on their own. It's okay.
[320:25] You don't need to like, you know, try
[320:26] and develop some big fancy framework.
[320:29] Well, model intelligence has gotten to
[320:30] the point where we can actually make use
[320:32] of these things now. So long as you're
[320:33] nuanced and kind of smart about how you
[320:35] do it. So the catch between this is
[320:38] there's implementation complexity
[320:39] because you are now inserting your own
[320:40] biases and how you think the model
[320:42] should operate. Then you're also
[320:43] compounding errors. What do I mean by
[320:45] compounding errors? I mean, you know, if
[320:47] you think about it, there's a step here
[320:48] where in order for my parent agent to
[320:50] send something off to a child or sub
[320:52] agent, it needs to summarize what it is
[320:54] that it wants the sub agent to do. And
[320:56] so that right there is a step. And that
[320:58] step might be like 99% accurate. But as
[321:00] we know, if you have a bunch of things
[321:01] that are 99% accurate, if you add enough
[321:05] steps into the process, eventually that
[321:07] turns out into something that is much
[321:09] less than 99% accurate, right? It might
[321:11] be like uh I think my example was 99.9%
[321:14] stretched out over a,000 tasks was 36%
[321:16] accuracy at the end of it. So you know
[321:18] the more uh steps you have like
[321:20] summarization steps sending to this this
[321:22] does some summarization sends back the
[321:24] more area you're inserting in the
[321:25] process and the higher the variability
[321:26] is. So basically what you need to do is
[321:28] you just need to find a situation where
[321:30] the added error as a result of the
[321:32] additional steps is outweighed
[321:34] essentially by the beneficial effect on
[321:36] the context. And there's no real
[321:38] non-trivial way to know this right off
[321:40] the top of your head. Like you need to
[321:41] test this. You need to try this. Now
[321:43] since I've tested this and trying this,
[321:45] my recommendation is to stick to two sub
[321:48] aent types for now. And there's in in
[321:49] particular just two that I'm going to
[321:51] talk about. Before I tell you what those
[321:52] two are, the other two big wins from sub
[321:55] agents are there's context management.
[321:57] Your main agent will stay super clean
[321:58] and it'll only have things that are
[322:00] highly relevant to what it is that we
[322:01] want. So let's say you delegate to a
[322:03] bunch of sub aents that have MCP access.
[322:05] Those sub aents are the ones that load
[322:07] up all the context and other MCP. Then
[322:09] they do the job and then they report
[322:10] back. If your sub aents are atomic
[322:12] enough, obviously we can do that over
[322:13] and over and over again and we can
[322:14] actually make some real headway without
[322:15] polluting the context window. The second
[322:17] is parallelization. So sub aents can
[322:19] actually run all simultaneously. What
[322:21] you'll find when you delegate to sub
[322:22] agents like I'll show you later is a
[322:25] single agent can spawn multiple and then
[322:28] those multiple basically all run on
[322:29] their own and report back whenever
[322:31] they're individually finished. So if
[322:33] you've ever seen, you know, Gemini or
[322:35] Claude sort of do research, typically
[322:37] what'll occur is it'll spin up, you
[322:39] know, three or four research sub aents
[322:42] because that's native to their
[322:43] architecture and they're basically just
[322:45] going to wait until all three or four of
[322:48] these are completed. But these don't
[322:50] occur top down. It's not like this
[322:51] finishes first, this finishes second,
[322:53] this finishes third, this finishes
[322:54] fourth. These are all individual
[322:56] processes. So this one might finish
[322:58] first and report back. This one could
[323:00] finish second, this one could finish
[323:01] third, and this one could finish fourth.
[323:03] It's a very interesting phenomenon that
[323:04] you guys have probably seen but not
[323:06] fully understood where that comes from
[323:07] yet. A good example of that
[323:08] parallelization is if you want to scrape
[323:10] a bunch of leads. I do tons of lead
[323:11] scraping, hence why it's always my
[323:12] example. But um you know, you don't need
[323:14] to scrape all these one by one. You
[323:16] don't need to scrape, let's say, 30,000
[323:17] independently through some big serial
[323:19] thing. You can actually just have your
[323:21] parent agent, okay, spin up three sub
[323:23] aents and maybe every sub agent itself
[323:26] uses some form of parallelization to do
[323:28] a task. And so now what you're doing,
[323:30] and I know this sounds really fancy,
[323:32] you're probably like, does it actually
[323:33] work? Now what you're doing is you're
[323:34] basically just cutting the total amount
[323:35] of time it takes to do this thing down.
[323:37] And then what what occurs is once these
[323:39] are all done, okay, if you kind of like
[323:40] check mark these, they report their
[323:42] results back to the main agent. Then the
[323:44] main agent's task is really just
[323:45] consolidating these, putting them
[323:47] together, which if you think about it
[323:48] like the act of I don't know stitching
[323:49] together three lists of things is a lot
[323:51] easier of a task to ask a parent agent
[323:53] than you know actually going through the
[323:54] orchestration of scraping that many
[323:56] leads. If something previously takes 3
[323:57] hours sequentially with the spin up, the
[324:00] uh scraping and then the wind down. This
[324:02] might only take 30 minutes in parallel
[324:03] because you are consolidating those
[324:05] fixed costs uh in terms of spin up and
[324:07] then wind down and then your parent
[324:09] agent just gets the results. In terms of
[324:10] like the technical and logistical bits
[324:12] where sub aents live, they're defined as
[324:14] markdown files. Exact same thing as the
[324:16] directives. Nothing really different
[324:17] here. Uh in clawed code specifically,
[324:20] they're included/
[324:22] aents. So this is a tople folder with
[324:25] another folder underneath it. And then
[324:26] if you want to go global as in have that
[324:28] accessible like across your entire
[324:30] project directory, then you put it in
[324:31] your current directory. Claude/ aents.
[324:34] The disambiguation there isn't super
[324:36] important. If you want sub agents to
[324:38] only have access to a specific workspace
[324:40] or project, this is how you do it. But
[324:41] if you wanted to have access to
[324:42] everything, uh then you'd put it over
[324:44] here and that way sub agents can work
[324:45] across your workspaces. Now, other
[324:47] agenda coding tools do follow similar
[324:49] patterns. There is no consensus, at
[324:51] least not as of the time of this
[324:52] recording, how Gemini is organizing its
[324:54] sub aents, how Codeex and so on and so
[324:56] forth are organizing their sub aents.
[324:57] But rest assured, everybody has their
[324:59] own little framework and it's all about
[325:00] like the system prompt, right? You can
[325:02] absolutely just have these models spin
[325:03] up the equivalent of the claw code
[325:05] version of sub aents. It's just a matter
[325:07] of doing a little bit more heavy lifting
[325:08] up front. The anatomy of a sub aent file
[325:11] right now is again you have the name
[325:14] then you'll have the description and
[325:15] then also really important you have the
[325:17] permissions. So which tools the sub aent
[325:20] can access tools in our do framework for
[325:22] instance are going to be directives and
[325:23] executions. After that, you have the
[325:25] system prompt. And just like we do
[325:27] system prompts across the entire
[325:29] workspace, we also have a sub aent
[325:31] specific system prompts. Um, you guys
[325:34] don't actually need to know any of this.
[325:35] I just say make me a sub agent that does
[325:37] X, Y, and Z. And this sort of stuff is
[325:39] just baked into um at least the Claude
[325:41] family of models as of the time of this
[325:42] recording. It'll most certainly be baked
[325:44] into other ones as well. So yeah, you
[325:45] don't need to create these yourself. You
[325:46] can just ask the agent to do it. Um
[325:48] here's an example prompt. literally just
[325:50] create a sub agent called document that
[325:52] gets called after every workflow to
[325:53] update to consolidate changes in the
[325:55] directive and execution scripts. It'll
[325:57] go through a process of creating the
[325:58] thing. I'm going to show you what that
[325:59] looks like in practice and yeah, you're
[326:01] done. Your agent will generate a file,
[326:03] put in the correct folder, and then it's
[326:04] immediately available. Talk about
[326:06] something recursive, huh? It's agents
[326:07] creating agents. I should note that
[326:09] agents can create the definition of an
[326:11] agent, but an agent can only spawn an a
[326:14] sub aent. Sub agents can't spawn more
[326:16] sub agents themselves. And this is like
[326:17] a memory constraint. They don't want sub
[326:19] aents to be able to spawn more sub aents
[326:21] to be able to spawn more sub aents
[326:22] because essentially what you're going to
[326:23] do is you're going to end up with a
[326:25] situation where you know your parent
[326:26] agent spins up two sub aents your sub
[326:29] aents spin up two sub aents your two sub
[326:31] aents spin up two more sub aents and so
[326:33] on and so on and so on and so forth
[326:35] until basically your I don't know CPU is
[326:37] as hot as the surface of the sun not to
[326:39] mention you know some safety and
[326:40] security concerns and stuff like that so
[326:43] um really what happens is we sort of
[326:45] limit it to if we just cut all this
[326:47] stuff out these too. And so your parent
[326:49] agent can spin up however many sub aents
[326:51] it wants, but they all report back to
[326:52] that parent agent. So what are those two
[326:54] sub aents that I talked about that I
[326:56] personally find genuinely useful?
[326:58] They're not required to be clear. You
[327:00] can absolutely use DO and whatever other
[327:02] framework um it is that you want to
[327:03] build with without sub aents. But I
[327:05] found that these actually improve the
[327:07] accuracy and quality of my execution
[327:08] scripts and they are a joy to use as
[327:10] opposed to something that is you know
[327:11] laborious and time inensive and so on
[327:13] and so forth. The first is the reviewer
[327:16] sub agent. So a main issue with building
[327:19] directive orchestration executions or
[327:21] cloud skills is your orchestrator will
[327:23] write a bunch of code. And so if you ask
[327:25] it, hey, how's this code looking? It's
[327:27] going to be biased towards thinking that
[327:29] that code is correct because it just,
[327:30] you know, probably ran it a bunch of
[327:31] times and it sees some correct runs in
[327:33] its history. The unfortunate thing is
[327:35] that's kind of like asking somebody to
[327:36] read their own essay right after writing
[327:38] it. Um, any experienced writers will
[327:40] know what you want to do is you want to
[327:41] take a little bit of a break. You want
[327:42] to like take a deep breath, go sit down
[327:44] somewhere else, you know, like do not
[327:46] look or read that essay. Come back to it
[327:47] maybe an hour or two later because when
[327:49] you come back to it an hour or two
[327:50] later, your mind is no longer polluted
[327:52] by all the biases and your own flavoring
[327:55] of thought surrounding, you know, how
[327:56] good that essay is. When you come back
[327:58] to it, you basically come back to it
[327:59] with fresh eyes and you can tell by
[328:01] definition whether or not it is a good
[328:02] essay or a bad essay, whether it's some
[328:04] of your good best work or maybe some
[328:05] sort of mediocre work. And so reviewer
[328:07] sub agents work basically the exact same
[328:09] way. Instead of the orchestrator which
[328:12] remembers all its decisions, what we do
[328:13] is we give it to something that can
[328:14] actually see a lot more clearly. What
[328:16] occurs is the reviewer gets loaded with
[328:18] completely fresh context which is just
[328:20] the directives and just the executions
[328:22] that we built. We then ask it to
[328:24] evaluate the script purely on its
[328:26] quality. In short, it acts like a second
[328:28] pair of eyes. We give it no context
[328:30] about what this thing is for. And the
[328:31] idea is it needs to like determine the
[328:33] context through the code. Meaning the
[328:34] code has to be documented. It has to be
[328:36] pretty straightforward to understand and
[328:38] read. Has to be written simply. And then
[328:39] if you think about it, if it has no
[328:40] context whatsoever, it'll be able to
[328:41] look at it and be like, hm, that seems
[328:43] kind of weird because most other code
[328:44] like this will probably have some error
[328:46] handling, but this one doesn't. I think
[328:48] this should probably build in some error
[328:49] handling and then it can provide
[328:50] suggestions back to the main agent who
[328:52] is sort of biased to actually go and and
[328:54] build the thing. How do you do this?
[328:55] Well, your main agent just calls sub
[328:57] agents automatically when you define
[328:58] them in the system prompt. So in
[329:00] agents.mmd, after you create any script,
[329:02] use the reviewer sub agent to check for
[329:04] its quality. That's a totally okay thing
[329:06] to write somewhere in your agents.MG um
[329:08] G or system prompt. Um while it won't be
[329:10] 100% accurate, aka it's not going to do
[329:12] this every single time, you know, it
[329:14] will do this up until the context window
[329:15] gets polluted enough, which is a pretty
[329:17] reasonable thing uh to do. And I find
[329:19] just having this probably improves my
[329:20] accuracy a good 5 10%. In addition, you
[329:23] can obviously also ask the model to do
[329:24] things manually. So you could say, "Hey,
[329:26] uh that's great. Call the reviewer sub
[329:28] agent, just make sure everything's
[329:29] okay." Or, "Call our reviewer and ensure
[329:31] that you know this is fine. Hey, I want
[329:33] you to make some edits after you're done
[329:34] making those edits. Ping reviewer,
[329:36] double check that it's okay. If it's
[329:37] okay, then give me the thumbs up. These
[329:39] are all just flavors and variants of
[329:40] things that you can ask your agent.
[329:42] Obviously, your mileage varies and it's
[329:44] up to you. The second sub aent that I
[329:46] recommend building is a document sub
[329:48] agent. So, this one updates directives
[329:51] based on what the system has learned
[329:52] over time. You know, after your workflow
[329:54] self anneal for a while inside of your
[329:56] IDE, sometimes the agent will forget to
[329:58] update. That's just because, as I
[330:00] mentioned, it has a ton of context and
[330:02] so it's going to forget some of the
[330:03] things that you mentioned initially in
[330:04] the system prompt like, "Hey, I want you
[330:05] to update your thing." So, what the
[330:07] document does is it just reviews scripts
[330:09] and then it updates the directives to
[330:10] reflect their current behavior. A lot of
[330:12] the time in practice, what happens is
[330:14] you'll have some um issues with your
[330:16] script and so the agent will go and
[330:17] update the script over and over and over
[330:19] and over again. And then the directive
[330:21] will be untouched despite the fact that
[330:22] you spent all this time um updating the
[330:24] script. And then on a fresh instance of
[330:26] a new agent, maybe tomorrow or the next
[330:28] day, you try running the workflow and
[330:29] then it goes like, "hm, this is weird. I
[330:31] tried running the execution script, but
[330:32] it looks like it wants different
[330:33] parameters. What's going on here? I I
[330:35] followed the directive." And then, you
[330:37] know, there's a big debugging step and
[330:38] then it fixes it. But it takes like, I
[330:40] don't know, 5 or 10 minutes. Well, just
[330:41] call your document sub agent and have it
[330:43] just rectify everything right then and
[330:44] there instead. What you do is you give
[330:46] it read access to all files and then
[330:48] write access just to your directives.
[330:50] So, it can read through all of your
[330:51] execution scripts, but it can't make any
[330:52] updates to that. And then it can update
[330:54] the directives to match the execution
[330:56] scripts. This is pretty simple, too.
[330:58] Create a sub aent whose job is reviewing
[331:00] scripts and updating documentation so
[331:01] everything aligns and just call it
[331:02] whenever you update a script. Anytime
[331:04] you make a change, your main flow will
[331:06] then call the document sub agent. Just
[331:07] do some review. The document will review
[331:09] the scripts and summarize the changes
[331:11] automatically since it's sort of like
[331:12] trained to do so with its prompt. Now,
[331:14] as I mentioned before, the really cool
[331:16] thing about sub aents is they don't just
[331:17] work in sequence. Um, they can work in
[331:19] parallel. What I mean by parallel? Well,
[331:21] just like opening new tabs, sub aents
[331:23] let you run tasks in parallel. Just like
[331:25] opening three or four instances of
[331:26] Gemini and then asking each to do a
[331:28] different thing. You could just run
[331:29] three or four sub agents within a single
[331:31] window. Now, your parent agent has the
[331:34] ability to run multiple agents what's
[331:35] called synchronously and then wait for
[331:36] the results of all of them. And so, as
[331:38] I've talked to you guys many times, you
[331:40] know, if you have some parent A, this
[331:42] can now whip up C, B, and then D, and
[331:45] then it can combine the results into
[331:47] some result E, loop that back around,
[331:49] and then just use that result to, you
[331:50] know, proceed instead of doing
[331:52] everything sequentially. Because this
[331:54] this can take a fair amount of time,
[331:56] right? If every single step here takes,
[331:59] I don't know, 20 minutes, that's 20
[332:00] minutes here, 20 minutes there, 20
[332:02] minutes there. Why not just like
[332:03] consolidate them all and then only have
[332:04] one 20-minut step? Parallelization is
[332:07] probably one of the freest wins in
[332:08] computing to be honest because most of
[332:09] your CPU cores and GPU cores are
[332:11] literally just left idle 99% of the
[332:13] time. This is a good way that you can
[332:14] make use of them. When you do this, the
[332:16] context window will also stay really
[332:17] small. It's usually under a couple
[332:18] thousand tokens in the main thread to do
[332:19] the thing. And then every sub aent works
[332:22] independently without cluttering your
[332:23] primary workspace, assuming that you
[332:24] know you you you give it the right
[332:26] system prompt so that it can do that.
[332:28] Hey, I want you to store intermediate
[332:30] research results in, you know,
[332:32] tmp/ressearch instead of polluting my uh
[332:35] parent agents context window. Now,
[332:37] obviously when you give sub agents
[332:38] autonomy, okay, and keep in mind that
[332:40] that autonomy is also given by the
[332:43] parent agent. So, it's like you're
[332:44] multiplying autonomies just like you're
[332:45] multiplying probabilities. Obviously,
[332:47] safety becomes pretty important, right?
[332:49] And so, what I recommend is giving each
[332:51] sub agent different tool access. You
[332:53] need to specifically say you can only do
[332:55] X, Y, or Z. So, your guardrails have to
[332:58] be a lot stronger than let's say the
[332:59] guardrails on, I don't know, some other
[333:01] sort of agent. I'm just going to draw my
[333:04] little bowling ball analogy over here,
[333:06] but it is very much one of those things.
[333:07] You do need to have some sort of
[333:08] guardrail. I think of it like giving my
[333:10] intern, you know, readonly access to my
[333:13] production database. Production database
[333:14] being like my live actual database that,
[333:17] you know, people are really using. I
[333:18] don't know. You know, I've had some
[333:20] issues in the past where people that
[333:21] aren't very skilled come into my
[333:22] organization and then they start
[333:23] screwing around with databases they
[333:25] probably shouldn't be touching and then
[333:26] I don't know, they drop my tables and
[333:28] then all of a sudden everything's all
[333:29] crappy. So, you know, an SOP that I and
[333:31] I think a lot of other people probably
[333:33] use is, hey, you know, if you're new to
[333:34] my organization, you only get read
[333:36] access to things. You can only like look
[333:37] at it. If you want to make changes, ask
[333:39] me. Well, sub agents are very, very
[333:40] similar. And this is obviously an
[333:42] architectural pattern that we're
[333:43] borrowing from hierarchical
[333:44] organizations. This is called lease
[333:45] privilege. It's where you give each
[333:46] agent only the resources it needs for a
[333:49] specific job. If you think about the
[333:50] document sub aent that I was telling you
[333:52] about, the document sub agent only
[333:53] really needs to be able to read the
[333:55] executions. It doesn't need to be able
[333:57] to write them. The only thing it needs
[333:59] to be able to write, which is sort of
[334:00] like the really scary thing is the
[334:02] directives. And so in that way, we
[334:04] ensure that it's only really ever, hey,
[334:06] information from executions goes into
[334:08] directives, not really the other way
[334:09] around. I could of course create like a
[334:11] hypers specialized optimized coding
[334:13] agent which has a bunch of context about
[334:14] the best ways to do code. Then maybe I
[334:16] give that read access to my directives
[334:18] and write access to my executions or
[334:19] something. A couple of other limitations
[334:21] about sub agents that I want to talk
[334:22] about because I think they're really
[334:24] shiny and they're fun and everybody
[334:25] likes being the top of some big
[334:27] organization. They add some overhead and
[334:29] they also add some latency. So spinning
[334:31] up a sub agent and getting some results
[334:33] back does take extra time is not instant
[334:35] unfortunately because you are literally
[334:36] spinning up like a separate entity. So
[334:39] for simple tasks, your main agent will
[334:40] almost always be faster just doing it
[334:42] directly. And so like most simple tasks,
[334:43] it'll just do the main thread. I'm not
[334:45] going to spin up a sub agent to do my
[334:46] research for me. Even though some of
[334:48] that is just built into the way that
[334:49] these agents now work, uh I'm just going
[334:51] to be like, hey, you know, look up this
[334:52] and get me the results. I'm not going to
[334:54] be like, spin up the research sub agent
[334:56] and then feed that into the
[334:57] decision-making sub aent and so on and
[334:59] so forth because I think that's just
[335:01] kind of BS. So yeah, I don't really use
[335:03] sub aents for most things. The time cost
[335:04] often isn't worth it. I'll only really
[335:06] use it in the context of like a hypersp
[335:08] specific framework like directive
[335:09] orchestration execution like cloud
[335:11] skills and so on and so forth. So let me
[335:13] show you how to actually create one of
[335:14] these sub aents. I'm using sub aents in
[335:16] cloud code just because cloud code is
[335:18] currently like the defined sub aent
[335:21] pattern. So I could just say hey make me
[335:22] a sub aent it'll do it. I want you guys
[335:24] to know that you can build sub aents or
[335:25] at least things that are analogous to
[335:27] sub aents in whatever model uh structure
[335:30] you want. All a sub aent really is
[335:32] doesn't have a formal definition yet,
[335:33] but I'm going to define it is something
[335:35] that does not have context aside from
[335:38] the input that it is given by a parent
[335:40] agent. So, I want to create a reviewer
[335:42] sub agent, right? In order to create a
[335:43] reviewer sub aent, I'm just going to
[335:44] like voice dump my um my requirements
[335:47] directly in. Hi, I'd like to create a
[335:49] reviewer sub aent. The whole idea behind
[335:51] the reviewer sub agent is it will look
[335:53] at the execution scripts that another
[335:55] agent develops and it will look at it
[335:57] with totally fresh eyes and just
[335:58] determine if this is done in as
[336:00] effectively or efficiently a manner as
[336:02] humanly possible. It will then provide
[336:04] instructions to the top level agent
[336:06] which can then take that guidance and
[336:08] review to improve the quality of the
[336:10] build.
[336:11] I'm just going to feed all that in
[336:13] directly. It's then going to do some
[336:15] tinkering and some thinking.
[336:17] Then it's going to ask me a bunch of
[336:18] questions. My main goal here is I want
[336:21] you to be able to call the sub agent as
[336:23] required. So set it up in whatever way
[336:25] allows you to do the calling.
[336:28] I also want you to check everything. All
[336:31] of the above. The output format should
[336:33] just be whatever is most amendable or
[336:36] convenient for you since you are going
[336:38] to be the one that is calling it. Okay.
[336:39] Funnily enough, I ran into a limit um
[336:42] earlier when I tried finishing that. So,
[336:44] I went and I added um what's called
[336:46] additional credits, which is pretty easy
[336:48] to do essentially in Claude. Anyway,
[336:50] your current session eventually hits a
[336:52] cap. I'm using the Claude Max plan, so I
[336:54] have a fair amount of usage, but yeah, I
[336:56] eventually do run into some sort of
[336:57] issue. Uh and so what I did is I enabled
[337:00] the extra usage toggle and then I said,
[337:02] "Hey, just use this to pay for any extra
[337:03] usage whenever I do." I set a very low
[337:06] spending cap because I very rarely run
[337:07] into sessions. It's my fault for just
[337:09] doing like 20 demos today. Anyway, um
[337:12] after that I then had this run on a
[337:14] test. So I said, "Hey, run the reviewer
[337:16] on scrape_cross_nicheoutliers.
[337:19] py." So it's now actually running a
[337:21] test. It's saying, "Hey, read the
[337:23] directive first. Understand the
[337:24] criteria. Read the script completely.
[337:25] Produce the structure of view output
[337:26] specified in the directive. Be
[337:28] ruthlessly honest and specific." And so
[337:30] this thing is only going to have read
[337:32] functionality. And it since found me a
[337:34] bunch of information that I could use to
[337:35] improve it. script is functional but a
[337:37] significant efficiency issues. Excessive
[337:39] API calls, no rate limiting and
[337:41] potential quota exhaustion. Here they
[337:43] are. Wonderful, wonderful, wonderful.
[337:46] This is really cool. An O squared string
[337:48] matching for 175 niche terms. Full
[337:50] transcript load only 8K characters used.
[337:53] So now we can do basically a fix. I'll
[337:55] say great, try this on the create
[337:59] proposal
[338:01] flow. I'm doing this because um the
[338:03] create proposal flow is pretty solid,
[338:05] but it's also quite simple and I
[338:06] actually want to see how this would work
[338:08] doing a review on create proposal. It's
[338:10] now spinning up base sub agent. Now the
[338:12] way that sub aents work at least in
[338:13] cloud code is there's a defined
[338:15] structure. They live include/comands
[338:19] inside of the commands is the sub aent
[338:21] tool spec. As you see, we haven't
[338:23] actually done that. There is no um you
[338:25] know reviewer sub aent here. That's
[338:27] because the model typically defaults
[338:29] just doing this in the directive
[338:30] orchestration execution framework way by
[338:32] just like having a directive called hey
[338:34] you're the agent but we want to do this
[338:36] in claude format specifically just
[338:38] because the probability of this working
[338:40] is a lot higher on like totally fresh u
[338:42] roles so what I'm going to say is
[338:45] excellent work before you proceed create
[338:48] an actual claude command for this right
[338:51] now you are using a directive to spawn
[338:52] the sub aent but I instead want you to
[338:54] search through theclaw pod folder and
[338:58] see how it should be done. After you're
[339:00] done, update the execution script with
[339:04] the reviewer sub agents thoughts.
[339:10] This is fantastic. It found a bunch of
[339:12] discordant issues that probably
[339:14] significantly increased error rate. Now
[339:16] we have correct paths. Everything here
[339:18] is much more on board with uh uh the
[339:21] directive. And we've even gone as far as
[339:23] actually creating the claude command. So
[339:26] this is fantastic. What I will now say
[339:27] is great test create_proposal.
[339:30] py with the demo sales call transcript
[339:33] intmp. It found it. Now what it's doing
[339:36] is generating all of the information.
[339:38] This is the same thing that I ran in an
[339:40] earlier demo in case you guys are aware.
[339:42] It's going to use a plausible email.
[339:44] Create the JSON input and then test.
[339:46] Cool. And this actually significantly
[339:48] improved the functioning of create
[339:50] proposal. Previously we had to do some
[339:52] some polling. Now what it does is it
[339:54] waits for the document to be ready
[339:55] before returning the link. Um so we
[339:58] actually have this um ready and we've
[340:00] significantly improved the effectiveness
[340:02] of the script as well. It's a welcome
[340:04] surprise. I wasn't actually expecting to
[340:06] improve this. Looks like the one issue
[340:08] here is it just titled this with the
[340:10] company name which made that spill over
[340:12] to a second line. I can obviously change
[340:13] that anytime I want. But yeah, the rest
[340:16] of this looks pretty solid. I'm not
[340:17] seeing any major issues here. So
[340:19] fantastic work. Hopefully it's clear.
[340:21] You can use a reviewer sub agent and a
[340:24] document sub agent to significantly
[340:26] increase the effectiveness of not just
[340:27] the DO framework but your agentic
[340:30] workflows in general. And that's that.
[340:32] Thank you very much for making it
[340:34] through the agentic workflows course. If
[340:35] you guys have made it through the many,
[340:37] many hours of content, you are now in a
[340:39] position where you can use and leverage
[340:40] aic workflows better than probably 99.9%
[340:44] of the rest of the population. The skill
[340:45] set that you guys have is
[340:46] extraordinarily in demand right now.
[340:48] Whether you want to use it for your own
[340:50] business, maybe a software business,
[340:52] maybe an agency or service business, an
[340:54] ecom business, or in a consulting
[340:56] business to help other people with their
[340:57] businesses through Agentic Workflows.
[340:59] So, whatever category you're in, take
[341:01] the knowledge that you've learned today
[341:03] and use it to produce great things and
[341:04] accelerate the transition to a more
[341:06] efficient economy. If you guys like this
[341:08] sort of thing and want to learn how to
[341:09] implement agentic workflows in other
[341:10] people's businesses, please check out
[341:12] Maker School. It's my 90-day
[341:14] accountability roadmap that guarantees
[341:16] you your first customer for AI
[341:18] automation or agentic workflow
[341:20] consulting businesses. That means that
[341:21] by the end of the 90-day period, you
[341:23] will have your first customer or I'll
[341:25] give you your money back. More
[341:26] generally, it's just a great community.
[341:27] We have over 2,000 fantastically
[341:29] talented and capable people in there.
[341:31] It'd be great to add another. Aside from
[341:33] that, want to thank you from the bottom
[341:34] of my heart for making it to the end of
[341:35] the video. Have a lovely rest of the day
[341:37] and best of luck implementing Agentic
[341:39] workflows.
