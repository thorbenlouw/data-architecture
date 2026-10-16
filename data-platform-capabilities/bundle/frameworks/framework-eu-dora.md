---
type: Framework
id: framework-eu-dora
title: DORA (Digital Operational Resilience Act)
description: Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.
aliases: [DORA, Digital Operational Resilience Act, Regulation (EU) 2022/2554]
kind: regulation
publisher: European Union
resource: https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en
related: [framework-bcbs-239, framework-edm-cdmc, framework-gdpr]
applies_to:
- usecase-security-log-analytics
- usecase-platform-modernisation
- persona-risk-compliance
- persona-platform-engineer
- persona-security-officer
mappings:
- ref: Chapter II – ICT risk management (Articles 5 to 16)
  summary: Financial entities keep a documented ICT risk management framework, owned by the management body, reviewed at least yearly and after major incidents, audited, and improved from lessons learned.
  capabilities: [compliance-evidence, data-security-posture, configuration-guardrails, platform-incident-management]
- ref: Article 8 – Identification
  summary: Identify, classify and document information assets, ICT assets and the dependencies between them, including those that rely on third parties.
  capabilities: [data-catalogue, data-classification, cross-system-lineage, data-security-posture]
- ref: Article 9 – Protection and prevention
  summary: Protect data and systems with security policies, least-privilege access, strong authentication, encryption, network controls and controlled change.
  capabilities:
  - identity-authentication
  - access-control
  - privileged-access
  - encryption
  - network-security
  - configuration-guardrails
- ref: Article 10 – Detection
  summary: Detect anomalous activity, performance problems and incidents promptly, with several layers of control and defined alert thresholds.
  capabilities: [data-threat-detection, platform-observability, audit-logging, data-security-posture]
- ref: Articles 11 and 12 – Response and recovery; backup, restoration and recovery
  summary: Keep tested continuity and recovery plans, back data up to systems kept separate from the source, and restore within set recovery objectives.
  capabilities:
  - backup-restore
  - immutable-backups
  - cross-region-failover
  - resilience-testing
  - platform-incident-management
- ref: Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23)
  summary: Detect, classify and manage ICT incidents, work out which data and services they affected, and report major ones to the competent authority within set deadlines.
  capabilities:
  - platform-incident-management
  - data-breach-response
  - platform-observability
  - data-threat-detection
  - audit-logging
  - pipeline-monitoring
- ref: Chapter IV – Digital operational resilience testing (Articles 24 to 27)
  summary: Test ICT systems regularly, from vulnerability scans to failover and recovery tests, with threat-led penetration testing for the most significant firms.
  capabilities: [resilience-testing, cross-region-failover, backup-restore, data-security-posture, network-security]
- ref: Chapter V, Section I – ICT third-party risk management (Articles 28 to 30)
  summary: Manage risk from ICT providers, keep a register of contracts, control provider access and have exit strategies that let data and workloads move.
  capabilities:
  - compliance-evidence
  - data-export
  - platform-migration
  - open-table-formats
  - deployment-options
  - privileged-access
- ref: Chapter V, Section II – Oversight of critical ICT third-party providers (Articles 31 to 44)
  summary: EU supervisors oversee providers whose failure would affect many financial entities.
  capabilities: [compliance-evidence, deployment-options]
- ref: Chapter VI – Information-sharing arrangements (Article 45)
  summary: Financial entities may share cyber threat information and intelligence with each other in trusted communities, protecting sensitive and personal data.
  capabilities: [external-data-sharing, data-threat-detection, deidentification, data-classification]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

