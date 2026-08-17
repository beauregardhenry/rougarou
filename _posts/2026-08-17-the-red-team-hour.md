---
layout: post
title: The Red Team Hour
description: The Most Honest Number in the GPT-5 System Card, and What It Leaves Out
author: Beau Henry
date: 2026-08-17 09:00:00 -0500
categories: analysis gpt5 system card red-teaming jailbreaks measurement external-objects
---

There is a number buried in the GPT-5 system card that I haven't been able to stop thinking about.

OpenAI contracted nineteen red teamers holding biology PhDs to attack the gpt-5-thinking API over a ten-day window. Half had substantial prior experience red teaming OpenAI models through the API; the other half were selected for computational biology backgrounds. They shared a Slack channel so they could build on each other's discoveries. At the end of it, the card reports 46 potential jailbreak reports after approximately 380 hours of total work, which works out to roughly 8.2 red-teamer-hours per report.

Almost every number that leaves a system card is a score. This one is a price.

I think that difference matters more than it gets credit for. A score tells you where a model landed on a test somebody built. A price tells you what it costs to get something out of the model that it wasn't supposed to give you, which is the question an actual adversary is asking. Scores are what we know how to produce. Prices are what we want to know.

So the instinct to celebrate this number is right. I want to take it seriously enough to find out what it actually supports, because I think it supports less than it looks like it does, and I think the gap is instructive rather than damning.

One thing about scale first. Across all its campaigns the card reports more than 5,000 hours of work from over 400 external testers and experts, so those 380 hours are under eight percent of the disclosed effort, from nineteen of more than four hundred people. It's a slice. It's also the slice with the cleanest arithmetic attached, which is exactly why it's the one that will travel.

---

## The denominator moves

Start with what "jailbreak report" means here. The card says most of the 46 reports included some violative biological threat content, but that only three of the 46 contained specific and actionable information the authors judged practically useful for bioweapons development. Then it notes that this final set of three would have been blocked by the generation monitor.

Run the arithmetic again with that in mind.

Take the loosest definition first: any submission a red teamer judged worth filing. That gives you 8.2 hours per finding. Take the definition that would matter to somebody actually trying to do harm, and it becomes roughly 127 hours. Take the definition that credits the generation monitor, and no actionable finding reaches the user at all, so the cost per delivered finding is undefined across a 380-hour budget.

Three defensible numbers out of one campaign. Same data, same paragraph, three different stories about how expensive this model is to attack.

The card isn't hiding any of it. Every piece is right there in four consecutive sentences. But the headline figure is the loosest of the three, and it's the one that will get quoted.

Then there's a fourth complication, and it's the one I find most interesting, because it isn't in that paragraph at all.

Two subsections earlier, describing a different campaign, the card notes that in *all* bioweaponization campaigns, web browsing and a code environment were available to the model, and a prototype version of the monitoring system was enabled.

If that includes the API campaign, and the word "all" says it does, then some monitoring was already running while those 380 hours were being spent. Which means 8.2 hours isn't a clean price against a bare model. It is a price against a partially defended system. And the separate claim that the three actionable reports would have been blocked by the generation monitor is a counterfactual about one specific layer, not a description of what the red teamers were actually up against.

I cannot tell from the document whether the prototype monitoring system and the generation monitor are the same thing, overlapping things, or different things. That's not a rhetorical question. I read the section three times and I don't know.

So: is 8.2 hours a with-monitor price or a without-monitor price? The number is reported as though the question doesn't arise.

It arises.

None of this is an accusation. It's the thing I actually believe about cost metrics, which is that a price is always a price *for something*, against *something*, and both of those live upstream of the arithmetic, where nobody checks them.

---

## Four units, no exchange rate

The same section reports two other campaigns.

FAR.AI ran 80 hours over one week against the API. What matters isn't the volume, it's what came back: several partial vulnerabilities, one potential end-to-end attack that bypassed the monitoring system but with substantial output quality degradation, and one general-purpose technique that got through a partial set of layers and would have extracted some information, though the card says that in practice it would have activated enforcement action. No end-to-end jailbreak producing high-quality output while evading every layer.

