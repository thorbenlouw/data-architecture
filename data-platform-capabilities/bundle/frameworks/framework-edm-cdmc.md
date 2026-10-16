---
type: Framework
id: framework-edm-cdmc
title: CDMC (Cloud Data Management Capabilities)
description: A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
aliases: [CDMC, Cloud Data Management Capabilities, CDMC key controls, CDMC framework]
kind: control-framework
publisher: EDM Association (formerly EDM Council)
resource: https://edmcouncil.org/frameworks/cdmc/
related: [framework-edm-dcam, framework-bcbs-239, framework-gdpr, framework-eu-dora]
applies_to:
- usecase-sensitive-data-protection
- usecase-platform-modernisation
- persona-risk-compliance
- persona-security-officer
- persona-cdo
- persona-data-architect
mappings:
- ref: 1 Data Control Compliance (Governance and accountability)
  summary: Monitor compliance with data controls for sensitive data through metrics, and raise alerts automatically when controls fail.
  capabilities:
  - compliance-evidence
  - governance-metrics
  - active-metadata
  - data-classification
  - data-security-posture
- ref: 2 Ownership Field (Governance and accountability)
  summary: Record an owner for every sensitive data asset in the catalogue, fill the field automatically where possible and track how much is covered.
  capabilities: [data-ownership, data-catalogue, governance-metrics]
- ref: 3 Authoritative Data Sources and Provisioning Points (Governance and accountability)
  summary: Identify the authoritative source and approved provisioning points for data, and steer consumers towards them.
  capabilities: [data-certification, data-catalogue, master-data-management, data-trust-indicators]
- ref: 4 Data Sovereignty and Cross-Border Movement (Governance and accountability)
  summary: Know where sensitive data is stored and processed, and control and record any movement across borders.
  capabilities: [data-residency, data-policy-management, cross-region-sharing, cross-system-lineage]
- ref: 5 Cataloguing (Cataloguing and classification)
  summary: Catalogue all data, including sensitive data, automatically at the point of creation or ingestion.
  capabilities: [data-catalogue, metadata-harvesting, table-catalogue]
- ref: 6 Classification (Cataloguing and classification)
  summary: Classify data by sensitivity automatically and keep the classification with the data as it moves.
  capabilities: [data-classification, active-metadata, column-lineage]
- ref: 7 Entitlements and Access for Sensitive Data (Accessibility and usage)
  summary: Manage entitlements to sensitive data through tracked approvals, and review who has access.
  capabilities:
  - access-requests
  - attribute-based-access
  - role-based-access
  - stewardship-workflows
  - data-security-posture
- ref: 8 Data Consumption Purpose (Accessibility and usage)
  summary: Record why each consumer uses sensitive data and check that use stays within the agreed purpose.
  capabilities: [consent-management, data-usage-rights, access-requests, data-contracts, records-of-processing]
- ref: 9 Appropriate Security Controls (Protection and privacy)
  summary: Apply security controls such as encryption, masking and key management in line with the data's sensitivity.
  capabilities: [encryption, customer-managed-keys, column-masking, deidentification, network-security]
- ref: 10 Data Privacy Impact Assessments (Protection and privacy)
  summary: Carry out privacy impact assessments for personal data, triggered automatically by its classification and use.
  capabilities: [privacy-impact-assessment, data-classification, active-metadata, compliance-evidence]
- ref: 11 Data Quality Measurement (Data lifecycle)
  summary: Measure and report the quality of sensitive data and make the results visible to consumers where they use the data.
  capabilities: [data-quality-rules, data-quality-scorecards, data-trust-indicators, data-observability]
- ref: 12 Data Retention, Archiving and Purging (Data lifecycle)
  summary: Retain, archive and purge data according to defined schedules, and prove that it happened.
  capabilities: [data-retention, storage-tiering, audit-logging]
- ref: 13 Data Lineage (Data and technical architecture)
  summary: Capture lineage for sensitive data from source to consumption, at least for authoritative sources and key reports.
  capabilities: [cross-system-lineage, column-lineage, table-lineage]
- ref: 14 Cost Metrics (Data and technical architecture)
  summary: Measure and allocate the cost of storing, processing and moving data so that cost can be managed.
  capabilities: [cost-attribution, system-telemetry, usage-metadata, data-product-metering]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

