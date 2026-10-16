---
type: Technology
id: databricks-budgets
title: Databricks budgets
description: Account-level spend tracking at list price, filtered by workspace, resource type and tags. You set monthly thresholds with email alerts and, for Unity Gateway, optional per-user blocking.
platform: platform-databricks
kind: feature
availability: ga
realises: [spend-controls, cost-attribution, ai-spend-controls]
resource: https://docs.databricks.com/aws/en/admin/account-settings/budgets
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA in July 2026. Budgets are mainly alerts, not hard caps, and Unity Gateway blocking works only approximately. Genie has its own budget controls. A prebuilt usage dashboard (GA March 2026) over billing system tables shows spend by product, workspace, tag and user.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations) (primary): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md) (Platform operations): Limit, prioritise and attribute model and agent consumption per user, team or application.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Budgets](../aws/aws-budgets.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric capacities (F SKUs)](../microsoft/fabric-capacities.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery workload management](../google-cloud/gcp-bigquery-workload-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake resource monitors](../snowflake/snowflake-resource-monitors.md), [Snowflake cost anomaly detection](../snowflake/snowflake-cost-anomaly-detection.md) | [AI usage and spend controls](../../capabilities/platform-operations/ai-spend-controls.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md), [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
