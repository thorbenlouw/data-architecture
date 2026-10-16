---
type: Use Case
id: usecase-self-service-bi
title: Self-service BI
description: Analysts and business users explore governed data and build their own reports with trusted metrics.
aliases: [self-service analytics, governed self-service]
requires:
- {capability: semantic-layer, level: 3, why: Measures and joins defined once stop each self-built report from calculating KPIs its own way.}
- {capability: metric-definitions, level: 3, why: 'Key metrics need named owners and certified logic, or self-service multiplies conflicting definitions.'}
- {capability: dashboards-reports, level: 3, why: 'Users build and share dashboards themselves, using the platform''s standard tooling.'}
- {capability: ad-hoc-analysis, level: 2, why: Many questions are one-off and are answered by exploration rather than by a new dashboard.}
- {capability: data-catalogue, level: 3, why: Users have to find the right dataset and its definition without asking an engineer.}
- {capability: data-certification, level: 2, why: 'Users need to tell trusted, curated datasets apart from raw or experimental ones.'}
- {capability: sql-transformation, level: 2, why: 'Raw data must be modelled into clean, joined, analysis-ready tables before users can build on it.'}
- {capability: role-based-access, level: 3, why: 'Access is granted through roles mapped to groups, not one person and one report at a time.'}
- {capability: row-level-security, level: 3, why: 'One shared dashboard must show each region, branch or team only its own rows.'}
- {capability: access-requests, level: 2, why: Self-service stalls if getting access to a new dataset takes weeks of email.}
- {capability: identity-authentication, level: 3, why: 'Single sign-on lets BI tools pass the user''s identity through, so data permissions apply in every tool.'}
- {capability: sql-query-engine, level: 2, why: Interactive queries over large tables must return in seconds.}
- {capability: workload-isolation, level: 2, why: Unpredictable user queries must not slow the scheduled pipelines that refresh the data.}
- {capability: spend-controls, level: 2, why: 'Query timeouts, scan limits and budgets stop open-ended ad hoc queries from running up compute spend.'}
- capability: column-masking
  level: 2
  why: Self-built reports and exports draw on tables that hold personal fields, which must stay masked for users who do not need them.
- capability: data-trust-indicators
  level: 2
  why: The use case's own requirement that each dataset shows its actual freshness and state has to appear where users build and read reports.
