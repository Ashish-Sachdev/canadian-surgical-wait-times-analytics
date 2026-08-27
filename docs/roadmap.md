# Two-week MVP roadmap

This plan assumes 10 working days and a four-person team. The objective is a polished, understandable portfolio project—not a production health-data platform.

## MVP outcome

By the end of Day 10, the team should have:

- one cleaned CIHI dataset covering hip, knee and cataract surgery;
- one DuckDB database with a harmonized province-level table;
- five validated KPIs;
- a two-page Power BI or Tableau dashboard;
- a simple linear-regression trend forecast for the next two years;
- a clear README, limitations section and short presentation.

## Team roles

| Team member | Primary responsibility | Concrete output |
| --- | --- | --- |
| Member 1 — Project/analysis lead | Scope, KPI definitions, coordination and final story | KPI document and presentation narrative |
| Member 2 — Data preparation | Download, clean, transform and load CIHI data | Harmonized CSV and DuckDB table |
| Member 3 — Dashboard | Power BI/Tableau model, visuals and filters | Two-page dashboard |
| Member 4 — Modelling/QA | Regression, validation and data-quality review | Forecast output and QA checklist |

If there are three members, combine Project Lead and Modelling/QA. Everyone reviews at least one teammate's work.

## Ten-working-day plan

| Day | Focus | Tasks | End-of-day deliverable |
| --- | --- | --- | --- |
| 1 | Confirm the question | Select hip, knee and cataract; agree on five KPIs; assign roles; create GitHub issues | One-page project scope |
| 2 | Collect and understand data | Download CIHI 2008–2025 and 2008–2024 tables; read methodology; identify sheets and provincial exceptions | Source log and data notes |
| 3 | Clean the data | Keep only required procedures/fields; standardize province names, dates and units; preserve missing values | Clean interim CSV |
| 4 | Build DuckDB | Map procedures; create the harmonized table; load data; run quality checks; manually verify five source values | Reproducible database |
| 5 | Calculate KPIs | Median, P90, within benchmark, completed volume and YoY change; identify missing coverage | Validated KPI table |
| 6 | Explore findings | Create province comparisons and trends; choose three evidence-backed findings | EDA notebook/charts |
| 7 | Build dashboard page 1 | KPI cards, procedure selector, province comparison and benchmark visual | Province comparison page |
| 8 | Build page 2 and model | Trend/volume visuals; naive baseline; simple linear regression; forecast next two years | Trends/forecast page |
| 9 | Review and improve | Test filters; check every number; add source/period/tooltips; document limitations; accessibility review | Release candidate |
| 10 | Finalize and present | Fresh-run test, README update, screenshots, presentation rehearsal and final Git tag | Portfolio-ready v1.0 |

## Daily check-in

Hold one 15-minute check-in each day:

1. What did I finish?
2. What will I finish today?
3. What is blocking me?
4. Does any KPI or definition need team approval?

## Must-have versus optional

| Must have in two weeks | Optional only if ahead of schedule |
| --- | --- |
| CIHI province-level data | One provincial drill-down source |
| Three procedures | Hip-fracture repair or one cancer surgery |
| Five KPIs | Waiting-list rate per 100,000 |
| Two dashboard pages | Streamlit application |
| Simple linear regression | Ridge, Elastic Net or scenario modelling |
| Manual source refresh | Automated downloads |

## Definition of done

- The team can rebuild the DuckDB database from documented CIHI files.
- Five manually checked dashboard values match the source.
- Missing and suppressed values are not represented as zero.
- All comparisons use the same procedure, metric and reporting period.
- The regression is evaluated against the last-value baseline.
- The forecast is labelled exploratory and its limitations are visible.
- The README explains the problem, data, method, results and how to run the project.
- Every team member can explain their contribution and one project limitation.

## What not to do during the MVP

- Do not merge every provincial dataset.
- Do not add patient-level or restricted data.
- Do not build a complex API or web application.
- Do not use a random train/test split for time-series data.
- Do not create a “best province” score by arbitrarily combining metrics.
- Do not spend time forecasting before the dashboard KPIs have been verified.
