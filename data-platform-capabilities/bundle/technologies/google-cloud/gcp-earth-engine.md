---
type: Technology
id: gcp-earth-engine
title: Google Earth Engine
description: Cloud platform with a large catalogue of satellite imagery and other raster geospatial datasets, and APIs for analysing them at regional to global scale.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [geospatial-data]
resource: https://docs.cloud.google.com/earth-engine/docs
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Commercial use is licensed through Google Cloud. Earth Engine in BigQuery lets SQL users run raster statistics over vector geographies, and Earth Engine datasets can be shared through BigQuery sharing.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) (Specialised data types) (primary): Store, index and analyse location and shape data with spatial types and functions.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Location Service](../aws/aws-location-service.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Maps](../microsoft/azure-maps.md), [Maps in Microsoft Fabric](../microsoft/fabric-maps.md) (preview) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake geospatial data types and functions](../snowflake/snowflake-geospatial.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks spatial SQL (GEOMETRY and GEOGRAPHY)](../databricks/databricks-spatial-sql.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse geo data types and functions](../clickhouse/clickhouse-geo.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata in-database analytics functions](../teradata/teradata-in-database-analytics.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [PostGIS](../open-source/postgis.md), [Apache Sedona](../open-source/apache-sedona.md), [GeoParquet](../open-source/geoparquet.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Precisely Data Integrity Suite](../independent/precisely-data-integrity-suite.md) | [Geospatial data](../../capabilities/specialised-data/geospatial-data.md) |
