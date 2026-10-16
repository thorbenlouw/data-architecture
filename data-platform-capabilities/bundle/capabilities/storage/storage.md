---
type: Capability
id: storage
title: Storage and table management
description: Store data durably and cheaply in formats that many tools can read and manage it as reliable tables.
broader: []
related: [compute, engine-interoperability, decoupled-storage-compute, data-retention, business-continuity]
order: 2
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

This domain covers where data physically sits and how a collection of files becomes something engines can treat as a table. At the bottom is object storage: cheap, durable and almost unlimited, but with no idea of rows or schemas. Open file formats such as Parquet, ORC and Avro define how values are laid out inside each file, and columnar formats let queries read only the columns and blocks they need.

Open table formats such as Apache Iceberg, Delta Lake and Apache Hudi add a metadata layer that records which files make up a table at each version. That layer provides ACID commits, schema enforcement, row-level changes, partitioning and history. A table catalogue names the tables, points engines at their current metadata and applies permissions, increasingly by vending short-lived storage credentials. Data versioning, time travel, cloning and branching all build on the same snapshot metadata.

Platform-managed storage is the alternative: the vendor controls layout and format internally, which removes maintenance work but ties the data to one engine. Most estates use both. The main decisions in this domain are where the boundary sits between open storage shared by many engines and managed storage tuned for one, and which catalogue is the authority for table names and access.

# Key considerations

- Decide early which table format and which catalogue are authoritative. Changing either later means rewriting metadata for every table and repointing every engine.
- Open file formats remove engine lock-in only if the catalogue is open too. A proprietary catalogue in front of open files can recreate the same dependency.
- Storage is cheap per gigabyte, but request charges, cross-region transfer and retained history add up. Model them alongside capacity.
- Plan table maintenance from the start. Tables written by streams or frequent small batches degrade within days without compaction and snapshot expiry.
- History kept for time travel and versioning can hold personal data after a deletion request. Align retention settings with privacy and retention rules.

# Questions to ask

- Which engines and tools need to read or write the same data, now and over the next few years?
- How much data is stored today, how fast is it growing, and how much of it is queried regularly?
- Do residency, retention or erasure obligations constrain where data and its history are kept, and for how long?
- Who will own table maintenance, catalogue administration and storage cost?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Data versioning](data-versioning.md), [Object storage](object-storage.md), [Open file formats](file-formats.md), [Open table formats](open-table-formats.md), [Partitioning and clustering](partitioning-clustering.md), [Platform-managed storage](managed-storage.md), [Semi-structured data](semi-structured-data.md), [Table catalogue](table-catalogue.md) |
| Related | [Query and compute](../compute/compute.md), [Backup and disaster recovery](../platform-operations/business-continuity.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Retention and disposal](../governance/data-retention.md) |
| Needed by | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Processing and transformation](../processing/processing.md), [Serving and activation](../serving/serving.md) |

# Where it appears

- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 137 technologies; see their pages.
