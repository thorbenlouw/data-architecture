---
type: Technology
id: aws-cost-explorer
title: AWS Cost Explorer
description: Interactive tool for analysing spend and usage by service, account and cost allocation tag, with forecasts and rightsizing recommendations.
platform: platform-aws
kind: feature
availability: ga
realises: [cost-management, cost-attribution, cost-optimisation, cost-forecasting]
resource: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cost categories and cost allocation tags drive showback; Cost Optimization Hub consolidates savings recommendations across accounts.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost management](../../capabilities/platform-operations/cost-management.md) (Platform operations) (primary): Understand, allocate and control what the platform costs.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations): Find and act on savings such as idle compute, oversized clusters and unused data.
- [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) (Platform operations): Project future platform spend from usage trends, commitments and planned workloads, and flag spend that departs from its expected pattern.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Cost Management](../microsoft/azure-cost-management.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md), [Spend forecasting and anomaly detection](../../capabilities/platform-operations/cost-forecasting.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [Cost management](../../capabilities/platform-operations/cost-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md), [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
