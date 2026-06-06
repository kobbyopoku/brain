---
title: "22 Open Source Repos from Hedge Funds and Quant Firms. Jane Street , Man Group,Two Sigma, etc."
source: "https://x.com/zostaff/status/2056351832088207385"
author:
  - "[[@zostaff]]"
published: 2026-05-18
created: 2026-05-21
description: "Two Sigma, Man Group, Jane Street, D.E. Shaw, Hudson River Trading, Optiver, WorldQuantRenaissance Technologies, a fund averaging 66% annual..."
tags:
  - "hedge-fund"
  - "hedge"
  - "opensource"
  - "repo"
---
![Image](https://pbs.twimg.com/media/HIjzMH3XcAECS86?format=jpg&name=large)

## Two Sigma, Man Group, Jane Street, D.E. Shaw, Hudson River Trading, Optiver, WorldQuant

**Renaissance Technologies, a fund averaging 66% annual returns for three decades, has zero public repositories.**

**Citadel, with $65 billion in assets. Zero.**

**Bridgewater. Millennium. Point72. Also zero.**

The most secretive industry in the world keeps its code under lock and key. But 7 funds and quant firms from the top of the league decided otherwise and put part of their stack on GitHub. Their tools power many firms and almost the entire OCaml ecosystem.

**I went through everything they released. Here are 22 repositories from companies that move hundreds of billions of dollars in trades every day.**

```text
| Firm | What they manage | Repos in this article |
|---|---|---|
| Two Sigma | $70B AUM | 4 |
| Man Group | $228.7B AUM | 4 |
| Jane Street | $39.6B trading revenue (2025) | 4 |
| D.E. Shaw | $90B AUM | 4 |
| Hudson River Trading | $20B trading capital | 3 |
| Optiver | Global options market maker | 2 |
| WorldQuant | $9B AUM | 1 |
```

Almost everything below is under MIT, Apache 2.0, or BSD. The single exception: ArcticDB from Man Group uses the Business Source License (BSL), free for non-production use, paid license required for commercial deployment.

## Two Sigma ($70B AUM)

**Two Sigma only hires PhDs from MIT, Stanford, and CMU. Their engineers wrote tools that ended up powering Twitter, Apple, and Indeed. Here are 4 of them.**

**1\. twosigma/flint, 1k stars,** [https://github.com/twosigma/flint](https://github.com/twosigma/flint)

Time-series joins on top of Apache Spark with temporal tolerance. When you have billions of ticks and need to "find the nearest quote for every trade", this is the only sane option.

**2\. twosigma/beakerx, 2.8k stars,** [https://github.com/twosigma/beakerx](https://github.com/twosigma/beakerx)

Jupyter where Python, Scala, Groovy, Kotlin, Clojure, and Java all run in the same notebook. Two Sigma built this because their researchers use 5 languages in parallel.

**3\. twosigma/marbles, 116 stars,** [https://github.com/twosigma/marbles](https://github.com/twosigma/marbles)

Unit tests that explain why they failed in plain English, not a stack trace. If you're tired of reading pytest output, try this.

**4\. twosigma/cook, 338 stars,** [https://github.com/twosigma/cook](https://github.com/twosigma/cook)

Batch job scheduler on top of Mesos/Kubernetes. Two Sigma runs simulations on it that would crash any normal scheduler. Twitter, Apple, and Indeed use it too.

## Man Group / AHL ($228.7B AUM)

**Man Group, the largest publicly listed hedge fund in the world. Bloomberg paid them to license one of their databases. The same database sits on GitHub. Plus 3 more tools.**

**5\. man-group/ArcticDB, 2.3k stars,** [https://github.com/man-group/ArcticDB](https://github.com/man-group/ArcticDB)

The database Bloomberg bought from Man Group. Stores billions of rows of time-series data in S3 with no server. Pandas in, pandas out. If you still keep ticks in CSV, you should be embarrassed.

License: BSL, free for non-commercial use.

**6\. man-group/dtale, 5.1k stars,** [https://github.com/man-group/dtale](https://github.com/man-group/dtale)

Excel on top of pandas DataFrames in your browser. One line of code and you get an interface with filters, correlations, and charts. The most starred Man Group repo by a wide margin.

**7\. man-group/notebooker, 900 stars,** [https://github.com/man-group/notebooker](https://github.com/man-group/notebooker)

Turns Jupyter into a scheduled reporting engine. AHL uses it to run daily analytics for managers of . You can use it to run reports for your startup.

**8\. man-group/PyBloqs, 183 stars,** [https://github.com/man-group/PyBloqs](https://github.com/man-group/PyBloqs)

HTML reports from Python with no frontend. Tables, charts, layout: all assembled in blocks. Stop making "pretty presentations" in PowerPoint by hand.

## Jane Street ($39.6B trading revenue in 2025)

**Jane Street, the largest commercial user of OCaml in the world. 30 million lines of code. Almost 1 million of them public on GitHub. They wrote half of the OCaml ecosystem. This isn't a leak, it's a recruiting strategy. Here are 4 repos from the firm that just posted $16.1B in trading revenue for Q1 2026 alone.**

**9\. janestreet/core, 1.2k stars,** [https://github.com/janestreet/core](https://github.com/janestreet/core)

The alternative OCaml standard library. What Jane Street uses instead of stdlib across their entire codebase. If you write OCaml, you already depend on Core, even if you didn't know it.

**10\. janestreet/magic-trace, 5.3k stars,** [https://github.com/janestreet/magic-trace](https://github.com/janestreet/magic-trace)

High-resolution process tracer powered by Intel Processor Trace. When your profiler can't find the bug, magic-trace shows every CPU instruction the process executed. The most starred Jane Street repo.

**11\. janestreet/async, 233 stars,** [https://github.com/janestreet/async](https://github.com/janestreet/async)

Cooperative concurrency in OCaml. The foundation of Jane Street's entire trading infrastructure, which moved $2 trillion in equity volume per month in 2024.

**12\. janestreet/hardcaml, 1k stars,** [https://github.com/janestreet/hardcaml](https://github.com/janestreet/hardcaml)

OCaml library for hardware design (FPGA, ASIC). Yes, they write chips in OCaml. Because they can.

## D.E. Shaw ($90B AUM)

**D.E. Shaw, the fund where Jeff Bezos worked before leaving to start Amazon. They funded the development of IPython, Jupyter, and NumPy. And they released their internal tools.**

**13\. deshaw/pyflyby, 409 stars,** [https://github.com/deshaw/pyflyby](https://github.com/deshaw/pyflyby)

Auto-import for IPython and Jupyter. Forgot to write \`import pandas as pd\`, pyflyby drops it in for you. When you have 50 notebooks a day, this saves hours.

**14\. deshaw/pjrmi, 47 stars,** [https://github.com/deshaw/pjrmi](https://github.com/deshaw/pjrmi)

RPC between Python and Java with no glue code. D.E. Shaw wrote this so their Python researchers could call Java services directly. Turns Java into a Python extension.

**15\. deshaw/versioned-hdf5, 89 stars,** [https://github.com/deshaw/versioned-hdf5](https://github.com/deshaw/versioned-hdf5)

Version control for HDF5 files (git, but for scientific data). Built jointly with Quansight Labs. When you have terabytes of ticks and need to roll back to "yesterday's version" of the dataset.

**16\. deshaw/nbstripout-fast, 29 stars,** [https://github.com/deshaw/nbstripout-fast](https://github.com/deshaw/nbstripout-fast)

Strips outputs from Jupyter notebooks before git commits. Written in Rust because the original Python version was too slow for D.E. Shaw's scale.

## Hudson River Trading ($20B trading capital)

**HRT executes up to 5% of all U.S. equity trades. Every single day. They just reported $6.4B in trading revenue for Q1 2026, a 135% year-over-year jump. They write in C++, FPGA, and SystemVerilog, and they released some of that tooling publicly.**

**17\. hudson-trading/corral, 175 stars,** [https://github.com/hudson-trading/corral](https://github.com/hudson-trading/corral)

Structured concurrency for C++20. Coroutines without pain. HRT writes their trading infrastructure on this, the kind that demands microsecond latency.

**18\. hudson-trading/slang-server, 224 stars,** [https://github.com/hudson-trading/slang-server](https://github.com/hudson-trading/slang-server)

SystemVerilog language server. HRT designs FPGA chips for trading, and they needed a good LSP for Verilog. Didn't find one, wrote their own.

**19\. hudson-trading/heracles-ql, 27 stars,** [https://github.com/hudson-trading/heracles-ql](https://github.com/hudson-trading/heracles-ql)

A Python DSL for alerts. When you have hundreds of latency-sensitive services in production, regular Prometheus isn't enough.

## Optiver (global options market maker)

**Optiver, an Amsterdam-based market maker, trades options worldwide. Their infrastructure tools are tuned for nanosecond precision because in options, every microsecond is money.**

**20\. optiver/timestamp9, 65 stars,** [https://github.com/optiver/timestamp9](https://github.com/optiver/timestamp9)

Nanosecond timestamps for Python. When \`time.time()\` rounds to milliseconds and you lose trades because you can't distinguish event order.

**21\. optiver/optiver-asyncpg, production fork,** [https://github.com/optiver/optiver-asyncpg](https://github.com/optiver/optiver-asyncpg)

Their fork of asyncpg, the fast PostgreSQL client for asyncio. Used in production to write ticks at latencies psycopg2 can't reach.

## WorldQuant ($9B AUM)

**WorldQuant, the fund that turned alpha research into crowdsourcing through their BRAIN platform. Their official GitHub is almost empty. But their paper "101 Formulaic Alphas" is the most cited work in the quant industry over the last 10 years, and the community coded it up on GitHub.**

**22\. yli188/WorldQuant\_alpha101\_code, 748 stars,** [https://github.com/yli188/WorldQuant\_alpha101\_code](https://github.com/yli188/WorldQuant_alpha101_code)

Community implementation of all 101 alpha formulas from WorldQuant's legendary paper. This is what junior quants at hedge funds use to learn how alpha researchers think. Forked into dozens of real strategies.

## And what about the silent ones?

The list of firms that publish nothing is just as informative:

- Renaissance Technologies (~$130B AUM, 66% annual returns): zero public repos. Employees aren't even allowed to discuss their work in detail.
- Citadel / Citadel Securities (~$65B AUM): no official GitHub account, anything that looks like "Citadel" on GitHub belongs to other projects.
- Bridgewater Associates (~$100B AUM): zero.
- Millennium Management (~$70B AUM): zero.
- Point72 / Cubist Systems (~$35B AUM): zero.
- AQR Capital (~$99B AUM): formally has an account, but it contains only a pandas fork. Effectively nothing.

Why do some firms share while others lock everything down?

**The answer comes in three patterns:**

- Two Sigma, D.E. Shaw, Jane Street, and HRT treat open source as a recruiting brand. Their engineers come for interesting problems, and public code is the showcase. When Jane Street published magic-trace and got 5,300 stars, every infrastructure engineer who used it now knows where to send a CV.
- Man Group opened their tools because Bloomberg already licensed their main IP (ArcticDB). The rest is essentially marketing: they're a publicly listed company that needs to look modern to attract institutional money.
- Renaissance, Citadel, Bridgewater believe any public code = a hint to competitors. Renaissance doesn't even allow former employees to write detailed resumes about what they worked on. Their NDAs are textbook airtight.

## What this tells us about the industry

**The split between "open" and "closed" funds isn't random. It maps almost perfectly onto how each firm thinks about its competitive moat:**

1. If your edge is the people you hire: open up the code, attract more PhDs.
2. If your edge is the alpha you discover: close everything, keep the signals proprietary.

Two Sigma believes a smart researcher with great tools beats an average researcher with secret tools. Renaissance believes the opposite. Both have been right for 25+ years and counting.

# My resources:

## Trading here: https://polymarket.com/?r=zostaff

## My Telegram channel: https://t.me/zostaffsmartarc My GitHub: https://github.com/zostaff