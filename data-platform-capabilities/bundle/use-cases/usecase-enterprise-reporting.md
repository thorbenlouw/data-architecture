---
type: Use Case
id: usecase-enterprise-reporting
title: Enterprise management reporting
description: Produce trusted, consistent KPIs and management reports across the organisation.
requires:
- {capability: metric-definitions, level: 3, why: 'Each KPI needs one certified calculation and an owner, because packs go to the board.'}
- {capability: semantic-layer, level: 3, why: 'Dashboards, packs and analyst queries must all calculate KPIs from the same definitions.'}
- {capability: data-modelling, level: 3, why: Conformed dimensions let KPIs from different source systems be compared and combined.}
- {capability: hierarchy-management, level: 3, why: 'Figures roll up through legal entity, cost centre and product hierarchies that change during the year.'}
- {capability: reference-data-management, level: 2, why: 'Shared code lists such as currencies, regions and account mappings must be the same in every report.'}
- {capability: batch-ingestion, level: 3, why: 'Ledger, ERP, CRM and HR data arrives in scheduled batches that must load reliably.'}
- {capability: workflow-orchestration, level: 3, why: Close-related loads and refreshes run in a fixed order with dependencies and retries.}
- {capability: data-reconciliation, level: 3, why: Totals have to agree with the general ledger before any pack is released.}
- {capability: data-quality-rules, level: 3, why: Completeness and validity checks stop a pack being published from partial or broken data.}
- {capability: freshness-monitoring, level: 2, why: Report owners need to know before the morning meeting if a load is late.}
- {capability: dashboards-reports, level: 3, why: Managers work from interactive dashboards for their own areas.}
- {capability: paginated-reports, level: 2, why: 'Board and management packs need a fixed, printable layout.'}
- {capability: data-certification, level: 3, why: Official KPI datasets must be clearly marked so nobody reports from a lookalike.}
- {capability: row-level-security, level: 2, why: Divisional managers see their own figures before group results are released.}
- capability: transformation-as-code
  level: 3
  why: Conformed dimensions and KPI logic are built as reviewed, versioned models, so every change to a board KPI can be traced and reviewed.
- {capability: data-testing, level: 2, why: Logic and regression tests catch a changed KPI before a pack goes to the board.}
- capability: manual-adjustments
  level: 2
  why: Late accruals and reclassifications after close are entered with approval and a reason in the platform, or packs stop reconciling with the ledger.
benefits_from:
- {capability: time-travel, why: Recreate figures as they stood when a pack was published.}
- {capability: temporal-data, why: Report both as-reported and restated history when hierarchies or late adjustments change past periods.}
- {capability: column-lineage, why: Shows how each KPI was derived when someone challenges it.}
- {capability: application-data-products, why: Vendor-published ERP datasets reduce the effort of extracting and interpreting ledger data.}
- {capability: enterprise-planning, why: Compare actuals with budget and forecast on the same governed data.}
- {capability: data-alerting, why: Deliver packs to subscribers on schedule and flag KPIs that cross thresholds.}
- {capability: data-quality-scorecards, why: Track quality of the reporting data month by month.}
- {capability: master-data-management, why: A single customer and product record avoids double counting across business units.}
- {capability: environment-promotion, why: KPI logic changes are tested and approved before they reach the production reporting run.}
personas:
- persona-cdo
- persona-business-user
- persona-data-analyst
- persona-analytics-engineer
- persona-data-engineer
- persona-data-steward
patterns:
- data-warehouse
- dimensional-modelling
- slowly-changing-dimensions
- data-marts
- medallion-architecture
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Executives, boards and divisional managers need one set of KPIs, such as revenue, margin, headcount and customer numbers, calculated the same way everywhere and tied back to the finance ledger. The data comes mostly from ERP, CRM and HR systems in daily or monthly batches, is conformed to shared dimensions such as product, customer, legal entity and cost centre, and is published as dashboards and formatted management packs on a fixed calendar that follows the financial close.

Good looks like a monthly pack that is ready on time and reconciles to the ledger, every KPI having an owner and a documented definition, and any figure from an earlier period reproducible as it was reported. Arguments in meetings are about what the numbers mean, not whether they are right.

# Non-functional requirements

- Monthly KPIs are available within an agreed number of working days after the ledger closes, often two to five.
- Daily dashboards are refreshed before the start of the business day.
- Totals reconcile to the ledger within an agreed tolerance before release.
- Any past period can be reproduced as originally reported, and restatements are recorded with a reason.

# Risks

