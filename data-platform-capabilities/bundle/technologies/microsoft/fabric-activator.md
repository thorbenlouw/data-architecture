---
type: Technology
id: fabric-activator
title: Fabric Activator
description: A no-code rules engine that watches streams, reports and Fabric events per business object and triggers alerts, pipelines, functions or Power Automate flows.
formerly: [Data Activator]
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-alerting, event-driven-triggering]
resource: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports stateful conditions such as becomes, increases and absence of data. Publishing business events and rules over warehouse queries or ontology entities are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI) (primary): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Fabric Real-Time Intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Looker](../google-cloud/gcp-looker.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake alerts and notifications](../snowflake/snowflake-alerts.md), [Snowflake CoWork](../snowflake/snowflake-cowork.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL alerts](../databricks/databricks-sql-alerts.md), [Databricks AI/BI dashboards](../databricks/databricks-ai-bi-dashboards.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickStack](../clickhouse/clickhouse-clickstack.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Superset](../open-source/apache-superset.md), [Metabase](../open-source/metabase.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Tableau Pulse](../independent/tableau-pulse.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) |
