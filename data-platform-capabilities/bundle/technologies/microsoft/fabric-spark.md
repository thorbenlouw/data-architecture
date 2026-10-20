---
type: Technology
id: fabric-spark
title: Apache Spark in Microsoft Fabric
description: Managed Spark runtime with starter pools, custom pools and a native vectorised execution engine for data engineering and data science jobs.
aliases: [Fabric Spark, Native Execution Engine]
platform: platform-microsoft
kind: feature
availability: ga
realises:
- distributed-processing
- dataframe-apis
- stream-processing
- serverless-compute
- native-execution-acceleration
- runtime-management
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs on capacity units, or on pay-as-you-go Autoscale Billing for Spark outside the capacity. The Native Execution Engine accelerates Spark SQL and DataFrames. Fabric Runtime 2.0 (Spark 4.x) is in preview. Spark job definitions run non-interactive jobs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation) (primary): Process large datasets in parallel across a cluster of machines.
- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) (Query and compute): Speed up engines by running operators in native, vectorised code without changing user code.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Engineering

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR Serverless](../aws/aws-emr-serverless.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [Google Cloud Managed Service for Apache Spark on clusters](../google-cloud/gcp-managed-spark-clusters.md), [Google Cloud Dataflow](../google-cloud/gcp-dataflow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpark](../snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse server](../clickhouse/clickhouse-server.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Integration advanced mode](../informatica/informatica-cdi-advanced-mode.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md), [Cloudera Base on premises](../cloudera/cloudera-base-on-premises.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Code Repositories](../palantir/palantir-code-repositories.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku code recipes and notebooks](../dataiku/dataiku-code-recipes-notebooks.md) | [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Apache Gluten](../open-source/apache-gluten.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Vectorised native execution](../../capabilities/compute/native-execution-acceleration.md) |
