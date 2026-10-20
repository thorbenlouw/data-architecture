---
type: Use Case
id: usecase-privacy-rights
title: Privacy rights handling
description: Find, report and erase an individual's data across the estate within legal deadlines.
aliases: [DSAR handling, right to erasure]
requires:
- {capability: data-subject-requests, level: 3, why: 'Access, correction and erasure requests run through a standard, tracked process.'}
- {capability: data-classification, level: 3, why: Every table and column holding personal data must be labelled to be found.}
- {capability: metadata-harvesting, level: 3, why: 'New tables and files must be picked up automatically, or the inventory goes out of date.'}
- {capability: entity-resolution, level: 2, why: The same person appears under different identifiers in different systems.}
- {capability: cross-system-lineage, level: 2, why: Downstream copies and derived tables that hold the person's data must be found.}
- {capability: row-level-updates, level: 3, why: Individual rows must be deleted or corrected efficiently in very large tables.}
- {capability: table-maintenance, level: 3, why: 'Deleted rows must also be purged from old data files and table history, not only hidden.'}
- {capability: data-retention, level: 3, why: Retention rules and legal holds decide what may be erased and what must be kept.}
- {capability: records-of-processing, level: 2, why: 'Access responses must state purposes, recipients and retention for the person''s data.'}
- {capability: workflow-orchestration, level: 2, why: Requests fan out to many systems and must be tracked against legal deadlines.}
- {capability: data-export, level: 2, why: 'Subject access responses must be produced in a readable, portable format.'}
- {capability: backup-restore, level: 2, why: Erasure must not be undone when backups are restored.}
- {capability: audit-logging, level: 3, why: 'Evidence of what was found, changed and deleted, and when, must be kept.'}
benefits_from:
- {capability: deidentification, why: Pseudonymised data reduces what must be found and changed.}
- {capability: master-data-management, why: A golden customer record gives a starting point for each search.}
- {capability: consent-management, why: Links requests to what the person agreed to.}
- {capability: data-security-posture, why: Finds copies of personal data that the catalogue does not know about.}
- {capability: unstructured-lineage, why: Locates documents and AI indexes that contain the person's data.}
- {capability: change-feeds, why: Propagates deletions to downstream consumers automatically.}
- {capability: active-metadata, why: Applies personal-data tags automatically to derived tables.}
- {capability: compliance-evidence, why: Gives regulators summary evidence across all requests.}
- {capability: crypto-shredding, why: 'Makes a person''s data unreadable in backups, event logs and archives that cannot be rewritten within the deadline.'}
personas:
- persona-security-officer
- persona-risk-compliance
- persona-data-engineer
- persona-data-steward
- persona-platform-engineer
- persona-software-engineer
patterns: [shift-left]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Under GDPR, UK GDPR, CCPA and similar laws, people can ask an organisation what personal data it holds about them, ask for a copy, ask for corrections or ask for it to be erased. Each request has a legal deadline, often one month. On a data platform this means finding every record about the person across raw, curated and derived tables, files, indexes and exports, assembling a report or applying the erasure, and keeping evidence that it was done.

Good looks like requests completed within deadline at the volume that arrives, erasure applied everywhere including derived tables, history kept by table formats, search indexes and copies in downstream tools, backups handled according to a documented policy, and an audit trail for each request. This is only possible when the platform knows where personal data is and how it flows.

# Non-functional requirements

- Requests are completed within legal deadlines, such as one month under GDPR (extendable in some cases) and 45 days under CCPA.
- Erasure covers analytical, derived and indexed copies, and backups follow a documented policy.
- The requester's identity is verified before any data is released.
- Each request has a retained evidence trail.
- The process copes with request volumes from tens to thousands a month.

# Risks

- Copies in sandboxes, notebooks and exports outside the catalogue are missed.
- Deleted rows remain in table history, search indexes or model training sets.
- Poor matching releases one person's data to another.
- A manual process cannot keep up when volumes rise.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Data subject requests](../capabilities/governance/data-subject-requests.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Access, correction and erasure requests run through a standard, tracked process. |
| [Data classification](../capabilities/governance/data-classification.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Every table and column holding personal data must be labelled to be found. |
| [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 3 (Defined) | New tables and files must be picked up automatically, or the inventory goes out of date. |
| [Entity resolution](../capabilities/master-data/entity-resolution.md) | [Master and reference data](../capabilities/master-data/master-data.md) | 2 (Managed) | The same person appears under different identifiers in different systems. |
| [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md) | [Metadata and discovery](../capabilities/metadata/metadata.md) | 2 (Managed) | Downstream copies and derived tables that hold the person's data must be found. |
| [Row-level updates and deletes](../capabilities/storage/row-level-updates.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Individual rows must be deleted or corrected efficiently in very large tables. |
| [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md) | [Storage and table management](../capabilities/storage/storage.md) | 3 (Defined) | Deleted rows must also be purged from old data files and table history, not only hidden. |
| [Retention and disposal](../capabilities/governance/data-retention.md) | [Governance and compliance](../capabilities/governance/governance.md) | 3 (Defined) | Retention rules and legal holds decide what may be erased and what must be kept. |
| [Records of processing](../capabilities/governance/records-of-processing.md) | [Governance and compliance](../capabilities/governance/governance.md) | 2 (Managed) | Access responses must state purposes, recipients and retention for the person's data. |
| [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md) | [Orchestration](../capabilities/orchestration/orchestration.md) | 2 (Managed) | Requests fan out to many systems and must be tracked against legal deadlines. |
| [Data export](../capabilities/serving/data-export.md) | [Serving and activation](../capabilities/serving/serving.md) | 2 (Managed) | Subject access responses must be produced in a readable, portable format. |
| [Backup and restore](../capabilities/platform-operations/backup-restore.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Erasure must not be undone when backups are restored. |
| [Audit logging](../capabilities/security/audit-logging.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Evidence of what was found, changed and deleted, and when, must be kept. |

# Capabilities that help

| Capability | Why |
|---|---|
| [De-identification](../capabilities/governance/deidentification.md) | Pseudonymised data reduces what must be found and changed. |
| [Master data management](../capabilities/master-data/master-data-management.md) | A golden customer record gives a starting point for each search. |
| [Consent and purpose management](../capabilities/governance/consent-management.md) | Links requests to what the person agreed to. |
| [Data security posture management](../capabilities/security/data-security-posture.md) | Finds copies of personal data that the catalogue does not know about. |
| [Document and unstructured lineage](../capabilities/metadata/unstructured-lineage.md) | Locates documents and AI indexes that contain the person's data. |
| [Change feeds](../capabilities/serving/change-feeds.md) | Propagates deletions to downstream consumers automatically. |
| [Active metadata](../capabilities/metadata/active-metadata.md) | Applies personal-data tags automatically to derived tables. |
| [Compliance controls and evidence](../capabilities/governance/compliance-evidence.md) | Gives regulators summary evidence across all requests. |
| [Crypto-shredding](../capabilities/security/crypto-shredding.md) | Makes a person's data unreadable in backups, event logs and archives that cannot be rewritten within the deadline. |

# Personas

- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [Risk and compliance officer](../personas/persona-risk-compliance.md): Needs assurance, with evidence, that data controls meet regulatory and internal requirements.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Data steward](../personas/persona-data-steward.md): Looks after the definition, quality and proper use of data in a business domain.
- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Software engineer](../personas/persona-software-engineer.md): Builds applications that produce data for the platform or consume data from it.

# Patterns

- [Shift-left data quality and governance](../patterns/shift-left.md)

# Frameworks that apply

- [GDPR](../frameworks/framework-gdpr.md): Regulation (EU) 2016/679, the EU's general law on processing personal data, which sets principles, legal bases, individuals' rights and controller duties.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 12 of 13 | [Records of processing](../capabilities/governance/records-of-processing.md) |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 11 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| [Google Cloud](../platforms/platform-google-cloud.md) | 11 of 13 | [Entity resolution](../capabilities/master-data/entity-resolution.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 10 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| [Databricks](../platforms/platform-databricks.md) | 8 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data export](../capabilities/serving/data-export.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 7 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Records of processing](../capabilities/governance/records-of-processing.md) |
| [Informatica](../platforms/platform-informatica.md) | 6 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data export](../capabilities/serving/data-export.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 8 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data export](../capabilities/serving/data-export.md) |
| [Oracle](../platforms/platform-oracle.md) | 5 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data export](../capabilities/serving/data-export.md) |
| [SAP](../platforms/platform-sap.md) | 3 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md), [Audit logging](../capabilities/security/audit-logging.md) |
| [Teradata](../platforms/platform-teradata.md) | 2 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data export](../capabilities/serving/data-export.md) |
| [IBM](../platforms/platform-ibm.md) | 6 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data export](../capabilities/serving/data-export.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| [Palantir](../platforms/platform-palantir.md) | 3 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| [SAS](../platforms/platform-sas.md) | 4 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Workflow orchestration](../capabilities/orchestration/workflow-orchestration.md), [Data export](../capabilities/serving/data-export.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| [Dataiku](../platforms/platform-dataiku.md) | 3 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Data classification](../capabilities/governance/data-classification.md), [Metadata harvesting](../capabilities/metadata/metadata-harvesting.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [End-to-end lineage](../capabilities/metadata/cross-system-lineage.md), [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Table maintenance and optimisation](../capabilities/storage/table-maintenance.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Data export](../capabilities/serving/data-export.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 8 of 13 | [Data subject requests](../capabilities/governance/data-subject-requests.md), [Entity resolution](../capabilities/master-data/entity-resolution.md), [Retention and disposal](../capabilities/governance/data-retention.md), [Records of processing](../capabilities/governance/records-of-processing.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
| [Independent vendors](../platforms/platform-independent.md) | 10 of 13 | [Row-level updates and deletes](../capabilities/storage/row-level-updates.md), [Data export](../capabilities/serving/data-export.md), [Backup and restore](../capabilities/platform-operations/backup-restore.md) |
