---
type: Technology
id: snowflake-account-usage
title: Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE
description: Shared SNOWFLAKE database schemas that expose query, login, metering, storage, access, task, AI and billing history as views, for one account or the whole organisation.
aliases: [ACCOUNT_USAGE, ORGANIZATION_USAGE]
platform: platform-snowflake
kind: feature
availability: ga
realises: [system-telemetry, cost-attribution, usage-metadata, query-performance-analysis]
resource: https://docs.snowflake.com/en/sql-reference/account-usage
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Views have latency of up to a few hours and keep one year of history. A FOCUS-format cost view is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations) (primary): Expose platform usage, billing and operational data as queryable tables.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Usage and popularity metadata](../../capabilities/metadata/usage-metadata.md) (Metadata and discovery): Show who uses which data, how often and how, to guide discovery and clean-up.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview), [Azure Monitor](../microsoft/azure-monitor.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
