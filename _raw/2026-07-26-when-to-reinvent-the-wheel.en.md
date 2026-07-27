---
layout: post
title: "Coding in Mid-2026"
excerpt: "A personal look at the latest coding models, agent workflows, when to fork and extract third-party code, and why human learning is now the real bottleneck."
date: 2026-07-26
lang: en
published: true
---

TL;DR:

- Agents are dominating the coding landscape.
- Reinventing the wheel - forking and extracting what you need - is becoming the better practice.
- Optimizing for learning has become the key to success in vibe coding.
- Learn the basics, understand system design, avoid overengineering, and refactor in a timely manner.
- Avoid FOMO, focus on what matters.
- Models are improving fast, but humans are improving even faster.

## The current state of the art in coding models


Note: I started this draft on June 21, 2026, but only found the time to publish it today.

It has been a while since I last wrote about vibe coding. Almost exactly one year ago, I was bragging about writing one million lines of code with Cursor in half a year. I didn't share more about it partly because I've been so busy with work and partly because coding with agents has become the industry standard. However, I haven't stopped vibe coding. I've coded a hell of a lot more as the models have gotten better and better.

What's the current state of the art in coding models?

First of all, what's the best coding model? Fable? GPT-5.6 Sol? Opus 5? It's a highly subjective question, and I'm going to share my view from a historical perspective.

