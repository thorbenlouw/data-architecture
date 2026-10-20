---
type: Capability
id: metric-definitions
title: Governed metric definitions
description: Define, certify and version key business metrics with owners and calculation logic.
aliases: [metric store, KPI definitions, certified metrics, metric catalogue, KPI catalogue]
broader: [semantic-layer]
related: [business-glossary, data-certification, critical-data-elements, column-lineage, data-ownership]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Take monthly recurring revenue or churn rate. As a governed metric, each is recorded with its calculation, the dimensions it can be cut by, its time grain, an accountable owner and a certification status. Definitions are versioned, so when finance changes how churn treats paused accounts, the old and new versions are both kept with an effective date and consumers can see what changed and when.

Metrics are the part of a semantic model most often argued about, so they need more control than ordinary fields: review before change, a named owner, and documentation that ties the number to its business meaning. Definitions are increasingly written as code in version-controlled files, which gives review and history, though some teams manage them through a catalogue interface. A governed metric differs from a glossary term: the glossary explains what active customer means in words, while the metric definition is the calculation a tool can execute.

# Key considerations

- Not every measure needs governance. Start with the few dozen metrics that reach executives, regulators or customers, and certify those.
- Ratios and distinct counts cannot be summed across groups. Definitions must say how a metric aggregates, or tools will roll it up wrongly.
- Agree how definition changes are announced and whether history is restated, since a changed metric breaks comparisons with past reports.
- Link each metric to its glossary term and to lineage, so people can trace a number back to its sources.

# Questions to ask

- Which metrics are reported externally or to the board, and who signs them off?
- When two teams calculate the same metric differently, who decides which is right?
- Must past reports be reproducible after a definition changes?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Semantic layer](semantic-layer.md) |
| Related | [Approximate query processing](../compute/approximate-query-processing.md), [Business glossary](../metadata/business-glossary.md), [Column-level lineage](../metadata/column-lineage.md), [Conversational analytics](conversational-analytics.md), [Critical data elements](../governance/critical-data-elements.md), [Data certification](../metadata/data-certification.md), [Experimentation and causal measurement](experimentation.md), [Ownership and stewardship](../governance/data-ownership.md), [Packaged analytics content](packaged-analytics.md), [Semantic model interchange](semantic-model-interchange.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3)
- **Patterns:** [Data marts](../../patterns/data-marts.md) · [Dimensional modelling](../../patterns/dimensional-modelling.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Business user](../../personas/persona-business-user.md) · [Chief data officer](../../personas/persona-cdo.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 7 – Accuracy (reporting); Principle 8 – Comprehensiveness · [DCAM v3](../../frameworks/framework-edm-dcam.md): 8 Analytics Management

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | DAX measures; scorecard goals | [Power BI semantic models](../../technologies/microsoft/powerbi-semantic-models.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [LookML](../../technologies/google-cloud/gcp-lookml.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake semantic views](../../technologies/snowflake/snowflake-semantic-views.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog metric views](../../technologies/databricks/databricks-metric-views.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere catalog and Data Marketplace](../../technologies/sap/sap-datasphere-catalog.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Semantic Models](../../technologies/dataiku/dataiku-semantic-models.md) (unconfirmed) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Ossie (incubating)](../../technologies/open-source/apache-ossie.md) (preview), [Cube Core](../../technologies/open-source/cube-core.md), [MetricFlow](../../technologies/open-source/metricflow.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [AtScale](../../technologies/independent/atscale.md), [Cube Cloud](../../technologies/independent/cube-cloud.md), [dbt Semantic Layer](../../technologies/independent/dbt-semantic-layer.md), [Tableau Pulse](../../technologies/independent/tableau-pulse.md) |
