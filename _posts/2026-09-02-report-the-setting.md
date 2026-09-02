Somewhere in the GPT-5 system card a footnote exists that should be a standard.

The card reports a SWE-Bench result, then explains every preparedness evaluation in the document ran at the model's maximum trained-in verbosityj (which is higher than the "high" setting available in the API). The 74.9% figure published in the GPT-5 launch blog post ran at the API default. It adds, plainly, that changes in verbosity potentially lead to variation in eval performance.

Two numbers exist in public. Same model; same benchmark. Instead of hoping nobody put them side by side, the authors explained the discrepancy before anyone found it.

That footnote is only sixty words or so and converts a future correction into a present disclosure; it should teach the reader about the brittleness of benchmark numbers.

The card employs footnotes elsewhere to similar effect.

The multimodal virology evaluation notes that prior system cards reported a single-select variant; SecureBio has since updated the eval to a harder multi-select variant and the card plots the new version on SecureBio's recommendation. In a single sentence,anyone who planned to comparfe this year's number to last year's getstold that they simply cannot.

Under methodology notes, the footnote explains that the 95% confidence intervals come from a bootstrap that resamples model attempts per problem, then says the quiet part: this method captures sampling variance but not problem-level variance, and can produce overly tight intervals, with pass rate near 0% or 100% within a few attempts.

Read that again. The document tells you its own error bars are too narrow, and where. Would most readers notice? This might just be the most trustworthy paragraph in the section.

Here is the general form:

Every benchmark number is a number under a configuration. Verbosity setting? Temperature? Was browsing enabled? What was blocklisted? How many rollouts? Was the reported metric pass@1 or pass@12 across the best set? Which variant of the eval, from which version of the dataset, and on what date? Wasb the model deployed the version or a helpful-only variant? Was the monitoring stack was on?

Change any one of those variables and the number moves - sometimes a little, and  sometimes clear across the threshold the number exists to inform.

A benchmark result reported without its configuration is not a result; it is an anecdote wearing a decimal point, and it will be quoted for two years by people who have no way to reproduce it and no idea they can't.

Report the setting right next to the number, not in an appendix.

A paragraph is not necessary, just a single line. Something along the lines of pass@12 over 16 rollouts, max trained-in verbosity, browsing off, dataset v2.1, July 2026 — dense and ugly, but completely sufficient.

A natural oobjection is that this clutters the document, which, of course, it does. However, the alternative is a document that reads cleanly but cannot be checked or independently verified, which is a terrible trade no matter how you look at it, because the whole purpose of publishing eval numbers is to let people outside the building verify and reason about them.

A second natural objection: nobody reads that line. Mostly true, but also irrelevant. The line is not there for the median reader; t is there for the one person who tries to reproduce the result, and for the version of you eighteen months from now who needs to know whether this year's number and last year's are the same measurement.

But maybe I'm a bit biased here, after spending eight years around methods sections in medical research, where the configuration is the paper — the dose, the assay, the antibody, the machine, the lot number — where a result reported without this information is not publishable, because it contains no information.

Frontier evaluation is a young field, but I think it needs to apply a similar level of rigor. The field already imported the good instinct. Take the next steps. The verbosity footnote, the dataset-change note, the confidence interval caveat — those were written by people who understand exactly what I'm asking for, and who did it without being asked.

Make rigor and honesty a rule, not just a habit; habits are the first to go when a launch is late.