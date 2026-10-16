---
type: Capability
id: encryption
title: Encryption
description: Encrypt data at rest and in transit, with keys managed securely.
broader: [security]
related: [secrets-management, deidentification, network-security, immutable-backups, data-residency]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Encryption at rest makes stored data unreadable without the key, and should cover files, table storage, backups, logs and temporary disks. Encryption in transit, normally TLS, protects data moving between clients, engines, storage and other services. Most platforms use envelope encryption: data is encrypted with data keys, which are themselves encrypted by key-encryption keys held in a key management service or hardware security module. Keys can then be rotated, and access to them controlled and logged separately from the data.

Cloud platforms now encrypt at rest by default, so the architectural questions are about keys: who holds and controls them, how they are rotated and how far you trust the operator. Encryption protects against lost disks, stolen backups and storage access that bypasses the platform, but not against anyone who can query the data through the platform with valid credentials; that is the job of access control. Field-level encryption goes further by encrypting individual values in the application, so only holders of a specific key can read them.

# Key considerations

- Check that encryption covers every place data lands: temporary and spill storage, caches, logs, backups, exports and replicas.
- Require TLS on every connection, including internal service traffic and older drivers and connectors, and disable outdated protocol versions.
- Field-level encryption protects values from administrators and broad readers, but encrypted fields are hard to filter, join or aggregate.
- Record which algorithms and key lengths protect which data. That record is the starting point for cryptographic agility.

# Questions to ask

- Which regulations or contracts specify encryption, key ownership or algorithms?
- Who should be able to decrypt the data: the platform operator, the organisation only, or specific applications?
- Is all traffic encrypted, including between internal services and from older tools?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Narrower | [Crypto-shredding](crypto-shredding.md), [Cryptographic agility](cryptographic-agility.md), [Customer-managed keys](customer-managed-keys.md) |
| Related | [Data residency and sovereignty](../governance/data-residency.md), [De-identification](../governance/deidentification.md), [Immutable backups](../platform-operations/immutable-backups.md), [Network security](network-security.md), [Object storage](../storage/object-storage.md), [Secrets management](secrets-management.md) |

# Where it appears

- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 1, Initial)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 9 Appropriate Security Controls (Protection and privacy) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 9 – Protection and prevention · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VII – Unlawful international governmental access · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality; Article 32 – Security of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Key Management Service](../../technologies/aws/aws-kms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Information Protection](../../technologies/microsoft/purview-information-protection.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Key Management Service](../../technologies/google-cloud/gcp-cloud-kms.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database security features](../../technologies/oracle/oracle-database-security.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database security (roles, row-level security, encryption)](../../technologies/teradata/teradata-security.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Sensitive Data Scanner and Cipher](../../technologies/palantir/palantir-sensitive-data-scanner-cipher.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenBao](../../technologies/open-source/openbao.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Protegrity Data Security Platform](../../technologies/independent/protegrity-data-security-platform.md) |

Narrower capabilities are realised by a further 9 technologies; see their pages.
