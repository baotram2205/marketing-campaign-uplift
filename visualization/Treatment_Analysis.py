# visualization/propensity.py

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def plot_propensity_score_distribution(
    df,
    treatment_col,
    propensity_col,
    bins=40,
    figsize=(8, 6)
):
    """
    Plot the estimated propensity score distributions for the
    treatment and control groups.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing treatment assignment and propensity scores.
    treatment_col : str
        Name of the treatment indicator column (1=Treatment, 0=Control).
    propensity_col : str
        Name of the propensity score column.
    bins : int, default=40
        Number of histogram bins.
    figsize : tuple, default=(8, 6)
        Figure size.
    """

    plt.figure(figsize=figsize)

    plt.hist(
        df.loc[df[treatment_col] == 1, propensity_col],
        bins=bins,
        alpha=0.6,
        density=True,
        label="Treatment"
    )

    plt.hist(
        df.loc[df[treatment_col] == 0, propensity_col],
        bins=bins,
        alpha=0.6,
        density=True,
        label="Control"
    )

    plt.xlabel("Propensity Score")
    plt.ylabel("Density")
    plt.title("Distribution of Estimated Propensity Scores")

    plt.legend()
    plt.tight_layout()
    plt.show()



def plot_propensity_score_boxplot(
    df,
    treatment_col,
    propensity_col,
    figsize=(8, 6),
):
    """
    Plot propensity score distributions by treatment group using a boxplot.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing treatment assignments and propensity scores.
    treatment_col : str
        Name of the treatment indicator column (0=Control, 1=Treatment).
    propensity_col : str
        Name of the propensity score column.
    figsize : tuple, default=(8, 6)
        Figure size.
    """

    plt.figure(figsize=figsize)

    df.boxplot(
        column=propensity_col,
        by=treatment_col,
        grid=False,
    )

    plt.suptitle("")
    plt.title("Propensity Scores by Treatment Group")

    plt.xlabel("Treatment")
    plt.ylabel("Propensity Score")

    plt.tight_layout()
    plt.show()


def plot_treatment_model_coefficients(
    coef_table: pd.DataFrame,
    feature_col: str = "Feature",
    coefficient_col: str = "Coefficient",
    figsize: tuple[int, int] = (8, 6),
) -> None:
    """
    Plot logistic regression coefficients for treatment assignment.

    Parameters
    ----------
    coef_table : pandas.DataFrame
        Table containing feature names and logistic regression coefficients.
    feature_col : str, default="Feature"
        Column containing feature names.
    coefficient_col : str, default="Coefficient"
        Column containing coefficient values.
    figsize : tuple[int, int], default=(8, 6)
        Figure size.
    """
    required_columns = {feature_col, coefficient_col}
    missing_columns = required_columns.difference(coef_table.columns)

    if missing_columns:
        raise KeyError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    coef_plot = coef_table.sort_values(
        by=coefficient_col,
        ascending=True,
    )

    plt.figure(figsize=figsize)

    plt.barh(
        coef_plot[feature_col],
        coef_plot[coefficient_col],
    )

    plt.axvline(
        x=0,
        color="black",
        linestyle="--",
        linewidth=1,
    )

    plt.xlabel("Logistic Regression Coefficient")
    plt.ylabel("Pre-treatment Covariates")
    plt.title(
        "Logistic Regression Coefficients for Treatment Assignment"
    )

    plt.tight_layout()
    plt.show()




def plot_covariate_balance(
    balance_table: pd.DataFrame,
    smd_col: str = "Absolute SMD",
    threshold: float = 0.10,
    figsize: tuple[int, int] = (8, 6),
) -> None:
    """
    Plot the absolute standardized mean differences (SMD) of
    pre-treatment covariates.

    Parameters
    ----------
    balance_table : pandas.DataFrame
        Covariate balance table containing Absolute SMD values.
    smd_col : str, default="Absolute SMD"
        Column containing the absolute SMD values.
    threshold : float, default=0.10
        Covariate balance threshold.
    figsize : tuple[int, int], default=(8, 6)
        Figure size.
    """

    if smd_col not in balance_table.columns:
        raise KeyError(f"Column '{smd_col}' not found in balance_table.")

    smd_plot = balance_table.sort_values(
        by=smd_col,
        ascending=True,
    )

    plt.figure(figsize=figsize)

    plt.barh(
        smd_plot.index,
        smd_plot[smd_col],
    )

    plt.axvline(
        x=threshold,
        linestyle="--",
        label=f"Balance threshold: |SMD| = {threshold:.2f}",
    )

    plt.xlabel("Absolute Standardized Mean Difference")
    plt.ylabel("Pre-treatment Covariate")
    plt.title("Covariate Balance Between Treatment and Control Groups")

    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_treatment_distribution(
    df: pd.DataFrame,
    treatment_col: str,
    figsize: tuple[int, int] = (6, 4),
) -> None:
    """
    Plot the treatment assignment distribution.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset containing the treatment assignment.
    treatment_col : str
        Name of the treatment indicator column.
    figsize : tuple[int, int], default=(6, 4)
        Figure size.
    """

    if treatment_col not in df.columns:
        raise KeyError(f"Column '{treatment_col}' not found in DataFrame.")

    plt.figure(figsize=figsize)

    sns.countplot(
        data=df,
        x=treatment_col,
    )

    plt.xticks(
        [0, 1],
        ["Control", "Treatment"],
    )

    plt.title("Treatment Assignment Distribution")
    plt.xlabel("Group")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.show()

def plot_standardized_mean_difference(
    balance_table: pd.DataFrame,
    smd_col: str = "Absolute SMD",
    threshold: float = 0.10,
    figsize: tuple[int, int] = (8, 6),
) -> None:
    """
    Plot the absolute standardized mean differences (SMD) of
    pre-treatment covariates.

    Parameters
    ----------
    balance_table : pandas.DataFrame
        Table containing the absolute SMD values.
    smd_col : str, default="Absolute SMD"
        Column containing the absolute SMD values.
    threshold : float, default=0.10
        Covariate balance threshold.
    figsize : tuple[int, int], default=(8, 6)
        Figure size.
    """

    if smd_col not in balance_table.columns:
        raise KeyError(f"Column '{smd_col}' not found in balance_table.")

    plot_data = balance_table.sort_values(
        by=smd_col,
        ascending=True,
    )

    plt.figure(figsize=figsize)

    plt.barh(
        plot_data.index,
        plot_data[smd_col],
    )

    plt.axvline(
        x=threshold,
        color="red",
        linestyle="--",
        label=f"Balance Threshold (|SMD| = {threshold:.2f})",
    )

    plt.xlabel("Absolute Standardized Mean Difference")
    plt.ylabel("Pre-treatment Covariates")
    plt.title("Standardized Mean Difference of Pre-treatment Covariates")

    plt.legend()
    plt.tight_layout()
    plt.show()