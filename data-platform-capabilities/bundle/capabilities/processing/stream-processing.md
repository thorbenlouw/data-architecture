---
type: Capability
id: stream-processing
title: Stream processing
description: Transform, join and aggregate events continuously as they arrive, keeping state across events.
aliases: [real-time processing, near-real-time processing, streaming ETL, event stream processing, Flink]
broader: [processing]
related: [streaming-ingestion, streaming-inference, change-feeds, real-time-analytics, change-data-capture]
depends_on: [event-streaming]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A stream processor reads events from a log such as Apache Kafka, applies logic to each one as it arrives, and writes results to another stream or a table. Unlike a stateless filter, it keeps state between events, such as running totals per customer or the last known position of each vehicle. Engines such as Apache Flink and Spark Structured Streaming save this state at regular checkpoints, so a failed job can resume without losing or double-counting events.

It is needed when the value of data falls quickly with time: fraud signals, stock levels, operational alerts, live personalisation. The hard parts are state, ordering, late data, joins between streams and exactly-once results end to end. Approaches range from per-event processing with millisecond latency to micro-batches every few seconds, which are simpler but slower. Streaming ingestion, by contrast, moves events into storage with little change, and a real-time analytical database answers ad hoc queries over fresh data rather than running fixed logic.

# Key considerations

- State size drives cost and recovery time. Expire state that is no longer needed and choose a state store that fits the volume.
- Exactly-once results need idempotent or transactional destinations; checkpoints alone do not guarantee them.
- Changing the logic of a running job may mean migrating or rebuilding its state. Plan upgrades and replays from the start.
- Streaming jobs never stop, so they need on-call owners, monitoring of how far consumers lag behind, and spare capacity.

# Questions to ask

- Which decisions lose value if data is minutes or hours old?
- What delay from event to action is actually acceptable?
- Can results tolerate duplicates or approximate counts, or must they be exact?
- Who will operate long-running streaming jobs around the clock?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md) |
| Narrower | [Event-time windowing](event-time-windowing.md), [Streaming SQL](streaming-sql.md) |
| Related | [Change data capture](../ingestion-integration/change-data-capture.md), [Change feeds](../serving/change-feeds.md), [Edge data processing](edge-data-processing.md), [Event streaming](../ingestion-integration/event-streaming.md), [Feature engineering](../machine-learning/feature-engineering.md), [Online feature store](../machine-learning/online-feature-store.md), [Real-time analytical database](../compute/real-time-analytics.md), [Streaming inference](../mlops/streaming-inference.md), [Streaming ingestion](../ingestion-integration/streaming-ingestion.md) |
| Depends on | [Event streaming](../ingestion-integration/event-streaming.md) |
| Needed by | [Streaming inference](../mlops/streaming-inference.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (benefits from) · [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2) · [Personalised recommendations](../../use-cases/usecase-recommendations.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (requires, level 3) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 2)
- **Patterns:** [Kappa architecture](../../patterns/kappa-architecture.md) · [Lambda architecture](../../patterns/lambda-architecture.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined) · [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Managed Service for Apache Flink | [Amazon Managed Service for Apache Flink](../../technologies/aws/aws-managed-flink.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Apache Spark in Microsoft Fabric](../../technologies/microsoft/fabric-spark.md), [Azure IoT Operations](../../technologies/microsoft/azure-iot-operations.md), [Azure Stream Analytics](../../technologies/microsoft/azure-stream-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Dataflow (Apache Beam) | [BigQuery continuous queries](../../technologies/google-cloud/gcp-bigquery-continuous-queries.md), [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Streaming Analytics](../../technologies/cloudera/cloudera-streaming-analytics.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle GoldenGate](../../technologies/oracle/oracle-goldengate.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud for Apache Flink](../../technologies/ibm/confluent-cloud-flink.md), [Confluent Platform](../../technologies/ibm/confluent-platform.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Pipeline Builder](../../technologies/palantir/palantir-pipeline-builder.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Beam](../../technologies/open-source/apache-beam.md), [Apache Flink](../../technologies/open-source/apache-flink.md), [Kafka Streams](../../technologies/open-source/apache-kafka-streams.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Estuary](../../technologies/independent/estuary.md) |

Narrower capabilities are realised by a further 15 technologies; see their pages.
