---
type: Capability
id: catalogue-federation
title: Catalogue federation
description: Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
aliases: [catalogue of catalogues, federated catalogue]
broader: [table-catalogue]
related:
- query-federation
- data-policy-management
- platform-migration
- internal-data-sharing
- data-catalogue
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A federating catalogue connects to other catalogues, such as a Hive Metastore, another Iceberg REST catalogue or a database's own system tables, and shows their tables in its own namespace. The metadata stays with the source and is read through, or mirrored automatically, instead of being registered again by hand. Permissions, auditing and lineage are applied in the federating catalogue, so a user granted access to `finance.ledger` gets it whether the table lives in an old metastore or in another cloud.

It is useful during migrations, after acquisitions, and where business units run different platforms, because it gives one place to find and govern tables without moving them. It differs from query federation, which runs queries against external systems; catalogue federation deals with metadata and permissions, although the two are often combined. Limits appear quickly: write support, freshness of mirrored metadata and which policies the sources actually honour vary widely.

# Key considerations

- Federated tables are often read-only. Check whether writes and commits go through the federating catalogue or must go to the source.
- Find out whether metadata is read live or cached. Cached metadata can show dropped or changed tables until it refreshes.
- Permissions in the federating catalogue only protect access through it. Direct access to the source catalogue or its storage must be closed or governed too.
- Decide whether federation is a step towards consolidation or a lasting design. A lasting design needs an owner for every connection.

# Questions to ask

- How many separate catalogues or metastores exist today, and who owns each?
- Is the aim one point of governance, one point of discovery, or a later migration?
- Do users need to write to federated tables, or only read them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Table catalogue](table-catalogue.md) |
| Related | [Data catalogue](../metadata/data-catalogue.md), [Internal data sharing](../data-sharing/internal-data-sharing.md), [Metadata interoperability](../metadata/metadata-interoperability.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Open-protocol sharing](../data-sharing/open-protocol-sharing.md), [Platform migration](../platform-operations/platform-migration.md), [Policy management](../governance/data-policy-management.md), [Query federation](../compute/query-federation.md), [Table format conversion](table-format-conversion.md) |

# Where it appears

- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 4, Measured) · [Storage and table management](../../maturity/track-storage.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena](../../technologies/aws/aws-athena.md), [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md), [Lakehouse architecture of Amazon SageMaker](../../technologies/aws/aws-sagemaker-lakehouse.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Mirrored Azure Databricks Catalog](../../technologies/microsoft/fabric-mirrored-azure-databricks-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake catalog-linked databases](../../technologies/snowflake/snowflake-catalog-linked-databases.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks catalog federation](../../technologies/databricks/databricks-catalog-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse DataLakeCatalog database engine](../../technologies/clickhouse/clickhouse-datalakecatalog.md) (preview) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database Catalog](../../technologies/oracle/oracle-autonomous-ai-database-catalog.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [Apache Polaris](../../technologies/open-source/apache-polaris.md) |
