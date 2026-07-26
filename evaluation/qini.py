from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklift.metrics import qini_auc_score, qini_curve


@dataclass
class QiniResult:
    """
    Store Qini curve coordinates and the normalized Qini AUC.
    """

    targeted_customers: np.ndarray
    incremental_conversions: np.ndarray
    random_baseline: np.ndarray
    qini_auc: float


def calculate_qini(
    y_true: pd.Series | np.ndarray,
    treatment: pd.Series | np.ndarray,
    uplift_score: pd.Series | np.ndarray,
) -> QiniResult:
    """
    Calculate the Qini curve and normalized Qini AUC.

    Parameters
    ----------
    y_true:
        Observed binary conversion outcome.

    treatment:
        Binary treatment indicator:
        1 = treatment group
        0 = control group.

    uplift_score:
        Estimated customer uplift scores used to rank customers.

    Returns
    -------
    QiniResult
        Qini curve coordinates, random-targeting baseline,
        and normalized Qini AUC.
    """

    y_true_array = np.asarray(y_true)
    treatment_array = np.asarray(treatment)
    uplift_array = np.asarray(uplift_score)

    if not (
        len(y_true_array)
        == len(treatment_array)
        == len(uplift_array)
    ):
        raise ValueError(
            "y_true, treatment, and uplift_score must have "
            "the same number of observations."
        )

    if len(y_true_array) == 0:
        raise ValueError("Input arrays cannot be empty.")

    if np.isnan(y_true_array).any():
        raise ValueError("y_true contains missing values.")

    if np.isnan(treatment_array).any():
        raise ValueError("treatment contains missing values.")

    if np.isnan(uplift_array).any():
        raise ValueError("uplift_score contains missing values.")

    if not set(np.unique(y_true_array)).issubset({0, 1}):
        raise ValueError("y_true must contain only binary values 0 and 1.")

    if not set(np.unique(treatment_array)).issubset({0, 1}):
        raise ValueError(
            "treatment must contain only binary values 0 and 1."
        )

    targeted_customers, incremental_conversions = qini_curve(
        y_true=y_true_array,
        uplift=uplift_array,
        treatment=treatment_array,
    )

    normalized_qini_auc = qini_auc_score(
        y_true=y_true_array,
        uplift=uplift_array,
        treatment=treatment_array,
    )

    random_baseline = (
        targeted_customers
        / targeted_customers[-1]
        * incremental_conversions[-1]
    )

    return QiniResult(
        targeted_customers=targeted_customers,
        incremental_conversions=incremental_conversions,
        random_baseline=random_baseline,
        qini_auc=float(normalized_qini_auc),
    )


def plot_qini(
    qini_result: QiniResult,
    model_label: str = "T-Learner",
    figsize: tuple[int, int] = (8, 5),
) -> None:
    """
    Plot the model Qini curve against random targeting.

    Parameters
    ----------
    qini_result:
        Output returned by calculate_qini().

    model_label:
        Label displayed for the uplift model.

    figsize:
        Matplotlib figure size.
    """

    plt.figure(figsize=figsize)

    plt.plot(
        qini_result.targeted_customers,
        qini_result.incremental_conversions,
        label=model_label,
    )

    plt.plot(
        qini_result.targeted_customers,
        qini_result.random_baseline,
        linestyle="--",
        label="Random Targeting",
    )

    plt.xlabel("Number of Targeted Customers")
    plt.ylabel("Incremental Conversions")
    plt.title("Qini Curve")

    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()