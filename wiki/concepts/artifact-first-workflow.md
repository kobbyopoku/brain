---
type: concept
title: Artifact-First Workflow
created: 2026-05-05
updated: 2026-06-06
aliases: [artifact-workflow, artifact-emission-pattern, single-artifact-pattern]
tags: [agent-output, ai-design, artifacts, sandboxed-preview, generation-pattern]
---

# Artifact-First Workflow

> An agent-output pattern where the agent emits a single self-contained HTML wrapped in an `<artifact>` tag, the host surface renders it in a sandboxed `srcdoc` iframe, and exports flow from there to multiple formats (PDF, PPTX, ZIP, Markdown). Originated in Anthropic's [[wiki/entities/claude-design|Claude Design]]; replicated and extended in [[wiki/entities/open-design|Open Design]].

## Definition

The **artifact-first workflow** is a generation pattern in which:

1. The agent produces a single, self-contained HTML document (with embedded CSS and minimal JavaScript) wrapped in an `<artifact>` tag.
2. The host surface extracts the artifact, renders it in a **sandboxed `srcdoc` iframe**, and shows it as a live preview.
3. The user inspects the artifact visually, requests changes, or exports.
4. **Exports flow from the artifact**: HTML (raw), PDF (Chrome headless render), PPTX (html-to-pptx conversion), ZIP (artifact + assets), Markdown (semantic export).
5. The artifact remains the source-of-truth — iterations modify the artifact; exports are derivable.

The pattern privileges **HTML as the universal intermediate format**: an HTML artifact can render visually, export to PDF, convert to a slide deck, or produce structured data. Other formats (Figma files, design tokens JSON, native PowerPoint) require specialized tooling; HTML works everywhere.

## Why it matters

Artifact-first solves three problems with traditional agent-design generation:

1. **Multi-format flexibility from one source.** Without artifact-first, an agent generating a "deck" produces PowerPoint XML; one generating a "landing page" produces HTML; one generating a "PDF report" produces a different format again. Each requires different tooling, and outputs are not freely interchangeable. With artifact-first, a single HTML can become any of those formats via export pipelines.
2. **Live preview without local server.** Sandboxed `srcdoc` iframes render arbitrary HTML safely (no network access, no parent-frame access). The user sees the result instantly without "save → open → reload" cycles or local dev servers.
3. **Iteration locality.** All edits target the artifact directly. The agent doesn't have to maintain a separate "design representation" alongside the rendered output — the rendered output *is* the representation.

The pattern is also **architecturally clean** for tools like Open Design: one input format (markdown brief + skill + DESIGN.md), one output format (HTML artifact), one rendering surface (sandboxed iframe), one export pipeline (HTML → others). Engineering complexity stays low even as the user-visible surface area grows.

## Treatment across sources

- [[wiki/sources/nexu-io-open-design]] — canonical wiki source. Open Design's workflow centers on artifact emission and sandboxed rendering. Open Design's `import/claude-design` ZIP endpoint also confirms Claude Design uses the same pattern with portable artifacts.
- [[wiki/entities/claude-design]] — the proprietary Anthropic product that originated the pattern. No primary source from Anthropic is yet ingested directly; observations are inferred.
- [[wiki/sources/trq212-x-html-effectiveness]] — *2026-05-08*. **Strongest first-party Anthropic argument for the pattern yet ingested.** [[wiki/entities/trq212|Thariq Shihipar]] (Claude Code lead at Anthropic) makes the substantive case: *"if an output is meant to be reviewed, clicked, compared, edited, or shared, HTML is often closer to the real workspace."* Distinguishes the artifact-first pattern from Markdown-as-default and provides 20 worked examples at [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness). Validates Open Design's architectural bet from inside Anthropic.
- [[wiki/sources/nateherk-claude-design-tally-brand]] frames it as the **strongest first-party evidence yet** for the pattern: Claude Design's verifier loop (screenshot → inspect → fix before the user sees it) is the artifact-first surface extended with an evaluator-optimizer self-validation loop.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] frames it **obliquely**: describes the user-facing Claude Design workflow that drives artifact emission, but does not discuss the artifact mechanism directly — it is the underlying emission model.
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] frames it **adjacently**: the generated-interface-as-surface idea echoes the HTML/artifact-as-output thesis; both argue generated artifacts beat static formats as the interface.
- *Adjacent treatments not yet ingested*: Vercel v0 (similar pattern: AI generates Next.js components, renders in sandboxed preview); Figma Make (different format but similar pattern); HTML-PDF tooling like Puppeteer / Playwright.

