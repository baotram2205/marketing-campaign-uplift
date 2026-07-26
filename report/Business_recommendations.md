# Business Recommendations

## Business Question 1

### Does the marketing campaign increase customer conversion?

Yes.

All causal estimators consistently produced a positive Average Treatment Effect (ATE), indicating that the campaign generates incremental customer conversions.

---

## Business Question 2

### Should every customer receive the campaign?

No.

The estimated average treatment effect is positive but relatively small across the overall population. A blanket campaign would therefore be inefficient.

---

## Business Question 3

### Which customers should be targeted?

Customers with the highest predicted uplift scores.

The T-Learner successfully ranked customers according to their expected incremental treatment effect, as demonstrated by the positive Qini curve and a Normalized Qini AUC of **0.104555**.

---

## Business Question 4

### Recommended campaign strategy

Rank customers by predicted uplift score and target the top **20%** of customers.

This strategy is expected to generate more incremental conversions than random targeting while improving marketing efficiency and reducing unnecessary campaign costs.