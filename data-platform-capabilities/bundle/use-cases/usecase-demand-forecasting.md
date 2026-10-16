---
type: Use Case
id: usecase-demand-forecasting
title: Demand forecasting
description: Forecast demand by product, location and time to plan stock, staff and supply.
aliases: [sales forecasting, supply planning forecasts]
requires:
- {capability: batch-ingestion, level: 3, why: 'Sales, stock, price and promotion data arrive from POS, ERP and supply systems on a schedule.'}
- {capability: time-series-data, level: 2, why: 'History must be stored and queried efficiently by product, location and period.'}
- {capability: data-quality-rules, level: 3, why: 'Missing sales days, stock-outs and returns distort demand unless they are detected and handled.'}
- {capability: hierarchy-management, level: 3, why: 'Forecasts are made and reconciled across product, location and time hierarchies that change.'}
- {capability: distributed-processing, level: 2, why: Training and scoring millions of series must run in parallel within the cycle.}
- {capability: model-training, level: 2, why: Models are retrained on each cycle or on a regular schedule.}
- {capability: experiment-tracking, level: 2, why: Methods and parameters must be compared across many series and segments.}
- {capability: model-evaluation, level: 3, why: Backtests against naive baselines by segment decide which method each series uses.}
- {capability: batch-inference, level: 3, why: The full forecast is produced on a fixed cycle for every series and horizon.}
- {capability: workflow-orchestration, level: 3, why: 'Data refresh, training, forecasting and publication run in order before planning deadlines.'}
- {capability: model-performance-monitoring, level: 3, why: 'Forecast accuracy and bias are measured against actuals each period, at each level.'}
- {capability: data-writeback, level: 2, why: 'Planners adjust forecasts for known events, and those overrides must be stored and measured.'}
- {capability: ml-pipelines, level: 3, why: 'Data validation, training, backtesting and forecasting for every series run as one automated pipeline each cycle.'}
benefits_from:
- {capability: pretrained-predictive-models, why: Pretrained time-series models give usable forecasts for new or sparse series.}
- {capability: data-enrichment, why: 'Weather, holidays and local events explain demand changes.'}
- {capability: enterprise-planning, why: Feeds forecasts straight into budgeting and sales and operations planning.}
- {capability: external-data-sharing, why: Shares forecasts with suppliers without sending files.}
- {capability: automl, why: Selects methods per segment with little manual effort.}
- {capability: hyperparameter-tuning, why: Improves accuracy for high-value series.}
- {capability: reverse-etl, why: Pushes forecasts into replenishment and workforce systems.}
- {capability: product-information-management, why: Product attributes help forecast new products from similar ones.}
personas:
- persona-data-scientist
- persona-ml-engineer
- persona-business-user
- persona-data-analyst
- persona-data-engineer
patterns: [fti-pipelines, medallion-architecture, dimensional-modelling]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Retailers, manufacturers, distributors and service organisations forecast demand by product, location and period to decide stock levels, production, staffing and purchasing. Sales history, promotions, prices, stock positions, calendars and sometimes weather are combined into time series, often millions of them, and models are trained and run on a regular cycle. Forecasts are reconciled across product and location hierarchies, reviewed and adjusted by planners, and passed to planning and supply systems.

Good looks like forecasts that beat simple baselines at the levels where decisions are made, bias tracked and corrected, planner overrides recorded and measured, and each cycle finished before the planning meeting. Lost sales during stock-outs must be handled, otherwise the model learns that demand was low when there was simply nothing to sell.

# Non-functional requirements

- Granularity down to product, location and day or week, often millions of series.
- Each cycle, daily or weekly, completes within its batch window before planning decisions.
- Horizons from a few days for replenishment to 12 to 18 months for capacity and budgets.
- Every published forecast is versioned so it can later be compared with actuals.

# Risks

