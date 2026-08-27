"""Train the MVP linear-trend model and write two-year forecasts."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from wait_times.models.linear_trend import forecast_linear_trends


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/processed/wait_times_harmonized.csv"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/processed/wait_times_forecast.csv"),
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    input_path = args.input if args.input.is_absolute() else root / args.input
    output_path = args.output if args.output.is_absolute() else root / args.output
    if not input_path.exists():
        raise SystemExit(f"Input not found: {input_path}")

    forecasts = forecast_linear_trends(pd.read_csv(input_path))
    if forecasts.empty:
        raise SystemExit("No series had at least five unique annual observations.")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    forecasts.to_csv(output_path, index=False)
    print(f"Wrote {len(forecasts):,} forecast rows to {output_path}.")


if __name__ == "__main__":
    main()
