---
type: Capability
id: serverless-compute
title: Serverless compute
description: Run workloads without managing servers, with capacity allocated on demand and billed by use.
broader: [compute-options]
related: [elastic-scaling, spend-controls, cost-attribution, event-driven-triggering, workload-isolation]
depends_on: [decoupled-storage-compute]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The provider keeps a pool of ready capacity and assigns it to each query, job or function as it arrives, then takes it back. You do not choose instance types or cluster sizes, though you may set limits or a performance level. Billing follows consumption, measured as data scanned, compute-seconds or abstract capacity units. A query run at 03:00 against a dataset nobody else uses starts within seconds and costs only what it consumes, with nothing left running afterwards.

It suits intermittent and unpredictable work, small teams without platform engineers, and event-driven jobs. It moves the risk: there is no idle cost, but cost now follows behaviour, so an inefficient query or a runaway loop is billed in full. It also hides tuning settings, which helps until a workload needs them. The label covers a wide range, from per-query engines priced by bytes scanned to serverless warehouses, serverless Spark and functions, each with different limits on run time, memory and networking.

# Key considerations

- Set limits per user, per query and per project before broad rollout. Pay-per-use without limits makes one bad query expensive.
- Know how use is measured. Pricing by bytes scanned rewards partitioning and columnar formats; pricing by compute time rewards efficient code.
- Cold-start delay, concurrency quotas and maximum run times vary. Test them against the workload.
- Confirm that serverless compute runs inside your network and security boundary, with private connectivity and the same governance as provisioned compute.

# Questions to ask

- How much of the time would a provisioned cluster sit idle for this workload?
- Is anyone available to size and tune clusters, or should the provider do it?
- How will consumption be capped and attributed to teams?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Compute provisioning options](compute-options.md) |
| Related | [Agent hosting and runtime](../generative-ai/agent-runtime.md), [Budgets and spend controls](../platform-operations/spend-controls.md), [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Cost management](../platform-operations/cost-management.md), [Elastic scaling](elastic-scaling.md), [Event-driven triggering](../orchestration/event-driven-triggering.md), [Workload isolation](workload-isolation.md) |
| Depends on | [Decoupled storage and compute](decoupled-storage-compute.md) |

# Where it appears

- **Personas:** [FinOps practitioner](../../personas/persona-finops-practitioner.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena](../../technologies/aws/aws-athena.md), [Amazon Athena for Apache Spark](../../technologies/aws/aws-athena-spark.md), [Amazon EMR Serverless](../../technologies/aws/aws-emr-serverless.md), [Amazon MWAA Serverless](../../technologies/aws/aws-mwaa-serverless.md), [Amazon Redshift Serverless](../../technologies/aws/aws-redshift-serverless.md), [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery on-demand pricing | [BigQuery](../../technologies/google-cloud/gcp-bigquery.md), [Cloud Run](../../technologies/google-cloud/gcp-cloud-run.md), [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | serverless features (Snowpipe, serverless tasks, Automatic Clustering) and Adaptive Compute | [Snowflake Adaptive Compute](../../technologies/snowflake/snowflake-adaptive-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Free Edition](../../technologies/databricks/databricks-free-edition.md), [Databricks serverless compute](../../technologies/databricks/databricks-serverless-compute.md), [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud](../../technologies/clickhouse/clickhouse-cloud.md) |
| [Informatica](../../platforms/platform-informatica.md) | serverless runtime environment | [IDMC serverless runtime environment](../../technologies/informatica/informatica-serverless-runtime-environment.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Flow](../../technologies/oracle/oracle-oci-data-flow.md), [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Cloud](../../technologies/teradata/teradata-cloud.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud for Apache Flink](../../technologies/ibm/confluent-cloud-flink.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Lake Compute](../../technologies/independent/dbt-lake-compute.md) (preview), [Elastic Cloud](../../technologies/independent/elastic-cloud.md), [MotherDuck](../../technologies/independent/motherduck.md), [Prefect Cloud](../../technologies/independent/prefect-cloud.md) |
