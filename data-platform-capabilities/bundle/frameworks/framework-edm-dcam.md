---
type: Framework
id: framework-edm-dcam
title: DCAM v3
description: The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
aliases: [DCAM, Data Management Capability Assessment Model, EDM Council DCAM, DCAM v3]
kind: maturity-model
publisher: EDM Association (formerly EDM Council)
resource: https://edmcouncil.org/frameworks/dcam/
related: [framework-bcbs-239, framework-edm-cdmc, framework-dama-dmbok]
applies_to:
- persona-cdo
- persona-data-steward
- persona-risk-compliance
- usecase-regulatory-reporting
- usecase-enterprise-reporting
mappings:
- ref: 1 Data Strategy, DMS & Business Case
  summary: Setting a data management strategy and a business case that ties data work to business goals; mostly organisational, with policy, scope and progress measures as the platform touch points.
  capabilities: [data-policy-management, governance-metrics, data-domains]
- ref: 2 Data Management Program & Funding
  summary: Establishing the data management programme, its roles and a sustainable funding model; funding models depend on knowing what data work costs.
  capabilities: [data-ownership, cost-attribution, cost-forecasting, governance-metrics]
- ref: 3 Architecture – Business, Data & Technology
  summary: Defining business, data and technology architecture together so that data is designed, located and moved consistently.
  capabilities: [data-modelling, data-lineage, data-domains, metadata-interoperability, deployment-options]
- ref: 4 Business Data Knowledge
  summary: Capturing the business meaning of data through a glossary, metadata management and data requirements, with approval of terms by stewards.
  capabilities: [business-glossary, data-catalogue, metadata-harvesting, semantic-layer, stewardship-workflows]
- ref: 5 Data Quality Management
  summary: Defining quality requirements for the data that matters most, measuring them and managing issues through to their root cause.
  capabilities:
  - data-quality-rules
  - critical-data-elements
  - data-profiling
  - data-quality-scorecards
  - data-observability
  - data-issue-management
  - impact-analysis
- ref: 6 Govern Data & DMP
  summary: Running the governance structures, policies and standards that oversee data and the data management programme.
  capabilities:
  - data-ownership
  - stewardship-workflows
  - data-policy-management
  - data-certification
  - governance-metrics
  - data-domains
- ref: 7 Data Management Operations, Risk & Control
  summary: Operating data management day to day with a control environment, risk management and evidence that controls work.
  capabilities: [compliance-evidence, data-issue-management, data-lineage, audit-logging, pipeline-monitoring]
- ref: 8 Analytics Management
  summary: Governing analytics and models, including their platforms, lifecycle, data access and ethical use.
  capabilities:
  - model-governance
  - ai-governance
  - model-registry
  - analytical-sandboxes
  - metric-definitions
  - access-requests
  - fairness-assessment
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

DCAM is the EDM Association's capability and assessment framework for data management and analytics, widely used by banks and other regulated firms to benchmark their data programmes and to show supervisors progress against expectations such as BCBS 239. Version 3, released in July 2025, has eight components, 34 capabilities and 101 sub-capabilities, each scored against auditable evidence; it merged architecture into one component and added Business Data Knowledge (glossary and metadata). The full framework and its scoring matrix are available to member firms, and secondary sources describe the scale as running from "Not Initiated" to "Enhanced". The publisher renamed itself from EDM Council to EDM Association in July 2025 when it agreed to acquire the Object Management Group.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| 1 Data Strategy, DMS & Business Case | Setting a data management strategy and a business case that ties data work to business goals; mostly organisational, with policy, scope and progress measures as the platform touch points. | [Policy management](../capabilities/governance/data-policy-management.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Data domains](../capabilities/governance/data-domains.md) |
| 2 Data Management Program & Funding | Establishing the data management programme, its roles and a sustainable funding model; funding models depend on knowing what data work costs. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Spend forecasting and anomaly detection](../capabilities/platform-operations/cost-forecasting.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) |
| 3 Architecture – Business, Data & Technology | Defining business, data and technology architecture together so that data is designed, located and moved consistently. | [Data modelling and design](../capabilities/development-lifecycle/data-modelling.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Data domains](../capabilities/governance/data-domains.md), [Metadata interoperability](../capabilities/metadata/metadata-interoperability.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| 4 Business Data Knowledge | Capturing the business meaning of data through a glossary, metadata management and data requirements, with approval of terms by stewards. | [Business glossary](../capabilities/metadata/business-glossary.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Semantic layer](../capabilities/analytics-bi/semantic-layer.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md) |
| 5 Data Quality Management | Defining quality requirements for the data that matters most, measuring them and managing issues through to their root cause. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data profiling](../capabilities/data-quality/data-profiling.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data observability](../capabilities/data-quality/data-observability.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Impact analysis](../capabilities/metadata/impact-analysis.md) |
| 6 Govern Data & DMP | Running the governance structures, policies and standards that oversee data and the data management programme. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Policy management](../capabilities/governance/data-policy-management.md), [Data certification](../capabilities/metadata/data-certification.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Data domains](../capabilities/governance/data-domains.md) |
| 7 Data Management Operations, Risk & Control | Operating data management day to day with a control environment, risk management and evidence that controls work. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data issue management](../capabilities/data-quality/data-issue-management.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Audit logging](../capabilities/security/audit-logging.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| 8 Analytics Management | Governing analytics and models, including their platforms, lifecycle, data access and ethical use. | [Model governance](../capabilities/mlops/model-governance.md), [AI governance](../capabilities/governance/ai-governance.md), [Model registry](../capabilities/machine-learning/model-registry.md), [Analytical sandboxes](../capabilities/analytics-bi/analytical-sandboxes.md), [Governed metric definitions](../capabilities/analytics-bi/metric-definitions.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Bias and fairness assessment](../capabilities/machine-learning/fairness-assessment.md) |

# Related frameworks

- [BCBS 239](framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [CDMC (Cloud Data Management Capabilities)](framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [DAMA-DMBOK 2](framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.
- [ISO 8000 (data quality)](framework-iso-8000.md): A series of international standards on data quality, covering concepts, quality management processes, profiling, rules, master data exchange and sensor data.

# Applies to

- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
- [Data steward](../personas/persona-data-steward.md) (persona): Looks after the definition, quality and proper use of data in a business domain.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Regulatory reporting](../use-cases/usecase-regulatory-reporting.md) (use case): Produce accurate, auditable and reproducible submissions to regulators.
- [Enterprise management reporting](../use-cases/usecase-enterprise-reporting.md) (use case): Produce trusted, consistent KPIs and management reports across the organisation.
