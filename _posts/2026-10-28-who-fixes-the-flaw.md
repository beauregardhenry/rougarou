---
layout: post
title: "Finding the Flaw Is Getting Easier. Who Has Time to Fix It?"
description: "AI can find vulnerabilities faster, but maintainers and operators still need the time and resources to turn discoveries into protection."
author: Beau Henry
date: 2026-10-28 08:00:00 -0500
categories: ai-security open-source vulnerability-management
image: /assets/img/finding-the-flaw-hero.png
sources:
  - title: "PHP: 2026 News Archive"
    url: "https://www.php.net/archive/2026.php/"
    note: "Documents the October 21 security releases and the recommendation to update immediately."
  - title: "Wiz: PHP2Shell"
    url: "https://www.wiz.io/blog/php2shell-php-rce"
    note: "Describes the vulnerabilities, their history in PHP, and how Wiz used AI during its research."
  - title: "OpenAI: Patch the Planet"
    url: "https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/"
    note: "Describes the coordinated PHP response, maintainer support, subsidized Daybreak access, and the proposed response framework."
  - title: "Google Cloud: Responding to Core PHP Vulnerabilities"
    url: "https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619"
    note: "Describes the vulnerabilities and AI contributions to detection and patch validation."
  - title: "CERT-EU: Critical Vulnerabilities in PHP"
    url: "https://www.cert.europa.eu/publications/security-advisories/2026-018"
    note: "Advises immediate patching and recommends considering isolation when prompt patching is not feasible."
  - title: "Reuters: Governments, Companies Take Websites Offline over PHP Flaws"
    url: "https://www.reuters.com/technology/websites-taken-offline-over-php-risks-2026-10-21/"
    note: "Reports precautionary shutdowns of websites and services following disclosure."
---

On October 21, PHP shipped emergency patches for two critical remote code execution flaws. Much of the web runs on PHP.

Two teams found overlapping vulnerabilities independently. Calif identified one using OpenAI's GPT-5.6 Sol through OpenAI's Patch the Planet program. Wiz reported both, also using AI in its research. PHP's maintainers led the fixes and release, while OpenAI, Wiz, Cloudflare and others contributed research and coordination.

Wiz said the underlying flaws had been present in PHP's codebase for more than a decade. Finding them is a real result. What happened after the discovery shows how much work it takes to turn that result into protection.

## A finding is a work order

A vulnerability report arrives as a claim. Someone has to confirm it and establish which versions are affected. Maintainers then need a fix they can test, along with a plan for telling people who depend on the software.

The independent discoveries also raise a harder possibility: someone looking to exploit an overlapping flaw might be able to find it too. We do not know when that might happen. The possibility makes the time needed to prepare and deploy a fix consequential.

AI can help after discovery. Wiz used models in its exploit research, and Google Cloud reported AI contributions to attack detection and patch validation.

I want to know how much capacity those tools add across the response. More findings give defenders more to work with, but the people receiving them still need time to act.

## A patch has to reach the system

PHP urged users to update immediately. CERT-EU advised organizations that could not patch promptly to consider isolating affected internet-facing applications until they could apply and verify a fix.

Government agencies and other organizations across Europe took services offline as a precaution.

Inside each organization, someone had to determine which systems were exposed. The update then had to be deployed and checked. Taking a service offline could reduce exposure while that work was underway, but it could also interrupt a service people depended on.

A released patch makes a fix available. It does not tell us how far the fix has traveled.

## What the support buys

OpenAI's account takes the capacity problem seriously. It describes funding for maintainers and hands-on engineering support. Model access is part of the response, including a $1 billion commitment in subsidized Daybreak access for organizations protecting essential services with limited security resources. OpenAI also proposes a framework for coordinating responses and asks the security community for feedback.

I would like to know how that support reaches the work.

Paid maintainer time creates room to investigate and review a report. An engineer can help develop a fix or test it against supported releases. The organization installing that fix may need help locating an old deployment that nobody realized was still running.

Each form of support buys something different. A well-supported response to one emergency does not establish that the same help will be available for the next.

## Count the work through to protection

OpenAI has asked for feedback on its framework. Put the later stages in the count.

A count of confirmed findings and released fixes tells us what researchers and maintainers accomplished. Where providers or operators can observe deployment, report how many affected systems received the fix and how long remediation took. Report protective measures such as isolation, too, with their limits.

Maintainers may not know who runs their software. Providers may see only their own customers' systems. Any number published should make that scope clear.

This is harder than counting vulnerabilities. It gets us closer to knowing whether the response reached the people exposed.

There is a familiar operational mistake here: increase the output of one stage and assume the people downstream can absorb it. Their backlog becomes the place where the improvement stops.

Finding a serious flaw is valuable. The value reaches users through the people who fix it and the people who install the fix. The next announcement should say who they are and who is paying for their time.