---
type: Capability
id: geospatial-data
title: Geospatial data
description: Store, index and analyse location and shape data with spatial types and functions.
aliases: [GIS, spatial analytics]
broader: [specialised-data]
related: [data-enrichment, file-formats, deidentification, data-usage-rights, dashboards-reports]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Location data comes as points such as a delivery address, lines such as a road, and polygons such as a flood zone or sales territory. Spatial types store these shapes together with a coordinate reference system, which says how coordinates map onto the earth. Spatial functions measure distance, test whether a point lies inside a polygon, find overlapping shapes or locate the nearest depot to each customer. Spatial indexes, and grid systems such as H3 or geohash that give each location a cell identifier, speed these queries by narrowing candidates before exact tests.

It is needed in logistics, insurance risk, retail site planning, telecoms, agriculture and public services. Vector data (points, lines and polygons) is handled differently from raster data, which is gridded imagery such as satellite or elevation data, and many platforms support only vector data well. Open Geospatial Consortium standards, formats such as GeoParquet and GeoJSON, and spatial types in open table formats make geospatial data easier to move between tools.

# Key considerations

- Agree coordinate reference systems and convert on load. Mixing them gives wrong distances without any error.
- Spatial joins between large tables are expensive without spatial indexes or grid cells used as join keys.
- Turning addresses into coordinates often needs third-party data with licence restrictions.
- Precise locations can identify people. Treat them as personal data and coarsen them where possible.

# Questions to ask

- Is the need mainly points and distances, polygons and boundaries, or raster imagery?
- How large are the spatial joins, for example millions of events against thousands of areas?
- Which mapping and GIS tools must read the results?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Related | [Dashboards and interactive reports](../analytics-bi/dashboards-reports.md), [Data enrichment](../processing/data-enrichment.md), [Data licensing and usage rights](../governance/data-usage-rights.md), [De-identification](../governance/deidentification.md), [Open file formats](../storage/file-formats.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Location Service](../../technologies/aws/aws-location-service.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Maps](../../technologies/microsoft/azure-maps.md), [Maps in Microsoft Fabric](../../technologies/microsoft/fabric-maps.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery geospatial analytics](../../technologies/google-cloud/gcp-bigquery-geospatial.md), [Google Earth Engine](../../technologies/google-cloud/gcp-earth-engine.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake geospatial data types and functions](../../technologies/snowflake/snowflake-geospatial.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks spatial SQL (GEOMETRY and GEOGRAPHY)](../../technologies/databricks/databricks-spatial-sql.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse geo data types and functions](../../technologies/clickhouse/clickhouse-geo.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata in-database analytics functions](../../technologies/teradata/teradata-in-database-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Sedona](../../technologies/open-source/apache-sedona.md), [GeoParquet](../../technologies/open-source/geoparquet.md), [PostGIS](../../technologies/open-source/postgis.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md) |
