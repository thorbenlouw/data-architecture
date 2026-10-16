---
type: Pattern
id: lakehouse
title: Lakehouse
description: Warehouse-style tables, transactions and governance on open formats in object storage, shared by many engines.
aliases: [open lakehouse, data lakehouse]
uses:
- object-storage
- open-table-formats
- acid-transactions
- table-catalogue
- engine-interoperability
- decoupled-storage-compute
- columnar-storage
- table-maintenance
- time-travel
- credential-vending
related: [data-lake, data-warehouse, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data stays in open files such as Parquet in object storage, and an open table format such as Apache Iceberg, Delta Lake or Apache Hudi adds a metadata layer that records which files make up each version of a table. That layer provides atomic commits, schema enforcement, time travel and row-level updates. A table catalogue records where each table lives and who may use it, so SQL engines, Spark jobs and ML frameworks can work on one copy. The term was set out in a 2021 CIDR paper by researchers at Databricks, though Netflix, Uber and others had built open table formats a few years earlier.

The aim is to stop running a lake for data science and a separate warehouse for BI, with copies and pipelines between them. Choosing a lakehouse is mostly a choice about openness: which catalogue governs the tables, and whether several engines can write as well as read. A warehouse engine that reads and writes open table formats can be part of a lakehouse; the difference lies in who controls the storage and metadata.

# When to use

- BI, data science and ML teams need to work on the same data without copying it between a lake and a warehouse.
- You want to avoid storage lock-in and keep the option to change or add query engines.
- You need warehouse behaviour such as updates, deletes and history on data held in object storage.

# Watch out for

- The catalogue becomes the point of control and of lock-in; check that it offers an open API, such as the Iceberg REST catalogue, and that other engines can write through it.
- Tables need regular compaction, snapshot expiry and clustering, or performance and storage cost degrade.
- Engines support table format features unevenly; test multi-engine writes, deletes and schema changes before relying on them.
- Fine-grained access rules must be enforced by every engine that reads the tables, not only by one.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Object storage](../capabilities/storage/object-storage.md): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Open table formats](../capabilities/storage/open-table-formats.md): Manage collections of files as transactional tables with a defined schema, history and metadata.
- [ACID transactions](../capabilities/storage/acid-transactions.md): Commit concurrent writes atomically so readers never see partial or conflicting results.
- [Table catalogue](../capabilities/storage/table-catalogue.md): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Multi-engine interoperability](../capabilities/compute/engine-interoperability.md): Let several engines read and write the same tables through open formats and shared catalogues.
- [Decoupled storage and compute](../capabilities/compute/decoupled-storage-compute.md): Scale storage and compute independently and let several compute clusters work on the same data.
- [Columnar storage](../capabilities/storage/columnar-storage.md): Store data column by column with compression and statistics so analytical queries read only what they need.
- [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Time travel](../capabilities/storage/time-travel.md): Query or restore a table as it was at an earlier point in time or version.
- [Storage credential vending](../capabilities/storage/credential-vending.md): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

# Related patterns

- [Data lake](data-lake.md)
- [Data warehouse](data-warehouse.md)
- [Medallion architecture](medallion-architecture.md)
- [ELT](elt.md)

# Where it appears

- **Use cases:** [Self-service domain onboarding](../use-cases/usecase-domain-onboarding.md) · [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) · [Security and log analytics](../use-cases/usecase-security-log-analytics.md)
- **Personas:** [Data architect](../personas/persona-data-architect.md) · [Data platform engineer](../personas/persona-platform-engineer.md)
