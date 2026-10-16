---
type: Technology
id: fabric-workspace-monitoring
title: Fabric workspace monitoring
description: Collects logs and metrics from warehouses, pipelines, Eventhouses, semantic models and other items into a KQL database for querying and alerting.
platform: platform-microsoft
kind: feature
availability: preview
realises: [platform-observability, pipeline-monitoring, query-performance-analysis, system-telemetry]
resource: https://learn.microsoft.com/en-us/fabric/fundamentals/workspace-monitoring-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Uses capacity; 30-day default retention. The Monitoring hub gives a simpler run history across items.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations): Expose platform usage, billing and operational data as queryable tables.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trail (event tables, logging, tracing and metrics)](../snowflake/snowflake-trail.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md), [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Operational Insights](../informatica/informatica-operational-insights.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
