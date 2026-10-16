---
type: Framework
id: framework-gdpr
title: GDPR
description: Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.
aliases: [General Data Protection Regulation, Regulation (EU) 2016/679, EU GDPR, UK GDPR, RGPD, DSGVO]
kind: regulation
publisher: European Union
resource: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
related: [framework-eu-ai-act, framework-edm-cdmc, framework-eu-data-act, framework-eu-dora]
applies_to:
- usecase-privacy-rights
- usecase-sensitive-data-protection
- usecase-marketing-activation
- usecase-customer-360
- persona-security-officer
- persona-risk-compliance
mappings:
- ref: Article 5(1)(a) – Lawfulness, fairness and transparency
  summary: Processing must have a legal basis and be fair and open to the people concerned.
  capabilities: [privacy-management, consent-management, records-of-processing, data-lineage]
- ref: Article 5(1)(b) – Purpose limitation
  summary: Data collected for one purpose must not be reused for incompatible purposes.
  capabilities: [consent-management, attribute-based-access, data-policy-management, records-of-processing]
- ref: Article 5(1)(c) – Data minimisation
  summary: Only the personal data needed for the purpose may be processed.
  capabilities: [column-masking, deidentification, data-classification, privacy-enhancing-technologies]
- ref: Article 5(1)(d) – Accuracy
  summary: Personal data must be accurate and corrected or erased without delay when wrong.
  capabilities: [data-quality-rules, data-cleansing, master-data-management]
- ref: Article 5(1)(e) – Storage limitation
  summary: Identifiable data must not be kept longer than the purpose requires.
  capabilities: [data-retention, deidentification, crypto-shredding]
- ref: Article 5(1)(f) – Integrity and confidentiality
  summary: Data must be protected against unauthorised access, loss and damage.
  capabilities:
  - access-control
  - encryption
  - identity-authentication
  - network-security
  - data-loss-prevention
  - data-threat-detection
  - audit-logging
  - backup-restore
- ref: Article 5(2) – Accountability
  summary: Controllers must be able to demonstrate that they comply.
  capabilities: [compliance-evidence, records-of-processing, audit-logging, data-lineage]
- ref: Articles 6 and 7 – Lawfulness of processing and conditions for consent
  summary: Each use needs a legal basis, and where that is consent it must be recorded and as easy to withdraw as to give.
  capabilities: [consent-management, records-of-processing]
- ref: Article 9 – Special categories of personal data
  summary: Sensitive data such as health, biometric or ethnic data may be processed only under specific conditions.
  capabilities: [data-classification, attribute-based-access, column-masking, deidentification]
- ref: Article 15 – Right of access
  summary: People can obtain a copy of their data and information about how it is used, by whom and for how long.
  capabilities: [data-subject-requests, data-catalogue, data-classification, records-of-processing]
- ref: Article 16 – Right to rectification
  summary: People can have inaccurate data about them corrected.
  capabilities: [data-subject-requests, row-level-updates, master-data-management]
- ref: Article 17 – Right to erasure
  summary: People can have their data erased in defined cases, which must reach all copies including history and backups.
  capabilities:
  - data-subject-requests
  - row-level-updates
  - crypto-shredding
  - table-maintenance
  - data-retention
  - data-lineage
- ref: Article 18 – Right to restriction of processing
  summary: People can have processing of their data paused while a dispute is resolved.
  capabilities: [data-subject-requests, row-level-security, attribute-based-access]
- ref: Article 19 – Notification to recipients
  summary: Controllers must pass rectifications, erasures and restrictions on to everyone the data was disclosed to.
  capabilities: [data-lineage, impact-analysis, records-of-processing, external-data-sharing]
- ref: Article 20 – Right to data portability
  summary: People can receive their data in a structured, machine-readable format and have it sent to another controller.
  capabilities: [data-subject-requests, data-export]
- ref: Article 21 – Right to object
  summary: People can object to processing, including for direct marketing, which must then stop.
  capabilities: [consent-management, data-subject-requests]
- ref: Article 22 – Automated individual decision-making
  summary: People have rights around decisions made solely by automated means, including human intervention and an explanation.
  capabilities: [human-oversight, model-explainability, decision-management, model-governance]
- ref: Article 25 – Data protection by design and by default
  summary: Build protections such as pseudonymisation into processing and limit data use by default.
  capabilities: [deidentification, column-masking, privacy-enhancing-technologies, data-classification]
- ref: Article 30 – Records of processing activities
  summary: Controllers and processors keep a record of what personal data they process, why, with whom it is shared and how long it is kept.
  capabilities: [records-of-processing, data-catalogue, data-lineage, data-classification]
