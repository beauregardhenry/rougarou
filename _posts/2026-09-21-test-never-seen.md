---
layout: post
title: The Test the Lab Never Sees
description: DeepMind protected a private benchmark and proprietary model weights inside one sealed evaluation. The public still needs a receipt showing what happened there.
author: Beau Henry
date: 2026-09-21 09:00:00 -0500
categories: ai-safety evaluation privacy reproducibility accountability
image: /assets/img/the-test-the-lab-never-sees-hero.png
sources:
  - title: "Google DeepMind: Technical report on double-blind AI evaluations"
    url: "https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/piloting-the-worlds-first-double-blind-ai-evaluations/double-blind-evaluations-technical-report.pdf"
    note: "The primary source for the secure-enclave design, attestation process, participant roles, and implementation limits discussed in this essay."
---

Google DeepMind recently ran Gemini 2.5 Flash Lite against a benchmark Google could not inspect. The evaluator never took possession of the model weights. The two met inside a temporary encrypted environment, and the team shut that environment down when the run ended.

The [technical report](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/piloting-the-worlds-first-double-blind-ai-evaluations/double-blind-evaluations-technical-report.pdf) does not publish a model score because the evaluation process was the object of the experiment. The team wanted to know whether an outside evaluator could test a proprietary model without handing its private questions to the company that built it or receiving the company's weights in return.

The pilot solved that exchange problem and left the evidence problem intact. Readers still need to know what ran, what the protected environment proved, and where trust remained.

Private benchmarks lose value once their questions reach a model developer. A prompt can enter a training set deliberately, leak into one accidentally, or influence post-training after engineers see where the model failed. Contracts and zero-logging agreements reduce that risk while still asking the evaluator to trust the company holding the logs.

Model developers face the corresponding problem. Frontier weights contain valuable intellectual property and capabilities that could be misused if they escaped. Most companies will not hand them to every outside group that wants to preserve the secrecy of a test.

A secure enclave gives both sides what they need without requiring either to surrender what it needs to protect.

## Two secrets in one machine

DeepMind and its partners at OpenMined, AVERI, MLCommons, and the Singapore AI Safety Institute built the pilot around a secure enclave. The model weights entered through an encrypted connection. A reserve set of private AILuminate prompts entered separately. According to the report, no model had previously processed those prompts.

Before either party released its material, the enclave produced a signed account of the software it was running. Each party could compare that account with the software it had agreed to use. The model and benchmark met only after those checks passed. AVERI received and scored the outputs, and the team decommissioned the temporary environment after the run.

That is more useful than a promise that nobody looked.

In this pilot, attestation recorded the approved software and memory encryption protected what moved through the enclave. The assurance extended only as far as the code participants could inspect and the services they still had to trust. Cryptography made those boundaries easier to locate. It did not remove them.

## Where the protection stopped

The report is unusually direct about those boundaries.

Running Gemini entirely through inspectable, open-source methods required more engineering work than the project could support. Some proprietary implementations remained outside the allowlist review. AVERI knew that and accepted the setup.

The guest operating system's source is open, and its build process receives outside checks. Individual builds still cannot be reproduced independently because private signing keys are involved. Google services also signed and verified the attestation report, leaving Google inside part of the verification path.

At the lowest level, the arrangement assumes the cloud provider and hardware manufacturer will not collude. Closed firmware remains an input the other participants cannot rebuild. Higher in the stack, legal agreements and human code review consumed more effort than the additional computing did.

Those limits define what the cryptographic guarantee can carry. The environment can establish that agreed code ran under protected conditions. It cannot establish that every component was independently inspectable or that every participant disappeared from the chain of trust.

The report earns confidence by saying so.

## A clean run can still support a weak claim

The enclave protects the integrity of an agreed procedure. It does not establish that the procedure was good.

A benchmark can remain perfectly secret and still measure the wrong capability. Its prompts may cover the domain poorly. Its scoring rule may flatten an important difference. The evaluator might test a model snapshot or configuration that differs from the product people will use. None of those failures requires anyone to steal the questions or tamper with the run.

Encryption also leaves selective reporting untouched. The paper opens with an example of a frontier lab testing many private model variants on a public arena and publishing the best performer. A double-blind system can attest to every run it executes. It cannot force the company to disclose those runs unless the evaluation agreement requires it.

That becomes consequential when a result informs a release decision. A lab could submit one model variant, receive an unfavorable result, make changes, and return with another. There may be good reasons to do that. Safety work should improve the model. The public report should still say how many versions entered the process and which result belongs to the released system.

The parties also decide who receives the result. A protected computation that sends an aggregate only to the model owner creates a different kind of accountability from one that gives the evaluator the raw outputs and the right to publish its conclusion. The enclave can execute either arrangement faithfully. The arrangement itself remains a governance choice.

## Publish the receipt

Keeping the benchmark private changes what another reader can reproduce. The prompts cannot appear in an appendix, and most researchers cannot rerun a frontier model from its weights. Conventional open reproduction is unavailable by design.

A public receipt can replace the parts of ordinary reproduction that secrecy removes.

The receipt should identify the model snapshot and explain how its configuration relates to the deployed product. If the evaluation used a helpful-only variant, an unreleased checkpoint, or different system settings, the report should say so where it reports the result.

The benchmark can remain sealed while the report names its version, the origin of its reserve set, and the scoring procedure. Hashes can identify the evaluation code and attested runtime without exposing either party's protected material. Any proprietary component that escaped inspection belongs in the same account, along with the party that accepted it.

Readers also need the history surrounding the result. The receipt should say whether other model variants were run and whether every completed run entered the record. It should identify who saw the raw outputs, who applied the scoring rule, and who received the final result.

None of this reveals a private prompt. All of it changes how much weight the finding can bear.

An authorized evaluator could repeat the sealed test against the same attested model. A technical reviewer could inspect the public portions of the environment and compare the recorded fingerprints. The questions would remain useful, and the procedure would become easier to check.

## What the lock should mean

The report's authors want double-blind evaluation to become simple enough that people recognize its assurances the way they recognize the HTTPS lock in a browser.

The analogy sets the right limit. A browser lock establishes a narrow fact about a connection and the identity attached to it. It does not certify that the website is honest.

A double-blind evaluation mark should carry an equally precise meaning. It can establish that the model owner did not receive the private benchmark and that the evaluator did not take possession of the weights. A stronger implementation may also establish that both parties approved the code and that the recorded computation ran without alteration.

The mark cannot validate the benchmark, connect the tested model to the product in use, or show that an unfavorable run was not withheld. The public receipt has to carry those claims.

I want this approach to become standard for high-stakes evaluations. DeepMind's pilot gives outside evaluators a better way to protect their questions while testing models they do not own. Its technical report earns confidence by showing the machinery and documenting where the first implementation fell short of its own ideal.

The next version should preserve that discipline in the public record. DeepMind has shown that private questions and private weights can meet without either party taking custody of the other. A benchmark can remain private without turning the safety case private too.