---
type: Technology
id: oracle-goldengate
title: Oracle GoldenGate
description: Log-based change data capture and replication between databases, and from databases to Kafka, cloud warehouses and Iceberg tables, available as software and as the managed OCI GoldenGate.
aliases: [OCI GoldenGate]
platform: platform-oracle
kind: software
availability: ga
realises:
- change-data-capture
- database-replication
- streaming-ingestion
- stream-processing
- database-migration
resource: https://blogs.oracle.com/dataintegration/announcing-oracle-goldengate-for-distributed-applications-and-analytics-26ai-general-availability
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Current line is GoldenGate 26ai; GoldenGate for Distributed Applications and Analytics 26ai (GA February 2026) replicates into Iceberg on S3-compatible storage with REST catalogues, Amazon S3 Tables and BigQuery. GoldenGate Stream Analytics adds continuous processing in OCI GoldenGate. Often used for zero-downtime migrations and active-active replication.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration) (primary): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) (Ingestion and integration): Replicate operational databases continuously into the analytical platform without building pipelines.
- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Database migration](../../capabilities/platform-operations/database-migration.md) (Platform operations): Move databases to new engines or platforms, converting schemas and keeping data in sync until cut-over.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [AWS zero-ETL integrations](../aws/aws-zero-etl-integrations.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database migration](../../capabilities/platform-operations/database-migration.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Mirroring in Microsoft Fabric](../microsoft/fabric-mirroring.md), [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Fabric Copy job](../microsoft/fabric-copy-job.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Datastream](../google-cloud/gcp-datastream.md), [Google Cloud Database Migration Service](../google-cloud/gcp-database-migration-service.md), [BigQuery change data capture](../google-cloud/gcp-bigquery-cdc.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Database migration](../../capabilities/platform-operations/database-migration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md), [Data mirroring for Snowflake Postgres](../snowflake/snowflake-postgres-data-mirroring.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md), [ClickHouse Managed Postgres](../clickhouse/clickhouse-managed-postgres.md) (preview) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Application Ingestion and Replication](../informatica/informatica-application-ingestion-and-replication.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Landscape Transformation Replication Server](../sap/sap-landscape-transformation.md), [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Replication](../ibm/ibm-data-replication.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Debezium](../open-source/debezium.md), [Flink CDC](../open-source/apache-flink-cdc.md), [RisingWave](../open-source/risingwave.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Striim Cloud](../independent/striim-cloud.md), [Estuary](../independent/estuary.md), [Fivetran HVR](../independent/fivetran-hvr.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Database replication and mirroring](../../capabilities/ingestion-integration/database-replication.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
