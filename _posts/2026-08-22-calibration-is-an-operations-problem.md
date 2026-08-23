---
layout: post
title: Calibration is an Operations Problem
description: Where the GPT-5 System Card Separates Evidence From Judgment Well, Where It Does Not, and Why That is an Operations Job
author: Beau Henry
date: 2026-08-22 09:00:00 -0500
categories: calibration analysis gpt5 system-card documentation operations editorial-standards evidence-and-judgment
---

When I wrote *The Calibration Standard* I put the whole burden on the model. Nine rules, three of them hard stops, all of them addressed to a system that cannot reliably tell what it knows from what it invented.

I still think that framing is right as far as it goes. I have come to think it does not go very far.

The reason is that a model's calibration failure is contained. It produces one bad answer for one person, who can usually check. An organization's calibration failure produces a document that a regulator reads, that a journalist quotes, that three other organizations cite, and that nobody can check because the underlying data never left the building. Trace one of those citations back far enough and it's usually the same thing: a threshold or a baseline that was somebody's judgment call, repeated so many times it reads as the measurement itself. Same failure — inability to distinguish what you measured from what you concluded — at a scale where the correction mechanism does not run in time.

Model calibration is a research problem. Organizational calibration is an operations problem, and it is mostly solved with document design.

---

## Where Calibration Becomes Visible

A system card is the artifact where an organization's calibration is legible to outsiders. It contains three kinds of sentence, and the whole question is whether a reader can tell them apart.

There are measurements. A model scored some percentage on a benchmark. Red teamers filed some number of reports over some number of hours. These are checkable in principle and arguable in practice.

Assessments are different: a result "does not meet the threshold" for a risk category, a mitigation is "sufficient," a residual risk is "sufficiently minimized." These are judgments, made by people, according to criteria that may or may not appear in the document.

Then there's the transition — the sentence where a measurement becomes an assessment. That sentence is where nearly all of the interesting content lives, and it is almost never marked.

Take the expert baseline problem. The GPT-5 system card reports a tacit-knowledge and troubleshooting benchmark with two reference points: a consensus expert baseline of 80% and an 80th-percentile PhD expert baseline of 63%. It then reports that no tested model outperforms the consensus baseline, though all of them outperform the 80th-percentile baseline.

Both sentences are true. They are the same measurement. They produce opposite headlines — *models still below human experts* and *models beat 80% of PhDs* — and which one a reader walks away with depends entirely on a choice made upstream about which baseline to foreground.

The card reports both, and that matters. The document is more calibrated than the discourse that will consume it. But the *choice* of baseline is a judgment, the judgment is consequential, and the document does not say who made it or why 80th percentile was the relevant threshold rather than 50th or 95th. The measurement is transparent. The reasoning around the measurement is not.

That's the shape of organizational miscalibration — not lying, not even hedging, just failing to mark the seam where evidence stops and judgment starts, so the reader inherits a conclusion wearing the clothes of a fact.

---

## The Footnote That Gets It Right

Here is a case where the same document gets it right, and I think it is worth studying because it is small.

The card reports a SWE-Bench result, then adds a note: all preparedness evaluations in the card were run at the model's maximum trained-in verbosity, which is higher than the "high" setting available in the API, and the 74.9% figure in the GPT-5 launch blog post was run at the API default. It states directly that changes in verbosity can lead to variation in eval performance.

Two numbers exist in public for the same model on the same benchmark. Rather than hoping nobody notices, the document explains why, names both configurations, and warns that the setting matters.

That footnote is calibration as an operational practice. It cost the authors maybe sixty words. It converts what would have been a discovered inconsistency — the kind that generates a thread and then a correction — into a disclosed one. And it teaches the reader something true about eval methodology in the process.

It doesn't hedge. It says exactly what was different and what the difference does. My own Rule 1 was supposed to be about this distinction and I don't think I made it well enough: hedging is what you do when you don't know which part is soft. Calibration is what you do when you do know.

---

## Four Things a Calibrated Document Does

None of these are research. All of them are process, and all of them can be assigned to a person. Naming the denominator and publishing the setting restate, as standing rules, arguments I already made about specific numbers in one document. Marking the transition generalizes a different argument about that same document — not about a number, but about a seam. Saying who decided is new.

**Mark the transition.** When a paragraph moves from measurement to assessment, say so: "We measured X; on the basis of X and our threshold criteria, we assess Y." It costs a little elegance. It means the reader knows, at every point, whether they're looking at a measurement or a judgment.

**Name the denominator at the point of use.** Not in a methods appendix twelve pages later. A rate, a cost, or a count that travels without its denominator will be quoted the same way it was published: without one.

**Publish the setting.** Every number is a number under a configuration. Verbosity, temperature, tooling, whether browsing was on, how many rollouts, which metric over which subset. Strip the configuration and what's left is not a result, because nobody outside the building can do anything with it except repeat it.

**Say who decided, or say that a person decided.** Not necessarily a name — I understand why organizations don't want individual analysts attached to threshold calls. But "we assess" and "the threshold was not met" are different sentences, and the second one hides an actor the first one at least gestures at. Passive voice is where accountability goes to be laundered.

---

## This Is an Operations Job

Every one of those four is a documentation standard enforced across contributors who did not write it and do not report to whoever did. That is not a research function. It is the same job as a journal's editorial standard, or a hospital's protocol review, or the person at a startup whose job is to check the marketing page against the product before it ships.

I have done two of those three: journal editorial standards enforced across researchers who did not report to me, and the marketing-page-against-the-product check at a startup where the product changed faster than the copy did. The pattern was identical both times: the standard is easy to write, trivially agreed to in principle, and violated constantly under deadline pressure by good people who are trying to finish.

Nobody wants that job to exist. It slows things down and it is unpleasant to be the one asking. It is also the difference between an organization whose published claims can be trusted and one whose claims merely have not been checked yet.

I wrote nine rules for a model because that was the system I could reach from my desk. The harder version is the same nine rules pointed at the people writing about the model, and somebody has to be assigned to enforce it.

*The Calibration Standard* is [here](https://rougarou.io). Still take it, still break it, still tell me where.
