---
type: Technology
id: snowflake-cost-anomaly-detection
title: Snowflake cost anomaly detection
description: Flags days when account or organisation consumption falls outside the expected range, with optional anomaly monitors scoped by tags or service types.
platform: platform-snowflake
kind: feature
availability: ga
realises: [spend-controls, cost-forecasting]
resource: https://docs.snowflake.com/en/user-guide/cost-anomalies
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Anomaly monitors scoped by tags or service types are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations) (primary): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) (Platform operations): Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Budgets](../aws/aws-budgets.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks budgets](../databricks/databricks-budgets.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md), [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
