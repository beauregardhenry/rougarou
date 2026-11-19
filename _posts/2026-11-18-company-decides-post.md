---
layout: post
title: The Company Still Decides When to Stop
description: California can fine an AI developer for breaking its own safety framework, but not stop it from weakening one. Loosening a catastrophic-risk safeguard should require outside approval against a common floor.
author: Beau Henry
date: 2026-11-18 08:00:00 -0600
categories: ai-safety ai-policy regulation frontier-ai
image: /assets/img/the-company-still-decides-when-to-stop-hero.png
sources:
  - title: "California Business and Professions Code §22757.12 (SB 53, Transparency in Frontier Artificial Intelligence Act)"
    url: "https://california.public.law/codes/business_and_professions_code_section_22757.12"
    note: "Requires large frontier developers to publish and comply with a frontier AI framework, lists the subjects it must address, and requires a modified framework and justification within 30 days of a material modification. Sets no approval step and no minimum strictness."
  - title: "GovAI: Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections"
    url: "https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections"
    note: "Source for the earlier RSP's public commitment not to train or deploy models capable of catastrophic harm, the v2 competitor clause, the unilateral-slowdown rationale and the note that existing safeguards stayed in place."
  - title: "Anthropic: Anthropic's Responsible Scaling Policy, Version 3.0"
    url: "https://www.anthropic.com/news/responsible-scaling-policy-v3"
    note: "Anthropic's explanation of the February 2026 revision, including the collective-action argument, slow government action, the ASL-3 safeguards and conditional external review of Risk Reports."
  - title: "OpenAI: Preparedness Framework, Version 2 (April 2025)"
    url: "https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf"
    note: "Allows OpenAI to adjust its requirements if another developer releases a High or Critical capability system without comparable safeguards, subject to public disclosure, no meaningful increase in overall risk and safeguards more protective than the other developer's."
---

Anthropic was right to drop a safety promise it could not keep. That is the problem.

Its Responsible Scaling Policy used to state "a public commitment not to train or deploy models capable of causing catastrophic harm." Version 3.0, published in February, removed that language. ([GovAI](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections)) Critics read it as a retreat. Anthropic described the new commitments as more realistic. Some of the safeguards in its earlier policy, the company wrote, "might prove outright impossible to implement without collective action." Government action had "moved slowly." ([Anthropic](https://www.anthropic.com/research/responsible-scaling-policy-v3))

I believe the explanation. A pledge that a company would break under competitive pressure is worse than no pledge. It tells the public a line exists where none does. Anthropic said so openly, and it deserves credit for that.

But follow the explanation to its conclusion. If adequate protection requires competitors to act together, a promise from one company can't provide it. Neither can promises from five companies, each free to revise its own. The revision is the best evidence yet that voluntary safety frameworks cannot do the job they were sold to do.

## The exits were already written

The pause language was not the first thing to bend. Version 2 of Anthropic's policy already allowed it to lower its safeguards if another developer would "pass, or be on track to imminently pass" a capability threshold without "equivalent" protections. ([GovAI](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections)) OpenAI added a similar clause in April 2025: "If another frontier AI developer releases a high-risk system without comparable safeguards, we may adjust our requirements." ([OpenAI](https://openai.com/index/updating-our-preparedness-framework/))

OpenAI attached conditions. It would first confirm that the risk landscape had changed and acknowledge the adjustment publicly. It would also keep its safeguards more protective than the competitor's. Those conditions are serious. Another company's release really can change what a precaution accomplishes.

Notice who checks the conditions. The developer decides whether the landscape changed. The developer decides whether its adjustment meaningfully raises risk.

Picture the meeting. A competitor has shipped. Your safeguards are holding up your release. Your researchers disagree about how much risk a launch adds. A published framework can structure that argument. It cannot take the commercial stakes out of the room, and it cannot overrule the people who wrote it.

## California made the frameworks binding. It bound the wrong thing.

The gap isn't hypothetical. California's SB 53 took effect in January. It requires the largest frontier developers to publish a safety framework and comply with it. A developer that fails to comply with its own framework faces civil penalties of up to $1 million per violation, enforced by the state attorney general. ([Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2025/10/california-enacts-sb-53-creating-new-requirements-for-developers-of-frontier-artificial-intelligence-models-and-related-whistleblower-provisions), [Covington](https://www.globalpolicywatch.com/2025/10/california-governor-signs-landmark-ai-safety-legislation/))

That sounds like the binding rule critics asked for. Now look at how changes work. A developer that materially modifies its framework must publish the new version and a justification within 30 days. The law punishes a company for breaking its own rules. It lets the company rewrite them, as long as it explains afterward.

Anthropic's revision came after SB 53 took effect. Anthropic explained itself at length. No regulator had the authority to say no.

## Two kinds of revision

Safety policies have to change. A test can turn out to measure the wrong thing. A safeguard can fail against the threat it was built for. Freezing a policy would preserve its mistakes along with its protections.

But there are two different reasons to loosen a requirement. One is that the evidence improved: the risk turned out smaller than feared, or a cheaper safeguard works as well. The other is that the requirement can't be met. Anthropic's own explanation puts its revision in the second category. The safeguards might be impossible without collective action.

That second kind of revision is the one an outside party most needs to review. "We can't meet this" may be true. It is also the claim a company has the strongest commercial reason to make.

## What would actually bind

Here is the rule I want. A developer can tighten its safety framework on its own whenever it likes. Loosening it requires someone else's sign-off.

That someone needs access to the evidence and the authority to refuse. It could be a public agency, or an independent body the industry funds but does not control. In a genuine emergency, a developer could act first and submit the change for review within a fixed period. Otherwise, the looser rule doesn't take effect until the reviewer agrees.

This is a narrow demand. It doesn't tell labs how to build safeguards, and labs are good at that work. Anthropic's earlier policy pushed it to develop protections it later deployed, including the ASL-3 safeguards it activated in May 2025. The company also says the policy encouraged OpenAI and Google DeepMind to adopt similar frameworks. ([Anthropic](https://www.anthropic.com/research/responsible-scaling-policy-v3))

Version 3.0 does require external review of Anthropic's risk reports, but only "in certain circumstances," and the company says its current models do not yet require it. ([Anthropic](https://www.anthropic.com/research/responsible-scaling-policy-v3)) The outside check exists on paper. The company decides when it applies.

Bad regulation is a real risk. A reviewer could be slow or captured. Those are reasons to design the reviewer carefully. They are not reasons to leave the decision with the one party that pays for delay.

The competitor clause shows why. If a rival's release genuinely changed the risk, a competent reviewer should agree quickly. If it didn't, the clause was only ever a license.

Anthropic was honest that one company cannot solve an industry's coordination problem. The answer is not to accept that problem as a permanent reason for each company to set its own limits.

A voluntary framework tells us how a developer intends to decide. A law that enforces the framework tells us the developer will follow its rules until it changes them. Neither tells us who gets to tell it no.