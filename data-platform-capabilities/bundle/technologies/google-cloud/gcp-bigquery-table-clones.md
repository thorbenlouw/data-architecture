---
type: Technology
id: gcp-bigquery-table-clones
title: BigQuery table clones
description: Writable copies of a table that share storage with the base table and are billed only for data that later changes in either.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [zero-copy-cloning, test-data-management]
resource: https://docs.cloud.google.com/bigquery/docs/table-clones-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Clones work at table level only; there is no dataset- or project-level clone, so environment copies need scripting.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) (Storage and table management) (primary): Create an instant copy of a table, schema or database that shares storage with the original until either changes.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Data Warehouse zero-copy table clone](../microsoft/fabric-warehouse-zero-copy-clone.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake zero-copy cloning](../snowflake/snowflake-zero-copy-cloning.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Perforce Delphix](../independent/perforce-delphix.md) | [Test data management](../../capabilities/development-lifecycle/test-data-management.md), [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
