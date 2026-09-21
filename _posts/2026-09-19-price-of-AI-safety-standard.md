# The Price of an AI Safety Standard

Last week I tried to compare three outside red-team campaigns in [Anthropic’s Claude Opus 5 system card](https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf). Trajectory Labs spent close to 100 hours. 10a Labs reported about 16 hours of manual testing and also used an automated attacker. Grayswan’s effort appears in a different unit: 150 automated attempts per task. The results sit together in the card’s safeguards section, but the reported effort gives readers no common basis for comparing them.

I wrote about that gap because a result means less when you cannot tell how hard someone looked for a failure. Anthropic was reporting voluntary testing of its own model. Now imagine an outside assessment becoming a condition of releasing a model. Whoever defines the required work would also influence what it costs to enter the market.

That is where [Ben Shapiro’s warning](https://www.dailywire.com/episode/ben-shapiro-show-ep-2506) about regulatory capture hits hardest. He suspects the largest AI labs want safety rules that protect their lead. I cannot establish that by guessing what their executives believe about AI risk. Their policy proposals give us something better to examine.

## Read the proposal

[OpenAI’s September policy statement](https://openai.com/index/ai-policy-window/) calls for mandatory federal requirements tied to a model’s capabilities. It proposes common testing and independent assessments. It also says the rules should apply to a handful of well-resourced labs at the frontier, spare smaller developers operating below it, preserve room for open-weight models, and avoid entrenching incumbents.

I take those commitments seriously. I would also like to see how they survive the drafting process.

A developer approaching the frontier needs a reasonably predictable way to know when the obligations begin. Its capabilities may only become clear after training, so the law also needs a workable transition when a model crosses the threshold. Otherwise, a company could learn late in development that releasing its model requires an assessment it never planned or budgeted for.

The assessment itself needs a defined method. My problem with the Opus 5 card was never that its outside teams failed to try hard enough. I could not tell how to weigh one team’s hours against another team’s automated attempts. Once an evaluation has legal force, leaving the required level of scrutiny vague becomes much harder to defend. Two developers could both receive an “independent assessment” while facing very different amounts of work.

## How a private practice becomes a public rule

OpenAI’s statement describes another route worth watching. The company says it is developing its own framework for monitoring and reporting serious model behavior, and hopes that work can inform federal policy. It also wants to develop voluntary monitoring standards with other frontier labs. OpenAI says those standards would complement federal safeguards and democratic oversight.

Monitoring and an independent release assessment are different requirements. Both raise a question about who establishes the method. If a practice developed by the largest labs later becomes the expected way to comply with a federal rule, those labs will already have people and procedures in place. A new lab reaching the frontier would likely have to build them. The size of that burden depends on the rule’s details; no one has established it from the policy statement alone.

This is a more useful way to investigate Shapiro’s concern than an argument about whether AI executives are sincere. OpenAI has said it wants to avoid entrenching incumbents. The method adopted, and the cost of complying with it, will show whether that promise holds.

[Competition authorities in the United States, United Kingdom, and Europe](https://www.ftc.gov/system/files/ftc_gov/pdf/ai-joint-statement.pdf) have warned that established firms can extend their advantages through control of computing resources and distribution. Their statement does not find that safety assessments have this effect. It does give us reason to ask whether a new compliance cost would add to advantages already in place.

## Keep the safety question in view

Shapiro also asks for a credible account of the danger these rules are meant to address. The [2026 International AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) says current systems lack the capabilities needed for a loss-of-control scenario, while relevant capabilities are improving. Experts disagree about the likelihood and timing of future catastrophic harm.

That uncertainty is a reason to examine capabilities carefully. It is also a reason to be precise about what an assessment measures. A result that can stop a release should give the public enough information to judge the method behind it.

Shapiro describes closed-model companies as having an interest in restricting open models. Their public positions are more complicated. [Anthropic’s CEO says](https://www.anthropic.com/news/position-open-weights-models) the company has never advocated a ban on open-weight models, and calls for testing sufficiently capable open and closed models alike. OpenAI’s proposal explicitly says open models have a place in the market. Those statements deserve to be included in the argument. The requirements eventually written into law will tell us more about their effect on competition.

I could support a mandatory assessment that measures a defined risk and gives developers a fair way to prepare. Before making one a condition of release, lawmakers should publish the method and estimate what it would cost a capable new entrant to comply. A developer that fails should learn enough to address the finding and try again.

Shapiro identified a possible failure in AI regulation; he has not shown that the labs are already engineering it. OpenAI says its proposed rules should protect competition. I would hold it, and any government that adopts those rules, to that promise. Show us what the assessment requires. Show us what a lab outside the room where it was designed would have to pay. Only then can we judge whether the rule buys safety at a price the public should accept.