---
type: Capability
id: change-data-capture
title: Change data capture
description: Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
aliases: [CDC, log-based replication]
broader: [ingestion-integration]
related: [database-replication, event-streaming, change-feeds, mainframe-integration, idempotent-loading]
depends_on: [row-level-updates]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Databases write every committed change to a transaction log (called a write-ahead, redo or binary log depending on the engine) before applying it. A CDC process reads that log and turns each insert, update and delete into an event with the row's key, its new values, often its old values, the operation type and the commit position. When a customer changes their address, the event arrives downstream within seconds and a merge step updates the platform's copy, including deletes that query-based extraction would miss.

CDC is the standard way to keep analytical copies of operational data fresh without query load on the source, and it preserves every intermediate change for history tables and audit. Log-based capture is preferred. Trigger-based capture writes changes to shadow tables and slows every transaction, and timestamp queries are really incremental extraction. Database replication packages capture and apply into one managed service; raw CDC often feeds an event stream read by several consumers. Debezium is a widely used open-source example.

# Key considerations

- The initial snapshot and the start of log reading must line up exactly, or changes are lost or applied twice. Check how this works for large tables.
- Source log retention limits how long CDC can be stopped before a full resnapshot is needed. Agree retention with the database team.
- Source schema changes must flow through or be handled deliberately, or the apply step fails.
- Apply changes in commit order for each key. Parallel apply that reorders updates to the same row gives wrong results.
- Log access needs elevated privileges and sometimes configuration changes, such as enabling full row logging, that need approval from source owners.

# Questions to ask

- Which source databases and versions are involved, and will their owners grant log access?
- How fresh must the analytical copy be, and is every intermediate change needed or only current state?
- How long are transaction logs kept on each source?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Related | [ACID transactions](../storage/acid-transactions.md), [Batch ingestion](batch-ingestion.md), [Change feeds](../serving/change-feeds.md), [Consent and purpose management](../governance/consent-management.md), [Database extraction](database-extraction.md), [Database replication and mirroring](database-replication.md), [Deduplication and idempotent loading](idempotent-loading.md), [Event streaming](event-streaming.md), [Incremental processing](../processing/incremental-processing.md), [Mainframe data integration](mainframe-integration.md), [Operational data store](../serving/operational-data-store.md), [Row-level updates and deletes](../storage/row-level-updates.md), [Stream processing](../processing/stream-processing.md), [Streaming SQL](../processing/streaming-sql.md) |
| Depends on | [Row-level updates and deletes](../storage/row-level-updates.md) |
| Needed by | [Database migration](../platform-operations/database-migration.md), [Database replication and mirroring](database-replication.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 2) · [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 2) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 2) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3)
- **Patterns:** [Separate read models](../../patterns/cqrs-read-models.md) · [ELT](../../patterns/elt.md) · [Slowly changing dimensions](../../patterns/slowly-changing-dimensions.md) · [Transactional outbox](../../patterns/transactional-outbox.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md) · [Data engineer](../../personas/persona-data-engineer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 2, Managed) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Integration and Interoperability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS DMS ongoing replication | [AWS Database Migration Service](../../technologies/aws/aws-dms.md), [AWS zero-ETL integrations](../../technologies/aws/aws-zero-etl-integrations.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Copy job](../../technologies/microsoft/fabric-copy-job.md), [Fabric Eventstream](../../technologies/microsoft/fabric-eventstream.md), [Mirroring in Microsoft Fabric](../../technologies/microsoft/fabric-mirroring.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Datastream; BigQuery CDC upserts | [BigQuery change data capture](../../technologies/google-cloud/gcp-bigquery-cdc.md), [Datastream](../../technologies/google-cloud/gcp-datastream.md), [Google Cloud Database Migration Service](../../technologies/google-cloud/gcp-database-migration-service.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Openflow CDC connectors; data mirroring (Snowflake Postgres) | [Data mirroring for Snowflake Postgres](../../technologies/snowflake/snowflake-postgres-data-mirroring.md), [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickPipes CDC (PeerDB) | [ClickHouse Managed Postgres](../../technologies/clickhouse/clickhouse-managed-postgres.md) (preview), [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../../technologies/clickhouse/clickhouse-clickpipes-cdc.md) |
| [Informatica](../../platforms/platform-informatica.md) | incremental load in Database Ingestion and Replication | [Informatica Application Ingestion and Replication](../../technologies/informatica/informatica-application-ingestion-and-replication.md), [Informatica Database Ingestion and Replication](../../technologies/informatica/informatica-database-ingestion-and-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) | GoldenGate | [Oracle GoldenGate](../../technologies/oracle/oracle-goldengate.md) |
| [SAP](../../platforms/platform-sap.md) | Replication flows | [SAP Datasphere replication flows](../../technologies/sap/sap-datasphere-replication-flows.md), [SAP Landscape Transformation Replication Server](../../technologies/sap/sap-landscape-transformation.md) |
| [IBM](../../platforms/platform-ibm.md) | Data Replication | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md), [IBM Data Replication](../../technologies/ibm/ibm-data-replication.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md), [Debezium](../../technologies/open-source/debezium.md), [Flink CDC](../../technologies/open-source/apache-flink-cdc.md), [PostgreSQL](../../technologies/open-source/postgresql.md), [RisingWave](../../technologies/open-source/risingwave.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Boomi Data Integration](../../technologies/independent/boomi-data-integration.md), [Estuary](../../technologies/independent/estuary.md), [Fivetran](../../technologies/independent/fivetran.md), [Fivetran HVR](../../technologies/independent/fivetran-hvr.md), [Qlik Replicate](../../technologies/independent/qlik-replicate.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md), [Striim Cloud](../../technologies/independent/striim-cloud.md) |
