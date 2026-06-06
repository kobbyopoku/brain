---
type: source
title: zostaff — 22 Open-Source Repos from Hedge Funds and Quant Firms (Jane Street, Man Group, Two Sigma, etc.)
created: 2026-06-06
updated: 2026-06-06
source_url: https://x.com/zostaff/status/2056351832088207385
source_type: x-thread
author: zostaff (@zostaff)
source_date: 2026-05-18
raw_path: raw/22 Open Source Repos from Hedge Funds and Quant Firms. Jane Street , Man Group,Two Sigma, etc..md
content_status: substantive-verbatim
tags: [open-source, hedge-fund, quant, github, time-series, data-engineering, ocaml, jupyter, recruiting-brand, competitive-moat]
---

# zostaff — 22 Open-Source Repos from Hedge Funds and Quant Firms (Jane Street, Man Group, Two Sigma, etc.)

> An X-thread catalog of 22 GitHub repositories open-sourced by 7 elite quant/hedge-fund firms (Two Sigma, Man Group, Jane Street, D.E. Shaw, Hudson River Trading, Optiver, WorldQuant), framed around the thesis that whether a firm open-sources its stack maps onto whether its competitive moat is *people* (open up, recruit PhDs) or *alpha* (lock everything down).

## TL;DR

zostaff surveys the public GitHub footprint of the world's top quant firms and finds a sharp split: 7 firms put part of their stack on GitHub (mostly MIT / Apache 2.0 / BSD), while the most secretive — Renaissance Technologies, Citadel, Bridgewater, Millennium, Point72, AQR — publish essentially nothing. The 22 repos cluster into data/time-series tooling (ArcticDB, flint, dtale), researcher productivity (beakerx, pyflyby, notebooker), low-level systems (Jane Street's OCaml stack, HRT's C++/SystemVerilog tools), and quant research (WorldQuant's community-implemented 101 Formulaic Alphas). The load-bearing analytical claim: open-vs-closed isn't random — it maps onto whether a firm's edge is the people it hires or the alpha it discovers.

## Key takeaways

- **The open/closed split maps onto the firm's moat.** If the edge is *people you hire* → open the code to attract more PhDs (Two Sigma, D.E. Shaw, Jane Street, HRT). If the edge is *alpha you discover* → close everything to deny hints to competitors (Renaissance, Citadel, Bridgewater).
- **Open source as a recruiting brand.** Jane Street explicitly treats public code as a recruiting strategy — "30 million lines of code, almost 1 million public on GitHub… This isn't a leak, it's a recruiting strategy." magic-trace's 5,300 stars signal to every infrastructure engineer where to send a CV.
- **Jane Street is the largest commercial user of OCaml in the world** and wrote "half of the OCaml ecosystem"; its `core` library is the de-facto OCaml standard-library replacement that downstream OCaml users depend on whether they know it or not.
- **Man Group's open-sourcing is partly downstream of monetization**: Bloomberg licensed ArcticDB from Man Group, so the remaining IP exposure is low and open source becomes marketing for a publicly listed firm needing to "look modern to attract institutional money."
- **ArcticDB is the one non-permissive repo** — Business Source License (BSL), free for non-production use, paid for commercial deployment. Everything else in the list is MIT / Apache 2.0 / BSD.
- **Quant tooling has crossed into mainstream tech**: Two Sigma's `cook` scheduler is used by Twitter, Apple, and Indeed; D.E. Shaw funded the development of IPython, Jupyter, and NumPy.
- **The repos cluster by function** — time-series/data (flint, ArcticDB, dtale), researcher productivity (beakerx, pyflyby, notebooker, PyBloqs, marbles), low-level systems (Jane Street OCaml stack, HRT corral/slang-server, optiver timestamp9/asyncpg), and quant research (WorldQuant alpha101).
- **The "silent" firms are themselves informative.** Renaissance Technologies (~$130B AUM, ~66% annual returns for three decades) has zero public repos and bars former employees from writing detailed resumes; Citadel, Bridgewater, Millennium, Point72/Cubist publish nothing; AQR has only a pandas fork.
- **WorldQuant's actual GitHub is nearly empty** — its influence is the *paper* "101 Formulaic Alphas," the most-cited quant work of the last decade, which the community (yli188) implemented on GitHub.
- **Latency-driven engineering shows in the tooling choices**: HRT writes trading infra in C++20 structured-concurrency (corral) for microsecond latency; Optiver builds nanosecond Python timestamps (timestamp9) and forks asyncpg for tick-write speed psycopg2 can't reach; D.E. Shaw rewrote nbstripout in Rust because the Python version was too slow at their scale.
- **Scale anchors cited**: Jane Street posted $16.1B trading revenue in Q1 2026 and moved $2T equity volume/month in 2024; HRT executes up to 5% of all U.S. equity trades daily and reported $6.4B Q1 2026 revenue (+135% YoY).

