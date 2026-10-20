---
type: Capability
id: data-anomaly-detection
title: Data anomaly detection
description: Learn normal patterns in data and alert on unexpected changes without hand-written rules.
aliases: [ML-based monitors]
broader: [data-observability]
related: [augmented-analytics, drift-detection, data-quality-rules, data-issue-management]
depends_on: [data-profiling]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The tool builds time-series models from history for metrics such as row counts, null rates, distinct counts, averages and category shares, allowing for trend, weekly cycles and seasonality. If Monday loads usually hold about 2 million rows and today's holds 1.2 million, or the share of orders in euros jumps from 30% to 70%, it raises an alert showing the expected range next to the observed value.

It catches the failures hand-written rules miss: a source system change, a silent filter bug, a partner sending partial files. It needs history to learn from, and it raises false positives after genuine business changes, so owners must be able to mark alerts as expected. Methods range from simple statistical bounds to machine learning across many metrics at once. It differs from augmented analytics, which looks for business changes worth acting on; here the target is broken or suspect data.

# Key considerations

- Models need weeks of stable history. New or highly seasonal datasets need rules or wider bounds at first.
- Let owners mark alerts as expected, for example after a planned migration or promotion, so models adapt instead of repeating the alert.
- Monitor segments as well as totals. A total row count can look normal while one country has disappeared.
- Computing statistics for many columns on many tables costs compute. Choose metrics and sampling deliberately.

# Questions to ask

- Which failures have reached consumers despite existing rules?
- How many tables need monitoring, and could rules realistically be written for all of them?
- Who will triage anomaly alerts and give feedback on them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data observability](data-observability.md) |
| Related | [Augmented analytics](../analytics-bi/augmented-analytics.md), [Data issue management](data-issue-management.md), [Data profiling](data-profiling.md), [Data quality rules](data-quality-rules.md), [Data threat detection](../security/data-threat-detection.md), [Drift detection](../mlops/drift-detection.md), [Spend forecasting and anomaly detection](../platform-operations/cost-forecasting.md) |
| Depends on | [Data profiling](data-profiling.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 4, Measured)
- **Frameworks:** [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-210 to 8000-230 – Sensor data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Glue Data Quality anomaly detection observations | [AWS Glue Data Quality](../../technologies/aws/aws-glue-data-quality.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake data quality monitoring (data metric functions)](../../technologies/snowflake/snowflake-data-quality-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) | Data quality monitoring anomaly detection | [Databricks data quality monitoring anomaly detection](../../technologies/databricks/databricks-dqm-anomaly-detection.md) (preview) |
| [Informatica](../../platforms/platform-informatica.md) | data observability events | [Informatica data observability](../../technologies/informatica/informatica-data-observability.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data observability in IBM watsonx.data integration](../../technologies/ibm/ibm-data-observability.md), [Data quality in IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence-quality.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Data Quality rules](../../technologies/dataiku/dataiku-data-quality.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Bigeye AI Trust Platform](../../technologies/independent/bigeye.md), [Collibra Data Quality & Observability](../../technologies/independent/collibra-data-quality-observability.md), [Monte Carlo Data + AI Observability](../../technologies/independent/monte-carlo-data-observability.md), [Sifflet](../../technologies/independent/sifflet.md), [Soda Cloud](../../technologies/independent/soda-cloud.md) |
