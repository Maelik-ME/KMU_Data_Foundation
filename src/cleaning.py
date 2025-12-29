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


def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse order_date column into datetime.
    Invalid or ambiguous dates become NaT.
    """
    df = df.copy()

    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"],
            errors="coerce",
            dayfirst=True
        )

    return df


def parse_amounts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse amount_chf column into numeric.
    Invalid values become NaN.
    """
    df = df.copy()

    if "amount_chf" in df.columns:
        df["amount_chf"] = pd.to_numeric(
            df["amount_chf"],
            errors="coerce"
        )

    return df
