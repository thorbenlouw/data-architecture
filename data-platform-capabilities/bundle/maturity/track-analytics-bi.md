---
type: Maturity Track
id: track-analytics-bi
title: Analytics and BI
description: How consistently people across the organisation explore, report on and act on data using shared definitions and governed tools.
covers:
- analytics-bi
- semantic-layer
- metric-definitions
- semantic-model-interchange
- dashboards-reports
- dashboards-as-code
- paginated-reports
- ad-hoc-analysis
- conversational-analytics
- augmented-analytics
- embedded-analytics
- spreadsheet-integration
- data-alerting
- data-writeback
- enterprise-planning
- data-consumer-portal
- packaged-analytics
- analytical-sandboxes
- external-identity
- experimentation
related_tracks: [track-serving, track-metadata-catalogue, track-master-data]
levels:
- level: 1
  name: Initial
  summary: Reporting is built by individuals in spreadsheets and desktop files from extracts.
  criteria:
  - Key figures such as revenue or headcount differ between reports because each author calculates them separately.
  - Reports are built in spreadsheets or desktop BI files from extracts and shared by email.
  - There is no list of which reports exist or who uses them.
  capabilities: [ad-hoc-analysis]
- level: 2
  name: Managed
  summary: A BI team publishes dashboards and scheduled reports from the platform on a shared BI service.
  criteria:
  - Dashboards on the BI service connect to platform tables or refreshed extracts, not to personal files.
  - The BI team maintains core dashboards with filters and drill-down for the main business areas.
  - Formatted, printable operational and regulatory reports are produced from the same platform data.
  - Scheduled deliveries and threshold alerts replace reports circulated by hand.
  - Standard reporting for a packaged business application uses the vendor's prebuilt content where it fits.
  capabilities: [dashboards-reports, paginated-reports, data-alerting, packaged-analytics]
- level: 3
  name: Defined
  summary: Metrics and business models are defined once in a semantic layer and reused by every tool.
  criteria:
  - Core metrics are defined in a semantic layer with owner, formula and version, and certified dashboards may use only these definitions.
  - Business users build their own reports and pivots, including from spreadsheet tools, on governed semantic models, and analysts try out new data in sandboxes with quotas, expiry dates and the platform's access controls instead of taking extracts.
  - Dashboards are stored as versioned definitions and deployed through the same review process as the models they use.
  - Each user has one portal listing the dashboards, apps and agents shared with them, with certification status shown.
  - Targets and corrections entered by users are written back to governed tables with an audit trail instead of offline spreadsheets.
  capabilities:
  - semantic-layer
  - metric-definitions
  - dashboards-as-code
  - spreadsheet-integration
  - data-consumer-portal
  - data-writeback
  - analytical-sandboxes
- level: 4
  name: Measured
  summary: Usage, performance and the accuracy of self-service answers are measured against targets.
  criteria:
  - Report usage is measured, and dashboards with no views in 90 days are flagged to their owners for retirement.
  - Natural-language questions are answered through the semantic layer, and accuracy is scored against a set of reference questions.
  - Dashboard load times are tracked against a target, and regressions are reported to owners.
  - Analytics embedded in customer-facing applications has monitored uptime, signs external users in through a customer and partner identity service, and has tested tenant isolation.
  - Budgets and forecasts are built on governed data with versioned plans and approval workflows.
  capabilities: [conversational-analytics, embedded-analytics, enterprise-planning, external-identity]
- level: 5
  name: Optimising
  summary: Insight is pushed to owners proactively, the effect of actions is measured with controlled experiments, and definitions and models improve from what users fail to find.
  criteria:
  - Anomalies and drivers in key metrics are surfaced to owners automatically, and the share of alerts that lead to action is tracked.
  - Metric definitions are exchanged between BI, semantic and AI tools in a standard format, so one edit reaches every tool.
  - Questions that self-service could not answer are logged and used to extend the semantic models.
  - Actions such as campaigns, price changes and product features are tested against holdout groups, and their measured effect, with its uncertainty, is recorded before wider rollout.
  capabilities: [augmented-analytics, semantic-model-interchange, experimentation]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up replaces conflicting spreadsheets and one-off reports with metrics defined once, dashboards reviewed like code, and self-service that lets business users answer their own questions, including in natural language, without getting different numbers. Typical blockers are metric logic duplicated inside each BI tool, report sprawl that nobody prunes, and a central analytics team that becomes a bottleneck because nobody trusts self-service results.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Reporting is built by individuals in spreadsheets and desktop files from extracts.

