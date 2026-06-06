---
title: "Memory isn't a plugin. Skills aren't a plugin. They're the same harness."
source: "https://x.com/tricalt/status/2055876832797581406"
author:
  - "[[@tricalt]]"
published: 2026-05-17
created: 2026-05-21
description: "Memory APIs are not a viable product category, and skill systems are just markdown. We've been saying it for a while.@sarahwooders and @hwch..."
tags:
  - "memory"
  - "plugin"
  - "skills"
  - "harness"
---
![Image](https://pbs.twimg.com/media/HIfu7HiawAA1ooX?format=jpg&name=large)

Memory APIs are not a viable product category, and skill systems are just markdown. We've been saying it for a while.

[@sarahwooders](https://x.com/@sarahwooders) and [@hwchase17](https://x.com/@hwchase17) made the case last month that memory isn't a plugin and that it is the harness instead.

I made the same argument earlier, from the other side. We argued in a post that got 1.7M views that [skills aren't static files](https://x.com/tricalt/status/2032179887277060476). Skills degrade silently in dynamic environments. They need a loop — Observe → Inspect → Amend → Evaluate.

Both arguments are in essence about the same harness. A world model.

## Treat skills and memory as the same harness

A world model is whatever the agent is aware of and what it uses to predict the next action it should take. In an agent harness, it is a broad state of all things you touch: the codebase layout, the tool schemas, the file system, the last 20 turns of conversation and the user's preferences.

The world model is the entire aggregate of context that the harness loads to decide the next step.

You can look at memory as a broad harness and skill as a specific one.

## Is skill a subset of memory?

Skills are the part that records what to do. A SKILL.md is a procedure-level claim: "to do task T, run steps X, Y, Z."

Skills extend memory with a practical ability to do N tasks. Skills are a compressed procedure. It says "the world has responded to X, Y, Z by producing T in the past, and probably will again."

Memory observes the world while skills codifies it into a rule.

We've extended cognee to store skills and memory in the same store. Self-improvement runtime and agentic retriever share the same graph nodes.

## How Cognee handles it?

cognee.remember("skills/") now lets you ingest skills with one line.

Inside Cognee a SkillChangeEvent emits memory events when skill changes. The skill is a memory node that evolves, is traceable, and controllable.

Skills improve by reading their memory. Memory improves by amending the skills attached to it. There's no clean line between them because there should not be one.

We have recently organized a hackathon where users built 21 LLM Knowledge Wikis in 3 hours using Cognee and Redis as session store!

And they did so because improving skills and memory is trivial in our new API:

```python
proposal_result = await cognee.remember(
        SkillRunEntry(
            selected_skill_id=skill_to_improve,
            task_text="Review the current skiill,
            result_summary="Review missed boundary bug.",
            success_score=score,
            feedback=-1.0 if score < 0.7 else 1.0,
        ),
        dataset_name=DATASET,
        session_id=SESSION,
        skill_improvement={
            "skill_name": skill_to_improve,
            "apply": False,
            "score_threshold": 0.9,
        },
    )
```

![Image](https://pbs.twimg.com/media/HIfvVw4bkAAUfCy?format=jpg&name=large)

How self-improvement works for Skills added to Cognee

## Conclusion

Every world model outside board games is permanently misspecified. The harness's job isn't to fix the schema. It's to run a controller on top of one that's wrong by construction. Cognee is that controller, and skill self-improvement is the first step.

It doesn't matter if you use a memory api, skills, or an agent md file. Even compaction strategies are part of the same play.

It is the same world model.

The harness that wins treats memory and skills as one comprehensive world model from the start.

Imho, if your memory system can't route a skill, it's not memory, let alone a world model.

Try it out yourself, Cognee is [open-source](https://github.com/topoteretes/cognee)