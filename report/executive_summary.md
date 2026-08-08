# Executive Summary

## Project Objective

This project evaluates the effectiveness of a marketing campaign using causal inference and uplift modeling on the Criteo Uplift dataset.

The objectives are to:

- estimate the overall causal effect of the campaign on customer conversion;
- identify heterogeneity in customer treatment response;
- compare uplift modeling approaches for customer-level treatment effect estimation;
- rank customers according to their expected incremental response;
- develop a more efficient campaign targeting strategy.

---

## Key Findings

### Exploratory Data Analysis

- The dataset contains approximately 14 million customer observations.
- The treatment group is substantially larger than the control group, creating an imbalanced treatment allocation.
- Customer conversion is a rare event, with low response rates in both treatment and control groups.

### Overall Treatment Effect

The campaign produces a positive average effect on customer conversion.

On the held-out test population:

- Treatment conversion rate: **0.3136%**
- Control conversion rate: **0.1900%**
- Average Treatment Effect (ATE): **+0.1236 percentage points**

This indicates that the campaign increases customer conversion on average.

### Treatment Effect Heterogeneity

The treatment effect is not uniform across customers.

Although **99.68%** of customers have a positive predicted CATE, most customers have relatively small incremental effects, while a smaller group exhibits substantially stronger treatment response.

This heterogeneity provides an opportunity to improve campaign efficiency through customer-level targeting.

### Uplift Model Performance

The T-Learner and X-Learner were evaluated as alternative approaches for estimating and ranking customer-level treatment effects.

The X-Learner demonstrated stronger uplift ranking performance:

| Model | Qini Coefficient |
| --- | ---: |
| T-Learner | 624.21 |
| X-Learner | **1073.98** |

The X-Learner therefore was selected as the final model for customer uplift ranking and campaign targeting.

### Campaign Targeting

Incremental campaign gain is highly concentrated among customers with the highest predicted uplift.

| Population Targeted | Total Gain Captured |
| ---: | ---: |
| Top 5% | 52.0% |
| Top 10% | 70.9% |
| **Top 20%** | **83.3%** |
| Top 30% | 86.8% |
| Top 50% | 92.6% |
| 100% | 100.0% |

Targeting approximately the **top 20% of customers** captures **83.3% of the total cumulative incremental gain**, while reaching only one-fifth of the population.

---

## Business Recommendations

The campaign should not be applied uniformly across the entire customer population.

Customers should instead be ranked using their **X-Learner predicted uplift scores**, with marketing resources prioritized toward customers with the highest expected incremental response.

Under the current evaluation, the **top 20% of customers represents a practical targeting range**, capturing most of the available incremental gain while maintaining substantially higher targeting efficiency than broad population targeting.

The final operational cutoff should additionally consider campaign cost, conversion value, available budget, and other business constraints.

---

## Limitations

- Customer conversion is a rare outcome, which can introduce greater variability when evaluating uplift within smaller customer segments.
- Customer-level treatment effects are model estimates and cannot be directly observed for individual customers.
- The analysis evaluates targeting performance based on incremental conversion gain but does not incorporate campaign cost or monetary conversion value.
- The recommended 20% targeting threshold should therefore be interpreted as a practical model-based targeting range rather than a profit-maximizing optimum.

---

## Future Work

- Compare the X-Learner with additional heterogeneous treatment effect models such as Causal Forest.
- Incorporate campaign cost and conversion value to optimize targeting based on expected incremental profit.
- Evaluate model stability across different samples and campaign periods.
- Develop business-specific targeting thresholds based on budget and operational capacity.