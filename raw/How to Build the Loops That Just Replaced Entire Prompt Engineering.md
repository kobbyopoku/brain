---
title: "How to Build the Loops That Just Replaced Entire Prompt Engineering"
source: "https://x.com/hanakoxbt/status/2077387678241141070"
author:
  - "[[@hanakoxbt]]"
published: 2026-07-15
created: 2026-07-21
description: "For two years, getting more out of an AI agent meant writing a better prompt.That era is quietly ending. The best engineers in the world sto..."
tags:
  - "clippings"
  - "agentic-engineering"
  - "loop-engineering"
---
![Image](https://pbs.twimg.com/media/HNRbhcEXoAAl0un?format=jpg&name=large)

For two years, getting more out of an AI agent meant writing a better prompt.

That era is quietly ending. The best engineers in the world stopped writing prompts a while ago and started writing loops - systems that prompt the agent, check the result, and keep running until the work is done.

Karpathy's overnight script found 20 optimizations he had missed in two decades of tuning by hand. Boris Cherny, who built Claude Code, has not written a line of code this year. Anthropic engineers now merge close to 8x more code per day than they did in 2024.

None of them typed anything smarter. They stopped typing at all.

Here is what a loop actually is, when you need one, when you do not, and how to build your first one.

## 700 experiments while the human slept

March 2026. Andrej Karpathy pushes three files to GitHub. Around 630 lines of code.

One file held the model. One scored it. One told the agent what to explore and what to leave alone. The agent could only touch the training file. Nothing else.

The cycle was boring on purpose. Read the code, propose a change, train for five minutes, check if the score improved, keep the change if it did, roll back if it did not, then go again.

He pointed it at a model he had already tuned by hand for two decades. He let it run for two days.

It ran 700 experiments. It found 20 improvements. One of them was a missing scalar multiplier in the attention mechanism, subtle, not the kind of bug any linter would ever catch, but exactly the kind of thing a careful engineer could have found and never did.

Shopify's CEO ran the same trick overnight on an internal model. He woke up to a 19 percent quality gain on a model half the size of the previous one.

The insight is not "the AI is smarter." Humans get tired after experiment twelve. Loops do not get tired at all.

![Image](https://pbs.twimg.com/media/HNRUy_3XUAAf1EM?format=jpg&name=large)

## A loop is not a prompt on a schedule

Most people hear "loop" and think cron. That misses the whole thing.

A prompt is one instruction. A loop is a goal the AI keeps working toward until it gets there, with nobody in the chair. It plans, executes, verifies its own result, feeds the result back in, and repeats.

Five stages: discover, plan, execute, verify, iterate. Three of them do the actual work.

The verifier is the heart of the loop. Without a real gate on the output, you do not have a loop, you have the agent grading its own homework forever. A gate is a test that passes or fails, a build that compiles or crashes, a linter that returns zero or non-zero. Not a second agent with an opinion.

State is what makes the loop learn. A file on the side, a Linear board, a project log, somewhere outside the conversation that records what was tried and what failed. Tomorrow's run resumes instead of starting from scratch.

A stop condition is what keeps it sane. Every real loop has two exits: the goal is met, or a hard cap fires. Skip this and you have built a machine that runs all night for nothing.

Miss any of the three and you have not built a loop. You have built an expensive script.

## The four conditions before you build one

Loops earn their cost only when four things are true at the same time. Miss one and the setup takes more than it returns.

- The task repeats at least weekly. Less than that and the setup cost never amortizes.
- Something can automatically fail the work. A test, a type check, a linter, a build.
- Your token budget can absorb the waste. Loops re-read context, retry, explore.
- The agent has senior engineer tools. Logs, a reproduction environment, the ability to run the code it writes and see what breaks.

The honest version, the part nobody selling loops will tell you: most people do not need the heavy version yet. If you are on a consumer plan trying to run overnight verification loops on serious work, the token bill arrives before the productivity gain does.

Good first loops are the boring ones. CI triage. Dependency bumps. Lint-and-fix passes. Flaky test reproduction. Issue-to-PR drafts on a codebase with strong tests already in place.

Bad first loops are the interesting ones. Architecture rewrites. Auth code. Payments. Anything where "done" is a judgment call and a human still has to weigh in.

## The five blocks that make a loop real

Every real loop is assembled from the same five pieces. Claude Code and Codex ship all of them now.

The first is automation. The heartbeat. Something that fires the loop on a schedule or an event. /loop runs on a cadence. /goal keeps going until a condition you defined actually holds. Without a heartbeat, the loop is a script you ran once and forgot about.

The second is a skill. Project knowledge saved as a claude-md file the agent reads on every run. Without it, the loop re-derives your context from zero each cycle. With it, intent compounds. The loop knows your conventions, your build steps, the thing you never do because of that one incident three months ago.

The third is sub-agents. The maker and the checker cannot be the same model. The one that wrote the code is far too generous grading its own work. The one that wrote the article misses its own weak sections. Writer fast and cheap. Reviewer slow and strict. That separation is most of the quality.

The fourth is connectors. The loop opens the pull request, closes the ticket, pings the channel when CI turns green. This is the difference between an agent that says "here is a suggested fix" and a report waiting for you in the morning saying the PR is already merged.

The fifth is the verifier. The test, type check, or build that fails bad work automatically. Everything else is plumbing. This is the block that decides whether the loop helps you or just spends your money.

Stack these together and you get what serious teams now run at scale. Dozens of loops, each owning one narrow job, running side by side while everyone sleeps. One engineer used a fleet loop like this to rewrite an entire codebase from one language to another in about six days, work that would have taken close to a year by hand.

![Image](https://pbs.twimg.com/media/HNRVPRiXYAA6RMl?format=jpg&name=large)

## Where loops fail silently

Loops do not crash. They bill you in silence. Two failure modes worth naming, both of which get worse as the loop gets better, not easier.

The first is the Ralph Wiggum loop. Engineer Geoffrey Huntley documented it. The agent decides it is done too early, emits the completion signal on a half-finished job, and the loop exits satisfied. Without a hard objective gate, the loop keeps running the next night, keeps spending, keeps producing work nobody will accept.

The fix is not a smarter agent. It is a dumber gate. A test that passes or fails. A build that compiles or does not. Something with no opinion.

The second is subtler. Comprehension debt. The faster the loop ships code you did not write, the larger the gap between what your repo contains and what you actually understand. A smooth-running loop charges compound interest on that gap. The day you have to debug a system nobody on the team has read costs more than the tokens ever did.

Cognitive surrender comes with it. When the loop runs itself, it is tempting to stop forming an opinion and accept whatever comes back. Designing the loop is the cure when you do it with judgment. It is the accelerant when you do it to avoid thinking. Same action, opposite outcome.

Two people can build the exact same loop and end up in opposite places. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. The loop does not know the difference. You do.

![Image](https://pbs.twimg.com/media/HNRVE03WsAI5Bg7?format=jpg&name=large)

## Start with one loop, not ten

The mistake everyone makes is trying to build the whole system on day one. Ten loops, a dashboard, a fleet. It collapses by the weekend because you cannot tell which loop did what.

Start with one. Pick the most annoying recurring task you have, the thing you check every morning out of habit, and turn that single job into a loop. Let it run for a few days. Watch where it overreaches. Watch where it misses. Tighten. Then add the second one.

The order matters more than the tools. Get one manual run reliable first, not fast, reliable. Turn that run into a claude-md skill. Wrap the skill in a loop with an objective gate and a hard stop condition. And then, only then, put it on a schedule. Skipping ahead, scheduling something you have not made reliable by hand, is exactly how loops blow up while you sleep.

The metric that decides if the loop is working is not tokens spent or tasks attempted or PRs opened. It is cost per accepted change. If your accepted-change rate is below 50 percent, you are doing the review work the loop was meant to remove, and the loop is losing.

Karpathy stopped writing training code. Cherny stopped prompting. Neither of them stopped thinking. If you take one thing from this, take that. The loop is a system that does the boring 95 percent while you keep your full attention on the 5 percent that actually carries risk.

You are paying for a fleet of agents and using one chat window.

**Follow me and subscribe to my Telegram channel:** [https://t.me/+75nMf005jRpjMDU1](https://t.me/+75nMf005jRpjMDU1)