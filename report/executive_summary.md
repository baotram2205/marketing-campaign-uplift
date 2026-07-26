# Executive Summary

## Project Objective

This project evaluates the effectiveness of a marketing campaign using causal inference and uplift modeling on the Criteo Uplift dataset. The objectives are to estimate the Average Treatment Effect (ATE), identify customers with the highest incremental treatment effect, and provide actionable campaign recommendations.

---

## Key Findings

### Exploratory Data Analysis

- The dataset contains approximately 14 million customer observations.
- Treatment and control groups are well balanced.
- Customer conversion is a rare event, making uplift modeling appropriate.

### Causal Inference

Four causal estimators were evaluated.

| Estimator | Result |
|-----------|--------|
| Difference in Means | Positive ATE |
| Regression Adjustment | Positive ATE |
| Inverse Propensity Weighting | Positive ATE |
| Doubly Robust | Positive ATE |

All estimators consistently indicate that the campaign has a positive causal effect on customer conversion.

### Uplift Modeling

A T-Learner with LightGBM was trained to estimate customer-level treatment effects.

The model achieved:

- Normalized Qini AUC = **0.104555**

The Qini curve demonstrates that the model successfully ranks customers according to their expected incremental treatment effects and consistently outperforms random targeting.

---

## Business Recommendations

Rather than sending the campaign to every customer, marketing resources should be focused on customers with the highest predicted uplift scores.

The proposed targeting strategy recommends contacting the **top 20% of ranked customers**, where the greatest incremental conversion gains are expected.

---

## Limitations

- Only observed confounding variables were adjusted.
- Results depend on the quality of the available customer features.
- External business constraints such as campaign budget and customer lifetime value were not incorporated.

---

## Future Work

- Compare additional uplift models such as X-Learner and Causal Forest.
- Optimize the targeting threshold using expected business ROI.
- Incorporate treatment cost and customer lifetime value into campaign optimization.