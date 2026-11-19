---
layout: post
title: A Detector Score Is Not a Verdict
description: Turnitin's own instructions say not to discipline a student on its AI score alone. Adelphi did anyway, and a judge annulled the finding. A school should be able to show how it knows before cheating goes on a student's record.
author: Beau Henry
date: 2026-11-19 08:00:00 -0600
categories: ai-detection education academic-integrity evaluation
image: /assets/img/a-detector-score-is-not-a-verdict-hero.png
sources:
  - title: "Matter of Newby v. Adelphi Univ., 2026 NY Slip Op 26021 (Sup. Ct. Nassau County, Jan. 28, 2026)"
    url: "https://www.nycourts.gov/reporter/3dseries/2026/2026_26021.htm"
    note: "Annuls Adelphi's academic integrity finding and appeal denial and orders the record expunged. Source for the 100% Turnitin score, the two parent-run detectors, the professor's follow-up email and the procedural findings."
  - title: "Turnitin: Using the AI Writing Report"
    url: "https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report"
    note: "States that the AI writing detection model may misidentify text and should not be used as the sole basis for adverse actions against a student."
  - title: "Turnitin: AI writing detection model release notes"
    url: "https://guides.turnitin.com/hc/en-us/articles/28294949544717-AI-writing-detection-model"
    note: "July 16, 2024 release: scores from 1% to 19% no longer surfaced on new reports because of higher false positives in that range. Earlier reports still show them with an asterisk."
  - title: "Liang, Yuksekgonul, Mao, Wu and Zou: GPT detectors are biased against non-native English writers (Patterns, 2023)"
    url: "https://doi.org/10.1016/j.patter.2023.100779"
    note: "Seven detectors averaged a 61.3% false-positive rate on 91 human-written TOEFL essays and were near-perfect on 88 U.S. eighth-grade essays. Simplifying the U.S. essays' word choices increased misclassification."
---

A freshman turns in a history essay. His professor runs it through an AI detector, and it reportedly comes back 100% AI. The student says he wrote it himself, with help from a university tutor. He gets a zero.

That happened to Orion Newby at Adelphi University. Newby is autistic and was enrolled in Adelphi's support program for students on the spectrum. He brought results from two other detectors that rated the same essay human-written. The school denied his appeal anyway. In January, a New York judge annulled the finding, called it "without valid basis and devoid of reason," and ordered Adelphi to expunge his record. ([CBS New York](https://www.cbsnews.com/newyork/news/orion-newby-adelphi-university-ai-plagiarism-accusations), [Plagiarism Today](https://www.plagiarismtoday.com/2026/02/11/adelphi-student-wins-ai-plagiarism-lawsuit/))

The judge didn't rule on whether detectors work. The ruling faulted the school for ignoring the evidence Newby offered. That's the part worth paying attention to. The software produced a number. People at the school treated the number as an answer.

Here's my position. No school should discipline a student on an AI detector score. Detectors aren't worthless. But the accuracy figure a vendor publishes answers a different question from the one a teacher is asking.

## The number and the question

Turnitin is the detector most schools use. It says its document false positive rate is under 1% "for documents with over 20% of AI writing." ([Turnitin](https://www.turnitin.co.uk/blog/ai-writing-detection-update-from-turnitins-chief-product-officer))

I read that sentence several times. A false positive is a human-written paper flagged as AI. A human-written paper has no AI writing in it. So what is over 20%? My best reading is the detector's own score: when Turnitin reports 20% or more, it's wrong about a fully human paper less than 1% of the time. Below 20%, Turnitin says false positives are more common.

Grant the number anyway. It tells you how often an honest paper gets flagged. That's the vendor's question. The teacher holding a flagged paper has a different one: did this student cheat?

The answer to the second question depends on something the first leaves out. How many of your students used AI at all? If almost none did, most of your flags will land on honest work, even with a low error rate. The detector can't know that about your class. You might.

## Small rates, real students

One percent sounds small until you count papers. Turnitin's detector processed 38.5 million submissions in its first six weeks. ([Campus Technology](https://campustechnology.com/Articles/2023/05/Turnitin-Says-Its-AI-Detector-Analyzed-38M-Submissions-in-Six-Weeks.aspx?Page=2)) Picture a university that runs 20,000 honest essays through it in a semester. At 1%, about 200 students who did nothing wrong get flagged. Each one sits across from a teacher holding a printout and tries to prove a negative. Turnitin said it plainly in 2023: behind each false positive is a real student.

The errors don't fall evenly, either. A 2023 Stanford study tested seven popular detectors on essays written by non-native English speakers. On average, the detectors labeled 61% of those human essays as AI-generated. On essays by U.S. eighth graders, they almost never made that mistake. ([Liang et al., summarized by CASRAI](https://casrai.org/news/ai-detector-false-positive-controversies-2026)) Simpler vocabulary and plainer sentences read as machine writing. That describes a lot of people writing in their second language.

Turnitin wasn't one of the seven. Its own 1% comes from a test on 800,000 academic papers written before ChatGPT existed. Your classroom is not that test set.

## The tools keep changing

OpenAI released its own detector in January 2023. By July it was gone, "due to its low rate of accuracy." ([The Register](https://www.theregister.com/2023/07/26/openai_ai_classifier/)) Some universities have switched AI detection off. Curtin University in Australia turned off Turnitin's AI feature at the start of this year.

Turnitin has updated its model several times since launch, including twice this year. Its release notes say old reports aren't rescored after an update. ([Turnitin release notes](https://guides.turnitin.com/hc/en-us/articles/28294949544717-AI-writing-detection-model)) The same essay can get a different score depending on when it was submitted. A number that moves with the software version isn't a fact about the student.

## "So we do nothing?"

This is where teachers push back, and I understand why. Many are grading stacks of essays they suspect a chatbot wrote. "Don't discipline on the detector" can sound like "give up."

It doesn't mean that. Treat the score as a reason to look closer, never as the finding. Then look at evidence a student can respond to. Ask for drafts or the document's version history. Sit down for ten minutes and have the student walk you through the argument and where the sources came from. A student who wrote the paper can usually do that. A student who pasted it usually can't.

That takes longer than reading a number. It should. A cheating finding can follow a student onto a transcript and into every application after it. They're owed a process that weighs their side. Adelphi's didn't, and a judge said so.

The detector can tell you how often it's wrong about honest papers. It can't tell you whether this student wrote this one. Only a person looking at the work can.