- Spreadsheet adjustments made after the platform step break reconciliation and audit trails.
- Hierarchy changes during the year are applied inconsistently, so historical comparisons are wrong.
- KPI owners are not named and definitions drift between divisions.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Each KPI needs one certified calculation and an owner, because packs go to the board. |
| [Semantic layer](../capabilities/analytics-bi/semantic-layer.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Dashboards, packs and analyst queries must all calculate KPIs from the same definitions. |
| [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Conformed dimensions let KPIs from different source systems be compared and combined. |
| [Hierarchy management](../capabilities/master-data/hierarchy-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | Figures roll up through legal entity, cost centre and product hierarchies that change during the year. |
| [Reference data management](../capabilities/master-data/reference-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 2 (Managed) | Shared code lists such as currencies, regions and account mappings must be the same in every report. |
| [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md) | [Ingestion and integration](../capabilities/ingestion-integration/ingestion-integration.md) | 3 (Defined) | Ledger, ERP, CRM and HR data arrives in scheduled batches that must load reliably. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 3 (Defined) | Close-related loads and refreshes run in a fixed order with dependencies and retries. |
| [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Totals have to agree with the general ledger before any pack is released. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Completeness and validity checks stop a pack being published from partial or broken data. |
| [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 2 (Managed) | Report owners need to know before the morning meeting if a load is late. |
| [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Managers work from interactive dashboards for their own areas. |
| [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Board and management packs need a fixed, printable layout. |
| [Data certification](../capabilities/metadata/data-certification.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Official KPI datasets must be clearly marked so nobody reports from a lookalike. |
| [Row-level security](../capabilities/security/row-level-security.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Divisional managers see their own figures before group results are released. |
| [Transformation as code](../capabilities/processing/transformation-as-code.md) | [Processing and transformation](../capabilities/processing/processing.md) | 3 (Defined) | Conformed dimensions and KPI logic are built as reviewed, versioned models, so every change to a board KPI can be traced and reviewed. |
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 2 (Managed) | Logic and regression tests catch a changed KPI before a pack goes to the board. |
| [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 2 (Managed) | Late accruals and reclassifications after close are entered with approval and a reason in the platform, or packs stop reconciling with the ledger. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Time travel](../capabilities/storage/time-travel.md) | Recreate figures as they stood when a pack was published. |
| [Bitemporal data](../capabilities/specialised-data/temporal-data.md) | Report both as-reported and restated history when hierarchies or late adjustments change past periods. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | Shows how each KPI was derived when someone challenges it. |
| [Vendor-supplied application data products](../capabilities/data-products/application-data-products.md) | Vendor-published ERP datasets reduce the effort of extracting and interpreting ledger data. |
| [Planning and forecasting](../capabilities/analytics-bi/enterprise-planning.md) | Compare actuals with budget and forecast on the same governed data. |
| [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md) | Deliver packs to subscribers on schedule and flag KPIs that cross thresholds. |
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | Track quality of the reporting data month by month. |
| [Master data management](../capabilities/master-data/master-data-management.md) | A single customer and product record avoids double counting across business units. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | KPI logic changes are tested and approved before they reach the production reporting run. |

# Personas

- [Chief data officer](../personas/persona-cdo.md): Accountable for the organisation's data strategy, value, risk and governance.
- [Business user](../personas/persona-business-user.md): Uses data, reports and AI assistants to make decisions, without deep technical skills.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.

# Patterns

- [Data warehouse](../patterns/data-warehouse.md)
- [Dimensional modelling](../patterns/dimensional-modelling.md)
- [Slowly changing dimensions](../patterns/slowly-changing-dimensions.md)
- [Data marts](../patterns/data-marts.md)
- [Medallion architecture](../patterns/medallion-architecture.md)

# Frameworks that apply

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [DAMA-DMBOK 2](../frameworks/framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [DCAM v3](../frameworks/framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 8 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 10 of 17 (+2 in preview) | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) (preview only), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 17 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Data certification](../capabilities/metadata/data-certification.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 17 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Databricks](../platforms/platform-databricks.md) | 10 of 17 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 17 (+2 in preview) | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Transformation as code](../capabilities/processing/transformation-as-code.md) (preview only), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Informatica](../platforms/platform-informatica.md) | 9 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Oracle](../platforms/platform-oracle.md) | 6 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [SAP](../platforms/platform-sap.md) | 8 of 17 | [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Teradata](../platforms/platform-teradata.md) | 1 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Batch ingestion](../capabilities/ingestion-integration/batch-ingestion.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [IBM](../platforms/platform-ibm.md) | 3 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Row-level security](../capabilities/security/row-level-security.md), [Transformation as code](../capabilities/processing/transformation-as-code.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Palantir](../platforms/platform-palantir.md) | 8 of 17 | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 9 of 17 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md), [Data certification](../capabilities/metadata/data-certification.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| [Independent vendors](../platforms/platform-independent.md) | 15 of 17 | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) |
