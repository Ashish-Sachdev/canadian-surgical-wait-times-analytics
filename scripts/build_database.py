"""Build the DuckDB analytics mart from harmonized or synthetic sample data."""

from __future__ import annotations

import argparse
from pathlib import Path

from wait_times.db import build_database


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-sample", action="store_true", help="Use synthetic test data")
    parser.add_argument("--database", type=Path, default=Path("data/analytics.duckdb"))
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    data_path = (
        root / "data/sample/wait_times_example.csv"
        if args.use_sample
        else root / "data/processed/wait_times_harmonized.csv"
    )
    if not data_path.exists():
        raise SystemExit(
            f"Input not found: {data_path}. Add harmonized data or pass --use-sample."
        )
    database_path = args.database if args.database.is_absolute() else root / args.database
    count = build_database(root, data_path, database_path)
    print(f"Built {database_path} with {count:,} wait-time rows.")


if __name__ == "__main__":
    main()
