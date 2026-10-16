---
type: Capability
id: query-performance-analysis
title: Query and job performance analysis
description: Inspect query plans, job stages, run history and bottlenecks to tune performance and cost.
aliases: [query profile, job profiling, Spark UI]
broader: [platform-observability]
related:
- query-acceleration
- partitioning-clustering
- workload-management
- cost-optimisation
- table-maintenance
depends_on: [sql-query-engine]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A query profile breaks execution into operators, such as scans, joins, aggregations and data exchange between nodes, with the rows, bytes and time for each. Distributed jobs add a stage view: how long each stage and task took, how much data was shuffled, and whether one task ran far longer than the rest because its key held most of the data. From these an engineer can see that a join grew one million rows into two billion, that a filter did not prune partitions, or that a job spilled to disk. Run history shows which queries and jobs cost most or have slowed over time, by user, warehouse, pipeline and dashboard.

A few queries and jobs usually account for most of the compute bill, so this is where tuning pays. Engines increasingly add advice, such as recommended clustering keys or materialised views. Workload management controls when and where work runs; this capability explains why individual queries and jobs are slow or expensive.

# Key considerations

- Keep query history long enough to compare before and after a change and to spot gradual slowdowns.
- Tag queries with the application, dashboard or pipeline that issued them, so slow queries can be traced to an owner.
- Separate queue time from execution time. Queries waiting for capacity need workload changes, not tuning.
- Query text can contain sensitive literal values. Restrict who can read history across all users.

# Questions to ask

- Which queries or dashboards do users complain about, and how slow are they?
- Who in the team can read query plans and act on them today?
- How much compute spend comes from the 20 most expensive queries?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform observability](platform-observability.md) |
| Related | [Query and compute](../compute/compute.md), [Cost optimisation](cost-optimisation.md), [Elastic scaling](../compute/elastic-scaling.md), [Indexes and data skipping](../compute/data-skipping-indexes.md), [Partitioning and clustering](../storage/partitioning-clustering.md), [Query acceleration](../compute/query-acceleration.md), [SQL query engine](../compute/sql-query-engine.md), [Table maintenance and optimisation](../storage/table-maintenance.md), [Usage and system telemetry](system-telemetry.md), [Workload management](../compute/workload-management.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data engineer](../../personas/persona-data-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon CloudWatch](../../technologies/aws/aws-cloudwatch.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric workspace monitoring](../../technologies/microsoft/fabric-workspace-monitoring.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery INFORMATION_SCHEMA views](../../technologies/google-cloud/gcp-bigquery-information-schema.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake ACCOUNT_USAGE and ORGANIZATION_USAGE](../../technologies/snowflake/snowflake-account-usage.md), [Snowflake Query History, Query Profile and query insights](../../technologies/snowflake/snowflake-query-profile.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks SQL](../../technologies/databricks/databricks-sql.md), [Databricks system tables](../../technologies/databricks/databricks-system-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | Query Insights, system.query_log | [ClickHouse Query Insights and system tables](../../technologies/clickhouse/clickhouse-cloud-monitoring.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Observability](../../technologies/cloudera/cloudera-observability.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Viewpoint](../../technologies/teradata/teradata-viewpoint.md) |
