---
type: Maturity Track
id: track-governance
title: Governance operating model
description: How clearly the rules, roles and controls for managing data are defined, implemented on the platform and evidenced.
covers:
- data-ownership
- data-policy-management
- data-classification
- data-retention
- data-residency
- compliance-evidence
- data-certification
- data-domains
- critical-data-elements
- data-usage-rights
- governance-metrics
- stewardship-workflows
- regulatory-submission
- manual-adjustments
related_tracks: [track-metadata-catalogue, track-lineage, track-privacy, track-security]
levels:
- level: 1
  name: Initial
  summary: Policies exist on paper, and ownership and evidence depend on individuals.
  criteria:
  - Data policies exist as documents, but no platform setting implements them.
  - Who owns a dataset is known by habit, and nobody is accountable when it is wrong.
  - Data is kept indefinitely, and deletion happens only when storage runs out.
  - Audit evidence is gathered by hand for each request, often as screenshots.
  capabilities: []
- level: 2
  name: Managed
  summary: Owners, sensitivity labels and retention periods are recorded for the main data.
  criteria:
  - Named owners and stewards are recorded for the main data domains.
  - Sensitive datasets are labelled by hand using a defined scheme such as public, internal, confidential and restricted.
  - Retention periods are set for regulated data, and deletion jobs exist for part of it.
  - Owners mark the datasets that key reports rely on as certified.
  capabilities: [data-ownership, data-classification, data-retention, data-certification]
- level: 3
  name: Defined
  summary: Domains with stewardship workflows, machine-readable policies and location rules are applied consistently across platforms.
  criteria:
  - Data assets, products and owners are grouped into business domains, each with its own stewards, and tasks such as term approvals and classification reviews reach the right steward through a queue with deadlines, delegation and a recorded decision.
  - Policies are defined centrally in machine-readable form and applied through tags or policy engines on every platform.
  - Storage and processing are restricted to approved regions by platform configuration, and cross-border transfers are recorded.
  - Critical data elements for regulatory and financial reporting are listed, each with stricter quality, lineage and access requirements.
  - Licence terms and permitted uses, including whether model training is allowed, are recorded for every external or purchased dataset.
  capabilities:
  - data-domains
  - data-policy-management
  - data-residency
  - critical-data-elements
  - data-usage-rights
  - stewardship-workflows
- level: 4
  name: Measured
  summary: Coverage is reported against targets, controls are tested and evidenced automatically, and regulatory returns are validated before filing.
  criteria:
  - The share of assets that are owned, described, classified, monitored and access-controlled is reported per domain against targets.
  - New data is classified automatically at ingestion, and stewards review only uncertain results.
  - Automated control tests raise alerts for failures such as an unowned sensitive table or an unclassified column.
  - Auditors receive control evidence drawn from platform logs and reports without manual collection.
  - Regulatory returns are produced from governed tables in the regulator's format and validated against its rules before filing, and each manual adjustment to a reported figure has an approver, a reason and an audit record.
  capabilities: [governance-metrics, compliance-evidence, regulatory-submission, manual-adjustments]
- level: 5
  name: Optimising
  summary: Governance is built into templates, and policy changes and gaps are managed from evidence.
  criteria:
  - Policy changes are tested against the catalogue before release to show which assets and users they affect.
  - Coverage gaps are prioritised by risk and usage, and the time to close them is tracked.
  - Templates and pipelines apply governance rules at creation, so new assets start compliant and exceptions are recorded.
  - Disposal is verified by sampling deleted records across copies and backups.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up turns governance from policy documents and committees into ownership, classification and controls that are recorded on the platform, enforced automatically and reported as coverage figures. DCAM v3 scores this kind of programme against evidence, and CDMC's fourteen key controls describe what level 4 looks like for sensitive data in the cloud, with owners recorded, classification automated, residency and retention enforced and control failures alerted. Typical blockers are owners named without time or authority, classification done once by a project, and policies written in terms the platform cannot enforce.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Policies exist on paper, and ownership and evidence depend on individuals.

