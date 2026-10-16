---
type: Technology
id: gcp-cloud-kms
title: Google Cloud Key Management Service
description: Creates and manages encryption keys, including hardware-backed and externally held keys, used as customer-managed encryption keys by Google Cloud services.
aliases: [Cloud KMS, Cloud HSM, Cloud External Key Manager, Cloud KMS Autokey]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [encryption, customer-managed-keys, crypto-shredding]
resource: https://docs.cloud.google.com/kms/docs/key-management-service
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Cloud HSM, Cloud External Key Manager and Autokey (automatic key provisioning) are part of the family. Data is encrypted at rest by default with Google-managed keys.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Encryption](../../capabilities/security/encryption.md) (Security and access) (primary): Encrypt data at rest and in transit, with keys managed securely.
- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access): Encrypt platform data with keys you control, so you can rotate or revoke them.
- [Crypto-shredding](../../capabilities/security/crypto-shredding.md) (Security and access): Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Key Management Service](../aws/aws-kms.md) | [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Azure Key Vault](../microsoft/azure-key-vault.md) | [Encryption](../../capabilities/security/encryption.md), [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md) | [Encryption](../../capabilities/security/encryption.md) |
