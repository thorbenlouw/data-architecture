---
type: Technology
id: vortex
title: Vortex
description: Extensible columnar file format and toolkit with pluggable encodings and compression, designed for fast random access and scans on object storage.
platform: platform-open-source
kind: open-standard
availability: ga
realises: [columnar-storage, file-formats, multimodal-data-formats]
resource: https://github.com/vortex-data/vortex
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, an incubation-stage LF AI & Data project, originally from SpiralDB. The file format is declared stable from version 0.36. A candidate Parquet alternative; Iceberg 1.11's pluggable file format API is designed to allow formats such as Vortex and Lance.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management) (primary): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
- [Multimodal data formats](../../capabilities/storage/multimodal-data-formats.md) (Storage and table management): Store images, audio, video and embeddings together with tabular columns in formats built for fast random access.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift](../aws/aws-redshift.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Delta table optimization and V-Order](../microsoft/fabric-delta-optimisation-v-order.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [MergeTree table engine family](../clickhouse/clickhouse-mergetree.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database](../teradata/teradata-database.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Db2](../ibm/ibm-db2.md) | [Columnar storage](../../capabilities/storage/columnar-storage.md) |
