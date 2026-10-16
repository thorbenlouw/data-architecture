---
type: Framework
id: framework-bcbs-239
title: BCBS 239
description: Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
aliases:
- RDARR
- PERDARR
- risk data aggregation and risk reporting
- Principles for effective risk data aggregation and risk reporting
- BCBS239
kind: principles
publisher: Basel Committee on Banking Supervision (Bank for International Settlements)
resource: https://www.bis.org/publ/bcbs239.htm
related: [framework-edm-dcam, framework-edm-cdmc, framework-eu-dora]
applies_to:
- usecase-regulatory-reporting
- usecase-enterprise-reporting
- persona-risk-compliance
- persona-cdo
- persona-data-steward
- persona-data-architect
mappings:
- ref: Principle 1 – Governance
  summary: The board and senior management approve and oversee the risk data framework, know its limitations and have it validated independently.
  capabilities:
  - data-ownership
  - data-policy-management
  - critical-data-elements
  - governance-metrics
  - compliance-evidence
- ref: Principle 2 – Data architecture and IT infrastructure
  summary: Design architecture to support aggregation in normal times and under stress, with group-wide taxonomies, single identifiers for entities such as legal entities and counterparties, clear ownership and a place in business continuity planning.
  capabilities:
  - business-glossary
  - reference-data-management
  - master-data-management
  - entity-resolution
  - hierarchy-management
  - data-ownership
  - data-modelling
  - business-continuity
- ref: Principle 3 – Accuracy and integrity
  summary: Produce accurate data with mostly automated aggregation, reconciled to sources, from a single authoritative source per risk type and a shared data dictionary, with manual steps documented and controlled.
  capabilities:
  - data-reconciliation
  - data-quality-rules
  - critical-data-elements
  - column-lineage
  - data-certification
  - business-glossary
  - manual-adjustments
- ref: Principle 4 – Completeness
  summary: Capture all material risk data across the group and be able to break it down by business line, legal entity, asset type, industry and region.
  capabilities:
  - data-reconciliation
  - data-quality-rules
  - data-quality-scorecards
  - hierarchy-management
  - semantic-layer
  - critical-data-elements
- ref: Principle 5 – Timeliness
  summary: Produce up-to-date aggregated data quickly enough for normal reporting and faster under stress.
  capabilities: [freshness-monitoring, data-slas, incremental-processing, elastic-scaling, workload-management]
- ref: Principle 6 – Adaptability
  summary: Meet ad hoc, stress-scenario and supervisory requests quickly by generating new subsets and views of the data, and absorb changes in the business and in regulation.
  capabilities: [ad-hoc-analysis, semantic-layer, analytical-sandboxes, query-acceleration, elastic-scaling]
- ref: Principle 7 – Accuracy (reporting)
  summary: Reconcile and validate reports, keep an inventory of validation rules, explain approximations and adjustments, and report data errors as exceptions.
  capabilities:
  - data-reconciliation
  - data-quality-rules
  - manual-adjustments
  - regulatory-submission
  - data-issue-management
  - metric-definitions
- ref: Principle 8 – Comprehensiveness
  summary: Cover all material risk areas, including limits, concentrations and forward-looking stress results.
  capabilities: [metric-definitions, semantic-layer, dashboards-reports, paginated-reports]
- ref: Principle 9 – Clarity and usefulness
  summary: Make reports clear and tailored to their audience, backed by an inventory and classification of risk data items.
  capabilities:
  - dashboards-reports
  - critical-data-elements
  - business-glossary
  - data-catalogue
  - data-trust-indicators
- ref: Principle 10 – Frequency
  summary: Set reporting frequency by need and by how fast risks change, increase it under stress and test the ability to deliver on time.
  capabilities: [workflow-orchestration, data-slas, pipeline-monitoring, resilience-testing, paginated-reports]
- ref: Principle 11 – Distribution
  summary: Deliver reports quickly to the right recipients while keeping them confidential.
  capabilities: [data-alerting, data-consumer-portal, role-based-access, row-level-security]
- ref: Principle 12 – Review
  summary: Supervisors review compliance regularly, including tests with short deadlines and in stress conditions, which requires figures to be traced and reproduced as they stood at a past date.
  capabilities: [compliance-evidence, cross-system-lineage, temporal-data, audit-logging]
- ref: Principle 13 – Remedial actions and supervisory measures
  summary: Supervisors require timely remediation with timetables and can impose measures such as capital add-ons.
  capabilities: [compliance-evidence, data-issue-management, governance-metrics]
