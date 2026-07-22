---
title: "Liquid: Back to the future"
source: "https://x.com/benjaminsehl/status/2079633466581258469"
author:
  - "[[@benjaminsehl]]"
published: 2026-07-21
created: 2026-07-22
description: "Why Shopify is moving theme structure back into readable code—and what that unlocks for developers, merchants, and agents.Exactly 12 years a..."
tags:
  - "clippings"
  - "software-craft"
---
![Image](https://pbs.twimg.com/media/HNxXhNhX0AApFLT?format=jpg&name=large)

Why Shopify is moving theme structure back into readable code—and what that unlocks for developers, merchants, and agents.

Exactly 12 years ago today, I started building my first Shopify store.

I wasn’t really a developer. I was a tech-savvy designer who knew HTML, CSS, and just enough jQuery to be dangerous. What I did know was that I wanted a storefront that felt completely custom to the brand I was building—but I didn’t want to manage an entire commerce stack just to get there.

Then I found Shopify.

I downloaded Timber, opened its collection template, and everything clicked:

```text
{% for product in collection.products %}
  {% include 'product-grid-item' %}
{% endfor %}
```

The whole template was 100 lines of code. I could understand how it worked simply by reading the code. I barely needed the documentation beyond [Mark Dunkley’s cheat sheet](https://cheat.markdunkley.com/).

For theme developers, that was a golden era of legibility. For merchants, global Theme Settings clearly weren't enough.

## The trade-off we made

Theme settings only took us so far. In 2016, Shopify introduced Sections, and three things changed at once.

1. Merchants became merchandisers. People who couldn’t code could shape pages and tell a much richer product story.
2. Developers became component designers. Sections had to be modular, flexible, and work in any order.
3. And themes became products. Developers had to think about the interface they were crafting and make deliberate trade-offs between ease of use and flexibility.

Those forces accelerated with Dawn in 2016, and then again with Horizon last year, and the introduction of "blocks" as the core composable unit in themes.

To represent sections and blocks across every template, Shopify needed a serialization format. Templates moved to JSON.

That trade-off gave merchants far more control, but it came with a developer-experience cost: you could no longer understand a page by reading one file. You had to cross-reference JSON, Liquid, schemas, settings, sections, and blocks to reconstruct how the page worked.

The moment templates became JSON, they stopped being a great developer surface. They became an auto-saved output—something we literally warned developers not to edit by hand.

That was a rational trade for the "imperative software" era; where merchants shaped a store through buttons, knobs, and settings to specify exactly what should change.

AI changes the equation.

## A great developer experience is a great agent experience

When we gave Sidekick the ability to edit themes, the Online Store Editor entered its "declarative software" era. Simple example, instead of opening a color picker and selecting \`[#0000FF](https://x.com/search?q=%230000FF&src=hashtag_click)\`, a merchant could simply say, “Make this blue.”

Merchants have already made 25 million Sidekick theme edits this year, and 1 in 5 merchants are using AI to edit their theme.

At the same time, developers are increasingly using agents to write code. That means Shopify now has two connected jobs:

1. Give agents better guidance.
2. Give them better feedback.

For guidance, we’re releasing improved Liquid skills. Themes can also carry agent instructions through a \`.agents\` directory, and include files like \`AGENTS.md\` and \`DESIGN.md\`, to help coding agents understand how you want code to be written, and how to keep your designs on brand.

For feedback, we’ve expanded the \`{% doc %}\` tag into typed contracts for snippets and blocks. Parameters can be documented, typed, validated by Theme Check, and paired with examples to how to use it.

```text
{% doc %}
  @param {string} [variant]
  @param {string} [tag]

  @example
  {% block 'text', tag: 'h1' %}
    Featured Collection
  {% endblock %}
{% enddoc %}
```

When you're writing code by hand this gives you realtime feedback, intellisense, and errors; and it also gives agents a way to discover valid parameters, learn what good output looks like, and get actionable feedback when they hallucinate an API that doesn’t exist.

We’ve also added 20 new Theme Check rules covering contracts, structure, validation, complexity, nesting, and file-size limits.

The amazing thing for developers like me, in the agent era is that it rewards the same things we've always wanted: legible code, explicit contracts, and fast feedback.

So we asked a bigger question: what would the ideal theme architecture look like if it treated those qualities as first principles?

We’ve been building a new Shopify base theme, that pulls all of our ideas together.

(I should mention… this is a new architecture to optimize for coding agents, but it's not a forced rewrite. Existing themes will continue to work forever; Liquid has and always will be a forever API.)

## Page structure is readable code again

The first thing you'll notice about the new theme is when you open its \`templates\` directory; the templates are Liquid files again.

Its collection template is roughly the same length as Timber’s, and the overall theme has 93% fewer lines of code than Horizon. This isn’t meant to be a batteries-included theme like Horizon, it’s there to make it really easy to build with all of the commerce primitives in Shopify and to lay a foundation for how to get the best possible performance, but leaves you to build all the things that make each merchant's store unique.

Why move page structure back into Liquid?

The deeper problem with serialized configuration isn’t that JSON is inherently bad. It’s that configuration has a constrained vocabulary. A theme developer has to anticipate the compositions a merchant might want.

Imagine a section containing one button. A merchant asks an agent to add a second button beside it.

In a settings-driven architecture, the theme must already expose a group block capable of holding both buttons, or the developer must have anticipated a second-button setting.

In HTML, you add another button and wrap the pair in a \`div\`.

Every leading model already understands HTML. It is expressive, local, and token-efficient. And Shopify has had the language needed to combine that expressiveness with commerce for more than 20 years: Liquid.

## Blocks and HTML, together

The new architecture introduces a composable \`{% block %}\` tag that can be used directly inside Liquid templates.

```text
<div class="mb-8">
  {% block 'text',
    tag: 'h1',
    block.settings.variant: 'type-heading-xl',
    class: 'mb-2'
  %}
    {{ collection.title | escape }}
  {% endblock %}
</div>
```

Blocks accept named parameters. They can contain nested content. Their parameters can be typed through \`{% doc %}\`. They define the boundaries of what merchants can interact with, while ordinary HTML handles everything else.

If you’ve used a component system like React, the model will feel familiar: parameters behave like props, and nested content behaves like children. But it remains Liquid—simple enough to read from top to bottom in one file.

This makes composition explicit without requiring every piece of markup to become another section, block, or setting.

## Fine-grained reactivity with partials

Theme developers have stretched the Section Rendering API far beyond what it was originally designed to do because it was the best available tool for server-driven reactivity.

We wanted something more precise.

Inspired by emerging work on declarative partial updates, we’re bringing a simple primitive called **partials** to Liquid.

Wrap a region that can be re-rendered:

```text
{% partial 'cart-count' %}
  <span>
    {{ 'cart.count' | t: count: cart.item_count }}
  </span>
{% endpartial %}
```

Then fetch fresh HTML and apply it where needed:

```javascript
const html = await partials.fetch('cart-items', 'cart-count');
partials.apply(html);
```

That’s it. Fine-grained server-rendered updates without rendering an entire section or introducing a virtual DOM.

Adding to cart can update the relevant cart regions in a few lines. This one primitive will let us remove thousands of lines of reactivity code from Horizon.

## Standard Events and Actions

We’re also making common storefront interactions simpler and more interoperable.

Standard Actions provide a shared contract for operations such as updating a cart. Standard Events let themes and apps react through the same stable vocabulary.

```text
const { cart } = await Shopify.actions.updateCart({
  lines: [{
    merchandiseId: variant.id,
    quantity: 1,
  }],
});
```

This is easier for developers to write, easier for apps to integrate with, and easier for agents to understand. Standard Actions work across Shopify stores today, and WebMCP support gives browser agents a semantic path to browse and add products while the storefront responds to those interactions.

The goal isn’t to bolt an “AI mode” onto the storefront. It is to make the storefront’s capabilities clear and composable for every participant: themes, apps, developers, and agents.

## Making Liquid safer to evolve

There were also some obvious language capabilities we wanted to add to Liquid: boolean expressions, infix operators with precedence, and literal arrays and objects.

The blocker wasn’t a lack of desire. Liquid’s historical parser accepted ambiguous syntax that wasn’t formally valid. Introducing new syntax could therefore change how existing themes behaved.

The team undertook a major migration to move themes safely onto a strict parser. That work gives us room to evolve Liquid without breaking the storefronts that already depend on it.

It unlocks simpler, more familiar expressions:

```text
{{ 1 + 1 }}
{{ false && false || true }}
{% assign products = ["shirt", "hat", "shoes"] %}
```

It also makes errors more predictable—for developers and for agents.

## One more thing: Tailwind

Coming soon, we’re bringing Tailwind support to Liquid themes.

Agents are great at it. Developers already understand it. And it gives us a shared styling language built around design tokens, without forcing merchants to inherit a complicated build system.

That shared vocabulary matters. The better agents understand structure, contracts, and styling intent, the more developers can focus on the parts of a storefront that actually differentiate a brand.

## Back to the future

Twelve years ago, Shopify clicked for me because I could open a theme, read the code, and understand the store.

Over time, we made themes vastly more flexible for merchants, but the code became harder to see through.

Agents give us a chance to reunite those two things: the flexibility merchants need and the legibility developers deserve.

That is the direction behind this new architecture:

- Liquid templates as readable page structure.
- Composable, typed blocks alongside ordinary HTML.
- Agent skills and repository-level guidance.
- Richer feedback through \`{% doc %}\` and Theme Check.
- Fine-grained reactivity through partials.
- Shared storefront contracts through Standard Events and Actions.
- A strict parser that lets Liquid evolve safely.
- Tailwind as a common styling language.

The developer preview and documentation are available now:

[https://shopify.dev/docs/storefronts/themes/getting-started/developer-preview](https://shopify.dev/docs/storefronts/themes/getting-started/developer-preview)

Give it a shot, and send me your feedback. I can't wait to see what you build!