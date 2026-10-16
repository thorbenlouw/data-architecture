---
type: Technology
id: azure-iot-hub
title: Azure IoT Hub
description: A managed hub for secure, bidirectional messaging with millions of devices, with device identity, routing and device twins.
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [iot-ingestion]
resource: https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration) (primary): Collect high-volume telemetry securely from devices and edge gateways.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS IoT Core](../aws/aws-iot-core.md), [AWS IoT SiteWise](../aws/aws-iot-sitewise.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
