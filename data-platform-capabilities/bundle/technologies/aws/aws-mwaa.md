---
type: Technology
id: aws-mwaa
title: Amazon Managed Workflows for Apache Airflow
description: Managed Apache Airflow environments in your VPC that run Python DAGs with autoscaled workers and CloudWatch logging.
aliases: [Amazon MWAA, MWAA]
platform: platform-aws
kind: managed-service
availability: ga
realises:
- workflow-orchestration
- asset-based-orchestration
- backfill-replay
- pipeline-monitoring
- runtime-management
resource: https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Supports Airflow 3 (including asset-based scheduling) as well as Airflow 2. Environments are billed while running, whether or not tasks execute. SageMaker Unified Studio workflows are built on it.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md), [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Airflow](../open-source/apache-airflow.md), [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Astronomer Astro](../independent/astronomer-astro.md), [Dagster+](../independent/dagster-plus.md), [Prefect Cloud](../independent/prefect-cloud.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
