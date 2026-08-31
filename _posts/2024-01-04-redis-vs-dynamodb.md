---
layout: post
title: "Redis vs Dynamo DB"
description: How to Pick a Fight
author: Beau Henry
date:   2023-09-10 05:42:26 -0500
categories: war saas business agile innovation boring
---
<p style="text-alighn: center;">
Manifesto for Agile Software Development
We are uncovering better ways of developing software by doing it and helping others do it.
Through this work we have come to value:
Individuals and interactions over processes and tools
Working software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over following a plan
That is, while there is value in the items on the right, we value the items on the left more.
Kent Beck, Mike Beedle, Arie van Bennekum, Alistair Cockburn, Ward Cunningham, Martin
Fowler, James Grenning, Jim Highsmith, Andrew Hunt, Ron Jeffries, Jon Kern, Brian Marick,
Robert C. Martin, Steve Mellor, Ken Schwaber, Jeff Sutherland, and Dave Thomas”
https://agilemanifesto.org/
</p>

---
***
---

## How to Pick a Fight: Strong Opinions Held Loosely
## On Technical Debt
Ward Cunningham, one of the Agile Manifesto authors, in explaining to his boss why he needed to spend time refactoring, said that some problems with code are like financial debt, in that it is alright to borrow against the future so long as you pay it off. In doing so, he coined the term <em>Technical Debt</em>.
At its core, technical debt is a useful tool to talk about the need for refactoring and improving source code and its architecture. But, as Ward explains, technical debt also provides a valuable way to talk about “...team commitments, goals alignment, and code quality across organizational
boundaries.” Pretty cool.

Code incurs technical debt from a wide variety of issues related to structure, duplication, (lack of) test coverage, comments, documentation, bugs, complexity, discipline, and style, just to name a few sources. Each of these problem categories accumulate technical debt because they hinder overall productivity and the pace at which the organization can deliver new features. Technical Debt also emerges during the product life cycle. As you gain understanding of your product needs, you may begin to feel your initial infrastructure like a dragging anchor slowing the company down. Suboptimal infrastructure leads to time and money spent overcoming unnecessary complexity and draining resources from high value strategic initiatives (what you should really be focusing on). This, in turn, hurts Cloaked’s ability to compete in the market. We could free that time and focus on making data-driven decisions with insights gained from Honeycomb’s telemetry, instead of paying off technical debt.

## On Innovation
Chooing a new tool is an inflection point with respect to technical debt because choosing the wrong tool has serious implications for the work an engineering team is able to complete. While new tools run the risk of hindering productivity, if incorporated in a smart way the new tools will be manageable and beneficial. Make sure you’re picking tools that fit architecturally, are actively maintained, and most importantly, do what you need them to do (so think about volume/scale).

Dan McKinley was a software engineer at Etsy for six years. During his time there, Etsy was known for having a highly productive engineering team. His teams’ success did not just come from the code they wrote, but from their philosophy and culture.

Part of that philosophy included <em>Innovation Tokens</em>. Learn more in his piece, Choose Boring
Technology.

To paraphrase Dan, Cloaked gets three Innovation Tokens. Spend the tokens as you will, but once they are spent there are no more innovation tokens to spend for a good long while. The point? Choose boring technology, because the number of places where the company can truly innovate are much more limited than you might think.

It would be nice to live in a world where you could simply choose the best tool for the job, but many times the best tool for the job isn’t widely known within the organization. Technology that requires us to stub our toes, train the team, and integrate deeply into our daily workflow is exactly the kind that can cost an Innovation Token. Reality at Cloaked requires decision-making that sets the company up for long term success without interrupting the short term.

## The Rise of Redis
Now that we’ve talked about two forces that fight technology adoption, technical debt and <em>innovation tokens</em>, let’s talk about Redis.

Redis is absolutely awesome at what it does. It is a “...fast (sub-millisecond response times), open source, in-memory key-value data structure store that is useful as a database, cache, message broker, and streaming engine.” Redis is broadly known by engineers and is cheap and easy to get started with. It can be run locally, in CI, and managed for us in AWS, so it is easy to understand why we use Redis for caching and for our work queues as those needs arose.

But, using Redis comes with a few important pain points: it does not natively provide access control, is not secure by default, is prone to data loss under specific circumstances, is targeted by sophisticated malware, and scaling it is difficult (involving sharding, HAProxy, Redis Sentinel, and convoluted AWS integrations).

While untested code incurs technical debt, so does untested automation. Testing infrastructure automation has been historically difficult and prohibitively expensive in terms of man hours, so our tools to scale Redis will continue being a source of technical debt.
Old school technologies (like those based in data centers) developed for use on racked bare metal servers, require a different thought process than modern, fully managed serverless cloud technologies. As we already mentioned, scaling a Redis cluster is an undertaking, and since it requires more RAM to scale, it is expensive too. In a cloud native serverless environment scaling just happens, and it happens without technical debt or <em>cognitive overhead</em>.

Effortless scaling is just one of the many reasons cloud native tools are dope. A few more reasons: they facilitate building highly flexible, resilient applications while increasing development efficiency, reducing costs, and maximizing availability for customers. The best part? Cloud native tools have reached a level of maturity that means serverless tools can be implemented without costing Cloaked an innovation token. See? Dope.

## Exploring AWS Tools
## DynamoDB
From AWS: “Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-Region replication, in-memory caching, and data import and export tools.”

Breaking that down, serverless means nothing to provision, patch, or manage, no software to install or maintain, no versioning, no maintenance windows (zero downtime), and use can scale to zero. Key-value NoSQL database sounds a lot like Redis, yeah? But did you catch the fully managed part? That means super low technical debt. And if you have a need for speed DAX (DynamoDB Accelerator) is a fully managed in-memory cache that improves DynamoDB performance from millisecond to microsecond latency.

Encrypted at rest means the services meet compliance and regulatory requirements. We can
choose to use AWS-owned keys (default), AWS-managed keys, or customer-managed keys,
with AWS Key Management Service provided at no more charge.
Point-in-time Recovery means we can restore the table to any point in time, down to the second,
for the preceding 35 days using a single API call, with no impact on performance or availability.
Finally, IAM roles allow us to delegate access to just those applications that need it.

## SQS
Utilizing the fully managed AWS Simple Queue Service means we can reliably deliver large volumes of data, at any level of throughput, without losing messages or needing other services to be available. We can securely send sensitive data between applications and centrally manage our keys using AWS KMS. SQS scales elastically and cost-effectively based on usage so we don’t have to worry about capacity planning and/or pre-provisioning.

## Consummatum Est
Having introduced several concepts, like The Agile Manifesto (emphasis on individuals, interactions, and responding to change), technical debt, and innovation tokens, we hope you understand (or at least can appreciate) why it is time for Cloaked to pivot away from Redis towards the AWS ecosystem of fully managed, serverless, cloud-native tools. When complete, the pivot will reduce engineering’s cognitive load and Cloaked’s overall technical debt, setting up our company to seamlessly handle the anticipated surge of paying customers. This blog is about creating a healthy dialogue, so we would love your feedback if you’re feeling froggy. 

Thoughts? Comments? Suggestions? Please reach out.