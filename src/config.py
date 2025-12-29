from pathlib import Path

# Project root (one level above src/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = DATA_DIR / "output"

# Files
RAW_PATH = RAW_DIR / "orders.csv"
PROCESSED_PATH = PROCESSED_DIR / "orders.parquet"
