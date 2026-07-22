---
title: "Building software that lasts"
source: "https://x.com/saradu/status/2079695483174551578"
author:
  - "[[@saradu]]"
published: 2026-07-21
created: 2026-07-22
description: "San Francisco is anxious about housing again.Rent in Nob Hill is 57% higher than it was this time last year. $50,000-a-month rentals are sni..."
tags:
  - "clippings"
  - "software-craft"
---
![Image](https://pbs.twimg.com/media/HNyOsG7bsAA6VHO?format=jpg&name=large)

San Francisco is anxious about housing again.

Rent in Nob Hill is 57% higher than it was this time last year. $50,000-a-month rentals are sniped overnight. Recently, a [tweet](https://x.com/evanjconrad/status/2078678912499126325?s=20) petitioning for a billboard that says “Your rent could be $500/mo if we built market rate housing in San Francisco” has garnered thousands of likes.

SF has seen manias like this before, but this high is higher than ever.

![Image](https://pbs.twimg.com/media/HNyMqNma8AAzpAx?format=jpg&name=large)

What’s different this time isn’t just the scale of the rents or the valuations - it’s the scale of speed. Booms have always compressed time; urgency speeds up what people believe is possible. But AI has compressed time further. Revenue curves used to have a slope and now they simply go vertical.

I was at a World Cup party on Sunday and spoke to a few engineers from Cursor. They had been there only eight or nine months, yet all of them said it felt like three years. None of them had experienced time pass like that before.

The output of a boom is easy to spot. New skylines (less so these days, unfortunately), new startups, new products. The volume of software being produced today is hard to comprehend.

But a boom leaves behind more than visible artifacts. It leaves invisible foundations. In cities, that’s the ground beneath the buildings. In software it’s the architecture that future engineers and agents must reason about. At startups and organizations at large, it’s the habits and incentives that determine what’s built and maintained in the future, and even more importantly, what’s allowed to be thrown away. The next generation builds then inherits the foundations, whether they remain sound or not.

## A city built on landfill

In 1848, San Francisco had roughly 1,000 residents. By the end of 1849, it had about 25,000.

This is difficult to picture because cities don’t normally grow that fast. For calibration, SF has 800,000 residents today. A 25× increase would leave the Bay Area with 20 million people by next summer: a Mumbai or Beijing appearing almost overnight.

No city is prepared for growth on that scale. San Francisco was still a fishing village. Its first surveyor had only just finished drawing a neat rectangular grid across the hills before the Gold Rush hit.

There was no time to think, so SF simply grew outwards. Yerba Buena Cove was filled with whatever could create land quickly: sand, rubble, garbage, abandoned ships were thrown in to create the foundations of what Fidi and Rincon Hill now stand on. We still live on top of the garbage.

![Image](https://pbs.twimg.com/media/HNyMtbobgAAU5vJ?format=jpg&name=large)

## A lot of code is landfill

AI coding feels insanely addictive because it feels possible to prompt million-dollar businesses into existence. The demand is real too; the traditional economy aches for AI as much as SF’s residents yearn to build it. Crusty old software that never exposed an API can finally be unlocked with computer use. Industries that once seemed impossible to automate have become fair game overnight.

And the frontier keeps pushing outward. Text and voice agents are only beginning to reach the long tail of the economy. When there’s so much greenfield market to capture, restraint feels irrational.

Historically, tech debt accrued at roughly the speed a team could type. Today, it grows at the speed models can infer. Those speeds differ by orders of magnitude and the difference is compounding: every generated layer becomes the foundation on which the next layer is generated.

This is not an argument that models write bad code though. Much of the code they produce is perfectly good. Some of it is better than what the reviewing engineer would have written.

The problem is that code has become cheaper while patience has become more expensive, especially when customers are waiting and competitors are shipping.

![Image](https://pbs.twimg.com/media/HNyMvpIbgAAKZhT?format=jpg&name=large)

Every line that enters a codebase becomes part of the environment that future humans and agents must reason about. Good foundations require reading patiently, poring over commit history, questioning abstractions, and occasionally deciding that the right answer is actually to delete large swaths of the architecture. All of those things are slower than writing net new code.

That tradeoff becomes especially difficult during a boom. Demoable features and X launches are visible outputs, whereas a weekend spent reading old code is not. Yet the decisions that matter most are often invisible: whether to build something at all, and how to reshape what already exists. Those decisions determine the foundations on which everything else rests.

## It’s hard to delete things

If creation is so cheap, shouldn’t deletion become more valuable?

Deletion, especially by agents, frightens people. When GPT-5.6 Sol began deleting things last week, the [uproar](https://x.com/brunolemos/status/2076769881534398974?s=20) was immediate (of course that’s an extreme and bad example). Deleting code has an unbounded perceived risk profile while adding code rarely feels existential. If a feature is wrong, it can be rewritten. If it contains bugs, they can be patched.

Organizations therefore evolve to reward creation far more than deletion. They measure velocity, celebrate shipped features, and praise output. Few define a reward signal for making a system simpler.

The software ecosystem reinforces this lesson too. No AI code review platform advertises “fewer PRs merged.” They advertise writing more of it, and merging faster. It’s all about more throughput. Case studies from these vendors typically frame the entire problem as code review being a throughput bottleneck: you can generate a million lines of code, but if review only supports a thousand, that’s all you’re shipping. The million lines are treated as latent value to unlock rather than a liability to prune.

Even the vendors sense the trap: in a since-deleted blogpost, CodeRabbit admitted that AI has made it easy for teams to “generate more work than they can comfortably understand,” yet the product still sells faster merges.

Agents inherit these incentives and propagate them while they remain chained to human reviewers and systems.

## Landfill breaks down

During the 1989 Loma Prieta earthquake, parts of SF built on landfill suffered liquefaction. Ground that had carried weight for decades abruptly stopped behaving like ground and large parts of the Marina collapsed.

![Image](https://pbs.twimg.com/media/HNyOMdhaIAAVLWK?format=jpg&name=large)

Software fails in similar ways. Rushed code becomes the foundation for more rushed code. Each layer rests on assumptions that fewer people understand than the one below it. The system may survive perfectly fine for years, but then a migration, an outage, or a security incident puts pressure on many layers at once, and what seemed solid begins to disintegrate.

It would be easy to end the piece here with a simple rule: build slowly if you want things to last. But booms rarely permit that luxury. Delay has an obvious cost; haste often appears free.

The cost of doing so doesn’t just disappear. You’re only changing when you pay the bill. You can pay it upfront by understanding the foundations and the subsequent layers. Or you can pay it afterwards, by deleting and rebuilding what was cheap and flimsy. The mistake is to think you can avoid paying the cost of rushed execution at all.

## Structural impermanence

Tokyo is unusual in that it has been destroyed and rebuilt several times over. Fires, earthquakes, and American firebombing have forged a city with a unique relationship with permanence.

Today, markets reinforce that expectation. A Japanese house loses almost all of its value after 20 years. The land is the asset, the structure is just temporary. The average building in Tokyo lasts 30 years, while in the US, it’s more than double that.

Tokyo, like SF, has also been shaped by booms and frenzied economic development. While the city has become the largest metropolitan area in the world, housing has remained affordable, and is significantly cheaper than in New York, London, Hong Kong, or SF. This is not because of rent control or subsidies. Instead of letting supply dwindle, Tokyo builds frenetically: national zoning law sharply limits local governments’ ability to block development, so individual buildings are routinely torn down and replaced with denser, more useful ones.

But not everything in Tokyo is built to be disposable. The city has expanded significantly thanks to the backbone that is the Tokyo Metro, which makes $500M in annual net profit (whereas BART and Muni are subsidized and not expected to generate profits). While the buildings come and go, the transit system is what makes continual rebuilding, and low rents, possible.

<video preload="none" tabindex="-1" playsinline="" aria-label="Embedded video" poster="https://pbs.twimg.com/amplify_video_thumb/2079691950547218432/img/SLRzEdXnzngdAeCL.jpg" style="width: 100%; height: 100%; position: absolute; background-color: black; top: 0%; left: 0%; transform: rotate(0deg) scale(1.005);"><source type="video/mp4" src="blob:https://x.com/67a2a642-ba62-4d92-aa26-62e144dc85bf"></video>

![](https://pbs.twimg.com/amplify_video_thumb/2079691950547218432/img/SLRzEdXnzngdAeCL.jpg?name=large)

The lesson in Tokyo is that permanence should be earned instead of being a default. Pour concrete only where you’re certain. Build everything else to be temporary, cheap to replace, and easy to rebuild.

## Build slowly or build so it won’t last

Boom times are exhilarating. Everything feels possible and everything happens faster. Time itself seems to speed up, as though the future can be pulled forward by force of will.

Taking your time feels contrarian right now. Even our language reflects it. The most cracked engineers “rip tokens,” and the builders who embrace acceleration are always “maxxing” something.

And the market often rewards the impatient. Revenue doesn’t care about perfect or sustainable architecture, and sometimes the only way to discover the right system is to build it first. But the foundations of a codebase are no cheaper to change because they were laid in haste.

This tradeoff predates LLMs, but agents amplify the consequences of our choices. We’re getting very good at teaching agents how to produce software but we’re much worse at teaching them when not to, or when existing work has outlived its usefulness. Perhaps the missing piece is incentive design: agent teams that become increasingly willing to revisit, simplify, and delete as a codebase matures.

Until then, future won’t be limited by how quickly we can build. It will be limited by how patiently we choose our foundations, and how ruthlessly we’re willing to erase everything else.