from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm


@dataclass
class ATEResult:
    """
    Store the estimated Average Treatment Effect (ATE).
    """

    ate: float


@dataclass
class ATEResult:
    treated_mean: float | None = None
    control_mean: float | None = None
    ate: float = 0.0

def difference_in_means(
    outcome: pd.Series,
    treatment: pd.Series,
) -> ATEResult:

    treated_mean = outcome[treatment == 1].mean()
    control_mean = outcome[treatment == 0].mean()

    ate = treated_mean - control_mean

    return ATEResult(
        treated_mean=float(treated_mean),
        control_mean=float(control_mean),
        ate=float(ate),
    )


from sklearn.linear_model import LinearRegression


def regression_adjustment(
    X: pd.DataFrame,
    outcome: pd.Series,
    treatment: pd.Series,
) -> ATEResult:
    """
    Estimate ATE using regression adjustment through
    potential-outcome prediction.
    """

    X_reg = X.copy()
    X_reg["treatment"] = treatment.to_numpy()

    model = LinearRegression()
    model.fit(X_reg, outcome)

    X_treated = X_reg.copy()
    X_treated["treatment"] = 1

    X_control = X_reg.copy()
    X_control["treatment"] = 0

    y1_pred = model.predict(X_treated)
    y0_pred = model.predict(X_control)

    ate = np.mean(y1_pred - y0_pred)

    return ATEResult(
        ate=float(ate),
    )


def inverse_probability_weighting(
    outcome: pd.Series,
    treatment: pd.Series,
    propensity_score: pd.Series | np.ndarray,
) -> ATEResult:
    """
    Estimate the Average Treatment Effect using
    Inverse Probability Weighting.
    """

    outcome_array = np.asarray(outcome)
    treatment_array = np.asarray(treatment)

    propensity = np.clip(
        np.asarray(propensity_score),
        1e-6,
        1 - 1e-6,
    )

    ipw_scores = (
        treatment_array * outcome_array / propensity
        - (1 - treatment_array)
        * outcome_array
        / (1 - propensity)
    )

    ate = np.mean(ipw_scores)

    return ATEResult(
        ate=float(ate),
    )
    


def doubly_robust(
    X: pd.DataFrame,
    outcome: pd.Series,
    treatment: pd.Series,
    propensity_score: pd.Series,
    treatment_model,
    control_model,
) -> ATEResult:
    """
    Estimate the Average Treatment Effect using the
    Doubly Robust estimator.

    The function uses:
    - a propensity score model,
    - an outcome model for treated customers,
    - an outcome model for control customers.
    """

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")

    if not (
        len(X)
        == len(outcome)
        == len(treatment)
        == len(propensity_score)
    ):
        raise ValueError(
            "X, outcome, treatment, and propensity_score must "
            "contain the same number of rows."
        )

    propensity = np.clip(
        np.asarray(propensity_score),
        1e-6,
        1 - 1e-6,
    )

    outcome_array = np.asarray(outcome)
    treatment_array = np.asarray(treatment)

    # Predicted potential outcomes
    mu1 = treatment_model.predict_proba(X)[:, 1]
    mu0 = control_model.predict_proba(X)[:, 1]

    # Doubly Robust pseudo-outcome
    dr_scores = (
        mu1
        - mu0
        + treatment_array
        * (outcome_array - mu1)
        / propensity
        - (1 - treatment_array)
        * (outcome_array - mu0)
        / (1 - propensity)
    )

    ate = dr_scores.mean()

    return ATEResult(
        ate=float(ate),
    )