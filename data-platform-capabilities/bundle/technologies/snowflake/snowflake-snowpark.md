---
type: Technology
id: snowflake-snowpark
title: Snowpark
description: DataFrame and function APIs for Python, Java and Scala that push processing down into Snowflake warehouses as SQL, plus runtimes for running that code in the engine.
platform: platform-snowflake
kind: feature
availability: ga
realises: [dataframe-apis, user-defined-functions, distributed-processing, runtime-management]
resource: https://docs.snowflake.com/en/developer-guide/snowpark/index
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation) (primary): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowpark

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md), [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric semantic link (SemPy)](../microsoft/fabric-semantic-link.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md), [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md), [Databricks Connect](../databricks/databricks-connect.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Cloud Analytic Services (CAS)](../sas/sas-cloud-analytic-services.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dask](../open-source/dask.md), [Apache Spark](../open-source/apache-spark.md), [Polars](../open-source/polars.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Distributed processing](../../capabilities/processing/distributed-processing.md), [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
