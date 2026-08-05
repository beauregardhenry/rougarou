Hey Team,

Recently, we've been talking about how getting to 10,000 users is the next goal for Cloaked. I've been thinking about the obstacles we have in our way and have identified some work that I think will have an outsized impact, and I wanted to explain why I think this work is so important.

Finding product market fit is critical for the success of Cloaked. That means finding the set of features, the marketing, the customer base, and the business model that will make Cloaked a financially viable business. Paul Graham thinks about startups in terms of being “default dead” or “default alive,” defining the difference as whether the startup reaches profitability with the funding they currently have in the bank. When a startup is default alive you can talk about ambitious goals. When a startup is default dead the entire focus MUST be on becoming default alive.

He was talking about finding the product market fit.

We have not found product market fit, yet. On our journey to finding it, we will make countless changes to the product. We hope that these changes improve customer acquisition and activation, but right now, we can’t distinguish between success and failure. We need to be able to measure the impact of our changes, so that we can revert the failures and double down on our successes.

One method of measuring the impact of our product changes involves serving different versions of the product to different users. We can then measure the success of our changes by comparing the behavior of the users who saw the changes to the behavior of the users who didn't see the changes. This is called A/B testing.

To facilitate A/B testing we use a tool called feature flags. Feature flags provide a way to turn features on or off for different users. Our feature flag engine, provided by posthog, allows us to create cohorts of users, then turn features on or off based on cohort. Client applications (mobile app, dashboard, and extension) then receive posthog’s feature flags in their user metadata, provided by the backend API, and use the flags to determine which features to show the user.

In order to run a valid experiment, we need to be able to measure the results. By setting expectations for our results, we know what to measure to help us determine success or failure.

Defining success for our current experiment (using feature flags to A/B test): we expect to be able to run more experiments than we do currently, and we expect measurable results. We will know the proposed methodology was successful when Cloaked increases the frequency of its data driven product decisions.

I hope everyone starts thinking about the work we're doing as a series of experiments, instead of taking for granted that our work simply has to be valuable, because it doesn’t. By considering our work an experiment from the outset, we can judge the success of a feature against Key Performance Indicators to determine if the feature is worth continued investment. (KPIs include number of feature flags created, number of experiments run, and percentage of new product decisions informed by the results of experiments.)

A/B feature flag testing will definitely help us find product market fit faster, and get to 10,000 users, which means we are default alive and able to constructively talk about more ambitious plans.

Thanks,

Jake
