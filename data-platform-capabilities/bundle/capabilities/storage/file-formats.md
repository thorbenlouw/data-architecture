---
type: Capability
id: file-formats
title: Open file formats
description: Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
aliases: [storage formats]
broader: [storage]
related: [engine-interoperability, semi-structured-data, file-ingestion, schema-registry, data-export]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

An open file format has a published specification for how values, types and metadata are encoded, so any tool that implements it can read the file without the program that wrote it. Columnar formats such as Apache Parquet and ORC suit analytics. Row formats such as Apache Avro suit record-by-record writing and messaging, and carry their schema with the data. Text formats such as CSV and JSON are easy to produce and inspect but slow to parse, loosely typed and large. Apache Arrow defines a matching in-memory columnar layout for passing data between processes without conversion.

The choice affects cost, speed and portability for the life of the data. A CSV file holds no types, so each reader reinterprets dates and decimals; a Parquet file records types, compression and per-column statistics. The usual practice is to accept what sources send at the edge, then convert anything that will be queried to a columnar format. File formats describe single files; table formats describe which files make up a table.

# Key considerations

- Standardise on a small set of formats for curated data. Each extra format needs reader support, tests and conversion code.
- Writer settings matter as much as the format. Compression codec, row group size, dictionary encoding and file size all change read performance.
- Readers do not all support every feature. Check nested types, time zones, decimals and newer encodings across every engine that will read the files.
- Keep the original raw files where replay or audit needs them, even after converting to a columnar format.

# Questions to ask

- In which formats do sources deliver data today, and which tools must read the stored data?
- Is the data mostly read in large analytical scans, or written and read one record at a time?
- How long must the data stay readable, and by which future tools?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Narrower | [Columnar storage](columnar-storage.md), [Multimodal data formats](multimodal-data-formats.md) |
| Related | [Data export](../serving/data-export.md), [File ingestion](../ingestion-integration/file-ingestion.md), [Geospatial data](../specialised-data/geospatial-data.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Schema registry](../metadata/schema-registry.md), [Semi-structured data](semi-structured-data.md) |
| Needed by | [Open table formats](open-table-formats.md), [Single-node processing](../processing/single-node-processing.md) |

# Where it appears

- **Patterns:** [Data lake](../../patterns/data-lake.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 1, Initial)
- **Frameworks:** [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VI – Switching between data processing services; Chapter VIII – Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Data Firehose](../../technologies/aws/aws-data-firehose.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery external tables and load jobs](../../technologies/google-cloud/gcp-bigquery-external-tables.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake external tables](../../technologies/snowflake/snowflake-external-tables.md), [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../../technologies/snowflake/snowflake-semi-structured-data.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse integration table engines and table functions](../../technologies/clickhouse/clickhouse-integration-engines.md), [clickhouse-local](../../technologies/clickhouse/clickhouse-local.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Avro](../../technologies/open-source/apache-avro.md), [Apache ORC](../../technologies/open-source/apache-orc.md), [Apache Parquet](../../technologies/open-source/apache-parquet.md), [GeoParquet](../../technologies/open-source/geoparquet.md), [Vortex](../../technologies/open-source/vortex.md) |

Narrower capabilities are realised by a further 13 technologies; see their pages.
