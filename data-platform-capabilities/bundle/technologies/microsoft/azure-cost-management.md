---
type: Technology
id: azure-cost-management
title: Microsoft Cost Management
description: Analyses Azure spend by subscription, resource and tag, with budgets, alerts, exports and Advisor savings recommendations.
formerly: [Azure Cost Management]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [cost-attribution, spend-controls, cost-optimisation, cost-forecasting]
resource: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sees a Fabric capacity as one Azure resource; per-workspace attribution needs the Capacity Metrics app.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.
- [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) (Platform operations): Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cost Explorer](../aws/aws-cost-explorer.md), [AWS Data Exports](../aws/aws-data-exports.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview), [Databricks budgets](../databricks/databricks-budgets.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Processing Unit (IPU) consumption pricing](../informatica/informatica-ipu-pricing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
