# Contributing

## Branches

- `main`: reviewed and reproducible work only
- `feature/<short-name>`: new data source, analysis, model or dashboard
- `fix/<short-name>`: corrections

## Pull-request checklist

- [ ] Source URL, licence, retrieval date and definition are recorded.
- [ ] Raw data remains unchanged and outside Git.
- [ ] New columns are documented in `docs/data_dictionary.md`.
- [ ] Units are converted to days only when conversion is valid.
- [ ] Suppression and missing values are preserved, not changed to zero.
- [ ] Comparability tier is assigned.
- [ ] Quality checks pass.
- [ ] Dashboard or model claims can be reproduced from code.
- [ ] No patient-level information, credentials or large binaries are committed.

## Commit style

Use short, specific messages such as:

```text
feat: add CIHI hip and knee loader
fix: preserve suppressed Saskatchewan counts
docs: explain cataract first-eye exception
```