## Notable quotes

> "The most secretive industry in the world keeps its code under lock and key. But 7 funds and quant firms from the top of the league decided otherwise and put part of their stack on GitHub. Their tools power many firms and almost the entire OCaml ecosystem."

> "Jane Street, the largest commercial user of OCaml in the world. 30 million lines of code. Almost 1 million of them public on GitHub. They wrote half of the OCaml ecosystem. This isn't a leak, it's a recruiting strategy."

> "If your edge is the people you hire: open up the code, attract more PhDs. If your edge is the alpha you discover: close everything, keep the signals proprietary. … Two Sigma believes a smart researcher with great tools beats an average researcher with secret tools. Renaissance believes the opposite. Both have been right for 25+ years and counting."

## Notes

- **The catalog as a list of practical, adoptable tools.** Beyond the hedge-fund framing, many of these repos are directly usable infrastructure for any data-heavy product. For Godwin's products that handle time-series / tabular data at scale ([[wiki/projects/vedge|Vedge]], [[wiki/projects/kivora|Kivora]]), `dtale` (browser DataFrame explorer), `notebooker` (Jupyter-as-scheduled-reporting), `PyBloqs` (HTML reports from Python without a frontend), and `pyflyby` (auto-import for notebooks) are the most transplantable. ArcticDB is interesting for serverless time-series-in-S3 but the BSL license is a commercial blocker.
- **The moat-mapping thesis is the genuinely portable insight** and generalizes beyond quant: an organization's willingness to open-source is a signal about *where it believes its defensibility lives* — in talent/distribution (open) vs. in a proprietary secret (closed). Worth holding next to the [[wiki/concepts/ai-automation-services|AI services]] vs proprietary-product strategic question that recurs across Godwin's portfolio.
- **Numbers should be treated as source-reported, not verified.** AUM figures, trading-revenue figures, return percentages, and star counts are as zostaff states them (mid-2026); they are plausible but uncited to primary filings. Flag for re-check before any are reused as facts elsewhere.
- **One garbled line in the raw**: the notebooker entry reads "run daily analytics for managers of ." (a dropped figure) — the missing AUM-managed number is not recoverable from the source.
- **Author is promotional** — the post ends with a Polymarket referral link and a Telegram channel; zostaff appears to be a finance/markets content creator. The repo catalog itself is the load-bearing content; the framing essay (open vs closed moats) is the interpretive value-add.
- **Adjacency to an existing wiki source.** This is structurally a sibling of [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — both are curated "N open-source repos you should know" catalogs — but with a quant-finance lens and an explicit strategic thesis rather than a role-replacement framing.

## Mentioned entities

- [[wiki/entities/zostaff]] — author of the thread; finance/markets content creator (Polymarket referral, Telegram channel).
- [[wiki/entities/two-sigma]] — quant firm (~$70B AUM); 4 repos (flint, beakerx, marbles, cook).
- [[wiki/entities/man-group]] — largest publicly listed hedge fund (~$228.7B AUM); 4 repos (ArcticDB, dtale, notebooker, PyBloqs).
- [[wiki/entities/jane-street]] — largest commercial OCaml user; 4 repos (core, magic-trace, async, hardcaml).
- [[wiki/entities/d-e-shaw]] — quant fund (~$90B AUM); 4 repos (pyflyby, pjrmi, versioned-hdf5, nbstripout-fast).
- [[wiki/entities/hudson-river-trading]] — HFT firm (~$20B trading capital); 3 repos (corral, slang-server, heracles-ql).
- [[wiki/entities/optiver]] — Amsterdam options market maker; 2 repos (timestamp9, optiver-asyncpg).
- [[wiki/entities/worldquant]] — quant fund (~$9B AUM); BRAIN crowdsourced-alpha platform; "101 Formulaic Alphas" paper.
- [[wiki/entities/renaissance-technologies]] — secretive quant fund (~$130B AUM, ~66% returns); zero public repos.
- [[wiki/entities/citadel]] — hedge fund / market maker (~$65B); no official GitHub.
- [[wiki/entities/bridgewater-associates]] — hedge fund (~$100B AUM); zero repos.
- [[wiki/entities/millennium-management]] — hedge fund (~$70B AUM); zero repos.
- [[wiki/entities/point72]] — hedge fund (~$35B AUM, incl. Cubist Systematic); zero repos.
- [[wiki/entities/aqr-capital]] — quant fund (~$99B AUM); GitHub holds only a pandas fork.
- [[wiki/entities/arcticdb]] — Man Group serverless time-series database; BSL license; Bloomberg licensee.
- [[wiki/entities/dtale]] — Man Group's browser DataFrame explorer (Excel-on-pandas); most-starred Man Group repo.
- [[wiki/entities/notebooker]] — Man Group tool turning Jupyter into a scheduled reporting engine.
- [[wiki/entities/pybloqs]] — Man Group library generating HTML reports from Python without a frontend.
- [[wiki/entities/flint]] — Two Sigma time-series joins on Apache Spark with temporal tolerance.
- [[wiki/entities/beakerx]] — Two Sigma polyglot Jupyter (Python/Scala/Groovy/Kotlin/Clojure/Java in one notebook).
- [[wiki/entities/marbles]] — Two Sigma unit-test library with plain-English failure explanations.
- [[wiki/entities/cook]] — Two Sigma batch scheduler on Mesos/Kubernetes; used by Twitter, Apple, Indeed.
- [[wiki/entities/janestreet-core]] — Jane Street's alternative OCaml standard library.
- [[wiki/entities/magic-trace]] — Jane Street high-resolution process tracer (Intel Processor Trace); most-starred Jane Street repo.
- [[wiki/entities/janestreet-async]] — Jane Street cooperative-concurrency OCaml library.
- [[wiki/entities/hardcaml]] — Jane Street OCaml library for hardware design (FPGA/ASIC).
- [[wiki/entities/pyflyby]] — D.E. Shaw auto-import for IPython/Jupyter.
- [[wiki/entities/pjrmi]] — D.E. Shaw Python↔Java RPC with no glue code.
- [[wiki/entities/versioned-hdf5]] — D.E. Shaw version control for HDF5 files (built with Quansight Labs).
- [[wiki/entities/nbstripout-fast]] — D.E. Shaw Rust rewrite that strips Jupyter outputs before git commits.
- [[wiki/entities/corral]] — HRT structured concurrency for C++20.
- [[wiki/entities/slang-server]] — HRT SystemVerilog language server (LSP).
- [[wiki/entities/heracles-ql]] — HRT Python DSL for alerts.
- [[wiki/entities/timestamp9]] — Optiver nanosecond timestamps for Python.
- [[wiki/entities/optiver-asyncpg]] — Optiver production fork of asyncpg (fast asyncio PostgreSQL client).
- [[wiki/entities/worldquant-alpha101-code]] — yli188's community implementation of WorldQuant's 101 alpha formulas.
- [[wiki/entities/apache-spark]] — distributed compute engine flint builds on.
- [[wiki/entities/jupyter]] — notebook platform underlying beakerx, notebooker, pyflyby, nbstripout-fast; D.E. Shaw funded its development.
- [[wiki/entities/ocaml]] — functional language; Jane Street's primary stack and the ecosystem it dominates.
- [[wiki/entities/bloomberg]] — licensed ArcticDB from Man Group.
- [[wiki/entities/quansight-labs]] — co-developer of versioned-hdf5.

## Related concepts

- [[wiki/concepts/competitive-moat]] — the load-bearing thesis: open-vs-closed source maps onto whether the firm's moat is talent or proprietary alpha.
- [[wiki/concepts/open-source-as-recruiting]] — open-sourcing internal tooling as a talent-acquisition / employer-brand strategy (Jane Street, Two Sigma, D.E. Shaw, HRT).
- [[wiki/concepts/time-series-data-engineering]] — recurring problem domain across the catalog (flint, ArcticDB, dtale, timestamp9).

## Related sources

- [[wiki/sources/heynavtoor-10-repos-replace-eng-team]] — sibling "curated open-source repos" catalog; role-replacement framing vs this source's quant-firm + strategic-moat framing.
