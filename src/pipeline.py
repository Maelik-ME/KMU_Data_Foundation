import sys
import logging

from src.io import load_csv, save_parquet
from src.cleaning import (
    standardize_column_names,
    parse_dates,
    parse_amounts
)
from src.validation import (
    check_missing_values,
    check_duplicates
)
from src.config import RAW_PATH, PROCESSED_PATH
from src.logging_config import setup_logging


def run_pipeline() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)

    try:
        logger.info("Loading raw data")
        df = load_csv(RAW_PATH)

        logger.info("Standardizing column names")
        df = standardize_column_names(df)

        logger.info("Cleaning data")
        df = parse_dates(df)
        df = parse_amounts(df)

        logger.info("Running data quality checks")
        missing = check_missing_values(df)
        duplicates = check_duplicates(df, key="orderid")

        if missing:
            logger.warning(f"Missing values detected: {missing}")

        if duplicates > 0:
            logger.error(f"Duplicate order IDs detected: {duplicates}")
            logger.error("Pipeline stopped due to data quality violation")
            sys.exit(1)

        logger.info("Saving processed data")
        save_parquet(df, PROCESSED_PATH)

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.exception("Unexpected pipeline failure")
        sys.exit(2)


if __name__ == "__main__":
    run_pipeline()