- Stock-outs are read as low demand and forecasts spiral downwards.
- Planner overrides are not measured, so it is unknown whether they help.
- New stores, new products and hierarchy changes break the history models rely on.
- Complex models do not beat simple baselines once maintenance cost is counted.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Sales, stock, price and promotion data arrive from POS, ERP and supply systems on a schedule. |
| [Time-series data](../capabilities/specialised-data/time-series-data.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 2 (Managed) | History must be stored and queried efficiently by product, location and period. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Missing sales days, stock-outs and returns distort demand unless they are detected and handled. |
| [Hierarchy management](../capabilities/master-data/hierarchy-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | Forecasts are made and reconciled across product, location and time hierarchies that change. |
| [Distributed processing](../capabilities/processing/distributed-processing.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Training and scoring millions of series must run in parallel within the cycle. |
| [Model training](../capabilities/machine-learning/model-training.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Models are retrained on each cycle or on a regular schedule. |
| [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 2 (Managed) | Methods and parameters must be compared across many series and segments. |
| [Model evaluation](../capabilities/machine-learning/model-evaluation.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Backtests against naive baselines by segment decide which method each series uses. |
| [Batch inference](../capabilities/mlops/batch-inference.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | The full forecast is produced on a fixed cycle for every series and horizon. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 3 (Defined) | Data refresh, training, forecasting and publication run in order before planning deadlines. |
| [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md) | [ML operations](../capabilities/mlops/mlops.md) | 3 (Defined) | Forecast accuracy and bias are measured against actuals each period, at each level. |
| [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Planners adjust forecasts for known events, and those overrides must be stored and measured. |
| [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) | [Machine learning development](../capabilities/machine-learning/machine-learning.md) | 3 (Defined) | Data validation, training, backtesting and forecasting for every series run as one automated pipeline each cycle. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Pretrained predictive models](../capabilities/machine-learning/pretrained-predictive-models.md) | Pretrained time-series models give usable forecasts for new or sparse series. |
| [Data enrichment](../capabilities/processing/data-enrichment.md) | Weather, holidays and local events explain demand changes. |
| [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md) | Feeds forecasts straight into budgeting and sales and operations planning. |
| [External data sharing](../capabilities/data-sharing/external-data-sharing.md) | Shares forecasts with suppliers without sending files. |
| [AutoML](../capabilities/machine-learning/automl.md) | Selects methods per segment with little manual effort. |
| [Hyperparameter tuning](../capabilities/machine-learning/hyperparameter-tuning.md) | Improves accuracy for high-value series. |
| [Reverse ETL](../capabilities/serving/reverse-etl.md) | Pushes forecasts into replenishment and workforce systems. |
| [Product information management](../capabilities/master-data/product-information-management.md) | Product attributes help forecast new products from similar ones. |

# Personas

- [Data scientist](../personas/persona-data-scientist.md): Explores data and builds statistical and machine learning models.
- [ML engineer](../personas/persona-ml-engineer.md): Takes models to production and keeps them running reliably.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.

# Patterns

- [Feature, training and inference pipelines](../patterns/fti-pipelines.md)
- [Medallion architecture](../patterns/medallion-architecture.md)
- [Dimensional modelling](../patterns/dimensional-modelling.md)

# Frameworks that apply

- [Google Cloud MLOps levels](../frameworks/framework-google-mlops-levels.md): Google Cloud's three-level description of how far an organisation has automated the building, training and release of machine learning systems.
- [Microsoft MLOps maturity model](../frameworks/framework-microsoft-mlops-maturity.md): A five-level model from Microsoft that describes MLOps maturity across people, model creation, model release and application integration.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 10 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 12 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 10 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 11 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) |
| [Databricks](../platforms/platform-databricks.md) | 9 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 13 | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Informatica](../platforms/platform-informatica.md) | 5 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 5 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) |
| [SAP](../platforms/platform-sap.md) | 5 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [Model training](../capabilities/machine-learning/model-training.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Teradata](../platforms/platform-teradata.md) | 6 of 13 | [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Model evaluation](../capabilities/machine-learning/model-evaluation.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md) |
| [IBM](../platforms/platform-ibm.md) | 6 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Palantir](../platforms/platform-palantir.md) | 7 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Experiment tracking](../capabilities/machine-learning/experiment-tracking.md), [Batch inference](../capabilities/mlops/batch-inference.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Model performance monitoring](../capabilities/mlops/model-performance-monitoring.md), [ML pipelines](../capabilities/machine-learning/ml-pipelines.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 12 of 13 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md) |
| [Independent vendors](../platforms/platform-independent.md) | 10 of 13 | [Time-series data](../capabilities/specialised-data/time-series-data.md), [Distributed processing](../capabilities/processing/distributed-processing.md), [Batch inference](../capabilities/mlops/batch-inference.md) |
