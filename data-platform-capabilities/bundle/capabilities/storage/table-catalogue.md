---
type: Capability
id: table-catalogue
title: Table catalogue
description: Register tables, their schemas and storage locations so engines can find, govern and share them.
aliases: [metastore, Iceberg REST catalogue, Hive metastore, technical catalogue]
broader: [storage]
related: [data-catalogue, engine-interoperability, access-control, metadata-harvesting, open-table-formats]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A table catalogue maps names such as `sales.orders` to what an engine needs to use the table: where its current metadata lives, its schema, its properties and who may read or write it. For Iceberg tables, and increasingly for other formats, the catalogue also performs the atomic commit by moving the pointer to each table's latest snapshot, so all writers must go through it. The Iceberg REST catalogue specification has become a common interface, letting engines from different vendors use the same catalogue; the Hive Metastore is the older standard. Tables are usually organised in a hierarchy of catalogue, schema (or namespace) and table.

The catalogue is where storage, engines and governance meet. Whoever controls it controls naming, access and, in practice, which engines can take part. A table catalogue is technical and serves engines at query time. A data catalogue is a discovery tool for people, with descriptions, owners and lineage, and usually harvests its technical metadata from table catalogues. Some products combine the two.

# Key considerations

- Choose a catalogue with an open API that every engine you use supports for both reads and writes. Otherwise each engine needs its own copy of the metadata.
- Every query plan and commit passes through the catalogue. Treat its availability and latency as a production dependency, with backup and recovery.
- Decide where access policies are enforced: in the catalogue, in each engine, or both. Policies defined in one engine do not follow the data to another.
- Design the namespace around domains and environments early. Renaming catalogues and schemas later breaks code and grants.

# Questions to ask

- How many engines need to find and write the same tables?
- Is there one authoritative catalogue today, or several that disagree?
- Where are permissions defined, and must they hold whichever engine is used?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Narrower | [Catalogue federation](catalogue-federation.md), [Storage credential vending](credential-vending.md) |
| Related | [Metadata and discovery](../metadata/metadata.md), [Access control](../security/access-control.md), [ACID transactions](acid-transactions.md), [Data catalogue](../metadata/data-catalogue.md), [Metadata harvesting](../metadata/metadata-harvesting.md), [Model registry](../machine-learning/model-registry.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Offline feature store](../machine-learning/offline-feature-store.md), [Open table formats](open-table-formats.md), [Table format conversion](table-format-conversion.md) |
| Needed by | [Internal data sharing](../data-sharing/internal-data-sharing.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md) |

# Where it appears

- **Patterns:** [Lakehouse](../../patterns/lakehouse.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 2, Managed) · [Storage and table management](../../maturity/track-storage.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 5 Cataloguing (Cataloguing and classification) · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Infrastructures & Servers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS Glue Data Catalog | [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Lakehouse (schemas) in OneLake | [Fabric Lakehouse](../../technologies/microsoft/fabric-lakehouse.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Lakehouse runtime catalog (formerly BigLake metastore) | [Dataproc Metastore](../../technologies/google-cloud/gcp-dataproc-metastore.md), [Google Cloud Lakehouse runtime catalog](../../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Horizon Catalog / Horizon Iceberg REST Catalog | [Snowflake Horizon Catalog](../../technologies/snowflake/snowflake-horizon-catalog.md), [Snowflake Open Catalog](../../technologies/snowflake/snowflake-open-catalog.md) (deprecated) |
| [Databricks](../../platforms/platform-databricks.md) | Unity Catalog metastore | [Unity Catalog](../../technologies/databricks/databricks-unity-catalog.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | DataLakeCatalog database engine (data catalogs) |  |
| [Cloudera](../../platforms/platform-cloudera.md) | Hive Metastore / Iceberg REST Catalog | [Cloudera Iceberg REST Catalog](../../technologies/cloudera/cloudera-iceberg-rest-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) | Autonomous AI Database Catalog / Data Catalog metastore | [OCI Data Catalog](../../technologies/oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../../technologies/oracle/oracle-autonomous-ai-database-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [Dremio Cloud](../../technologies/sap/dremio-cloud.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Tableflow](../../technologies/ibm/confluent-tableflow.md), [IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Iceberg tables in Palantir Foundry](../../technologies/palantir/palantir-iceberg-tables.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [Apache Hive Metastore](../../technologies/open-source/apache-hive-metastore.md), [Apache Polaris](../../technologies/open-source/apache-polaris.md), [DuckLake](../../technologies/open-source/ducklake.md), [Iceberg REST Catalog specification](../../technologies/open-source/apache-iceberg-rest-catalog-spec.md), [Project Nessie](../../technologies/open-source/project-nessie.md), [Unity Catalog (open source)](../../technologies/open-source/unity-catalog.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Managed Data Lake Service](../../technologies/independent/fivetran-managed-data-lake-service.md) |

Narrower capabilities are realised by a further 19 technologies; see their pages.
