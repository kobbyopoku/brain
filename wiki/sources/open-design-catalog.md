---
type: source
title: Open Design Catalog — full inventory of 139 design systems + 71 skills + 9 craft docs
created: 2026-05-05
updated: 2026-05-05
source_url: https://github.com/nexu-io/open-design
source_type: github-repo-catalog
author: nexu-io
source_date: 2026-05-05
raw_path: raw/open-design/
tags: [design-systems, claude-code-skills, design-md, catalog, open-design, comprehensive-inventory]
---

# Open Design Catalog — full inventory of 139 design systems + 71 skills + 9 craft docs

> Companion catalog source to [[wiki/sources/nexu-io-open-design|nexu-io/open-design]] (the architectural overview). This page enumerates **every artifact** the Open Design repo ships: 139 brand DESIGN.md files, 71 SKILL.md bundles, 9 craft discipline docs, plus visual-directions, device frames, and prompt-template indexes. All raw content fetched into `raw/open-design/` (2.5MB, 227 markdown files) on 2026-05-05.

## TL;DR

The architectural source page covers *what Open Design is*; this page covers *what's in it*. Use this as a lookup index when you need to know *"does Open Design have a DESIGN.md for X?"* or *"what skill matches the surface I'm building?"*.

**Counts (live, 2026-05-05)**:
- **139 design systems** across 20 categories (~70 product brands + ~57 design styles + 2 starters + others).
- **71 skills** across 6 functional groups (prototypes, decks, docs, media, integrations, meta).
- **9 craft discipline docs** (anti-ai-slop, accessibility, animation, color, typography, form-validation, rtl-bidi, state-coverage, plus README).
- **5 visual directions** (Editorial Monocle, Modern Minimal, Tech Utility, Brutalist, Soft Warm) — see [[visual-directions]].
- **5 device frames** (iPhone 15 Pro, Pixel, iPad Pro, MacBook, Browser Chrome — HTML files in `assets/frames/`).
- **94 prompt templates** (44 image + 50 video JSON files in `prompt-templates/`).

**Raw layer**: every artifact is stored locally at `raw/open-design/<subdir>/` and is directly readable by AI agents without re-fetching from GitHub.

## Design systems (139 brands across 20 categories)

