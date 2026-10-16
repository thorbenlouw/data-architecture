---
type: Capability
id: workflow-orchestration
title: Workflow orchestration
description: Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
aliases: [DAGs, job scheduling, Airflow]
broader: [orchestration]
related: [pipeline-monitoring, transformation-as-code, ci-cd, declarative-pipelines]
tags: [orchestration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A workflow is described as a directed acyclic graph (DAG): tasks connected by arrows that show which must finish before others start. A daily sales workflow might extract from three sources in parallel, load each, run transformations, run data quality tests, and publish the reporting tables only if the tests pass. The orchestrator starts it at 06:00, retries a failed task up to three times with a delay, and alerts the owning team if the run fails or has not finished by 08:00. Apache Airflow is the best-known open-source example.

This is the base of most batch data platforms. It turns a collection of scripts and cron entries into something with dependencies, visibility and recovery. Orchestrators differ in how workflows are defined (Python code, YAML or a visual designer), whether tasks can be generated dynamically, and where tasks run (on workers, in containers or by calling external services). Fixed schedules are simple but fragile when upstream work runs late, which event-driven and data-aware approaches address.

# Key considerations

- Keep tasks small and idempotent so one failed step can be retried without rerunning the whole workflow.
- Pass the logical date or data interval to every task instead of using the current time, so reruns and backfills process the right period.
- Do not run heavy processing on orchestrator workers. Hand it to engines and keep the orchestrator responsive.
- Set timeouts and expected completion times per task. A task that hangs for hours can do more harm than one that fails quickly.

# Questions to ask

- How are pipelines scheduled today, and what happens when one fails overnight?
- Who writes workflows: engineers in code, or analysts who need a visual tool?
- How many tasks run per day, and how many must run at once at peak?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Orchestration](orchestration.md) |
| Broader | [Orchestration](orchestration.md) |
| Related | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Processing and transformation](../processing/processing.md), [Agent hosting and runtime](../generative-ai/agent-runtime.md), [Batch inference](../mlops/batch-inference.md), [CI/CD](../development-lifecycle/ci-cd.md), [Declarative pipelines](../processing/declarative-pipelines.md), [Event-driven triggering](event-driven-triggering.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md), [Table-level lineage](../metadata/table-lineage.md), [Transformation as code](../processing/transformation-as-code.md) |
| Needed by | [Batch ingestion](../ingestion-integration/batch-ingestion.md), [ML pipelines](../machine-learning/ml-pipelines.md), [Pipeline monitoring and alerting](../platform-operations/pipeline-monitoring.md) |

# Where it appears

- **Use cases:** [Churn prediction](../../use-cases/usecase-churn-prediction.md) (requires, level 2) · [Demand forecasting](../../use-cases/usecase-demand-forecasting.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Patterns:** [ELT](../../patterns/elt.md) · [ETL](../../patterns/etl.md) · [Lambda architecture](../../patterns/lambda-architecture.md) · [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md) · [Write-audit-publish](../../patterns/write-audit-publish.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Orchestration](../../maturity/track-orchestration.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 10 – Frequency · [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – infrastructure provisioning plane · [Google Cloud MLOps levels](../../frameworks/framework-google-mlops-levels.md): Level 1 – ML pipeline automation · [Microsoft MLOps maturity model](../../frameworks/framework-microsoft-mlops-maturity.md): Level 1 – DevOps but no MLOps

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon MWAA; Step Functions state machines | [Amazon Managed Workflows for Apache Airflow](../../technologies/aws/aws-mwaa.md), [Amazon MWAA Serverless](../../technologies/aws/aws-mwaa-serverless.md), [AWS Step Functions](../../technologies/aws/aws-step-functions.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Pipelines | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Fabric Apache Airflow job](../../technologies/microsoft/fabric-apache-airflow-job.md), [Pipelines in Fabric Data Factory](../../technologies/microsoft/fabric-pipelines.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Managed Service for Apache Airflow (formerly Cloud Composer); BigQuery pipelines | [BigQuery pipelines](../../technologies/google-cloud/gcp-bigquery-pipelines.md), [Google Cloud Managed Service for Apache Airflow](../../technologies/google-cloud/gcp-managed-airflow.md), [Google Cloud Workflows](../../technologies/google-cloud/gcp-workflows.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | tasks and task graphs | [Snowflake tasks and task graphs](../../technologies/snowflake/snowflake-tasks.md) |
| [Databricks](../../platforms/platform-databricks.md) | Lakeflow Jobs | [Lakeflow Jobs](../../technologies/databricks/databricks-lakeflow-jobs.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse refreshable materialized views](../../technologies/clickhouse/clickhouse-refreshable-materialized-views.md) |
| [Informatica](../../platforms/platform-informatica.md) | taskflows | [Informatica Cloud Data Integration (CDI)](../../technologies/informatica/informatica-cloud-data-integration.md), [Informatica PowerCenter](../../technologies/informatica/informatica-powercenter.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | Cloudera Data Engineering Airflow | [Cloudera Data Engineering](../../technologies/cloudera/cloudera-data-engineering.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Integration](../../technologies/oracle/oracle-oci-data-integration.md), [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md) |
| [SAP](../../platforms/platform-sap.md) | Task chains | [SAP Datasphere](../../technologies/sap/sap-datasphere.md), [SAP Data Intelligence Cloud](../../technologies/sap/sap-data-intelligence-cloud.md) (deprecated) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Airflow](../../technologies/open-source/apache-airflow.md), [Dagster](../../technologies/open-source/dagster.md), [Kestra](../../technologies/open-source/kestra.md), [Prefect](../../technologies/open-source/prefect.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [Boomi Data Integration](../../technologies/independent/boomi-data-integration.md), [Dagster+](../../technologies/independent/dagster-plus.md), [dbt platform](../../technologies/independent/dbt-platform.md), [Matillion Maia Foundation](../../technologies/independent/matillion-maia-foundation.md), [Prefect Cloud](../../technologies/independent/prefect-cloud.md) |
