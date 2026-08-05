---
layout: post
title: "The Importance of Testing Your Code"
description: ghostwritten blog post
author: Jake Gaylor
date:   2024-01-04 05:42:26 -0500
categories: accountability testing unit integration end-to-end
---

What is the overarching purpose of this blog?

This blog exists to examine the role that personal accountability, effective communication, empathy and understanding, continuous learning and improvement, building trust and psychological safety, leadership and influence, and resilience & perseverance play in organizational success. And we hope you’ll find some lessons that prove useful in other areas of life.

Here’s a simple question: do you want to be better at what you do? Of course you do, right? (If not, click here [link to Arjun’s calendar] to talk about it.)

We do too, and we hope this blog benefits us both.

As we examine different aspects of SPEARs culture, dig into the role of privacy and security at Cloaked, and explain why we work the way we do, we ask that you keep an open mind and engage us in debate so that you/we/us all get better together.

Software Testing
Let’s start off talking about a subject that might involve some pretty strong opinions: Testing (and not the SATs). Let’s talk about software testing.

Stated simply, software testing is the process of evaluating and verifying that your code does what it is supposed to do. But the real power of software testing is its ability to help engineering organizations scale their time. As a startup, we work with limited resources and tight timelines. Things that scale our time are worth their weight in gold, so we should explore the role of software testing in Cloaked’s growth and success.

There are about a dozen different ways to apply software testing, including Unit Testing, Integration Testing, End-to-End Testing, System Testing, Performance Testing, Regression Testing, User Acceptance Testing, and more. For now, let’s investigate three types of testing (unit testing, integration testing, and end-to-end testing), and how they can help Cloaked get to market faster, with fewer defects, and less rework.

Let’s take a moment to define a few terms though
Time to Market is a measurement of how long it takes us to have an idea and deliver an implementation to production.
A test is a piece of code that asserts another piece of code behaves as expected.
A defect is anything that causes software to produce incorrect or unexpected results.

Unit Testing
Unit Tests confirm the behavior of a discrete component or piece of functionality in isolation. A unit test might test a function, a class, or a module, but the defining criteria requires that the unit be tested in isolation. Unit tests are code that gets committed at the same time as the code they test, and often run on the developer’s workstation, but it is a best practice to also run them in CI (when code gets
pushed to GitHub) before being merged.

Unit testing is our first line of defense, protecting us from introducing defects into trunk. By detecting and pinpointing defects, then addressing them before merging to trunk, you save yourself or a team member time spent debugging/troubleshooting in the future. Furthermore, well unit-tested code tends to be well factored which leads to improved code quality and reduces the cost of future code reviews. This facilitates development moving smoothly, and at a faster pace, while reducing the need for costly rework.

A thorough test suite gives us confidence that the unit of work is correctly implemented when we write it, and it also allows us to determine if we make a breaking change later. By going a step further and writing tests for features before coding them, we determine when our implementation is correct. (If this sounds interesting to you, you might like Test Driven Development [https://martinfowler.com/bliki/TestDrivenDevelopment.html]).

Integration Testing
Integration testing ensures that a group of units work together as intended. This type of testing is very broad and pieces of it often get mixed up with unit testing, while other pieces get confused for end-to-end-testing. The defining features of an integration test are 1) that it tests multiple units working together to create the desired result, and 2) that it doesn’t test the entire system, but focuses instead on the integration of two or more units to perform a single function.

At Cloaked we use integration testing to make sure that our individual products work as expected when run in isolation, testing the integration of the units composing our application into a functioning product. We often run these tests in the same suite as our unit tests because the biggest difference between integration testing and unit testing is the setup of the test case.

Integration testing can also be used to test multiple products together, as in the case of dashboard and api. A well written integration suite will provide us with confidence that changing a dependency in a system will not introduce a defect.

End-to-End Testing
End-to-end testing ensures that the entire system functions as expected when connected together. These tests drive our client applications in an automated way and ensure that the expected results appear on the screen in response. The defining feature of end-to-end tests is that none of the systems are mocked out. The test is as close to a real user’s experience as we can get.

End-to-end testing at Cloaked is a work in progress, and currently takes many forms. Our regression testing efforts, the smoke suite, feature testing in dev, and Playwright each play a role in our end-to-end testing. By running end-to-end tests against pre-production environments we gain confidence that we can promote the code to production without introducing defects. By running those same tests
against the production environment we can alert on-call engineers when the system starts
failing to work as intended.

Conclusion
Now that we’ve explored the different ways that software testing can help save you time, release software faster, and with fewer defects, we hope you agree with us that this is an investment worth making. SPEAR can help you get started with software testing, or help you explore ways to take your game to the next level. Please reach out to us in #team-spear to talk about any projects where you might want to collaborate.

Do you know of any other ways we can leverage testing to help Cloaked? Are we getting the benefits available to us using unit, integration and e2e testing? Are there some quick wins we can get? We’d love to hear about it.

I know we left a lot unexplored in this article, but we will continue to share our thoughts on testing in the coming weeks. Let us know what you’d like to hear more about. On the list are a dive into the different ways that QA, QE, and SDET skill sets can help us, exploring the capabilities of Playwright, and talking through the challenges that face different types of product teams.

We will explore the muddy waters between QA and Security Testing in a live demonstration on August Xth so come see us in https://securitywarroom.com.