---
type: Technology
id: apache-xtable
title: Apache XTable (incubating)
description: Converter that translates table metadata between Iceberg, Delta Lake and Hudi so one copy of the data can be read as any of the three formats.
aliases: [XTable]
formerly: [OneTable]
platform: platform-open-source
kind: open-source
availability: preview
realises: [table-format-conversion, engine-interoperability]
resource: https://incubator.apache.org/projects/xtable.html
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, in the ASF Incubator since February 2024, originally from Onehouse. Translates metadata only, not data files. Delta UniForm and Iceberg-compatible metadata in Paimon solve the same problem inside a single format.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table format conversion](../../capabilities/storage/table-format-conversion.md) (Storage and table management) (primary): Expose one copy of table data in several table formats by generating or translating metadata.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Apache Iceberg tables in Snowflake](../snowflake/snowflake-iceberg-tables.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Iceberg reads (UniForm)](../databricks/databricks-iceberg-reads-uniform.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table format conversion](../../capabilities/storage/table-format-conversion.md) |
