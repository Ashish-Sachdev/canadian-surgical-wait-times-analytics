"""Small, transparent linear-trend forecast for the two-week MVP."""

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

OUTPUT_COLUMNS = [
    "province_code",
    "procedure_code",
    "forecast_year",
    "predicted_median_wait_days",
    "model_name",
    "trained_through_year",
    "test_mae",
    "naive_test_mae",
]


def forecast_linear_trends(
    data: pd.DataFrame,
    *,
    horizon: int = 2,
    test_periods: int = 2,
    minimum_observations: int = 5,
) -> pd.DataFrame:
    """Evaluate and forecast each province/procedure series without shuffling time."""
    frame = data.copy()
    frame["year"] = pd.to_datetime(frame["period_end"]).dt.year
    frame["median_wait_days"] = pd.to_numeric(frame["median_wait_days"], errors="coerce")
    frame = frame[
        (frame["geography_level"] == "province")
        & (frame["comparability_tier"] == "A")
        & frame["median_wait_days"].notna()
    ]

    rows: list[dict[str, object]] = []
    for (province, procedure), series in frame.groupby(["province_code", "procedure_code"]):
        series = series.sort_values("year")
        if series["year"].duplicated().any() or len(series) < minimum_observations:
            continue

        split = len(series) - test_periods
        if split < 2:
            continue
        train = series.iloc[:split]
        test = series.iloc[split:]

        evaluation_model = LinearRegression().fit(train[["year"]], train["median_wait_days"])
        test_prediction = evaluation_model.predict(test[["year"]])
        test_mae = mean_absolute_error(test["median_wait_days"], test_prediction)
        naive_prediction = [train["median_wait_days"].iloc[-1]] * len(test)
        naive_mae = mean_absolute_error(test["median_wait_days"], naive_prediction)

        final_model = LinearRegression().fit(series[["year"]], series["median_wait_days"])
        last_year = int(series["year"].max())
        future_years = pd.DataFrame({"year": range(last_year + 1, last_year + horizon + 1)})
        future_predictions = final_model.predict(future_years)

        for forecast_year, prediction in zip(future_years["year"], future_predictions):
            rows.append(
                {
                    "province_code": province,
                    "procedure_code": procedure,
                    "forecast_year": int(forecast_year),
                    "predicted_median_wait_days": max(0.0, float(prediction)),
                    "model_name": "linear_trend",
                    "trained_through_year": last_year,
                    "test_mae": float(test_mae),
                    "naive_test_mae": float(naive_mae),
                }
            )
    return pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
