---
type: Capability
id: database-extraction
title: Database extraction
description: Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
aliases: [JDBC extract, high-watermark extraction]
broader: [batch-ingestion]
related: [change-data-capture, database-replication, data-reconciliation, mainframe-integration]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Extraction reads a source database with SQL queries, bulk export utilities or snapshot features and writes the result to the platform. A typical job runs `SELECT ... FROM orders WHERE updated_at > :last_run` against a read replica, splits large tables into primary-key ranges so they can be read in parallel, and lands the output as files or tables. For document and key-value stores the equivalent is a collection scan or an export API.

It is the simplest way to bring operational data into analytics and needs no access to transaction logs. The costs are load on the source, missed hard deletes and data only as fresh as the last run. Change data capture reads the transaction log instead, sees every change including deletes, and puts far less load on the source. Extraction remains the right tool for initial loads, for sources where log access is refused, and for small reference tables that are cheap to copy in full.

# Key considerations

- Extract from read replicas or snapshots where possible. Long queries on a primary can hold locks or bloat its undo logs.
- Detect hard deletes separately, for example by periodic comparison of key lists, if incremental queries cannot see them.
- Map data types with care. Timestamps without time zones, high-precision decimals and character encodings are common sources of silent corruption.
- Extract related tables from a consistent snapshot, or totals across them will not reconcile.

# Questions to ask

- Can the source team provide a replica, a snapshot or a scheduled export instead of queries on production?
- Do the important tables have reliable last-modified columns?
- Do deletes in the source matter to downstream consumers?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Batch ingestion](batch-ingestion.md) |
| Related | [Change data capture](change-data-capture.md), [Data reconciliation](../data-quality/data-reconciliation.md), [Database replication and mirroring](database-replication.md), [Mainframe data integration](mainframe-integration.md) |

# Where it appears

- **Patterns:** [ETL](../../patterns/etl.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 1, Initial)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Database Migration Service](../../technologies/aws/aws-dms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Fabric Copy job](../../technologies/microsoft/fabric-copy-job.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Data Transfer Service](../../technologies/google-cloud/gcp-bigquery-data-transfer-service.md), [Cloud Data Fusion](../../technologies/google-cloud/gcp-data-fusion.md), [Dataflow templates](../../technologies/google-cloud/gcp-dataflow-templates.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Connect](../../technologies/databricks/databricks-lakeflow-connect.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse integration table engines and table functions](../../technologies/clickhouse/clickhouse-integration-engines.md), [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../../technologies/clickhouse/clickhouse-clickpipes-cdc.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Integration (CDI)](../../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Database Ingestion and Replication](../../technologies/informatica/informatica-database-ingestion-and-replication.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Integration](../../technologies/oracle/oracle-oci-data-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [SAS](../../platforms/platform-sas.md) | SAS/ACCESS engines | [SAS Data Hub](../../technologies/sas/sas-data-hub.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku connections](../../technologies/dataiku/dataiku-connections.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Airbyte](../../technologies/open-source/airbyte.md), [dlt (data load tool)](../../technologies/open-source/dlt.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Fivetran](../../technologies/independent/fivetran.md) |
