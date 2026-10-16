---
type: Technology
id: palantir-automate
title: Palantir Automate
description: Rules that watch Ontology data or schedules and send notifications, run actions or call AIP Logic when conditions are met.
platform: platform-palantir
kind: feature
availability: ga
realises: [event-driven-triggering, data-alerting]
resource: https://www.palantir.com/docs/foundry/getting-started/application-reference/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Typical for alerting operators and for running agents on new or changed objects. Build schedules for pipelines are configured separately.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration) (primary): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon EventBridge](../aws/aws-eventbridge.md), [AWS IoT Core](../aws/aws-iot-core.md), [AWS Step Functions](../aws/aws-step-functions.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Activator](../microsoft/fabric-activator.md), [Fabric Real-Time hub](../microsoft/fabric-real-time-hub.md), [Azure Event Grid](../microsoft/azure-event-grid.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Eventarc](../google-cloud/gcp-eventarc.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowpipe](../snowflake/snowflake-snowpipe.md), [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [S3Queue and AzureQueue table engines](../clickhouse/clickhouse-s3queue.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Application Integration (CAI)](../informatica/informatica-cloud-application-integration.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