- Key figures such as revenue or headcount differ between reports because each author calculates them separately.
- Reports are built in spreadsheets or desktop BI files from extracts and shared by email.
- There is no list of which reports exist or who uses them.

**Capabilities first relied on:** [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md)

## Level 2: Managed

A BI team publishes dashboards and scheduled reports from the platform on a shared BI service.

- Dashboards on the BI service connect to platform tables or refreshed extracts, not to personal files.
- The BI team maintains core dashboards with filters and drill-down for the main business areas.
- Formatted, printable operational and regulatory reports are produced from the same platform data.
- Scheduled deliveries and threshold alerts replace reports circulated by hand.
- Standard reporting for a packaged business application uses the vendor's prebuilt content where it fits.

**Capabilities first relied on:** [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md)

## Level 3: Defined

Metrics and business models are defined once in a semantic layer and reused by every tool.

- Core metrics are defined in a semantic layer with owner, formula and version, and certified dashboards may use only these definitions.
- Business users build their own reports and pivots, including from spreadsheet tools, on governed semantic models, and analysts try out new data in sandboxes with quotas, expiry dates and the platform's access controls instead of taking extracts.
- Dashboards are stored as versioned definitions and deployed through the same review process as the models they use.
- Each user has one portal listing the dashboards, apps and agents shared with them, with certification status shown.
- Targets and corrections entered by users are written back to governed tables with an audit trail instead of offline spreadsheets.

**Capabilities first relied on:** [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md)

## Level 4: Measured

Usage, performance and the accuracy of self-service answers are measured against targets.

- Report usage is measured, and dashboards with no views in 90 days are flagged to their owners for retirement.
- Natural-language questions are answered through the semantic layer, and accuracy is scored against a set of reference questions.
- Dashboard load times are tracked against a target, and regressions are reported to owners.
- Analytics embedded in customer-facing applications has monitored uptime, signs external users in through a customer and partner identity service, and has tested tenant isolation.
- Budgets and forecasts are built on governed data with versioned plans and approval workflows.

**Capabilities first relied on:** [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [External user and tenant identity](../capabilities/security/external-identity.md)

## Level 5: Optimising

Insight is pushed to owners proactively, the effect of actions is measured with controlled experiments, and definitions and models improve from what users fail to find.

- Anomalies and drivers in key metrics are surfaced to owners automatically, and the share of alerts that lead to action is tracked.
- Metric definitions are exchanged between BI, semantic and AI tools in a standard format, so one edit reaches every tool.
- Questions that self-service could not answer are logged and used to extend the semantic models.
- Actions such as campaigns, price changes and product features are tested against holdout groups, and their measured effect, with its uncertainty, is recorded before wider rollout.

**Capabilities first relied on:** [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md)

# Capabilities in scope

[Analytics and BI](../capabilities/analytics-bi/analytics-bi.md), [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Augmented analytics](../capabilities/analytics-bi/augmented-analytics.md), [Conversational analytics](../capabilities/analytics-bi/conversational-analytics.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Dashboards as code](../capabilities/analytics-bi/dashboards-as-code.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Data entry and write-back](../capabilities/analytics-bi/data-writeback.md), [Embedded analytics](../capabilities/analytics-bi/embedded-analytics.md), [Experimentation and causal measurement](../capabilities/analytics-bi/experimentation.md), [External user and tenant identity](../capabilities/security/external-identity.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Packaged analytics content](../capabilities/analytics-bi/packaged-analytics.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Semantic model interchange](../capabilities/analytics-bi/semantic-model-interchange.md), [Spreadsheet integration](../capabilities/analytics-bi/spreadsheet-integration.md)

# Related tracks

- [Data serving](track-serving.md): How well curated data reaches applications, people and operational tools at the latency, volume and reliability they need.
- [Metadata and catalogue](track-metadata-catalogue.md): How completely and accurately data assets are described, findable and connected through metadata, for people and for machines.
- [Master and reference data](track-master-data.md): How consistently core business entities and shared code lists are identified, matched and maintained across systems.

Levels follow the shared [maturity scale](maturity-scale.md).
