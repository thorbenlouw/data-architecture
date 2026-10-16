---
type: Technology
id: aws-data-exports
title: AWS Data Exports
description: Delivers billing, cost optimisation and carbon emissions data to S3 on a schedule as CUR 2.0 or FOCUS tables, with SQL column selection.
aliases: [CUR 2.0, AWS Cost and Usage Report 2.0]
platform: platform-aws
kind: feature
availability: ga
realises: [system-telemetry, cost-attribution, sustainability-reporting]
resource: https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

CUR 2.0 is the recommended replacement for the legacy Cost and Usage Report, which still exists; the AWS Usage Report is closed to new customers. FOCUS 1.2 eases multi-cloud FinOps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations) (primary): Expose platform usage, billing and operational data as queryable tables.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Sustainability and carbon management](../../capabilities/platform-operations/sustainability-reporting.md) (Platform operations): Measure and reduce the carbon emissions and energy use of data workloads.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Azure Monitor](../microsoft/azure-monitor.md), [Fabric workspace monitoring](../microsoft/fabric-workspace-monitoring.md) (preview) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Query Insights and system tables](../clickhouse/clickhouse-cloud-monitoring.md) | [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
