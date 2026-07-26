import os
from pathlib import Path
from dotenv import load_dotenv


def load_configuration():
    """
    Load project configuration from .env file.
    """

    project_root = Path(__file__).resolve().parent.parent
    env_path = project_root / ".env"

    load_dotenv(env_path)

    return {
        "dataset_path": os.getenv("DATASET_PATH"),
        "target": os.getenv("TARGET_COLUMN"),
        "treatment": os.getenv("TREATMENT_COLUMN"),
    }