---
type: Technology
id: gcp-knowledge-catalog-data-insights
title: Knowledge Catalog data insights
description: Uses Gemini to draft table and column descriptions, suggested questions and SQL queries from metadata and profiles.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [ai-generated-documentation, augmented-analytics]
resource: https://docs.cloud.google.com/dataplex/docs/data-insights
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Insights for structured data are GA; insights for unstructured data such as PDFs in Cloud Storage are in preview. The same insights appear in BigQuery as dataset and table insights.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) (Metadata and discovery) (primary): Draft descriptions, tags and documentation for data assets using AI, for people to review.
- [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) (Analytics and BI): Use automation and machine learning to surface insights, anomalies and explanations without being asked.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Knowledge Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Copilot in Power BI](../microsoft/powerbi-copilot.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md), [Augmented analytics](../../capabilities/analytics-bi/augmented-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake AI-generated descriptions](../snowflake/snowflake-cortex-descriptions.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Catalog Explorer](../databricks/databricks-catalog-explorer.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku Catalog](../dataiku/dataiku-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [dbt Copilot](../independent/dbt-copilot.md), [Anomalo](../independent/anomalo.md), [Collibra Data Catalog](../independent/collibra-data-catalog.md) | [AI-generated documentation](../../capabilities/metadata/ai-generated-documentation.md) |
