---
type: Technology
id: palantir-resource-management
title: Palantir Resource Management
description: Administration views of compute and storage usage by project and resource, with limits for controlling consumption.
platform: platform-palantir
kind: feature
availability: ga
realises: [cost-attribution, spend-controls, system-telemetry]
resource: https://www.palantir.com/docs/foundry/getting-started/application-reference/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Foundry is licensed on compute and storage usage, so this is the main FinOps tool; Control Panel holds wider administration.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations) (primary): Attribute spend to teams, products and workloads using tags and usage data.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.
- [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) (Platform operations): Expose platform usage, billing and operational data as queryable tables.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Data Exports](../aws/aws-data-exports.md), [AWS Cost Explorer](../aws/aws-cost-explorer.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Fabric Capacity Metrics app](../microsoft/fabric-capacity-metrics-app.md), [Microsoft Cost Management](../microsoft/azure-cost-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md), [BigQuery INFORMATION_SCHEMA views](../google-cloud/gcp-bigquery-information-schema.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../snowflake/snowflake-account-usage.md), [Snowflake budgets](../snowflake/snowflake-budgets.md), [Snowflake Cortex AI Gateway](../snowflake/snowflake-cortex-ai-gateway.md) (preview) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks serverless usage policies](../databricks/databricks-serverless-usage-policies.md) (preview), [Databricks budgets](../databricks/databricks-budgets.md), [Databricks system tables](../databricks/databricks-system-tables.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Usage and system telemetry](../../capabilities/platform-operations/system-telemetry.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md), [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Processing Unit (IPU) consumption pricing](../informatica/informatica-ipu-pricing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Observability](../cloudera/cloudera-observability.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Dagster+](../independent/dagster-plus.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) |
