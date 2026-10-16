---
type: Technology
id: sap-landscape-transformation
title: SAP Landscape Transformation Replication Server
description: Trigger-based replication server that captures changes from SAP ABAP systems and other databases and applies them in near real time to HANA or other targets.
aliases: [SLT, SAP SLT, SAP LT Replication Server]
platform: platform-sap
kind: software
availability: ga
realises: [change-data-capture, database-replication]
resource: https://help.sap.com/docs/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Widely deployed for feeding HANA sidecars and BW; Datasphere replication flows now cover many of the same scenarios in the cloud.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md), [AWS Database Migration Service](../aws/aws-dms.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Copy job](../microsoft/fabric-copy-job.md), [Fabric Eventstream](../microsoft/fabric-eventstream.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md), [RisingWave](../open-source/risingwave.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran HVR](../independent/fivetran-hvr.md), [Qlik Replicate](../independent/qlik-replicate.md), [Striim Cloud](../independent/striim-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
