from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


@dataclass
class PropensityModelResult:
    model: LogisticRegression
    propensity_scores: np.ndarray
    coefficient_table: pd.DataFrame


def fit_propensity_model(
    X: pd.DataFrame,
    treatment: pd.Series,
    max_iter: int = 1000,
    random_state: int = 42,
) -> PropensityModelResult:
    """
    Fit a logistic regression model for treatment assignment.

    Parameters
    ----------
    X:
        DataFrame containing pre-treatment covariates.

    treatment:
        Binary treatment indicator where 1 represents treatment
        and 0 represents control.

    max_iter:
        Maximum number of iterations for logistic regression.

    random_state:
        Random seed used by the logistic regression model.

    Returns
    -------
    PropensityModelResult
        Fitted model, propensity scores, and coefficient table.
    """

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")

    if not isinstance(treatment, pd.Series):
        treatment = pd.Series(treatment, index=X.index)

    if len(X) != len(treatment):
        raise ValueError("X and treatment must have the same number of rows.")

    if X.isna().any().any():
        raise ValueError("X contains missing values.")

    if treatment.isna().any():
        raise ValueError("Treatment contains missing values.")

    treatment_values = set(treatment.unique())

    if not treatment_values.issubset({0, 1}):
        raise ValueError("Treatment must contain only binary values 0 and 1.")

    model = LogisticRegression(
        max_iter=max_iter,
        random_state=random_state,
    )

    model.fit(X, treatment)

    propensity_scores = model.predict_proba(X)[:, 1]

    coefficient_table = pd.DataFrame(
        {
            "Feature": X.columns,
            "Coefficient": model.coef_[0],
        }
    )

    coefficient_table["Absolute Coefficient"] = (
        coefficient_table["Coefficient"].abs()
    )

    coefficient_table = coefficient_table.sort_values(
        by="Absolute Coefficient",
        ascending=False,
    ).reset_index(drop=True)

    return PropensityModelResult(
        model=model,
        propensity_scores=propensity_scores,
        coefficient_table=coefficient_table,
    )