- ref: Principle 14 – Home/host cooperation
  summary: Supervisors in different jurisdictions cooperate on reviews and share concerns about cross-border data obstacles.
  capabilities: [compliance-evidence, data-residency]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The Basel Committee published its Principles for effective risk data aggregation and risk reporting in January 2013, first for global systemically important banks and later applied by many supervisors to domestic systemically important banks. Supervisors enforce them, so for banks they behave like regulation, and they drive investment in data dictionaries, lineage, reconciliation, data quality and fast, flexible reporting platforms. The fourteen principles fall into four groups: overarching governance and infrastructure, risk data aggregation capabilities, risk reporting practices, and supervisory review. The Committee's November 2023 progress report found that most of the 31 banks assessed still had substantial work to do to comply fully.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Principle 1 – Governance | The board and senior management approve and oversee the risk data framework, know its limitations and have it validated independently. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Principle 2 – Data architecture and IT infrastructure | Design architecture to support aggregation in normal times and under stress, with group-wide taxonomies, single identifiers for entities such as legal entities and counterparties, clear ownership and a place in business continuity planning. | [Business glossary](../capabilities/metadata/business-glossary.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Master data management](../capabilities/master-data/master-data-management.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Backup and disaster recovery](../capabilities/platform-operations/business-continuity.md) |
| Principle 3 – Accuracy and integrity | Produce accurate data with mostly automated aggregation, reconciled to sources, from a single authoritative source per risk type and a shared data dictionary, with manual steps documented and controlled. | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data certification](../capabilities/metadata/data-certification.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) |
| Principle 4 – Completeness | Capture all material risk data across the group and be able to break it down by business line, legal entity, asset type, industry and region. | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Hierarchy management](../capabilities/master-data/hierarchy-management.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Critical data elements](../capabilities/governance/critical-data-elements.md) |
| Principle 5 – Timeliness | Produce up-to-date aggregated data quickly enough for normal reporting and faster under stress. | [Freshness monitoring](../capabilities/data-quality/freshness-monitoring.md), [Data service levels](../capabilities/data-products/data-slas.md), [Incremental processing](../capabilities/processing/incremental-processing.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md), [Workload management](../capabilities/compute/workload-management.md) |
| Principle 6 – Adaptability | Meet ad hoc, stress-scenario and supervisory requests quickly by generating new subsets and views of the data, and absorb changes in the business and in regulation. | [Ad hoc analysis](../capabilities/analytics-bi/ad-hoc-analysis.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Query acceleration](../capabilities/compute/query-acceleration.md), [Elastic scaling](../capabilities/compute/elastic-scaling.md) |
| Principle 7 – Accuracy (reporting) | Reconcile and validate reports, keep an inventory of validation rules, explain approximations and adjustments, and report data errors as exceptions. | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md) |
| Principle 8 – Comprehensiveness | Cover all material risk areas, including limits, concentrations and forward-looking stress results. | [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) |
| Principle 9 – Clarity and usefulness | Make reports clear and tailored to their audience, backed by an inventory and classification of risk data items. | [Dashboards and interactive reports](../capabilities/analytics-bi/dashboards-reports.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Business glossary](../capabilities/metadata/business-glossary.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| Principle 10 – Frequency | Set reporting frequency by need and by how fast risks change, increase it under stress and test the ability to deliver on time. | [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data service levels](../capabilities/data-products/data-slas.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Paginated reports](../capabilities/analytics-bi/paginated-reports.md) |
| Principle 11 – Distribution | Deliver reports quickly to the right recipients while keeping them confidential. | [Alerts and subscriptions](../capabilities/analytics-bi/data-alerting.md), [Data consumer portal](../capabilities/analytics-bi/data-consumer-portal.md), [Role-based access control](../capabilities/security/role-based-access.md), [Row-level security](../capabilities/security/row-level-security.md) |
| Principle 12 – Review | Supervisors review compliance regularly, including tests with short deadlines and in stress conditions, which requires figures to be traced and reproduced as they stood at a past date. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Audit logging](../capabilities/security/audit-logging.md) |
| Principle 13 – Remedial actions and supervisory measures | Supervisors require timely remediation with timetables and can impose measures such as capital add-ons. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) |
| Principle 14 – Home/host cooperation | Supervisors in different jurisdictions cooperate on reviews and share concerns about cross-border data obstacles. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md) |

# Related frameworks

- [DCAM v3](framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [CDMC (Cloud Data Management Capabilities)](framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DORA (Digital Operational Resilience Act)](framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.

# Applies to

- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md) (use case): Produce accurate, auditable and reproducible submissions to regulators.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) (use case): Produce trusted, consistent KPIs and management reports across the organisation.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
- [Data steward](../personas/persona-data-steward.md) (persona): Looks after the definition, quality and proper use of data in a business domain.
- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
