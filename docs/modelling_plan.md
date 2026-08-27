# Simple two-week modelling plan

## Goal

Create an understandable, exploratory two-year forecast of median surgical wait time. This is a small portfolio demonstration of regression—not a production forecasting system.

## MVP model

Build a separate model for each province/procedure series:

```text
median_wait_days = intercept + coefficient × year
```

Use only:

- reporting year;
- median Wait 2 in days;
- province;
- procedure.

The province and procedure identify the series; they do not need to become complex features in the first version.

## Evaluation

1. Sort each series by year.
2. Train on all years except the latest 2–3 observations.
3. Predict the held-out years.
4. Compare mean absolute error with a naive model that repeats the latest training value.
5. If regression does not beat the naive model, say so and use the naive model as the official baseline.

Do not randomly split observations because that would let future years influence the training set.

## Output columns

- `province_code`
- `procedure_code`
- `forecast_year`
- `predicted_median_wait_days`
- `model_name`
- `trained_through_year`
- `test_mae`
- `naive_test_mae`

## Honest interpretation

The model assumes the historical linear trend continues. It does not know about future funding, staffing, policy, population changes, unexpected backlogs or new surgical capacity. Display it as “exploratory trend forecast.”

## Future versions

After the MVP, add lagged waits, completed volume, population ageing, workforce, beds and spending; then test Ridge regression, time-series models and prediction intervals. These belong in the future backlog.
