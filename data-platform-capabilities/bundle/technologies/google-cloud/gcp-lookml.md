---
type: Technology
id: gcp-lookml
title: LookML
description: Looker's Git-backed modelling language for defining dimensions, measures, joins and access rules once for all queries.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [semantic-layer, metric-definitions, version-control, ci-cd, data-testing, dashboards-as-code]
resource: https://docs.cloud.google.com/looker/docs/what-is-lookml
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Looker Continuous Integration (GA) validates SQL, content and LookML on pull requests and can run from GitHub Actions, GitLab CI or dbt Cloud. A VS Code extension with a LookML agent went GA in September 2026, and a visual modelling canvas is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI) (primary): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md) (Analytics and BI): Define, certify and version key business metrics with owners and calculation logic.
- [Version control integration](../../capabilities/development-lifecycle/version-control.md) (Development and DataOps): Keep code and configuration in Git and work with branches from inside the platform.
- [CI/CD](../../capabilities/development-lifecycle/ci-cd.md) (Development and DataOps): Build, test and deploy pipelines, models and infrastructure automatically on every change.
- [Data pipeline testing](../../capabilities/development-lifecycle/data-testing.md) (Development and DataOps): Test transformation logic and data with unit, integration and regression tests before release.
- [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) (Analytics and BI): Define dashboards in version-controlled files that are reviewed and tested alongside the models they use.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** Looker

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI semantic models](../microsoft/powerbi-semantic-models.md), [Azure Analysis Services](../microsoft/azure-analysis-services.md), [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake semantic views](../snowflake/snowflake-semantic-views.md), [Snowflake Horizon Context](../snowflake/snowflake-horizon-context.md) (preview) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog metric views](../databricks/databricks-metric-views.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Analytics Cloud](../oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../oracle/oracle-fusion-data-intelligence.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP BW/4HANA](../sap/sap-bw4hana.md), [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [Dremio Cloud](../sap/dremio-cloud.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Cube Core](../open-source/cube-core.md), [Lightdash](../open-source/lightdash.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md), [Dashboards as code](../../capabilities/analytics-bi/dashboards-as-code.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [AtScale](../independent/atscale.md), [dbt Semantic Layer](../independent/dbt-semantic-layer.md), [Cube Cloud](../independent/cube-cloud.md) | [Governed metric definitions](../../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
