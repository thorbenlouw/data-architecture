---
type: Technology
id: ibm-streamsets
title: IBM StreamSets
description: Low-code streaming and batch ingestion tool whose pipelines detect and adapt to schema drift, deployable as SaaS or in the customer's cloud or data centre.
aliases: [StreamSets]
platform: platform-ibm
kind: software
availability: ga
realises: [streaming-ingestion, schema-evolution, custom-connectors, hybrid-data-plane]
resource: https://www.ibm.com/products/streamsets
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Acquired from Software AG in 2024; still sold under its own name but delivered as the streaming capability within watsonx.data integration. A Python SDK supports pipelines as code.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) (Ingestion and integration) (primary): Load continuous event streams from brokers, applications or devices into the platform with seconds-level latency.
- [Schema enforcement and evolution](../../capabilities/storage/schema-evolution.md) (Storage and table management): Reject data that does not match a table's schema, and change schemas safely over time.
- [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md) (Ingestion and integration): Build and run connectors for sources with no prebuilt option, using an SDK or framework.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** IBM watsonx.data integration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift streaming ingestion](../aws/aws-redshift-streaming-ingestion.md), [Amazon Data Firehose](../aws/aws-data-firehose.md), [Amazon Kinesis Data Streams](../aws/aws-kinesis-data-streams.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md), [Azure Event Hubs](../microsoft/azure-event-hubs.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Storage Write API](../google-cloud/gcp-bigquery-storage-write-api.md), [Google Cloud Managed Service for Apache Kafka](../google-cloud/gcp-managed-kafka.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md), [Snowflake Connector for Kafka](../snowflake/snowflake-connector-for-kafka.md), [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Kafka table engine](../clickhouse/clickhouse-kafka-engine.md), [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Streaming with Apache Kafka](../oracle/oracle-oci-streaming-kafka.md), [Oracle GoldenGate](../oracle/oracle-goldengate.md) | [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md), [Apache Pulsar](../open-source/apache-pulsar.md), [Apache Paimon](../open-source/apache-paimon.md) | [Custom connector development](../../capabilities/ingestion-integration/custom-connectors.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Estuary](../independent/estuary.md), [Imply Polaris](../independent/imply-polaris.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Streaming ingestion](../../capabilities/ingestion-integration/streaming-ingestion.md) |
