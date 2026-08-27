"""Data quality rules shared by scripts and tests."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from wait_times.db import FACT_COLUMNS

VALID_PROVINCES = {"BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL"}
VALID_TIERS = {"A", "B", "C"}


def validate_wait_times(path: Path) -> list[str]:
    """Return human-readable validation errors; an empty list means success."""
    data = pd.read_csv(path)
    errors: list[str] = []
    missing_columns = sorted(set(FACT_COLUMNS) - set(data.columns))
    if missing_columns:
        return [f"Missing columns: {missing_columns}"]

    unknown_provinces = set(data["province_code"].dropna()) - VALID_PROVINCES
    if unknown_provinces:
        errors.append(f"Unknown province codes: {sorted(unknown_provinces)}")
    unknown_tiers = set(data["comparability_tier"].dropna()) - VALID_TIERS
    if unknown_tiers:
        errors.append(f"Unknown comparability tiers: {sorted(unknown_tiers)}")

    for column in ["median_wait_days", "p90_wait_days", "completed_volume", "waiting_volume"]:
        numeric = pd.to_numeric(data[column], errors="coerce")
        if (numeric.dropna() < 0).any():
            errors.append(f"Negative values found in {column}")

    pct = pd.to_numeric(data["within_benchmark_pct"], errors="coerce").dropna()
    if ((pct < 0) | (pct > 100)).any():
        errors.append("within_benchmark_pct must be between 0 and 100")

    period_start = pd.to_datetime(data["period_start"], errors="coerce")
    period_end = pd.to_datetime(data["period_end"], errors="coerce")
    if period_start.isna().any() or period_end.isna().any():
        errors.append("Invalid period dates found")
    elif (period_end < period_start).any():
        errors.append("period_end occurs before period_start")

    duplicate_key = [
        "source_id",
        "province_code",
        "geography_level",
        "geography_name",
        "procedure_code",
        "period_start",
        "period_end",
        "wait_segment",
    ]
    if data.duplicated(duplicate_key).any():
        errors.append("Duplicate harmonized record keys found")
    return errors


def validate_source_catalogue(path: Path) -> list[str]:
    sources = pd.read_csv(path).fillna("")
    errors: list[str] = []
    if sources["source_id"].duplicated().any():
        errors.append("Duplicate source_id values found")
    for index, url in sources["landing_url"].items():
        if not str(url).startswith("https://"):
            errors.append(f"Row {index + 2} has an invalid landing_url")
    return errors
