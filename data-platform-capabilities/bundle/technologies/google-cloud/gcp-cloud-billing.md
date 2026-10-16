---
type: Technology
id: gcp-cloud-billing
title: Google Cloud Billing
description: Billing accounts, budgets and alerts, detailed billing export to BigQuery and FinOps reports for attributing and controlling Google Cloud spend.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [cost-attribution, spend-controls, cost-optimisation, cost-forecasting]
resource: https://docs.cloud.google.com/billing/docs/concepts
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Labels and tags on resources and BigQuery jobs drive attribution; budgets alert but do not stop spend unless wired to automation. Recommender and FinOps hub highlight idle and oversized resources.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.
- [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) (Platform operations): Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cost Explorer](../aws/aws-cost-explorer.md), [AWS Data Exports](../aws/aws-data-exports.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview), [Databricks budgets](../databricks/databricks-budgets.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Processing Unit (IPU) consumption pricing](../informatica/informatica-ipu-pricing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
