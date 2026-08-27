import pandas as pd

from wait_times.models.linear_trend import forecast_linear_trends


def test_linear_trend_forecasts_two_future_years() -> None:
    data = pd.DataFrame(
        {
            "province_code": ["ON"] * 6,
            "procedure_code": ["HIP_REPLACEMENT"] * 6,
            "geography_level": ["province"] * 6,
            "comparability_tier": ["A"] * 6,
            "period_end": [f"{year}-09-30" for year in range(2019, 2025)],
            "median_wait_days": [120, 118, 116, 114, 112, 110],
        }
    )

    result = forecast_linear_trends(data)

    assert result["forecast_year"].tolist() == [2025, 2026]
    assert result["predicted_median_wait_days"].tolist() == [108.0, 106.0]
    assert (result["test_mae"] <= result["naive_test_mae"]).all()
