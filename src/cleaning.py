import pandas as pd

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names:
    - lowercase
    - replace spaces with underscores
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
