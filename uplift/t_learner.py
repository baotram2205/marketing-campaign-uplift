from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split


@dataclass
class TrainTestData:
    """
    Container for train-test split data.
    """

    X_train: pd.DataFrame
    X_test: pd.DataFrame
    T_train: pd.Series
    T_test: pd.Series
    Y_train: pd.Series
    Y_test: pd.Series


@dataclass
class TLearnerResult:
    """
    Container for trained T-Learner models and training information.
    """

    treatment_model: Any
    control_model: Any
    treatment_training_time: float
    control_training_time: float
    treatment_sample_size: int
    control_sample_size: int


@dataclass
class CATEResult:
    """
    Container for estimated potential outcomes and CATE.
    """

    p_treatment: np.ndarray
    p_control: np.ndarray
    estimated_cate: np.ndarray
    results: pd.DataFrame


def split_uplift_data(
    X: pd.DataFrame,
    treatment: pd.Series,
    outcome: pd.Series,
    test_size: float = 0.20,
    random_state: int = 42,
) -> TrainTestData:
    """
    Split uplift data into training and testing sets.

    The split is stratified by treatment assignment so that the treatment
    proportions are preserved across the training and testing datasets.

    Parameters
    ----------
    X:
        DataFrame containing pre-treatment customer features.

    treatment:
        Binary treatment indicator:
        1 = treatment group
        0 = control group.

    outcome:
        Binary outcome indicator.

    test_size:
        Proportion of observations assigned to the testing set.

    random_state:
        Random seed for reproducibility.

    Returns
    -------
    TrainTestData
        Training and testing features, treatment indicators, and outcomes.
    """

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")

    if not isinstance(treatment, pd.Series):
        treatment = pd.Series(treatment, index=X.index)

    if not isinstance(outcome, pd.Series):
        outcome = pd.Series(outcome, index=X.index)

    if not (len(X) == len(treatment) == len(outcome)):
        raise ValueError(
            "X, treatment, and outcome must contain the same number of rows."
        )

    if X.isna().any().any():
        raise ValueError("X contains missing values.")

    if treatment.isna().any():
        raise ValueError("Treatment contains missing values.")

    if outcome.isna().any():
        raise ValueError("Outcome contains missing values.")

    treatment_values = set(treatment.unique())

    if not treatment_values.issubset({0, 1}):
        raise ValueError(
            "Treatment must contain only binary values 0 and 1."
        )

    if treatment.nunique() != 2:
        raise ValueError(
            "Treatment must contain both treatment and control observations."
        )

    (
        X_train,
        X_test,
        T_train,
        T_test,
        Y_train,
        Y_test,
    ) = train_test_split(
        X,
        treatment,
        outcome,
        test_size=test_size,
        random_state=random_state,
        stratify=treatment,
    )

    return TrainTestData(
        X_train=X_train,
        X_test=X_test,
        T_train=T_train,
        T_test=T_test,
        Y_train=Y_train,
        Y_test=Y_test,
    )


