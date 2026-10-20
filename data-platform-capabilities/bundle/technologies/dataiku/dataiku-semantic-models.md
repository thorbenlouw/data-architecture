---
type: Technology
id: dataiku-semantic-models
title: Dataiku Semantic Models
description: Business models of tables, columns, relationships and metrics that agents use to turn natural-language questions into correct SQL.
platform: platform-dataiku
kind: feature
availability: unconfirmed
realises: [ai-context-layer, metric-definitions, conversational-analytics]
resource: https://doc.dataiku.com/dss/latest/semantic-models/index.html
tags: [dataiku]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:15:00Z'}
---

Introduced in version 14.4 and built on the Semantic Models Lab plugin, which reached version 1.0 in May 2026. Models are versioned, tested in a validation playground and with prompt sets of questions and expected SQL, and deployed for agents to query through the Semantic Model Query Tool. Version 15.1 made them reusable assets in the Dataiku Catalog.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery) (primary): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) (Analytics and BI): Ask questions of data in natural language and get answers, charts or SQL back.

**Platform:** [Dataiku](../../platforms/platform-dataiku.md)  
**Availability:** unconfirmed  
**Product family:** Dataiku Platform for AI Success

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Quick Sight](../aws/aws-quick-sight.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric data agent](../microsoft/fabric-data-agent.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery conversational analytics](../google-cloud/gcp-bigquery-conversational-analytics.md), [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Genie Agents](../databricks/databricks-genie-agents.md), [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Tera](../teradata/teradata-tera.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Cube Cloud](../independent/cube-cloud.md), [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Conversational analytics](../../capabilities/analytics-bi/conversational-analytics.md), [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) |
