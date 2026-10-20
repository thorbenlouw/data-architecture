---
type: Technology
id: prefect
title: Prefect
description: Python workflow orchestration framework that turns ordinary functions into observable, retryable flows with schedules and event-based automations.
platform: platform-open-source
kind: open-source
availability: ga
realises: [workflow-orchestration, event-driven-triggering, pipeline-monitoring]
resource: https://docs.prefect.io/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, company-led by Prefect Technologies, which sells Prefect Cloud. Prefect 3 is current. Lighter-weight than Airflow for teams writing mostly Python.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Step Functions](../aws/aws-step-functions.md), [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Astronomer Astro](../independent/astronomer-astro.md), [Prefect Cloud](../independent/prefect-cloud.md), [Dagster+](../independent/dagster-plus.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
