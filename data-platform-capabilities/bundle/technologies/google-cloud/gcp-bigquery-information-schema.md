---
type: Technology
id: gcp-bigquery-information-schema
title: BigQuery INFORMATION_SCHEMA views
description: System views exposing jobs, slot usage, reservations, storage, table metadata and replication state as queryable tables.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [system-telemetry, query-performance-analysis, cost-attribution]
resource: https://docs.cloud.google.com/bigquery/docs/information-schema-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Combined with the query execution graph and administrative resource charts, these are the main sources for chargeback and tuning. Jobs views carry labels used for cost attribution.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations) (primary): Expose platform usage, billing and operational data as queryable tables.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview), [Azure Monitor](../microsoft/azure-monitor.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
