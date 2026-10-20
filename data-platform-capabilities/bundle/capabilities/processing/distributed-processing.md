---
type: Capability
id: distributed-processing
title: Distributed processing
description: Process large datasets in parallel across a cluster of machines.
aliases: [big data processing, cluster processing, Spark]
broader: [processing]
related:
- single-node-processing
- partitioning-clustering
- native-execution-acceleration
- elastic-scaling
- table-maintenance
depends_on: [compute-options]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The engine splits a dataset into partitions and processes them in parallel on many machines. A coordinator plans the job as stages; workers read their partitions, apply the transformations and exchange data over the network, a step called a shuffle, whenever a join or aggregation needs all rows with the same key on one worker. Apache Spark is the best-known general engine of this kind, and massively parallel SQL engines use the same idea. A job that would take ten hours on one machine can finish in minutes on fifty.

It is needed when data volume, memory or run time exceed what one machine can offer: multi-terabyte joins, large backfills, feature pipelines over years of events. The costs are coordination overhead, network traffic during shuffles, skew where one key holds most of the data, and harder debugging. Lost work is recovered by recomputing or retrying failed partitions. Many workloads now fit on one large machine, so reserve clusters for the jobs that need them.

# Key considerations

- Skewed keys are the most common cause of slow jobs. Prefer engines with adaptive execution that split oversized partitions.
- Shuffles dominate cost. Partition and cluster tables on common join keys to reduce them.
- Cluster start-up time matters for short jobs. Serverless or pre-warmed pools reduce it.
- Thousands of small output files slow every reader. Size output files deliberately or rely on table maintenance.

# Questions to ask

- What are the largest datasets and joins, and how long may they take?
- How many jobs really need more memory or processors than one large machine provides?
- Who will tune and troubleshoot cluster jobs?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Compute provisioning options](../compute/compute-options.md), [Distributed training](../machine-learning/distributed-training.md), [Elastic scaling](../compute/elastic-scaling.md), [Partitioning and clustering](../storage/partitioning-clustering.md), [Single-node processing](single-node-processing.md), [Spot and interruptible compute](../compute/interruptible-compute.md), [SQL query engine](../compute/sql-query-engine.md), [Table maintenance and optimisation](../storage/table-maintenance.md), [Vectorised native execution](../compute/native-execution-acceleration.md) |
| Depends on | [Compute provisioning options](../compute/compute-options.md) |

# Where it appears

- **Use cases:** [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 2)
- **Patterns:** [Data lake](../../patterns/data-lake.md) · [ETL](../../patterns/etl.md) · [Lambda architecture](../../patterns/lambda-architecture.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Big Data and Data Science

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena for Apache Spark](../../technologies/aws/aws-athena-spark.md), [Amazon EMR on EC2](../../technologies/aws/aws-emr-on-ec2.md), [Amazon EMR on EKS](../../technologies/aws/aws-emr-on-eks.md), [Amazon EMR Serverless](../../technologies/aws/aws-emr-serverless.md), [AWS Glue ETL](../../technologies/aws/aws-glue-etl.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md), [Azure Synapse Analytics](../../technologies/microsoft/azure-synapse-analytics.md), [Azure Databricks](../../technologies/microsoft/azure-databricks.md) (distribution of Databricks) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Managed Service for Apache Spark (formerly Dataproc) | [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md), [Google Cloud Managed Service for Apache Spark on clusters](../../technologies/google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowpark](../../technologies/snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../../technologies/snowflake/snowflake-snowpark-connect-for-spark.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse server](../../technologies/clickhouse/clickhouse-server.md) |
| [Informatica](../../platforms/platform-informatica.md) | advanced mode on an advanced cluster | [Informatica Cloud Data Integration advanced mode](../../technologies/informatica/informatica-cdi-advanced-mode.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Base on premises](../../technologies/cloudera/cloudera-base-on-premises.md), [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Flow](../../technologies/oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Databricks](../../technologies/sap/sap-databricks.md) (distribution of Databricks) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Elastic Python Compute](../../technologies/teradata/teradata-elastic-python-compute.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Spark engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-spark.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Code Repositories](../../technologies/palantir/palantir-code-repositories.md) |
| [SAS](../../platforms/platform-sas.md) | CAS (Cloud Analytic Services) | [SAS Cloud Analytic Services (CAS)](../../technologies/sas/sas-cloud-analytic-services.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku code recipes and notebooks](../../technologies/dataiku/dataiku-code-recipes-notebooks.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Beam](../../technologies/open-source/apache-beam.md), [Apache Flink](../../technologies/open-source/apache-flink.md), [Apache Gluten](../../technologies/open-source/apache-gluten.md), [Apache Hadoop (HDFS and YARN)](../../technologies/open-source/apache-hadoop.md), [Apache Sedona](../../technologies/open-source/apache-sedona.md), [Apache Spark](../../technologies/open-source/apache-spark.md), [Dask](../../technologies/open-source/dask.md) |
