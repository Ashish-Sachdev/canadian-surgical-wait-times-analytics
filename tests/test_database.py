from pathlib import Path

import duckdb

from wait_times.db import build_database

ROOT = Path(__file__).resolve().parents[1]


def test_build_database(tmp_path: Path) -> None:
    database = tmp_path / "test.duckdb"
    count = build_database(
        ROOT,
        ROOT / "data/sample/wait_times_example.csv",
        database,
    )
    assert count == 12
    with duckdb.connect(str(database), read_only=True) as connection:
        latest_count = connection.execute(
            "SELECT COUNT(*) FROM vw_latest_province_kpis"
        ).fetchone()[0]
    assert latest_count == 6
