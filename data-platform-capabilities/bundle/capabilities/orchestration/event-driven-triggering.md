---
type: Capability
id: event-driven-triggering
title: Event-driven triggering
description: Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
aliases: [sensors, file-arrival triggers]
broader: [orchestration]
related: [workflow-orchestration, file-ingestion, message-queuing, change-feeds, freshness-monitoring]
tags: [orchestration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Here a pipeline starts in response to a signal rather than a clock. The signal can be a storage notification that a file has landed, a commit to a table, a message on a queue or topic, a webhook from a SaaS application, or another pipeline finishing. If a partner's daily file arrives at 03:12 one day and 05:40 the next, a trigger starts processing moments after each arrival, instead of a fixed 06:00 job that either waits too long or runs before the file exists.

It shortens the time between data arriving and being usable, and removes the padding added to schedules to allow for late upstream work. In return, load is less predictable, and bursts, duplicate signals and missed signals must be handled. Implementations include sensors that poll for a condition, push notifications from storage or catalogues, and triggers on table changes. Data-aware orchestration goes further, reasoning about the state of whole datasets rather than reacting to single events.

# Key considerations

- Notifications can be lost or duplicated. Pair push triggers with a periodic check for anything missed, and make runs idempotent.
- Group bursts into one run where possible. A thousand files landing together should not start a thousand pipelines.
- Polling sensors occupy workers while they wait. At scale, prefer push notifications or sensors that release their worker between checks.
- Record which event started each run, so a result can be traced back to its trigger.

# Questions to ask

- Which inputs arrive at unpredictable times, and how much delay does a fixed schedule add?
- Which systems can emit notifications, and how reliable are they?
- What should happen when an expected event never arrives?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Orchestration](orchestration.md) |
| Broader | [Orchestration](orchestration.md) |
| Related | [Active metadata](../metadata/active-metadata.md), [Alerts and subscriptions](../analytics-bi/data-alerting.md), [Change feeds](../serving/change-feeds.md), [File ingestion](../ingestion-integration/file-ingestion.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Message queuing](../ingestion-integration/message-queuing.md), [Serverless compute](../compute/serverless-compute.md), [Workflow orchestration](workflow-orchestration.md) |

# Where it appears

- **Use cases:** [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Orchestration](../../maturity/track-orchestration.md) (from level 3, Defined)
- **Frameworks:** [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Pipeline triggers

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | EventBridge rules and S3 Event Notifications | [Amazon EventBridge](../../technologies/aws/aws-eventbridge.md), [AWS IoT Core](../../technologies/aws/aws-iot-core.md), [AWS Step Functions](../../technologies/aws/aws-step-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Event Grid](../../technologies/microsoft/azure-event-grid.md), [Fabric Activator](../../technologies/microsoft/fabric-activator.md), [Fabric Real-Time hub](../../technologies/microsoft/fabric-real-time-hub.md), [Pipelines in Fabric Data Factory](../../technologies/microsoft/fabric-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Eventarc](../../technologies/google-cloud/gcp-eventarc.md), [Google Cloud Managed Service for Apache Airflow](../../technologies/google-cloud/gcp-managed-airflow.md), [Google Cloud Workflows](../../technologies/google-cloud/gcp-workflows.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake tasks and task graphs](../../technologies/snowflake/snowflake-tasks.md), [Snowpipe](../../technologies/snowflake/snowflake-snowpipe.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Jobs](../../technologies/databricks/databricks-lakeflow-jobs.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [S3Queue and AzureQueue table engines](../../technologies/clickhouse/clickhouse-s3queue.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Application Integration (CAI)](../../technologies/informatica/informatica-cloud-application-integration.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Automate](../../technologies/palantir/palantir-automate.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Airflow](../../technologies/open-source/apache-airflow.md), [Kestra](../../technologies/open-source/kestra.md), [Prefect](../../technologies/open-source/prefect.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [Prefect Cloud](../../technologies/independent/prefect-cloud.md) |
