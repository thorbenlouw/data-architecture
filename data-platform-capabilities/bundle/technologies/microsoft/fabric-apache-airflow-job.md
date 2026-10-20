---
type: Technology
id: fabric-apache-airflow-job
title: Fabric Apache Airflow job
description: Managed Apache Airflow inside Fabric for running Python-defined DAGs without operating the Airflow infrastructure.
formerly: [Data workflows]
platform: platform-microsoft
kind: feature
availability: ga
realises: [workflow-orchestration]
resource: https://learn.microsoft.com/en-us/fabric/data-factory/apache-airflow-jobs-concepts
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Successor to Azure Data Factory Workflow Orchestration Manager. No private network support yet and a single Airflow version; Git and deployment pipeline support is still preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Fabric Data Factory

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md), [AWS Step Functions](../aws/aws-step-functions.md), [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku scenarios](../dataiku/dataiku-scenarios.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Astronomer Astro](../independent/astronomer-astro.md), [Boomi Data Integration](../independent/boomi-data-integration.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
