# 📈 Marketing Campaign Optimization using Causal Inference & Uplift Modeling

> An end-to-end causal analytics project for evaluating marketing campaign effectiveness and improving customer targeting using **Causal Inference** and **Uplift Modeling**.

---

# 📖 Project Overview

Traditional predictive models estimate **who is likely to convert**, but they do not determine whether a marketing campaign actually causes that conversion.

This project uses causal inference and uplift modeling to answer a different set of questions:

- 🎯 Does the marketing campaign increase customer conversion?
- 📊 Does treatment response differ across customers?
- 👥 Which customers are most likely to benefit from treatment?
- 📈 Can uplift-based targeting outperform broad or random targeting?
- 💰 How can marketing resources be allocated more efficiently?

The final framework estimates both the overall causal effect of the campaign and customer-level heterogeneous treatment effects to support data-driven campaign targeting.

# 🎯 Project Objectives

The project aims to:

- Estimate the **Average Treatment Effect (ATE)** of the campaign.
- Evaluate treatment assignment and causal assumptions.
- Estimate **Conditional Average Treatment Effects (CATE)**.
- Compare alternative uplift modeling approaches.
- Rank customers by predicted incremental treatment response.
- Evaluate targeting performance using **Decile Analysis and Qini metrics**.
- Develop a practical campaign targeting strategy.

---

# 📂 Dataset

**Criteo Uplift Prediction Dataset**

The dataset contains approximately 14 million customer observations from an online advertising experiment.

Key variables include:

- Customer features
- Treatment assignment
- Conversion outcome

The dataset is characterized by:

- Highly imbalanced treatment and control sample sizes.
- Rare customer conversion events.
- Large-scale customer-level behavioral data.

## 🧠 Methodology

Raw Dataset
      │
      ▼
Exploratory Data Analysis (EDA)
      │
      ▼
Randomization Assessment
 ├── Covariate Balance
 ├── Standardized Mean Difference (SMD)
 ├── Propensity Score Overlap
 └── Logistic Regression Check
      │
      ▼
Causal Identification
 ├── DAG Construction
 ├── Consistency
 ├── Ignorability
 └── Positivity
      │
      ▼
Average Treatment Effect (ATE)
 ├── Difference in Means
 ├── Regression Adjustment
 ├── Inverse Probability Weighting
 └── Doubly Robust
      │
      ▼
Conditional Average Treatment Effect (CATE)
 ├── T-Learner
 └── X-Learner
      │
      ▼
Model Evaluation
 ├── CATE Distribution
 ├── Decile Analysis
 ├── Qini Curve
 └── T-Learner vs X-Learner Comparison
      │
      ▼
Customer Ranking & Campaign Targeting

The analysis begins with exploratory data analysis and validation of the randomized treatment assignment. Covariate balance, standardized mean differences, propensity score overlap, and logistic regression diagnostics are used to assess whether the treatment and control groups satisfy the assumptions required for causal inference.

The overall campaign effectiveness is then estimated using four complementary ATE estimators: Difference in Means, Regression Adjustment, Inverse Probability Weighting (IPW), and Doubly Robust. Consistent estimates across these methods provide evidence that the estimated treatment effect is robust.

To identify which customers benefit most from the campaign, heterogeneous treatment effects are estimated using both T-Learner and X-Learner. Their performance is compared using uplift-specific evaluation metrics, including decile analysis and the Qini curve. The best-performing model is then used to rank customers by predicted uplift and recommend a data-driven targeting strategy.

# 🏗️ Project Structure

```text
project/
│
├── data/
│   └── criteo-uplift-v2.1.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Causal_Inference_Analysis.ipynb
│
├── causal/
├── uplift/
├── evaluation/
├── visualization/
├── features/
├── report/
│
├── environment.yml
└── README.md