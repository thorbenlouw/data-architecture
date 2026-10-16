---
type: Technology
id: aws-kms
title: AWS Key Management Service
description: Managed service for creating, rotating and controlling encryption keys used by AWS services and applications.
aliases: [AWS KMS]
platform: platform-aws
kind: managed-service
availability: ga
realises: [encryption, customer-managed-keys, crypto-shredding]
resource: https://docs.aws.amazon.com/kms/latest/developerguide/overview.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Customer managed keys can be disabled or scheduled for deletion to revoke access; external key stores keep key material outside AWS. Nearly all data services support KMS keys at rest.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Encryption](../../capabilities/security/encryption.md) (Security and access) (primary): Encrypt data at rest and in transit, with keys managed securely.
- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access): Encrypt platform data with keys you control, so you can rotate or revoke them.
- [Crypto-shredding](../../capabilities/security/crypto-shredding.md) (Security and access): Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Azure Key Vault](../microsoft/azure-key-vault.md) | [Encryption](../../capabilities/security/encryption.md), [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Encryption](../../capabilities/security/encryption.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md) | [Encryption](../../capabilities/security/encryption.md) |
