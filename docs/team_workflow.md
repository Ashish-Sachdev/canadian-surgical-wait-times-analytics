# Team workflow

## Board columns

`Backlog → Ready → In progress → Review → Done`

Each issue should contain the source/feature, acceptance criteria, owner, reviewer and expected file paths.

## Data handoff contract

The data engineer publishes only the harmonized schema documented in `data_dictionary.md`. The BI and modelling teammates query DuckDB views rather than maintaining private spreadsheet copies.

## Review rules

- At least one teammate reviews every pull request.
- A metric-definition change requires lead and QA approval.
- A source refresh includes row counts and changed-period notes.
- Dashboard filters and model features must be committed as documentation or code.

## File naming

- Raw file: `<publisher>_<dataset>_<release-date>.<ext>`
- Notebook: `01_source_profile.ipynb`, `02_eda.ipynb`, `03_model.ipynb`
- Processed output: `wait_times_harmonized.csv`
- Forecast output: `wait_times_forecast.csv`

## Decision log template

```markdown
## YYYY-MM-DD — Decision title

- Decision:
- Reason:
- Alternatives considered:
- Impacted files/metrics:
- People present:
```