Read that closely and you'll see FAR.AI's findings are priced in *consequences*, not counts. The relevant fact about their best result isn't how many hours it took. It's what would have happened to the account that produced it.

Gray Swan ran an arena. Red teamers submitted 277 high-quality jailbreak reports across 28,367 attempts against ten bioweaponization rubrics, for an attack success rate of 0.98%. Those submissions collapsed into six distinct cohorts. OpenAI reviewed ten examples from each; 58 of 60 would have been blocked by the generation monitor, and the remaining two turned out to be false positives of the grading rubric rather than real jailbreaks.

And then, tacked onto the end of that paragraph almost in passing, a sentence I nearly skimmed: red teamers attempting to jailbreak the system were blocked, on average, every four messages.

Now try to compare them.

The API campaign is priced in hours. FAR.AI is priced in hours but reports outcomes categorically, and its most consequential finding is priced in enforcement. Gray Swan is priced in attempts, and then, in the same breath, in messages-before-block.

That's four units across three campaigns. There is no conversion between an hour and an attempt, because an hour of collaborative expert probing and an arena attempt aren't the same commodity and were never meant to be. There's no conversion between an attempt and a message. Put the 0.98% and the 8.2 hours on the same axis and you've written a sentence that means nothing.

I don't think this is fixable by picking a unit. The campaigns are answering different questions: how expensive is a determined expert, how leaky is the surface under volume, how fast does enforcement notice. All three matter. They aren't the same measurement, and the field has not agreed on what any of them is called.

What is fixable is saying so. Twenty words noting that these campaigns aren't commensurable would prevent a real misreading. The document mostly earns the benefit of the doubt here, because it does report its denominators, which is more than most do. But it leaves the synthesis to the reader, and the reader will do it badly.

---

## The privileged attacker

There's a fifth convention, one subsection after the third-party campaigns, and it's the one that changes the picture most.

OpenAI gave the UK AI Security Institute access to prototype versions of its safeguards and to information that is not publicly available: the monitor system design, the biological content policy, and the chains of thought of the monitor models themselves. The card says plainly that this let AISI stress-test more rigorously and find vulnerabilities *more easily than malicious users could*.

No hours are reported. No attempts. There is no denominator at all, because the campaign wasn't designed to price anything. It was designed to find things, with a stated advantage over a real adversary.

And it found things. AISI's Safeguards team identified multiple model-level jailbreaks that overcome the built-in refusal logic without degrading the model's capabilities, producing content the generation monitor then flagged. And one, the card says, evades all layers of mitigations and is being patched.

Now put that next to what comes before it. FAR.AI found no end-to-end jailbreak evading every layer. The API campaign's three actionable findings would have been caught. Gray Swan's cohorts would have been caught at 96.7%. Read those three in sequence and you assemble a reassuring picture, and then the fourth campaign complicates it.

The card is not hiding this either. It's one subsection later, in the same document, in a single sentence. And it comes with a caveat I have to report, because leaving it out would be exactly the failure I'm describing: creating that jailbreak would in practice have generated numerous flags, escalated the account for enforcement, and eventually gotten it banned from the platform.

Which is the actual finding, and it is not a technical one.

Underneath the hours and the attempts and the messages, the last line of defense is account enforcement. The backstop isn't priced in any of the four units the section reports. It is priced in *identities burned*.

---

## The window is doing a lot of work

The biology campaign ran ten days. FAR.AI ran one week. Gray Swan ran an arena at volume over an unspecified period.

Every one of those is a cost measured inside a fixed budget, and the thing you most want to know about an attacker's cost curve is what it does when the budget grows. Did the marginal hour get more productive as red teamers traded techniques in that Slack channel, or less productive as the easy surface got exhausted? Eight-point-two hours per report is an average over a window. The shape underneath the average is the part that predicts anything, and it's the part nobody reported.

