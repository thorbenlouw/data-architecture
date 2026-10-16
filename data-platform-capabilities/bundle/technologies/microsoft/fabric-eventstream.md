---
type: Technology
id: fabric-eventstream
title: Fabric Eventstream
description: No-code capture, transformation and routing of event streams from Event Hubs, Kafka, IoT Hub, database CDC and other sources into Fabric destinations.
platform: platform-microsoft
kind: feature
availability: ga
realises: [streaming-ingestion, streaming-sql, change-data-capture, stream-to-table]
resource: https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Real-Time Intelligence (formerly Synapse Real-Time Analytics plus Data Activator). The SQL operator became GA in March 2026; DeltaFlow and Oracle CDC are preview. Exposes a Kafka-compatible custom endpoint, so it overlaps with Azure Event Hubs for Fabric-centric designs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Streaming SQL](../../capabilities/processing/streaming-sql.md) (Processing and transformation): Express continuous transformations and incrementally maintained views over streams in SQL.
- [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) (Ingestion and integration): Capture inserts, updates and deletes from source databases, usually from transaction logs, and apply them downstream with low latency.
- [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) (Ingestion and integration): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Fabric Real-Time Intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md), [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle GoldenGate](../oracle/oracle-goldengate.md), [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Striim Cloud](../independent/striim-cloud.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Estuary](../independent/estuary.md) | [Change data capture](../../capabilities/ingestion-integration/change-data-capture.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Streaming SQL](../../capabilities/processing/streaming-sql.md), [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
