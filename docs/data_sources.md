# Data source catalogue

Verified on **2026-08-27**. The machine-readable catalogue is [config/sources.csv](../config/sources.csv).

## Best starting datasets

1. **CIHI 2008–2025 priority procedures (XLSX):** latest comparable hip and knee wait times and volumes at national, provincial and selected regional levels.
2. **CIHI 2008–2024 priority procedures (XLSX):** broader procedure coverage, including cataract, hip fracture, cancer surgeries, CABG, radiation, CT and MRI.
3. **CIHI methodology notes (PDF):** required definitions, inclusion/exclusion rules, benchmarks and provincial exceptions.
4. **Nova Scotia Socrata dataset and B.C. open data:** strongest public machine-readable provincial drill-down candidates.
5. **Ontario, Manitoba, Alberta, Quebec and New Brunswick dashboards/exports:** valuable detail but require filter/version documentation.

## Provincial availability

| Province | Provincial public source | Bulk machine-readable? | Best use | Main warning |
| --- | --- | --- | --- | --- |
| BC | BC Surgical Wait Times | Yes, CSV | Quarterly hospital/procedure detail | Scheduled inpatient/day surgery; confirm current resource version |
| AB | Alberta Health System Dashboard | Conditional visual export | Facility and surgery trends | Power BI export/schema may change |
| SK | Surgical Performance and Wait Times | Mainly PDF/HTML | Quarterly procedure and area detail | Extraction work; suppressed counts |
| MB | Wait Time Dashboard and surgical tables | Linked XLSX for some histories | Monthly median, waiting and completed counts | Selected services and changing coverage |
| ON | Ontario Health Wait Times Results | Yes, dashboard CSV export | Wait 1/Wait 2, priority, hospital and region | Export filters must be recorded; full WTIS is restricted |
| QC | Données Québec surgery wait-list portrait | Yes, CSV | Wait-list, specialty and institution analysis | Prospective waiting list differs from completed-case wait |
| NB | Surgical Wait Time website | No documented bulk file | Procedure, hospital and surgeon median/P90 | Selected procedures; HTML extraction; suppression |
| NS | Nova Scotia Open Data/Socrata | Yes, CSV/API | Consultation and surgery waits by procedure/community | Check measure and period columns before joining |
| PE | CIHI provincial indicators | No separate provincial file found | Pan-Canadian comparison | Less provincial drill-down |
| NL | Provincial Wait Times pages/reports | Mainly HTML/PDF | Selected procedure/zone cross-check | No public bulk machine-readable file identified |

## CIHI scope notes

CIHI reports median, 90th percentile, volume and within-benchmark rates where a benchmark exists. The reporting cohort is generally retrospective: it describes procedures completed in a defined period. The start is commonly the date the patient and physician agree to surgery and the patient is ready; the end is the procedure date. Provincial exceptions must be retained.

Do not treat these as interchangeable:

- retrospective wait of completed patients;
- prospective age of patients still waiting;
- wait from referral to specialist consult (Wait 1);
- wait from decision-to-treat to surgery (Wait 2);
- calendar-year, fiscal-year, quarterly and April–September cohorts.

## Recommended source priority

For a cross-province visual, use this order:

1. Same CIHI release, procedure, metric and reporting period.
2. Same pan-Canadian definition but different CIHI release, with a visible version note.
3. Provincial values mapped exactly to the CIHI definition and marked Tier B.
4. Province-only detail marked Tier C; never place it in a national ranking.

## Context datasets for regression

- Statistics Canada 17-10-0005-01: observed population by age and province.
- Statistics Canada 17-10-0057-01: population projections by scenario.
- CIHI health workforce tables: physicians, nurses and other professional supply.
- CIHI Hospital Beds: staffed and operational capacity.
- CIHI National Health Expenditure Trends: province-level health spending.

These improve context, but a small annual panel still limits forecast certainty.

## Access-restricted options

Patient-level DAD, NACRS, WTIS and provincial registry data may require a formal request, research agreement, ethics/privacy review and fees. Do not make access to those files a dependency for the class project. Public aggregate sources are enough for a strong dashboard and baseline forecast.
