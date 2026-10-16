---
type: Use Case
id: usecase-regulatory-reporting
title: Regulatory reporting
description: Produce accurate, auditable and reproducible submissions to regulators.
aliases: [regulatory returns, RDARR, prudential reporting]
requires:
- {capability: critical-data-elements, level: 3, why: The data items behind each return must be identified so the strictest controls apply to them.}
- {capability: cross-system-lineage, level: 3, why: 'Regulators expect each figure to be traced from source system to submission, not only inside the warehouse.'}
- {capability: column-lineage, level: 3, why: Reviewers need to see which source fields and rules produced each reported value.}
- capability: data-reconciliation
  level: 4
  why: Totals must be proven against source and ledger automatically on every run, with breaks tracked against tolerance.
- {capability: data-quality-rules, level: 3, why: Documented validity and completeness checks are part of the control framework regulators review.}
- {capability: temporal-data, level: 3, why: 'Returns must be reproduced as at the reporting date and as known at submission, including later restatements.'}
- {capability: data-retention, level: 3, why: 'Submission data and supporting records must be kept for the period the regulator sets, often five to ten years.'}
- capability: reference-data-management
  level: 3
  why: Regulatory code lists and mappings, such as counterparty and product classifications, must be versioned and approved.
- {capability: workflow-orchestration, level: 3, why: 'Reporting runs follow a fixed calendar with dependencies, sign-off points and reruns.'}
- {capability: environment-promotion, level: 3, why: Changes to reporting logic must be tested and approved before they reach production.}
- {capability: audit-logging, level: 3, why: 'Who changed data, rules or adjustments, and when, must be provable.'}
- {capability: data-ownership, level: 3, why: Each critical data element and each return needs an accountable owner who signs off.}
- {capability: data-issue-management, level: 3, why: 'Control breaks and quality issues must be logged, assigned and resolved with evidence.'}
- {capability: compliance-evidence, level: 3, why: 'Auditors and supervisors ask for evidence that controls ran, not only that they exist.'}
- {capability: data-testing, level: 3, why: Regression tests must show that a logic change does not alter reported values unexpectedly before a submission run.}
- capability: manual-adjustments
  level: 3
  why: Post-run adjustments to returns are a control that supervisors and auditors sample, so each needs approval, evidence and an as-reported version.