- ref: Article 32 – Security of processing
  summary: Apply security suited to the risk, such as encryption, pseudonymisation, resilience, timely restoration and regular testing of the measures.
  capabilities: [encryption, deidentification, access-control, backup-restore, resilience-testing, audit-logging]
- ref: Articles 33 and 34 – Personal data breach notification
  summary: Report breaches to the regulator within 72 hours where required, and tell affected people when the risk is high.
  capabilities:
  - data-breach-response
  - data-threat-detection
  - audit-logging
  - data-classification
  - data-security-posture
  - data-loss-prevention
- ref: Article 35 – Data protection impact assessment
  summary: Assess high-risk processing, such as large-scale profiling, before it starts.
  capabilities: [privacy-impact-assessment, data-classification, records-of-processing, compliance-evidence]
- ref: Articles 44 to 49 – Transfers to third countries
  summary: Personal data may leave the EU only on the basis of adequacy, appropriate safeguards or specific derogations.
  capabilities: [data-residency, cross-region-sharing, customer-managed-keys, records-of-processing]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The General Data Protection Regulation has applied since May 2018 and, with the UK GDPR, is the main source of privacy requirements on data platforms in Europe. Its principles and rights translate into concrete platform needs: classification of personal data, purpose-bound access, retention and deletion that reaches every copy, subject access and erasure across the estate, records of processing, pseudonymisation, security and control of international transfers. The Commission's Digital Omnibus proposal of 19 November 2025 (COM(2025) 837) would amend the GDPR, but as of October 2026 it is still at committee stage in the European Parliament and is not law. Only the articles that most directly drive platform capabilities are mapped here.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Mapping to capabilities

| Area | Summary | Capabilities |
|---|---|---|
| Article 5(1)(a) – Lawfulness, fairness and transparency | Processing must have a legal basis and be fair and open to the people concerned. | [Privacy management](../capabilities/governance/privacy-management.md), [Consent and purpose management](../capabilities/governance/consent-management.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data lineage](../capabilities/metadata/data-lineage.md) |
| Article 5(1)(b) – Purpose limitation | Data collected for one purpose must not be reused for incompatible purposes. | [Consent and purpose management](../capabilities/governance/consent-management.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Policy management](../capabilities/governance/data-policy-management.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| Article 5(1)(c) – Data minimisation | Only the personal data needed for the purpose may be processed. | [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md), [Data classification](../capabilities/governance/data-classification.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md) |
| Article 5(1)(d) – Accuracy | Personal data must be accurate and corrected or erased without delay when wrong. | [Data quality rules](../capabilities/data-quality/data-quality-rules.md), [Data cleansing and standardisation](../capabilities/data-quality/data-cleansing.md), [Master data management](../capabilities/master-data/master-data-management.md) |
| Article 5(1)(e) – Storage limitation | Identifiable data must not be kept longer than the purpose requires. | [Retention and disposal](../capabilities/governance/data-retention.md), [De-identification](../capabilities/governance/deidentification.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md) |
| Article 5(1)(f) – Integrity and confidentiality | Data must be protected against unauthorised access, loss and damage. | [Access control](../capabilities/security/access-control.md), [Encryption](../capabilities/security/encryption.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Audit logging](../capabilities/security/audit-logging.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| Article 5(2) – Accountability | Controllers must be able to demonstrate that they comply. | [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Audit logging](../capabilities/security/audit-logging.md), [Data lineage](../capabilities/metadata/data-lineage.md) |
| Articles 6 and 7 – Lawfulness of processing and conditions for consent | Each use needs a legal basis, and where that is consent it must be recorded and as easy to withdraw as to give. | [Consent and purpose management](../capabilities/governance/consent-management.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| Article 9 – Special categories of personal data | Sensitive data such as health, biometric or ethnic data may be processed only under specific conditions. | [Data classification](../capabilities/governance/data-classification.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [De-identification](../capabilities/governance/deidentification.md) |
| Article 15 – Right of access | People can obtain a copy of their data and information about how it is used, by whom and for how long. | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data classification](../capabilities/governance/data-classification.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| Article 16 – Right to rectification | People can have inaccurate data about them corrected. | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Master data management](../capabilities/master-data/master-data-management.md) |
| Article 17 – Right to erasure | People can have their data erased in defined cases, which must reach all copies including history and backups. | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Data lineage](../capabilities/metadata/data-lineage.md) |
| Article 18 – Right to restriction of processing | People can have processing of their data paused while a dispute is resolved. | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Row-level security](../capabilities/security/row-level-security.md), [Attribute- and tag-based access control](../capabilities/security/attribute-based-access.md) |
| Article 19 – Notification to recipients | Controllers must pass rectifications, erasures and restrictions on to everyone the data was disclosed to. | [Data lineage](../capabilities/metadata/data-lineage.md), [Impact analysis](../capabilities/metadata/impact-analysis.md), [Records of processing](../capabilities/governance/records-of-processing.md), [External data sharing](../capabilities/data-sharing/external-data-sharing.md) |
| Article 20 – Right to data portability | People can receive their data in a structured, machine-readable format and have it sent to another controller. | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data export](../capabilities/serving/data-export.md) |
| Article 21 – Right to object | People can object to processing, including for direct marketing, which must then stop. | [Consent and purpose management](../capabilities/governance/consent-management.md), [Data subject requests](../capabilities/governance/data-subject-requests.md) |
| Article 22 – Automated individual decision-making | People have rights around decisions made solely by automated means, including human intervention and an explanation. | [Human oversight of AI](../capabilities/governance/human-oversight.md), [Model explainability](../capabilities/machine-learning/model-explainability.md), [Decision management](../capabilities/serving/decision-management.md), [Model governance](../capabilities/mlops/model-governance.md) |
| Article 25 – Data protection by design and by default | Build protections such as pseudonymisation into processing and limit data use by default. | [De-identification](../capabilities/governance/deidentification.md), [Column security and dynamic masking](../capabilities/security/column-masking.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Data classification](../capabilities/governance/data-classification.md) |
| Article 30 – Records of processing activities | Controllers and processors keep a record of what personal data they process, why, with whom it is shared and how long it is kept. | [Records of processing](../capabilities/governance/records-of-processing.md), [Data catalogue](../capabilities/metadata/data-catalogue.md), [Data lineage](../capabilities/metadata/data-lineage.md), [Data classification](../capabilities/governance/data-classification.md) |
| Article 32 – Security of processing | Apply security suited to the risk, such as encryption, pseudonymisation, resilience, timely restoration and regular testing of the measures. | [Encryption](../capabilities/security/encryption.md), [De-identification](../capabilities/governance/deidentification.md), [Access control](../capabilities/security/access-control.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Resilience and recovery testing](../capabilities/platform-operations/resilience-testing.md), [Audit logging](../capabilities/security/audit-logging.md) |
| Articles 33 and 34 – Personal data breach notification | Report breaches to the regulator within 72 hours where required, and tell affected people when the risk is high. | [Data breach response](../capabilities/security/data-breach-response.md), [Data threat detection](../capabilities/security/data-threat-detection.md), [Audit logging](../capabilities/security/audit-logging.md), [Data classification](../capabilities/governance/data-classification.md), [Data security posture management](../capabilities/security/data-security-posture.md), [Data loss prevention](../capabilities/security/data-loss-prevention.md) |
| Article 35 – Data protection impact assessment | Assess high-risk processing, such as large-scale profiling, before it starts. | [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Data classification](../capabilities/governance/data-classification.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) |
| Articles 44 to 49 – Transfers to third countries | Personal data may leave the EU only on the basis of adequacy, appropriate safeguards or specific derogations. | [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Cross-region and cross-cloud sharing](../capabilities/data-sharing/cross-region-sharing.md), [Customer-managed keys](../capabilities/security/customer-managed-keys.md), [Records of processing](../capabilities/governance/records-of-processing.md) |

