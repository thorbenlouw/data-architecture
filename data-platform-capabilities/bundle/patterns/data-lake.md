---
type: Pattern
id: data-lake
title: Data lake
description: A store of raw data in open files of any structure, with schema applied when the data is read.
uses:
- object-storage
- file-formats
- file-ingestion
- semi-structured-data
- unstructured-data
- distributed-processing
- data-catalogue
- metadata-harvesting
- storage-tiering
related: [lakehouse, medallion-architecture, data-warehouse, elt]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Files land in cheap object storage in the form the sources produce them: CSV extracts, JSON events, Parquet, logs, images. Nothing is modelled in advance; each consumer applies a structure when it reads the files, which is called schema-on-read. James Dixon, then CTO of Pentaho, coined the term around 2010, contrasting a lake of water in its natural state with the cleaned and bottled data of a data mart. Early lakes ran on the Hadoop distributed file system; most now use cloud object storage, with engines such as Apache Spark or Trino reading the files.

A lake suits keeping everything at low cost before you know how it will be used, feeding data science, holding very large volumes and storing data that does not fit tables. Without a catalogue, owners and quality controls it tends to become a "data swamp" where nobody knows what files mean or whether they are current. Plain files also lack transactions, so concurrent writes and row-level updates are hard. The lakehouse pattern grew out of closing those gaps.

# When to use

- You need to retain large volumes of raw data cheaply, including semi-structured and unstructured content.
- Data science and ML teams want direct access to files in open formats.
- Sources and their uses are still uncertain, so modelling up front would be premature.

# Watch out for

- Without a catalogue, owners and retention rules, the lake fills with files nobody can interpret or safely delete.
- Plain files give no transactional guarantees; readers can see half-written data, and updates or deletes for privacy requests are slow.
- Access control at file or folder level is coarse; row and column rules need a table layer above the files.
- Many small files slow queries and raise storage request costs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities it relies on

- [Object storage](../capabilities/storage/object-storage.md): Store any volume of files cheaply and durably as the foundation of a data lake or lakehouse.
- [Open file formats](../capabilities/storage/file-formats.md): Store data in open, well-specified file formats such as Parquet, ORC, Avro and JSON.
- [File ingestion](../capabilities/ingestion-integration/file-ingestion.md): Detect and load files arriving in landing storage, processing each file exactly once.
- [Semi-structured data](../capabilities/storage/semi-structured-data.md): Store and query nested data such as JSON without flattening it first.
- [Unstructured data management](../capabilities/specialised-data/unstructured-data.md): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Distributed processing](../capabilities/processing/distributed-processing.md): Process large datasets in parallel across a cluster of machines.
- [Data catalogue](../capabilities/metadata/data-catalogue.md): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md): Move data between hot, cool and archive tiers automatically based on age or access patterns.

# Related patterns

- [Lakehouse](lakehouse.md)
- [Medallion architecture](medallion-architecture.md)
- [Data warehouse](data-warehouse.md)
- [ELT](elt.md)

# Where it appears

- **Use cases:** [Security and log analytics](../use-cases/usecase-security-log-analytics.md)
