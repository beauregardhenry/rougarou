---
layout: post
title: The Anthropic Red-Team Hour
description: Three outside teams tested Claude Opus 5 safeguards and reported it in hours, hours, and attempts — the same unit problem I found in the OpenAI system card in August, now in the document from the company I am applying to.
author: Beau Henry
date: 2026-09-10 09:00:00 -0500
categories: ai-safety writing evaluation career
---

Three outside teams tested Claude Opus 5's cyber safeguards this year, employing different lengths of effort. Close to 100 hours went to Trajectory Labs. They completed one task using prompting built for that task. They found no new universal jailbreak strategies, so their result does not generalize. About 16 hours went to 10a Labs, which found nothing. Grayswan's automated attacker ran 150 times against each task and succeeded at none of them.

## Rank those three efforts by how hard they tried.

You can't. The numbers aren't missing. They're more precise than most disclosures I've read this year. Two are denominated in hours. One is denominated in attempts, and nothing in the document converts between the units. A human spending 16 hours on a problem isn't less thorough than a script making 150 short attempts at it. That depends on what an "attempt" contains, and whether the attacker learned anything across the 150 tries. The card doesn't say. It reports three numbers in sequence, doing the same job in the argument without doing the same thing.

I made a version of this argument in August about the GPT-5 system card: a red-team finding is a price, not a score. A document reporting several prices in incompatible currencies hasn't told you the total cost. I didn't expect to make the same argument about the company I'm trying to work for three weeks later. That's not a gotcha. A more useful reading: the problem is not a competitor's carelessness, but a habit that shows up wherever red-team results get written up under deadline, regardless of who's writing them.

## What the section actually supports.

Here's what the card says directly: an automated internal test found a "very low attack success rate" for Opus 5's safeguards. The opening paragraph already covers the three external campaigns, and all four data points point the same way: none produced a working universal jailbreak. The one partial result, from Trajectory Labs, is the task-specific success the card itself flags as non-generalizing.

That's a real finding. Four independent efforts, using different methods, converged on the same practical outcome. Convergence across independent methods is strong evidence, stronger than any single number would be. But the card doesn't make the convergence argument. It doesn't say the three campaigns agree with each other and with the internal test, despite the mismatched units. The document states three facts in sequence and lets the reader assemble a conclusion the text never writes down. Are these three efforts even measuring related things, or just adjacent things? The card leaves that question for the reader. Most readers won't notice there's a question to answer.

I read the section twice looking for a sentence that ties the three together: a line stating these results are consistent with one another, or that the campaigns aren't directly comparable but each independently supports the conclusion. I found neither. What's there is a paragraph of clean, well-sourced facts that reads like a conclusion while skipping the work a conclusion requires.

## Why the missing exchange rate matters more here than it did for GPT-5.

The GPT-5 red-team hours measured a biology-specific jailbreak surface, tested by nineteen contracted PhDs against a threat model where one successful jailbreak is catastrophic. Opus 5's Section 3.5.2 measures cyber safeguards instead, a different domain with a different threat model. The stakes differ between the two. What repeats is the documentation practice: how the write-up handles incompatible units. This isn't the same finding recurring. The editorial shortcut is the same, only in a different chapter. That's worse. The shortcut isn't tied to one evaluator's blind spot. This gets written up as a genre: "we hired some outside people and they didn't break it," independent of what "it" is.

A technical reader treats this card as evidence to weigh rather than a marketing claim to accept. Read it that way and the missing exchange rate becomes the whole ballgame. I can't tell you whether 16 hours from 10a Labs is a stronger result than Trajectory Labs' 100 hours. I can tell you Trajectory Labs' 100 hours produced one caveat-laden partial result, and 10a Labs' 16 hours produced a clean negative. On its face, the shorter engagement looks like the stronger result. That's an accident of formatting, not a finding. A denominator exists to prevent that kind of flip.

## What I'd want instead.

This doesn't need more testing. It needs arithmetic, done in the document instead of left for the reader.

Whether the three campaigns count as independent confirmations of one thing, or as separate probes of different sub-surfaces that happen to share a chapter, changes the appropriate confidence language. The card doesn't say which.

An attempt could use a time equivalent. "150 attempts averaging N minutes each" turns Grayswan's number into something that sits next to hours without forcing a reader to guess.

Task-specific prompting bought Trajectory Labs one result. How many tasks did they attempt in total? A success rate of 1 in 5 reads differently than 1 in 40, and the card reports neither.

The card never says what would change the conclusion. If a fifth lab spent 200 hours and found nothing, would that add confidence? Or would the card treat it as redundant with the first three? A document that states what evidence would move it is a document a reader can calibrate against.

None of this requires new red-teaming. What it requires is treating the write-up as an argument that has to hold together. Right now it reads as a list of things that happened, credited to whoever did them, in order.

## A recurring thought.

I picked this document assuming Anthropic's system cards were the counterexample: the place where the discipline I asked OpenAI to show in August already exists. Mostly it does. The confidence intervals throughout this card are more careful than anything in the GPT-5 document, and I'll get to that in a separate piece. Section 3.5.2 is a reminder that "we're more rigorous than the other lab" is a claim earned section by section, every time. I'd rather find that out reading a system card than find it out on the job. If anyone from @Anthropic can show me the paragraph I missed, the one that reconciles hours and attempts, I'll update this piece and date the correction, the same way I said I would in August.