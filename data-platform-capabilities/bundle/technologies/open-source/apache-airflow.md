---
type: Technology
id: apache-airflow
title: Apache Airflow
description: Workflow orchestrator in which pipelines are defined in Python as task graphs (DAGs) and run on schedules, data events or on demand.
aliases: [Airflow]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- workflow-orchestration
- asset-based-orchestration
- event-driven-triggering
- backfill-replay
- pipeline-monitoring
resource: https://airflow.apache.org/announcements/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ASF top-level project, Apache 2.0; current release is 3.3.2 (September 2026). Airflow 3.0 (April 2025) added a Task SDK and Task Execution API for remote and multi-language workers, DAG versioning, assets (formerly datasets) with event-driven scheduling from message queues, scheduler-managed backfills and a new UI; 3.1 added human-in-the-loop tasks. Managed versions include Astronomer, Amazon MWAA and Google Cloud Composer.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md), [AWS Step Functions](../aws/aws-step-functions.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Astronomer Astro](../independent/astronomer-astro.md), [Prefect Cloud](../independent/prefect-cloud.md), [Dagster+](../independent/dagster-plus.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
