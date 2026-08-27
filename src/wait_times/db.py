"""DuckDB build utilities."""

from __future__ import annotations

from pathlib import Path

import duckdb

FACT_COLUMNS = [
    "source_id",
    "province_code",
    "geography_level",
    "geography_name",
    "procedure_code",
    "procedure_name",
    "period_start",
    "period_end",
    "reporting_frequency",
    "wait_segment",
    "median_wait_days",
    "p90_wait_days",
    "completed_volume",
    "waiting_volume",
    "benchmark_days",
    "within_benchmark_pct",
    "is_suppressed",
    "comparability_tier",
    "definition_version",
    "source_url",
    "retrieved_at",
]


def build_database(project_root: Path, data_path: Path, database_path: Path) -> int:
    """Create the DuckDB analytics mart and return the inserted fact row count."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = duckdb.connect(str(database_path))
    try:
        connection.execute((project_root / "sql" / "schema.sql").read_text(encoding="utf-8"))
        connection.execute("DELETE FROM fact_wait_times")
        connection.execute(
            "CREATE OR REPLACE TEMP TABLE staging_wait_times AS "
            "SELECT * FROM read_csv_auto(?, header = true, all_varchar = false)",
            [str(data_path)],
        )
        available = {
            row[1]
            for row in connection.execute("PRAGMA table_info('staging_wait_times')").fetchall()
        }
        missing = sorted(set(FACT_COLUMNS) - available)
        if missing:
            raise ValueError(f"Input data is missing required columns: {missing}")

        column_list = ", ".join(FACT_COLUMNS)
        connection.execute(
            f"INSERT INTO fact_wait_times ({column_list}) "
            f"SELECT {column_list} FROM staging_wait_times"
        )
        connection.execute((project_root / "sql" / "views.sql").read_text(encoding="utf-8"))
        return connection.execute("SELECT COUNT(*) FROM fact_wait_times").fetchone()[0]
    finally:
        connection.close()
