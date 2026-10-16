---
type: Technology
id: snowflake-snowpipe-streaming
title: Snowpipe Streaming
description: Ingests rows directly into tables through SDKs (Java, Python, Node.js) or a REST API, with no files, making data queryable within seconds.
platform: platform-snowflake
kind: feature
availability: ga
realises: [streaming-ingestion, iot-ingestion, idempotent-loading]
resource: https://docs.snowflake.com/en/user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The high-performance architecture (up to 20 GB/s per table, about 5 seconds to queryable) is recommended for new work. Elastic Channels became GA in September 2026, and Snowpipe Streaming can also write to Iceberg tables. The classic architecture is still supported but planned for deprecation, with an 18-month migration window after the announcement.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration): Collect high-volume telemetry securely from devices and edge gateways.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowpipe

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Event Hubs](../microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md), [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md), [Imply Polaris](../independent/imply-polaris.md), [Striim Cloud](../independent/striim-cloud.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
