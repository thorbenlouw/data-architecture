---
type: Technology
id: snowflake-streamlit
title: Streamlit in Snowflake
description: Hosts Streamlit Python apps as Snowflake objects, on warehouse or container runtimes, with access governed by Snowflake roles.
aliases: [SiS]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-applications, dashboards-reports]
resource: https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The container runtime and secrets support became GA in March 2026. Streamlit apps can also be packaged inside Native Apps.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps) (primary): Build and host interactive data applications next to the data, under platform security.
- [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) (Analytics and BI): Build and share visual, interactive dashboards with filters and drill-down.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick](../aws/aws-quick.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric user data functions](../microsoft/fabric-user-data-functions.md), [Power BI scorecards and goals](../microsoft/powerbi-scorecards.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Apps](../databricks/databricks-apps.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Streamlit](../open-source/streamlit.md), [marimo](../open-source/marimo.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Sisense](../independent/sisense.md), [Domo](../independent/domo.md), [Sigma Computing](../independent/sigma.md) | [Dashboards and interactive reports](../../capabilities/analytics-bi/dashboards-reports.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
