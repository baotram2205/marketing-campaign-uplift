import matplotlib.pyplot as plt
import pandas as pd




def plot_cate_distribution(
    results: pd.DataFrame,
    cate_col: str = "estimated_cate",
    bins: int = 50,
    figsize: tuple[int, int] = (8, 5),
) -> None:
    """
    Plot the distribution of estimated Conditional Average Treatment Effects (CATE).

    Parameters
    ----------
    results : pandas.DataFrame
        DataFrame containing estimated CATE values.
    cate_col : str, default="estimated_cate"
        Column containing estimated CATE values.
    bins : int, default=50
        Number of histogram bins.
    figsize : tuple[int, int], default=(8, 5)
        Figure size.
    """

    if cate_col not in results.columns:
        raise KeyError(f"Column '{cate_col}' not found in results.")

    plt.figure(figsize=figsize)

    plt.hist(
        results[cate_col],
        bins=bins,
    )

    plt.xlabel("Estimated Conditional Average Treatment Effect (CATE)")
    plt.ylabel("Number of Customers")
    plt.title("Distribution of Estimated CATE")

    plt.tight_layout()
    plt.show()


def plot_train_test_treatment_distribution(
    train_ratio: pd.Series,
    test_ratio: pd.Series,
    figsize: tuple[int, int] = (6, 4),
) -> None:
    """
    Plot the treatment distribution in the training and test sets.

    Parameters
    ----------
    train_ratio : pandas.Series
        Treatment proportions in the training set.
    test_ratio : pandas.Series
        Treatment proportions in the test set.
    figsize : tuple[int, int], default=(6, 4)
        Figure size.
    """

    ratio_df = pd.concat(
        [train_ratio, test_ratio],
        axis=1,
    )

    ratio_df.columns = ["Train", "Test"]

    ratio_df.plot(
        kind="bar",
        figsize=figsize,
    )

    plt.ylabel("Proportion")
    plt.xlabel("Treatment")
    plt.title("Treatment Distribution After Train-Test Split")

    plt.tight_layout()
    plt.show()