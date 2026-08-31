---
layout: post
title: Which Expert Did You Beat?
description: How Expert Baselines Turn Methodological Choices Into Model Claims
author: Beau Henry
date: 2026-08-31 09:00:00 -0500
categories: analysis ai evaluations system cards benchmarks expert baselines measurement methodology
---

Here are two sentences from the same evaluation, in the same system card, about the same model, on the same benchmark. Both are true.

No tested model outperformed the consensus expert baseline.

Every tested model outperformed the 80th-percentile PhD baseline.

The benchmark measures tacit knowledge in biology: the kind of knowledge you pick up by running the protocol, standing in the lab, or talking to someone who has.

The consensus expert baseline sits at 80%. The 80th-percentile PhD baseline sits at 63%.

Every model cleared 63. Every model missed 80.

Same scores. Opposite headlines.

The numbers did not create the contradiction. The noun did.

“Expert baseline” sounds like a fixed point: the bar, the line, the threshold a model either clears or misses. Here, it names two different constructions. The document gives you both. Many documents give you one.

<em>That choice can determine the headline.</em>

A consensus baseline asks one kind of question about expert performance. A percentile baseline asks another. One combines expert judgments according to some aggregation method. The other locates an individual score within a distribution of expert scores. Neither deserves the title the expert baseline without qualification.

They answer different questions while wearing the same two words.

That should make you care less about whether the model “beat experts” and more about who built the finish line.

Someone had to decide which experts counted. Someone had to decide how to combine their answers, or whether to combine them at all. Someone chose the percentile. Someone chose the sample. Someone chose which comparison belonged in the table and which comparison belonged in the prose.

Those choices happened before the headline existed.

<em>By the time you reach the system card, they look like facts of the benchmark.</em>

They are choices embedded in the benchmark.

That does not make the evaluation suspect. In this case, reporting both baselines does the reader a favor. It exposes a seam that another document might hide.

The problem begins when the seam disappears.

If a system card says a model “beat the expert baseline,” a reader should be able to answer a few basic questions: Which experts? How many? How did they perform? How did the evaluators construct the baseline? Why did they choose that construction?

Without those answers, “beat the expert baseline” tells you less than it appears to tell you.

The phrase converts a methodological choice into an empirical fact.

That move matters because readers know to inspect a spectacular result. A model jumps twenty points, and everyone starts checking the benchmark. People look for contamination, leakage, cherry-picking, bad samples, broken graders.

Ordinary numbers receive less attention.

<em>So do ordinary nouns.</em>

Baseline.
Expert.
Consensus.

They look like plumbing. They sound like the parts of the evaluation that someone settled before the interesting work began.

That is where judgment disappears most cleanly.

The important question, then, is not whether the model beat “an expert.”

<em>Which expert did it beat?</em>

More to the point: which definition of expert performance did the evaluation ask it to beat?

A specific group produced a specific distribution. Someone turned that distribution into a comparison point through a specific method. Another method sat beside it and produced a different conclusion from the same model scores.

So name the baseline. Do not write “the expert baseline” when you mean a consensus score, a percentile, a median, or an individual expert’s result. Give the comparison point a name precise enough that a reader can tell what it measures.

Then report how it was constructed. Identify the experts, the sample, the aggregation rule, the percentile, and the reason for choosing that method. If another reasonable construction produces a different headline, report that one too.

A baseline is not a natural fact waiting to be discovered. It is a comparison built from judgments. Those judgments belong in the result, not hidden behind it.

If the construction can change whether a model “beat experts,” it is not a footnote. It is part of the claim.

And if a document will not tell you what “expert” means, do not accept the headline until it does.