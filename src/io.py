import pandas as pd
from pathlib import Path

def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(path)
