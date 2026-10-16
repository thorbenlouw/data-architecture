---
type: Technology
id: snowflake-resource-monitors
title: Snowflake resource monitors
description: Credit quotas on warehouses or the whole account that notify or suspend warehouses when thresholds are reached.
platform: platform-snowflake
kind: feature
availability: ga
realises: [spend-controls]
resource: https://docs.snowflake.com/en/user-guide/resource-monitors
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Resource monitors cover warehouse compute only. Use budgets for serverless and AI spend.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations) (primary): Set budgets, quotas and alerts, and stop runaway spend automatically.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Budgets](../aws/aws-budgets.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md), [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks budgets](../databricks/databricks-budgets.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md), [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
