---
type: Maturity Track
id: track-privacy
title: Privacy
description: How reliably the organisation meets its obligations to the people its data describes, from purpose and consent to rights requests and de-identification.
covers:
- privacy-management
- data-subject-requests
- consent-management
- deidentification
- privacy-enhancing-technologies
- records-of-processing
- privacy-impact-assessment
- data-breach-response
- crypto-shredding
related_tracks: [track-governance, track-security, track-data-sharing]
levels:
- level: 1
  name: Initial
  summary: Privacy obligations are handled case by case through emails and spreadsheets.
  criteria:
  - Access and erasure requests are handled by emailing teams and asking them to search their systems.
  - Personal data is used in identifiable form in development and analytics.
  - The register of processing, if any, is a spreadsheet kept by the privacy team with no link to datasets.
  capabilities: []
- level: 2
  name: Managed
  summary: Defined procedures cover rights requests, assessments and pseudonymisation for the main personal datasets.
  criteria:
  - A procedure with named contacts handles rights requests for the main systems, and completion dates are recorded.
  - Direct identifiers are pseudonymised or tokenised in analytical copies of the main personal datasets.
  - New projects known to the privacy team complete an impact assessment on a standard template.
  - The register of processing lists purposes, data categories and recipients for the main activities.
  capabilities: [data-subject-requests, deidentification, privacy-impact-assessment, records-of-processing]
- level: 3
  name: Defined
  summary: Consent and purpose are available to the platform as data and enforced in access rules, and breaches are assessed from catalogue evidence.
  criteria:
  - Each person's consents and permitted purposes are held centrally and available to platform jobs and policies.
  - Access to personal data is granted for a stated purpose, and policy rules filter queries by purpose and consent.
  - Rights requests are fulfilled by an automated search of catalogued personal data, located through classification.
  - Each entry in the register of processing links to the datasets and pipelines it describes.
  - A breach procedure uses the catalogue, classification and access logs to establish which data and which people an incident exposed, and notifications to regulators and individuals are made within the legal deadlines and recorded.
  capabilities: [consent-management, data-breach-response]
- level: 4
  name: Measured
  summary: Deadlines, erasure reach and privacy techniques are measured and triggered automatically.
  criteria:
  - Rights requests are tracked against legal deadlines, and completion rates and systems reached are reported.
  - Erasure reaches history, derived tables and backups, by deleting records or by destroying the per-person keys that encrypt them, and is verified by sampled checks.
  - A dataset newly classified as personal triggers an impact assessment automatically.
  - Aggregate releases use minimum group sizes or differential privacy, and privacy budgets are tracked.
  capabilities: [privacy-enhancing-technologies, crypto-shredding]
- level: 5
  name: Optimising
  summary: Privacy controls are applied by default and tested against changing re-identification risk.
  criteria:
  - De-identified datasets are tested for re-identification risk on a schedule, and techniques change when risk rises.
  - A withdrawn consent reaches every downstream use, including training sets for models, within a measured time.
  - Masking, purpose tags and retention are applied by templates when a dataset is created.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up means personal data is known, used only for permitted purposes and de-identified where possible, and access or erasure requests reach every copy within the legal deadline. GDPR's purpose limitation, data protection by design, records of processing and individuals' rights set the bar, and CDMC key control 10 expects impact assessments to be triggered automatically by classification, which is level 4 here. Typical blockers are personal data copied widely before anyone classifies it, consent captured in front-end systems but not carried to the platform, and history and backups that erasure jobs do not reach.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Privacy obligations are handled case by case through emails and spreadsheets.

- Access and erasure requests are handled by emailing teams and asking them to search their systems.
- Personal data is used in identifiable form in development and analytics.
- The register of processing, if any, is a spreadsheet kept by the privacy team with no link to datasets.

## Level 2: Managed

Defined procedures cover rights requests, assessments and pseudonymisation for the main personal datasets.

- A procedure with named contacts handles rights requests for the main systems, and completion dates are recorded.
- Direct identifiers are pseudonymised or tokenised in analytical copies of the main personal datasets.
- New projects known to the privacy team complete an impact assessment on a standard template.
- The register of processing lists purposes, data categories and recipients for the main activities.

**Capabilities first relied on:** [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Records of processing](../capabilities/governance/records-of-processing.md)

## Level 3: Defined

Consent and purpose are available to the platform as data and enforced in access rules, and breaches are assessed from catalogue evidence.

- Each person's consents and permitted purposes are held centrally and available to platform jobs and policies.
- Access to personal data is granted for a stated purpose, and policy rules filter queries by purpose and consent.
- Rights requests are fulfilled by an automated search of catalogued personal data, located through classification.
- Each entry in the register of processing links to the datasets and pipelines it describes.
- A breach procedure uses the catalogue, classification and access logs to establish which data and which people an incident exposed, and notifications to regulators and individuals are made within the legal deadlines and recorded.

**Capabilities first relied on:** [Consent and purpose management](../capabilities/governance/consent-management.md), [Data breach response](../capabilities/security/data-breach-response.md)

## Level 4: Measured

Deadlines, erasure reach and privacy techniques are measured and triggered automatically.

- Rights requests are tracked against legal deadlines, and completion rates and systems reached are reported.
- Erasure reaches history, derived tables and backups, by deleting records or by destroying the per-person keys that encrypt them, and is verified by sampled checks.
- A dataset newly classified as personal triggers an impact assessment automatically.
- Aggregate releases use minimum group sizes or differential privacy, and privacy budgets are tracked.

**Capabilities first relied on:** [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md)

## Level 5: Optimising

Privacy controls are applied by default and tested against changing re-identification risk.

- De-identified datasets are tested for re-identification risk on a schedule, and techniques change when risk rises.
- A withdrawn consent reaches every downstream use, including training sets for models, within a measured time.
- Masking, purpose tags and retention are applied by templates when a dataset is created.

# Capabilities in scope

[Consent and purpose management](../capabilities/governance/consent-management.md), [Crypto-shredding](../capabilities/security/crypto-shredding.md), [Data breach response](../capabilities/security/data-breach-response.md), [Data subject requests](../capabilities/governance/data-subject-requests.md), [De-identification](../capabilities/governance/deidentification.md), [Privacy impact assessment](../capabilities/governance/privacy-impact-assessment.md), [Privacy management](../capabilities/governance/privacy-management.md), [Privacy-enhancing technologies](../capabilities/governance/privacy-enhancing-technologies.md), [Records of processing](../capabilities/governance/records-of-processing.md)

# Related tracks

- [Governance operating model](track-governance.md): How clearly the rules, roles and controls for managing data are defined, implemented on the platform and evidenced.
- [Security and access control](track-security.md): How well data is protected from unauthorised access, loss and misuse, from identity through fine-grained access to threat detection.
- [Data sharing](track-data-sharing.md): How safely and efficiently data is shared between teams and with external parties without unnecessary copies.

Levels follow the shared [maturity scale](maturity-scale.md).
