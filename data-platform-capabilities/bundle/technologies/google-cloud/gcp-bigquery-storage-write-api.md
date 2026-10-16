---
type: Technology
id: gcp-bigquery-storage-write-api
title: BigQuery Storage Write API
description: High-throughput API for streaming or batch-committing rows into BigQuery tables with exactly-once semantics, readable within seconds.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [streaming-ingestion, batch-ingestion, idempotent-loading]
resource: https://docs.cloud.google.com/bigquery/docs/write-api
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In July 2026 Google renamed the legacy tabledata.insertAll streaming method "Storage Write API (REST)" and the gRPC interface "Storage Write API (gRPC)". The gRPC path is the one used for CDC upserts and for writing to Iceberg managed tables (preview).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md) (Ingestion and integration): Load data from sources on a schedule or on demand, in bulk or incrementally.
- [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) (Ingestion and integration): Make loads safe to retry or replay by removing duplicates on write so nothing is counted twice.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Event Hubs](../microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md), [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md), [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM StreamSets](../ibm/ibm-streamsets.md), [Confluent Cloud](../ibm/confluent-cloud.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Batch ingestion](../../capabilities/ingestion-integration/batch-ingestion.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md), [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Estuary](../independent/estuary.md), [Imply Polaris](../independent/imply-polaris.md), [Striim Cloud](../independent/striim-cloud.md) | [Deduplication and idempotent loading](../../capabilities/ingestion-integration/idempotent-loading.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
