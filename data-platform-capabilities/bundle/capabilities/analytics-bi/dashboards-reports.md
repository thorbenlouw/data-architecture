---
type: Capability
id: dashboards-reports
title: Dashboards and interactive reports
description: Build and share visual, interactive dashboards with filters and drill-down.
aliases: [viz, data visualisation]
broader: [analytics-bi]
related: [semantic-layer, data-certification, usage-metadata, row-level-security, result-caching]
depends_on: [sql-access]
tags: [analytics-bi]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A dashboard puts several charts, tables and headline figures on one screen, linked by shared filters, so choosing a region or date range updates everything at once. Users drill from a summary to detail, for example from monthly sales by country to the orders behind one figure, and save or share their views. Dashboards query the platform live or work from extracts cached in the BI tool, refreshed on a schedule or on demand.

Dashboards serve monitoring and routine decisions, where the same questions come up again and again. They differ from ad hoc analysis, which answers new questions, and from paginated reports, which fix layout for printing. The main choices are between centrally built, certified dashboards and self-service building by business users, and between live connections and extracts. Most organisations need both kinds of content, with a clear signal of which is trusted.

# Key considerations

- Dashboards multiply. Track usage and retire unused ones, or search results fill with near duplicates.
- Live queries keep one copy of data and one security model but put user load on the platform. Extracts are fast but need their own refresh schedule and access controls.
- Interactive filters generate many queries per page view. Test performance with realistic concurrency, not a single user.
- Row-level security must still hold when a dashboard is shared, exported or emailed.

# Questions to ask

- How many viewers and creators are expected, and how many are active at peak?
- How fresh must dashboard data be: daily, hourly or near real time?
- Who may publish dashboards that others treat as trusted?
- Do users export underlying data, and must exports respect the same access rules?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Analytics and BI](analytics-bi.md) |
| Broader | [Analytics and BI](analytics-bi.md) |
| Narrower | [Dashboards as code](dashboards-as-code.md) |
| Related | [Data certification](../metadata/data-certification.md), [Geospatial data](../specialised-data/geospatial-data.md), [Result caching](../compute/result-caching.md), [Row-level security](../security/row-level-security.md), [Semantic layer](semantic-layer.md), [Usage and popularity metadata](../metadata/usage-metadata.md) |
| Depends on | [SQL and programmatic access](../serving/sql-access.md) |

# Where it appears

- **Use cases:** [Enterprise management reporting](../../use-cases/usecase-enterprise-reporting.md) (requires, level 3) · [Operational reporting](../../use-cases/usecase-operational-reporting.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md)
- **Maturity tracks:** [Analytics and BI](../../maturity/track-analytics-bi.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 8 – Comprehensiveness; Principle 9 – Clarity and usefulness · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Warehousing and Business Intelligence

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Quick Sight](../../technologies/aws/aws-quick-sight.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Real-Time Dashboard](../../technologies/microsoft/fabric-real-time-dashboards.md), [Maps in Microsoft Fabric](../../technologies/microsoft/fabric-maps.md) (preview), [Power BI Report Server](../../technologies/microsoft/powerbi-report-server.md), [Power BI reports and dashboards](../../technologies/microsoft/powerbi-reports.md), [Power BI scorecards and goals](../../technologies/microsoft/powerbi-scorecards.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Looker; Data Studio (formerly Looker Studio) | [Google Data Studio](../../technologies/google-cloud/gcp-data-studio.md), [Looker](../../technologies/google-cloud/gcp-looker.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowsight dashboards](../../technologies/snowflake/snowflake-snowsight-dashboards.md), [Streamlit in Snowflake](../../technologies/snowflake/snowflake-streamlit.md) |
| [Databricks](../../platforms/platform-databricks.md) | AI/BI dashboards | [Databricks AI/BI dashboards](../../technologies/databricks/databricks-ai-bi-dashboards.md), [Genie One](../../technologies/databricks/databricks-genie-one.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud SQL console (with Dashboards and ClickHouse Assistant)](../../technologies/clickhouse/clickhouse-sql-console.md), [ClickHouse data source plugin for Grafana](../../technologies/clickhouse/clickhouse-grafana-plugin.md), [ClickStack](../../technologies/clickhouse/clickhouse-clickstack.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Visualization](../../technologies/cloudera/cloudera-data-visualization.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Analytics Cloud](../../technologies/oracle/oracle-analytics-cloud.md), [Oracle Fusion Data Intelligence](../../technologies/oracle/oracle-fusion-data-intelligence.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Analytics Cloud](../../technologies/sap/sap-analytics-cloud.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Contour and Quiver](../../technologies/palantir/palantir-contour-quiver.md), [Palantir Workshop](../../technologies/palantir/palantir-workshop.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Superset](../../technologies/open-source/apache-superset.md), [Lightdash](../../technologies/open-source/lightdash.md), [Metabase](../../technologies/open-source/metabase.md), [OpenSearch](../../technologies/open-source/opensearch.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [dbt Charts](../../technologies/independent/dbt-charts.md) (unconfirmed), [Domo](../../technologies/independent/domo.md), [Omni Analytics](../../technologies/independent/omni.md), [Qlik Cloud Analytics](../../technologies/independent/qlik-cloud-analytics.md), [Sigma Computing](../../technologies/independent/sigma.md), [Sisense](../../technologies/independent/sisense.md), [Tableau Cloud](../../technologies/independent/tableau-cloud.md), [ThoughtSpot Analytics](../../technologies/independent/thoughtspot-analytics.md) |

Narrower capabilities are realised by a further 5 technologies; see their pages.
