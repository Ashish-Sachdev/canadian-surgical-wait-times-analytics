# KPI definitions

| KPI | Formula | Grain | Caveat |
| --- | --- | --- | --- |
| Median wait (days) | Publisher's 50th percentile | Province × procedure × period | Completed-case metric unless stated otherwise |
| P90 wait (days) | Publisher's 90th percentile | Province × procedure × period | Better signal of long waits than the median |
| Within-benchmark rate | `completed_within_benchmark / eligible_completed × 100` | Province × procedure × period | Use publisher value when denominator rules are not available |
| Completed volume | Count of eligible completed procedures | Province × procedure × period | Compare matched period lengths |
| Waiting-list volume | Eligible cases waiting on snapshot date | Province × procedure × snapshot | Prospective measure; not a wait duration |
| Backlog per 100k | `waiting_volume / population × 100000` | Province × procedure × snapshot | Population year should match the snapshot |
| YoY wait change | `(current_wait - prior_wait) / prior_wait × 100` | Same province/procedure/period type | Do not calculate across unmatched cohort lengths |
| Benchmark gap | `p90_wait_days - benchmark_days` | Province × procedure × period | Negative is better; only where benchmark exists |
| Throughput ratio | `completed_volume / additions_to_waitlist` | Province × procedure × period | Requires wait-list additions, often unavailable |

## Benchmark reference

| Procedure | Benchmark |
| --- | --- |
| Hip replacement | Within 182 days |
| Knee replacement | Within 182 days |
| Cataract surgery | Within 112 days |
| Hip-fracture repair | Within 48 hours |
| Radiation therapy | Within 28 days of ready-to-treat |

CABG urgency categories are not sufficiently consistent for one current national benchmark. Cancer surgery, CT and MRI are reported without a single pan-Canadian benchmark in the main CIHI series.

## Dashboard formatting

- Show median and P90 together.
- Show numerator/volume or a coverage note beside percentages.
- Use “Not reported” for null and “Suppressed” for protected values.
- Include the reporting period in every tooltip.
- Use neutral colours for rankings; do not imply clinical quality from access metrics alone.