The richer alternative to the [[wiki/sources/refero-design-systems-for-ai-agents|Refero catalog]]. Each entry uses the **9-section schema** documented in [[design-md]] (atmosphere → palette → typography → components → layout → depth → do/don't → responsive → agent-prompt-guide). Raw at `raw/open-design/design-systems/<brand>/DESIGN.md`.

### AI & LLM (14 brands)

- [[wiki/entities/anthropic|claude]] — Anthropic's AI assistant. Warm terracotta accent, clean editorial layout.
- [[wiki/entities/cohere|cohere]] — Enterprise AI platform. Vibrant gradients, data-rich dashboard aesthetic.
- [[wiki/entities/elevenlabs|elevenlabs]] — AI voice platform. Dark cinematic UI, audio-waveform aesthetics.
- [[wiki/entities/huggingface|huggingface]] — ML community hub. Sunny yellow accent, monospace identity, cheerful and dense.
- [[wiki/entities/minimax|minimax]] — AI model provider. Bold dark interface with neon accents.
- [[wiki/entities/mistral-ai|mistral-ai]] — Open-weight LLM provider. French-engineered minimalism, purple-toned.
- [[wiki/entities/ollama|ollama]] — Run LLMs locally. Terminal-first, monochrome simplicity.
- [[wiki/entities/openai|openai]] — Calm, near-monochrome system anchored in deep teal-black with generous white space and editorial typography.
- [[wiki/entities/opencode-ai|opencode-ai]] — AI coding platform. Developer-centric dark theme.
- [[wiki/entities/replicate|replicate]] — Run ML models via API. Clean white canvas, code-forward.
- [[wiki/entities/runwayml|runwayml]] — AI video generation. Cinematic dark UI, media-rich layout.
- [[wiki/entities/together-ai|together-ai]] — Open-source AI infrastructure. Technical, blueprint-style design.
- [[wiki/entities/voltagent|voltagent]] — AI agent framework. Void-black canvas, emerald accent, terminal-native.
- [[wiki/entities/x-ai|x-ai]] — Elon Musk's AI lab. Stark monochrome, futuristic minimalism.

### Productivity & SaaS (10)

- [[wiki/entities/arc|arc]] — *"The browser that browses for you."* Translucent surfaces, gradient warmth, sidebar-first layout.
- [[wiki/entities/cal|cal]] — Open-source scheduling. Clean neutral UI, developer-oriented simplicity.
- [[wiki/entities/discord|discord]] — Voice / chat platform. Deep blurple, dark-first surfaces, playful accent moments.
- [[wiki/entities/duolingo|duolingo]] — Language-learning platform. Bright owl green, chunky shadows, gamified joy.
- [[wiki/entities/intercom|intercom]] — Customer messaging. Friendly blue palette, conversational UI patterns.
- [[wiki/entities/linear|linear-app]] — Project management. Ultra-minimal, precise, purple accent. *(Sample DESIGN.md confirmed 9-section schema, ~370 lines.)*
- [[wiki/entities/mintlify|mintlify]] — Documentation platform. Clean, green-accented, reading-optimized.
- [[wiki/entities/notion|notion]] — All-in-one workspace. Warm minimalism, serif headings, soft surfaces.
- [[wiki/entities/resend|resend]] — Email API. Minimal dark theme, monospace accents.
- [[wiki/entities/zapier|zapier]] — Automation platform. Warm orange, friendly illustration-driven.

### Developer Tools (8)

- [[wiki/entities/cursor|cursor]] — AI-first code editor. Sleek dark interface, gradient accents.
- [[wiki/entities/expo|expo]] — React Native platform. Dark theme, tight letter-spacing, code-centric.
- [[wiki/entities/github|github]] — Code-forward platform. Functional density, blue-on-white precision, Primer foundations.
- [[wiki/entities/lovable|lovable]] — AI full-stack builder. Playful gradients, friendly dev aesthetic.
- [[wiki/entities/raycast|raycast]] — Productivity launcher. Sleek dark chrome, vibrant gradient accents.
- [[wiki/entities/superhuman|superhuman]] — Fast email client. Premium dark UI, keyboard-first, purple glow.
- [[wiki/entities/vercel|vercel]] — Frontend deployment. Black and white precision, Geist font.
- [[wiki/entities/warp|warp]] — Modern terminal. Dark IDE-like interface, block-based command UI.

### Backend & Data (8)

- [[wiki/entities/clickhouse|clickhouse]] — Fast analytics database. Yellow-accented, technical documentation style.
- [[wiki/entities/composio|composio]] — Tool integration platform. Modern dark with colorful integration icons.
- [[wiki/entities/hashicorp|hashicorp]] — Infrastructure automation. Enterprise-clean, black and white.
- [[wiki/entities/mongodb|mongodb]] — Document database. Green leaf branding, developer documentation focus.
- [[wiki/entities/posthog|posthog]] — Product analytics. Playful hedgehog branding, developer-friendly dark UI.
- [[wiki/entities/sanity|sanity]] — Headless CMS. Red accent, content-first editorial layout.
- [[wiki/entities/sentry|sentry]] — Error monitoring. Dark dashboard, data-dense, pink-purple accent.
- [[wiki/entities/supabase|supabase]] — Open-source Firebase alternative. Dark emerald theme, code-first.

### Fintech & Crypto (7)

- [[wiki/entities/binance|binance]] — Crypto exchange. Bold yellow accent on monochrome, trading-floor urgency.
- [[wiki/entities/coinbase|coinbase]] — Crypto exchange. Clean blue identity, trust-focused, institutional feel.
- [[wiki/entities/kraken|kraken]] — Crypto trading. Purple-accented dark UI, data-dense dashboards.
- [[wiki/entities/mastercard|mastercard]] — Global payments network. Warm cream canvas, orbital pill shapes, editorial warmth.
- [[wiki/entities/revolut|revolut]] — Digital banking. Sleek dark interface, gradient cards, fintech precision.
- [[wiki/entities/stripe|stripe]] — Payment infrastructure. Signature purple gradients, weight-300 elegance.
- [[wiki/entities/wise|wise]] — Money transfer. Bright green accent, friendly and clear.

### Media & Consumer (12)

- [[wiki/entities/apple|apple]] — Consumer electronics. Premium white space, SF Pro, cinematic imagery.
- [[wiki/entities/ibm|ibm]] — Enterprise technology. Carbon design system, structured blue palette.
- [[wiki/entities/nvidia|nvidia]] — GPU computing. Green-black energy, technical power aesthetic.
- [[wiki/entities/pinterest|pinterest]] — Visual discovery. Red accent, masonry grid, image-first.
- [[wiki/entities/playstation|playstation]] — Gaming console retail. Three-surface channel layout, quiet-authority display type, cyan hover-scale.
- [[wiki/entities/spacex|spacex]] — Space technology. Stark black and white, full-bleed imagery, futuristic.
- [[wiki/entities/spotify|spotify]] — Music streaming. Vibrant green on dark, bold type, album-art-driven.
- [[wiki/entities/theverge|theverge]] — Tech editorial media. Acid-mint and ultraviolet accents, Manuka display, rave-flyer story tiles.
- [[wiki/entities/uber|uber]] — Mobility platform. Bold black and white, tight type, urban energy.
- [[wiki/entities/vodafone|vodafone]] — Global telecom brand. Monumental uppercase display, Vodafone Red chapter bands.
- [[wiki/entities/wired|wired]] — Tech magazine. Paper-white broadsheet density, custom serif display, mono kickers, ink-blue links.
- [[wiki/entities/xiaohongshu|xiaohongshu]] — Lifestyle UGC social platform. Singular brand red, generous radius, content-first.

### E-Commerce & Retail (5)

- [[wiki/entities/airbnb|airbnb]] — Travel marketplace. Warm coral accent, photography-driven, rounded UI.
- [[wiki/entities/meta|meta]] — Tech retail store. Photography-first, binary light/dark surfaces, Meta Blue CTAs.
- [[wiki/entities/nike|nike]] — Athletic retail. Monochrome UI, massive uppercase type, full-bleed photography.
- [[wiki/entities/shopify|shopify]] — E-commerce platform. Dark-first cinematic, neon green accent, ultra-light type.
- [[wiki/entities/starbucks|starbucks]] — Global coffee retail brand. Four-tier green system, warm cream canvas, full-pill buttons.

### Automotive (6)

- [[wiki/entities/bmw|bmw]] — Luxury automotive. Dark premium surfaces, precise German engineering aesthetic.
- [[wiki/entities/bugatti|bugatti]] — Hypercar brand. Cinema-black canvas, monochrome austerity, monumental display type.
- [[wiki/entities/ferrari|ferrari]] — Luxury automotive. Chiaroscuro editorial, Ferrari Red accents, cinematic black.
- [[wiki/entities/lamborghini|lamborghini]] — Supercar brand. True black surfaces, gold accents, dramatic uppercase typography.
- [[wiki/entities/renault|renault]] — French automotive. Vibrant aurora gradients, NouvelR typography, bold energy.
- [[wiki/entities/tesla|tesla]] — Electric automotive. Radical subtraction, full-viewport photography, near-zero UI.

### Design & Creative (7)

- [[wiki/entities/airtable|airtable]] — Spreadsheet-database hybrid. Colorful, friendly, structured data aesthetic.
- [[wiki/entities/canva|canva]] — Visual creation platform. Vivid purple-blue gradient, generous spacing, friendly geometry.
- [[wiki/entities/clay|clay]] — Creative agency. Organic shapes, soft gradients, art-directed layout.
- [[wiki/entities/figma|figma]] — Collaborative design tool. Vibrant multi-color, playful yet professional.
- [[wiki/entities/framer|framer]] — Website builder. Bold black and blue, motion-first, design-forward.
- [[wiki/entities/miro|miro]] — Visual collaboration. Bright yellow accent, infinite canvas aesthetic.
- [[wiki/entities/webflow|webflow]] — Visual web builder. Blue-accented, polished marketing site aesthetic.

### Editorial & Print (1)

- [[wiki/entities/kami|kami]] — Editorial paper system: warm parchment canvas, ink-blue accent, serif-led hierarchy. Built for resumes, one-pagers, white papers, portfolios, slide decks — anything that should feel like high-quality print rather than UI. Multilingual by design (EN · zh-CN · ja).

### Editorial · Studio (1)

- [[wiki/entities/atelier-zero|atelier-zero]] — A magazine-grade, collage-driven visual system: warm paper canvas, surreal compositions, editorial-grade typography.

### Modern & Minimal (10)

- [[wiki/entities/clean|clean]] — Simplicity-focused; ample whitespace, legible typography, limited palette.
- [[wiki/entities/contemporary|contemporary]] — Current-era minimalist design with bento grids, dark mode, accessible layouts.
- [[wiki/entities/flat|flat]] — 2D minimalist style with vibrant colors, no 3D effects, fast and user-friendly.
- [[wiki/entities/minimal|minimal]] — Stripped-back design emphasizing whitespace and restrained color.
- [[wiki/entities/modern|modern]] — Contemporary editorial style with serif typography and clean layouts.
- [[wiki/entities/mono|mono]] — Monospace-driven, matrix-inspired design with high contrast and compact density.
- [[wiki/entities/refined|refined]] — Carefully curated modern minimal with elegant serif typography.
- [[wiki/entities/shadcn|shadcn]] — Shadcn/ui-inspired with monochrome palette and utility-first patterns.
- [[wiki/entities/simple|simple]] — Straightforward, no-frills with clean typography and neutral colors.
- [[wiki/entities/sleek|sleek]] — Modern minimalist with clean lines and intentional color palette.

### Bold & Expressive (8)

- [[wiki/entities/bold|bold]] — Heavyweight typography, high-contrast colors, commanding layouts.
- [[wiki/entities/brutalism|brutalism]] — Raw, anti-design aesthetic with concrete-architecture inspiration.
- [[wiki/entities/colorful|colorful]] — Vibrant high-contrast palettes and gradients.
- [[wiki/entities/dramatic|dramatic]] — High-contrast theatrical design with bold immersive layouts.
- [[wiki/entities/energetic|energetic]] — Dynamic, vibrant; thick borders, geometric shapes, high-contrast.
- [[wiki/entities/expressive|expressive]] — Personality-driven; bold colors, playful graphics, dynamic layouts.
- [[wiki/entities/neobrutalism|neobrutalism]] — Modern brutalism: bold borders, vivid accents, raw layouts on warm surfaces.
- [[wiki/entities/vibrant|vibrant]] — Lively colorful design with bold playful typography.

### Creative & Artistic (11)

- [[wiki/entities/artistic|artistic]] — High-contrast expressive style with creative typography.
- [[wiki/entities/cafe|cafe]] — Cozy cafe-inspired with warm tones and soft typography.
- [[wiki/entities/cosmic|cosmic]] — Futuristic sci-fi with dark themes and vibrant neon accents.
- [[wiki/entities/creative|creative]] — Playful, character-driven with expressive typography and bold graphics.
- [[wiki/entities/doodle|doodle]] — Hand-drawn, sketch-like with handwritten fonts and imperfect lines.
- [[wiki/entities/editorial|editorial]] — Magazine-inspired with refined serif typography and structured grids.
- [[wiki/entities/fantasy|fantasy]] — Game-inspired fantasy with bold premium visuals.
- [[wiki/entities/friendly|friendly]] — Approachable; rounded elements, soft pastels, ample whitespace.
- [[wiki/entities/lingo|lingo]] — Playful minimal with bright colors, rounded shapes, tactile 3D borders.
- [[wiki/entities/publication|publication]] — Print-inspired language for books, magazines, reports.
- [[wiki/entities/storytelling|storytelling]] — Narrative-driven; visuals, copy, interaction guide the user.

### Professional & Corporate (10)

- [[wiki/entities/ant|ant]] — Structured enterprise design system; clarity, consistency, efficiency for data-dense apps.
- [[wiki/entities/application|application]] — App dashboard with purple-themed aesthetic, top-bar nav, card-based.
- [[wiki/entities/corporate|corporate]] — Professional brand-aligned with structured grids and minimalist layouts.
- [[wiki/entities/dashboard|dashboard]] — Dark-themed cloud-platform; modular grids, glass-like panels, strong data hierarchy.
- [[wiki/entities/elegant|elegant]] — Graceful refined; delicate typography, minimal palette, polished layouts.
- [[wiki/entities/enterprise|enterprise]] — Clean high-contrast for data-driven workflows; intuitive drag-and-drop.
- [[wiki/entities/luxury|luxury]] — High-end dark with bold headings, monochromatic palette, premium feel.
- [[wiki/entities/material|material]] — Google's Material Design with layered surfaces and dynamic theming.
- [[wiki/entities/premium|premium]] — Apple-inspired premium with precise spacing and modern typography.
- [[wiki/entities/professional|professional]] — Polished business-ready with modern typography and structured layouts.

### Layout & Structure (4)

- [[wiki/entities/bento|bento]] — Modular grid layout with card-like blocks and clear hierarchy.
- [[wiki/entities/levels|levels]] — Conversion-focused; removes friction, guides toward action.
- [[wiki/entities/perspective|perspective]] — Spatial depth with isometric views and 3D-like realism.
- [[wiki/entities/spacious|spacious]] — Generous whitespace, consistent padding, grid-based.

### Morphism & Effects (6)

- [[wiki/entities/claymorphism|claymorphism]] — Soft rounded 3D-like shapes mimicking malleable clay.
- [[wiki/entities/glassmorphism|glassmorphism]] — Frosted glass with translucent layers and subtle blur.
- [[wiki/entities/gradient|gradient]] — Smooth color transitions and gradient-rich surfaces.
- [[wiki/entities/neon|neon]] — Electric neon glow with high-contrast color pairings.
- [[wiki/entities/neumorphism|neumorphism]] — Soft extruded UI elements with inner/outer shadows on monochrome.
- [[wiki/entities/skeumorphism|skeumorphism]] — Real-world mimicry with textured surfaces and 3D effects.

### Retro & Nostalgic (4)

- [[wiki/entities/dithered|dithered]] — Dot-pattern rendering simulating shades with limited palette.
- [[wiki/entities/paper|paper]] — Paper-textured, print-inspired with minimal colors.
- [[wiki/entities/retro|retro]] — Throwback design with vintage typography and high-contrast retro palettes.
- [[wiki/entities/vintage|vintage]] — 1950s-1990s nostalgia with skeuomorphic touches and grainy textures.

### Themed & Unique (5)

- [[wiki/entities/agentic|agentic]] — Conversational AI-first interface with minimal controls and delegated task flows.
- [[wiki/entities/futuristic|futuristic]] — Forward-looking design with tech-inspired typography.
- [[wiki/entities/pacman|pacman]] — Retro arcade with pixel fonts, dotted borders, 8-bit aesthetics.
- [[wiki/entities/tetris|tetris]] — Classic block-game inspired with playful colors and bold display fonts.
- [[wiki/entities/totality-festival|totality-festival]] — Web — festival-experience aesthetic.

### Starter (2)

- [[wiki/entities/default|default]] — A clean, product-oriented default. Use when the brief doesn't call for a specific brand.
- [[wiki/entities/warm-editorial|warm-editorial]] — A serif-led magazine aesthetic. Terracotta accent on warm off-white paper.

### Overlap with [[wiki/sources/refero-design-systems-for-ai-agents|Refero catalog]] (10 brands)

The wiki has both Refero AND Open Design DESIGN.md for these brands:

| Brand | Refero raw | Open Design raw |
|---|---|---|
| airbnb | `raw/airbnb/DESIGN.md` | `raw/open-design/design-systems/airbnb/DESIGN.md` |
| apple | `raw/apple/DESIGN.md` (+ `raw/apple-alt/DESIGN.md`) | `raw/open-design/design-systems/apple/DESIGN.md` |
| cursor | `raw/cursor/DESIGN.md` | `raw/open-design/design-systems/cursor/DESIGN.md` |
| elevenlabs | `raw/elevenlabs/DESIGN.md` | `raw/open-design/design-systems/elevenlabs/DESIGN.md` |
| linear (linear-app) | `raw/linear/DESIGN.md` | `raw/open-design/design-systems/linear-app/DESIGN.md` |
| openai | `raw/openai/DESIGN.md` | `raw/open-design/design-systems/openai/DESIGN.md` |
| raycast | `raw/raycast/DESIGN.md` | `raw/open-design/design-systems/raycast/DESIGN.md` |
| stripe | `raw/stripe/DESIGN.md` | `raw/open-design/design-systems/stripe/DESIGN.md` |
| superhuman | `raw/superhuman/DESIGN.md` | `raw/open-design/design-systems/superhuman/DESIGN.md` |
| anthropic / claude | `raw/anthropic/DESIGN.md` | `raw/open-design/design-systems/claude/DESIGN.md` |

For these brands, prefer the Open Design version when maximum-fidelity is needed (richer 9-section schema, ~2.5× the line count). The Refero versions remain authoritative as the *catalog snapshot* used in cross-brand pattern observations on [[design-md]].

## Skills (71 bundles across 6 functional groups)

Each skill is a `SKILL.md` file with YAML frontmatter (`name`, `description`, `triggers`) plus prose specifying process, output format, edge cases. Raw at `raw/open-design/skills/<name>.md`.

### Prototypes (web + mobile + dashboards)

- **web-prototype** — Generic web prototype shell.
- **web-prototype-taste-brutalist** — Brutalist-flavored web prototype.
- **web-prototype-taste-editorial** — Editorial-flavored web prototype.
- **web-prototype-taste-soft** — Soft/warm-flavored web prototype.
- **mobile-app** — Mobile app screen.
- **mobile-onboarding** — Mobile onboarding flow.
- **gamified-app** — Gamified product (Duolingo/Pacman-flavor).
- **dating-web** — Consumer dating/matchmaking dashboard.
- **hatch-pet** — Pet/companion-app prototype.
- **saas-landing** — Single-page SaaS landing (hero/features/proof/pricing/CTA).
- **kanban-board** — Kanban work-queue UI.
- [[wiki/entities/dashboard|dashboard]] — Admin/analytics dashboard.
- **pricing-page** — Pricing page surface.
- **kami-landing** — Kami-flavored editorial landing.
- **open-design-landing** — Open Design's own marketing surface.
- **wireframe-sketch** — Low-fidelity wireframe.
- **live-artifact** — Stream-rendered live HTML artifact.
- **blog-post** — Long-form article / blog post layout.
- **docs-page** — Documentation page (inline-start nav, scrollable article).
- **waitlist-page** — Pre-launch waitlist page.
- **social-media-dashboard** — Social media analytics dashboard.

### Decks / presentations (the html-ppt family — 17 flavors)

The largest single skill family — Open Design's bet that decks-as-HTML are a primary output format. All emit a single `<artifact>` that exports to PPTX via the `pptx-html-fidelity-audit` companion skill.

- **html-ppt** — Base deck framework.
- **html-ppt-product-launch** — Product-launch deck flavor.
- **html-ppt-pitch-deck** — Investor pitch deck.
- **html-ppt-tech-sharing** — Technical sharing / brown-bag.
- **html-ppt-weekly-report** — Weekly status report.
- **html-ppt-knowledge-arch-blueprint** — Knowledge-architecture blueprint.
- **html-ppt-presenter-mode-reveal** — Presenter-reveal mode.
- **html-ppt-graphify-dark-graph** — Dark graph-heavy deck.
- **html-ppt-hermes-cyber-terminal** — Cyber-terminal aesthetic (the one whose name surfaced [[wiki/entities/hermes-agent|Hermes Agent]] earlier).
- **html-ppt-obsidian-claude-gradient** — Obsidian-Claude gradient flavor.
- **html-ppt-taste-brutalist** — Brutalist-flavored deck.
- **html-ppt-taste-editorial** — Editorial-flavored deck.
- **html-ppt-xhs-pastel-card** — Xiaohongshu pastel-card deck.
- **html-ppt-xhs-post** — Xiaohongshu post format.
- **html-ppt-xhs-white-editorial** — Xiaohongshu white-editorial format.
- **html-ppt-testing-safety-alert** — Safety/alert message format.
- **html-ppt-dir-key-nav-minimal** — Directional-key-nav minimal deck.
- **html-ppt-course-module** — Course-module format.
- **kami-deck** — Kami-flavored deck (editorial paper).
- **replit-deck** — Replit-flavored deck.
- **simple-deck** — Bare-bones deck.
- **open-design-landing-deck** — Open Design's own landing-deck.
- **magazine-poster** — Magazine-style poster.
- **image-poster** — Single-image poster.
- **social-carousel** — Multi-card carousel.
- **guizang-ppt** — Bundled-verbatim from [[wiki/entities/guizang-ppt-skill|guizang-ppt-skill]].

### Documents (PRDs, runbooks, OKRs, finance, etc.)

- **design-brief** — Structured design brief in I-Lang protocol.
- **pm-spec** — Product manager spec / PRD.
- **eng-runbook** — Engineering runbook (alerts, dashboards, escalation).
- **weekly-update** — Weekly status update.
- **meeting-notes** — Structured meeting notes.
- **hr-onboarding** — HR onboarding document.
- **finance-report** — Finance report layout.
- **team-okrs** — Team OKR document.
- **digital-eguide** — Two-spread digital e-guide (cover + content).
- **invoice** — Invoice layout.
- **email-marketing** — Brand product-launch email.

### Media generation (image / video / motion / audio)

- **hyperframes** — HTML→MP4 motion graphics with GSAP timelines.
- **motion-frames** — Motion-graphic frames.
- **sprite-animation** — Sprite-based animation.
- **video-shortform** — Short-form video output.
- **audio-jingle** — Audio jingle / sound effects.

### Integrations (Orbit family — agent-to-platform connectors)

The "orbit" family connects the agent to specific external platforms. Likely one orbit per integration target.

- **orbit-general** — Generic orbit integration shell.
- **orbit-github** — GitHub orbit.
- **orbit-gmail** — Gmail orbit.
- **orbit-linear** — Linear (project mgmt) orbit.
- **orbit-notion** — Notion orbit.

### Meta-skills (for self-improvement and quality gates)

- **critique** — 5-dimension expert design review on any HTML artifact (the 5-dim self-critique mechanism from [[anti-ai-slop-machinery]] codified as a skill).
- **tweaks** — Surgical artifact modifications.
- **pptx-html-fidelity-audit** — Audit how well an HTML artifact translates to PPTX.

## Craft documents (9 design-discipline rules)

The `craft/` directory contains Open Design's *enforced design discipline* — the rules the daemon's `lint-artifact` linter checks at P0. These are the canonical sources for several wiki concepts. Raw at `raw/open-design/craft/`.

- **anti-ai-slop.md** — *The canonical document for [[anti-ai-slop-machinery]]*. Lists the **seven cardinal sins** (auto-enforced at P0): default Tailwind indigo as accent (specific hex blacklist: `#6366f1`, `#4f46e5`, `#4338ca`, `#3730a3`, `#8b5cf6`, `#7c3aed`, `#a855f7`); two-stop "trust" gradients (purple→blue, blue→cyan, indigo→pink); emoji as feature icons (✨, 🚀, 🎯, ⚡, 🔥, 💡 in `<h*>`/`<button>`/`<li>`/`class*="icon"`); sans-serif on display when seed binds a serif; (4 more). Adapted from the open-source `refero_skill` (MIT) by [[wiki/entities/refero|Refero]]. **The lint surface is auto-enforced**: `apps/daemon/src/lint-artifact.ts` ships the indigo blacklist as `AI_DEFAULT_INDIGO`. Lineage clarified: anti-ai-slop discipline originated in Refero's open-source skill; Open Design tightened and codified it.
- **accessibility-baseline.md** — Required accessibility rules (~12.9 KB).
- **animation-discipline.md** — Motion-design rules (~9.1 KB).
- **color.md** — Color discipline (~3.1 KB).
- **form-validation.md** — Form-validation discipline (~17.2 KB — the largest craft doc; deep specification).
- **rtl-and-bidi.md** — Right-to-left and bidirectional text rules (~12.2 KB).
- **state-coverage.md** — Component state-coverage rules (loading/error/empty/success — ~7.1 KB).
- **typography.md** — Typography discipline (~3.1 KB).
- **README.md** — Index for the craft/ directory (~4.6 KB).

## Other resources

### Visual directions (5)

5 deterministic OKLch palette + font-stack presets — see [[visual-directions]] for the canonical concept page. The agent picks one when no brand context exists; *no improvisation* allowed.

### Device frames (5 HTML files)

Pixel-accurate device frames in `assets/frames/`:

- **iphone-15-pro.html**
- **android-pixel.html**
- **ipad-pro.html**
- **macbook.html**
- **browser-chrome.html**

Plus README at `raw/open-design/meta/frames-README.md`. The "shared frames" convention prevents agents from inventing different device chrome per render.

### Prompt templates (94 JSON files)

`prompt-templates/` directory contains 44 image-generation + 50 video-generation prompt templates as JSON. Not fetched as raw markdown (they're JSON, not knowledge artifacts in the wiki sense). Names visible via the GitHub UI; categories include 3D-stone-staircase-evolution, anime-martial-arts, e-commerce-live-stream, game-screenshot, ancient-guardian-dragon, decade-of-refinement-glow-up.

### Top-level meta files (8)

- **README.md** (87 KB) — comprehensive project overview.
- **AGENTS.md** (10.7 KB) — the agent contract; same shape as Hermes Agent's AGENTS.md.
- **CLAUDE.md** (11 bytes — likely a one-line redirect to AGENTS.md).
- **CHANGELOG.md** (34.4 KB) — version history.
- **QUICKSTART.md** (14.3 KB) — getting started guide.
- **CONTRIBUTING.md** (17.7 KB) — contribution guide.
- **TRANSLATIONS.md** (14.5 KB) — i18n / localization.
- **frames-README.md** (2.8 KB) — frame-asset documentation.

## Sub-claims and details

### Lineage clarification: anti-ai-slop originated in Refero, was codified in Open Design

The [[anti-ai-slop-machinery]] concept page was written from the [[wiki/sources/nexu-io-open-design|Open Design architectural source]] which characterized the discipline as Open Design's. The canonical `craft/anti-ai-slop.md` clarifies: the discipline was **adapted from `refero_skill`** (MIT-licensed open-source skill by Refero), then *"tightened to match Open Design's lint surface."* The anti-ai-slop concept page should now reflect this: Refero originated the skill, Open Design productionized it with a daemon-level linter (`apps/daemon/src/lint-artifact.ts`).

### Cross-brand observation: 70+ product brands + 60+ design styles is a deliberate split

Open Design's catalog deliberately mixes *real product brands* (Apple, Stripe, Linear, Tesla — pulling from real product surfaces) with *named aesthetic styles* (brutalism, claymorphism, doodle, retro). This is structurally distinct from Refero's catalog which is *brand-only*. Implication: an agent given "design a brutalist landing page" can use the Open Design `brutalism` DESIGN.md without reference to any specific brand. Refero requires picking a brand whose aesthetic happens to match.

### Skill family observation: HTML decks are the largest single skill family

17 of 71 skills (~24%) are `html-ppt-*` deck variants. This is a strong thesis: HTML-as-deck is Open Design's primary differentiated output relative to native PowerPoint generation. The `pptx-html-fidelity-audit` skill is the explicit acknowledgment that the conversion is lossy.

### Orbit family suggests a platform-agent integration architecture

The `orbit-*` skills (general, github, gmail, linear, notion) imply a *platform-integration substrate* in the Open Design daemon. Functionally analogous to MCP servers but skill-shaped — the agent calls an `orbit-github` skill to interact with GitHub rather than calling a github MCP. Worth investigating: are orbits a meaningful alternative to MCPs or just a thin wrapper around them?

### Number alignment: README claims vs live counts

| Claim source | Design systems | Skills |
|---|---|---|
| README (April 2026) | 129 | 31 |
| README (May 2026, archive sentence) | 138 | 64 |
| **Live (this ingest, 2026-05-05)** | **139** | **71** |

The repo ships ~7-10 new design systems and ~7 new skills per recent month. Re-fetching the catalog quarterly is the right cadence.

## Notes

- **The catalog as the wiki coverage**: this page intentionally does NOT spawn 139 individual brand source pages or 71 individual skill source pages. Per the [[wiki/sources/nexu-io-open-design|architectural source]] and the maintainer-mode design discussion (2026-05-05), per-artifact source pages would dilute wiki signal-to-noise. The raw layer + this catalog index is the appropriate level of fidelity. Specific brands or skills can graduate to substantive source pages on-demand.
- **For [[wiki/projects/vedge|Vedge]] specifically**: this catalog gives you instant access to every Open Design surface. For `vedge_landing`, the most relevant skills are `saas-landing` (single-page conversion-optimized landing) and `pricing-page` (the [[ai-seo|AI SEO]]-recommended `/pricing` surface). Most relevant DESIGN.md files: **linear-app** (modern dev-tool feel), **stripe** (trust signaling for billing/claims), **notion** (warm-clinical), **supabase** or **posthog** (developer-friendly dark UI if Vedge needs dev-portal vibes).
- **Cross-cite with [[wiki/concepts/anti-ai-slop-machinery]]**: the canonical `craft/anti-ai-slop.md` is now in `raw/open-design/craft/anti-ai-slop.md` — agents querying the concept can read the actual rules with hex-code blacklists rather than just the wiki summary.
- **Cross-cite with [[wiki/sources/nexu-io-open-design]]**: the architectural overview source is the *what is Open Design* page; this catalog is the *what's in Open Design* page. Together they cover the project comprehensively.

## Mentioned entities

- [[wiki/entities/open-design]] — the platform.
- [[wiki/entities/nexu-io]] — maintainer.
- [[wiki/entities/refero]] — origin of anti-ai-slop discipline (`refero_skill` upstream).
- All 33 brand entities currently in the wiki (substantive coverage from prior ingest cycles).
- *(120+ additional brand entity stubs would map to the 139 brands listed above; not creating en masse — see Notes.)*

## Related concepts

- [[design-md]] — the file format; Open Design's 9-section schema is the richer alternative to Refero's 5-section.
- [[claude-code-skills]] — the SKILL.md mechanism Open Design uses for 71 bundles.
- [[anti-ai-slop-machinery]] — the canonical doc lives at `raw/open-design/craft/anti-ai-slop.md`.
- [[markdown-as-agent-contract]] — instantiated at multiple layers across the catalog.
- [[visual-directions]], [[question-form-first]], [[byok-proxy]], [[artifact-first-workflow]] — concepts derived from the architectural source page.

## Related sources

- [[wiki/sources/nexu-io-open-design]] — companion architectural overview source.
- [[wiki/sources/refero-design-systems-for-ai-agents]] — sibling catalog (smaller, SaaS-distributed via MCP).
- [[wiki/syntheses/refero-open-design-claude-design-comparison]] — three-way comparison synthesis.
