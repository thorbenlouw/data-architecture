---
type: Technology
id: snowflake-query-profile
title: Snowflake Query History, Query Profile and query insights
description: Snowsight views of query history, operator-level execution plans and automatic insights, used to diagnose slow or expensive queries.
platform: platform-snowflake
kind: feature
availability: ga
realises: [query-performance-analysis]
resource: https://docs.snowflake.com/en/user-guide/ui-snowsight-activity
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations) (primary): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowsight

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon CloudWatch](../aws/aws-cloudwatch.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL](../databricks/databricks-sql.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Viewpoint](../teradata/teradata-viewpoint.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
