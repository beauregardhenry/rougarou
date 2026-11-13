---
layout: post
title: More Pull Requests Is Not a Return
description: Anthropic says auto mode users ship about 25% more pull requests. Before calling that a return on investment, ask what reached customers sooner.
author: Beau Henry
date: 2026-11-13 09:00:00 -0600
categories: agents measurement software-delivery ai-coding
sources:
  - title: "Anthropic: Auto mode is now the default in Claude Code for Pro, Max, and Team plans"
    url: "https://claude.com/blog/auto-mode-default-in-claude-code"
    note: "Gives the 25% pull request figure without a stated comparison group, period or definition of a shipped pull request. Calls the gain output. Describes the classifier and the Adobe and Nuro examples."
  - title: "Google DORA: 2025 State of AI-assisted Software Development"
    url: "https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf"
    note: "Reports AI adoption associated with higher delivery throughput, a reversal from 2024, and with continued delivery instability."
  - title: "Google Cloud: Introducing the DORA AI Capabilities Model"
    url: "https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model"
    note: "Describes working in small batches as a long-standing DORA principle that is especially powerful in AI-assisted environments."
---

Anthropic says auto mode users among its Team and Enterprise adopters of Claude Code ship about 25% more pull requests. ([Anthropic](https://claude.com/blog/auto-mode-default-in-claude-code)) It's a usage statistic. I would not put it in a board deck under "productivity."

Anthropic doesn't either. Its announcement calls the gain output. The word tends to change on the way to the board deck.

## Compared to whom?

The announcement doesn't name the baseline. The figure came out on August 7, a week before auto mode became the default. Every auto mode user in that data had switched it on. The engineers who do that may be the ones who already used Claude Code most. That alone could produce a gap.

Nothing in the announcement claims auto mode caused the difference. Even if it did, I'd still want to know what happened to the extra pull requests.

## The check moves to the pull request

Auto mode removes the prompts that asked an engineer to approve each command. A classifier screens the agent's actions instead. Sessions run longer with no one watching.

The human check doesn't go away. It moves to the pull request. The extra pull requests land on the one checkpoint left.

Say an agent runs overnight and opens three pull requests by morning. If the engineer spends the morning working out which changes are safe to merge, the dashboard shows triple the output. The customer is still waiting for the fix.

The reverse is possible. If those three changes are small, easy to review and independently useful, more pull requests might be exactly what the team wants. Working in small batches is a long-standing DORA recommendation. You can tell which case you're in by looking at what happened after the pull requests opened.

## Throughput and instability

Google's 2025 DORA report found AI adoption associated with higher software delivery throughput, a reversal from the year before. It also found adoption still associated with more delivery instability. ([DORA](https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf)) A team can ship more changes and spend more time recovering from them. Both results belong on the same slide.

## What I'd ask before renewing

The measures already exist. DORA tracks how long a change takes to reach production and how often a deployment fails. Many engineering teams already collect both.

If I were approving the renewal, I'd compare those numbers from before and after auto mode. Then I'd trace a handful of changes customers asked for, from request to production, and count the engineer time spent on review and rework. If a release broke something, I'd count the time it took to fix.

Before and after isn't a controlled experiment either. It's still closer to what you're paying for than a pull request count.

If the vendor shows you 25% more pull requests, ask what reached customers sooner. If nobody can answer, you have no business calling it a return on investment.