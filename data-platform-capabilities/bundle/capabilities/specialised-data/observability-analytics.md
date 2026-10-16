---
type: Capability
id: observability-analytics
title: Observability data analytics
description: Store and analyse logs, metrics and traces from applications and infrastructure at scale, with search, dashboards and alerts.
aliases: [OpenTelemetry analytics, log analytics]
broader: [specialised-data]
related: [platform-observability, time-series-data, full-text-search, storage-tiering, data-threat-detection]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Applications and infrastructure emit three kinds of telemetry. Logs are timestamped text or structured events; metrics are numeric time series such as request counts or processor load; traces follow one request across services as a tree of timed steps called spans. OpenTelemetry offers a common way to collect all three. An observability store indexes or compresses them for fast search by time, service and field, runs dashboards and alert rules, and can link a latency spike in a metric to the traces and log lines behind it.

Engineering, operations and security teams use it to detect and diagnose incidents and understand system behaviour. Volumes are very large, most data is never read, and value sits mainly in the latest hours, so sampling, tiering and retention dominate the design. Dedicated observability tools provide ready-made workflows; analytical platforms with fast search and columnar storage can keep data longer and join it with business data such as customer impact. Platform observability is narrower: it monitors the data platform itself.

# Key considerations

- Filter, sample and aggregate at collection time. Keeping everything at full detail is expensive.
- Use tiered retention, with recent data fast to query and older data in cheap storage queried on demand.
- Logs often contain personal data and secrets. Scrub them before storage.
- Metric labels with many distinct values, such as user or request IDs, drive up cost and slow queries in many systems.

# Questions to ask

- How much telemetry arrives per day, and how long must each type be kept?
- Who needs it: operations, security, product teams or auditors?
- Must telemetry be joined with business or customer data?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Related | [Approximate query processing](../compute/approximate-query-processing.md), [Data threat detection](../security/data-threat-detection.md), [Full-text search](full-text-search.md), [Platform observability](../platform-operations/platform-observability.md), [Real-time analytical database](../compute/real-time-analytics.md), [Storage tiering and lifecycle](../storage/storage-tiering.md), [Time-series data](time-series-data.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon CloudWatch](../../technologies/aws/aws-cloudwatch.md), [Amazon OpenSearch Service](../../technologies/aws/aws-opensearch-service.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Explorer](../../technologies/microsoft/azure-data-explorer.md), [Azure Monitor](../../technologies/microsoft/azure-monitor.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Logging](../../technologies/google-cloud/gcp-cloud-logging.md), [Google Cloud Monitoring](../../technologies/google-cloud/gcp-cloud-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Observe by Snowflake](../../technologies/snowflake/snowflake-observe.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse TimeSeries table engine](../../technologies/clickhouse/clickhouse-timeseries.md) (preview), [ClickStack](../../technologies/clickhouse/clickhouse-clickstack.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenSearch](../../technologies/open-source/opensearch.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Elastic Cloud](../../technologies/independent/elastic-cloud.md) |