- {capability: regulatory-submission, level: 3, why: 'Returns must be mapped to the regulator''s templates, validated against its rules and their filing tracked.'}
benefits_from:
- {capability: data-quality-scorecards, why: Shows quality trends for critical data elements to the risk committee.}
- {capability: master-data-management, why: A single counterparty or customer record stops exposures being split or counted twice.}
- {capability: hierarchy-management, why: Legal entity and group structures drive consolidation.}
- {capability: time-travel, why: Makes short-term investigation of recent runs quick.}
- {capability: resilience-testing, why: Proves reports can still be produced during outages and stress events.}
- {capability: data-certification, why: Marks the authoritative sources that returns are allowed to draw on.}
- {capability: backfill-replay, why: Restatements rerun past reporting periods with corrected logic or source data.}
- {capability: data-export, why: Bulk extracts for regulators that accept plain files.}
personas:
- persona-risk-compliance
- persona-data-steward
- persona-data-engineer
- persona-data-analyst
- persona-cdo
- persona-data-architect
patterns: [data-vault, data-warehouse, write-audit-publish, slowly-changing-dimensions, shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Banks, insurers, utilities, healthcare providers and listed companies submit fixed-format returns to regulators on capital, liquidity, risk exposures, transactions and other measures. Each figure has to be correct, complete, delivered by a deadline and explainable years later. Data comes from many source systems, is integrated with full history, checked against controls, adjusted where needed through an approved and recorded process, and turned into the regulator's templates and file formats.

Good looks like submissions that go out on time with no late corrections, every reported figure traceable back to source records through each transformation, any past submission reproducible as it was sent, and evidence for auditors that is produced by the platform rather than assembled by hand. In banking, BCBS 239 sets out these expectations for risk data in detail.

# Non-functional requirements

- Submissions meet fixed regulatory deadlines, often a set number of days after period end, with resubmission possible on request.
- Every reported figure links to source records, transformation version and any manual adjustment.
- Records are retained for the regulatory period and can be retrieved for examination.
- Ad hoc requests from supervisors, especially in a stress event, can be answered within days or hours.

# Risks

- Spreadsheet steps outside the platform's controls make figures impossible to trace or reproduce.
- Lineage stops at the warehouse boundary, so the link to source systems cannot be shown.
- Logic changes are made without regression tests and alter previously reported figures.
- Regulatory definitions are misread when translated into data rules, and no owner checks them.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Critical data elements](../capabilities/governance/critical-data-elements.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | The data items behind each return must be identified so the strictest controls apply to them. |
| [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Regulators expect each figure to be traced from source system to submission, not only inside the warehouse. |
| [Column-level lineage](../capabilities/metadata/column-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | Reviewers need to see which source fields and rules produced each reported value. |
| [Data reconciliation](../capabilities/data-quality/data-reconciliation.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 4 (Measured) | Totals must be proven against source and ledger automatically on every run, with breaks tracked against tolerance. |
| [Data quality rules](../capabilities/data-quality/data-quality-rules.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Documented validity and completeness checks are part of the control framework regulators review. |
| [Bitemporal data](../capabilities/specialised-data/temporal-data.md) | [Specialised data types](../capabilities/specialised-data/specialised-data.md) | 3 (Defined) | Returns must be reproduced as at the reporting date and as known at submission, including later restatements. |
| [Retention and disposal](../capabilities/governance/data-retention.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Submission data and supporting records must be kept for the period the regulator sets, often five to ten years. |
| [Reference data management](../capabilities/master-data/reference-data-management.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 3 (Defined) | Regulatory code lists and mappings, such as counterparty and product classifications, must be versioned and approved. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 3 (Defined) | Reporting runs follow a fixed calendar with dependencies, sign-off points and reruns. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Changes to reporting logic must be tested and approved before they reach production. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Who changed data, rules or adjustments, and when, must be provable. |
| [Ownership and stewardship](../capabilities/governance/data-ownership.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Each critical data element and each return needs an accountable owner who signs off. |
| [Data issue management](../capabilities/data-quality/data-issue-management.md) | [Data quality and observability](../capabilities/data-quality/data-quality.md) | 3 (Defined) | Control breaks and quality issues must be logged, assigned and resolved with evidence. |
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Auditors and supervisors ask for evidence that controls ran, not only that they exist. |
| [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Regression tests must show that a logic change does not alter reported values unexpectedly before a submission run. |
| [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md) | [Analytics and BI](../capabilities/analytics-bi/analytics-bi.md) | 3 (Defined) | Post-run adjustments to returns are a control that supervisors and auditors sample, so each needs approval, evidence and an as-reported version. |
| [Regulatory submission](../capabilities/serving/regulatory-submission.md) | [Serving and activation](../capabilities/serving/serving.md) | 3 (Defined) | Returns must be mapped to the regulator's templates, validated against its rules and their filing tracked. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md) | Shows quality trends for critical data elements to the risk committee. |
| [Master data management](../capabilities/master-data/master-data-management.md) | A single counterparty or customer record stops exposures being split or counted twice. |
| [Hierarchy management](../capabilities/master-data/hierarchy-management.md) | Legal entity and group structures drive consolidation. |
| [Time travel](../capabilities/storage/time-travel.md) | Makes short-term investigation of recent runs quick. |
| [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md) | Proves reports can still be produced during outages and stress events. |
| [Data certification](../capabilities/metadata/data-certification.md) | Marks the authoritative sources that returns are allowed to draw on. |
| [Backfill and reprocessing](../capabilities/orchestration/backfill-replay.md) | Restatements rerun past reporting periods with corrected logic or source data. |
| [Data export](../capabilities/serving/data-export.md) | Bulk extracts for regulators that accept plain files. |

# Personas

- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data analyst](../personas/persona-data-analyst.md): Answers business questions through analysis, dashboards and reports.
- [Chief data officer](../personas/persona-cdo.md): Accountable for the organisation's data strategy, value, risk and governance.
- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.

# Patterns

- [Data Vault](../patterns/data-vault.md)
- [Data warehouse](../patterns/data-warehouse.md)
- [Write-audit-publish](../patterns/write-audit-publish.md)
- [Slowly changing dimensions](../patterns/slowly-changing-dimensions.md)
- [Shift-left data quality and governance](../patterns/shift-left.md)

# Frameworks that apply

- [BCBS 239](../frameworks/framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [DCAM v3](../frameworks/framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 8 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 11 of 17 (+1 in preview) | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 9 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 17 (+1 in preview) | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Data issue management](../capabilities/data-quality/data-issue-management.md) (preview only) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 4 of 17 (+1 in preview) | [Critical data elements](../capabilities/governance/critical-data-elements.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md) (preview only) |
| [Informatica](../platforms/platform-informatica.md) | 9 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 4 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Oracle](../platforms/platform-oracle.md) | 3 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [SAP](../platforms/platform-sap.md) | 4 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Audit logging](../capabilities/security/audit-logging.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Teradata](../platforms/platform-teradata.md) | 2 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [IBM](../platforms/platform-ibm.md) | 7 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data pipeline testing](../capabilities/development-lifecycle/data-testing.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Palantir](../platforms/platform-palantir.md) | 4 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 8 of 17 | [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Reference data management](../capabilities/master-data/reference-data-management.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md) |
| [Independent vendors](../platforms/platform-independent.md) | 15 of 17 | [Data reconciliation](../capabilities/data-quality/data-reconciliation.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md) |
