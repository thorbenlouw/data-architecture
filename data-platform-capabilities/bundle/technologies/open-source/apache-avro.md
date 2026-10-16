---
type: Technology
id: apache-avro
title: Apache Avro
description: Row-based binary serialisation format with an embedded schema and well-defined schema evolution rules, widely used for Kafka messages.
aliases: [Avro]
platform: platform-open-source
kind: open-standard
availability: ga
realises: [file-formats, schema-evolution]
resource: https://avro.apache.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project. Usually paired with a schema registry for event streams; Iceberg uses it for manifest files.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Open file formats](../../capabilities/storage/file-formats.md) (Storage and table management) (primary): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Data Firehose](../aws/aws-data-firehose.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery external tables and load jobs](../google-cloud/gcp-bigquery-external-tables.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake external tables](../snowflake/snowflake-external-tables.md), [Snowflake semi-structured data types (VARIANT, OBJECT, ARRAY)](../snowflake/snowflake-semi-structured-data.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [clickhouse-local](../clickhouse/clickhouse-local.md), [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md) | [Open file formats](../../capabilities/storage/file-formats.md) |
