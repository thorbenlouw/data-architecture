---
type: Technology
id: snowflake-native-app-framework
title: Snowflake Native App Framework
description: Packages data, code, Streamlit UIs, containers, agents and MCP servers as applications that consumers install and run in their own accounts through listings.
aliases: [Snowflake Native Apps]
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-applications, data-marketplace, external-data-sharing, application-sharing]
resource: https://docs.snowflake.com/en/developer-guide/native-apps/native-apps-about
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Provider logic stays hidden from consumers. Apps with containers run on Snowpark Container Services compute pools in the consumer account. Cortex Agents and MCP servers inside apps became GA in August 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) (Development and DataOps) (primary): Build and host interactive data applications next to the data, under platform security.
- [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) (Data sharing and collaboration): Publish, find and subscribe to data products and datasets, internally or commercially.
- [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) (Data sharing and collaboration): Share live data with customers, partners and suppliers under agreed terms.
- [Data application distribution](../../capabilities/data-sharing/application-sharing.md) (Data sharing and collaboration): Package code, models, interfaces and data as installable applications that run in the consumer's environment.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Collaboration

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick](../aws/aws-quick.md), [AWS Data Exchange](../aws/aws-data-exchange.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md), [External data sharing](../../capabilities/data-sharing/external-data-sharing.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric user data functions](../microsoft/fabric-user-data-functions.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Cloud Run](../google-cloud/gcp-cloud-run.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Apps](../databricks/databricks-apps.md), [Databricks Marketplace](../databricks/databricks-marketplace.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md), [Data application distribution](../../capabilities/data-sharing/application-sharing.md), [Data marketplace](../../capabilities/data-sharing/data-marketplace.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera AI Workbench](../cloudera/cloudera-ai-workbench.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Workshop](../palantir/palantir-workshop.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku webapps and Dataiku Applications](../dataiku/dataiku-webapps.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Streamlit](../open-source/streamlit.md), [marimo](../open-source/marimo.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Sisense](../independent/sisense.md), [Domo](../independent/domo.md), [Hex](../independent/hex.md) | [Data application hosting](../../capabilities/development-lifecycle/data-applications.md) |
