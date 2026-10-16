---
type: Technology
id: databricks-unity-catalog-functions
title: Unity Catalog functions (UDFs)
description: SQL, Python, Scala and Java user-defined functions registered and governed in Unity Catalog. They run on serverless and standard compute with sandboxing.
platform: platform-databricks
kind: feature
availability: ga
realises: [user-defined-functions]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/september
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Scala and Java UDFs became GA in July 2026 and scalar and batch Python UDFs in September 2026. Functions can be tagged and used as ABAC masking or filter functions and as agent tools.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation) (primary): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery user-defined functions](../google-cloud/gcp-bigquery-udfs.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake user-defined functions and stored procedures](../snowflake/snowflake-udfs-and-procedures.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse user-defined functions](../clickhouse/clickhouse-udfs.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache DataFusion](../open-source/apache-datafusion.md), [Apache Spark](../open-source/apache-spark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