benefits_from:
- {capability: business-glossary, why: Plain-language definitions of business terms cut misinterpretation of fields and measures.}
- {capability: freshness-monitoring, why: Users see when data is late instead of drawing conclusions from yesterday's figures.}
- {capability: result-caching, why: Popular dashboards load quickly and cost less when results are reused.}
- {capability: elastic-scaling, why: Compute grows for month-end and Monday-morning peaks in concurrent users.}
- {capability: spreadsheet-integration, why: Users who work in spreadsheets can stay on governed data instead of exporting copies.}
- {capability: usage-metadata, why: Usage figures show which reports to promote and which to retire.}
- {capability: conversational-analytics, why: Less technical users can ask questions in plain language over the same semantic layer.}
- {capability: data-preparation, why: Analysts can combine their own files with curated data without starting a pipeline project.}
- {capability: cost-attribution, why: Teams see what their dashboards and queries cost.}
- {capability: transformation-as-code, why: 'Curated models built as tested, documented code can grow with demand without breaking existing reports.'}
- {capability: analytical-sandboxes, why: Users combine their own files with curated data inside the platform instead of in exported copies.}
- {capability: data-loss-prevention, why: 'Limits or logs bulk downloads of sensitive data, a listed risk and requirement.'}
personas:
- persona-data-analyst
- persona-business-user
- persona-analytics-engineer
- persona-data-steward
- persona-data-engineer
- persona-platform-engineer
patterns: [dimensional-modelling, data-marts, one-big-table, medallion-architecture]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

When every new report has to go through a central BI team, requests queue for weeks and people fall back on extracts and spreadsheets that soon disagree with each other. Self-service BI moves report building to analysts and business users, but only over curated, documented datasets and shared metric definitions, so that the freedom does not produce many versions of the same number. Engineers and analytics engineers load and model the data, the semantic layer defines measures and joins once, and users explore, build and share dashboards on top of it within the permissions they already hold.

Good looks like this: most new questions are answered without an engineering ticket, the same KPI gives the same value in every report, users can tell which datasets are certified, and the curated layer grows with demand rather than being bypassed. Usage figures show which reports matter and which can be retired.

# Non-functional requirements

- Common dashboard interactions return within a few seconds at peak concurrency, which is often hundreds of users at month end.
- Each curated dataset publishes its expected freshness, typically daily or hourly, and its actual state.
- The same access rules apply whether data is reached through BI, SQL or a spreadsheet connection.
- Exports and downloads of sensitive data are limited or logged.

# Risks

- Report sprawl, with thousands of unofficial dashboards whose definitions conflict.
- Ad hoc queries without limits drive up compute spend.
- The curated layer does not cover users' real questions, so they go back to raw data and spreadsheets.
- Sensitive data leaks through extracts that leave the platform's controls.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Measures and joins defined once stop each self-built report from calculating KPIs its own way. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Key metrics need named owners and certified logic, or self-service multiplies conflicting definitions. |
| [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Users build and share dashboards themselves, using the platform's standard tooling. |
| [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Many questions are one-off and are answered by exploration rather than by a new dashboard. |
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Users have to find the right dataset and its definition without asking an engineer. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Users need to tell trusted, curated datasets apart from raw or experimental ones. |
| [SQL transformation](../capabilities/processing/sql-transformation.md) | [Processing and transformation](../capabilities/processing/processing.md) | 2 (Managed) | Raw data must be modelled into clean, joined, analysis-ready tables before users can build on it. |
| [Role-based access control](../capabilities/security/role-based-access.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Access is granted through roles mapped to groups, not one person and one report at a time. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | One shared dashboard must show each region, branch or team only its own rows. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Self-service stalls if getting access to a new dataset takes weeks of email. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Single sign-on lets BI tools pass the user's identity through, so data permissions apply in every tool. |
| [SQL query engine](../capabilities/compute/sql-query-engine.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Interactive queries over large tables must return in seconds. |
| [Workload isolation](../capabilities/compute/workload-isolation.md) | [Query and compute](../capabilities/compute/compute.md) | 2 (Managed) | Unpredictable user queries must not slow the scheduled pipelines that refresh the data. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Query timeouts, scan limits and budgets stop open-ended ad hoc queries from running up compute spend. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Self-built reports and exports draw on tables that hold personal fields, which must stay masked for users who do not need them. |
| [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | The use case's own requirement that each dataset shows its actual freshness and state has to appear where users build and read reports. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Business glossary](../capabilities/metadata/business-glossary.md) | Plain-language definitions of business terms cut misinterpretation of fields and measures. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | Users see when data is late instead of drawing conclusions from yesterday's figures. |
| [Result caching](../capabilities/compute/result-caching.md) | Popular dashboards load quickly and cost less when results are reused. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | Compute grows for month-end and Monday-morning peaks in concurrent users. |
| [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md) | Users who work in spreadsheets can stay on governed data instead of exporting copies. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | Usage figures show which reports to promote and which to retire. |
| [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) | Less technical users can ask questions in plain language over the same semantic layer. |
| [Self-service data preparation](../capabilities/processing/data-preparation.md) | Analysts can combine their own files with curated data without starting a pipeline project. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | Teams see what their dashboards and queries cost. |
| [Transformation as code](../capabilities/processing/transformation-as-code.md) | Curated models built as tested, documented code can grow with demand without breaking existing reports. |
| [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md) | Users combine their own files with curated data inside the platform instead of in exported copies. |
| [Data loss prevention](../capabilities/security/data-loss-prevention.md) | Limits or logs bulk downloads of sensitive data, a listed risk and requirement. |

# Personas

- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.

# Patterns

- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [Data marts](../patterns/data-marts.md)
- [One big table](../patterns/one-big-table.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 13 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data certification](../capabilities/metadata/data-certification.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 16 of 16 |  |
| [Google Cloud](../platforms/platform-google-cloud.md) | 15 of 16 | [Data certification](../capabilities/metadata/data-certification.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 14 of 16 | [Data certification](../capabilities/metadata/data-certification.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Databricks](../platforms/platform-databricks.md) | 15 of 16 | [Access requests and reviews](../capabilities/security/access-requests.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 10 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data certification](../capabilities/metadata/data-certification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Informatica](../platforms/platform-informatica.md) | 6 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Data certification](../capabilities/metadata/data-certification.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 8 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data certification](../capabilities/metadata/data-certification.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 16 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Data certification](../capabilities/metadata/data-certification.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Role-based access control](../capabilities/security/role-based-access.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [SAP](../platforms/platform-sap.md) | 7 of 16 | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Data certification](../capabilities/metadata/data-certification.md), [Role-based access control](../capabilities/security/role-based-access.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Teradata](../platforms/platform-teradata.md) | 4 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data certification](../capabilities/metadata/data-certification.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [IBM](../platforms/platform-ibm.md) | 4 of 16 | [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Data certification](../capabilities/metadata/data-certification.md), [SQL transformation](../capabilities/processing/sql-transformation.md), [Role-based access control](../capabilities/security/role-based-access.md), [Row-level security](../capabilities/security/row-level-security.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Palantir](../platforms/platform-palantir.md) | 9 of 16 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data certification](../capabilities/metadata/data-certification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [SQL query engine](../capabilities/compute/sql-query-engine.md), [Workload isolation](../capabilities/compute/workload-isolation.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 12 of 16 | [Data certification](../capabilities/metadata/data-certification.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| [Independent vendors](../platforms/platform-independent.md) | 13 of 16 | [Role-based access control](../capabilities/security/role-based-access.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) |