def train_t_learner(
    X_train: pd.DataFrame,
    treatment_train: pd.Series,
    outcome_train: pd.Series,
    treatment_model: Any | None = None,
    control_model: Any | None = None,
    random_state: int = 42,
) -> TLearnerResult:
    """
    Train a T-Learner using separate treatment and control outcome models.

    Parameters
    ----------
    X_train:
        Training features.

    treatment_train:
        Binary treatment indicator for the training observations.

    outcome_train:
        Binary conversion outcome for the training observations.

    treatment_model:
        Optional model for the treatment group. If omitted, an
        LGBMClassifier is created.

    control_model:
        Optional model for the control group. If omitted, an
        LGBMClassifier is created.

    random_state:
        Random seed used when default LightGBM models are created.

    Returns
    -------
    TLearnerResult
        Trained treatment and control models together with training
        durations and sample sizes.
    """

    if not isinstance(X_train, pd.DataFrame):
        raise TypeError("X_train must be a pandas DataFrame.")

    if not isinstance(treatment_train, pd.Series):
        treatment_train = pd.Series(
            treatment_train,
            index=X_train.index,
        )

    if not isinstance(outcome_train, pd.Series):
        outcome_train = pd.Series(
            outcome_train,
            index=X_train.index,
        )

    if not (
        len(X_train)
        == len(treatment_train)
        == len(outcome_train)
    ):
        raise ValueError(
            "X_train, treatment_train, and outcome_train must have "
            "the same number of rows."
        )

    treated_mask = treatment_train == 1
    control_mask = treatment_train == 0

    X_train_treated = X_train.loc[treated_mask]
    Y_train_treated = outcome_train.loc[treated_mask]

    X_train_control = X_train.loc[control_mask]
    Y_train_control = outcome_train.loc[control_mask]

    if X_train_treated.empty:
        raise ValueError(
            "The training data contains no treated observations."
        )

    if X_train_control.empty:
        raise ValueError(
            "The training data contains no control observations."
        )

    if treatment_model is None:
        treatment_model = LGBMClassifier(
            random_state=random_state,
            verbosity=-1,
        )

    if control_model is None:
        control_model = LGBMClassifier(
            random_state=random_state,
            verbosity=-1,
        )

    start_time = time.time()

    treatment_model.fit(
        X_train_treated,
        Y_train_treated,
    )

    treatment_training_time = time.time() - start_time

    start_time = time.time()

    control_model.fit(
        X_train_control,
        Y_train_control,
    )

    control_training_time = time.time() - start_time

    return TLearnerResult(
        treatment_model=treatment_model,
        control_model=control_model,
        treatment_training_time=treatment_training_time,
        control_training_time=control_training_time,
        treatment_sample_size=len(X_train_treated),
        control_sample_size=len(X_train_control),
    )


def estimate_cate(
    treatment_model: Any,
    control_model: Any,
    X: pd.DataFrame,
    treatment: pd.Series | None = None,
    outcome: pd.Series | None = None,
) -> CATEResult:
    """
    Estimate potential outcome probabilities and CATE using a T-Learner.

    Parameters
    ----------
    treatment_model:
        Fitted model trained on treated observations.

    control_model:
        Fitted model trained on control observations.

    X:
        Features for the customers whose treatment effects are estimated.

    treatment:
        Optional observed treatment indicator to include in the returned
        results table.

    outcome:
        Optional observed outcome to include in the returned results table.

    Returns
    -------
    CATEResult
        Predicted treatment probability, predicted control probability,
        estimated CATE, and a customer-level results table.
    """

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X must be a pandas DataFrame.")

    p_treatment = treatment_model.predict_proba(X)[:, 1]
    p_control = control_model.predict_proba(X)[:, 1]

    estimated_cate = p_treatment - p_control

    results = X.copy()

    if treatment is not None:
        if len(treatment) != len(X):
            raise ValueError(
                "Treatment and X must contain the same number of rows."
            )

        results["treatment"] = np.asarray(treatment)

    if outcome is not None:
        if len(outcome) != len(X):
            raise ValueError(
                "Outcome and X must contain the same number of rows."
            )

        results["actual_conversion"] = np.asarray(outcome)

    results["p_treatment"] = p_treatment
    results["p_control"] = p_control
    results["estimated_cate"] = estimated_cate
    # Alias for evaluation
    results["uplift_score"] = estimated_cate

    return CATEResult(
        p_treatment=p_treatment,
        p_control=p_control,
        estimated_cate=estimated_cate,
        results=results,
    )

def estimate_t_cate(
    treatment_model,
    control_model,
    X,
):
    """
    Estimate Conditional Average Treatment Effects (CATE)
    using a fitted T-Learner.

    Parameters
    ----------
    treatment_model : fitted classifier
        Outcome model trained on the treatment group.

    control_model : fitted classifier
        Outcome model trained on the control group.

    X : array-like
        Feature matrix used for CATE estimation.

    Returns
    -------
    estimated_cate : np.ndarray
        Estimated individual treatment effects.

    mu1 : np.ndarray
        Predicted outcome probabilities under treatment.

    mu0 : np.ndarray
        Predicted outcome probabilities under control.
    """

    # Potential outcome under treatment
    mu1 = treatment_model.predict_proba(X)[:, 1]

    # Potential outcome under control
    mu0 = control_model.predict_proba(X)[:, 1]

    # T-Learner CATE
    estimated_cate = mu1 - mu0

    return estimated_cate, mu1, mu0