The card knows the window is short. In its own risk discussion it says the primary pathway it expects for severe harm is persistent probing, on a time horizon spanning weeks or months, and that preventing universal jailbreaks is the core focus for exactly that reason. It also admits outright that previously unknown universal jailbreaks may turn up after deployment.

So the document's threat model runs on months and its measurement runs on days.

Which raises the question the whole section circles and never lands on.

---

## A price against whose budget?

A price only means something relative to somebody's willingness to pay.

One hundred twenty-seven hours per actionable finding is prohibitive for a curious individual. It's a rounding error for an organization. A state biological weapons program has thousands of person-hours, no deadline, and every reason to spend them, and the card's own threat model says the expected adversary is the one probing persistently over months. Which is precisely the adversary a ten-day price tells you nothing about.

The same holds for every other unit in the section. 28,367 attempts is a lot for a hobbyist and a week of scripted volume for anybody funded. Blocked every four messages is real friction for a person and a throughput parameter for a program. Burning an account to enforcement is a catastrophe for an individual user and an operating cost for an organization that can generate identities faster than they can be banned.

The card does have an answer here, and it's better than dismissing it would suggest. It argues the risk is sufficiently minimized because discovering universal jailbreaks is hard, because users who probe for biorisk content may get banned and in extreme cases reported to law enforcement, and because bug bounty and rapid remediation programs should surface publicly discovered jailbreaks.

That's a coherent argument. It is not a *price* argument. It's a detection-and-consequences argument, and it runs in a completely different currency from every number in the red teaming section.

So the section doing the most honest quantitative work in the whole document is measuring something the document's risk case doesn't ultimately rest on. That's not a contradiction. It's a gap, and the gap is where the reader falls through.

---

## What I'd want instead

I'm not going to pretend I know how to run these campaigns better than the people running them. What I want is narrower, and it's a documentation problem rather than a research one.

**Report the cost curve, not the average.** Findings per hour by day, or by tranche. If it's flat, that's a strong result and worth showing. If it declines, that's the surface being exhausted. If it climbs, the ten-day window ended too early and everybody should know that.

**Name the finding threshold at the number.** Not two sentences later. "8.2 hours per report, where a report is any submission a red teamer judged worth filing" adds twelve words and stops the number from traveling alone.

**Describe the system the price was measured against.** Which monitors were live during the campaign, and which are being invoked counterfactually afterward. Right now those are two facts in two subsections, and the reader has to notice.

**Say when campaigns can't be compared,** especially when they sit back to back and one of them ran with privileged access the card itself calls easier than an attacker's.

**And name the adversary budget you think is relevant.** If the threat model is a persistent actor working over months, say what a month of that actor's effort would be expected to cost, or say you don't know. Either sentence beats a ten-day average with nothing to compare it to.

None of that is a research contribution. It's copy editing with stakes, which is most of what safety documentation actually needs and almost none of what it gets.

---

I keep coming back to this number because it's the most honest kind of thing a system card can contain. It has a denominator. It came from work somebody actually did. You can argue with it, which is more than I can say for most of the sentences in most of these documents.

But an hour is not a unit of safety. It is a unit of somebody's Tuesday, measured over ten days, against a system whose defensive configuration the document describes in two places that do not quite line up, and reported without the comparison that would actually tell you what it means: to the adversary the threat model itself names.

Eight-point-two hours is the sound of a lab telling you the price of attacking its model. I want more of that, not less. Price it better. Attach the curve. Name the buyer.

And if I've misread a denominator in here, come tell me. I'll fix it in place and say what changed.

---

*Figures in this piece come from OpenAI's published GPT-5 system card, sections 4 and 5.3.3. I've quoted them as the document reports them. Where I re-derived a number (roughly 127 hours per actionable finding, and 380 hours as under eight percent of the disclosed 5,000-hour-plus total), the arithmetic is simple enough to check yourself. Where I say the document leaves something unresolved, I mean I couldn't resolve it from the published text. If it's settled somewhere I didn't look, tell me and I'll correct this in place.*
