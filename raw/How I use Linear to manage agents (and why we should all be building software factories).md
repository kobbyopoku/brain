---
title: "How I use Linear to manage agents (and why we should all be building software factories)"
source: "https://x.com/enginoid/status/2078850177926938666"
author:
  - "[[@enginoid]]"
published: 2026-07-19
created: 2026-07-21
description: "Linear is probably my best-value subscription at the moment. I pay the sole user fee of $12/mo and the company agents have eaten through ~40..."
tags:
  - "clippings"
  - "software-factories"
  - "agent-tooling"
---
![Image](https://pbs.twimg.com/media/HNmL9rWXAAAVo02?format=jpg&name=large)

Linear is probably my best-value subscription at the moment. I pay the sole user fee of $12/mo and the company agents have eaten through ~400 issues in the past month.

I use Linear to organize my tickets and feed them into coding agents to do in parallel. Linear is a central place of coordination and a great interface for me to organize the work at my laptop and on the go.

What I have today is a fairly low-tech and crude prototype compared to how I want it to be, at software factory automation level 5. Unfortunately, it gets the job done well enough that I'm forced to work on my product rather than play software Factorio.

## Tickets are organized into an an outcome hierarchy

When vanilla agents manage tickets, they scatter tickets rather creatively in the backlog, and often use their own cryptic lingo, like "Fix gated-access exception in owned-compute handler."

For my own clarity of what needs to be done (which is the whole point of Linear), I've set them up to maintain a hierarchy of tickets named after outcomes rather than the technical task.

![Image](https://pbs.twimg.com/media/HNeaqRyXsAAa1m5?format=jpg&name=large)

Tasks are organized into a hierarchy of outcomes. (They typically end up containing more technical subtasks as agents start executing.)

Arranging the tickets as a tree means that I can encourage agents to finish trees of epics down to the root, and it gives me a high-level sense of progress.

This is something that I've always found to work well in teams, but works exceptionally with agents because unlike most of us, they are very happy to actually organize the backlog.

**Triage is an inbox for future prompts**

The agents work on 3-5 "workstreams" at a time, that are determined not to change the same code area (by an LLM workflow). To avoid interrupting that process, I report issues into the triage inbox rather than starting new agents when I see issues.

I don't have to think about prioritization for what I put into the triage inbox - I just drop anything I can think of that needs doing. This ticket started out as a screenshot, and later got fleshed out according to the agents' "ticket intake guidelines."

![Image](https://pbs.twimg.com/media/HNecs8xX0AAByf8?format=jpg&name=large)

This ticket started out as just the screenshot that I dropped into triage, and got expanded by the agent into something clearer. The Triage inbox has become a key way for me to drop things that need fixing.

## Formatting tickets for agents

The ticket is the contract between me and the agent, kind of like a plan, but to make them maximally readable to humans, they all have a "Goal", "Why" and "Outcomes" section. This is to help me remember clearly what a ticket is about, and to give the agent a good shot of solving the real need.

Focusing on the target state avoids overly constraining the implementation approach. At the point of defining a ticket, the code is typically not deeply researched, so the exact approach is best left up to the implementing agent. As in human teams, implementer autonomy works great for agents if they have a clear standard to work to.

![Image](https://pbs.twimg.com/media/HNeigUuW0AAL8jI?format=jpg&name=large)

To help the agent, there are two more sections:

- Implementation approach: where we do inject any guidance on implementation approach, usually coming from me.
- Verifications: Created by the ticket-authoring agent under strict guidance about the minimal testing procedure for new features. They generally always include "Automated", "Manual" and "Visual" checks. (I'm planning to replace manual checks with automated ones for repeatability in the future. These checks would depend on a robust computer-use agent.)

An agent will be blocked from closing a task if any of the checklist items are unchecked, to avoid cheating or hasty work. (The agent can, of course, still cheat or remove checkboxes -- but in practice they don't as it requires a higher degree of dishonesty than typical "I'm done" declarations.)

![Image](https://pbs.twimg.com/media/HNeiqfqWMAAGlaL?format=jpg&name=large)

## Organizing work into batches

I've found the best balance by organizing work into batches of 3-5 parallel workstreams. Depending on the day and the size of the work in each batch, these batches can take from 30 minutes to 4+ hours, yielding 2-4 batches in a day.

**Driver: My own quality of life**

An important philosophy of this system is my own quality of life. The batches are unsupervised (and Claude's AskUser hook is blocked – so it doesn't ask a question after 15 minutes and do nothing for 2 hours).

Because agents like to ask you to unblock by taking actions on the computer like logging into a browser, it was important to tell the agents that the agent is unsupervised ("but monitored for quality and safety", in a feeble but low-effort attempt to reduce cheating or sabotage).

This buys me back focus to do deep work and do my reviews and kick-offs in chunks, rather than the exhausting affair of task-switching between agent windows all day.

**How batches work**

To create a batch, I use a a "workstream update" skill, which:

1. Makes sure anything in progress is actually in progress, and makes other work available to pick up.
2. Reads any new tickets that have come in from me or other agents (via triage).
3. Loads up on priorities - focusing on finishing work in progress, looking at steer from me and weekly goals, and seeing if anything new is urgent.
4. Proposes 4-5 agent prompts that I paste into the agents.

A workstream update is essentially a document that starts with high level context...

![Image](https://pbs.twimg.com/media/HNef7IUXUAA4fAj?format=jpg&name=large)

...and contains 3-5 segments of tasks assigned to agents. The agent that does the workstream update is prompted to make each section nonoverlapping in terms of area of the code, but to assign workstreams to agents that meaningfully advance a current goal.

![Image](https://pbs.twimg.com/media/HNegV38XsAAXXO3?format=jpg&name=large)

When I said the system was low-tech earlier, I meant it: I paste each workstram prompt into Codex, Claude Code, Cursor or Antigravity.

**Requiring work to be complete**

In the early iterations, I had a lot of issues with different agents fail to complete the assigned work. I want the agent to fully close the ticket (which includes merging the change), but agent would stop at various points before the full job was done: before committing code, before creating a PR, before marking it as ready to review, before it passes tests and reviews, before it's successfully merged, and before checking all checkboxes in the ticket.

To overcome this, I've gone to great lengths to make the agents actually finish work. This is a messier problem when you work with multiple harnesses and don't have a simple API to invoke the agent, so you have to rely on hooks rather than a typical workflow approach.

At this point, agents typically do finish their work. If they don't, they have to mark the ticket as either "Blocked" and raise a formal escalation for human help according to a human escalation standard (see below.)

Through prompts and hooks, the agent is required to:

- Register an "agent session", tied to the tickets.
- Mark the tickets in progress.
- Work on the tickets.
- Submit PRs and ensure they are merged and deployed.
- Ensure all code is pushed and in a PR.
- Tick off all checkboxes in each ticket.
- Ensure all the tickets are marked as closed or blocked.
- Upload a transcript of the session, for root cause analysis.
- Mark the agent session as complete. (If the session was interactive – eg. if I asked some questions about the codebase that were not related to a ticket, the agent can ask for a "waiver" to follow formal closeout that would ordinarily require tickets that are verified as done.)

The hooks were essential to ensure that the agents were finishing their tasks. There are occasional false positives where an agent blocks on an issue that a human is not needed for – for example, when our MCP server doesn't support a tool that they need but they actually have the ability to just deploy a new tool to the MCP server. But for the most part, they're good about finishing.

## Human escalations

Much of my work now is around access control - creating accounts and moving secrets from hither to thither.

Agents are notoriously bad at assigning work to humans, because they have the curse of knowledge – they generally expect that you have exactly the same mental state, and that you know exactly what they mean by "needing this to deploy the component quality ratchet."

They also love giving you tasks that take fifteen minutes rather than two, by saying things like "add a GitHub app" rather than giving the exact instructions and configuration.

To combat this, I've prompted them to be careful in their phrasing of human escalations and assume that the human is very busy, really not in the headspace. The human knows very little about the code, the problem being solved, or why they are even there. I also ask them to go out of their way to make it easy for the human to do the work quickly without much thinking (eg. by writing scripts.)

Lastly, I ask them to ensure that all other unblocked work proceeds optimistically, so that there is a minimal amount of work to complete the task when the human escalation is resolved.

![Image](https://pbs.twimg.com/media/HNenT8KXkAAIzRi?format=jpg&name=large)

## Linear + agent quirks

In general, Linear's MCP server works really well, but I did need to make three minor adjustments to the interface with Linear. Those were just enough to replace their MCP server with our own:

- **Support for updating ticket summaries through diffs.** Agents had a tendency to post their updates through keeping the ticket description correct. This is generally good behavior, but they would tend to completely override the verification criteria and other nice details of the original ticket, which is important for the reviewer agent. So I banned direct edits but gave the LLMs a tool to send diffs for patches.
- **Giving agents their own identity, rather than mine.** The Linear MCP server uses your personal OAuth by default. I had to quickly switch to giving the agents a different MCP server with an app-based authentication and identity. I wasn't getting any notifications when agents assigned tasks to me, as they were operating as me, and a lot of the time I was confused about whether the agent had closed a task or I had.
- **Minor ergonomics.** The \`get\_issue\` command that comes through the vanilla MCP server wouldn't always return enough context for the agents, including comments and subtasks, so this ensures that they have the full picture without having to "remember" to ask for everything.

## How it's working

This system works really well and was an exceptional improvement over my previous attempts to think hard to assign tickets work, and monitor completions reactively.

Linear is a joy to use for task management and is especially wonderful on the go. The agents have done a tremendous amount of work through this system and they seem to benefit from the context they can get from the ticket templates.

Because the format is human-optimized and outcome-focused, I also have an easy time verifying the tickets are asking for the right things. Overall, my attention scales a lot better than it did before I implemented this system.

I was able to prototype this quickly just using desktop agent harnesses, which was quick but also a constraint due to how much cheaper subscription tokens are. I'll probably keep this setup for some time, because it's practical and because for better or for worse, software factories are not my main business.

The hacks that I use to manage the state machine from a ticket to a completed code need to be replaced with a proper state machine, so the system can be more easily measured (eg. for completion rate and defect rate), progressed (when things get stuck) and continually improved.

Most of the things I want to improve require breaking out of the restrictions of using a harness:

- **Replacing hooks with workflows.** The hacks I've put in place to manage "agent sessions" are deeply disturbing. It tracks what agents are active, but also allows root-cause analysis into agents that are slow or produce bad results. But this heinous implementation requires the agent to go rummaging for transcripts to upload, in locations that depend on the harness. If I wasn't dependent on subscriptions for economics, it would be much more pleasant to just invoke the agents via API from the linear tickets and manage agent session postconditions through a proper workflow representation.
- **Workflows with measurement.** I'm a big fan of process management, continuous improvement and the Toyota Production System. All of those juicy ideas apply remarkably well to software factories -- all that's left is capturing metrics (like completion rate, defect rate and variance) and starting to systematically improve the low-hanging fruit.
- **Evals.** Since much of my work is around evals and I depend very strongly on coding agents, it feels ironic that I don't have evals for my own coding agents. It would be extremely useful to be able to repeat the same task under different guidance, and run the whole suite at least weekly. But they're a little annoying to set up when you're using multiple harnesses, so I haven't bothered. It feels like I'm standardizing around OpenAI, which conveniently doesn't consider it a ToS violation, so this could be coming soon and is probably the low-hanging fruit for me now.

## Software factories are the future, and now's the time to get them right

I'm interested in hearing from more people working on software factories, and so I want to make the case for why software engineers should be enthusiastically working on them.

There's considerable divide, and maybe awkward hesitation, on whether we should be building towards software factories – systems that generate production-quality software with humans working at their highest leverage.

Whether they're "real" or not, in the same way there was divide whether agents would be widely used for coding 2-3 years ago. The companies who best acted on the belief that LLMs would write good code created extreme value in the software world – and have been acquired in amounts ranging from $2.5 to $60 billion. This suggests that it can be valuable to be optimistic, and plan for success when the signs are there.

The biggest symptom that there is a divide today is that many people are now discussing whether it's a worthwhile goal to automate code review, or whether engineers should read every PR. "Do you look at the code?" is a question I get asked a lot by other engineers who are also trying to figure out the right balance.

I'm surprised by the hesitation that we have about software factories being the future. To me, it's obvious that it is worth automating everything that is possible to automate, as long as that automation can successfully deliver production-grade software.

The signs that it's possible are clearer than ever, and while we're probably going to see industry-wide tools and patterns emerge, there are steps that all teams can be taking to start taking advantage of automation today and building towards the metaphorical puck.

To make that automation work well for software engineers as professionals and build workflows that allow us to do energizing work, we should take an active part in shaping it rather than let it happen to us. Do we want to spend all our time reviewing PRs and approving agent actions, or do we want to design systems that allow us deep work and creativity? These world are equally possible and depend largely on the effort we put into making software factories human-friendly.

Software factories are worthwhile in the same way coding agents are worthwhile – the benefits will be too good to ignore, and unless you build software as a hobby, you will will have to go there for competitive reasons whether you like the idea of automating software or not.

The most advanced companies today are working on the review/verification bottleneck. Next comes the long-horizon bottleneck. Then there will be token cost bottleneck. Then perhaps the specification bottleneck. At some point, the user validation bottleneck. It feels like the fundamental pieces are here already, and that it's about composition and economics. We are already in an industrial revolution.

So the question isn't whether, but how. In the past we used waterfall, scrum, extreme programming (and many other buzzwords) to organize these activities into a system that reliably produced software, hopefully on schedule and under budget.

These methodologies made sense, because human development of software takes place in a complex adaptive network rather than through controllable processes. Whenever we tried to introduce heavyweight processes, we discovered that it just doesn't work well with human cognition or motivation to deliver a 30 page document before building anything.

My personal bet is that outside of the human parts, most of the mechanics of delivering code seem better modelled than an industrial process: something that is rigorously defined and dependent on standardization, measurement, and process control.

The role of humans will be:

- Understanding what needs building.
- Instructing building to happen in the right way, typically out of band from the specific task. (At the "factory" level.)
- At the task execution level, lend creativity, intuition and foresight into research, sensemaking, and optimization tasks.
- Evaluating whether delivered software meets professional and human desirability standards.
- Building, maintaining and improving the factories the make software.

The most exciting times in technology have always been when lots of people are trying to solve the same problem and everyone brings their own insight and experiences – this was certainly the case in the evolution of the interactive web (from jQuery to React) and web applications (from Rails to Django and FastAPI). Everyone was sharing what was working, and it was a really fun time.

It'd be great to expedite how much we talk about software factories by getting the awkward bit out of the way: acknowledging that they are definitely happening.

I'm curious to see work from people who are trying to build software factories and to hear about what's working and what isn't, so we can all figure out and build the best future of software together.