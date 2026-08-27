CREATE TABLE IF NOT EXISTS dim_source (
    source_id VARCHAR PRIMARY KEY,
    jurisdiction VARCHAR NOT NULL,
    publisher VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    source_type VARCHAR NOT NULL,
    landing_url VARCHAR,
    verified_on DATE
);

CREATE TABLE IF NOT EXISTS fact_wait_times (
    source_id VARCHAR NOT NULL,
    province_code VARCHAR NOT NULL,
    geography_level VARCHAR NOT NULL,
    geography_name VARCHAR NOT NULL,
    procedure_code VARCHAR NOT NULL,
    procedure_name VARCHAR NOT NULL,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    reporting_frequency VARCHAR NOT NULL,
    wait_segment VARCHAR NOT NULL,
    median_wait_days DOUBLE,
    p90_wait_days DOUBLE,
    completed_volume BIGINT,
    waiting_volume BIGINT,
    benchmark_days DOUBLE,
    within_benchmark_pct DOUBLE,
    is_suppressed BOOLEAN NOT NULL,
    comparability_tier VARCHAR NOT NULL,
    definition_version VARCHAR NOT NULL,
    source_url VARCHAR NOT NULL,
    retrieved_at DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_forecast (
    model_id VARCHAR NOT NULL,
    province_code VARCHAR NOT NULL,
    procedure_code VARCHAR NOT NULL,
    forecast_year INTEGER NOT NULL,
    target_metric VARCHAR NOT NULL,
    point_forecast DOUBLE NOT NULL,
    lower_80 DOUBLE,
    upper_80 DOUBLE,
    lower_95 DOUBLE,
    upper_95 DOUBLE,
    scenario VARCHAR NOT NULL,
    trained_through_year INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL
);
