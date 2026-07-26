import sys
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Make project root importable immediately when setup is imported
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def configure_notebook():
    """
    Configure the notebook environment.
    """

    warnings.filterwarnings("ignore")

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", 100)
    pd.set_option("display.width", 120)
    pd.set_option("display.float_format", "{:.2f}".format)

    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)