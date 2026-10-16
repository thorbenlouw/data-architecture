---
type: Technology
id: polars
title: Polars
description: DataFrame library written in Rust with Python bindings, using lazy query optimisation and a streaming engine to process data larger than memory on one machine.
platform: platform-open-source
kind: open-source
availability: ga
realises: [dataframe-apis, single-node-processing]
resource: https://pola.rs/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MIT licence, led by Polars Inc. Polars Cloud, its distributed managed service, is commercial and separate from the open-source library. It is often chosen in place of pandas for medium-sized data pipelines.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation) (primary): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [Single-node processing](../../capabilities/processing/single-node-processing.md) (Processing and transformation): Process small to medium datasets quickly on one machine using in-process engines.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric semantic link (SemPy)](../microsoft/fabric-semantic-link.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery DataFrames](../google-cloud/gcp-bigquery-dataframes.md), [Google Cloud Managed Service for Apache Spark serverless](../google-cloud/gcp-managed-spark-serverless.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md), [Single-node processing](../../capabilities/processing/single-node-processing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
