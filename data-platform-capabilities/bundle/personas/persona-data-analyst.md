---
type: Persona
id: persona-data-analyst
title: Data analyst
description: Answers business questions through analysis, dashboards and reports.
cares_about:
- data-catalogue
- data-certification
- data-trust-indicators
- metric-definitions
- semantic-layer
- ad-hoc-analysis
- dashboards-reports
- business-glossary
- sql-access
- access-requests
- freshness-monitoring
- analytical-sandboxes
- data-preparation
- spreadsheet-integration
- column-lineage
- notebooks
- conversational-analytics
- data-alerting
- data-issue-management
- usage-metadata
- row-level-security
- column-masking
- elastic-scaling
patterns: [dimensional-modelling, data-marts, one-big-table]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data analysts work for a function such as finance, sales, operations, marketing or HR, or in a central analytics team serving several. They write SQL, build dashboards and reports, and explain to managers what the figures mean. A large part of their week goes on recurring reports, one-off requests and working out why a number looks wrong.

Success is answers that stakeholders act on, delivered quickly, with figures that match other reports. Good analysts spend most of their time on interpretation and recommendation, not on finding, cleaning and reconciling data.

# Goals

- Find the right, trusted data quickly.
- Answer questions in hours rather than weeks.
- Produce figures that reconcile with finance and with other teams' reports.
- Automate recurring reports so time goes on analysis.

# Jobs

- Search the catalogue for datasets and check their definitions and freshness.
- Write SQL and explore data to answer one-off questions.
- Build and maintain dashboards and scheduled reports.
- Prepare and combine data, including files from the business, for analysis.
- Explain and reconcile figures that differ between reports.
- Request access to new data.
- Upload business files and combine them with platform data in a shared team space.
- Report a wrong or late figure to the data owner and follow it to resolution.
- Hand over an analysis that others now rely on so it can become a governed dataset or dashboard.

# Pain points

- Several similar tables exist and it is unclear which one is correct.
- Access approvals take days or weeks.
- Dashboards disagree because definitions differ.
- Data is stale with nothing to say it is late.
- Queries on large tables slow down at month end.
- Combining their own files with platform data means exporting to a laptop or raising a pipeline request.
- Dashboards and tables give no sign that data is late or that a check failed overnight.

# Questions they ask

- Which dataset is the certified source for this measure?
- Can I combine my spreadsheet with platform data without starting a pipeline project?
- How fresh is this data, and how will I know when it is late?
- Why can I not see some rows or columns, and how do I get access?
- Where can my team keep uploaded files and our own tables, and for how long?
- How do I tell the owner that a number is wrong, and how will I know it has been fixed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Capabilities they rely on most

| Capability | Domain | What it does |
|---|---|---|
| [Data catalogue](../capabilities/metadata/data-catalogue.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Provide a searchable inventory of data assets with descriptions, owners, quality and usage. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Mark assets as trusted, deprecated or under review so consumers know what to rely on. |
| [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show consumers, where they use data, whether a dataset, dashboard or answer is certified, fresh, passing its checks and free of open incidents. |
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define, certify and version key business metrics with owners and calculation logic. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Define business entities, measures and relationships once so every tool calculates them the same way. |
| [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Explore data freely with SQL editors, pivots and visual exploration to answer one-off questions. |
| [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Build and share visual, interactive dashboards with filters and drill-down. |
| [Business glossary](../capabilities/metadata/business-glossary.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Define business terms and link them to the data that represents them. |
| [SQL and programmatic access](../capabilities/serving/sql-access.md) | [Serving and activation](../capabilities/serving/serving.md) | Connect tools and code to the platform through standard drivers and protocols. |
| [Access requests and reviews](../capabilities/security/access-requests.md) | [Security and access](../capabilities/security/security.md) | Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Detect when data arrives later than expected or misses its freshness target. |
| [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Give analysts and teams governed spaces on the platform where they can upload files, create tables and try out analyses, with quotas, expiry and the platform's access controls. |
| [Self-service data preparation](../capabilities/processing/data-preparation.md) | [Processing and transformation](../capabilities/processing/processing.md) | Let analysts profile, clean and reshape data interactively without engineering help. |
| [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Work with governed platform data directly from spreadsheet tools. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Track how each column is derived from source columns. |
| [Notebooks](../capabilities/development-lifecycle/notebooks.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | Develop interactively with code, results and narrative together, with collaboration and scheduling. |
| [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Ask questions of data in natural language and get answers, charts or SQL back. |
| [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | Notify people when data crosses thresholds, or deliver reports to them on a schedule. |
| [Data issue management](../capabilities/data-quality/data-issue-management.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | Log, assign, track and resolve data quality incidents with their owners. |
| [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | Show who uses which data, how often and how, to guide discovery and clean-up. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | Restrict which rows each user sees based on who they are. |
| [Column security and dynamic masking](../capabilities/security/column-masking.md) | [Security and access](../capabilities/security/security.md) | Hide or mask sensitive columns depending on who is querying. |
| [Elastic scaling](../capabilities/compute/elastic-scaling.md) | [Query and compute](../capabilities/compute/compute.md) | Add and remove compute automatically as load changes, including for bursts of concurrent users. |

# Patterns

- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [Data marts](../patterns/data-marts.md)
- [One big table](../patterns/one-big-table.md)

# Use cases they take part in

- [Conversational analytics for business users](../use-cases/usecase-conversational-bi.md): Business users ask questions of governed data in plain language and get trustworthy answers.
- [Demand forecasting](../use-cases/usecase-demand-forecasting.md): Forecast demand by product, location and time to plan stock, staff and supply.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md): Produce trusted, consistent KPIs and management reports across the organisation.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md): Build audiences from platform data and sync them to marketing and advertising tools.
- [Operational reporting](../use-cases/usecase-operational-reporting.md): Report on current operations within minutes of events happening.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md): Produce accurate, auditable and reproducible submissions to regulators.
- [Self-service BI](../use-cases/usecase-self-service-bi.md): Analysts and business users explore governed data and build their own reports with trusted metrics.
