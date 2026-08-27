"""Validate the harmonized data and source catalogue."""

from __future__ import annotations

import argparse
from pathlib import Path

from wait_times.quality import validate_source_catalogue, validate_wait_times


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-sample", action="store_true", help="Check synthetic test data")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    data_path = (
        root / "data/sample/wait_times_example.csv"
        if args.use_sample
        else root / "data/processed/wait_times_harmonized.csv"
    )
    if not data_path.exists():
        raise SystemExit(f"Input not found: {data_path}")

    errors = validate_wait_times(data_path)
    errors.extend(validate_source_catalogue(root / "config/sources.csv"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("All quality checks passed.")


if __name__ == "__main__":
    main()
