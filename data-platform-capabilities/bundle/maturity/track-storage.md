---
type: Maturity Track
id: track-storage
title: Storage and table management
description: How well data is kept in durable, open, maintained tables that many engines can read, update and trust.
covers:
- storage
- object-storage
- storage-tiering
- object-file-access
- file-formats
- columnar-storage
- multimodal-data-formats
- open-table-formats
- acid-transactions
- schema-evolution
- row-level-updates
- partitioning-clustering
- table-maintenance
- table-format-conversion
- table-catalogue
- catalogue-federation
- credential-vending
- managed-storage
- semi-structured-data
- data-versioning
- time-travel
- zero-copy-cloning
- data-branching
related_tracks: [track-compute, track-resilience, track-specialised-data, track-platform-migration]
levels:
- level: 1
  name: Initial
  summary: Data is kept as loose files or in single-purpose databases, with layout decided by each job.
  criteria:
  - Files in object storage or file shares are a mix of CSV, JSON and spreadsheets with no recorded schema.
  - Jobs overwrite files in place, so readers sometimes see half-written data.
  - Changing one record means rewriting a whole file or partition by hand.
  - Nobody can say which of several copies of a dataset is current.
  capabilities: [object-storage, file-formats]
- level: 2
  name: Managed
  summary: A team stores analytical data in columnar or platform-managed tables registered in a catalogue.
  criteria:
  - Analytical data is held in columnar formats such as Parquet or in platform-managed tables, not row-based text files.
  - Tables are registered in a catalogue with schema and location, and jobs refer to table names instead of file paths.
  - Large tables are partitioned on the columns most queries filter by, usually a date.
  - Nested data such as JSON is stored in native semi-structured types rather than flattened into text.
  capabilities: [columnar-storage, table-catalogue, managed-storage, partitioning-clustering, semi-structured-data]
- level: 3
  name: Defined
  summary: Transactional tables with schema control and history are the written platform standard.
  criteria:
  - The platform standard requires new analytical tables to use an open table format such as Apache Iceberg, Delta Lake or Apache Hudi, or managed tables with the same transactional guarantees.
  - Writes that do not match a table's declared schema fail, and the platform standard lists which changes are allowed in place, such as adding a nullable column.
  - Corrections and privacy erasures run as row-level MERGE or DELETE statements, not partition rewrites.
  - Users can query or restore any table as it was at an earlier version within a defined retention window.
  - Engines receive short-lived, table-scoped storage credentials from the catalogue instead of holding keys to whole buckets.
  capabilities:
  - open-table-formats
  - acid-transactions
  - schema-evolution
  - row-level-updates
  - data-versioning
  - time-travel
  - credential-vending
- level: 4
  name: Measured
  summary: Table health and storage cost are monitored, and maintenance runs automatically.
  criteria:
  - Compaction, snapshot expiry and orphan-file removal run automatically, and small-file counts per table are monitored against a threshold.
  - Lifecycle rules move data to cheaper tiers by age or access, and storage cost per domain is reported monthly.
  - Development and test copies are made by zero-copy clones or data branches, and the number of full physical copies is tracked.
  - Engines query tables registered in other catalogues, such as another business unit's or a legacy metastore, through federation instead of re-registering them by hand.
  capabilities: [table-maintenance, storage-tiering, zero-copy-cloning, data-branching, catalogue-federation]
- level: 5
  name: Optimising
  summary: Layout, formats and copies are adjusted continuously from measured access patterns.
  criteria:
  - Partition and clustering keys are changed based on query patterns, with scan statistics recorded before and after.
  - Engines that need a different table format read the same files through generated metadata, so no table is duplicated only to serve a second engine.
  - Training jobs, file-based tools and agents read lake data in place through file-system access or multimodal formats, and exported copies are tracked towards zero.
  - How long each table keeps snapshots for time travel is set from how far back restores and audits have actually needed to reach.
  capabilities: [table-format-conversion, object-file-access, multimodal-data-formats]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up turns a lake of loose files into transactional tables with schemas, history and a catalogue, so several engines can share one copy, privacy deletions actually happen, and queries stay fast as volume grows. Progress is often blocked by legacy formats such as CSV dumps, tables that nobody maintains until they slow down, proprietary storage that only one engine can read, and no owner for storage layout decisions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Data is kept as loose files or in single-purpose databases, with layout decided by each job.

- Files in object storage or file shares are a mix of CSV, JSON and spreadsheets with no recorded schema.
- Jobs overwrite files in place, so readers sometimes see half-written data.
- Changing one record means rewriting a whole file or partition by hand.
- Nobody can say which of several copies of a dataset is current.

