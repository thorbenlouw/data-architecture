---
type: Technology
id: azure-key-vault
title: Azure Key Vault
description: Stores secrets, keys and certificates with access control, rotation and HSM backing, including Managed HSM for single-tenant keys.
aliases: [Azure Key Vault Managed HSM]
platform: platform-microsoft
kind: managed-service
availability: ga
realises: [secrets-management, customer-managed-keys, crypto-shredding]
resource: https://learn.microsoft.com/en-us/azure/key-vault/general/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access) (primary): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.
- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access): Encrypt platform data with keys you control, so you can rotate or revoke them.
- [Crypto-shredding](../../capabilities/security/crypto-shredding.md) (Security and access): Make specific data unreadable everywhere, including in backups, by destroying the encryption keys that protect it.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Secrets Manager](../aws/aws-secrets-manager.md), [AWS Key Management Service](../aws/aws-kms.md) | [Secrets management](../../capabilities/security/secrets-management.md), [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Secret Manager](../google-cloud/gcp-secret-manager.md), [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Secrets management](../../capabilities/security/secrets-management.md), [Crypto-shredding](../../capabilities/security/crypto-shredding.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake secrets](../snowflake/snowflake-secrets.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Secrets in Unity Catalog](../databricks/databricks-secrets-in-unity-catalog.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
