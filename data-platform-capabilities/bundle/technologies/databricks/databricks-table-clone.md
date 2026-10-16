---
type: Technology
id: databricks-table-clone
title: Databricks table clone (shallow and deep clone)
description: Copies a table at a given version. A shallow clone copies only metadata and points at the source files, while a deep clone copies the data as well.
aliases: [Delta table clone]
platform: platform-databricks
kind: feature
availability: ga
realises: [zero-copy-cloning, backup-restore, test-data-management]
resource: https://docs.databricks.com/aws/en/delta/clone
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Shallow clones suit development and testing. Deep clones are used for backups and migration. DEEP CLONE also works for managed Iceberg tables. There is no Git-style branching of lakehouse tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) (Storage and table management) (primary): Create an instant copy of a table, schema or database that shares storage with the original until either changes.
- [Backup and restore](../../capabilities/platform-operations/backup-restore.md) (Platform operations): Take point-in-time backups of data and metadata and restore them when needed.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Delta Lake on Databricks

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse zero-copy table clone](../microsoft/fabric-warehouse-zero-copy-clone.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table clones](../google-cloud/gcp-bigquery-table-clones.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake zero-copy cloning](../snowflake/snowflake-zero-copy-cloning.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Backup, Archive and Restore and Data Mover](../teradata/teradata-bar-data-mover.md) | [Backup and restore](../../capabilities/platform-operations/backup-restore.md), [Test data management](../../capabilities/development-lifecycle/test-data-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Perforce Delphix](../independent/perforce-delphix.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
