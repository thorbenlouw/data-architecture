---
type: Capability
id: open-table-formats
title: Open table formats
description: Manage collections of files as transactional tables with a defined schema, history and metadata.
aliases: [lakehouse tables, Iceberg, Delta Lake, Hudi]
broader: [storage]
related: [engine-interoperability, table-catalogue, change-feeds, decoupled-storage-compute, managed-storage]
depends_on: [object-storage, file-formats]
tags: [storage]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A table format adds a metadata layer over data files in object storage. Each commit writes a new snapshot listing exactly which data files belong to the table, with the schema, partition layout and per-file statistics. Readers start from the current snapshot instead of listing directories, so they see a consistent table even while writers add files. Apache Iceberg, Delta Lake and Apache Hudi are the main open specifications. They differ in metadata layout and features, but each turns a folder of Parquet files into a table with transactions, history and a schema.

This is what makes a lakehouse possible: warehouse-style tables, with updates, deletes and concurrent writers, kept in open files that several engines can use. It replaces Hive-style tables, which defined a table as a directory and offered no atomic commits or reliable schema changes. Which format you pick matters less than it did, because engines increasingly support more than one and conversion tools exist, but the catalogue and maintenance approach still need deciding.

# Key considerations

- Check write support, not only read support, for each engine. Many engines read every format but write only one well.
- Feature support varies by format version and engine. Deletion vectors, row lineage, variant types and multi-table transactions arrive at different times in different engines.
- Concurrent writers need a catalogue or storage layer with atomic commits. Test conflict behaviour with real write patterns.
- Tables do not maintain themselves. Snapshots, small files and orphaned files pile up unless maintenance runs.
- Metadata can grow large for tables with millions of files or very frequent commits, which slows query planning.

# Questions to ask

- Which engines must write to these tables, not only read them?
- How many concurrent writers and commits per hour will the busiest tables see?
- Is there an existing investment in one format, or a main platform that favours one?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Storage and table management](storage.md) |
| Broader | [Storage and table management](storage.md) |
| Narrower | [ACID transactions](acid-transactions.md), [Partitioning and clustering](partitioning-clustering.md), [Row-level updates and deletes](row-level-updates.md), [Schema enforcement and evolution](schema-evolution.md), [Table format conversion](table-format-conversion.md), [Table maintenance and optimisation](table-maintenance.md) |
| Related | [Specialised data types](../specialised-data/specialised-data.md), [Change feeds](../serving/change-feeds.md), [Decoupled storage and compute](../compute/decoupled-storage-compute.md), [Hybrid and multi-cloud deployment](../platform-operations/deployment-options.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Offline feature store](../machine-learning/offline-feature-store.md), [Platform-managed storage](managed-storage.md), [Table catalogue](table-catalogue.md) |
| Depends on | [Object storage](object-storage.md), [Open file formats](file-formats.md) |
| Needed by | [Multi-engine interoperability](../compute/engine-interoperability.md), [Open-protocol sharing](../data-sharing/open-protocol-sharing.md), [Stream-to-table materialisation](../ingestion-integration/stream-to-table.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Patterns:** [Lakehouse](../../patterns/lakehouse.md) · [Medallion architecture](../../patterns/medallion-architecture.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Storage and table management](../../maturity/track-storage.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Storage and Operations · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter V, Section I – ICT third-party risk management (Articles 28 to 30) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VI – Switching between data processing services

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | S3 Tables (Apache Iceberg table buckets) | [Amazon S3 Tables](../../technologies/aws/aws-s3-tables.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Lakehouse](../../technologies/microsoft/fabric-lakehouse.md), [OneLake](../../technologies/microsoft/fabric-onelake.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | BigQuery tables for Apache Iceberg / Iceberg managed tables | [BigQuery tables for Apache Iceberg](../../technologies/google-cloud/gcp-bigquery-iceberg-managed-tables.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Apache Iceberg tables in Snowflake](../../technologies/snowflake/snowflake-iceberg-tables.md), [pg_lake](../../technologies/snowflake/snowflake-pg-lake.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Delta Lake on Databricks](../../technologies/databricks/databricks-delta-lake.md), [Unity Catalog managed Iceberg tables](../../technologies/databricks/databricks-managed-iceberg-tables.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../../technologies/clickhouse/clickhouse-data-lake.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Apache Iceberg in Cloudera](../../technologies/cloudera/cloudera-lakehouse-iceberg.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Lakehouse](../../technologies/oracle/oracle-autonomous-ai-lakehouse.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Open Table Format support (Apache Iceberg and Delta Lake)](../../technologies/teradata/teradata-open-table-format.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Netezza Performance Server](../../technologies/ibm/ibm-netezza.md), [IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Iceberg tables in Palantir Foundry](../../technologies/palantir/palantir-iceberg-tables.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Hudi](../../technologies/open-source/apache-hudi.md), [Apache Iceberg](../../technologies/open-source/apache-iceberg.md), [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Delta Lake](../../technologies/open-source/delta-lake.md), [DuckLake](../../technologies/open-source/ducklake.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran Managed Data Lake Service](../../technologies/independent/fivetran-managed-data-lake-service.md), [MotherDuck](../../technologies/independent/motherduck.md), [Qlik Open Lakehouse](../../technologies/independent/qlik-open-lakehouse.md), [Redpanda Cloud](../../technologies/independent/redpanda-cloud.md) |

Narrower capabilities are realised by a further 43 technologies; see their pages.
