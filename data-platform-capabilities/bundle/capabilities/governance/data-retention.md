---
type: Capability
id: data-retention
title: Retention and disposal
description: Keep data for as long as required, then delete it reliably, including from history, snapshots and backups, with legal holds when needed.
broader: [governance]
related: [storage-tiering, immutable-backups, row-level-updates, table-maintenance, records-of-processing]
depends_on: [data-classification, row-level-updates]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Each category of data gets a retention period from law, contract or policy, for example "keep transaction records for seven years after account closure" or "delete web logs after 13 months". The platform applies the period by deleting, archiving or anonymising data when it expires, usually through scheduled jobs driven by tags on tables or by date columns within them. A legal hold suspends deletion of data relevant to litigation or an investigation until the hold is lifted.

Keeping data too long increases breach impact, storage cost and privacy risk; deleting it too soon breaks legal and business obligations. Retention is harder than it looks on modern platforms, because table history, snapshots, backups, replicas, caches, exports and derived tables all hold copies, and a period set on the source does not reach them unless it is propagated. Retention differs from storage tiering, which moves data to cheaper storage but keeps it, and from immutable backups, which deliberately prevent deletion for a fixed time.

# Key considerations

- Define retention by data category and attach it through classification or domain policy, rather than setting periods table by table.
- Account for every copy: table history, snapshots, backups, replicas, extracts and derived tables. Deletion in one place is not disposal.
- Retention clocks often start from a business event, such as contract end, not from the load date. Store the date needed to calculate expiry.
- Legal holds must override deletion everywhere, including automated table maintenance and storage lifecycle rules, and be logged.
- Record what was deleted, when and under which rule, so you can prove disposal happened.

# Questions to ask

- Is there an approved retention schedule, and is it mapped to datasets on the platform?
- Which retention periods start from a business event rather than from when data was loaded?
- How are legal holds raised, and which systems must honour them?
- How long do backups and table history keep data after it is deleted from the live table?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md) |
| Related | [Storage and table management](../storage/storage.md), [Agent memory](../generative-ai/agent-memory.md), [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md), [Backup and disaster recovery](../platform-operations/business-continuity.md), [Backup and restore](../platform-operations/backup-restore.md), [Crypto-shredding](../security/crypto-shredding.md), [Customer-managed keys](../security/customer-managed-keys.md), [Data subject requests](data-subject-requests.md), [Data versioning](../storage/data-versioning.md), [Immutable backups](../platform-operations/immutable-backups.md), [Inference logging](../mlops/inference-logging.md), [Policy management](data-policy-management.md), [Privacy management](privacy-management.md), [Records of processing](records-of-processing.md), [Row-level updates and deletes](../storage/row-level-updates.md), [Storage tiering and lifecycle](../storage/storage-tiering.md), [Table maintenance and optimisation](../storage/table-maintenance.md), [Time travel](../storage/time-travel.md) |
| Depends on | [Data classification](data-classification.md), [Row-level updates and deletes](../storage/row-level-updates.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 12 Data Retention, Archiving and Purging (Data lifecycle) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Document and Content Management · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection; Articles 19 and 26(6) – Log retention · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(e) – Storage limitation; Article 17 – Right to erasure · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Service-Level Agreement

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3](../../technologies/aws/aws-s3.md), [Amazon S3 storage classes and S3 Lifecycle](../../technologies/aws/aws-s3-storage-classes-lifecycle.md), [AWS Backup](../../technologies/aws/aws-backup.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Lifecycle Management](../../technologies/microsoft/purview-data-lifecycle-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake backups](../../technologies/snowflake/snowflake-backups.md), [Snowflake storage lifecycle policies](../../technologies/snowflake/snowflake-storage-lifecycle-policies.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | TTL | [ClickHouse TTL (time to live)](../../technologies/clickhouse/clickhouse-ttl.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM InfoSphere Optim](../../technologies/ibm/ibm-optim.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [BigID Next](../../technologies/independent/bigid-next.md), [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
