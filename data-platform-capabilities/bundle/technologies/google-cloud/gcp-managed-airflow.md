---
type: Technology
id: gcp-managed-airflow
title: Google Cloud Managed Service for Apache Airflow
description: Managed Apache Airflow environments for scheduling and monitoring DAGs of data and ML tasks across Google Cloud and external systems.
aliases: [Managed Airflow]
formerly: [Cloud Composer]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises:
- workflow-orchestration
- backfill-replay
- asset-based-orchestration
- event-driven-triggering
- runtime-management
resource: https://docs.cloud.google.com/composer/docs
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Renamed in April 2026; generations are now called Managed Airflow Gen 3, Gen 2 and Legacy Gen 1, and the API is still composer. Gen 3 offers both Airflow 3.x (with asset-based scheduling) and Airflow 2.x images. Reports lineage to Knowledge Catalog and has a remote MCP server.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md) (Orchestration): Rerun pipelines over historical periods or replay events to correct or rebuild data.
- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md) (Development and DataOps): Define, version and upgrade the engine runtimes, libraries and images that notebooks, jobs and model serving run on, so code reruns the same way and upgrades do not break it.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md), [AWS Step Functions](../aws/aws-step-functions.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Runtime and environment management](../../capabilities/development-lifecycle/runtime-management.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Airflow](../open-source/apache-airflow.md), [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md) | [Backfill and reprocessing](../../capabilities/orchestration/backfill-replay.md), [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Astronomer Astro](../independent/astronomer-astro.md), [Prefect Cloud](../independent/prefect-cloud.md), [Dagster+](../independent/dagster-plus.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
