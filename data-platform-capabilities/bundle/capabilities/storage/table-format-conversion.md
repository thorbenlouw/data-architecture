---
type: Capability
id: table-format-conversion
title: Table format conversion
description: Expose one copy of table data in several table formats by generating or translating metadata.
aliases: [UniForm, XTable, format interoperability]
broader: [open-table-formats]
related: [engine-interoperability, platform-migration, table-catalogue, catalogue-federation]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Table formats differ mainly in their metadata; the Parquet data files underneath are often compatible. Conversion tools read one format's metadata and write equivalent metadata in another, pointing at the same data files, so a table written as Delta Lake can also be read as Iceberg without copying any data. Apache XTable is an open-source example, and some formats can write a second format's metadata on every commit. Conversion can run once, to migrate a table, or after every commit, to keep several views of one table in step.

It helps when engines in one estate favour different formats, for example a processing platform that writes one and a warehouse or BI engine that reads another. It is usually an interim measure. Features in one format but not the other, such as deletion vectors or some partition transforms, may not translate, and continuous conversion adds delay and another moving part. Where engines support a common format natively, converging on it is simpler.

# Key considerations

- Check feature parity. Tables that use format-specific features may convert only partly, or not at all.
- Continuous conversion lags the source. Readers of the converted metadata may see slightly older data.
- Write only through the primary format. Writes through converted metadata can break the source table.
- Register converted tables in the catalogue consistently, so users do not see what look like two different tables.

# Questions to ask

- Which engines need to read the tables, and which formats does each support natively?
- Is the aim a one-off migration or lasting access in several formats?
- How fresh must the converted view of each table be?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Open table formats](open-table-formats.md) |
| Related | [Catalogue federation](catalogue-federation.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Platform migration](../platform-operations/platform-migration.md), [Table catalogue](table-catalogue.md) |

# Where it appears

- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../../technologies/microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Iceberg reads (UniForm)](../../technologies/databricks/databricks-iceberg-reads-uniform.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Apache XTable (incubating)](../../technologies/open-source/apache-xtable.md) (preview), [Delta Lake](../../technologies/open-source/delta-lake.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Managed Data Lake Service](../../technologies/independent/fivetran-managed-data-lake-service.md) |
