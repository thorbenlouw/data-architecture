---
type: Technology
id: fabric-warehouse-zero-copy-clone
title: Fabric Data Warehouse zero-copy table clone
description: Creates a copy of a warehouse table, at the current or a past point in time, that shares the underlying files with the original.
platform: platform-microsoft
kind: feature
availability: ga
realises: [zero-copy-cloning]
resource: https://learn.microsoft.com/en-us/fabric/data-warehouse/clone-table
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) (Storage and table management) (primary): Create an instant copy of a table, schema or database that shares storage with the original until either changes.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Warehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Aurora](../aws/aws-aurora.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery table clones](../google-cloud/gcp-bigquery-table-clones.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake zero-copy cloning](../snowflake/snowflake-zero-copy-cloning.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks table clone (shallow and deep clone)](../databricks/databricks-table-clone.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Perforce Delphix](../independent/perforce-delphix.md) | [Zero-copy cloning](../../capabilities/storage/zero-copy-cloning.md) |
