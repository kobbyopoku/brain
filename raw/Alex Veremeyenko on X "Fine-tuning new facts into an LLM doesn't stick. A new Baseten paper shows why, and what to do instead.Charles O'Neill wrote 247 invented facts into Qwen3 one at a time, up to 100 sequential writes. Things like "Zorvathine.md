---
title: "Alex Veremeyenko on X: \"Fine-tuning new facts into an LLM doesn't stick. A new Baseten paper shows why, and what to do instead.Charles O'Neill wrote 247 invented facts into Qwen3 one at a time, up to 100 sequential writes. Things like \"Zorvathine is a metal that melts when cooled below −10 °C\", facts https://t.co/Qn6Lp6fpSG\""
source: "https://x.com/alex_verem/status/2079269973030298064"
author:
published: 2026-07-20
created: 2026-07-22
description:
tags:
  - "clippings"
  - "llm-research"
  - "fine-tuning"
---
## Post

## Conversation[Alex Veremeyenko](https://x.com/alex_verem)[@alex\_verem](https://x.com/alex_verem)

Fine-tuning new facts into an LLM doesn't stick. A new Baseten paper shows why, and what to do instead. Charles O'Neill wrote 247 invented facts into Qwen3 one at a time, up to 100 sequential writes. Things like "Zorvathine is a metal that melts when cooled below −10 °C", facts the model cannot know in advance. First finding is interesting. How you write the fact decides what you get. Train on the bare statement, and the model recites at 97% but cannot use the fact. Train on 24 varied restatements, and the recitation-to-use gap shrinks from 27.4 points to 5.4, without the training data ever stating a conclusion. Then the forgetting. After 20 later writes, bare-statement facts retain 1% accuracy. Broad-data facts retain 46%. But forgotten facts are not erased. They keep 57–67% of the probability their write added. Under bare-statement training, 70% of wrong answers about a forgotten fact contain the newest fact instead of the one asked about. Asked about the first fact it wrote, the model answers with the twentieth. Composition fails too. Two facts in the weights cannot be used together: 32% accuracy, against 91% with both in the prompt. Asked to state a fact it was trained on, the model retrieves the right content 34% of the time. Paste a forgotten fact back into context and accuracy returns to 77–80%. The author's read: a weight write stores content without an address. Questions reach a fact only by accident of routing, and later writes redirect the route. No fix they tested, including projecting each update away from the measured conflict, kept old facts reachable. If facts must be retrieved on demand, composed, or survive further training, keep them in context.

[![Image](https://pbs.twimg.com/media/HNsNBYxa8AAbLY6?format=png&name=small)](https://x.com/alex_verem/status/2079269973030298064/photo/1)

[View quotes](https://x.com/alex_verem/status/2079269973030298064/quotes)

Post your reply

Turn Claude into 20+ different specialists for marketing & business. Install real expertise, not just prompts. Get my Claude skills bundle[961](https://x.com/alex_verem/status/2079269996983992825/analytics)[Ivana](https://x.com/ivanainai)[@ivanainai](https://x.com/ivanainai)

[Jul 20](https://x.com/ivanainai/status/2079270296935145525)

Going from 97% recall to 1% after 20 writes is brutal.[206](https://x.com/ivanainai/status/2079270296935145525/analytics)

So the researcher basically tried to gaslight an LLM? Must have been fun.

The takeaway isn't that fine tuning is broken. It's that persistent knowledge needs an addressable memory layer.

Quote

Gerard Sans | Axiom

@gerardsans

\> Me: here the jacobian conjecture disproven > Claude: oh my god x.com/gerardsans/sta…

[![Image](https://pbs.twimg.com/media/HNv5NTwXAAA4Luy?format=jpg&name=360x360)](https://x.com/gerardsans/status/2079529665178259917/photo/1)[46](https://x.com/gerardsans/status/2079546214043844612/analytics)