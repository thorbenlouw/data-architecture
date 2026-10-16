---
type: Capability
id: event-time-windowing
title: Event-time windowing
description: Group events into time windows by when they happened, handling late and out-of-order data.
aliases: [watermarks, tumbling windows, sliding windows]
broader: [stream-processing]
related:
- time-series-data
- iot-ingestion
- behavioural-event-collection
- backfill-replay
- edge-data-processing
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Events are grouped by the timestamp at which they happened rather than the moment they reach the processor. A five-minute tumbling window collects events whose event time falls in each five-minute slot; sliding windows overlap; session windows close after a gap in activity. Because events arrive late and out of order, the engine tracks a watermark, its estimate of how far event time has progressed, and closes a window only when the watermark passes the window's end plus any allowed lateness.

This matters whenever results must reflect what happened rather than network delays: a mobile app holding events while offline, sensors on patchy links, or stream partitions read at different speeds. Windows based on arrival time are simpler but give results that change with load and replays. The main choice is between speed and completeness: waiting longer for stragglers gives more accurate results, later. Events that arrive after the limit can be dropped, sent to a separate output, or used to correct results already emitted.

# Key considerations

- Set allowed lateness from measured delays, not guesses, and review it when sources change.
- Decide how downstream systems handle a corrected result for a window already emitted.
- Watermarks stall when one partition or source goes quiet. Check how the engine handles idle sources.
- Device clocks drift and time zones vary. Normalise event timestamps on capture.

# Questions to ask

- How late can events arrive, and how often does that happen?
- Is an early approximate result followed by a correction acceptable, or must each window be emitted once?
- What should happen to events that arrive after their window has closed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Stream processing](stream-processing.md) |
| Related | [Backfill and reprocessing](../orchestration/backfill-replay.md), [Behavioural event collection](../ingestion-integration/behavioural-event-collection.md), [Edge data processing](edge-data-processing.md), [IoT and telemetry ingestion](../ingestion-integration/iot-ingestion.md), [Streaming inference](../mlops/streaming-inference.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 3) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (benefits from)
- **Patterns:** [Kappa architecture](../../patterns/kappa-architecture.md)
- **Maturity tracks:** [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined) · [Transformation engineering](../../maturity/track-transformation.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Managed Service for Apache Flink](../../technologies/aws/aws-managed-flink.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Stream Analytics](../../technologies/microsoft/azure-stream-analytics.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Dataflow](../../technologies/google-cloud/gcp-dataflow.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Streaming Analytics](../../technologies/cloudera/cloudera-streaming-analytics.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Cloud for Apache Flink](../../technologies/ibm/confluent-cloud-flink.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Beam](../../technologies/open-source/apache-beam.md), [Apache Flink](../../technologies/open-source/apache-flink.md), [Kafka Streams](../../technologies/open-source/apache-kafka-streams.md), [Spark Structured Streaming](../../technologies/open-source/apache-spark-structured-streaming.md) |
