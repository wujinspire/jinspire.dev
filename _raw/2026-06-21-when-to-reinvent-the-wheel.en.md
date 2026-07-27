---
layout: post
title: "When to Reinvent the Wheel"
date: 2026-06-21
lang: en
published: false
---

TL;DR;


It has been a while since I last wrote about vibe coding. Partially because I've been so busy with work. However, I've not stopped vibe coding. I coded a hell lot more as model is getting so much better and better.

With those powerful tools, it has been really easy to reinvent whe wheel, or take whatever is needed into your code base. This used to be an extreme bad practice, but now it is becoming more and more commmon, and even best practice. But when?

As the famous saying goes, "Half the money I spend on advertising is wasted; the trouble is I don't know which half." So for here, what are the **principles** to decide when to reinvent the wheel?

## The current state of the art

Before answering the question about when to reinvent the wheel, let's first look at the state of the art, and some common probblems.

What's the best coding model? It's a highly subjective question, and I'm going to share my view, from a historical perspective.

- At one point, Opus 4.5 used to be cutting edgely better than anything else in the market. GPT 5.0 until 5.2 are basically garbage. At that point, people starts to realize that Anthropic is going to overrule the future of AI.
- The trend kept for a while, until they are so short on compute and starts to aggresively do quantization which makes people seek for alternatives. At that time, they have not yet sign the deal with XAI/SpaceX for renting the compute.
- Gemini 3 is still reasonable in debugging afew complicated cases, which unfortunately has not updated their model for too long. And 3.5 pro is stuck in hell. Even worse, people are leaving - Noam Shazeer, John Jumper, and a few VPs I've met.
- Back to Q1 where I'm so relying on Opus 4.5 but definitely hates degradation from the qualization of the  of model, GPT 5.3 codex starts to get my attention. It works surprisingly well, despite people complaining about the product chain and model confusion.
- Then they made changes, they realized that they need to cook coding. They abandoned Sora and focus all theri compute on Codex. They also unify the model release to GPT5.4, which is indeed a great model, that make them back into the game.
- Then it comes GPT 5.5, which is a phenominal model that most of my code are written by. It is so efficient in tokens. It is so good at github actions. It is so good at reasoning. It is so good at terminal CLIs. It hallucinates so less. I'd say it is definitely the best "coding" mode.
- But it is not omnipotent, it writes frontend code like a retard. This seems less of a problem in the past, but no vibe coders can resist the temptation of coding some frontend for visulization.
- Mythos / Fable 5 seem to change the game. I'd say the delay of the release really gave OpenAI some time to catch up. It is definitely NOT AGI. Not even close. The mystery around it easily makes people down when people sets the bar too high. It is indeed a good model. It definitely much more capable than Opus 4.8. I do not think it overrules GPT 5.5 in most domains, but definitely in a lot of domains.
- But it is so slow. It is also banned :)


After the status of the model, it's time to share about the current trend about harness.
- Cursor, the leading harness engineering platform, suffered from Strangle of Claude, desperately using Kimi2.5, and quagmired by it. SpaceX ended up buying them using the IPO craze, where the 60B is nothing compared to the valuation. It's definitely a great deal for both sides.
- Claude Code deniftely take most of the market share. It's indeed phenamonal. I perosonally still love to use cursor, but I need to admit the greatness of Claude Code.
- Now it comes to the main battle between Claude Code and Codex. Both are aiming for the same market. Both have CLI, VS Code extension, Cloude agents, and Desktop app.
- The Desktop app is definitely a great invention. But I have to say both are still improving. The hallucination of Claude Cowork makes it completely unusable. But it definitely has a first mover advantage on features.
- However, I have to say both are quite terrible. It is quite hard to share the context.

##


## The real and fake counter arguments

In one side, if you reivent the wheel, you can will encounter the problem of not easily pull the latest version of the original codebase. From my perspective, this is a false claim. Whenever you need to pull the latest version, you can always ask the AI to pull out what exactly you need.
