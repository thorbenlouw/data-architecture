---
type: Technology
id: clickhouse-cloud-monitoring
title: ClickHouse Query Insights and system tables
description: Console views of query volume, latency and errors built on system.query_log, alongside system tables, Cloud monitoring dashboards and Prometheus endpoints that expose server, query and ClickPipes metrics.
aliases: [system.query_log]
platform: platform-clickhouse
kind: feature
availability: ga
realises: [query-performance-analysis, system-telemetry, audit-logging]
resource: https://clickhouse.com/docs/cloud/get-started/query-insights
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

system.query_log and related tables record each query with user, timings and resources, which serves both tuning and basic audit. The organisation-level Prometheus endpoint is deprecated in favour of per-service and discovery endpoints.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations) (primary): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations): Expose platform usage, billing and operational data as queryable tables.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Query History, Query Profile and query insights](../snowflake/snowflake-query-profile.md), [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md), [Databricks SQL](../databricks/databricks-sql.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
