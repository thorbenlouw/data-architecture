---
type: Technology
id: databricks-lakeflow-jobs
title: Lakeflow Jobs
description: Built-in orchestrator that runs dependency graphs of notebooks, pipelines, SQL, dbt and other tasks on schedules or on file-arrival, table-update and continuous triggers, with retries and loops.
aliases: [Databricks Jobs]
formerly: [Databricks Workflows]
platform: platform-databricks
kind: managed-service
availability: ga
realises:
- workflow-orchestration
- event-driven-triggering
- pipeline-monitoring
- backfill-replay
- asset-based-orchestration
resource: https://docs.databricks.com/aws/en/jobs/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Table-update triggers start work when upstream Unity Catalog tables change, which gives a basic form of data-aware scheduling. Run history is available in the lakeflow system tables (GA January 2026). Jobs can run on serverless compute, with performance or standard mode.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration): Schedule work based on the freshness and dependencies of data assets rather than fixed times.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Lakeflow

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md), [AWS Step Functions](../aws/aws-step-functions.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Airflow](../open-source/apache-airflow.md), [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Astronomer Astro](../independent/astronomer-astro.md), [Prefect Cloud](../independent/prefect-cloud.md), [Dagster+](../independent/dagster-plus.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
