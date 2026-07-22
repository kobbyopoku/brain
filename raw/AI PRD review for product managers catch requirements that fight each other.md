---
title: "AI PRD review for product managers: catch requirements that fight each other"
source: "https://x.com/nurijanian/status/2076626469632254460"
author:
  - "[[@nurijanian]]"
published: 2026-07-13
created: 2026-07-21
description: "I've seen AI give PMs a PRD that reads clean while the requirements fight each other on the page.That danger is easy to miss because the doc..."
tags:
  - "clippings"
  - "product-management"
  - "prompts"
---
![Image](https://pbs.twimg.com/media/HNqgB91bMAAwR7D?format=jpg&name=large)

I've seen AI give PMs a PRD that reads clean while the requirements fight each other on the page.

That danger is easy to miss because the doc looks orderly, the headings are right, and the acceptance criteria sound plausible. Then Requirement 3 says approvals are final, Requirement 8 says admins can edit approvals after submission, and Requirement 12 says each approval change needs a complete audit trail.

Each line sounds reasonable alone. Together, they describe a product nobody can build.

That is where \`requirements-reconcile\` helps. The skill turns conflicting requirements into one unified list, so the PM can catch contradictions before they become engineering work.

![Image](https://pbs.twimg.com/media/HNGkYgRbkAA4knH?format=png&name=large)

## The failure mode

AI is good at writing requirements that sound plausible one by one. It can keep the tone consistent, fill empty sections, and make every bullet sound like it belongs in a spec.

It is weaker at holding one product model across the whole document unless you force it to check the requirements against each other.

That is why AI-generated PRDs need a contradiction pass before a polish pass.

A grammar pass asks whether the PRD reads well.

A contradiction pass asks whether the requirements can be true at the same time.

Those jobs look similar only after the doc already sounds clean.

## The audit

In the audit, generated requirements become claims the product model has to reconcile before anyone touches the wording.

For an admin approval flow, AI might generate requirements like these:

- Approvals are final once submitted.
- Admins can edit an approval after submission.
- Each approval change must create a complete audit trail.
- Users can approve items in bulk.
- Legal must require confirmation before any final action.

Before rewriting the bullets, name the conflict.

\`Final approvals\` conflicts with \`edit after submission\`.

\`Bulk approval\` creates risk for \`confirmation before any final action\`.

\`Complete audit trail\` can coexist with edits, but only if the product model treats edits as new events rather than changes to the original approval.

The PM can now turn the polished contradiction into an explicit decision.

## The reconciled list

A reconciled list keeps every original requirement visible and marks each one as \`in\`, \`out\`, or \`modified\`.

For the same approval flow, the output might look like this:

- \`in\`: Each final approval requires a confirmation step.
- \`modified\`: Admins cannot edit a submitted approval. They can reverse it with a new approval event that leaves the original audit trail intact.
- \`modified\`: Users can bulk approve only before the final confirmation step.
- \`in\`: Each approval, reversal, and bulk action creates an audit event.
- \`out\`: The team removes direct editing of submitted approvals because it contradicts the audit and finality model.

That list does more than a cleaner paragraph. It tells design what the product should do. It tells engineering which invariants to protect. It tells Legal where their requirement landed. It tells the PM which tradeoff the team made.

The list keeps contradictions visible instead of hiding them under nicer wording.

## Why AI makes this more important

Before AI, PMs wrote contradictions slowly. The mess stayed visible because it took time to produce.

With AI, the PRD arrives formatted. A model can produce 20 requirements in 10 seconds. When the draft looks smooth, the PM stops looking for cracks.

The PM creates value by checking whether the requirements can survive contact with each other, not by typing them faster.

AI can help with that too, but only if you give it the right job:

1. Preserve every original requirement.
2. Pair any requirements that clash.
3. Name the product rule behind each clash.
4. Mark each requirement \`in\`, \`out\`, or \`modified\`.
5. Explain the rationale in one sentence.

That turns the model from a requirements generator into a requirements auditor.

## What leaders can check

For heads of product, the reconciled list is a quality signal.

If an AI-assisted PRD has no \`out\`, no \`modified\`, and no named contradiction, the team may not have audited the requirements. They may have accepted the model's confidence as coherence.

A good requirements list shows the cuts by naming the attractive requirements the team removed because they fought the product model. It also names the requirements the team had to reshape before they could survive.

The method gives the PM a way to make trust visible. The model earns trust only when the contradictions have names.

Next time AI writes a PRD, ask for consistency before clarity.

Line the requirements up. Find the clashes. Preserve the original asks. Then write back the unified list as \`in\`, \`out\`, or \`modified\`.

What would it look like if that reconciliation ran on your actual company context, with your product rules and constraints already loaded, before every AI-generated PRD?

## Where this skill lives

![Image](https://pbs.twimg.com/media/HNGl_97bsAA2bCv?format=jpg&name=large)

\`requirements-reconcile\` is one of the 200+ skills inside PM OS, the Product Manager's AI Operating System. It runs in Claude Code, Cowork or Cursor on top of your company context files, so the unified requirements lists come back grounded in your product, your users, and your real constraints, instead of generic PM advice that could have come from any blog post.

You don't have to assemble any of it. PM OS wires \`requirements-reconcile\` into the broader operating layer alongside workflows for strategy, research, decisions, stakeholder work, and measurement.

## If you want the full system, it's here.