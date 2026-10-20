---
type: Capability
id: engine-interoperability
title: Multi-engine interoperability
description: Let several engines read and write the same tables through open formats and shared catalogues.
aliases: [open lakehouse, engine-agnostic storage]
broader: [compute]
related:
- credential-vending
- open-protocol-sharing
- table-format-conversion
- decoupled-storage-compute
- catalogue-federation
depends_on: [open-table-formats, table-catalogue]
tags: [compute]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sharing one copy of each table between engines, such as a SQL warehouse, a Spark cluster, a streaming engine and a Python notebook, rests on three things: an open table format that every engine can read and write, a shared catalogue that tells each engine where a table's current state is and coordinates commits, and access control that applies whichever engine is used. A streaming job can then write events into an Iceberg table that a BI engine queries and a data scientist reads from Python, all at the same version.

It lets teams pick the right engine for each workload, avoids copying data between systems and lowers dependence on one vendor. In practice support is uneven. Engines differ in which format features and versions they handle, many read more than they can write, and governance set in one engine may not be honoured by another. This concerns tables within one organisation's estate; open-protocol sharing applies similar ideas to external consumers.

# Key considerations

- Test every engine for reads and writes of the features you use, including row-level deletes, schema changes and newer data types.
- Name one catalogue as the authority. Engines committing to the same table through different catalogues will corrupt it.
- Governance must live in the catalogue or storage layer to apply to all engines. Policies defined inside one engine do not follow the data.
- Caches, indexes and materialised views usually belong to one engine. Expect different performance from each engine on the same table.

# Questions to ask

- Which engines need to read and write the same data, and which only read it?
- Where must access policies be enforced so they hold for every engine?
- How much does dependence on one vendor concern the organisation over the next contract cycle?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Query and compute](compute.md) |
| Broader | [Query and compute](compute.md) |
| Related | [Storage and table management](../storage/storage.md), [Specialised data types](../specialised-data/specialised-data.md), [Catalogue federation](../storage/catalogue-federation.md), [Decoupled storage and compute](decoupled-storage-compute.md), [Hybrid and multi-cloud deployment](../platform-operations/deployment-options.md), [Open file formats](../storage/file-formats.md), [Open table formats](../storage/open-table-formats.md), [Open-protocol sharing](../data-sharing/open-protocol-sharing.md), [Platform-managed storage](../storage/managed-storage.md), [Query federation](query-federation.md), [Single-node processing](../processing/single-node-processing.md), [Storage credential vending](../storage/credential-vending.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md), [Table catalogue](../storage/table-catalogue.md), [Table format conversion](../storage/table-format-conversion.md) |
| Depends on | [Open table formats](../storage/open-table-formats.md), [Table catalogue](../storage/table-catalogue.md) |

# Where it appears

- **Patterns:** [Lakehouse](../../patterns/lakehouse.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Compute and workload management](../../maturity/track-compute.md) (from level 3, Defined)
- **Frameworks:** [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VI – Switching between data processing services · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Infrastructures & Servers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift Spectrum](../../technologies/aws/aws-redshift-spectrum.md), [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md), [Lakehouse architecture of Amazon SageMaker](../../technologies/aws/aws-sagemaker-lakehouse.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Mirrored Azure Databricks Catalog](../../technologies/microsoft/fabric-mirrored-azure-databricks-catalog.md), [OneLake](../../technologies/microsoft/fabric-onelake.md), [OneLake shortcuts](../../technologies/microsoft/fabric-onelake-shortcuts.md), [OneLake table format virtualization (Delta Lake and Apache Iceberg)](../../technologies/microsoft/fabric-onelake-table-format-virtualisation.md) (unconfirmed), [Power BI Direct Lake](../../technologies/microsoft/powerbi-direct-lake.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Lakehouse Iceberg REST catalog | [BigQuery tables for Apache Iceberg](../../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md), [Google Cloud Lakehouse](../../technologies/google-cloud/gcp-lakehouse.md), [Google Cloud Lakehouse runtime catalog](../../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md), [pg_lake](../../technologies/snowflake/snowflake-pg-lake.md) (preview), [Snowflake catalog-linked databases](../../technologies/snowflake/snowflake-catalog-linked-databases.md), [Snowflake Horizon Iceberg REST Catalog API](../../technologies/snowflake/snowflake-horizon-iceberg-rest-catalog.md), [Snowflake Open Data Sharing](../../technologies/snowflake/snowflake-open-data-sharing.md) (preview), [Snowflake Open Catalog](../../technologies/snowflake/snowflake-open-catalog.md) (deprecated) |
| [Databricks](../../platforms/platform-databricks.md) | Iceberg reads (UniForm) and the Iceberg REST Catalog API | [Databricks catalog federation](../../technologies/databricks/databricks-catalog-federation.md), [Databricks Iceberg reads (UniForm)](../../technologies/databricks/databricks-iceberg-reads-uniform.md), [Unity Catalog Iceberg REST Catalog API](../../technologies/databricks/databricks-iceberg-rest-catalog.md), [Unity Catalog managed Iceberg tables](../../technologies/databricks/databricks-managed-iceberg-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../../technologies/clickhouse/clickhouse-data-lake.md), [ClickHouse DataLakeCatalog database engine](../../technologies/clickhouse/clickhouse-datalakecatalog.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Iceberg REST Catalog](../../technologies/cloudera/cloudera-iceberg-rest-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Lakehouse](../../technologies/oracle/oracle-autonomous-ai-lakehouse.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud Connect](../../technologies/sap/sap-bdc-connect.md), [SAP Snowflake](../../technologies/sap/sap-snowflake.md) (unconfirmed; distribution of Snowflake) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Fabric](../../technologies/teradata/teradata-fabric.md), [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../../technologies/teradata/teradata-open-table-format.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Iceberg tables in Palantir Foundry](../../technologies/palantir/palantir-iceberg-tables.md) (preview) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku connections](../../technologies/dataiku/dataiku-connections.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Arrow](../../technologies/open-source/apache-arrow.md), [Apache Polaris](../../technologies/open-source/apache-polaris.md), [Apache XTable (incubating)](../../technologies/open-source/apache-xtable.md) (preview), [Iceberg REST Catalog specification](../../technologies/open-source/apache-iceberg-rest-catalog-spec.md), [Trino](../../technologies/open-source/trino.md), [Unity Catalog (open source)](../../technologies/open-source/unity-catalog.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Managed Data Lake Service](../../technologies/independent/fivetran-managed-data-lake-service.md), [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md) |
