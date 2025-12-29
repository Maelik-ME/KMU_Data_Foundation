import sys
import logging

from src.io import (
    load_csv,
    save_parquet,
    save_output_csv
)

from src.cleaning import (
    standardize_column_names,
    parse_dates,
    parse_amounts
)

from src.validation import (
    check_missing_values,
    check_duplicates
)

from src.config import (
    RAW_PATH,
    PROCESSED_PATH,
    OUTPUT_PATH,
    STOP_ON_DUPLICATES,
    STOP_ON_MISSING_VALUES,
    DQ_REPORT_PATH
)

from src.logging_config import setup_logging
from src.reporting import save_data_quality_report


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
        duplicates = check_duplicates(df, "orderid")

        dq_report = {
            "missing_values": missing,
            "duplicate_primary_keys": duplicates
        }

        if missing:
            logger.warning(f"Missing values detected: {missing}")

        if duplicates > 0:
            logger.error(f"Duplicate order IDs detected: {duplicates}")

        logger.info("Saving data quality report")
        save_data_quality_report(
            report=dq_report,
            output_path=DQ_REPORT_PATH
        )

        if missing and STOP_ON_MISSING_VALUES:
            logger.error("Pipeline stopped due to missing values")
            sys.exit(1)

        if duplicates > 0 and STOP_ON_DUPLICATES:
            logger.error("Pipeline stopped due to duplicate primary keys")
            sys.exit(1)
            
        # --- Persist results ---
        logger.info("Saving processed data")
        save_parquet(df, PROCESSED_PATH)

        logger.info("Saving output data")
        save_output_csv(df, OUTPUT_PATH)

        save_data_quality_report(
            missing=missing,
            duplicates=duplicates,
            status="SUCCESS",
            path=DQ_REPORT_PATH
        )

        logger.info("Pipeline completed successfully")
        sys.exit(0)

    except Exception:
        logger.exception("Unexpected pipeline failure")
        sys.exit(2)


if __name__ == "__main__":
    run_pipeline()