DORA has applied since 17 January 2025 to banks, insurers, investment firms and other EU financial entities, and brings critical ICT third-party providers, including major cloud providers, under EU oversight. It is not a data regulation, but data platforms in financial services fall squarely within its ICT risk scope. Its pillars are ICT risk management, incident management and reporting, resilience testing, third-party risk management with a register of information, oversight of critical providers, and information sharing. For platform architects it mainly drives backup, recovery, failover, testing, observability and exit planning.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Chapter II – ICT risk management (Articles 5 to 16) | Financial entities keep a documented ICT risk management framework, owned by the management body, reviewed at least yearly and after major incidents, audited, and improved from lessons learned. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md) |
| Article 8 – Identification | Identify, classify and document information assets, ICT assets and the dependencies between them, including those that rely on third parties. | [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data classification](../capabilities/governance/data-classification.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Data security posture management](../capabilities/security/data-security-posture.md) |
| Article 9 – Protection and prevention | Protect data and systems with security policies, least-privilege access, strong authentication, encryption, network controls and controlled change. | [Identity and authentication](../capabilities/security/identity-authentication.md), [Access control](../capabilities/security/access-control.md), [Privileged access management](../capabilities/security/privileged-access.md), [Encryption](../capabilities/security/encryption.md), [Network security](../capabilities/security/network-security.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) |
| Article 10 – Detection | Detect anomalous activity, performance problems and incidents promptly, with several layers of control and defined alert thresholds. | [Data threat detection](../capabilities/security/data-threat-detection.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Audit logging](../capabilities/security/audit-logging.md), [Data security posture management](../capabilities/security/data-security-posture.md) |
| Articles 11 and 12 – Response and recovery; backup, restoration and recovery | Keep tested continuity and recovery plans, back data up to systems kept separate from the source, and restore within set recovery objectives. | [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Immutable backups](../capabilities/platform-operations/immutable-backups.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Platform incident management](../capabilities/platform-operations/platform-incident-management.md) |
| Chapter III – ICT-related incident management, classification and reporting (Articles 17 to 23) | Detect, classify and manage ICT incidents, work out which data and services they affected, and report major ones to the competent authority within set deadlines. | [Platform incident management](../capabilities/platform-operations/platform-incident-management.md), [Data breach response](../capabilities/security/data-breach-response.md), [Platform observability](../capabilities/platform-operations/platform-observability.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Audit logging](../capabilities/security/audit-logging.md), [Pipeline monitoring and alerting](../capabilities/platform-operations/pipeline-monitoring.md) |
| Chapter IV – Digital operational resilience testing (Articles 24 to 27) | Test ICT systems regularly, from vulnerability scans to failover and recovery tests, with threat-led penetration testing for the most significant firms. | [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Cross-region replication and failover](../capabilities/platform-operations/cross-region-failover.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Network security](../capabilities/security/network-security.md) |
| Chapter V, Section I – ICT third-party risk management (Articles 28 to 30) | Manage risk from ICT providers, keep a register of contracts, control provider access and have exit strategies that let data and workloads move. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Data export](../capabilities/serving/data-export.md), [Platform migration](../capabilities/platform-operations/platform-migration.md), [Open table formats](../capabilities/storage/open-table-formats.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md), [Privileged access management](../capabilities/security/privileged-access.md) |
| Chapter V, Section II – Oversight of critical ICT third-party providers (Articles 31 to 44) | EU supervisors oversee providers whose failure would affect many financial entities. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Hybrid and multi-cloud deployment](../capabilities/platform-operations/deployment-options.md) |
| Chapter VI – Information-sharing arrangements (Article 45) | Financial entities may share cyber threat information and intelligence with each other in trusted communities, protecting sensitive and personal data. | [External data sharing](../capabilities/data-sharing/external-data-sharing.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [De-identification](../capabilities/governance/deidentification.md), [Data classification](../capabilities/governance/data-classification.md) |

# Related frameworks

- [BCBS 239](framework-bcbs-239.md): Fourteen principles for how banks aggregate risk data and produce risk reports, in normal times and under stress.
- [CDMC (Cloud Data Management Capabilities)](framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [GDPR](framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.

# Applies to

- [Security and log analytics](../use-cases/usecase-security-log-analytics.md) (use case): Collect and analyse large volumes of logs to detect threats and investigate incidents.
- [Legacy warehouse migration](../use-cases/usecase-platform-modernisation.md) (use case): Move from an on-premises warehouse or Hadoop estate to a cloud data platform.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data platform engineer](../personas/persona-platform-engineer.md) (persona): Builds and runs the shared data platform and its self-service tooling.
- [Security and privacy officer](../personas/persona-security-officer.md) (persona): Protects data and makes sure it is used lawfully.
