---
type: Technology
id: sap-data-intelligence-cloud
title: SAP Data Intelligence Cloud
description: SAP's earlier pipeline, orchestration and metadata service for integrating SAP and non-SAP data and running ML pipelines.
aliases: [SAP Data Intelligence]
platform: platform-sap
kind: managed-service
availability: deprecated
realises: [workflow-orchestration, low-code-transformation, metadata-harvesting]
resource: https://www.sap.com/products/technology-platform/data-intelligence.html
tags: [sap]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP no longer develops it as a strategic product and directs customers to Datasphere replication and transformation flows and to BDC. Existing installations are still met.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration) (primary): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon MWAA Serverless](../aws/aws-mwaa-serverless.md), [AWS Step Functions](../aws/aws-step-functions.md), [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Apache Airflow job](../microsoft/fabric-apache-airflow-job.md), [Pipelines in Fabric Data Factory](../microsoft/fabric-pipelines.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery pipelines](../google-cloud/gcp-bigquery-pipelines.md), [Google Cloud Workflows](../google-cloud/gcp-workflows.md), [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake tasks and task graphs](../snowflake/snowflake-tasks.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse refreshable materialized views](../clickhouse/clickhouse-refreshable-materialized-views.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica PowerCenter](../informatica/informatica-powercenter.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Engineering](../cloudera/cloudera-data-engineering.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../oracle/oracle-ai-data-platform.md) | [Low-code transformation](../../capabilities/processing/low-code-transformation.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kestra](../open-source/kestra.md), [Prefect](../open-source/prefect.md), [Apache Airflow](../open-source/apache-airflow.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Astronomer Astro](../independent/astronomer-astro.md) | [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
