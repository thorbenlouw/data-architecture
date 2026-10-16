---
type: Capability
id: elastic-scaling
title: Elastic scaling
description: Add and remove compute automatically as load changes, including for bursts of concurrent users.
aliases: [autoscaling, concurrency scaling, auto-suspend]
broader: [compute]
related:
- workload-management
- spend-controls
- serverless-compute
- workload-isolation
- query-performance-analysis
depends_on: [decoupled-storage-compute]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Scaling up gives a cluster or warehouse bigger nodes for heavier queries. Scaling out adds nodes, or whole extra clusters behind the same endpoint, when many users arrive at once. At 09:00 on a Monday a dashboard warehouse might grow from one cluster to four as queries queue, then shrink back by mid-morning. Scaling in removes capacity as load falls. Serverless engines do all of this per query, with no visible cluster.

It lets capacity follow demand instead of being sized for the peak, which matters for BI concurrency spikes, month-end runs and event-driven pipelines. Policies set how eagerly to add capacity and how soon to remove it, trading queue time against cost. Scaling up helps one large query; scaling out helps many small ones. Scaling out across clusters works only where storage is separate from compute and the engine can route queries between clusters.

# Key considerations

- Set upper limits. Unlimited scaling turns a load spike or a runaway job into an unlimited bill.
- New capacity takes seconds to minutes to arrive. Pre-warm for known peaks instead of waiting for queues to build.
- New nodes start with empty caches, so the first queries they run are slower.
- Scaling does not fix inefficient queries. A badly written query spread over four clusters still costs four times as much.

# Questions to ask

- When do concurrency peaks happen, and how large are they?
- How long can users wait in a queue before capacity must grow?
- What maximum spend per hour or per day is acceptable during peaks?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Budgets and spend controls](../platform-operations/spend-controls.md), [Compute provisioning options](compute-options.md), [Distributed processing](../processing/distributed-processing.md), [Hyperparameter tuning](../machine-learning/hyperparameter-tuning.md), [Provisioned compute](provisioned-compute.md), [Query and job performance analysis](../platform-operations/query-performance-analysis.md), [Real-time inference](../mlops/real-time-inference.md), [Serverless compute](serverless-compute.md), [Workload isolation](workload-isolation.md), [Workload management](workload-management.md) |
| Depends on | [Decoupled storage and compute](decoupled-storage-compute.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (requires, level 3) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Data analyst](../../personas/persona-data-analyst.md) · [Data platform engineer](../../personas/persona-platform-engineer.md) · [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 5 – Timeliness; Principle 6 – Adaptability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Redshift concurrency scaling | [Amazon EMR Serverless](../../technologies/aws/aws-emr-serverless.md), [Amazon Redshift concurrency scaling](../../technologies/aws/aws-redshift-concurrency-scaling.md), [Amazon Redshift Serverless](../../technologies/aws/aws-redshift-serverless.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Data Warehouse](../../technologies/microsoft/fabric-data-warehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery editions](../../technologies/google-cloud/gcp-bigquery-editions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Adaptive Compute](../../technologies/snowflake/snowflake-adaptive-compute.md), [Snowflake multi-cluster warehouses](../../technologies/snowflake/snowflake-multi-cluster-warehouses.md), [Snowflake Query Acceleration Service](../../technologies/snowflake/snowflake-query-acceleration-service.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks serverless compute](../../technologies/databricks/databricks-serverless-compute.md), [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud](../../technologies/clickhouse/clickhouse-cloud.md), [ClickHouse Cloud Warehouses (compute-compute separation)](../../technologies/clickhouse/clickhouse-warehouses.md), [SharedMergeTree](../../technologies/clickhouse/clickhouse-sharedmergetree.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [IDMC serverless runtime environment](../../technologies/informatica/informatica-serverless-runtime-environment.md), [Informatica Cloud Data Integration advanced mode](../../technologies/informatica/informatica-cdi-advanced-mode.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Warehouse](../../technologies/cloudera/cloudera-data-warehouse.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md), [Oracle Autonomous AI Lakehouse](../../technologies/oracle/oracle-autonomous-ai-lakehouse.md) |
| [Teradata](../../platforms/platform-teradata.md) | Elastic compute | [Teradata Cloud](../../technologies/teradata/teradata-cloud.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [KServe](../../technologies/open-source/kserve.md) |