- At one point, Opus 4.5 was far ahead of anything else on the market. GPT-5.0 through GPT-5.2 were basically garbage. At that point, people started to believe that Anthropic would dominate the future of AI.
- The trend continued for a while, until Anthropic became so short on compute that it started to quantize its models aggressively, which made people seek alternatives. At that time, it had not yet signed the deal with xAI/SpaceX to rent compute.
- Gemini 3 was still useful for debugging a few complicated cases, but unfortunately, Google had gone too long without updating its models. Gemini 3.5 Pro was stuck in hell. Even worse, people were leaving - Noam Shazeer, John Jumper, and a few VPs I've worked with.
- Back in Q1, I relied heavily on Opus 4.5 but definitely hated the degradation caused by model quantization. GPT-5.3 Codex started to catch my attention. It worked surprisingly well, despite complaints about the product lineup and confusing model names (GPT-5.3 and GPT-5.3 Codex were separate models).
- Then OpenAI made changes. They realized that they needed to make coding their primary battlefield. They abandoned Sora and focused all their compute on Codex. They also unified the model release under GPT-5.4, which was indeed a great model that brought them back into the game.
- Then came GPT-5.5, a phenomenal model with which I've written most of my code. It is so token-efficient. It is so good at GitHub Actions. It is so good at reasoning. It is so good at terminal CLIs. It hallucinates much less. I'd say it was definitely the best coding model of its time.
- But it is not omnipotent: it writes terrible frontend code. This used to seem like less of a problem, but no vibe coder can resist the temptation to build a frontend for visualization.
- Mythos/Fable 5 seems to have changed the game again. I'd say the delayed release really gave OpenAI some time to catch up. It is definitely NOT AGI. Not even close. The mystery around it can easily disappoint people when they set the bar too high. It is indeed a good model. It is definitely much more capable than Opus 4.8. I do not think it outperforms GPT-5.5 in most domains, but it definitely does in many of them.
- But it is so slow. It was also banned :)
- (Update on July 26: it's available again, and Opus 5 is also out.)
- Then came GPT-5.6 Sol, which significantly improved its frontend coding ability.
- Kimi K3, a 2.8T-parameter model, is another atom bomb in the coding world.
- Then came Opus 5, whose speed and quality made Opus competitive again.
- So my personal rating for coding models is: GPT-5.6 Sol >= Opus 5 > Fable 5.


## The harness

Now that we've covered the models, it's time to discuss current trends in agent harnesses.
- Cursor, the leading agent-harness platform, was caught in Claude's stranglehold, turned desperately to Kimi 2.5, and became mired in that transition. SpaceX ended up buying it amid the IPO craze, when $60 billion was small relative to SpaceX's valuation. It was definitely a great deal for both sides.
- Claude Code has definitely captured most of the market. It's indeed phenomenal. I personally still love using Cursor, but I have to acknowledge the greatness of Claude Code.
- Then came the main battle between Claude Code and Codex. Both are aiming for the same market. Both offer a CLI, a VS Code extension, cloud agents, and a desktop app.
- Desktop apps are definitely a great invention. But I have to say that both are still improving. Claude Cowork's hallucinations make it completely unusable. But Claude Cowork definitely has a first-mover advantage in features, whereas the Codex app is further ahead in usability.
- I've genuinely enjoyed using the Codex app for multiple tasks: coding, planning, slides, Slack bots, etc. Clearly, the Codex app wins this battle.

It's time to talk about the true topic - the workflow.
- People have been talking about goals, loops, and now graphs. I think those are fancy terms that miss the essence. Frontier models already have the capability to deliver those results if you know what you want.
- Take me as an example: I usually don't know exactly what I want until I see an MVP. I never trust design docs, despite spending four years at Google immersed in design-doc culture. They do not work in this new world. It is just much more efficient to build something first, try it, and iterate. I don't believe you can predict all the bugs or bottlenecks until you build something.

To me, the harness itself is not the true focus. It will soon become a dead end - what matters is mastering the skill of expressing your intent in any format. As turning intent into code gets cheaper, one of software engineering's oldest rules starts to break down: don't reinvent the wheel.


## Reinventing the wheel


On the one hand, you should not reinvent the wheel if a third-party library does exactly what you need. On the other hand, owning the code gives you more control and lets you iterate much faster instead of anxiously waiting for the next release, which may introduce new bugs.


The agent era has pushed me toward the second option much more often.

With these powerful tools, it has become much easier to reinvent the wheel - to fork an existing project, extract what you need, and bring it into your own codebase. This used to be a terrible practice, but it is becoming more common and even the better choice in some cases.

As the famous saying goes, "Half the money I spend on advertising is wasted; the trouble is I don't know which half." The same applies to deciding when to reinvent the wheel: we know it works in some cases, but we don't know which ones. What are the **principles** that should guide the decision?


## The real and the fake arguments

I've been a believer in monorepos. I've found development across multiple codebases much slower than development in a single codebase. I've also found that most third-party software is poorly written. Some people blame AI and vibe coding. I think they are completely wrong. I've seen worse from humans. And AI-generated garbage should be blamed on the engineer who accepts it.

Another terrible argument is that if you reinvent the wheel, you will no longer be able to pull upstream updates easily. This is a false claim. Whenever you need an upstream update, you can ask AI to extract exactly the changes you need.

For any serious project, the moment you realize you need to change something in a third-party codebase, it's a good time to fork it and extract the useful parts into your own codebase. That is my simple rule of thumb, and the real argument behind it is simple: optimize for speed and reliability.

Back to coding: what is the true bottleneck?


## The true bottleneck

You are the true bottleneck in two areas: foundational knowledge and learning speed.
- I did not invent the phrase "You are the true bottleneck." This is common knowledge in Silicon Valley. You will feel exhausted when managing multiple AI sessions and context-switching all day. Karpathy once said he experienced AI psychosis and token anxiety on the *No Priors* podcast. I deeply relate. This workflow creates a false sense of achievement and productivity while making you anxious that you are not multitasking enough to truly unlock AI's full potential.
- Fortunately, there is already a term for this feeling - FOMO. The solution is simple: focus on what matters. A popular exercise often attributed to Warren Buffett says, "List your top 25 goals, select the five most important ones, and throw the remaining 20 into the trash can. They become your 'Avoid-at-All-Cost' list, meaning absolutely no distractions." The same principle applies here.
- Let's break down the two bottlenecks.
- First, knowledge is always the foundation of speed. If you have solid programming knowledge, you can easily catch agent hallucinations and overengineering. Yes, overengineering has been the biggest problem with agents. It is hard to scale when multiple sessions accumulate tech debt. It usually takes just one good idea (sometimes just one prompt) to make code more structured and organized - something AI is not always good at. It is also usually an antipattern to cram everything into one pull request. Basic coding knowledge is foundational. If you understand system design, it is much easier to guide your agent to build a scalable system. This is probably the biggest difference between people with and without strong software engineering experience.
- No one knows everything. Agents help you enter a field much more easily. It is a good idea to maximize your learning speed in that field instead of praying for your agent to fix everything and only verifying the result. By asking questions and learning the basic concepts, you will learn, grow, and iterate much faster. Knowledge is effectively infinite, but there are only a limited number of patterns you can grok and apply. Until you understand those patterns, it is not a good idea to fully trust your design of goals, loops, or graphs.
- For me, one constraint on learning speed is reading speed. Most daily coding tasks now involve reading comprehension. I've found that I'm not an efficient reader in English, so I've been communicating with my agent in Chinese. Language mixing is no longer just a problem for models; it is now a problem for me too :) I need to make an effort to improve this.
- Overall, I've found that I benefit a lot from understanding the basics - concepts, design patterns, and data flows.


So what's the current trend that actually matters in Silicon Valley?
- The belief is that everything can be coded. I see a lot of truth in this.
- Humans are the bottleneck. Optimize accordingly, which largely means optimizing for learning.

Models have improved a lot, but the people using them are improving even faster.
