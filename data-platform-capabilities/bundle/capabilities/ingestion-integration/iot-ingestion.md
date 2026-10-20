---
type: Capability
id: iot-ingestion
title: IoT and telemetry ingestion
description: Collect high-volume telemetry securely from devices and edge gateways.
broader: [streaming-ingestion]
related: [time-series-data, event-time-windowing, event-streaming, identity-authentication]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Device fleets send small, frequent readings, such as a temperature every second from thousands of sensors, over lightweight protocols like MQTT or HTTPS, often through edge gateways that collect from local devices. An IoT ingestion service authenticates each device with its own certificate, accepts messages on per-device or per-type topics, routes them to streams or storage, and keeps registry data such as model, location and firmware version alongside the readings.

Telemetry differs from business events in volume, in the number of separate senders and in its unreliability: devices go offline, clocks drift and buffered data arrives hours late in bursts. Security is per device, so a compromised device can be revoked without affecting the fleet. Industrial sites add protocols such as OPC UA and plant historians as sources. Edge data processing reduces what is sent; the readings usually end up stored as time-series data.

# Key considerations

- Provision and rotate device credentials at fleet scale. Credentials shared across devices make revocation impossible.
- Keep the device's event time as well as the received time, and expect clock skew and late arrival after outages.
- Plan for bursts when many devices reconnect at once, for example after a network or power failure.
- Keep the device registry and its history, since readings mean little without knowing which device sent them, where and in what configuration.

# Questions to ask

- How many devices are there, at what message rate and size, and over which networks?
- Can devices buffer data while offline, and for how long?
- Which protocols and industrial systems must be supported?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Streaming ingestion](streaming-ingestion.md) |
| Narrower | [Edge data processing](../processing/edge-data-processing.md) |
| Related | [Edge inference](../mlops/edge-inference.md), [Event streaming](event-streaming.md), [Event-time windowing](../processing/event-time-windowing.md), [Identity and authentication](../security/identity-authentication.md), [Time-series data](../specialised-data/time-series-data.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (requires, level 3)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 4, Measured)
- **Frameworks:** [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data · [ISO 8000 (data quality)](../../frameworks/framework-iso-8000.md): ISO 8000-210 to 8000-230 – Sensor data

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS IoT Core](../../technologies/aws/aws-iot-core.md), [AWS IoT SiteWise](../../technologies/aws/aws-iot-sitewise.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Event Grid](../../technologies/microsoft/azure-event-grid.md), [Azure IoT Hub](../../technologies/microsoft/azure-iot-hub.md), [Azure IoT Operations](../../technologies/microsoft/azure-iot-operations.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowpipe Streaming](../../technologies/snowflake/snowflake-snowpipe-streaming.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Zerobus Ingest](../../technologies/databricks/databricks-zerobus-ingest.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickPipes](../../technologies/clickhouse/clickhouse-clickpipes.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Streaming Ingestion and Replication](../../technologies/informatica/informatica-streaming-ingestion-and-replication.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Event Stream Processing](../../technologies/sas/sas-event-stream-processing.md) |

Narrower capabilities are realised by a further 5 technologies; see their pages.
