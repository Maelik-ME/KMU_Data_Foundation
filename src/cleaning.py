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

def parse_order_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse order_date column into datetime.
    Invalid or ambiguous dates become NaT.
    """
    df = df.copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce",
        dayfirst=True
    )

    return df