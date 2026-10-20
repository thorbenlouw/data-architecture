---
type: Technology
id: databricks-secrets-in-unity-catalog
title: Secrets in Unity Catalog
description: Credentials stored as governed Unity Catalog securables under a catalog.schema.secret name, with grants and audit.
platform: platform-databricks
kind: feature
availability: ga
realises: [secrets-management]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/august
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA in August 2026. They complement or replace workspace secret scopes and can back Unity Gateway provider credentials.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access) (primary): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Secrets Manager](../aws/aws-secrets-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Key Vault](../microsoft/azure-key-vault.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Secret Manager](../google-cloud/gcp-secret-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake secrets](../snowflake/snowflake-secrets.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku DSS](../dataiku/dataiku.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