**Capabilities first relied on:** [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md)

## Level 2: Managed

A team stores analytical data in columnar or platform-managed tables registered in a catalogue.

- Analytical data is held in columnar formats such as Parquet or in platform-managed tables, not row-based text files.
- Tables are registered in a catalogue with schema and location, and jobs refer to table names instead of file paths.
- Large tables are partitioned on the columns most queries filter by, usually a date.
- Nested data such as JSON is stored in native semi-structured types rather than flattened into text.

**Capabilities first relied on:** [Columnar storage](../capabilities/storage/columnar-storage.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md)

## Level 3: Defined

Transactional tables with schema control and history are the written platform standard.

- The platform standard requires new analytical tables to use an open table format such as Apache Iceberg, Delta Lake or Apache Hudi, or managed tables with the same transactional guarantees.
- Writes that do not match a table's declared schema fail, and the platform standard lists which changes are allowed in place, such as adding a nullable column.
- Corrections and privacy erasures run as row-level MERGE or DELETE statements, not partition rewrites.
- Users can query or restore any table as it was at an earlier version within a defined retention window.
- Engines receive short-lived, table-scoped storage credentials from the catalogue instead of holding keys to whole buckets.

**Capabilities first relied on:** [Open table formats](../capabilities/storage/open-table-formats.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Data versioning](../capabilities/storage/data-versioning.md), [Time travel](../capabilities/storage/time-travel.md), [Storage credential vending](../capabilities/storage/credential-vending.md)

## Level 4: Measured

Table health and storage cost are monitored, and maintenance runs automatically.

- Compaction, snapshot expiry and orphan-file removal run automatically, and small-file counts per table are monitored against a threshold.
- Lifecycle rules move data to cheaper tiers by age or access, and storage cost per domain is reported monthly.
- Development and test copies are made by zero-copy clones or data branches, and the number of full physical copies is tracked.
- Engines query tables registered in other catalogues, such as another business unit's or a legacy metastore, through federation instead of re-registering them by hand.

**Capabilities first relied on:** [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md)

## Level 5: Optimising

Layout, formats and copies are adjusted continuously from measured access patterns.

- Partition and clustering keys are changed based on query patterns, with scan statistics recorded before and after.
- Engines that need a different table format read the same files through generated metadata, so no table is duplicated only to serve a second engine.
- Training jobs, file-based tools and agents read lake data in place through file-system access or multimodal formats, and exported copies are tracked towards zero.
- How long each table keeps snapshots for time travel is set from how far back restores and audits have actually needed to reach.

**Capabilities first relied on:** [Table format conversion](../capabilities/storage/table-format-conversion.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md)

# Capabilities in scope

[Storage and table management](../capabilities/storage/storage.md), [ACID transactions](../capabilities/storage/acid-transactions.md), [Catalogue federation](../capabilities/storage/catalogue-federation.md), [Columnar storage](../capabilities/storage/columnar-storage.md), [Data branching and tagging](../capabilities/storage/data-branching.md), [Data versioning](../capabilities/storage/data-versioning.md), [File-system access to object storage](../capabilities/storage/object-file-access.md), [Multimodal data formats](../capabilities/storage/multimodal-data-formats.md), [Object storage](../capabilities/storage/object-storage.md), [Open file formats](../capabilities/storage/file-formats.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Partitioning and clustering](../capabilities/storage/partitioning-clustering.md), [Platform-managed storage](../capabilities/storage/managed-storage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Schema enforcement and evolution](../capabilities/storage/schema-evolution.md), [Semi-structured data](../capabilities/storage/semi-structured-data.md), [Storage credential vending](../capabilities/storage/credential-vending.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Table catalogue](../capabilities/storage/table-catalogue.md), [Table format conversion](../capabilities/storage/table-format-conversion.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Time travel](../capabilities/storage/time-travel.md), [Zero-copy cloning](../capabilities/storage/zero-copy-cloning.md)

# Related tracks

- [Compute and workload management](track-compute.md): How well compute is provisioned, isolated, scaled and tuned so that workloads meet performance targets at a known cost.
- [Resilience and recovery](track-resilience.md): How well the platform withstands and recovers from data loss, corruption, ransomware and outages within agreed targets.
- [Specialised data](track-specialised-data.md): How well the organisation stores, governs and analyses data that needs specialised types, indexes or engines, such as time series, location, graphs, searchable text, media, logs and bitemporal history.
- [Platform migration and portability](track-platform-migration.md): How safely and predictably the organisation moves workloads, code and data to new platforms, and how freely it can choose where the platform runs.

Levels follow the shared [maturity scale](maturity-scale.md).
