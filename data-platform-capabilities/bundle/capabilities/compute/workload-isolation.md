---
type: Capability
id: workload-isolation
title: Workload isolation
description: Run different workloads on separate compute so one cannot slow or starve another.
aliases: [compute isolation, multi-cluster]
broader: [compute]
related: [workload-management, multi-tenancy, cost-attribution, compute-user-isolation, provisioned-compute]
depends_on: [decoupled-storage-compute]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The common form is one warehouse or cluster per workload type: one for BI dashboards, one for nightly transformation, one for data science, each with its own size and budget. Other forms include separate serverless pools, resource groups inside one engine with fixed shares of CPU and memory, and fully separate accounts for regulated or external tenants. Because the data sits in shared storage, isolating compute does not mean copying data.

It protects service levels for important consumers and makes cost attribution simple, since each compute unit maps to an owner. The trade-off is utilisation: separated capacity cannot be lent to a neighbour while idle unless the platform allows bursting. This is isolation of performance. Stopping one user's code from reaching another's data on shared machines is a security matter, covered by shared compute isolation.

# Key considerations

- Group workloads by service level and access pattern, not only by team. Too many small clusters waste money and are hard to manage.
- Isolated compute still shares storage, catalogue and network. Check whether metadata services or storage throttling can still cause contention.
- Name, tag and apply policies to each compute unit when it is created, so chargeback and governance work from the start.
- Decide what happens when a pool is full: queue, scale out, or borrow from other pools.

# Questions to ask

- Which workloads have suffered from contention, and when?
- Which consumers have service levels that must hold whatever else is running?
- How is compute cost charged to teams today?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Backfill and reprocessing](../orchestration/backfill-replay.md), [Compute provisioning options](compute-options.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Decoupled storage and compute](decoupled-storage-compute.md), [Elastic scaling](elastic-scaling.md), [In-database machine learning](../machine-learning/in-database-ml.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Operational database integration](../serving/operational-database.md), [Provisioned compute](provisioned-compute.md), [Serverless compute](serverless-compute.md), [Shared compute isolation](../security/compute-user-isolation.md), [Workload management](workload-management.md) |
| Depends on | [Decoupled storage and compute](decoupled-storage-compute.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 2)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Data warehouse](../../patterns/data-warehouse.md)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift multi-warehouse (data sharing); Athena workgroups and Capacity Reservations | [Amazon Redshift data sharing](../../technologies/aws/aws-redshift-data-sharing.md), [Amazon Redshift Serverless](../../technologies/aws/aws-redshift-serverless.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Fabric capacities (F SKUs)](../../technologies/microsoft/fabric-capacities.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | reservation assignments | [BigQuery workload management](../../technologies/google-cloud/gcp-bigquery-workload-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake virtual warehouses](../../technologies/snowflake/snowflake-virtual-warehouses.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakeguard (user-code isolation) and separate warehouses | [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Warehouses (compute-compute separation) | [ClickHouse Cloud Warehouses (compute-compute separation)](../../technologies/clickhouse/clickhouse-warehouses.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Virtual Warehouses | [Cloudera Data Services on premises](../../technologies/cloudera/cloudera-data-services-on-premises.md), [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Cloud](../../technologies/teradata/teradata-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Kyuubi](../../technologies/open-source/apache-kyuubi.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [MotherDuck](../../technologies/independent/motherduck.md) |
