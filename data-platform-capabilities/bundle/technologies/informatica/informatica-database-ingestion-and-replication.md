---
type: Technology
id: informatica-database-ingestion-and-replication
title: Informatica Database Ingestion and Replication
description: Replicates relational and some non-relational databases to cloud warehouses, lakes, streaming platforms and databases, as an initial bulk load, as continuous log-based change capture, or as both in sequence.
formerly: [Cloud Mass Ingestion Databases, Mass Ingestion Databases]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [change-data-capture, database-replication, database-extraction, mainframe-integration]
resource: https://onlinehelp.informatica.com/IICS/prod/CDI/en/cc-cloud-dbi_intro/Introducing_Data_Ingestion_and_Replication.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Propagates DML and schema changes in near real time. It is one task type of the Data Ingestion and Replication service, which the IDMC menu still labels "Mass Ingestion". In 2026, CDC targets were extended to Microsoft Fabric Data Warehouse.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Mainframe data integration](../../capabilities/ingestion-integration/mainframe-integration.md) (Ingestion and integration): Capture and offload data from mainframe databases and files with minimal load on the host.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Data Ingestion and Replication

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Copy job](../microsoft/fabric-copy-job.md), [Fabric Eventstream](../microsoft/fabric-eventstream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Mainframe data integration](../../capabilities/ingestion-integration/mainframe-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md), [Airbyte](../open-source/airbyte.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Replicate](../independent/qlik-replicate.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md), [Fivetran HVR](../independent/fivetran-hvr.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Mainframe data integration](../../capabilities/ingestion-integration/mainframe-integration.md) |
