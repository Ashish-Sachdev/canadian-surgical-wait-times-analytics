from pathlib import Path

from wait_times.quality import validate_source_catalogue, validate_wait_times

ROOT = Path(__file__).resolve().parents[1]


def test_synthetic_sample_passes_quality_checks() -> None:
    errors = validate_wait_times(ROOT / "data/sample/wait_times_example.csv")
    assert errors == []


def test_source_catalogue_passes_quality_checks() -> None:
    errors = validate_source_catalogue(ROOT / "config/sources.csv")
    assert errors == []
