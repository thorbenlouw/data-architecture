---
type: Technology
id: fabric-capacity-metrics-app
title: Microsoft Fabric Capacity Metrics app
description: A Power BI app that reports capacity unit consumption by workspace, item and operation, including throttling and storage.
platform: platform-microsoft
kind: feature
availability: ga
realises: [system-telemetry, cost-attribution]
resource: https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The usual basis for chargeback, though its semantic model is not supported for other uses. A redesigned preview report exists. No alerting; use capacity events in Real-Time hub instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations) (primary): Expose platform usage, billing and operational data as queryable tables.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [Amazon S3 Metadata](../aws/aws-s3-metadata.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md), [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
