---
layout: post
title: Ghostwriting for a Company That Might Be Wrong
description: Two years writing what a privacy company said about itself taught me that the job was never really writing, it was verification, and nobody hires for that part out loud.
author: Beau Henry
date: 2026-09-07 09:00:00 -0500
categories: career writing ethics ai-safety
---

For two years my job was to write the things a privacy company said about itself.

The job looked like documentation and the occasional ghostwritten post for a founder. Most people picture that as writing. This is a verification job with a writing deliverable, and *almost nobody who hires for it says so out loud.*

There is the structural reason.

The person who writes the external content is the only person in the building who reads *all* of it. Engineering knows what engineering shipped. Product knows what the roadmap says. Support knows what customers are actually experiencing. Marketing knows what the deck claims. The content owner is the one whose desk all four of those cross, in writing, in the same week.

These basic facts mean the content owner gets positioned as the first person to notice when two of them disagree.

Nobody assigns that. The job description doesn't mention it. There is no headcount for it, and there is no process that routes the discrepancy anywhere. You just find yourself holding a paragraph that is about to go live and a piece of knowledge that says the paragraph is optimistic, and the only mechanism for doing anything about it is you deciding to be inconvenient.

## Three kinds of gap

Not all of these are the same problem and treating them the same is how you burn your credibility.

**Not yet true.** The feature is real and still in progress, but the copy already describes the finished version. This is the most common gap by a wide margin, and it's usually not a lie so much as a tense error: someone wrote in the present tense about something that still lives in a branch. The fix is almost always small: change *does* to *will*, or add a date and a scope line. Catching it three weeks out costs nothing; catching it three days out costs a great deal.

**No longer true.** The copy was accurate when it was written and the product moved. This one is invisible unless somebody is re-reading old pages against current behavior, which is a job nobody has and which decays silently for years. Every company I have been near has a page like this. Most have several.

**Never was true.** Rare, and not always accidental. Sometimes it's a chain. Someone explains a capability loosely in a meeting. Someone else writes it down tighter than it was said. A third person quotes the written version as a source. By the time it reaches a customer-facing page, it has three internal citations and no evidence. Sometimes it's simpler than that: someone decided what to tell an outside party and didn't check it first. Either way, this is the dangerous one, because it *looks* well-sourced.

Customers thought we were scanning the dark web for their information. The company had actually paid a data broker for access, then handed back a phone number search dressed up as detection. That's a meaningful gap on its own: a phone number pulls in more about a person than a Social Security number does, so the result felt like a live scan even though it was one lookup against data we'd bought. The deeper version of that gap surfaced later, while I was processing refunds. That wasn't officially my job, but at a company that size, whoever could do a task did it. Card payment to account to account holder is a two-step lookup. Stripe and PayPal support run the same one for every refund. The company had told the vendor and the public that data couldn't be deanonymized: no way to connect an account back to a real person. Internally, that wasn't in question. That was the exact workflow I used to send people their money back.

## The escalation problem

Catching discrepancies is the easy part. What happens next is the real job.

A few things I'd tell someone doing this for the first time.

**Escalate the sentence, not the person.** The replacement should already be written by the time you raise it. "This claim is ahead of the product" is a sentence about a document. "Marketing overstated it" is a sentence about a team, and the team will remember it long after the document ships. The first version gets fixed. The second gets defended.

Never arrive with only an objection. The true sentence should already be written, ideally one nearly as good as what it replaces. Most of the resistance you'll hit isn't resistance to accuracy. It's resistance to the delay of figuring out what to say instead, under a deadline, with a designer waiting. Do that work yourself and the actual cost of agreeing with you disappears.

**Go early and go quiet.** The same catch is a five-minute Slack thread at three weeks out and a four-person meeting at three days out. Same words, wildly different social cost. This is the single highest-leverage habit in the job, and it's entirely about calendar discipline rather than courage.

**Say the size out loud.** Not everything you catch is worth stopping the train. Flag every soft verb with the same urgency and you teach everyone to discount you. The one time it actually matters, you'll sound exactly like all the other times.

None of that works when the people you'd be escalating to are the ones who wrote the sentence.

I overheard the decision get made: the CEO and the head of legal deciding what to tell the vendor about whether the data could be linked back to a real person. This started at the top instead of traveling up through people and getting distorted along the way. Raising it afterward, with coworkers and with people above me, got a plain answer back: push this further and it ends your employment. The call to drop it was mine, and it was the wrong one. Keeping my job mattered more than doing the right thing, and the true cost of escalating never got tested.

## What it costs

The downside is real, and pretending otherwise would make this essay useless.

Nobody gets angry. You just stop getting looped in early. Nobody decides to exclude you. The draft just becomes marginally easier to send to someone who won't slow it down. Marginal ease compounds. Eighteen months later, you're seeing things two days before launch instead of three weeks.

The only defense I found is to be fast and useful in the same motion: turning things around quickly and fixing more than you flag. Return clean copy in a day, occasionally saying "this one sentence, though," and you keep the access. A memo instead, and you lose it.

This only works as your actual job, not something assigned to you, and I understand that isn't always available. When the standard is institutional, you're enforcing it. When it isn't, you're freelancing a conscience. People are entitled to find that annoying.

## Why I keep thinking about this

Integrity, or the lack of it, scales up. The scaled-up version is what frontier AI labs are producing right now.

A system card is external content about a product. People inside the building write it, describing capabilities and limitations that only a handful of insiders can verify. Every failure mode above is available. A mitigation gets described as deployed when it's actually staged. A claim stays published long after it stopped being true. An internal summary gets quoted as evidence for the very thing it was summarizing.

Labs have red-teams and eval suites, which a privacy startup's content team never had. Those catch a different problem: whether the model does the thing. They don't obviously catch whether the document about the model still matches the model. That's the same slow drift that ate the privacy startup's old feature pages, just with more reviewers and less time. The stakes are different by orders of magnitude. Nobody I've seen is assigned the specific job of reading the document against the thing it describes, early enough that fixing it is cheap. That takes standing to be inconvenient, and discipline not to spend it on small stuff.

Nobody else was going to do that for a privacy startup, so I did it myself. I'd rather be doing the same work on a system card, where the gap between "not yet true" and "no longer true" isn't a marketing overstatement. It's a capability claim nobody caught in time.
