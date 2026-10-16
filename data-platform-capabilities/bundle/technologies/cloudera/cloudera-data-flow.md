---
type: Technology
id: cloudera-data-flow
title: Cloudera Data Flow
description: Managed Apache NiFi service for building, deploying and autoscaling flows that collect, route and transform data from files, databases, APIs and streams.
aliases: [CDF]
formerly: [Cloudera DataFlow, Cloudera DataFlow for the Public Cloud, Hortonworks DataFlow, HDF]
platform: platform-cloudera
kind: managed-service
availability: ga
realises:
- streaming-ingestion
- file-ingestion
- low-code-transformation
- api-ingestion
- database-extraction
- edge-data-processing
resource: https://docs.cloudera.com/dataflow/cloud/index.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes a no-code Flow Designer, a catalogue of prebuilt ReadyFlows, and Cloudera Data Flow Functions, which run NiFi flows serverlessly on AWS Lambda, Azure Functions or Google Cloud Functions. Supports NiFi 1.x and 2.x. Edge collection uses Cloudera Edge Management (MiNiFi) for IoT devices.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md) (Ingestion and integration): Detect and load files arriving in landing storage, processing each file exactly once.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [API ingestion](../../capabilities/ingestion-integration/api-ingestion.md) (Ingestion and integration): Collect data from REST, GraphQL or SOAP APIs, handling pagination, authentication and rate limits.
- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Edge data processing](../../capabilities/processing/edge-data-processing.md) (Processing and transformation): Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Event Hubs](../microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md), [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md), [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md) | [File ingestion](../../capabilities/ingestion-integration/file-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [Striim Cloud](../independent/striim-cloud.md), [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
