---
type: Capability
id: database-replication
title: Database replication and mirroring
description: Replicate operational databases continuously into the analytical platform without building pipelines.
aliases: [zero-ETL, mirroring, managed replication]
broader: [ingestion-integration]
related: [operational-database, database-extraction, freshness-monitoring, database-migration]
depends_on: [change-data-capture]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A replication service connects to an operational database, copies the selected tables once and then applies every later change, usually read from the transaction log, to matching tables in the analytical platform. Configuration replaces pipeline code: choose a source, pick schemas or tables, and the copies stay within seconds or minutes of the source, often including schema changes. Mirroring is a variant in which the platform keeps a read-only replica that its engines query directly.

It is the quickest route to current operational data for analytics, and it avoids building and running separate capture, transport and merge components. The cost is less control: limited filtering and transformation in flight, fixed target layouts, and dependence on which source engines and versions are supported. Change data capture is the underlying technique; replication is the packaged, end-to-end form. Operational database integration is different again: it runs transactional databases alongside the platform rather than copying external ones into it.

# Key considerations

- Check source support precisely, including versions, managed-database variants and data types such as large objects and spatial columns.
- Replicated tables keep the source's transactional design. Plan the modelling layer that turns them into analytical structures.
- Monitor replication lag and alert on it. A stalled replica looks healthy until someone notices the data is days old.
- Agree how source schema changes are handled, especially dropped or renamed columns that downstream models use.

# Questions to ask

- Which operational databases must be available for analysis, and how fresh must they be?
- Is a straight copy enough, or must data be filtered or masked before it lands?
- Who will own replication health and the relationship with each source's database team?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [Change data capture](change-data-capture.md), [Database extraction](database-extraction.md), [Database migration](../platform-operations/database-migration.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Operational database integration](../serving/operational-database.md), [Query federation](../compute/query-federation.md), [Vendor-supplied application data products](../data-products/application-data-products.md) |
| Depends on | [Change data capture](change-data-capture.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Patterns:** [ELT](../../patterns/elt.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | zero-ETL integrations | [AWS zero-ETL integrations](../../technologies/aws/aws-zero-etl-integrations.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Mirroring | [Fabric open mirroring](../../technologies/microsoft/fabric-open-mirroring.md), [Mirroring in Microsoft Fabric](../../technologies/microsoft/fabric-mirroring.md), [SQL database in Microsoft Fabric](../../technologies/microsoft/fabric-sql-database.md), [Azure Synapse Link for Azure Cosmos DB](../../technologies/microsoft/azure-synapse-link-cosmos-db.md) (deprecated) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Datastream](../../technologies/google-cloud/gcp-datastream.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Data mirroring for Snowflake Postgres](../../technologies/snowflake/snowflake-postgres-data-mirroring.md), [Snowflake native connectors (Snowflake Connectors for ServiceNow, Google Analytics, SharePoint, PostgreSQL and MySQL)](../../technologies/snowflake/snowflake-native-connectors.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../../technologies/clickhouse/clickhouse-clickpipes-cdc.md) |
| [Informatica](../../platforms/platform-informatica.md) | Database Ingestion and Replication (formerly Mass Ingestion) | [Informatica Database Ingestion and Replication](../../technologies/informatica/informatica-database-ingestion-and-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle GoldenGate](../../technologies/oracle/oracle-goldengate.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere replication flows](../../technologies/sap/sap-datasphere-replication-flows.md), [SAP Landscape Transformation Replication Server](../../technologies/sap/sap-landscape-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Data Replication](../../technologies/ibm/ibm-data-replication.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Debezium](../../technologies/open-source/debezium.md), [Flink CDC](../../technologies/open-source/apache-flink-cdc.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran HVR](../../technologies/independent/fivetran-hvr.md), [Qlik Replicate](../../technologies/independent/qlik-replicate.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md), [Striim Cloud](../../technologies/independent/striim-cloud.md) |