# Related frameworks

- [EU AI Act](framework-eu-ai-act.md): Regulation (EU) 2024/1689, which sets risk-based rules for placing AI systems and general-purpose AI models on the EU market and using them.
- [CDMC (Cloud Data Management Capabilities)](framework-edm-cdmc.md): A framework of fourteen key controls for managing sensitive data in cloud and hybrid environments, with certification for cloud platforms and tools.
- [EU Data Act](framework-eu-data-act.md): Regulation (EU) 2023/2854 on fair access to and use of data, covering connected-product data, business-to-government access and switching between cloud services.
- [DORA (Digital Operational Resilience Act)](framework-eu-dora.md): Regulation (EU) 2022/2554, which sets ICT risk, incident, resilience testing and third-party requirements for EU financial entities.

# Applies to

- [Privacy rights handling](../use-cases/usecase-privacy-rights.md) (use case): Find, report and erase an individual's data across the estate within legal deadlines.
- [Sensitive data protection](../use-cases/usecase-sensitive-data-protection.md) (use case): Know where sensitive and personal data is across the platform, control who can reach it through one set of policies, and prove it to auditors.
- [Marketing audience activation](../use-cases/usecase-marketing-activation.md) (use case): Build audiences from platform data and sync them to marketing and advertising tools.
- [Customer 360](../use-cases/usecase-customer-360.md) (use case): Give every channel a single, trusted view of each customer.
- [Security and privacy officer](../personas/persona-security-officer.md) (persona): Protects data and makes sure it is used lawfully.
- [Risk and compliance officer](../personas/persona-risk-compliance.md) (persona): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
