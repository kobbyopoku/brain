---
title: "The AI skill of 2026 that almost nobody is teaching"
source: "https://x.com/rohit4verse/status/2077045458309091680"
author:
  - "[[@rohit4verse]]"
published: 2026-07-14
created: 2026-07-22
description: "I have spent two years building things on top of models I cannot see inside. Every fix I know how to make touches one of two places. I chang..."
tags:
  - "clippings"
  - "ai-careers"
---
![Image](https://pbs.twimg.com/media/HJFeRila0AAU58D?format=jpg&name=large)

I have spent two years building things on top of models I cannot see inside. Every fix I know how to make touches one of two places. I change what goes in, or I grade what comes out. The prompt, the context, the retrieval, the eval, the guardrail. The actual thinking that happens between the input and the output has always been off limits to me, the same way it has been off limits to almost everyone shipping production AI.

One afternoon a feature in our app broke in a way I had not seen before. It summarized a body of expert content and answered questions against it, and it had worked for weeks. Then it started inventing a citation that did not exist in our corpus, with the same confidence it used for the answers that were true. I did what any of us do. I opened the trace. I reread the system prompt. I added a line telling it not to make up sources. The hallucination got rarer. It did not go away. So I added a few-shot example. Then a refusal gate. Then an eval to catch the failure I could no longer reproduce on demand.

It took me too long to notice the obvious thing. Every one of those moves worked on the outside of the model. I was tuning the input and judging the output, and the part in the middle, the place where the model actually decided to fabricate that citation, stayed sealed. I never once looked at what it was doing while it did it. I could not. The tools I knew did not reach in there.

That seal has a name. We call it the black box. And in 2026 it is the first year I can honestly say a normal builder, not a frontier lab researcher, can start to open it.

## The skill nobody is selling you

Pull up any list of AI skills to learn this year. You already know what is on it, because the same five things are on every one of them. Prompt engineering, which everyone now pretends they were never bad at. Context engineering, the slightly more respectable cousin. Retrieval, so your model can read your documents. Agents, so it can take actions. Evals, so you can measure whether any of it worked.

I use all five. I teach some of them. They are real skills and they pay real money.

Notice what they share. Every one of them works on the outside of the model. You arrange better inputs, you wire up better tools around the box, you measure the outputs more carefully. The model itself stays a vendor you negotiate with through a slot in the door. You slide a prompt in, a response slides out, and you get very good at writing notes to pass through the slot.

There is a second skill. It is reading what the model is actually computing, and steering it at the level of its own concepts instead of its words. Operating it from the inside.

I am going to call it the inside-the-box skill, because nobody has given it a clean consumer name yet, and that is part of the point. Almost nobody teaches it. For a long time almost nobody could, because doing it at all meant working inside one of a handful of frontier labs with the people who invented the techniques. The knowledge lived in research papers and internal tooling, not in a Colab you could open on a Saturday.

That changed recently enough that most builders have not caught up. And it did not change because one company opened a slot for you. It changed because the labs that invented these techniques put the tools themselves in the open, on Hugging Face and GitHub, for free. The rest of this is me trying to close that gap, because I think the people who pick this up early get the same kind of head start the prompting crowd got in 2022, except this time the advantage is harder to copy.

## Why the box was sealed in the first place

To understand why the box stayed shut, you have to see what is actually in there.

The reflexive assumption is that the black box is about secrecy. The weights are hidden, the lab will not tell us, that sort of thing. That is wrong, and getting it wrong is why people dismiss this whole field. You can print every weight in an open model. You can capture every activation as it fires on a given input. None of it is hidden. I can dump the entire internal state of an open-source model to my disk tonight.

The problem is not access. The problem is that the meaning is tangled.

You would hope that somewhere in the network there is a neuron for "formal tone," and another for "this is Python code," and another for "the user is asking about the law." If that were true, interpreting a model would be like reading a labeled circuit board. It is not true. A single neuron fires for the Golden Gate Bridge, and for a legal disclaimer, and for the opening of a function, all at once, with no clean separation. The concepts are smeared across the neurons, and each neuron carries pieces of many concepts.

The field calls this superposition, and the neurons polysemantic, meaning many-meaninged. The model packs far more concepts than it has neurons by letting them overlap and share space. It is an efficient way to store knowledge and a terrible way to make that knowledge legible. Staring at the raw activations tells you almost nothing, the same way staring at a slice of wet brain tells you nothing about the memory it holds. The information is right there. You just cannot read it.

Now layer on the part that should worry anyone betting their product on these systems. Scaling made it worse. Every time we made models bigger and more capable, we also made them less legible, because more capability meant more concepts crammed into the same kind of tangled, overlapping representation. We have been racing in two directions at once. The models got smarter and our ability to see what they were thinking got further behind. We did not seal the box on purpose. We grew a thing whose inside we never designed and then acted surprised that we could not read it.

That is the honest reason debugging an LLM feels like superstition. You are not debugging. You are doing experiments on a system whose internals you have agreed, by default, not to look at.

## How you actually look inside

The thing that finally pried it open is almost funny in its simplicity.

If the problem is that meaning is smeared across neurons, then you train a second, smaller model whose only job is to un-smear it. That model is called a sparse autoencoder, an SAE, and it sits on one layer of the big model like a probe. You feed it the tangled activation vector from that layer and it pulls it apart into a much larger set of what we call features, where each feature is tuned to mean, as close as we can get, exactly one human-readable thing.

So instead of "neuron 4,201 is at 0.7," which means nothing, you get a list. The formal-tone feature is active. The refusal feature is active. The joke-setup feature is active. The reptile feature, weirdly, is also a little active, and now you get to wonder why. You have gone from a wall of numbers to a list of concepts the model is actually using right now.

The first time you see that list, prompting starts to feel primitive.

Here is what it looks like in code. It uses SAELens, an open-source library for loading and analyzing these autoencoders, together with one of the SAEs from Gemma Scope. Gemma Scope is DeepMind's open release of sparse autoencoders trained on every layer of its Gemma 2 models, published free on Hugging Face with a Colab to get you started. Both run on a single GPU. You run some text through the model, catch the activations at one layer, and ask the autoencoder which concepts were firing while it read.

```python
import torch
from transformer_lens import HookedTransformer
from sae_lens import SAE

# Gemma 2 (2B) plus one of DeepMind's open Gemma Scope autoencoders. Both free.
model = HookedTransformer.from_pretrained("google/gemma-2-2b")
sae, cfg, sparsity = SAE.from_pretrained(
    release="gemma-scope-2b-pt-res-canonical",
    sae_id="layer_20/width_16k/canonical",
)

prompt = "Write a formal complaint to my landlord about the leak."
_, cache = model.run_with_cache(prompt, prepend_bos=True)
acts = cache["blocks.20.hook_resid_post"]      # tangled residual stream at layer 20

features = sae.encode(acts)                     # smeared vector -> named concepts
top = features[0, -1].topk(10)                  # concepts firing on the last token
for value, idx in zip(top.values, top.indices):
    print(round(value.item(), 2), f"feature #{idx.item()}")

# Example output, after you look each index up in a feature dashboard:
# 9.0   Setup phrases in jokes and narratives
# 7.0   Formal definition or description of a concept
# 6.0   Reptiles and reptilian characteristics
```

That output replaces something. Today, when an agent goes off the rails, my debugging loop is to reread the transcript and guess. I look at the words it produced and I construct a story about why it produced them. That story is a guess dressed up as analysis. This is a debugger for behavior. It does not show me the words the model said, it shows me the concepts it was running while it said them. When the model fabricated that citation, I would not have to invent a theory about why. I could look at which features were lit and find the one driving it.

If you do not have a GPU, you do not even have to run the model yourself. Neuronpedia, an open-source interpretability platform, hosts these same autoencoders behind a free API and a browsable dashboard for every feature, so you can ask the same question over HTTP and get back named concepts with human-written labels attached.

```python
import requests

# Illustrative; exact endpoint and fields are in Neuronpedia's API docs.
# No GPU: ask a hosted SAE which features a prompt lights up.
resp = requests.post(
    "https://www.neuronpedia.org/api/activation/new",
    headers={"x-api-key": NEURONPEDIA_API_KEY},
    json={
        "model": "gemma-2-2b",
        "source": "20-gemmascope-res-16k",
        "text": "Write a formal complaint to my landlord about the leak.",
    },
)
for feat in resp.json()["activations"][:10]:
    print(feat["index"], round(feat["maxValue"], 2), feat["description"])
```

Either way, that is a fundamentally different relationship to the system. I stop interrogating the output like a detective and start reading the internals like a profiler. Anyone who has moved from print statements to a real debugger knows the size of that jump. The same jump now reaches the model's internals, and it reaches them through tools you can download tonight.

## From reading to steering

Reading the concepts is the first half. The half that actually changes how you build is that you can also change them.

Once a feature has a name and a value, you can set that value to something else and run the rest of the model forward from there. Every SAE feature has a direction it points in the model's activation space, and turning the feature up means adding a multiple of that direction back into the residual stream as the model computes. Turn the formal-tone feature up and the model writes like a lawyer without you ever typing the word "formal." Turn a refusal feature down and you have found a jailbreak, which, read the other way, is exactly how you learn to harden against one. Find the feature that tracks making things up and clamp it, and the fabrications drop. This is called feature steering, and I want to be precise about why it is not just a fancy prompt.

```python
# You found this index by inspecting which feature lights up on formal text.
FORMAL = 12345
direction = sae.W_dec[FORMAL]          # that concept's direction in activation space

def steer(resid, hook):
    return resid + 8.0 * direction     # add the concept back in, scaled

out = model.generate(
    "Write a quick note to my landlord about the leak.",
    fwd_hooks=[("blocks.20.hook_resid_post", steer)],
    max_new_tokens=120,
)
print(out)
```

One thing is missing from that code. Nowhere in there did I write "be formal" or "use a professional tone." I did not ask the model for anything. I reached past the prompt, found the model's own internal concept of formality, and turned it up. A prompt is a request you hope the model honors. Steering changes the computation that produces the answer. That is the whole distance between asking and operating, and the demos do not prepare you for how different it feels in your hands.

If installing an SAE feels like a lot for a first try, there is an even simpler on-ramp that has been open for a couple of years now, called representation engineering, or control vectors. Instead of an autoencoder, you build a single steering direction yourself from a handful of contrasting examples, formal versus casual, honest versus evasive, and add that direction at inference time. Libraries like repeng do it in a few lines, and it is the cheapest way to feel the effect before you go deeper.

```python
from repeng import ControlVector, ControlModel

model = ControlModel(base_model, layer_ids=list(range(-5, -18, -1)))

# Build one steering direction from contrasting examples. No SAE required.
formal = ControlVector.train(
    model, tokenizer,
    dataset=make_contrast_pairs(positive="formal, professional",
                                negative="casual, slangy"),
)

model.set_control(formal, coeff=1.5)   # dial the direction up (negative suppresses)
print(generate(model, "Write a note to my landlord about the leak."))
```

It gets better, because you can make the edits conditional on what the model is already doing. This is the part where it stopped feeling like a toy to me and started feeling like engineering. Inside the same forward hook, you read which concepts are live right now and only intervene when a condition holds.

```python
PIRATE, HUMOR = 4201, 8891             # feature indices found by inspection

def gated_steer(resid, hook):
    z = sae.encode(resid)              # which concepts are live at this moment?
    pirate_on = (z[..., PIRATE] > 0.75).unsqueeze(-1)

    # Only amplify humor *when* the model is already in pirate mode:
    resid = resid + 0.7 * pirate_on * sae.W_dec[HUMOR]

    # Or hard-stop generation when an unwanted concept runs away:
    if z[..., PIRATE].max() > 0.9:
        raise StopGeneration
    return resid
```

That is an if statement over the model's mind. You are writing control flow against concepts instead of tokens, and the condition is not a keyword in the text, it is the activation of an internal feature. This is the line that makes "build models the way you write software" feel literal instead of like a tagline somebody put on a landing page. And if you would rather not host any of this, Neuronpedia exposes a steering endpoint too, so you can raise or lower a named feature on a hosted model with a single call and a strength multiplier, no GPU in the loop.

Think about which of your own recurring failures this lets you attack directly. A tone that drifts wrong in long conversations, where today you keep reinjecting instructions. A model that refuses things it should not, or accepts things it should refuse. One specific hallucination that shows up in one specific situation. A jailbreak you can now study from the inside because you can watch the refusal feature get suppressed and decide to pin it back up. None of these get a fourteenth line in the system prompt. They get a dial.

## Proof this is not a toy

If this sounds academic, look at what it already produced.

Start with the failure that started this piece for me, hallucination. Researchers behind a method called Inference-Time Intervention, published at NeurIPS in 2023, showed you can attack it from the inside. They trained cheap probes to find the directions inside a model that separate its truthful answers from its false ones, then, at generation time, nudged the activations along the truthful direction. No fine-tuning, no expensive judge model grading every answer, just a direction and a dial. On the TruthfulQA benchmark it sharply improved how often the model gave truthful and informative answers, by some measures roughly doubling the score, from an intervention that costs almost nothing to run.

```python
# Inference-Time Intervention (Li et al., NeurIPS 2023), as an idea.
# Find the "truthful" direction with a probe, then shift activations toward it.
truth_dirs = fit_truth_probes(model, truthful_vs_false_pairs)   # per-head directions

def toward_truth(head_out, hook):
    return head_out + alpha * truth_dirs[hook.layer]            # shift, don't retrain

# The judge is not another model grading from the outside.
# The signal is a direction living inside the model itself.
```

That is the shape of the whole idea. The expensive way to fight a bad behavior is to stand outside the box with a grader and pay for a verdict on every output. The cheap way is to read a signal that already lives inside the box and act on it directly. The same move works whether the signal is a probe direction or a single SAE feature.

Then there is scale, which is where most people expect interpretability to fall over. The standard objection is that this might work on a toy model but will never survive a real one. That objection is getting hard to say with a straight face, because three different frontier labs have already run it at production scale and published the result. OpenAI decomposed GPT-4's internals into roughly 16 million features with a sparse autoencoder and open-sourced the training code. Anthropic did it to Claude 3 Sonnet, a model people actually ship against, and found millions of features they could steer, including the now-famous one for the Golden Gate Bridge. And DeepMind's Gemma Scope did not pick one layer, it trained autoencoders across every layer and sublayer of Gemma 2 and gave the whole suite away, with a second, larger release following at the end of 2025. The "it will not scale" line has three counterexamples you can download.

And then the part I cannot stop thinking about, because it stops being software and becomes science.

Years before any of this was a product, a team of DeepMind researchers reverse-engineered AlphaZero, the chess engine that taught itself the game, and published it in PNAS. They pulled out concepts the machine had learned that no human had ever named. In follow-up work, also in PNAS, they went further and taught those machine-discovered concepts back to world-class grandmasters, who measurably improved their play. An AI learned something true about chess that humans had missed, and researchers extracted it and handed it back.

Now point that same kind of toolkit at biology. In a project called InterPLM, researchers trained sparse autoencoders on a protein language model, the kind of model that learns the grammar of proteins the way an LLM learns the grammar of English, and found features that lined up with real biological structure, binding sites and structural motifs and functional families, concepts nobody had labeled for it. The work was published in Nature Methods, and the whole pipeline is open on GitHub. It is one of the clearest cases I know of someone reverse-engineering a foundation model and getting a genuine natural-science finding out the other side.

The technique that lets me turn down a hallucination in my app is the same technique that pulled new chess knowledge out of a machine and real biology out of a protein model. A toy does not do that.

## The tools just landed in your hands

This is why the year in the title is 2026 and not some hand-wavy "the future." The capability crossed from frontier-lab secret to something you can touch, and unlike the last wave of AI tooling, the thing you touch is not one company's hosted slot. It is a stack of open pieces, and you can assemble as much or as little of it as you want.

The interpreter models are open and free. Gemma Scope puts DeepMind's sparse autoencoders for Gemma 2 on Hugging Face, trained across every layer, with a Colab notebook to start. OpenAI open-sourced its SAE training code. Between them you have interpreters for real models sitting in public, no waitlist.

The libraries to drive them are open too. SAELens loads pretrained autoencoders and gives you the encode-and-decode loop, and it leans on TransformerLens, the workhorse library for reaching into a model's activations with hooks, the thing that made every steering example above a few lines instead of a research project.

The place to explore what you find is open. Neuronpedia, now fully open-source, is a hosted dashboard and free API over these autoencoders. Every feature has a page showing what activates it, you can steer features from the browser, and it even hosts the circuit-tracing tooling that labs use to follow a model's reasoning step by step. It replaces the internal, proprietary dashboards that used to live inside the labs.

And when the model is too big to fit on your hardware, that is handled in the open as well. NNsight, together with the National Deep Inference Fabric, lets you write the exact same read-and-steer code against a model you could never load locally and run it remotely, on shared research infrastructure, for free. You get to reach inside a seventy-billion-parameter model from a laptop.

```python
from nnsight import LanguageModel

# Run the same read/steer loop on a model too big for your GPU.
# NDIF executes it remotely on the open weights, for free.
llm = LanguageModel("meta-llama/Llama-3.3-70B-Instruct")

with llm.trace("The Golden Gate Bridge is", remote=True):
    resid = llm.model.layers[40].output[0]
    resid += 8.0 * bridge_direction          # steer inside a 70B model from a laptop
    prediction = llm.lm_head.output.argmax(dim=-1).save()
```

Strip all the tooling away and the core loop is small enough to hold in your head. Grab a layer's activations, encode them into named features, read or edit them, decode back, continue the forward pass. That is the whole skill.

```python
# The whole thing, against DeepMind's open Gemma Scope SAE:
acts     = cache["blocks.20.hook_resid_post"]   # smeared activations
features = sae.encode(acts)                      # -> named concepts (read)
features[..., FORMALITY] += 6.0                  # turn one concept up (edit)
steered  = sae.decode(features)                  # write it back (decode)
# ...then keep running the model forward from \`steered\`.
```

The barrier to starting used to be a job offer from a frontier lab. Now it is a weekend and a Hugging Face download.

## The honest part

I am not going to sell you a finished technology, because it is not one.

Interpretability is young, and it breaks in ways you should know about before you stake anything important on it. Superposition does not politely confine itself to one layer, it spreads across layers, and the clean single-layer SAE picture gets muddier the harder you look. Some features look perfectly steerable in a demo and then do not behave when you lean on them, because the thing the SAE labeled was not as clean a concept as the label suggested. And models self-repair. You suppress a feature, and the network routes around your edit downstream and heals the behavior you were trying to remove. This is a documented effect, sometimes called the Hydra effect, where ablating one component causes others to compensate as if the first were never gone, and it means a steering result that looks solid can quietly fail in production. Even the dictionary-of-features view that everything above rests on is being pushed on by the researchers who built it, toward understanding the geometry of the space those concepts live in and steering along the shape of that space rather than yanking one dial. That is a sign of a healthy young science, not a finished SDK, and you should treat it that way.

Then there is a debate I find more interesting than any of the technical caveats, and I want to lay it out fairly because it is unresolved.

The tempting next move, once you can read an internal signal for a bad behavior, is to use it during training. Turn your understanding of the internals into a reward, and optimize the model against it directly. It works, and some safety researchers think it is close to a forbidden move. The argument is sharp and worth sitting with. Your interpretability tools are valuable precisely because they are an honest window into the model. The moment you start optimizing the model against that window, you create pressure for the model to look good through the window while doing whatever it wants behind it. You can blind your own monitor by training against it. This is exactly the worry a group of researchers across several labs raised about chain-of-thought monitoring in 2025, and it is what one widely-read essay calls "the most forbidden technique." Once you have optimized against your window, you no longer know whether it is showing you the truth or showing you what the optimization taught it to show.

There is a partial defense, and it is worth knowing because it shapes how careful teams do this. You read the signal from a frozen reference copy of the model, not from the student being trained, and you do not let gradients flow back through the probe, so the student is not directly optimizing to fool it.

python

\# Using an internal probe as a training signal — and the safeguard that # makes it less dangerous: read the probe off a FROZEN reference model, # not the student, so the student cannot directly learn to fool it. for batch in rollouts: answer = policy.generate(batch.prompt) reward = truth\_probe(frozen\_ref.activations(answer)) # cheap internal signal policy.update(answer, reward)

It helps. It does not fully settle the objection, because pressure to look good through the window can leak in through subtler paths. I am not going to resolve this for you, because I do not think it is resolved. I think both sides are pointing at something real. What I will say is that knowing this tension exists is the difference between understanding the field and reposting a press release about it. If someone is selling you interpretability with no caveats, they have not read the disagreement.

## So here is the part that actually matters for you and me

Stop thinking of this as a research topic and start thinking of it as a layer in your stack.

You already have a mental model of the agent stack even if you have never drawn it. There are the weights, frozen, that you rent. There is the context you assemble each turn. There is the harness around it, the prompts and tools and retrieval and memory. There is the infrastructure underneath. Interpretability and steering slot in as a new layer, the one that sits below the prompt and right next to memory and tools, the layer where you operate on the representation instead of the text. For two years I have been doing all my engineering in the harness layer and pretending the model layer was a fixed input. It is not fixed anymore.

The near future is concrete, and it arrives sooner than most teams expect. You debug an agent by inspecting which features fired during the bad turn, instead of rereading the transcript and constructing a theory. You fix a drifting tone or a recurring fabrication by finding the one feature behind it and steering it, instead of appending the fourteenth instruction to a system prompt that nobody can read anymore. You catch a class of jailbreak by watching the refusal feature get suppressed in real time and pinning it back up. Reliability, the thing that has felt like an art for as long as I have done this, starts to feel like engineering, because for the first time you have an observation system and a control system pointed at the same object.

That is the real promise, and it is worth stating plainly. To control any process you need to observe it and to act on it, and interpretability gives you both at once, because it lets you decompose a model into parts, attach meaning to those parts, and change them. Every engineering discipline was gated by a fundamental science before it could mature. Steam engines ran for decades before thermodynamics explained them, and it was thermodynamics that turned them from craft into engineering. AI is sitting at exactly that inflection point now. We have been running the steam engines for years. The thermodynamics is finally showing up.

The people who ought to know think the curve is bending now, not someday. Anthropic's CEO, Dario Amodei, put out an essay in 2025 titled "The Urgency of Interpretability," arguing this is among the best bets we have for turning black-box networks into understandable, steerable systems, and setting a goal of being able to reliably detect most model problems within a few years. MIT Technology Review named mechanistic interpretability one of its ten breakthrough technologies of 2026. Anthropic, DeepMind, and OpenAI all run public interpretability programs and keep shipping open artifacts from them. None of that makes the science finished. All of it tells you where the serious attention is going.

Two kinds of builders are forming, and the split is quiet enough that most people have not noticed they are on a side. One kind will spend the next few years getting very good at talking to the outside of the box, better prompts, bigger context, cleverer retrieval, and they will do fine, because those skills are real and they are not going away. The other kind is learning to open the box and operate on what is inside. The gap between them is about to widen the way the prompting gap widened in 2022, when a handful of people figured out something the rest of us took a year to catch up on, and by then they were ahead in ways that compounded.

I know which side I want to be on. For two years I tuned the outside of a box and called it engineering. The interesting part was always inside. It is open now, and not just for the labs. The people who learn to read what is in there before everyone else will have an edge the prompt-only crowd will not even see coming, because you cannot see an edge that lives in a layer you have never looked at.

## How to actually start this weekend

You do not need permission and you do not need a budget. Three steps.

Pull one of DeepMind's Gemma Scope autoencoders from Hugging Face and run the SAELens Colab on the model card. Start with Gemma 2 2B and a middle layer if you want it to fit on modest hardware, or skip the GPU entirely and poke at the same features through Neuronpedia in your browser. Just get to the point where you can print a ranked list of the features firing on a prompt. Seeing it once rewires how you think about the model.

Then take one model behavior you actually hate, the tone that goes wrong, the refusal that misfires, a hallucination you can reproduce, and go hunting for the feature behind it. Steer it up and down until the behavior moves. You will fail a few times. That failure is the skill. Finding the dial is most of the work, turning it is the easy part.

Last, read the two pieces that frame the whole thing, Dario Amodei's "The Urgency of Interpretability" for the ambition, and the 2025 paper on chain-of-thought monitorability for the open argument about how easily you can blind your own window. Build with the ambition. Stay honest about the argument. That combination is rarer than either one alone, and it is the whole game.