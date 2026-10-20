---
type: Capability
id: workload-management
title: Workload management
description: Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
aliases: [resource groups, query queues]
broader: [compute]
related: [workload-isolation, elastic-scaling, query-performance-analysis, spend-controls, data-slas]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Workload management controls how a shared engine spends its capacity. Queries are classified by user, role, application or tag into queues or resource groups. Each group gets a share of CPU and memory, a priority, a concurrency limit and rules such as a maximum run time. A finance dashboard group might get high priority and a guaranteed share, while ad hoc exploration runs at lower priority and any query that scans more than a set amount, or runs past 30 minutes, is cancelled. Some engines also size memory per query and admit queries only when resources are free.

It makes a shared engine predictable when not every kind of work can have its own compute, and it limits the damage from runaway queries. It differs from workload isolation, which puts work on different compute; workload management arbitrates within the same compute. Most estates use both: isolation between the main workload types, and management within each one.

# Key considerations

- Keep classification rules simple and owned. Complex rule sets drift, and nobody can explain why a query waited.
- Tell users about timeouts and cancellation rules, with guidance on rewriting or rescheduling long queries.
- Priority alone does not help when long-running queries hold all the capacity. Combine it with concurrency limits or pre-emption.
- Review queue times and cancellations regularly. They show where capacity, isolation or query design need to change.

# Questions to ask

- Which queries must finish within a set time, and which can wait?
- Are there runaway queries today, and how are they handled?
- Do different user groups share the same compute, and does that cause disputes?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Budgets and spend controls](../platform-operations/spend-controls.md), [Cost management](../platform-operations/cost-management.md), [Data service levels](../data-products/data-slas.md), [Elastic scaling](elastic-scaling.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Workload isolation](workload-isolation.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 5 – Timeliness

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift](../../technologies/aws/aws-redshift.md), [Amazon Redshift concurrency scaling](../../technologies/aws/aws-redshift-concurrency-scaling.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery workload management (formerly capacity management) | [BigQuery workload management](../../technologies/google-cloud/gcp-bigquery-workload-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Adaptive Compute](../../technologies/snowflake/snowflake-adaptive-compute.md), [Snowflake multi-cluster warehouses](../../technologies/snowflake/snowflake-multi-cluster-warehouses.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Workload scheduling, settings profiles and quotas | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../../technologies/clickhouse/clickhouse-access-control.md), [ClickHouse workload scheduling](../../technologies/clickhouse/clickhouse-workload-scheduling.md) |
| [Teradata](../../platforms/platform-teradata.md) | TASM / workload management | [Teradata Database](../../technologies/teradata/teradata-database.md), [Teradata Viewpoint](../../technologies/teradata/teradata-viewpoint.md) |
| [SAS](../../platforms/platform-sas.md) | SAS Workload Orchestrator | [SAS Workload Management](../../technologies/sas/sas-workload-management.md) |
