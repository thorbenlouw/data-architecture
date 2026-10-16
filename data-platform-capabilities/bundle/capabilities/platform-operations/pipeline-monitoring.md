---
type: Capability
id: pipeline-monitoring
title: Pipeline monitoring and alerting
description: Track pipeline runs, failures and durations, and alert the right people.
broader: [platform-observability, orchestration]
related: [freshness-monitoring, data-issue-management, data-observability, table-lineage, data-slas]
depends_on: [workflow-orchestration]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each scheduled or triggered run is recorded: when it started, how long each task took, whether it succeeded, how many records it processed and how much compute it used. Runs are compared with history, so a job that normally takes 20 minutes and has now run for two hours raises an alert before it fails. Alerts go to the owning team by chat, email or paging tool, linked to the failed task's logs, and related alerts are grouped so one failure does not send fifty messages.

Most data incidents first appear as a failed or late pipeline, so this is usually the first operational capability a platform needs. Orchestrators provide much of it, but pipelines often span an ingestion service, a transformation project and a BI refresh, so a combined view needs run events from all of them, for example in OpenLineage format. Pipeline monitoring watches the process. Freshness monitoring and data observability watch the resulting data, catching jobs that succeeded but produced wrong or empty output.

# Key considerations

- Route alerts to the owning team, not a shared inbox. Ownership metadata on every pipeline makes this possible.
- Alert on lateness against an expected time as well as on failure. A job that never started produces no failure.
- Suppress downstream alerts when an upstream job fails, so responders see the cause rather than every symptom.
- Keep run history long enough to show trends in duration and cost, which signal problems before they become failures.

# Questions to ask

- How do teams learn that a pipeline has failed, and how long does that take?
- Do pipelines span several tools, and is there one view of a run across them?
- Which pipelines need out-of-hours response, and who is on call for them?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform observability](platform-observability.md), [Orchestration](../orchestration/orchestration.md) |
| Related | [Data quality and observability](../data-quality/data-quality.md), [Data issue management](../data-quality/data-issue-management.md), [Data observability](../data-quality/data-observability.md), [Data service levels](../data-products/data-slas.md), [Freshness monitoring](../data-quality/freshness-monitoring.md), [Platform incident management](platform-incident-management.md), [Table-level lineage](../metadata/table-lineage.md), [Workflow orchestration](../orchestration/workflow-orchestration.md) |
| Depends on | [Workflow orchestration](../orchestration/workflow-orchestration.md) |

# Where it appears

- **Use cases:** [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 3)
- **Patterns:** [Metadata-driven pipelines](../../patterns/metadata-driven-pipelines.md)
- **Personas:** [Data engineer](../../personas/persona-data-engineer.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 10 – Frequency · [DCAM v3](../../frameworks/framework-edm-dcam.md): 7 Data Management Operations, Risk & Control · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon CloudWatch](../../technologies/aws/aws-cloudwatch.md), [Amazon Managed Workflows for Apache Airflow](../../technologies/aws/aws-mwaa.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Monitor](../../technologies/microsoft/azure-monitor.md), [Fabric workspace monitoring](../../technologies/microsoft/fabric-workspace-monitoring.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Monitoring](../../technologies/google-cloud/gcp-cloud-monitoring.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake tasks and task graphs](../../technologies/snowflake/snowflake-tasks.md), [Snowflake Trail (event tables, logging, tracing and metrics)](../../technologies/snowflake/snowflake-trail.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Lakeflow Jobs](../../technologies/databricks/databricks-lakeflow-jobs.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Operational Insights](../../technologies/informatica/informatica-operational-insights.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Observability](../../technologies/cloudera/cloudera-observability.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Data observability in IBM watsonx.data integration](../../technologies/ibm/ibm-data-observability.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Health and data expectations](../../technologies/palantir/palantir-data-health.md), [Palantir Data Lineage](../../technologies/palantir/palantir-data-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Airflow](../../technologies/open-source/apache-airflow.md), [Marquez](../../technologies/open-source/marquez.md), [OpenTelemetry](../../technologies/open-source/opentelemetry.md), [Prefect](../../technologies/open-source/prefect.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [Dagster+](../../technologies/independent/dagster-plus.md) |
