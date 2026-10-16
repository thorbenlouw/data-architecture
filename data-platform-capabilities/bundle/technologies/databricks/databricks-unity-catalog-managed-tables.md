---
type: Technology
id: databricks-unity-catalog-managed-tables
title: Unity Catalog managed tables
description: Delta or Iceberg tables whose storage location, file layout, maintenance and lifecycle Unity Catalog manages, including on Databricks-managed default storage.
platform: platform-databricks
kind: feature
availability: ga
realises: [managed-storage, table-maintenance]
resource: https://docs.databricks.com/aws/en/optimizations/predictive-optimization
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Managed tables are needed for predictive optimisation, cross-engine ABAC and most new features. External Delta clients can create and write managed tables through the Unity REST API (Beta). Serverless workspaces use default storage rather than a customer bucket.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Platform-managed storage](../../capabilities/storage/managed-storage.md) (Storage and table management) (primary): Let the platform manage table storage layout, compression and durability internally.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon S3 Tables](../aws/aws-s3-tables.md), [Amazon Redshift](../aws/aws-redshift.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse](../microsoft/fabric-data-warehouse.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery managed storage](../google-cloud/gcp-bigquery-managed-storage.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake micro-partitioned table storage](../snowflake/snowflake-managed-storage.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [SharedMergeTree](../clickhouse/clickhouse-sharedmergetree.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Business Data Cloud](../sap/sap-business-data-cloud.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry](../palantir/palantir-foundry.md) | [Platform-managed storage](../../capabilities/storage/managed-storage.md) |
