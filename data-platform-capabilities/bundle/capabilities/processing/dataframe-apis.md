---
type: Capability
id: dataframe-apis
title: DataFrame APIs
description: Express transformations in Python, Scala or other languages through DataFrame interfaces that run in the engine.
aliases: [PySpark, Snowpark, BigQuery DataFrames]
broader: [processing]
related: [user-defined-functions, notebooks, feature-engineering, sql-transformation, data-testing]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A DataFrame is a table-like object in a programming language, with methods for filtering, joining, grouping and adding columns. The library records each call in a logical plan, and the engine optimises and runs the plan, often only when a result is requested. For example, `orders.filter(status == "paid").group_by("region").sum("amount")` runs as parallel compiled code inside the engine, not as a Python loop over rows.

DataFrames suit logic that is awkward in SQL: reusable functions, operations repeated over many columns, complex parsing, unit tests written with ordinary test frameworks, and work that mixes data preparation with machine learning libraries. pandas made the interface popular on one machine; Spark, Polars and others extend it to larger data, and some warehouses offer DataFrame APIs that compile to SQL so the code runs where the data is. Interfaces look alike but differ in behaviour, evaluation and scale, so code seldom moves between libraries unchanged.

# Key considerations

- Prefer the engine's built-in expressions to row-by-row Python functions, which pull data out of the optimised engine.
- Collecting a large result into local memory is a frequent cause of failed jobs.
- Portability libraries such as Ibis can run the same code on several engines, but cover only a subset of each engine's features.
- Apply the same review, tests and lineage capture as for SQL. Lineage tools often see SQL more clearly than DataFrame code.

# Questions to ask

- Which languages do your engineers and data scientists use every day?
- Which transformations are hard to express or test in SQL?
- Must the same code run on more than one engine, for example locally and on a cluster?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Related | [Data pipeline testing](../development-lifecycle/data-testing.md), [Feature engineering](../machine-learning/feature-engineering.md), [Notebooks](../development-lifecycle/notebooks.md), [Single-node processing](single-node-processing.md), [SQL transformation](sql-transformation.md), [User-defined functions and procedures](user-defined-functions.md), [Vectorised native execution](../compute/native-execution-acceleration.md) |

# Where it appears

- **Personas:** [Data engineer](../../personas/persona-data-engineer.md) · [Data scientist](../../personas/persona-data-scientist.md)
- **Maturity tracks:** [Transformation engineering](../../maturity/track-transformation.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena for Apache Spark](../../technologies/aws/aws-athena-spark.md), [Amazon EMR on EC2](../../technologies/aws/aws-emr-on-ec2.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md), [Fabric semantic link (SemPy)](../../technologies/microsoft/fabric-semantic-link.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery DataFrames](../../technologies/google-cloud/gcp-bigquery-dataframes.md), [Google Cloud Managed Service for Apache Spark serverless](../../technologies/google-cloud/gcp-managed-spark-serverless.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowpark, pandas on Snowflake, Snowpark Connect | [pandas on Snowflake](../../technologies/snowflake/snowflake-pandas-on-snowflake.md), [Snowpark](../../technologies/snowflake/snowflake-snowpark.md), [Snowpark Connect for Apache Spark](../../technologies/snowflake/snowflake-snowpark-connect-for-spark.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md), [Databricks Connect](../../technologies/databricks/databricks-connect.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [chDB](../../technologies/clickhouse/clickhouse-chdb.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Flow](../../technologies/oracle/oracle-oci-data-flow.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Elastic Python Compute](../../technologies/teradata/teradata-elastic-python-compute.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Spark engine in IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data-spark.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache DataFusion](../../technologies/open-source/apache-datafusion.md), [Apache Spark](../../technologies/open-source/apache-spark.md), [Dask](../../technologies/open-source/dask.md), [pandas](../../technologies/open-source/pandas.md), [Polars](../../technologies/open-source/polars.md) |
