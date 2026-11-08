---
layout: post
title: "One Year in Reflection"
excerpt: "Looking back on my first year at Reflection: building pre-training infrastructure from scratch, scaling from dense models to MoE on GB300, shipping Beam, and why open access is essential for a democratic AI future."
date: 2026-11-01
lang: en
pair: one-year-in-reflection.zh
---

I hit my one-year mark at Reflection - a meaningful milestone for me.

There is no better way to celebrate it than with a model release: we just shipped our first model, **Beam**.

A year ago, I joined Reflection as the first employee after the company pivoted to building open-source frontier models, and also as the first Chinese employee in the company.

So what happened over the past year?


## Building from Zero: Infra, Science, and Scale

I joined the infra team at Reflection, starting out on RL infra before fully transitioning to pre-training infra - where I got to put my large-scale systems background to work and push far beyond it.

Looking back, I can still feel the excitement of building almost everything from the ground up.

When we started, we could barely run a job with reasonable reliability. A 1k-GPU run on H100s required constant babysitting and would still fail regularly. To go from there to training frontier models, we had to lay every brick of the foundation ourselves:

- We built out the Kubernetes team and cluster foundation.
- We engineered fault tolerance and observability from scratch, turning fragile runs into self-healing systems.
- We onboarded **GB300** at scale and relentlessly hill-climbed our MFU and goodput.

What made this journey truly rare, though, was not just scaling the cluster - it was getting to be part of the whole process of building a language model from nothing alongside a deeply knowledgeable and driven team.

As we scaled from a handful of H100s to massive **GB300** clusters, I got to sit in on and contribute to the discussions around our transition from dense models to large-scale **MoE**, and experience firsthand how **science scales up** from small experiments to large training runs. Because people across infra, pre-training, and RL are so open and generous with their knowledge, none of these choices happen in silos. Every architecture decision is a balance between model quality, pre-training efficiency, and downstream inference - because inference speed directly dictates both how fast **RL** can generate rollouts and how practical the model is for real-world serving. Having worked across both RL and pre-training infra, it was rewarding to see how all the pieces connect across the full lifecycle of a model.

Even now, I still feel the excitement every time we kick off a big run. And out of all those runs, **Beam** was born.


## Why Open Access Matters: Intelligence and Democracy

After spending a year in the trenches seeing just how much compute, systems engineering, and scientific rigor it takes to train a frontier model, my conviction in our mission has only grown stronger.

Frontier AI is rapidly becoming the foundational layer of human thought, creativity, and productivity. When the barrier to building these models reaches thousands of next-generation GPUs and deeply specialized science, there is a very real danger that frontier intelligence gets locked behind a handful of closed APIs controlled by a few tech giants.

If a few corporations get to decide who can access intelligence, what questions are allowed to be asked, and how much it costs to think, that is not just a market monopoly - it is a threat to democracy itself.

**Open access is fundamentally about democracy and equal access.** A democratic future in the AI era requires that the weights, capabilities, and building blocks of intelligence remain accessible to everyone - independent developers, academic researchers, startups, and individuals around the world - without needing permission from a gatekeeper. People should have the freedom to inspect, customize, and build upon frontier models on their own terms.

But belief alone is not enough. **Mission requires speed.** Open source only matters as a counterweight to closed monopolies if open models can compete at the absolute frontier. If open models lag a generation behind, "democratization" becomes an empty promise. That urgency - the marriage of mission and speed - is why we push so hard on MFU, why we race to bring up new hardware like GB300, and why I still feel such a deep bond with Reflection and what we are building.


## The People and My Own Growth

Looking back, none of this speed or scale would have been possible without the people here. What makes Reflection special to me is the rare combination of qualities in my coworkers:

- **Deeply knowledgeable, yet genuinely kind:** I am surrounded by world-class researchers and engineers who know their craft inside out. Yet there is zero ego. People are always willing to patiently explain a modeling detail, debug a nasty systems issue together, or share hard-won intuitions across teams.
- **Driven and moving fast:** Everyone here shares the same values and urgency. Decisions don't get stuck in endless meetings - when we see a bottleneck, we align quickly, build the fix, and ship it. Working in such a fast-paced environment with people who care this much is contagious; it naturally pushes you to raise your own bar.

Growing alongside this team and a fast-moving company while building so many critical pieces from scratch has been incredibly rewarding. Over this past year, I have grown more than I could have imagined:

- **In knowledge:** I bridged the gap between pure large-scale infrastructure and frontier modeling - understanding not just how to keep thousands of GPUs running, but how architecture, science scale-up, pre-training, RL, and inference fit together as one unified system.
- **In mindset and thinking:** Operating in a high-velocity startup environment taught me to focus on what actually moves the needle, own problems end-to-end, and iterate without fear.
- **In AI use:** As someone building models every day, the way I collaborate with AI in my own engineering and thinking has also transformed completely.

One year in, and our first model is out in the world. Grateful for the team, the mission, and the journey so far - on to the next run.

