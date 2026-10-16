---
type: Technology
id: databricks-zerobus-ingest
title: Zerobus Ingest
description: A serverless push API that writes records straight into Unity Catalog Delta tables. Clients can use gRPC SDKs, REST, OpenTelemetry (OTLP), MQTT or Kafka-compatible producers, and no message broker is needed.
aliases: [Zerobus]
platform: platform-databricks
kind: managed-service
availability: ga
realises: [streaming-ingestion, iot-ingestion]
resource: https://docs.databricks.com/aws/en/ingestion/zerobus-overview
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It is documented under Lakeflow Connect as "direct write" and bills under Lakeflow Connect. Ingestion into streaming tables became GA in August 2026 and Arrow support in September 2026, and ingestion into default storage is in Public Preview. It is a lakehouse sink, not a general event bus, so it does not replace Kafka for application-to-application streaming.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration): Collect high-volume telemetry securely from devices and edge gateways.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Event Hubs](../microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md), [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [Striim Cloud](../independent/striim-cloud.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
