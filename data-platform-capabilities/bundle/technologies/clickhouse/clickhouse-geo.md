---
type: Technology
id: clickhouse-geo
title: ClickHouse geo data types and functions
description: Point, polygon and line types plus functions for great-circle distances, point-in-polygon tests, geohash, H3 and S2 indexing and Mapbox vector tile encoding.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [geospatial-data]
resource: https://clickhouse.com/docs/sql-reference/functions/geo
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Geospatial support is function-based; there is no dedicated spatial index, so filtering usually relies on H3 or geohash columns in the sorting key or on polygon dictionaries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types) (primary): Store, index and analyse location and shape data with spatial types and functions.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
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
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostGIS](../open-source/postgis.md), [Apache Sedona](../open-source/apache-sedona.md), [GeoParquet](../open-source/geoparquet.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Precisely Data Integrity Suite](../independent/precisely-data-integrity-suite.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
