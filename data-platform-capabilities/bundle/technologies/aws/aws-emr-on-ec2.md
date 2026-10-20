---
type: Technology
id: aws-emr-on-ec2
title: Amazon EMR on EC2
description: Managed clusters on EC2 that run Apache Spark, Hive, Trino, Flink, HBase and other open-source frameworks with versioned release labels.
formerly: [Amazon Elastic MapReduce]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- distributed-processing
- provisioned-compute
- dataframe-apis
- runtime-management
- interruptible-compute
resource: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Gives the most control over instance types, Spot usage and configuration. EMR Studio provides notebooks; Lake Formation enforcement and Iceberg are supported in recent releases (7.x).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [Provisioned compute](../../capabilities/compute/provisioned-compute.md) (Query and compute): Run workloads on clusters or warehouses you size and control, for predictable performance and cost.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.
- [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md) (Query and compute): Run fault-tolerant jobs on spare capacity at a large discount, accepting that the provider can reclaim it at short notice.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon EMR

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md), [Azure Synapse Analytics](../microsoft/azure-synapse-analytics.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md), [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark](../snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Spot and interruptible compute](../../capabilities/compute/interruptible-compute.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Apache Hadoop (HDFS and YARN)](../open-source/apache-hadoop.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Provisioned compute](../../capabilities/compute/provisioned-compute.md) |
