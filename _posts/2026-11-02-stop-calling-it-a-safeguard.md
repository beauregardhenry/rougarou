---
layout: post
title: Stop Calling It a Safeguard
description: Human reviewers caught 13.6% of dangerous commands in Anthropic's test. If review is part of your safety case, show that it catches consequential errors under real working conditions.
author: Beau Henry
date: 2026-11-02 08:00:00 -0600
categories: ai-safety human-oversight evaluation agents
image: /assets/img/stop-calling-it-a-safeguard-hero.png
sources:
  - title: "Anthropic: Auto mode is now the default in Claude Code for Pro, Max, and Team plans"
    url: "https://claude.com/blog/auto-mode-default-in-claude-code"
    note: "Reports the controlled test with 1,053 paid testers, the human and classifier catch rates, the 97% and 39% figures, and the recommendation to review high-stakes production changes."
  - title: "Anthropic: How we built Claude Code auto mode"
    url: "https://www.anthropic.com/research/claude-code-auto-mode"
    note: "Reports the classifier's evaluation, including its 17% miss rate on 52 real overeager actions."
  - title: "Anthropic: Measuring AI agent autonomy in practice"
    url: "https://www.anthropic.com/research/measuring-agent-autonomy"
    note: "Reports that experienced Claude Code users auto-approve and interrupt more, and argues against mandating specific interaction patterns."
  - title: "Anthropic: How AI agents shape experts' judgment calls"
    url: "https://www.anthropic.com/research/agents-judgment-calls"
    note: "Summarizes the randomized trial, including the 86% alignment rate, the repeated arguments and the self-selected comparison of serious errors."
  - title: "Herdagdelen, Joren and Tamkin: Who's Aligned to Whom? How AI Agents Shape Experts' Research Judgment Calls"
    url: "https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf"
    note: "Gives the trial's full methods, estimates and limitations."
  - title: "Dell'Acqua et al.: Navigating the Jagged Technological Frontier, Organization Science"
    url: "https://doi.org/10.1287/orsc.2025.21838"
    note: "Reports the preregistered BCG experiment, including correctness rates and coherence ratings for the task outside GPT-4's capability."
  - title: "DevOps.com: Anthropic Makes Claude Code's Auto Mode the Default, Betting Automation Beats Manual Review"
    url: "https://devops.com/anthropic-makes-claude-codes-auto-mode-the-default-betting-automation-beats-manual-review"
    note: "An example of coverage treating the 97% approval rate as evidence that people stopped reading prompts."
---

If your AI policy ends with "a human must review the output," you have assigned a task. You have not shown that anyone can do it.

Human review is the default safety claim in AI deployment. Most versions I have read come with no number attached. If human review is part of your safety case, show that it catches consequential errors under the conditions in which people actually work.

This August, Anthropic published the clearest public test I have seen. Human reviewers caught 13.6% of dangerous commands.

### The number

