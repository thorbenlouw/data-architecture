---
type: Technology
id: gcp-bigquery-dataframes
title: BigQuery DataFrames
description: Python library (bigframes) offering pandas- and scikit-learn-style APIs that compile to BigQuery SQL so data stays in BigQuery.
aliases: [bigframes]
platform: platform-google-cloud
kind: open-source
availability: ga
realises: [dataframe-apis, feature-engineering, ai-functions]
resource: https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0 licence. Python functions can be deployed as BigQuery remote or Python UDFs, and LLM calls go through BigQuery AI functions. Version 2.0 changed some defaults.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) (Processing and transformation) (primary): Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
- [Feature engineering](../../capabilities/machine-learning/feature-engineering.md) (Machine learning development): Turn raw data into model inputs in reusable, consistent pipelines.
- [AI functions in SQL](../../capabilities/processing/ai-functions.md) (Processing and transformation): Call language models from SQL or DataFrame code to classify, extract, summarise or translate data at scale.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena for Apache Spark](../aws/aws-athena-spark.md), [Amazon EMR on EC2](../aws/aws-emr-on-ec2.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric semantic link (SemPy)](../microsoft/fabric-semantic-link.md), [Apache Spark in Microsoft Fabric](../microsoft/fabric-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [pandas on Snowflake](../snowflake/snowflake-pandas-on-snowflake.md), [Snowpark Connect for Apache Spark](../snowflake/snowflake-snowpark-connect-for-spark.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Connect](../databricks/databricks-connect.md), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [chDB](../clickhouse/clickhouse-chdb.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Flow](../oracle/oracle-oci-data-flow.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Elastic Python Compute](../teradata/teradata-elastic-python-compute.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [IBM](../../platforms/platform-ibm.md) | [Spark engine in IBM watsonx.data](../ibm/ibm-watsonx-data-spark.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Polars](../open-source/polars.md), [pandas](../open-source/pandas.md), [Dask](../open-source/dask.md) | [DataFrame APIs](../../capabilities/processing/dataframe-apis.md) |
