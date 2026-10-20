---
type: Capability
id: data-alerting
title: Alerts and subscriptions
description: Notify people when data crosses thresholds, or deliver reports to them on a schedule.
aliases: [data alerts, threshold alerts, report subscriptions, early warning alerts]
broader: [analytics-bi]
related: [freshness-monitoring, augmented-analytics, event-driven-triggering, paginated-reports, reverse-etl]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Alerts and subscriptions push data to people instead of waiting for them to look. An alert is a condition on a query or metric, such as daily refunds above 2% of sales or stock below reorder level, evaluated on a schedule or when data refreshes. When it is met, the tool sends an email, chat message, mobile notification or webhook. A subscription delivers a dashboard or report snapshot to a list of recipients at a fixed time, such as every Monday at 07:00.

It matters for operational decisions that cannot wait for someone to open a dashboard, and for people who prefer reports in their inbox. Choices include fixed thresholds or learned baselines, evaluation on a schedule or on data change, and delivery to people or to systems that act automatically. Business alerts are distinct from pipeline and data quality alerts, which tell data owners about broken data rather than telling business users about business events.

# Key considerations

- Evaluate alerts after the data they depend on has refreshed, or they fire on stale or partial data.
- Alerts that fire too often get muted. Support owners, snoozing and thresholds that do not flap around a boundary.
- Snapshots emailed to many recipients may carry data some of them should not see. Render per recipient with their permissions, or restrict the audience.
- Webhook delivery turns alerts into automation. Treat those endpoints as integrations, with retries and monitoring.

# Questions to ask

- Which business events need someone to act within minutes or hours?
- Who receives scheduled reports today, and through which channels?
- Should an alert notify a person, or start a process?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Related | [Augmented analytics](augmented-analytics.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Paginated reports](paginated-reports.md), [Reverse ETL](../serving/reverse-etl.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 11 – Distribution

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Activator | [Fabric Activator](../../technologies/microsoft/fabric-activator.md), [Fabric operations agent](../../technologies/microsoft/fabric-operations-agent.md), [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Looker](../../technologies/google-cloud/gcp-looker.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake alerts and notifications](../../technologies/snowflake/snowflake-alerts.md), [Snowflake CoWork](../../technologies/snowflake/snowflake-cowork.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI/BI dashboards](../../technologies/databricks/databricks-ai-bi-dashboards.md), [Databricks SQL alerts](../../technologies/databricks/databricks-sql-alerts.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickStack](../../technologies/clickhouse/clickhouse-clickstack.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Automate](../../technologies/palantir/palantir-automate.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku scenarios](../../technologies/dataiku/dataiku-scenarios.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Superset](../../technologies/open-source/apache-superset.md), [Metabase](../../technologies/open-source/metabase.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Tableau Pulse](../../technologies/independent/tableau-pulse.md) |
