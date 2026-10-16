---
type: Technology
id: snowflake-managed-storage
title: Snowflake micro-partitioned table storage
description: Stores standard tables in immutable, compressed, columnar micro-partitions with per-partition statistics that Snowflake manages, giving ACID transactions and partition pruning.
platform: platform-snowflake
kind: feature
availability: ga
realises: [managed-storage, columnar-storage, acid-transactions, row-level-updates, schema-evolution]
resource: https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The format is proprietary and is not directly readable by other engines. Use Iceberg tables when other engines need file-level access.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management) (primary): Let the platform manage table storage layout, compression and durability internally.
- [Columnar storage](../../capabilities/storage/columnar-storage.md) (Storage and table management): Store data column by column with compression and statistics so analytical queries read only what they need.
- [ACID transactions](../../capabilities/storage/acid-transactions.md) (Storage and table management): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md) (Storage and table management): Update, delete and merge individual rows in large tables efficiently.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md), [Amazon Redshift](../aws/aws-redshift.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md), [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [ACID transactions](../../capabilities/storage/acid-transactions.md), [Columnar storage](../../capabilities/storage/columnar-storage.md), [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog managed tables](../databricks/databricks-unity-catalog-managed-tables.md), [Delta Lake on Databricks](../databricks/databricks-delta-lake.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md), [ACID transactions](../../capabilities/storage/acid-transactions.md), [Row-level updates and deletes](../../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [SharedMergeTree](../clickhouse/clickhouse-sharedmergetree.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud](../sap/sap-business-data-cloud.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
