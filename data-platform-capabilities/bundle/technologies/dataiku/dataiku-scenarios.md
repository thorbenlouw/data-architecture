---
type: Technology
id: dataiku-scenarios
title: Dataiku scenarios
description: Automation that builds datasets, verifies data quality rules, retrains models and runs other steps on schedules or triggers, and reports results by email, chat or webhook.
platform: platform-dataiku
kind: feature
availability: ga
realises: [workflow-orchestration, event-driven-triggering, continuous-training, data-testing, data-alerting]
resource: https://doc.dataiku.com/dss/latest/scenarios/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Triggers include time schedules, dataset changes, changes in SQL query results, completion of another scenario and custom Python. Build steps can retrain saved models, and a dashboard export step can send dashboards by email. Test scenarios run Python unit tests, integration tests and webapp tests on a project before it is deployed. Version 15.1 added a heatmap of scheduled runs.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) (Orchestration): Start pipelines when something happens, such as a file arriving, a table changing or a message being published.
- [Continuous training](../../capabilities/mlops/continuous-training.md) (ML operations): Retrain and redeploy models automatically when data, drift or schedules call for it.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md) (Analytics and BI): Notify people when data crosses thresholds, or deliver reports to them on a schedule.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** ga  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Step Functions](../aws/aws-step-functions.md), [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md), [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md), [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Automate](../palantir/palantir-automate.md) | [Alerts and subscriptions](../../capabilities/analytics-bi/data-alerting.md), [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Event-driven triggering](../../capabilities/orchestration/event-driven-triggering.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
