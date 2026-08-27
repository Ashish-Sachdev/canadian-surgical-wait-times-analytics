# Methodology and comparability

## Unit of analysis

Use a province–procedure–period panel for national comparison. Facility and surgeon rows belong in separate drill-down views and must not be averaged to create a provincial result unless the publisher supplies valid weights.

## Comparability tiers

| Tier | Meaning | Dashboard use |
| --- | --- | --- |
| A | Same CIHI definition, cohort, period, unit and procedure | National ranking and KPI cards |
| B | Provincial source mapped to the CIHI definition with only documented minor differences | Comparison with warning icon and footnote |
| C | Different wait segment, cohort, procedure definition, reporting period or unknown mapping | Province-only drill-down; no national ranking |

## Harmonization decisions

1. Keep Wait 1 and Wait 2 separate.
2. Store completed-case wait metrics separately from current waiting-list measures.
3. Convert valid weekly measures to calendar days, but retain the source unit in interim data.
4. Use fiscal/reporting period end as the model time index; keep both start and end dates.
5. Preserve provincial suppression.
6. Never average medians or P90s across facilities. Use the published province total.
7. Do not combine first- and second-eye cataract values when comparing against CIHI first-eye definitions.
8. Mark 2020–2022 as a structural-break period and include a pandemic indicator in modelling.

## Province scorecards

Avoid a single overall “best province” score in the first version. If the team later adds one, publish the formula and calculate only from Tier A metrics. A defensible example is the unweighted mean percentile rank across hip, knee and cataract within-benchmark rates, with at least two reported procedures required.

## Reproducibility record

For every download, record:

- source ID and URL;
- retrieval date;
- file name and reporting release;
- filters used for a dashboard export;
- licence/terms;
- checksum if the pipeline becomes automated;
- transformation script and output row count.
