---
type: Technology
id: databricks-serverless-usage-policies
title: Databricks serverless usage policies
description: Sets of tags applied automatically to the serverless usage of the users assigned to a policy, so that spend from notebooks, jobs, pipelines, serving, apps and Lakebase can be attributed.
formerly: [Serverless budget policies]
platform: platform-databricks
kind: feature
availability: preview
realises: [cost-attribution]
resource: https://docs.databricks.com/aws/en/admin/usage/budget-policies
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Public Preview. The tags appear in system.billing.usage. Admins create policies in workspace settings, and they feed budgets and chargeback reports.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [AWS Cost Explorer](../aws/aws-cost-explorer.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Microsoft Cost Management](../microsoft/azure-cost-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Processing Unit (IPU) consumption pricing](../informatica/informatica-ipu-pricing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Resource Management](../palantir/palantir-resource-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
