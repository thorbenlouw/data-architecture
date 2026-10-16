---
type: Technology
id: databricks-system-tables
title: Databricks system tables
description: Databricks-hosted tables in the system catalog that cover billing, audit, lineage, compute, query history, jobs, pipelines, serving, MLflow, classification, data quality and Lakebase activity.
platform: platform-databricks
kind: feature
availability: ga
realises: [system-telemetry, audit-logging, cost-attribution, query-performance-analysis]
resource: https://docs.databricks.com/aws/en/admin/system-tables/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Most tables keep data for 365 days, and configurable retention is in Beta. system.query.history became GA in September 2026. The older system.lineage and system.operational_data schemas are deprecated.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations) (primary): Expose platform usage, billing and operational data as queryable tables.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) (Platform operations): Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview), [Azure Monitor](../microsoft/azure-monitor.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Query and job performance analysis](../../capabilities/platform-operations/query-performance-analysis.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
