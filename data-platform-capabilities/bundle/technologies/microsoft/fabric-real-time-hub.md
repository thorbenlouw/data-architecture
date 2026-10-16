---
type: Technology
id: fabric-real-time-hub
title: Fabric Real-Time hub
description: A tenant-wide catalogue of streams and system events (Fabric, OneLake, job and Azure events) that users can discover, subscribe to and route.
platform: platform-microsoft
kind: feature
availability: ga
realises: [event-driven-triggering, event-api-catalogue]
resource: https://learn.microsoft.com/en-us/fabric/real-time-hub/real-time-hub-overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration) (primary): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Event and API catalogue](../../capabilities/metadata/event-api-catalogue.md) (Metadata and discovery): List the event streams and data APIs that systems publish, with owners, schemas, versions and consumers, so teams can find, subscribe to and safely change them.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Fabric Real-Time Intelligence

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS IoT Core](../aws/aws-iot-core.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
