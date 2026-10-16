---
type: Technology
id: fabric-user-data-functions
title: Fabric user data functions
description: Serverless Python functions hosted in Fabric, each with a REST endpoint, callable from pipelines, notebooks, Activator rules and Power BI reports.
platform: platform-microsoft
kind: feature
availability: ga
realises: [user-defined-functions, data-applications, data-apis, data-writeback]
resource: https://learn.microsoft.com/en-us/fabric/data-engineering/user-data-functions/user-data-functions-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Enable Power BI translytical task flows, in which report users write back to SQL databases, warehouses or lakehouses. Scheduled functions are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) (Processing and transformation) (primary): Extend the engine with custom functions and procedures written in SQL, Python, Java or other languages.
- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps): Build and host interactive data applications next to the data, under platform security.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery user-defined functions](../google-cloud/gcp-bigquery-udfs.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake user-defined functions and stored procedures](../snowflake/snowflake-udfs-and-procedures.md), [Snowpark](../snowflake/snowflake-snowpark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog functions (UDFs)](../databricks/databricks-unity-catalog-functions.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse user-defined functions](../clickhouse/clickhouse-udfs.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Cloud for Apache Flink](../ibm/confluent-cloud-flink.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache DataFusion](../open-source/apache-datafusion.md), [Apache Spark](../open-source/apache-spark.md) | [User-defined functions and procedures](../../capabilities/processing/user-defined-functions.md) |
