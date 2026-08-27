.PHONY: install demo-db db check forecast test

install:
	python -m pip install -e ".[dev]"

demo-db:
	python scripts/build_database.py --use-sample

db:
	python scripts/build_database.py

check:
	python scripts/run_quality_checks.py

forecast:
	python scripts/train_baseline.py

test:
	pytest -q
