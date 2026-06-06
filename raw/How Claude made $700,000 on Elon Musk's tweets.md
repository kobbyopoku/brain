---
title: "How Claude made $700,000 on Elon Musk's tweets"
source: "https://x.com/RetroChainer/status/2056283744802070766"
author:
  - "[[@RetroChainer]]"
published: 2026-05-18
created: 2026-05-21
description: "On an ordinary day, Elon Musk posted a tweet.Nothing unusual. He does it several times a day.But for a trader known as Aniki, that moment be..."
tags:
  - "claude"
---
![Image](https://pbs.twimg.com/media/HIdawTgWcAAJgT7?format=jpg&name=large)

# On an ordinary day, Elon Musk posted a tweet.

Nothing unusual. He does it several times a day.

But for a trader known as Aniki, that moment became a trade. Then another. Then another.

The result: **$700,000+ in net profit** on markets where people bet on how many tweets Musk posts in a week.

Most people hear this and assume the same thing: "he just guesses how many times Musk will tweet."

They're wrong. And that misunderstanding is exactly why they lose money.

## Part I: What These Markets Actually Are

Polymarket runs markets on real-world events. One of the most active formats: Elon Musk's weekly tweet count.

The structure is simple. The market splits into ranges:

- Fewer than 50 tweets?
- 50–75?
- 75–100?
- More than 200?

Each range is a separate contract. If "100–125 tweets" trades at **$0.34**, the market believes there's a 34% chance that's what happens.

The winner picked the correct range. Their share settles at **$1.00**. Everyone else loses.

Most participants play exactly this way: pick a range, place a bet, wait for the outcome.

Aniki played a completely different game.

**Key takeaway:** These markets aren't just prediction contests. They're order books with spreads, liquidity, and exploitable structure if you know where to look.

## Part II: Market Making Earning From the Act of Trading, Not the Outcome

Aniki's primary income source wasn't predicting Musk's tweets.

It was **market making**.

Every tweet market has 30 price ranges. Each range has an order book a list of buy and sell orders. Aniki simultaneously posted orders on **both sides** of the book across all 30 ranges at once.

The mechanics:

- Someone wants to buy a contract at $0.35 → Aniki sells at $0.36
- Someone wants to sell a contract at $0.33 → Aniki buys at $0.34

The difference is the **spread**. On each pair of trades, a few cents go to Aniki.

One cent sounds like nothing. But Aniki was executing between **1,700 and 2,900 trades** within a single weekly market cycle. Most trades were under $1. Some were under 10 cents.

In aggregate: stable, predictable income. Every week. Regardless of what Musk actually tweeted.

Aniki wasn't betting on the outcome. **He was the casino.**

**Key takeaway:** Market making extracts value from other people's trading activity, not from predicting the right outcome. The spread is the edge. Volume is the engine.

## Part III: Why This Cannot Be Done Manually

Maintaining live orders across 30 ranges simultaneously, reacting to market shifts faster than other participants, recalculating position sizes in real time this happens too fast for a human.

Aniki ran a **trading bot** connected to Polymarket's API. The system operated 24/7 without interruption.

The bot's logic, decision-making rules, and adaptation to changing conditions were all built with **Claude** used not as a chatbot, but as an infrastructure tool.

When you need to describe in plain language how the system should behave at extreme ranges, how to respond to anomalous trading volume, or how to recalculate positions when liquidity shifts Claude translates those descriptions into working code.

No development team. No months of programming.

The bot handled the execution. Claude handled the logic. The system ran continuously.

**Key takeaway:** This strategy is only possible at scale with automation. The bot isn't a shortcut it's the product. Without it, the edge disappears.

## Part IV: The "Lottery Ticket" Layer When Musk Does the Impossible

Market making is the foundation. Stable, reliable, slightly boring.

Aniki had a second layer. And it's where the most extraordinary results came from.

The extreme ranges in any tweet market "fewer than 10 tweets this week" or "more than 500" are priced very cheaply. The market considers them near-impossible. Sometimes the price is fractions of a cent.

Aniki quietly accumulated positions in these ranges.

These weren't large bets. They were **cheap options on the impossible.**

Sometimes Musk goes silent for days. Sometimes something happens that triggers a tweet storm. Sometimes the 1% outcome actually occurs.

When it did, Aniki's cheap positions paid **360x and 400x** the amount invested.

This isn't luck. It's architecture.

**Key takeaway:** Extreme-range positions cost almost nothing and can return multiples of hundreds. The expected value is positive precisely because everyone else ignores them.

## Part V: The Strategy Has a Name Nassim Taleb Described It First

The philosopher and trader Nassim Taleb formalized this approach long before Aniki applied it on Polymarket.

It's called the **Barbell Strategy**:

- **One side of the barbell:** the bulk of capital operates in maximally conservative mode market making, stable income, minimal risk.
- **Other side:** a small portion goes into positions with asymmetric risk profiles cheap, near-hopeless, but capable of returning hundreds of multiples on a rare event.
- **The middle is empty.** No "moderate" bets with "moderate" risk. Only stability plus antifragility.

That's exactly what Aniki executed. Every week. On every market.

**Key takeaway:** This isn't a trading hack. It's a named, documented strategy used by professional traders worldwide. The math behind it is solid.

## Part VI: The Math That Makes It Work

Two frameworks govern this strategy.

**Market making Kelly Criterion:**

f\* = (p × b - q) / b

Where p = probability of profitable trade, b = payout ratio, q = 1 - p.

In market making, p is high, b is small but consistent. Kelly says: **trade often, size small, protect capital.**

**Lottery tickets the formula flips:**

p is negligible. b is enormous. Kelly says: **bet almost nothing but bet.**

Together, these two layers build a system that **cannot completely fail.**

Market making protects capital week after week. Extreme positions create the potential for nonlinear growth when reality diverges from consensus.

Steady profit every week. Plus the occasional explosion that changes everything.

**Key takeaway:** The math isn't theoretical decoration it's the operating logic. Kelly Criterion tells you exactly how much to risk at each layer. The combination of layers is why the system is durable, not just occasionally profitable.

## Part VII: Can Anyone Replicate This?

To be direct: **replicating Aniki's exact setup is not possible for most people.**

Not because it's secret. Because it requires:

- A trading bot with real-time access to Polymarket's API
- Enough capital to maintain liquidity across all 30 ranges simultaneously
- Continuous system uptime 24 hours a day, 7 days a week
- The ability to build and maintain the infrastructure

Claude + the right prompt is not magic. It's infrastructure. And infrastructure needs to be built, configured, and maintained.

**But the principle works.**

Market making on prediction markets is a real strategy with real mathematical foundations. For those without Aniki's full setup, simpler systematic approaches exist for example, betting NO on heavy favorites, selected through backtests across dozens of markets. Less spectacular in scale. But structurally sound.

**Key takeaway:** The strategy is not secret. The barrier is infrastructure and capital, not information. The principles are available to anyone willing to build.

## The Bottom Line

Aniki didn't predict Musk's tweets.

He built a machine that earned money from the **act of other people trading**, while holding cheap positions on the off chance that the impossible happened.

The bot executed thousands of trades per week. Claude processed the logic. The system ran without stopping.

**$700,000+ in net profit is not a lucky outcome.**

It's what happens when someone asks the right question not "what will Musk tweet?" but "how do I earn regardless of what he tweets?"

This is the first article in a series on systematic strategies for prediction markets.

More analysis, breakdowns, and frameworks in the channel: [t.me/+U\_dHNSnUHCcxMDIy](https://t.me/+U_dHNSnUHCcxMDIy) All thanks to this tool: [t.me/poly\_parlay\_bot?start=RETROCHAINE](https://t.me/poly_parlay_bot?start=RETROCHAINE)