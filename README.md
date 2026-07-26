# 📈 Marketing Campaign Optimization using Causal Inference & Uplift Modeling

> An end-to-end causal analytics project for optimizing marketing campaigns using **Causal Inference** and **Uplift Modeling**.

---

# 📖 Project Overview

Traditional marketing campaigns often send promotions to every customer, resulting in unnecessary marketing costs and reduced campaign efficiency.

This project develops a **decision support system** that estimates the causal effect of marketing campaigns and recommends which customers should receive promotional offers.

Instead of predicting **who will convert**, the project predicts:

- 🎯 Who benefits from the campaign
- 🚫 Who should not receive the campaign
- 📊 Expected campaign effectiveness
- 💰 The optimal targeting strategy

---

# 🎯 Project Objectives

The project aims to estimate:

- ✅ Average Treatment Effect (ATE)
- ✅ Conditional Average Treatment Effect (CATE)
- ✅ Customer Uplift Score
- ✅ Customer Ranking
- ✅ Campaign Recommendation
- ✅ Expected Business Impact

---

# 📂 Dataset

**Dataset**

- Criteo Uplift Prediction Dataset

The dataset contains customer-level observations collected during an online advertising campaign, including:

- Customer features
- Treatment assignment
- Conversion outcome

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
```

---

# 📒 Notebook Overview

## 📙 01_EDA.ipynb

Exploratory Data Analysis

Main contents:

- Dataset overview
- Missing value analysis
- Duplicate analysis
- Outlier assessment
- Treatment distribution
- Conversion rate analysis
- Feature distributions
- Correlation analysis
- Dataset bias discussion
- Summary of exploratory findings

---

## 📘 02_Causal_Inference_Analysis.ipynb

Complete causal analytics pipeline.

### Part A – Causal Inference

- Treatment Assignment Analysis
- Covariate Balance
- Standardized Mean Difference (SMD)
- Logistic Regression Predicting Treatment
- Propensity Score Distribution
- Directed Acyclic Graph (DAG)
- Identification Strategy
- Causal Assumptions

---

### Part B – Uplift Modeling

**Selected Approach**

- Meta Learner

**Selected Model**

- T-Learner

**Base Learner**

- LightGBM

Outputs:

- Estimated CATE
- Customer Uplift Score
- Customer Ranking
- Campaign Recommendation

---

### Part C – Model Evaluation

Causal Estimators

- Difference in Means
- Regression Adjustment
- Inverse Propensity Weighting (IPW)
- Doubly Robust Estimation

Uplift Evaluation

- Qini Curve

Policy Evaluation

- Campaign Policies
- Business Interpretation
- Marketing Recommendation

---

# 📊 Key Results

The analysis shows that:

- ✅ The marketing campaign has a **positive Average Treatment Effect (ATE)**.
- ✅ Customers exhibit heterogeneous treatment effects, supporting the use of uplift modeling.
- ✅ The T-Learner successfully estimates customer-level treatment effects.
- ✅ Ranking customers by predicted uplift improves marketing efficiency.
- ✅ The **Top 20% targeting policy** provides the highest expected business value among the evaluated strategies.

---

# 🛠️ Technologies

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 🌲 LightGBM
- 📈 Matplotlib
- 📊 scikit-uplift

---

# 🚀 Getting Started

## 1️⃣ Create the environment

```bash
conda env create -f environment.yml
```

## 2️⃣ Activate the environment

```bash
conda activate uplift312
```

## 3️⃣ Launch Jupyter

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

---

# ▶️ Run the Project

Execute the notebooks in the following order:

1. 📙 01_EDA.ipynb
2. 📘 02_Causal_Inference_Analysis.ipynb

---

# 🎓 Learning Outcomes

This project demonstrates practical applications of:

- Exploratory Data Analysis (EDA)
- Causal Inference
- Treatment Effect Estimation
- Propensity Score Analysis
- Uplift Modeling
- Offline Policy Evaluation
- Data-driven Marketing Decision Support

---

# 👩‍💻 Author

**Tram Le**

Course Project

Marketing Campaign Optimization using Causal Inference & Uplift Modeling