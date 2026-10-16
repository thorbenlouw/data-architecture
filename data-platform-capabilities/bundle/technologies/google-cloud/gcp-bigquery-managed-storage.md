---
type: Technology
id: gcp-bigquery-managed-storage
title: BigQuery managed storage
description: Internal columnar storage for native BigQuery tables, with automatic compression, replication, partitioning, clustering and transactional writes.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [managed-storage, columnar-storage, partitioning-clustering, acid-transactions, schema-evolution]
resource: https://docs.cloud.google.com/bigquery/docs/storage_overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports time-unit, ingestion-time and integer-range partitioning, automatic re-clustering, multi-statement transactions and additive schema changes. Primary and foreign keys are informational only (used by the optimiser), and identity columns entered preview in August 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management) (primary): Let the platform manage table storage layout, compression and durability internally.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md) (Storage and table management): Organise table data by key columns so queries can skip data they do not need.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md), [Amazon Redshift](../aws/aws-redshift.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md), [Columnar storage](../../capabilities/storage/columnar-storage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Columnar storage](../../capabilities/storage/columnar-storage.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed tables](../databricks/databricks-unity-catalog-managed-tables.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [SharedMergeTree](../clickhouse/clickhouse-sharedmergetree.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud](../sap/sap-business-data-cloud.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Iceberg](../open-source/apache-iceberg.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Partitioning and clustering](../../capabilities/storage/partitioning-clustering.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
