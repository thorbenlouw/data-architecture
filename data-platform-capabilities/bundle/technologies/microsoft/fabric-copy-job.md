---
type: Technology
id: fabric-copy-job
title: Fabric Copy job
description: Moves data from many sources to Fabric and other destinations in full, watermark-incremental or CDC mode, without building a pipeline.
platform: platform-microsoft
kind: feature
availability: ga
realises: [batch-ingestion, database-extraction, change-data-capture, incremental-processing]
resource: https://learn.microsoft.com/en-us/fabric/data-factory/what-is-copy-job
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports append, merge, overwrite and SCD type 2 writes; CDC for SQL Server, Azure SQL and Managed Instance became GA in June 2026, while other CDC sources, SCD type 2 and auto-partitioning are preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration) (primary): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Incremental processing](../../capabilities/processing/incremental-processing.md) (Processing and transformation): Process only new or changed data instead of recomputing everything each run.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Factory

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake bulk loading (COPY INTO <table>)](../snowflake/snowflake-copy-into.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
