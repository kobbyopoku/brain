---
title: "LOOP ENGINEERING: THE 20-STEP PATH FROM PROMPTER TO SYSTEM DESIGNER"
source: "https://x.com/cyrilXBT/status/2079609999844691976"
author:
  - "[[@cyrilXBT]]"
published: 2026-07-21
created: 2026-07-22
description: "In June 2026, three people independently arrived at the same idea within a single week.Peter Steinberger, the builder of OpenClaw, said publ..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "loop-engineering"
---
![Image](https://pbs.twimg.com/media/HNxA8DhWUAA03Hq?format=jpg&name=large)

In June 2026, three people independently arrived at the same idea within a single week.

Peter Steinberger, the builder of OpenClaw, said publicly that you should stop prompting coding agents and start designing the loops that prompt them. At nearly the same moment, Boris Cherny, who leads Claude Code at Anthropic, said he no longer prompts Claude directly, he has loops running that prompt Claude and figure out what to do, and his actual job is writing loops. Days later, Addy Osmani, an engineer at Google, wrote the term up and gave it a name: loop engineering.

None of them invented the practice from nothing. They named something that was already happening, because the tools underneath it had quietly crossed a threshold. Coding agents had become reliable enough to finish a real task unattended. Scheduling had become cheap enough that running a task repeatedly, on a timer, stopped looking wasteful. The cost of a single agent run had dropped far enough that trying something five times cost less than thinking carefully about it once.

That threshold is the reason this roadmap exists. Prompting was the skill when a human needed to sit at the keyboard directing an agent line by line. Loop engineering is the skill now that the agent can be handed a goal and left to run. This is the complete 20-step path from one to the other, in order, because the order matters more than any individual step.

Here is why the order specifically matters, before the steps themselves. Loop engineering is not a single skill you either have or do not have. It is a stack, where each layer depends on the one beneath it actually being solid. Building a scheduling trigger, step 14, before you have a real stop condition, step 10, just means you have automated a system that can now waste money unattended instead of only while you are watching. Building persistence, step 11, before you have real verification, steps 6 and 7, means you are carefully recording lessons learned from a Judge that might be rubber-stamping bad output, which makes the persistence layer actively harmful rather than merely useless. Skipping ahead in this list does not just mean missing a feature. It means building the exciting-looking parts on top of a foundation that cannot actually support them, and discovering that only once something has already gone wrong at scale.

## Phase One: The Mental Shift (Steps 1 to 4)

Step 1: Accept That You Are The Bottleneck, Not The Model

The first real step is not technical. It is admitting that the limiting factor in your current workflow is not the model's capability, it is your own presence in the loop. Every time you sit and wait for a response, read it, then type the next instruction, you are the slowest part of the system by a wide margin. The model can act, verify, and retry far faster than you can supervise it doing so.

This step has no prompt attached to it. It is a decision. Until you actually believe this, every subsequent step will feel like unnecessary overhead instead of what it is, removing the actual bottleneck.

Step 2: Stop Confusing A Longer Prompt With A Better System

The instinct when something goes wrong is to add another instruction to the same prompt. Over months this produces a prompt that is a dense, self-contradicting wall of rules the model can no longer hold in working memory all at once, so it pattern-matches on whatever feels most recent and quietly drops the rest.

Loop engineering replaces this instinct entirely. Instead of adding another rule to a prompt, you add another component to a system. A verification step. A memory file. A scheduled trigger. The prompt itself should get shorter over time as the system around it gets more capable, not the other way around.

Step 3: Learn To See Every Task As Five Moves

Any single turn of a loop, regardless of the specific domain, decomposes into five moves. Discovery, figuring out what actually needs to happen. Handoff, passing the task to whatever will execute it. Verification, checking the result against something real. Persistence, recording what happened so it is not lost. Scheduling, deciding when this runs again.

Most people's current workflow only has two of these moves explicit, discovery and handoff, done manually, in a chat window. The other three either do not exist or happen invisibly in the person's own head. Loop engineering is the practice of making all five moves explicit and automatic.

Step 4: Identify Your First Real Candidate Task

Before building anything, pick one task you already do repeatedly, with a standard you could write down if asked. Not your hardest problem. Not something entirely novel. A task with a real, recognizable definition of done, something a colleague could look at and immediately agree was or was not completed correctly. This constraint matters more than it looks. A task with no clear definition of done cannot have step three, verification, built for it, and a loop without real verification is not a loop, it is just an unattended guess.

## Phase Two: Building The First Loop (Steps 5 to 9)

Step 5: Write The Definition Of Done Before Writing Any Prompt

This is the step most people skip and the one that determines whether everything after it works. Before you write a single instruction for the agent, write down, in plain language, exactly what a correct result looks like. Specific, checkable criteria, not a vague feeling of quality.

DEFINITION OF DONE for \[task name\]: - \[Specific, checkable criterion 1\] - \[Specific, checkable criterion 2\] - \[Specific, checkable criterion 3\] This task is NOT done if any of the above is missing, even if the output looks complete or polished.

If you cannot fill this out for your chosen task, return to step 4 and pick a different one.

Step 6: Separate The Builder From The Judge

The single most important architectural decision in any loop. The role that produces the work and the role that checks the work must be separated, because a model reviewing its own output in the same breath that produced it tends to defend that output rather than genuinely scrutinize it.

The Builder gets creative latitude and produces a first attempt. The Judge gets the Builder's output plus the definition of done from step 5, and nothing else it needs to be talked out of. Ideally the Judge also has access to something the Builder does not, a test suite, the original source document, live data, so its verdict comes from real evidence, not just a second opinion formed the same way the first one was.

Step 7: Give The Judge Ground Truth, Not Just An Opinion

A Judge that only sees the Builder's output can tell you whether it looks coherent. It cannot tell you whether it is actually correct. For coding tasks, ground truth is the test suite and the actual execution output. For content tasks, it is the original source material and brief, side by side with the draft. For research tasks, it is the actual documents that were supposed to be used.

If you cannot name the specific ground truth your Judge will check against, your loop does not have real verification yet, no matter how confident the Judge's language sounds.

Step 8: Write The Handoff Format Before You Write The Handoff Prompt

The Builder's output and the Judge's verdict both need a defined structure, not free-flowing prose, or the Manager in the next step has nothing reliable to route on.

BUILDER OUTPUT: deliverable + confidence + known uncertainties JUDGE VERDICT: PASS / FAIL / NEEDS REVISION + specific issues found + what ground truth this was checked against

Step 9: Run It Manually Once, All The Way Through, Before Automating Anything

Before you wire up scheduling or automatic retries, run the full Builder-then-Judge sequence yourself, by hand, once. Read the Judge's verdict critically. Would you have agreed with it? If the Judge passed something you know is wrong, or failed something that was actually fine, fix the ground truth or the criteria before moving forward. Automating a broken verification step just produces broken results faster.

A Worked Example Through Steps 5 To 9

To make the last five steps concrete, here is how they play out on a real, common task, turning a raw source document into a finished piece of content.

The definition of done, from step 5: every factual claim in the draft traces back to something actually present in the source document. The draft satisfies every specific requirement in the brief, length, tone, required structure. The core argument survives clearly, without being diluted by filler.

The Builder, from step 6, receives the source and the brief and produces a draft, along with an explicit statement of what it was uncertain about while writing, a number it was not fully sure was in the source, a claim it inferred rather than found stated outright.

The Judge, from step 7, receives the draft and the original source side by side, never the draft alone, and checks each of the three definition-of-done criteria separately, returning a pass or fail on each one individually rather than one blended overall score. Collapsing three distinct checks into a single verdict hides exactly which dimension actually failed, which is the single most common way a working loop quietly stops giving useful feedback.

The handoff format, from step 8, means the Judge's verdict arrives as a structured object, not a paragraph of hedged prose, three explicit pass or fail results with a specific reason attached to any failure.

Running this by hand once, per step 9, before automating anything, is what catches the case where your Judge is too lenient, passing a draft with a fabricated statistic because the writing style was polished, or too strict, failing a draft over a stylistic preference that was never actually in the brief. Both failure modes are common on a first attempt, and both are far cheaper to catch manually once than to discover after the loop has already run fifty times unattended.

## Phase Three: Adding The Loop's Missing Pieces (Steps 10 to 14)

Step 10: Build The Manager And Its Stop Condition

The Manager reads the Judge's verdict and decides what happens next. This is also where the loop's stop condition lives, and it must be written as hard logic, not a soft instruction the model can talk itself past.

STOP CONDITIONS: Maximum revisions: 3. On the 3rd failed verdict, escalate to a human with the full history, do not attempt a 4th cycle. Quality threshold: every item in the definition of done must show PASS. Budget ceiling: if this task exceeds \[X\] cost or \[Y\] time, stop immediately regardless of current state.

A loop without a real stop condition is not a system. It is a liability waiting for the day the task turns out to be genuinely unsolvable. The specific reason a soft instruction fails here is worth understanding, not just accepting. "Stop when it's good enough" inside a prompt is a suggestion, and a model under enough pressure, having failed several revisions already, will often talk itself into believing the current attempt is close enough to pass, precisely because it wants to produce a satisfying resolution to the task. A hard iteration counter checked mechanically by code, or by an explicit rule the Manager cannot reason its way around, does not have that failure mode.

Step 11: Add Persistence, So The Loop Remembers Across Runs

A loop that starts from zero every single time it runs has no memory of what it learned last time. Add a simple persistence layer, one file per genuinely new lesson, with a one-line summary at the top, recording what was learned or corrected and why it mattered. Critically, only record what is not already captured elsewhere, duplicated memory is noise, not knowledge.

The discipline that makes this step actually work long-term is restraint at write-time. The instinct is to log everything that happened in a session, which produces exactly the bloated-transcript problem this roadmap warned against in step 2, just moved into a memory folder instead of a prompt. A lesson worth writing down is something that would cost real time to rediscover if forgotten, not a record of routine work that succeeded exactly as expected.

Step 12: Add A Consolidation Pass On A Schedule

Persistence alone eventually produces the same problem as a bloated prompt, dozens of files, many saying slightly different versions of the same thing. On a recurring schedule, weekly is reasonable, review the memory files, merge duplicates into single, sharper lessons, and delete anything that has since proven wrong. The goal is fewer files with more density each, not an ever-growing pile.

This step is the one most people skip entirely, because it produces no visible new capability on its own, it only prevents a future problem. That invisibility is exactly why it needs to be scheduled explicitly rather than left to happen whenever someone notices the memory folder has gotten unwieldy, which in practice means it never happens until the loop's performance has already started degrading under the weight of contradictory, half-relevant lessons competing for the same context window.

Step 13: Add The Recall Step

At the start of any new run, have the loop scan the one-line summaries in memory, identify which lessons are actually relevant to the current task, and load only those. Explicitly instruct it to say when nothing in memory applies, rather than force-fitting an irrelevant past lesson onto a new situation just because memory exists.

Step 14: Add A Scheduling Trigger

Decide when this loop runs without you starting it manually. A cron job. A file watcher. A recurring calendar-driven trigger. This is the step that turns a system you run on demand into one that runs while you sleep, and it is usually the single easiest step in this entire list, and the one most people never bother implementing even after building everything else.

## Phase Four: Scaling And Hardening (Steps 15 to 18)

Step 15: Stress Test The Loop Before You Trust It

Before relying on this loop for anything real, deliberately test it against four failure modes.

Give it a genuinely unsolvable version of the task and confirm the Manager actually stops instead of looping forever, since a loop that only gets tested on tasks it can complete has never actually demonstrated it knows how to fail gracefully.

Feed the Judge an output you know is subtly wrong, something that reads well but contains a specific factual or logical error you planted deliberately, and confirm it actually catches the flaw rather than passing something plausible-sounding.

If the Builder and Judge share the same underlying model, feed the Judge a mistake that model characteristically makes and see if it waves the mistake through, since a Judge sharing the Builder's blind spots defeats the entire purpose of the separation from step 6.

Calculate the worst-case cost of the loop running to its maximum revision limit, using your most expensive model calls and longest reasonable output, and decide honestly whether that number, appearing on a real invoice, would alarm you.

Running these four tests before trusting a loop with anything that matters catches the overwhelming majority of failures that would otherwise show up for the first time in front of a client, a boss, or your own bank statement, rather than in a controlled test you ran on purpose.

Step 16: Route Tasks To The Right Model, Not The Same One Every Time

Once a loop works, resist the habit of running every part of it on your single favorite model. The Builder role usually benefits from your most capable model, since it is doing the actual hard reasoning and a weaker model here produces a worse first draft that costs more revision cycles to fix than it would have cost to generate well the first time.

The Judge role, checking against a specific written standard, often performs just as reliably on a smaller, cheaper, faster model, since it is not being asked to be creative, only consistent, and a smaller model checking against an extremely well specified checklist frequently matches a larger one at a fraction of the cost and latency.

The Manager, routing based on rules you already wrote down, almost never needs your most expensive model at all, since its job is executing logic you already specified, not open-ended reasoning, and it runs at least once per iteration regardless of how the Builder and Judge perform, which makes its per-call cost matter more than its raw capability.

This tiered approach, expensive model for building, cheap and consistent model for judging routine checks, cheap model for routing, is usually where the real cost savings in a loop come from. Most people assume cost control means fewer loops or fewer revisions. It actually comes from matching model cost to the actual difficulty of each specific role inside the loop you already built.

Step 17: Expand To A Second Loop, Not Five At Once

The temptation once the first loop works is to build several more immediately, tackling five different tasks in parallel because the architecture technically supports it now. Resist this longer than feels comfortable. Get one loop running reliably enough that you have genuinely stopped checking its output closely, meaning it consistently passes your own manual spot-checks over a real stretch of time, not just a single successful demo run everyone happened to watch closely. Only then start the second loop, on a different task, ideally one that maps onto something completely different from the first, so you are testing whether the underlying skeleton generalizes rather than just tuning the same task further.

Step 18: Give Yourself A Shared View Across All Running Loops

Once you have more than one loop running, track a shared view of cost and stop-condition triggers across all of them, not per-loop in isolation. A single loop with a reasonable per-task budget looks completely fine on its own. Ten loops each individually within budget can still sum to an alarming total nobody notices until the aggregate bill arrives, precisely because each individual loop's tracking looked fine in isolation.

Log every stop-condition trigger specifically, not just successful completions. A loop hitting its revision ceiling constantly, while others rarely do, is telling you its Judge's standard is miscalibrated, too strict to ever actually pass, or checking against the wrong ground truth entirely, not that the underlying task is simply hard. That pattern is invisible if you are only tracking successes and treating every escalation as an isolated, unremarkable event rather than a data point about that specific loop's design.

## Phase Five: Becoming A System Designer (Steps 19 and 20)

Step 19: Stop Measuring Yourself By Prompts Written

The clearest sign the shift has actually happened is a change in what you pay attention to day to day. A prompter tracks how many good prompts they wrote. A system designer tracks how many loops are running, how reliable each one is, and how much of their own time got returned to them by systems that no longer need supervision. If you are still measuring your own productivity in prompts typed, the mental shift from step one has not fully landed yet, regardless of how many loops you have technically built.

Step 20: Teach Someone Else The Five Moves

The final step is not really about your own systems anymore. It is confirming you actually internalized the shift by explaining it to someone else without reaching for jargon. Discovery, handoff, verification, persistence, scheduling. If you can walk another person through building their own first loop using only those five moves and the steps above, you have made the actual transition this roadmap describes. You are no longer the person inside the loop, typing the next instruction. You are the person who designed it, standing outside, watching it run.

## The Four Costs That Accrue Silently If You Skip Steps

Worth closing on a warning, since skipping steps in this roadmap does not fail loudly, it fails quietly, in ways that only show up much later.

Verification debt accumulates when you skip steps 6 and 7, building loops with no real Judge or no real ground truth. The loop looks like it is working because the output looks fine, right up until a mistake compounds silently across dozens of runs before anyone notices.

Comprehension rot sets in when you skip step 20, running loops you built once but could no longer explain or debug if they broke, because you never had to internalize why each piece existed.

Cognitive surrender happens when step 1 never really lands, when you keep manually double-checking every output out of habit long after the verification system has already proven itself, defeating the entire point of building the system in the first place.

Token blowout is what happens when you skip step 10, running loops with no real stop condition, discovering the actual cost only when the bill arrives.

Every one of these costs is avoidable, and every one of them is avoided by the same discipline. Build the steps in order. Do not skip the ones that feel unglamorous. The boring steps, the definition of done, the stop condition, the ground truth, are the ones actually doing the work. The interesting-sounding parts, the clever prompt, the elaborate architecture diagram, matter far less than whether the system you built actually knows when it is right, when it is wrong, and when to stop.

That is the entire distinction between a prompter and a system designer. Not cleverness. Discipline about the parts that are boring to build and easy to skip.

Follow [@cyrilXBT](https://x.com/@cyrilXBT) for the exact loop templates and Builder-Judge-Manager setups behind every step in this roadmap.