---
type: Capability
id: crypto-shredding
title: Crypto-shredding
description: Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it.
aliases: [key deletion erasure]
broader: [encryption, data-subject-requests]
related: [data-retention, immutable-backups, backup-restore, deidentification, customer-managed-keys]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data is encrypted with keys at a fine grain, such as one key per customer, tenant or dataset, and the keys are held in a key management service apart from the data. To erase a person's data, the system destroys that person's key. Every copy encrypted with it, in tables, logs, replicas and years of backups, becomes unreadable at once, without finding and rewriting each copy. The usual design is envelope encryption: a data key encrypts the records, and is itself encrypted by a master key held in the key service.

It solves erasure where deleting rows is impractical: immutable backups, append-only event streams, archived files and table history. Common uses are data subject requests, retention expiry and tenant offboarding. It needs field- or record-level encryption applied by the application or pipeline; storage encryption managed by the platform uses keys that are not tied to individuals. Revoking a customer-managed key is a coarse form that makes a whole account's data unreadable.

# Key considerations

- Destroying a key by mistake loses data for good. Key backup, replication and deletion need strict controls, separate duties and a waiting period before final destruction.
- Millions of per-person keys add load and cost to the key service. Caching data keys and grouping people into shared key buckets reduce this, at the cost of less precise erasure.
- Values decrypted and copied in clear, into derived tables, extracts, caches or search indexes, are not covered. Lineage must show where decrypted values flow.
- Encrypted fields cannot be filtered, joined or aggregated without decrypting them, which affects query design and performance.
- Confirm with legal and privacy teams that key destruction counts as erasure in your jurisdictions, and keep a record of each destruction as evidence.

# Questions to ask

- Where does personal data persist in places that cannot easily be rewritten, such as backups, event logs and archives?
- At what grain must erasure work: person, customer account, tenant or dataset?
- Who controls the encryption keys today, and can a single key be destroyed and proven destroyed?
- How would decrypted copies in downstream systems be found and removed?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Encryption](encryption.md), [Data subject requests](../governance/data-subject-requests.md) |
| Related | [Backup and restore](../platform-operations/backup-restore.md), [Customer-managed keys](customer-managed-keys.md), [De-identification](../governance/deidentification.md), [Immutable backups](../platform-operations/immutable-backups.md), [Retention and disposal](../governance/data-retention.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from)
- **Personas:** [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 4, Measured)
- **Frameworks:** [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(e) – Storage limitation; Article 17 – Right to erasure

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Key Management Service](../../technologies/aws/aws-kms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Key Vault](../../technologies/microsoft/azure-key-vault.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Key Management Service](../../technologies/google-cloud/gcp-cloud-kms.md) |