## Sub-claims and details

### Why `<artifact>` as the wrapper

The `<artifact>` tag is a *parsing convention* — it signals "this is a complete, self-contained output the host surface should extract and render separately from chat content." It's not an HTML standard tag; it's a custom tag the application's parsing layer recognizes.

Alternatives considered (per the design-tooling space):

- **Triple backtick code block**: works for plain code but doesn't carry a render hint.
- **JSON wrapper with `{type: "artifact", content: "..."}`**: more structured but not human-readable in chat.
- **Custom tag** (`<artifact>`, `<canvas>`, `<output>`): self-explanatory in the chat transcript and easy to parse.

Anthropic chose custom tag. Open Design follows the same convention. Other tools (Vercel v0, etc.) use triple-backtick + language hints (`` ```jsx ``).

### Sandboxed `srcdoc` iframe rendering

`<iframe srcdoc="<html>...</html>">` renders inline HTML in an iframe without making a network request. With `sandbox` attribute set, the iframe:

- Cannot access the parent frame's DOM (security).
- Cannot make network requests (security + privacy).
- Cannot execute JavaScript unless `sandbox="allow-scripts"` (typically allowed).
- Cannot navigate the parent frame.

This is the right primitive for "render arbitrary HTML safely" — the iframe acts as a security boundary that prevents the artifact from accessing application state.

The pattern's safety hinges on getting the sandbox attributes right: `sandbox="allow-scripts allow-same-origin"` would be insecure (gives the iframe origin access). `sandbox="allow-scripts"` (without `allow-same-origin`) is the right default for artifact rendering.

### Export pipeline architecture

| Format | Mechanism | Notes |
|---|---|---|
| **HTML** | Direct (artifact contents) | Highest fidelity. |
| **PDF** | Chrome headless print-to-PDF | Pixel-perfect rendering of the HTML; preserves CSS. |
| **PPTX** | html-to-pptx libraries (e.g. `pptx-html-fidelity-audit` skill) | Lossy: complex CSS may not translate to PowerPoint shape primitives. |
| **ZIP** | Artifact + extracted assets bundled | Useful for offline distribution. |
| **Markdown** | Semantic extraction from HTML | Lossy: visual styling discarded. |

The PPTX path is the most architecturally interesting — Open Design ships an explicit `pptx-html-fidelity-audit` skill whose job is to grade *how well* an HTML artifact translates to PPTX. This acknowledges the lossy-conversion problem and makes it explicit.

### Why HTML is the right intermediate

HTML wins as an artifact format for several reasons:

- **Universally renderable**: every browser, every mail client, every screenshot tool understands HTML.
- **Self-contained**: with embedded CSS and inline images (data URIs), an HTML file has zero external dependencies.
- **Lossless to PDF**: Chrome's print-to-PDF preserves layout fully.
- **Convertible to other formats**: tools exist for HTML → PPTX, HTML → MD, HTML → image.
- **Editable as source**: power users can edit the HTML directly.
- **Familiar to LLMs**: training corpora are dense with HTML; agents generate it well.

Alternatives considered: SVG (great for vector but poor for layout), Markdown (text-only), image bitmaps (lossy and uneditable), Figma JSON (proprietary), PDF (terminal — can't be edited). HTML is the only format that hits every requirement.

### Iteration model

Once an artifact exists:

1. User says "make the hero red."
2. Agent reads the existing artifact + the change request.
3. Agent emits a *new* artifact with the change applied.
4. Host surface diffs the new artifact against the previous, shows the new one as the preview.

This is a **stateful iteration** model — every turn produces a fresh artifact, but the artifact carries the full state. Compare with stateful conversational design tools (Figma, Sketch) where users *edit in place* and the design is the canonical state.

The artifact-first model has a useful property: **every turn's artifact is shareable independently**. The user can export turn 3's version while continuing to iterate; turn 7's version remains a separate artifact. No save points, no version control complexity — every turn is a release.

### Verifier loop over the artifact

Per [[wiki/sources/nateherk-claude-design-tally-brand]], Claude Design wraps artifact emission in a **self-validation loop**: it renders the artifact, takes a screenshot, inspects the result, and fixes defects *before the user sees the preview*. This is the artifact-first surface composed with an evaluator-optimizer pattern — the artifact is not just emitted and shown, it is emitted, evaluated against its own rendered output, and corrected in the same turn.

## Open questions and contradictions

- **Single-artifact emission limits multi-component design work.** A landing page is one artifact, but a design system spanning a landing page + dashboard + email is three artifacts. The pattern handles this by treating each as a separate generation, but loses the cross-artifact consistency that comes from a unified design source.
- **PPTX conversion is meaningfully lossy.** Open Design ships a fidelity-audit skill specifically because the conversion isn't perfect. Users expecting WYSIWYG PPTX may be disappointed.
- **JavaScript artifacts are constrained.** The sandboxed iframe limits what JS can do. Interactive prototypes (modals, animations, form validation) need careful sandboxed-design.
- **Artifact size limits.** Single-HTML artifacts can grow large (embedded images bloat them). Browsers and email clients cap at a few MB; LLM context limits cap at smaller numbers.
- **Versioning / branching of artifacts isn't natively supported.** "Show me the red-hero version side-by-side with the blue-hero version" requires the application surface to manage variant tracking.
- **Anthropic's exact `<artifact>` semantics aren't fully documented publicly.** Open Design's implementation matches the observed behavior of Claude Design but may diverge on edge cases.

## Related concepts

- [[design-md]] — DESIGN.md is the input the agent reads to produce the artifact.
- [[claude-code-skills]] — SKILL.md tells the agent what kind of artifact to produce.
- [[anti-ai-slop-machinery]] — the discipline applied during artifact generation.
- [[question-form-first]] — Turn-1 form precedes artifact generation.
- [[visual-directions]] — selects the aesthetic the artifact embodies.
- [[markdown-as-agent-contract]] — artifacts are contracts: agent commits to producing the rendered output.
- [[mcp-server]] — adjacent: Open Design's MCP exposes `get_artifact` for cross-repo access.

## Related entities

- [[wiki/entities/claude-design]] — the proprietary product that originated the pattern.
- [[wiki/entities/open-design]] — the open-source replication.
- [[wiki/entities/anthropic]] — publisher of the original pattern.
- [[wiki/entities/open-codesign]] — lineage credit for streaming-artifact-rendering primitives.
- [[wiki/entities/trq212]] — Thariq Shihipar, Claude Code lead at Anthropic; published the strongest first-party argument for the pattern.

## Mentioned in

- [[wiki/sources/nexu-io-open-design]]
- [[wiki/sources/trq212-x-html-effectiveness]]
- [[wiki/sources/nateherk-claude-design-tally-brand]] — verifier-loop evidence for the pattern.
- [[wiki/sources/prajwaltomar-claude-design-workflow]] — user-facing workflow driving artifact emission.
- [[wiki/sources/suyashkarn2-ai-trillion-dollar-blind-spot-static-website]] — generated-interface-as-surface echo of the artifact thesis.
