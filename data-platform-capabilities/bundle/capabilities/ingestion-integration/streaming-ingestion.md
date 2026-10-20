---
type: Capability
id: streaming-ingestion
title: Streaming ingestion
description: Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
aliases: [real-time ingestion, event ingestion]
broader: [ingestion-integration]
related: [event-streaming, stream-processing, table-maintenance, idempotent-loading, freshness-monitoring]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A streaming loader reads events continuously from a broker, an HTTP endpoint or a device gateway and writes them into tables within seconds of arrival. One subscribed to an orders topic might write a small batch every few seconds, commit its topic offsets only after the table write succeeds, and map each event's fields to table columns. Some platforms accept rows directly over a streaming API, with no broker in between.

It matters when consumers need data within seconds or minutes, such as operational dashboards, fraud features and stock levels. It brings costs batch does not have: always-on compute, many small files that need compaction, and harder failure handling. Approaches range from micro-batch loaders, through continuous row-level writes, to services that expose topics as tables directly. Stream processing differs: it transforms and aggregates events in flight, while streaming ingestion lands them with light changes only.

# Key considerations

- Commit source offsets and table writes together, or deduplicate on a key, to avoid loss or duplication after a restart.
- Frequent small commits create many small files. Schedule compaction, or query performance degrades within days.
- Decide what happens to events that fail parsing or schema checks: block the stream, drop them or send them to a dead-letter topic.
- Latency targets drive cost. A one-minute target can often use cheaper micro-batching than a one-second target.

# Questions to ask

- What end-to-end latency do consumers need, and what would they do differently with fresher data?
- What are the peak and average event rates, and how bursty is traffic?
- Must late or out-of-order events correct tables that have already been published?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Ingestion and integration](ingestion-integration.md) |
| Narrower | [Behavioural event collection](behavioural-event-collection.md), [IoT and telemetry ingestion](iot-ingestion.md), [Stream-to-table materialisation](stream-to-table.md) |
| Related | [Deduplication and idempotent loading](idempotent-loading.md), [Event streaming](event-streaming.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Real-time analytical database](../compute/real-time-analytics.md), [Stream processing](../processing/stream-processing.md), [Table maintenance and optimisation](../storage/table-maintenance.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (requires, level 2) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (requires, level 2) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Patterns:** [Lambda architecture](../../patterns/lambda-architecture.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 2, Managed)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Data Firehose; Redshift streaming ingestion | [Amazon Data Firehose](../../technologies/aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../../technologies/aws/aws-kinesis-data-streams.md), [Amazon OpenSearch Service](../../technologies/aws/aws-opensearch-service.md), [Amazon Redshift streaming ingestion](../../technologies/aws/aws-redshift-streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Event Hubs](../../technologies/microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../../technologies/microsoft/fabric-eventhouse.md), [Fabric Eventstream](../../technologies/microsoft/fabric-eventstream.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Pub/Sub BigQuery subscriptions; Storage Write API | [BigQuery Storage Write API](../../technologies/google-cloud/gcp-bigquery-storage-write-api.md), [Dataflow templates](../../technologies/google-cloud/gcp-dataflow-templates.md), [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md), [Google Cloud Managed Service for Apache Kafka](../../technologies/google-cloud/gcp-managed-kafka.md), [Google Cloud Pub/Sub](../../technologies/google-cloud/gcp-pubsub.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Snowpipe Streaming | [Snowflake Connector for Kafka](../../technologies/snowflake/snowflake-connector-for-kafka.md), [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md), [Snowpipe Streaming](../../technologies/snowflake/snowflake-snowpipe-streaming.md) |
| [Databricks](../../platforms/platform-databricks.md) | Zerobus Ingest | [Zerobus Ingest](../../technologies/databricks/databricks-zerobus-ingest.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | ClickPipes and the Kafka table engine | [ClickHouse Kafka table engine](../../technologies/clickhouse/clickhouse-kafka-engine.md), [ClickPipes](../../technologies/clickhouse/clickhouse-clickpipes.md) |
| [Informatica](../../platforms/platform-informatica.md) | Streaming Ingestion and Replication | [Informatica Streaming Ingestion and Replication](../../technologies/informatica/informatica-streaming-ingestion-and-replication.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Streaming with Apache Kafka](../../technologies/oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../../technologies/oracle/oracle-goldengate.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud](../../technologies/ibm/confluent-cloud.md), [IBM StreamSets](../../technologies/ibm/ibm-streamsets.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Druid](../../technologies/open-source/apache-druid.md), [Apache Paimon](../../technologies/open-source/apache-paimon.md), [Apache Pinot](../../technologies/open-source/apache-pinot.md), [Apache Pulsar](../../technologies/open-source/apache-pulsar.md), [Kafka Connect](../../technologies/open-source/apache-kafka-connect.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Estuary](../../technologies/independent/estuary.md), [Imply Polaris](../../technologies/independent/imply-polaris.md), [Qlik Open Lakehouse](../../technologies/independent/qlik-open-lakehouse.md), [Striim Cloud](../../technologies/independent/striim-cloud.md), [Tinybird](../../technologies/independent/tinybird.md) |

Narrower capabilities are realised by a further 22 technologies; see their pages.
