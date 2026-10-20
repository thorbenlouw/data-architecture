---
type: Technology
id: aws-iot-core
title: AWS IoT Core
description: Managed MQTT and HTTPS message broker that authenticates devices and routes their telemetry to other AWS services through rules.
platform: platform-aws
kind: managed-service
availability: ga
realises: [iot-ingestion, event-driven-triggering]
resource: https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Rules can forward to Kinesis, Firehose, S3, DynamoDB, Timestream and Lambda. AWS IoT Analytics and AWS IoT Events have announced end of support, so new designs route device data to general analytics services instead.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) (Ingestion and integration) (primary): Collect high-volume telemetry securely from devices and edge gateways.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure IoT Hub](../microsoft/azure-iot-hub.md), [Azure Event Grid](../microsoft/azure-event-grid.md), [Azure IoT Operations](../microsoft/azure-iot-operations.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe Streaming](../snowflake/snowflake-snowpipe-streaming.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Zerobus Ingest](../databricks/databricks-zerobus-ingest.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickPipes](../clickhouse/clickhouse-clickpipes.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Streaming Ingestion and Replication](../informatica/informatica-streaming-ingestion-and-replication.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Event Stream Processing](../sas/sas-event-stream-processing.md) | [IoT and telemetry ingestion](../../capabilities/ingestion-integration/iot-ingestion.md) |
