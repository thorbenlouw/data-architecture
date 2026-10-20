---
type: Technology
id: snowflake-alerts
title: Snowflake alerts and notifications
description: Scheduled or event-driven conditions written in SQL that run an action, such as sending email, webhook or cloud-queue notifications, when data meets them.
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-alerting, freshness-monitoring]
resource: https://docs.snowflake.com/en/user-guide/alerts
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI) (primary): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) (Data quality and observability): Detect when data arrives later than expected or misses its freshness target.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Activator](../microsoft/fabric-activator.md), [Fabric operations agent](../microsoft/fabric-operations-agent.md), [Power BI reports and dashboards](../microsoft/powerbi-reports.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL alerts](../databricks/databricks-sql-alerts.md), [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Freshness monitoring](../../capabilities/data-quality/freshness-monitoring.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Pulse](../independent/tableau-pulse.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
