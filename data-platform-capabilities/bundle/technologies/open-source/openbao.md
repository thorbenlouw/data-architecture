---
type: Technology
id: openbao
title: OpenBao
description: Secrets management server that stores, issues and rotates credentials, keys and certificates, forked from HashiCorp Vault.
platform: platform-open-source
kind: open-source
availability: ga
realises: [secrets-management, encryption]
resource: https://openbao.org/
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

MPL 2.0, under the Linux Foundation's OpenSSF. Created after HashiCorp moved Vault to the Business Source License in 2023; broadly API-compatible with Vault.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access) (primary): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Secrets Manager](../aws/aws-secrets-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Key Vault](../microsoft/azure-key-vault.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Secret Manager](../google-cloud/gcp-secret-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake secrets](../snowflake/snowflake-secrets.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Secrets in Unity Catalog](../databricks/databricks-secrets-in-unity-catalog.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
