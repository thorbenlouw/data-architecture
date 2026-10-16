---
type: Capability
id: cost-optimisation
title: Cost optimisation
description: Find and act on savings such as idle compute, oversized clusters and unused data.
broader: [cost-management]
related: [storage-tiering, table-maintenance, query-performance-analysis, usage-metadata, reserved-capacity]
depends_on: [system-telemetry]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Most savings come from a familiar list: clusters or warehouses larger than their queries need, compute that stays on with nothing running, auto-suspend settings that are too long, scheduled jobs on expensive interactive compute, tables nobody has read for a year, many small files that slow queries, full refreshes that could be incremental, and old versions or backups kept beyond policy. Many platforms now generate these findings from usage data, with estimated savings, and some apply fixes such as right-sizing automatically.

Optimisation works best as a regular routine rather than a one-off campaign, because new workloads keep adding waste. Savings come in three kinds. Using less means deleting, scheduling less often and processing incrementally. Paying less per unit means right-sizing, cheaper storage tiers, committed-use discounts and interruptible instances. Doing the same work more efficiently means tuning queries, clustering and caching. Each needs different people: owners decide what to stop, platform engineers change configuration and developers tune code.

# Key considerations

- Check usage before deleting. Tables that look unused may serve quarterly or annual processes, so archive them or restrict access first.
- Right-sizing changes performance. Measure query times and service levels before and after.
- Route each automated recommendation to the team that owns the resource, or nobody acts on it.
- Track realised savings, not estimated ones, so the effort can be justified and repeated.

# Questions to ask

- Which workloads account for most of the spend, and when were they last reviewed?
- Is there a routine for removing unused tables, clusters and environments?
- Do you use committed-use or reserved pricing, and does actual usage match the commitment?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Cost management](cost-management.md) |
| Related | [Partitioning and clustering](../storage/partitioning-clustering.md), [Provisioned compute](../compute/provisioned-compute.md), [Query and job performance analysis](query-performance-analysis.md), [Reserved and committed capacity](../compute/reserved-capacity.md), [Spot and interruptible compute](../compute/interruptible-compute.md), [Storage tiering and lifecycle](../storage/storage-tiering.md), [Sustainability and carbon management](sustainability-reporting.md), [Table maintenance and optimisation](../storage/table-maintenance.md), [Usage and popularity metadata](../metadata/usage-metadata.md), [Usage and system telemetry](system-telemetry.md), [Vectorised native execution](../compute/native-execution-acceleration.md) |
| Depends on | [Usage and system telemetry](system-telemetry.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2)
- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [FinOps](../../maturity/track-finops.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3 storage classes and S3 Lifecycle](../../technologies/aws/aws-s3-storage-classes-lifecycle.md), [AWS Cost Explorer](../../technologies/aws/aws-cost-explorer.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Cost Management](../../technologies/microsoft/azure-cost-management.md), [OneLake storage tiers and lifecycle management](../../technologies/microsoft/fabric-onelake-storage-tiers.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Billing](../../technologies/google-cloud/gcp-cloud-billing.md), [Google Cloud Storage Autoclass](../../technologies/google-cloud/gcp-cloud-storage-autoclass.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks predictive optimization](../../technologies/databricks/databricks-predictive-optimization.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud usage breakdown and spend alerts](../../technologies/clickhouse/clickhouse-cost-controls.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Integration FinOps](../../technologies/informatica/informatica-cdi-finops.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Lakehouse Optimizer](../../technologies/cloudera/cloudera-lakehouse-optimizer.md) |
