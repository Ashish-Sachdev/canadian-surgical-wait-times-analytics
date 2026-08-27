# Harmonized data dictionary

One row represents one province/geography, procedure, wait segment and reporting period.

| Column | Type | Required | Description |
| --- | --- | --- | --- |
| `source_id` | text | Yes | Stable ID from `config/sources.csv` |
| `province_code` | text | Yes | Two-letter code: BC, AB, SK, MB, ON, QC, NB, NS, PE, NL |
| `geography_level` | text | Yes | `province`, `region`, `facility` or `surgeon` |
| `geography_name` | text | Yes | Published geographic/facility label |
| `procedure_code` | text | Yes | Canonical value from the procedure crosswalk |
| `procedure_name` | text | Yes | Human-readable canonical name |
| `period_start` | date | Yes | Inclusive start date of cohort/reporting period |
| `period_end` | date | Yes | Inclusive end date of cohort/reporting period |
| `reporting_frequency` | text | Yes | `annual`, `semiannual`, `quarterly`, `monthly`, `snapshot` |
| `wait_segment` | text | Yes | `wait_1`, `wait_2`, `total`, or `not_applicable` |
| `median_wait_days` | number | No | Retrospective median wait in calendar days |
| `p90_wait_days` | number | No | Retrospective 90th-percentile wait in calendar days |
| `completed_volume` | integer | No | Completed procedures in the cohort |
| `waiting_volume` | integer | No | Patients/cases waiting at the snapshot date |
| `benchmark_days` | number | No | Applicable benchmark in days |
| `within_benchmark_pct` | number | No | Percentage from 0 to 100 |
| `is_suppressed` | boolean | Yes | True when publisher suppressed a value |
| `comparability_tier` | text | Yes | A, B or C per `docs/methodology.md` |
| `definition_version` | text | Yes | Short source/method version label |
| `source_url` | text | Yes | Page or file supporting the record |
| `retrieved_at` | date | Yes | Date file/page was retrieved |

## Missing and suppressed data

- Keep unavailable values as null, never zero.
- Set `is_suppressed = true` for symbols such as `*`, `<5`, or publisher suppression text.
- Keep the original value in a source-specific interim table if auditability requires it.
- Do not impute the target KPI for dashboard rankings.

## Unit conversion

- Weeks to days: multiply by 7 only if the source explicitly uses calendar weeks.
- Hours to days: divide by 24 only for modelling convenience; retain the original-unit interim column.
- Percentages are stored from 0 to 100, not 0 to 1.
