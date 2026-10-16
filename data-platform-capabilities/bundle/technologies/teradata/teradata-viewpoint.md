---
type: Technology
id: teradata-viewpoint
title: Teradata Viewpoint
description: Web console for monitoring Teradata systems, queries, sessions and workloads and for managing workload rules.
platform: platform-teradata
kind: software
availability: ga
realises: [platform-observability, query-performance-analysis, workload-management]
resource: https://www.teradata.com/platform
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Standard operations tool for Teradata estates; the database also exposes DBQL query logs and ResUsage tables for telemetry analysis.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview), [Azure Monitor](../microsoft/azure-monitor.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trail (event tables, logging, tracing and metrics)](../snowflake/snowflake-trail.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Operational Insights](../informatica/informatica-operational-insights.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
