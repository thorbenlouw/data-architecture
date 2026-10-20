---
type: Capability
id: semantic-layer
title: Semantic layer
description: Define business entities, measures and relationships once so every tool calculates them the same way.
aliases:
- metrics layer
- semantic model
- headless BI
- universal semantic layer
- semantic views
- metric views
- business layer
- OLAP cube
broader: [analytics-bi]
related: [ai-context-layer, business-glossary, conversational-analytics, data-modelling, query-acceleration]
depends_on: [sql-query-engine]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A semantic layer is a model that maps physical tables to business concepts: entities such as customer and order, the joins between them, dimensions to group by, and measures with their aggregation rules. A tool asks for revenue by region for last quarter, and the layer generates the SQL with the correct joins, filters and access rules. Revenue is defined once, for example as invoiced amount less credit notes, excluding internal accounts, and every dashboard, spreadsheet and AI agent gets the same figure.

It matters once several tools or teams report the same numbers and disagree. Approaches differ in where the model lives: inside one BI tool, as a standalone service that many tools query through SQL or APIs, or as definitions held in the warehouse itself. A semantic layer is not a transformation layer. Transformation builds and stores tables; the semantic layer describes how to query them at request time, though it may also manage caches or pre-aggregations for speed.

# Key considerations

- A layer tied to one BI tool gives consistency only inside that tool. Check which other tools, including spreadsheets, notebooks and AI agents, can query it.
- Decide what belongs in modelled tables and what in the layer. Complex, stable logic is usually better materialised upstream; the layer suits aggregation, joins and filters that vary by question.
- Generated SQL can be slow on large data. Check support for pre-aggregations or caching and how they stay correct as data changes.
- Row and column security must apply to queries through the layer as well as direct queries, ideally by passing the user's identity down to platform controls.

# Questions to ask

- How many tools need the same business definitions, and which ones?
- Who will own the model, and how are changes to it reviewed?
- Do AI agents or natural-language tools need to query metrics reliably?
- Is there one dominant BI tool whose own model could serve, or a mix of tools?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Narrower | [Governed metric definitions](metric-definitions.md), [Semantic model interchange](semantic-model-interchange.md) |
| Related | [Serving and activation](../serving/serving.md), [Metadata and discovery](../metadata/metadata.md), [Agent tool and data access](../generative-ai/agent-tool-access.md), [AI context layer](../metadata/ai-context-layer.md), [Business glossary](../metadata/business-glossary.md), [Conversational analytics](conversational-analytics.md), [Dashboards and interactive reports](dashboards-reports.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [End-to-end lineage](../metadata/cross-system-lineage.md), [Hierarchy management](../master-data/hierarchy-management.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Packaged analytics content](packaged-analytics.md), [Query acceleration](../compute/query-acceleration.md), [Read-optimised views](../serving/read-optimised-views.md), [Result caching](../compute/result-caching.md), [Spreadsheet integration](spreadsheet-integration.md) |
| Depends on | [SQL query engine](../compute/sql-query-engine.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Data warehouse](../../patterns/data-warehouse.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 4 – Completeness; Principle 6 – Adaptability; Principle 8 – Comprehensiveness · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence · [DCAM v3](../../frameworks/framework-edm-dcam.md): 4 Business Data Knowledge · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Context

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Semantic model (formerly dataset) | [Azure Analysis Services](../../technologies/microsoft/azure-analysis-services.md), [Fabric IQ ontology](../../technologies/microsoft/fabric-iq-ontology.md) (preview), [Power BI semantic models](../../technologies/microsoft/powerbi-semantic-models.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | LookML | [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | semantic views | [Snowflake Horizon Context](../../technologies/snowflake/snowflake-horizon-context.md) (preview), [Snowflake semantic views](../../technologies/snowflake/snowflake-semantic-views.md) |
| [Databricks](../../platforms/platform-databricks.md) | Unity Catalog metric views | [Unity Catalog metric views](../../technologies/databricks/databricks-metric-views.md) |
| [Oracle](../../platforms/platform-oracle.md) | Semantic model (RPD) | [Oracle Analytics Cloud](../../technologies/oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../../technologies/oracle/oracle-fusion-data-intelligence.md) |
| [SAP](../../platforms/platform-sap.md) | Business Builder / analytic models | [Dremio Cloud](../../technologies/sap/dremio-cloud.md), [SAP BW/4HANA](../../technologies/sap/sap-bw4hana.md), [SAP Datasphere](../../technologies/sap/sap-datasphere.md), [SAP Knowledge Graph](../../technologies/sap/sap-knowledge-graph.md) |
| [Palantir](../../platforms/platform-palantir.md) | Ontology | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Cube Core](../../technologies/open-source/cube-core.md), [Lightdash](../../technologies/open-source/lightdash.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [AtScale](../../technologies/independent/atscale.md), [Cube Cloud](../../technologies/independent/cube-cloud.md), [dbt Semantic Layer](../../technologies/independent/dbt-semantic-layer.md), [Denodo Platform](../../technologies/independent/denodo-platform.md), [Omni Analytics](../../technologies/independent/omni.md), [Select Star](../../technologies/independent/select-star.md), [Tableau Next](../../technologies/independent/tableau-next.md), [ThoughtSpot Analytics](../../technologies/independent/thoughtspot-analytics.md) |

Narrower capabilities are realised by a further 14 technologies; see their pages.