- Data policies exist as documents, but no platform setting implements them.
- Who owns a dataset is known by habit, and nobody is accountable when it is wrong.
- Data is kept indefinitely, and deletion happens only when storage runs out.
- Audit evidence is gathered by hand for each request, often as screenshots.

## Level 2: Managed

Owners, sensitivity labels and retention periods are recorded for the main data.

- Named owners and stewards are recorded for the main data domains.
- Sensitive datasets are labelled by hand using a defined scheme such as public, internal, confidential and restricted.
- Retention periods are set for regulated data, and deletion jobs exist for part of it.
- Owners mark the datasets that key reports rely on as certified.

**Capabilities first relied on:** [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Data classification](../capabilities/governance/data-classification.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Data certification](../capabilities/metadata/data-certification.md)

## Level 3: Defined

Domains with stewardship workflows, machine-readable policies and location rules are applied consistently across platforms.

- Data assets, products and owners are grouped into business domains, each with its own stewards, and tasks such as term approvals and classification reviews reach the right steward through a queue with deadlines, delegation and a recorded decision.
- Policies are defined centrally in machine-readable form and applied through tags or policy engines on every platform.
- Storage and processing are restricted to approved regions by platform configuration, and cross-border transfers are recorded.
- Critical data elements for regulatory and financial reporting are listed, each with stricter quality, lineage and access requirements.
- Licence terms and permitted uses, including whether model training is allowed, are recorded for every external or purchased dataset.

**Capabilities first relied on:** [Data domains](../capabilities/governance/data-domains.md), [Policy management](../capabilities/governance/data-policy-management.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md)

## Level 4: Measured

Coverage is reported against targets, controls are tested and evidenced automatically, and regulatory returns are validated before filing.

- The share of assets that are owned, described, classified, monitored and access-controlled is reported per domain against targets.
- New data is classified automatically at ingestion, and stewards review only uncertain results.
- Automated control tests raise alerts for failures such as an unowned sensitive table or an unclassified column.
- Auditors receive control evidence drawn from platform logs and reports without manual collection.
- Regulatory returns are produced from governed tables in the regulator's format and validated against its rules before filing, and each manual adjustment to a reported figure has an approver, a reason and an audit record.

**Capabilities first relied on:** [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md)

## Level 5: Optimising

Governance is built into templates, and policy changes and gaps are managed from evidence.

- Policy changes are tested against the catalogue before release to show which assets and users they affect.
- Coverage gaps are prioritised by risk and usage, and the time to close them is tracked.
- Templates and pipelines apply governance rules at creation, so new assets start compliant and exceptions are recorded.
- Disposal is verified by sampling deleted records across copies and backups.

# Capabilities in scope

[Approved manual adjustments](../capabilities/analytics-bi/manual-adjustments.md), [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md), [Critical data elements](../capabilities/governance/critical-data-elements.md), [Data certification](../capabilities/metadata/data-certification.md), [Data classification](../capabilities/governance/data-classification.md), [Data domains](../capabilities/governance/data-domains.md), [Data licensing and usage rights](../capabilities/governance/data-usage-rights.md), [Data residency and sovereignty](../capabilities/governance/data-residency.md), [Governance coverage metrics](../capabilities/governance/governance-metrics.md), [Ownership and stewardship](../capabilities/governance/data-ownership.md), [Policy management](../capabilities/governance/data-policy-management.md), [Regulatory submission](../capabilities/serving/regulatory-submission.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Stewardship workflows](../capabilities/governance/stewardship-workflows.md)

# Related tracks

- [Metadata and catalogue](track-metadata-catalogue.md): How completely and accurately data assets are described, findable and connected through metadata, for people and for machines.
- [Lineage](track-lineage.md): How completely and automatically the organisation can show where data came from, how it was changed and what depends on it.
- [Privacy](track-privacy.md): How reliably the organisation meets its obligations to the people its data describes, from purpose and consent to rights requests and de-identification.
- [Security and access control](track-security.md): How well data is protected from unauthorised access, loss and misuse, from identity through fine-grained access to threat detection.

Levels follow the shared [maturity scale](maturity-scale.md).
