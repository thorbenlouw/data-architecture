---
type: Technology
id: azure-iot-operations
title: Azure IoT Operations
description: An edge data plane on Arc-enabled Kubernetes with an MQTT broker, OPC UA and other connectors, and data flows that send processed data to the cloud.
platform: platform-microsoft
kind: software
availability: ga
realises: [iot-ingestion, stream-processing, deployment-options, edge-data-processing]
resource: https://learn.microsoft.com/en-us/azure/iot-operations/overview-iot-operations
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Runs offline for up to 72 hours. Sends to Event Hubs, Event Grid, ADLS, Azure Data Explorer and Fabric OneLake.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration) (primary): Collect high-volume telemetry securely from devices and edge gateways.
- [Stream processing](../../capabilities/processing/stream-processing.md) (Processing and transformation): Transform, join and aggregate events continuously as they arrive, keeping state across events.
- [Hybrid and multi-cloud deployment](../../capabilities/platform-operations/deployment-options.md) (Platform operations): Run the platform across clouds, regions or on-premises, or inside your own cloud account.
- [Edge data processing](../../capabilities/processing/edge-data-processing.md) (Processing and transformation): Filter, transform and buffer data on devices or sites before it reaches the platform, tolerating disconnection.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS IoT SiteWise](../aws/aws-iot-sitewise.md), [AWS IoT Core](../aws/aws-iot-core.md) | [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [Edge data processing](../../capabilities/processing/edge-data-processing.md), [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Stream processing](../../capabilities/processing/stream-processing.md) |
