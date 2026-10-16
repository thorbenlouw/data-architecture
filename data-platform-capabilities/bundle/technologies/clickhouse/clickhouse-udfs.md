---
type: Technology
id: clickhouse-udfs
title: ClickHouse user-defined functions
description: Extends ClickHouse with SQL lambda functions, executable functions that call external scripts such as Python over standard input and output, and experimental WebAssembly functions.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [user-defined-functions]
resource: https://clickhouse.com/docs/sql-reference/functions/udf
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Executable UDFs arrived in Cloud as a beta in June 2026 (with network-access UDFs in private beta) and the docs now describe them as generally available there; in open source they are labelled beta. WebAssembly UDFs are experimental and self-managed only.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation) (primary): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery user-defined functions](../google-cloud/gcp-bigquery-udfs.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake user-defined functions and stored procedures](../snowflake/snowflake-udfs-and-procedures.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog functions (UDFs)](../databricks/databricks-unity-catalog-functions.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache DataFusion](../open-source/apache-datafusion.md), [Apache Spark](../open-source/apache-spark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
