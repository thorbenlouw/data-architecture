---
type: Technology
id: dagster-plus
title: Dagster+
description: Managed control plane for Dagster's asset-based orchestration, with an asset catalogue, branch deployments, cost and performance insights and alerting.
aliases: [Dagster Plus]
formerly: [Dagster Cloud]
platform: platform-independent
vendor: Dagster Labs
kind: saas
availability: ga
realises:
- asset-based-orchestration
- workflow-orchestration
- environment-promotion
- cost-attribution
- pipeline-monitoring
- hybrid-data-plane
- ephemeral-environments
resource: https://dagster.io/docs/deployment/dagster-plus
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The managed edition of the open-source [Dagster](../open-source/dagster.md) orchestrator. Code runs on Dagster's infrastructure (Serverless) or in the customer's environment (Hybrid). The Catalog shows column-level lineage for assets that Dagster orchestrates.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) (Orchestration) (primary): Schedule work based on the freshness and dependencies of data assets rather than fixed times.
- [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) (Orchestration): Define pipelines as dependency graphs of tasks and run them on schedules with retries and alerts.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) (Platform operations): Track pipeline runs, failures and durations, and alert the right people.
- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Ephemeral development environments](../../capabilities/development-lifecycle/ephemeral-environments.md) (Development and DataOps): Create a short-lived, isolated environment for each developer or change, reusing production data and unchanged objects, and remove it when the work is merged.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Managed Workflows for Apache Airflow](../aws/aws-mwaa.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Managed Service for Apache Airflow](../google-cloud/gcp-managed-airflow.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Dynamic Tables](../snowflake/snowflake-dynamic-tables.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Jobs](../databricks/databricks-lakeflow-jobs.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Dagster](../open-source/dagster.md), [Apache Airflow](../open-source/apache-airflow.md) | [Data-aware orchestration](../../capabilities/orchestration/asset-based-orchestration.md), [Workflow orchestration](../../capabilities/orchestration/workflow-orchestration.md), [Pipeline monitoring and alerting](../../capabilities/platform-operations/pipeline-monitoring.md) |
