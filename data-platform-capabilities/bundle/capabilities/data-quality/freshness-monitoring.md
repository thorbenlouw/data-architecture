---
type: Capability
id: freshness-monitoring
title: Freshness monitoring
description: Detect when data arrives later than expected or misses its freshness target.
broader: [data-observability]
related: [data-slas, pipeline-monitoring, asset-based-orchestration, data-alerting, impact-analysis]
tags: [data-quality]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A freshness monitor compares the time a table was last updated, or the newest event timestamp it contains, with an expected schedule or service level, such as daily sales loaded by 06:00 or no more than 15 minutes behind the source. When the deadline passes without an update, owners and affected consumers are alerted, ideally before people start their day looking at stale dashboards.

Late data is one of the most common data incidents and one of the easiest to detect, so freshness is usually the first monitor deployed. Two measures are worth separating: when the table was last written, and how recent the data inside it is. A job can rewrite a table on time with yesterday's data if its source is stuck. Expectations can be set by hand or learned from past update patterns, and lineage can carry a late source's effect to its downstream tables early.

# Key considerations

- Measure the age of the data itself, such as the latest event or business date, not only the last write time.
- Schedules vary by weekday, month end and public holidays. Static thresholds raise false alarms; calendars or learned patterns reduce them.
- Alert consumers as well as producers when a service level is at risk, so they do not act on stale data.
- For streaming data, monitor lag in seconds or minutes per partition rather than daily arrival.

# Questions to ask

- When must each dataset be current, and how late is too late?
- Do sources deliver on irregular schedules, such as business days or month end only?
- Who should be told when data is late: producers, consumers or both?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data quality and observability](data-quality.md) |
| Broader | [Data observability](data-observability.md) |
| Related | [Alerts and subscriptions](../analytics-bi/data-alerting.md), [Data service levels](../data-products/data-slas.md), [Data-aware orchestration](../orchestration/asset-based-orchestration.md), [Database replication and mirroring](../ingestion-integration/database-replication.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Impact analysis](../metadata/impact-analysis.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Streaming ingestion](../ingestion-integration/streaming-ingestion.md) |
| Needed by | [Data service levels](../data-products/data-slas.md), [Data trust indicators](../metadata/data-trust-indicators.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 2) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Patterns:** [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Data product owner](../../personas/persona-data-product-owner.md)
- **Maturity tracks:** [Data quality and observability](../../maturity/track-data-quality.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 5 – Timeliness · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Service-Level Agreement

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Glue Data Quality](../../technologies/aws/aws-glue-data-quality.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Quality](../../technologies/microsoft/purview-data-quality.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake alerts and notifications](../../technologies/snowflake/snowflake-alerts.md), [Snowflake data quality monitoring (data metric functions)](../../technologies/snowflake/snowflake-data-quality-monitoring.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks data quality monitoring anomaly detection](../../technologies/databricks/databricks-dqm-anomaly-detection.md) (preview), [Databricks SQL alerts](../../technologies/databricks/databricks-sql-alerts.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica data observability](../../technologies/informatica/informatica-data-observability.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data observability in IBM watsonx.data integration](../../technologies/ibm/ibm-data-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Health and data expectations](../../technologies/palantir/palantir-data-health.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Monte Carlo Data + AI Observability](../../technologies/independent/monte-carlo-data-observability.md) |
