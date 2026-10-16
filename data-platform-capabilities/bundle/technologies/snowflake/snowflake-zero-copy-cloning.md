---
type: Technology
id: snowflake-zero-copy-cloning
title: Snowflake zero-copy cloning
description: Creates instant writable copies of tables, schemas or databases that share micro-partitions with the source until either side changes.
platform: platform-snowflake
kind: feature
availability: ga
realises: [zero-copy-cloning, test-data-management]
resource: https://docs.snowflake.com/en/user-guide/object-clone
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Often combined with Time Travel (CLONE ... AT) to build development and test environments from production. Clones do not inherit the source's grants unless COPY GRANTS is used.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) (Storage and table management) (primary): Create an instant copy of a table, schema or database that shares storage with the original until either changes.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse zero-copy table clone](../microsoft/fabric-warehouse-zero-copy-clone.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table clones](../google-cloud/gcp-bigquery-table-clones.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Perforce Delphix](../independent/perforce-delphix.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
