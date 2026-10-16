---
type: Technology
id: apache-sedona
title: Apache Sedona
description: Spatial computing engine that adds geospatial types, functions and spatial joins to Spark, Flink and other engines.
aliases: [Sedona, SedonaDB]
formerly: [GeoSpark]
platform: platform-open-source
kind: open-source
availability: ga
realises: [geospatial-data, distributed-processing]
resource: https://sedona.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0; Wherobots is the main commercial vendor. SedonaDB, a single-node engine in Rust, extends the project beyond Spark. Reads and writes GeoParquet and Iceberg geospatial types.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types) (primary): Store, index and analyse location and shape data with spatial types and functions.
- [Distributed processing](../../capabilities/processing/distributed-processing.md) (Processing and transformation): Process large datasets in parallel across a cluster of machines.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Location Service](../aws/aws-location-service.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Maps](../microsoft/azure-maps.md), [Maps in Microsoft Fabric](../microsoft/fabric-maps.md) (preview) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery geospatial analytics](../google-cloud/gcp-bigquery-geospatial.md), [Google Earth Engine](../google-cloud/gcp-earth-engine.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake geospatial data types and functions](../snowflake/snowflake-geospatial.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks spatial SQL (GEOMETRY and GEOGRAPHY)](../databricks/databricks-spatial-sql.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse geo data types and functions](../clickhouse/clickhouse-geo.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Precisely Data Integrity Suite](../independent/precisely-data-integrity-suite.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
