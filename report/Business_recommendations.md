# Business Recommendations

## Business Question 1

### Does the marketing campaign increase customer conversion?

**Yes.**

The treatment group achieved a conversion rate of **0.3136%**, compared with **0.1900%** for the control group.

The estimated Average Treatment Effect (ATE) is **0.001236**, equivalent to an increase of **0.1236 percentage points**.

This indicates that the marketing campaign has a positive average effect on customer conversion.


## Business Question 2

### Should every customer receive the campaign?

**No.**

Although the campaign has a positive average treatment effect, the X-Learner shows that the magnitude of treatment response varies substantially across customers.

Most customers have relatively small predicted uplift, while a smaller group accounts for a much larger incremental response.

Therefore, applying the campaign uniformly across all customers is unlikely to be the most efficient targeting strategy.

## Business Question 3

### Which customers should be targeted?

Customers with the **highest predicted uplift scores** should be prioritized.

The X-Learner ranks customers according to their expected incremental response to treatment.

The highest-ranked decile achieved an observed uplift of **0.008620**, substantially higher than most lower-ranked groups, providing evidence that the model successfully concentrates stronger treatment responders toward the top of the ranking.
---

## Business Question 4

### What campaign targeting strategy is recommended?

Customers should be ranked by their X-Learner predicted uplift score and the campaign should prioritize approximately the **top 20%** of customers.

The top 20% captures approximately **83.3% of the total cumulative incremental gain**, while targeting only one-fifth of the population.

Beyond this range, additional gain increases more slowly while gain per targeted customer continues to decline.

Therefore, the top 20% represents a practical targeting range under the current model.