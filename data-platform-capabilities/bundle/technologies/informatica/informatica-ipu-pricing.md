---
type: Technology
id: informatica-ipu-pricing
title: Informatica Processing Unit (IPU) consumption pricing
description: Single consumption currency for IDMC services, with usage metered and reported by service, runtime, sub-organisation and sandbox, so spend can be tracked and charged back.
aliases: [IPU, Informatica Processing Units]
platform: platform-informatica
kind: feature
availability: ga
realises: [cost-attribution, reserved-capacity]
resource: https://www.informatica.com/blogs/announcing-volume-tier-pricing-and-flex-ipu-consumption-based-pricing-for-informatica-intelligent-data-management-cloud.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

There are two options: Standard IPU (allowance expires monthly) and Flex IPU (allowance expires each contract year). Volume tier pricing lowers the unit price as commitments grow. IPUs can be bought through the AWS, Azure and Google Cloud marketplaces, and an IPU Management MCP server was added in 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.
- [Reserved and committed capacity](../../capabilities/compute/reserved-capacity.md) (Query and compute): Reserve compute, query, training or inference capacity in advance for guaranteed availability and lower unit cost.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [AWS Cost Explorer](../aws/aws-cost-explorer.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md), [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview), [Databricks budgets](../databricks/databricks-budgets.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