CDMC was written by an EDM Council working group of financial firms, cloud providers and vendors from 2020 and sets out the controls a regulated firm needs before it moves sensitive data to the cloud. Its core is fourteen key controls grouped into six components, each with objectives, questions, evidence and scoring criteria; it is the most direct bridge between governance requirements and concrete platform features such as catalogues, classification, entitlements, lineage and cost metrics. The current framework is CDMC v1, and cloud providers and tool vendors hold CDMC certifications against it. Many controls expect automation, for example that sensitive data is discovered, classified and reported on without manual effort.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| 1 Data Control Compliance (Governance and accountability) | Monitor compliance with data controls for sensitive data through metrics, and raise alerts automatically when controls fail. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Active metadata](../capabilities/metadata/active-metadata.md), [Data classification](../capabilities/governance/data-classification.md), [Data security posture management](../capabilities/security/data-security-posture.md) |
| 2 Ownership Field (Governance and accountability) | Record an owner for every sensitive data asset in the catalogue, fill the field automatically where possible and track how much is covered. | [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md) |
| 3 Authoritative Data Sources and Provisioning Points (Governance and accountability) | Identify the authoritative source and approved provisioning points for data, and steer consumers towards them. | [Data certification](../capabilities/metadata/data-certification.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Master data management](../capabilities/master-data/master-data-management.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md) |
| 4 Data Sovereignty and Cross-Border Movement (Governance and accountability) | Know where sensitive data is stored and processed, and control and record any movement across borders. | [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Policy management](../capabilities/governance/data-policy-management.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md) |
| 5 Cataloguing (Cataloguing and classification) | Catalogue all data, including sensitive data, automatically at the point of creation or ingestion. | [Data catalogue](../capabilities/metadata/data-catalogue.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Table catalogue](../capabilities/storage/table-catalogue.md) |
| 6 Classification (Cataloguing and classification) | Classify data by sensitivity automatically and keep the classification with the data as it moves. | [Data classification](../capabilities/governance/data-classification.md), [Active metadata](../capabilities/metadata/active-metadata.md), [Column-level lineage](../capabilities/metadata/column-lineage.md) |
| 7 Entitlements and Access for Sensitive Data (Accessibility and usage) | Manage entitlements to sensitive data through tracked approvals, and review who has access. | [Access requests and reviews](../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Role-based access control](../capabilities/security/role-based-access.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md), [Data security posture management](../capabilities/security/data-security-posture.md) |
| 8 Data Consumption Purpose (Accessibility and usage) | Record why each consumer uses sensitive data and check that use stays within the agreed purpose. | [Consent and purpose management](../capabilities/governance/consent-management.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Access requests and reviews](../capabilities/security/access-requests.md), [Data contracts](../capabilities/data-products/data-contracts.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| 9 Appropriate Security Controls (Protection and privacy) | Apply security controls such as encryption, masking and key management in line with the data's sensitivity. | [Encryption](../capabilities/security/encryption.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Network security](../capabilities/security/network-security.md) |
| 10 Data Privacy Impact Assessments (Protection and privacy) | Carry out privacy impact assessments for personal data, triggered automatically by its classification and use. | [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Data classification](../capabilities/governance/data-classification.md), [Active metadata](../capabilities/metadata/active-metadata.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| 11 Data Quality Measurement (Data lifecycle) | Measure and report the quality of sensitive data and make the results visible to consumers where they use the data. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data quality scorecards](../capabilities/data-quality/data-quality-scorecards.md), [Data trust indicators](../capabilities/metadata/data-trust-indicators.md), [Data observability](../capabilities/data-quality/data-observability.md) |
| 12 Data Retention, Archiving and Purging (Data lifecycle) | Retain, archive and purge data according to defined schedules, and prove that it happened. | [Retention and disposal](../capabilities/governance/data-retention.md), [Storage tiering and lifecycle](../capabilities/storage/storage-tiering.md), [Audit logging](../capabilities/security/audit-logging.md) |
| 13 Data Lineage (Data and technical architecture) | Capture lineage for sensitive data from source to consumption, at least for authoritative sources and key reports. | [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Column-level lineage](../capabilities/metadata/column-lineage.md), [Table-level lineage](../capabilities/metadata/table-lineage.md) |
| 14 Cost Metrics (Data and technical architecture) | Measure and allocate the cost of storing, processing and moving data so that cost can be managed. | [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Usage and system telemetry](../capabilities/platform-operations/system-telemetry.md), [Usage and popularity metadata](../capabilities/metadata/usage-metadata.md), [Data product usage metering](../capabilities/data-products/data-product-metering.md) |

# Related frameworks

- [DCAM v3](framework-edm-dcam.md): The Data Management Capability Assessment Model, an evidence-based framework for scoring how mature an organisation's data management programme is.
- [BCBS 239](framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [GDPR](framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
- [DORA (Digital Operational Resilience Act)](framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
- [DAMA-DMBOK 2](framework-dama-dmbok.md): The Data Management Body of Knowledge, a reference guide that splits data management into knowledge areas around a central governance function.

# Applies to

- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md) (use case): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) (use case): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Security and privacy officer](../personas/persona-security-officer.md) (persona): Protects data and makes sure it is used lawfully.
- [Chief data officer](../personas/persona-cdo.md) (persona): Accountable for the organisation's data strategy, value, risk and governance.
- [Data architect](../personas/persona-data-architect.md) (persona): Designs the data platform and how data flows, is modelled and is governed across the organisation.
