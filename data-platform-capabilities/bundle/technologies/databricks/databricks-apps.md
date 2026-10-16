---
type: Technology
id: databricks-apps
title: Databricks Apps
description: Serverless hosting for Python and Node.js web applications (for example Streamlit, Dash, Gradio and React) that run inside the workspace with Unity Catalog, SQL warehouse and OAuth integration.
platform: platform-databricks
kind: managed-service
availability: ga
realises: [data-applications, container-services]
resource: https://docs.databricks.com/aws/en/dev-tools/databricks-apps/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apps can be deployed from Git. Compute sizing, horizontal scaling (GA September 2026) and app telemetry are available. Apps also host Agent Runtime, and Lakebase is the usual transactional store for apps. Genie App Builder (Beta, September 2026) generates apps from natural-language prompts inside governed App Spaces.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps) (primary): Build and host interactive data applications next to the data, under platform security.
- [Container services](../../capabilities/compute/container-services.md) (Query and compute): Run custom containerised applications and services next to the data, inside the platform's security boundary.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick](../aws/aws-quick.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md) | [Container services](../../capabilities/compute/container-services.md), [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Streamlit in Snowflake](../snowflake/snowflake-streamlit.md), [Snowpark Container Services](../snowflake/snowflake-snowpark-container-services.md), [Snowflake Native App Framework](../snowflake/snowflake-native-app-framework.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Container services](../../capabilities/compute/container-services.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Streamlit](../open-source/streamlit.md), [marimo](../open-source/marimo.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Sisense](../independent/sisense.md), [Domo](../independent/domo.md), [Hex](../independent/hex.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
