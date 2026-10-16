---
type: Technology
id: gcp-eventarc
title: Eventarc
description: Routes events from Google Cloud services, audit logs, Cloud Storage and Pub/Sub to Cloud Run, Workflows and other targets.
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [event-driven-triggering, application-integration]
resource: https://docs.cloud.google.com/eventarc/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Commonly used to start pipelines when a file lands in Cloud Storage or a BigQuery job completes; Eventarc Advanced adds a managed message bus with filtering and transformation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration) (primary): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS Step Functions](../aws/aws-step-functions.md), [AWS IoT Core](../aws/aws-iot-core.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Grid](../microsoft/azure-event-grid.md), [Fabric Real-Time hub](../microsoft/fabric-real-time-hub.md), [Fabric Activator](../microsoft/fabric-activator.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
