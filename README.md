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

---
# 📖 System / Project Architecture

CRITEO UPLIFT DATA
        │
        ▼
┌─────────────────────────────┐
│     DATA PREPARATION        │
│ Cleaning / Feature Analysis │
│ Train-Test Split            │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│   CAUSAL VALIDATION         │
│ Randomization               │
│ Covariate Balance / SMD     │
│ Propensity Score            │
│ Causal Assumptions          │
└──────────────┬──────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
  OVERALL EFFECT   HETEROGENEOUS EFFECT
       ATE               CATE
        │                 │
 Difference in      ┌─────┴─────┐
 Means / RA /       ▼           ▼
 IPW / DR       T-Learner    X-Learner
                    │           │
                    └─────┬─────┘
                          ▼
                  MODEL EVALUATION
                  Qini Comparison
                          │
                          ▼
                    X-LEARNER
                   Final Model
                          │
                          ▼
                   Customer CATE
                   / Uplift Score
                          │
                          ▼
                    Uplift Ranking
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
           High        Medium      Low/Negative
             │
             ▼
                POLICY EVALUATION
              5% / 10% / 20% / ...
             Gain Capture / Efficiency
                          │
                          ▼
                  BUSINESS DECISION
                     TOP 20%



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

---

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