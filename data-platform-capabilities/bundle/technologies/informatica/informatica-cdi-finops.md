---
type: Technology
id: informatica-cdi-finops
title: Informatica Cloud Data Integration FinOps
description: Shows the cost and resource use of each workload and pipeline, and recommends or applies tuning to lower IPU and cloud compute spend.
platform: platform-informatica
kind: feature
availability: ga
realises: [cost-optimisation]
resource: https://docs.informatica.com/integration-cloud/data-integration/current-version.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This sits beside IPU metering: FinOps covers optimising pipelines, while IPU dashboards cover attributing consumption.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) (Platform operations) (primary): Find and act on savings such as idle compute, oversized clusters and unused data.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 storage classes and S3 Lifecycle](../aws/aws-s3-storage-classes-lifecycle.md), [AWS Cost Explorer](../aws/aws-cost-explorer.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake storage tiers and lifecycle management](../microsoft/fabric-onelake-storage-tiers.md) (preview), [Microsoft Cost Management](../microsoft/azure-cost-management.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Storage Autoclass](../google-cloud/gcp-cloud-storage-autoclass.md), [Google Cloud Billing](../google-cloud/gcp-cloud-billing.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks predictive optimization](../databricks/databricks-predictive-optimization.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud usage breakdown and spend alerts](../clickhouse/clickhouse-cost-controls.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Lakehouse Optimizer](../cloudera/cloudera-lakehouse-optimizer.md) | [Cost optimisation](../../capabilities/platform-operations/cost-optimisation.md) |
