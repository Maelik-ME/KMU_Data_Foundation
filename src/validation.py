import pandas as pd


def check_missing_values(df: pd.DataFrame) -> dict:
    """
    Return count of missing values per column.
    """
    return df.isna().sum().to_dict()


def check_duplicates(df: pd.DataFrame, key: str) -> int:
    """
    Check for duplicate primary keys.

    Returns number of duplicate rows.
    """
    if key not in df.columns:
        raise ValueError(f"Primary key column '{key}' not found in dataframe")

    return df.duplicated(subset=[key]).sum()
