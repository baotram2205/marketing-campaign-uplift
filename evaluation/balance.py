from __future__ import annotations

import numpy as np
import pandas as pd


def calculate_covariate_balance(
    X: pd.DataFrame,
    treatment: pd.Series,
    threshold: float = 0.10,
) -> pd.DataFrame:
    """
    Calculate covariate balance between treatment and control groups.

    Parameters
    ----------
    X:
        DataFrame containing pre-treatment covariates.

    treatment:
        Binary treatment indicator where:
        - 1 represents the treatment group
        - 0 represents the control group

    threshold:
        Absolute standardized mean difference threshold used to classify
        covariates as balanced. The default value is 0.10.

    Returns
    -------
    pd.DataFrame
        Covariate balance table containing group means, standard deviations,
        pooled standard deviation, SMD, absolute SMD, and balance status.
    """

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")

    if not isinstance(treatment, pd.Series):
        treatment = pd.Series(treatment, index=X.index)

    if len(X) != len(treatment):
        raise ValueError("X and treatment must contain the same number of rows.")

    treatment_values = set(treatment.dropna().unique())

    if not treatment_values.issubset({0, 1}):
        raise ValueError("Treatment must contain only binary values 0 and 1.")

    if treatment.isna().any():
        raise ValueError("Treatment contains missing values.")

    if X.isna().any().any():
        raise ValueError("X contains missing values.")

    # Separate pre-treatment covariates by treatment group
    X_treated = X.loc[treatment == 1]
    X_control = X.loc[treatment == 0]

    if X_treated.empty:
        raise ValueError("The treatment group contains no observations.")

    if X_control.empty:
        raise ValueError("The control group contains no observations.")

    # Calculate group means and standard deviations
    balance_table = pd.DataFrame(
        {
            "Control Mean": X_control.mean(),
            "Treatment Mean": X_treated.mean(),
            "Control SD": X_control.std(),
            "Treatment SD": X_treated.std(),
        }
    )

    # Calculate pooled standard deviation
    balance_table["Pooled SD"] = np.sqrt(
        (
            balance_table["Control SD"] ** 2
            + balance_table["Treatment SD"] ** 2
        )
        / 2
    )

    # Avoid division by zero for constant covariates
    mean_difference = (
        balance_table["Treatment Mean"]
        - balance_table["Control Mean"]
    )

    balance_table["SMD"] = np.where(
        balance_table["Pooled SD"] > 0,
        mean_difference / balance_table["Pooled SD"],
        np.where(mean_difference == 0, 0.0, np.nan),
    )

    balance_table["Absolute SMD"] = balance_table["SMD"].abs()

    # Classify covariate balance
    balance_table["Balance Status"] = np.where(
        balance_table["Absolute SMD"] < threshold,
        "Balanced",
        "Potential Imbalance",
    )

    # Sort from the most imbalanced to the most balanced covariate
    balance_table = balance_table.sort_values(
        by="Absolute SMD",
        ascending=False,
    )

    return balance_table