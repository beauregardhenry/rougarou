# Source review — September 16, 2026

Primary-source links have been added to six AI evaluation essays. Typos in “The Configuration Is the Finding” and the description of “Calibration is an Operations Problem” have been corrected. The existing arguments have not been rewritten.

## Verified against the original documents

Sources: [OpenAI's original 60-page GPT-5 System Card](https://cdn.openai.com/gpt-5-system-card.pdf) and [Anthropic's Claude Opus 5 System Card](https://anthropic.com/claude-opus-5-system-card). Page references below are PDF page numbers, which differ from the printed GPT-5 page labels by one.

- GPT-5 expert baselines: 80% consensus and 63% for the 80th-percentile PhD comparison; no tested model beats the former and all beat the latter (pages 26–27).
- GPT-5 configuration disclosures: the confidence-interval caveat (page 23), the single-select to multi-select virology change (page 25), and the maximum verbosity/API default explanation accompanying 74.9% SWE-Bench (page 37).
- GPT-5 red-teaming: nineteen biology PhDs, ten days, approximately 380 hours and 46 reports; three judged practically useful, which the document says the generation monitor would block (pages 51–52). The article's approximately 127 hours is a derived average, not a separate measured campaign result.
- GPT-5 third-party campaigns: FAR.AI's 80 hours, Gray Swan's 277 reports over 28,367 attempts, and its review of 60 examples (pages 52–53). The overall 5,000-plus hours and 400-plus testers are in section 4.
- GPT-5 monitor table: recall 0.838, precision 0.647, reliability above 99.9% (page 50). These do not establish a fixed probability of catching every future attack.
- Opus 5 external campaigns: roughly 100 hours for Trajectory Labs, around 16 hours for 10a Labs, and 150 attempts per task for Grayswan (page 51). The card also reports an automated attacker used by 10a Labs. The internal evaluation has a 400-call limit (page 50).

This review checks the central numerical claims and the cited passages. It does not certify every generalization in the essays or independently reproduce the labs' evaluations.

## Claims to revise before using “The Anthropic Red-Team Hour” as an application sample

1. **Independence and convergence.** The article calls the four efforts independent and says they reached the same practical outcome. The source describes different procedures; it does not establish statistical independence. A low internal attack success rate also does not mean zero successes. Suggested replacement: “The external teams reported limited success on the supplied tasks. The internal evaluation also reported a low attack success rate. I'd want to know how much their methods overlap before treating those results as independent confirmations.”
2. **Catastrophic consequence.** “One successful jailbreak is catastrophic” is stronger than the GPT-5 source supports. A jailbreak producing prohibited material is not itself a demonstrated catastrophe. Suggested replacement: “The GPT-5 campaign looked for actionable biological threat information. The practical consequence depends on what the model disclosed and what an attacker could do with it.”
3. **The proposed exchange rate.** Time per attempt would add useful context, but it would not establish equal difficulty or equal coverage across tasks and attacker methods. Suggested replacement: “Reporting time per attempt would help price the effort. Comparing the findings would still require a description of the tasks and what the attackers could see or change.”
4. **What further work is needed.** “This doesn't need more testing” is not established by the missing reporting details. Suggested replacement: “Some of this could be clarified using records from the existing campaigns. Whether additional testing is needed depends on what those records show.”
5. **Comparative confidence intervals.** “More careful than anything in the GPT-5 document” needs specific paired examples. The promised follow-up is not evidence for the comparison. Either supply those examples or narrow the sentence to the particular methods already inspected.
6. **10a Labs' effort.** The article's opening omits its automated attacker. The source gives no separate effort budget for that attacker, so the reported 16 hours should not be treated as a complete accounting of its campaign.

The essay remains in the archive, with sources attached. It is not one of the four homepage selections.

## Smaller issues in other essays

- **The Red Team Hour:** the paragraphs assigning “no deadline” and particular throughput/budget advantages to state actors are illustrative assumptions, not established by the system card. The core denominator argument stands without them. Suggested replacement for the first budget paragraph: “Whether 127 hours is prohibitive depends on the adversary's resources. The card's persistent-probing threat model makes a longer campaign relevant, but these results don't establish what another month of effort would buy.”
- **The Configuration Is the Finding:** changing a setting can change a result; the current “Change any one ... and the number moves” is categorical. Suggested change: “Change one of those variables and the result can move, sometimes enough to cross the threshold the evaluation is meant to inform.” The claim that the document's error bars “are too narrow” should preserve the source's conditional wording: they **can** be too narrow under the described conditions.
- **A System Card is a Ledger:** “with 84% recall inside it every time it appears” risks transferring an aggregate evaluation score to individual counterfactual blocking judgments. The source does not establish that those judgments are inferred only from the aggregate score. Keep the question about validation across deployments, but avoid treating the table as a fixed probability for every cited example.

## About-page basis

The biography uses experience already described in the published essays: journal editorial standards, checking startup marketing against the product, product documentation, and founder ghostwriting. No job titles, degrees, employer names, or new credentials have been added.
