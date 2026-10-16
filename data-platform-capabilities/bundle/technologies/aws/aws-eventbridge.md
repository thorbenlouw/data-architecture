---
type: Technology
id: aws-eventbridge
title: Amazon EventBridge
description: Serverless event bus, scheduler and point-to-point pipes that route events from AWS services, SaaS partners and applications to targets by rule.
aliases: [EventBridge Pipes, EventBridge Scheduler]
formerly: [Amazon CloudWatch Events]
platform: platform-aws
kind: managed-service
availability: ga
realises: [event-driven-triggering, application-integration]
resource: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Receives S3, Glue, Redshift, SageMaker and DataZone events, so it is the usual trigger layer for data pipelines. EventBridge Scheduler handles cron-style starts; Pipes connect streams and queues to targets with filtering and enrichment.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration) (primary): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Application integration](../../capabilities/ingestion-integration/application-integration.md) (Ingestion and integration): Connect applications through APIs, events and process flows in near real time, outside the analytical data path.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Event Grid](../microsoft/azure-event-grid.md), [Fabric Real-Time hub](../microsoft/fabric-real-time-hub.md), [Fabric Activator](../microsoft/fabric-activator.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [Application integration](../../capabilities/ingestion-integration/application-integration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