[Anthropic hired 1,053 paid testers](https://claude.com/blog/auto-mode-default-in-claude-code) for a coding study. Partway through each session, it swapped one permission prompt for a "clearly dangerous command." Testers refused that command 13.6% of the time. Anthropic's automated classifier blocked 89% of the same commands.

Performance also fell as sessions ran. Testers blocked about 17% early on and about 5% after 50 or more prior prompts. Head to head, the classifier blocked 800 commands a human approved, and humans blocked 6 that the classifier allowed.

Read the limits before you quote it. Testers worked in a test environment, not their own codebases, and they knew they were being evaluated. Nothing dangerous could run, so approving cost them nothing.

Anthropic also sells the product that won, and I found no full protocol beyond the blog post. The test does not meet the standard I just set, because it did not use testers' real work. It is still more evidence than a policy sentence provides.

### Activity is not detection

The figure that traveled furthest was a different one. Anthropic reported that users approve 97% of permission prompts, and [some coverage](https://devops.com/anthropic-makes-claude-codes-auto-mode-the-default-betting-automation-beats-manual-review) took that as proof people had stopped reading. It proves no such thing. Anthropic itself notes that most prompts are likely safe, and a perfect reviewer in a safe queue approves nearly everything.

An approval rate cannot separate attention from autopilot. To measure detection, you need to know which items warranted rejection. This is why the 13.6% tells you something and the 97% does not.

The same problem sits inside a more respectable claim. In February, [Anthropic reported](https://www.anthropic.com/research/measuring-agent-autonomy) that experienced Claude Code users auto-approve more and interrupt more. It concluded that oversight means being "in a position to intervene when it matters." I agree with the direction, but an interrupt rate only counts interventions. It does not show that they landed on the actions that mattered.

### Expertise does not settle it

The natural reply is to hire better reviewers. The evidence is not encouraging.

In [a preregistered field experiment](https://doi.org/10.1287/orsc.2025.21838), 373 BCG consultants worked a business case built to sit outside GPT-4's capability. The no-AI group was right 84.5% of the time. The AI groups were right 70.6% and 60% of the time, and their recommendations were rated more coherent even when wrong.

On October 27, [Anthropic reported a sharper result](https://www.anthropic.com/research/agents-judgment-calls). Fifty causal-inference analysts worked with an agent whose lean on each decision was set by coin flip. On four analytical decisions, they went with its lean 86% of the time, against 50% by chance. Afterward, 77% repeated its arguments and 15% credited it.

The lean was deliberately amplified, and this was one task in one field. Experience and expertise did not predict who deferred, though that analysis was exploratory. The authors' conclusion still holds: "a human reviewer is only an independent check if their judgment is their own."

The same study is no case against using agents. Serious errors appeared in the work of 3 of 50 agent users and 6 of 11 analysts who chose to work without one, although that group was less experienced and not randomized. The work may get cleaner while the judgment inside it becomes less independent.

### Anthropic has the same gap

Anthropic deserves credit for running this test. Its classifier got [a published evaluation in March](https://www.anthropic.com/research/claude-code-auto-mode), including a 17% miss rate on 52 real overeager actions. The human check it replaced got its first public catch rate that I know of in August. The machine was held to the higher standard.

Then the August post closes by recommending that people review high-stakes production changes themselves. That may be wise, since one deliberate review is a different task from prompt number 51. But the post gives no catch rate for that review. Its customer examples also describe engineers receiving finished pull requests for review.

Those checkpoints need the same test. So does plan approval, where users reject 39% of plans against 3% of permission prompts. A rejection rate is activity too. Test a flawed plan and a flawed pull request, then publish what people catch.

### Test the review you actually run

A catch rate is necessary, and it can still mislead. Easy test errors inflate it, and a reviewer who rejects everything scores well. Anthropic argues that it is too early to mandate specific interaction patterns, and I agree. Leave the interface open and require the result.

Any organization that puts human review in its safety case should run a controlled test that meets these conditions:

1. Use representative work and consequential errors your team has actually seen.
2. Run the actual review process, with its real tools, queue length and time pressure.
3. Build test items so they cannot leave the test.
4. Report misses and false rejections by reviewer level and queue position.
5. Trace each objection through escalation to confirm that catching the problem stopped it.

Anthropic's design shows the third condition is possible: it changed only the prompt text, so nothing dangerous could run. Set the minimum result in advance. Below it, redesign the process or drop the claim.

Reviewer level matters. A junior employee may be able to check some parts of a result and not others. A responsible process identifies that boundary. It does not wait for a failure to discover where the employee's competence ended.

Planted errors have one hard limit: judgment calls have no wrong answer to plant. Anthropic could measure deferral only because it randomized the agent's lean, which it says is rarely possible in real work. For consequential judgment calls, record an independent assessment before showing the model's recommendation, then examine why the reviewer changed their mind.

If your safety case depends on someone catching the mistake, test whether they can. Until then, you have assigned responsibility. You have not shown that anyone can carry it.

## Sources

- [Anthropic: Auto mode is now the default in Claude Code](https://claude.com/blog/auto-mode-default-in-claude-code), August 7, 2026
- [Anthropic: How we built Claude Code auto mode](https://www.anthropic.com/research/claude-code-auto-mode), March 25, 2026
- [Anthropic: Measuring AI agent autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy), February 18, 2026
- [Anthropic: How AI agents shape experts' judgment calls](https://www.anthropic.com/research/agents-judgment-calls), October 27, 2026, and [the full paper](https://www-cdn.anthropic.com/519c17a5d23a794e8b6d50a854048d0b61e0d73a.pdf)
- [Dell'Acqua et al., Organization Science, 2026](https://doi.org/10.1287/orsc.2025.21838)
- [DevOps.com coverage of the 97% figure](https://devops.com/anthropic-makes-claude-codes-auto-mode-the-default-betting-automation-beats-manual-review)
