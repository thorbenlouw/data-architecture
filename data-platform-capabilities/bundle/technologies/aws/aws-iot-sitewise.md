---
type: Technology
id: aws-iot-sitewise
title: AWS IoT SiteWise
description: Service for collecting, modelling and storing industrial equipment telemetry as asset hierarchies with time-series properties.
platform: platform-aws
kind: managed-service
availability: ga
realises: [iot-ingestion, time-series-data, edge-data-processing]
resource: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Edge gateways collect OPC UA and Modbus data. SiteWise Monitor (portals) and the Data Processing Pack have been closed to new customers since October 2025.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration) (primary): Collect high-volume telemetry securely from devices and edge gateways.
- [Time-series data](../../capabilities/specialised-data/time-series-data.md) (Specialised data types): Store and query time-stamped measurements efficiently, with time-based functions and retention.
- [Edge data processing](../../capabilities/processing/edge-data-processing.md) (Processing and transformation): Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure IoT Operations](../microsoft/azure-iot-operations.md), [Azure IoT Hub](../microsoft/azure-iot-hub.md), [Azure Event Grid](../microsoft/azure-event-grid.md) | [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
