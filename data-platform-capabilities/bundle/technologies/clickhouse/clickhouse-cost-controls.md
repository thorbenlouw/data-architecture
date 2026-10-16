---
type: Technology
id: clickhouse-cost-controls
title: ClickHouse Cloud usage breakdown and spend alerts
description: Console usage breakdown by service and cost category, a usage cost API, and organisation spend alerts at set thresholds of committed or budgeted spend.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [cost-attribution, spend-controls, cost-optimisation]
resource: https://clickhouse.com/docs/resources/changelogs/cloud/2026
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Spend alerts became GA in May 2026. Compute cost is mainly controlled through idling, autoscaling limits and read-only secondary services in warehouses.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cost Explorer](../aws/aws-cost-explorer.md), [AWS Data Exports](../aws/aws-data-exports.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview), [Databricks budgets](../databricks/databricks-budgets.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Processing Unit (IPU) consumption pricing](../informatica/informatica-ipu-pricing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
