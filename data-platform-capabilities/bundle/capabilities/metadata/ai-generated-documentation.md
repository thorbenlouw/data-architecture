---
type: Capability
id: ai-generated-documentation
title: AI-generated documentation
description: Draft descriptions, tags and documentation for data assets using AI, for people to review.
broader: [data-catalogue]
related: [ai-context-layer, data-classification, business-glossary, transformation-as-code]
depends_on: [metadata-harvesting, foundation-model-access]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A language model reads an asset's metadata, including its name, schema, sample values, the code that builds it, its lineage and the documentation of related assets, and proposes a description, column descriptions, tags, classifications and glossary links. Proposals are marked as AI-generated and wait for an owner to accept, edit or reject them. For example, a new table with columns `cust_id`, `ltv_12m` and `seg_cd` receives drafted descriptions explaining twelve-month lifetime value and the segment codes found in its transformation logic.

Large estates hold thousands of undocumented assets that manual effort never catches up with. AI drafts make broad coverage achievable but can be confidently wrong, especially about business meaning that the code does not reveal. It is used for bulk backfill, for drafting when an asset is created, and for suggesting documentation in code reviews of transformation projects. The text produced becomes input to search and to AI agents, so unreviewed errors spread. Classification applies sensitivity labels; this capability drafts the explanatory text, although both may use similar models.

# Key considerations

- Show clearly which descriptions are reviewed and which are unreviewed AI drafts, so people and agents know what they rely on.
- Sending sample values to a model can expose sensitive data. Check what is sent and to which model.
- Prioritise heavily used and certified assets for human review.
- Drafts improve with better inputs. Transformation code and lineage help far more than column names alone.

# Questions to ask

- What share of assets have useful descriptions today?
- Who will review drafts, and how much time can they give?
- May sample data be sent to the model used for drafting?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [AI context layer](ai-context-layer.md), [AI-assisted development](../development-lifecycle/ai-assisted-development.md), [Business glossary](business-glossary.md), [Data classification](../governance/data-classification.md), [Transformation as code](../processing/transformation-as-code.md) |
| Depends on | [Metadata harvesting](metadata-harvesting.md), [Foundation model access](../generative-ai/foundation-model-access.md) |

# Where it appears

- **Personas:** [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Copilot in Power BI](../../technologies/microsoft/powerbi-copilot.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data insights](../../technologies/google-cloud/gcp-knowledge-catalog-data-insights.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake AI-generated descriptions](../../technologies/snowflake/snowflake-cortex-descriptions.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Catalog Explorer](../../technologies/databricks/databricks-catalog-explorer.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Catalog](../../technologies/dataiku/dataiku-catalog.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Anomalo](../../technologies/independent/anomalo.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [dbt Copilot](../../technologies/independent/dbt-copilot.md) |
