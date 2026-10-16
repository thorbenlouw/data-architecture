---
type: Capability
id: immutable-backups
title: Immutable backups
description: Keep backups that nobody can delete or change before they expire, with legal holds, to protect against ransomware.
aliases: [WORM backups, vault lock]
broader: [backup-restore]
related: [data-retention, data-threat-detection, data-subject-requests, compliance-evidence]
depends_on: [object-storage]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The protection comes from the storage service, not from permissions. Write-once-read-many (WORM) object locking in compliance mode, or a locked backup vault, refuses any delete or overwrite until each object's retention date has passed, even from administrators or the account owner. An attacker with stolen admin credentials therefore cannot remove the copies. A legal hold blocks deletion with no end date until it is lifted, for data under investigation or litigation. Immutable copies are often also kept in a separate account with separate credentials, sometimes called a logical air gap.

Ransomware attackers now commonly delete or encrypt backups first, so the victim cannot recover without paying. Immutable backups survive that step. They also meet records rules in finance and other sectors that require some data to be kept in a form that cannot be rewritten or erased. The cost is rigidity: data locked in compliance mode cannot be deleted early, even if it was backed up by mistake or contains personal data that someone has asked to have erased.

# Key considerations

- Choose retention periods carefully before locking. In compliance mode nobody can shorten them, and storage charges continue until they expire.
- Document how erasure obligations apply to locked copies, for example by limiting their retention and re-applying erasures before any restore.
- Separate the accounts and credentials that manage backups from those that run the platform.
- Test restores from the immutable copy itself, not only from ordinary backups.

# Questions to ask

- Is ransomware recovery part of your threat model and continuity plan?
- Do regulations require any records to be kept in non-rewritable, non-erasable form?
- Who could delete your backups today, and with which credentials?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Backup and restore](backup-restore.md) |
| Related | [Audit logging](../security/audit-logging.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Crypto-shredding](../security/crypto-shredding.md), [Data subject requests](../governance/data-subject-requests.md), [Data threat detection](../security/data-threat-detection.md), [Encryption](../security/encryption.md), [Retention and disposal](../governance/data-retention.md), [Storage tiering and lifecycle](../storage/storage-tiering.md) |
| Depends on | [Object storage](../storage/object-storage.md) |

# Where it appears

- **Use cases:** [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Resilience and recovery](../../maturity/track-resilience.md) (from level 3, Defined)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Articles 11 and 12 – Response and recovery; backup, restoration and recovery

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon S3](../../technologies/aws/aws-s3.md), [AWS Backup](../../technologies/aws/aws-backup.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Backup](../../technologies/microsoft/azure-backup.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Storage](../../technologies/google-cloud/gcp-cloud-storage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake backups](../../technologies/snowflake/snowflake-backups.md) |
