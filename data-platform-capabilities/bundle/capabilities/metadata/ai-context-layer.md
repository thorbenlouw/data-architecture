---
type: Capability
id: ai-context-layer
title: AI context layer
description: Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
aliases: [context layer, agent context, verified queries]
broader: [metadata, generative-ai]
related: [semantic-layer, business-glossary, conversational-analytics, knowledge-graphs, genai-evaluation]
depends_on: [data-catalogue]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Agents that write SQL or answer data questions go wrong when they guess what tables and columns mean. The context layer gives them curated knowledge: business definitions, metric formulas, preferred tables and join paths, valid values, example questions paired with verified SQL, and local rules such as a financial year starting in April. It is served at question time through retrieval, semantic-layer APIs or MCP tools. For example, asked for last quarter's active customers, an agent retrieves the approved definition and a verified query and uses them instead of inventing a filter.

It largely determines the accuracy of conversational analytics and data agents: current models write competent SQL but cannot infer local business meaning. It draws together the semantic layer, glossary, catalogue descriptions and certification, and adds material written for models, such as verified queries and usage instructions. Curation is continuous: failed questions become new examples. A semantic layer computes metrics; the context layer also explains how and when to use data, in a form models can retrieve.

# Key considerations

- Start with high-value domains and real user questions. Broad, shallow coverage helps less than deep coverage of what people actually ask.
- Give verified queries and definitions owners and tests. Stale context produces confident wrong answers.
- Serve context from the same sources BI uses, so AI answers and dashboards agree.
- Respect permissions. Context can reveal that sensitive data exists and what it means.
- Measure accuracy with an evaluation set per domain and use failures to direct curation.

# Questions to ask

- How accurate are AI answers about your data today, and how is that measured?
- Where do business definitions and approved queries live now?
- Who will curate context for each domain?
- Which agents and tools need to consume it, and through which interface?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md), [Generative AI](../generative-ai/generative-ai.md) |
| Related | [Analytics and BI](../analytics-bi/analytics-bi.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [AI agents](../generative-ai/ai-agents.md), [AI-assisted development](../development-lifecycle/ai-assisted-development.md), [AI-generated documentation](ai-generated-documentation.md), [Business glossary](business-glossary.md), [Conversational analytics](../analytics-bi/conversational-analytics.md), [Generative AI evaluation](../generative-ai/genai-evaluation.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md), [Semantic layer](../analytics-bi/semantic-layer.md), [Semantic model interchange](../analytics-bi/semantic-model-interchange.md) |
| Depends on | [Data catalogue](data-catalogue.md) |
| Needed by | [Conversational analytics](../analytics-bi/conversational-analytics.md) |

# Where it appears

- **Use cases:** [Agentic process automation](../../use-cases/usecase-agentic-automation.md) (benefits from) · [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3)
- **Personas:** [AI engineer](../../personas/persona-ai-engineer.md) · [Analytics engineer](../../personas/persona-analytics-engineer.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 5, Optimising)
- **Frameworks:** [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Context · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Context

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric data agent](../../technologies/microsoft/fabric-data-agent.md), [Fabric IQ ontology](../../technologies/microsoft/fabric-iq-ontology.md) (preview), [Power BI semantic models](../../technologies/microsoft/powerbi-semantic-models.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery conversational analytics](../../technologies/google-cloud/gcp-bigquery-conversational-analytics.md), [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Horizon Context](../../technologies/snowflake/snowflake-horizon-context.md) (preview), [Snowflake semantic views](../../technologies/snowflake/snowflake-semantic-views.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Genie Agents](../../technologies/databricks/databricks-genie-agents.md), [Unity Catalog metric views](../../technologies/databricks/databricks-metric-views.md) |
| [SAP](../../platforms/platform-sap.md) |  | [Dremio Cloud](../../technologies/sap/dremio-cloud.md), [SAP Knowledge Graph](../../technologies/sap/sap-knowledge-graph.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Tera](../../technologies/teradata/teradata-tera.md) (preview) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | Semantic Models | [Dataiku Semantic Models](../../technologies/dataiku/dataiku-semantic-models.md) (unconfirmed) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md), [OpenMetadata](../../technologies/open-source/openmetadata.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Atlan](../../technologies/independent/atlan.md), [AtScale](../../technologies/independent/atscale.md), [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [Cube Cloud](../../technologies/independent/cube-cloud.md), [data.world](../../technologies/independent/data-world.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [dbt Semantic Layer](../../technologies/independent/dbt-semantic-layer.md), [Omni Analytics](../../technologies/independent/omni.md), [Select Star](../../technologies/independent/select-star.md), [Tableau Next](../../technologies/independent/tableau-next.md) |
