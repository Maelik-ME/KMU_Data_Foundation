import json
from pathlib import Path
from typing import Any, Dict

import numpy as np


def _to_python_type(value: Any) -> Any:
    """
    Convert numpy / pandas scalar types to native Python types
    so they can be serialized to JSON.
    """
    if isinstance(value, np.generic):
        return value.item()
    return value


def save_data_quality_report(
    report: Dict[str, Any],
    output_path: Path
) -> None:
    """
    Save data quality report as JSON.
    Ensures all values are JSON-serializable.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    clean_report = {
        key: _to_python_type(value)
        for key, value in report.items()
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(clean_report, f, indent=2)
