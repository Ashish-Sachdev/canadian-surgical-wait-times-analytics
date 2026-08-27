CREATE OR REPLACE VIEW vw_comparable_province_kpis AS
SELECT
    source_id,
    province_code,
    procedure_code,
    procedure_name,
    period_start,
    period_end,
    median_wait_days,
    p90_wait_days,
    completed_volume,
    benchmark_days,
    within_benchmark_pct,
    retrieved_at
FROM fact_wait_times
WHERE geography_level = 'province'
  AND comparability_tier = 'A'
  AND NOT is_suppressed;

CREATE OR REPLACE VIEW vw_latest_province_kpis AS
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY province_code, procedure_code
               ORDER BY period_end DESC, retrieved_at DESC
           ) AS row_num
    FROM vw_comparable_province_kpis
)
SELECT * EXCLUDE (row_num)
FROM ranked
WHERE row_num = 1;

CREATE OR REPLACE VIEW vw_benchmark_gap AS
SELECT *,
       p90_wait_days - benchmark_days AS p90_benchmark_gap_days
FROM vw_comparable_province_kpis
WHERE p90_wait_days IS NOT NULL
  AND benchmark_days IS NOT NULL;
