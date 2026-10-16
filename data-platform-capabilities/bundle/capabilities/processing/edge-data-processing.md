---
type: Capability
id: edge-data-processing
title: Edge data processing
description: Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.
aliases: [edge computing, edge flow management]
broader: [processing, iot-ingestion]
related: [time-series-data, event-time-windowing, streaming-inference, stream-processing, data-residency]
tags: [processing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Code runs on or near the devices that produce data, such as factory gateways, vehicles, shops or ships, before anything is sent to the central platform. Typical tasks are filtering noise, summarising sensor readings, converting industrial protocols, detecting anomalies locally and holding data in a local buffer while the connection is down. A wind turbine might sample vibration thousands of times a second but send only one-second summaries plus any reading above a threshold.

It is worth doing when bandwidth is expensive or limited, when decisions must be made on site within milliseconds, when connections drop for long periods, or when rules require some data to stay on site. The costs are running software on many remote devices with little compute or storage, and losing raw detail discarded at the edge. Deployments, configuration and updates are usually pushed centrally to fleets of devices. IoT ingestion collects data into the platform; edge processing decides what is worth sending.

# Key considerations

- Decide which raw data to keep locally and for how long, in case it is later needed for investigation or model training.
- Plan secure, staged software updates with rollback for large device fleets.
- Use store-and-forward with durable local buffers sized for the longest expected outage.
- Keep the device's own timestamps so central processing can order events correctly after delayed upload.

# Questions to ask

- How much data do devices produce, and what does it cost to transmit?
- Which decisions must be made on site without waiting for the central platform?
- How long can sites be disconnected, and what must happen meanwhile?
- How many devices or sites must be managed, and by whom?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Processing and transformation](processing.md) |
| Broader | [Processing and transformation](processing.md), [IoT and telemetry ingestion](../ingestion-integration/iot-ingestion.md) |
| Related | [Customer-hosted data plane](../platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../governance/data-residency.md), [Edge inference](../mlops/edge-inference.md), [Event-time windowing](event-time-windowing.md), [Stream processing](stream-processing.md), [Streaming inference](../mlops/streaming-inference.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 2)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 5, Optimising) · [Transformation engineering](../../maturity/track-transformation.md) (from level 5, Optimising)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS IoT SiteWise](../../technologies/aws/aws-iot-sitewise.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure IoT Operations](../../technologies/microsoft/azure-iot-operations.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Flow](../../technologies/cloudera/cloudera-data-flow.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache NiFi](../../technologies/open-source/apache-nifi.md) |
