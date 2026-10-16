---
type: Technology
id: cloudera-observability
title: Cloudera Observability
description: Monitoring and analysis service for Cloudera workloads that shows job and query performance, recommends fixes and reports resource use and cost by workload.
formerly: [Cloudera Workload XM, Workload XM, WXM]
platform: platform-cloudera
kind: saas
availability: ga
realises: [platform-observability, query-performance-analysis, cost-attribution, pipeline-monitoring]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Covers Spark, Hive, Impala and Data Engineering jobs across on-cloud and on-premises clusters; its FinOps views attribute cost to users and workloads.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform observability](../../capabilities/platform-operations/platform-observability.md) (Platform operations) (primary): Monitor jobs, queries, services and usage across the platform with logs, metrics and traces.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview), [Azure Monitor](../microsoft/azure-monitor.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Monitoring](../google-cloud/gcp-cloud-monitoring.md), [Google Cloud Logging](../google-cloud/gcp-cloud-logging.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trail (event tables, logging, tracing and metrics)](../snowflake/snowflake-trail.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse data source plugin for Grafana](../clickhouse/clickhouse-grafana-plugin.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Operational Insights](../informatica/informatica-operational-insights.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Platform observability](../../capabilities/platform-operations/platform-observability.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenTelemetry](../open-source/opentelemetry.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Platform observability](../../capabilities/platform-operations/platform-observability.md) |
