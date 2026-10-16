---
type: Technology
id: clickhouse-clickstack
title: ClickStack
description: Observability stack that combines the HyperDX UI, a preconfigured OpenTelemetry collector and ClickHouse to store and search logs, traces, metrics and session replays, with dashboards and alerts.
aliases: [HyperDX]
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [observability-analytics, dashboards-reports, data-alerting, time-series-data]
resource: https://clickhouse.com/docs/use-cases/observability/clickstack/overview
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Launched in May 2025 after ClickHouse acquired HyperDX (MIT licence). Runs self-managed (Docker, Helm), as Managed ClickStack inside ClickHouse Cloud, or as ClickStack Cloud, a serverless option in private preview since June 2026. AI Notebooks are in beta and an open-source ClickStack MCP server exists. It targets application and infrastructure observability rather than data observability.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) (Specialised data types) (primary): Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Azure Monitor](../microsoft/azure-monitor.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md), [Time-series data](../../capabilities/specialised-data/time-series-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md), [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Observe by Snowflake](../snowflake/snowflake-observe.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenSearch](../open-source/opensearch.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Elastic Cloud](../independent/elastic-cloud.md) | [Observability data analytics](../../capabilities/specialised-data/observability-analytics.md) |
