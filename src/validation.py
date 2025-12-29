import pandas as pd

def check_missing_values(df: pd.DataFrame) -> dict:
    """
    Check for missing values per column.
    Returns a dictionary with counts.
    """
    missing = df.isna().sum()
    return missing[missing > 0].to_dict()


def check_duplicates(df: pd.DataFrame, subset: list) -> int:
    """
    Check for duplicate rows based on subset of columns.
    Returns number of duplicate rows.
    """
    return df.duplicated(subset=subset).sum()
