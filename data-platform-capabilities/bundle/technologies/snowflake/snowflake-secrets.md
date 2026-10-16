---
type: Technology
id: snowflake-secrets
title: Snowflake secrets
description: Schema-level secret objects that hold credentials, OAuth tokens and keys for integrations, UDFs, Openflow and container services, so code does not contain them.
platform: platform-snowflake
kind: feature
availability: ga
realises: [secrets-management]
resource: https://docs.snowflake.com/en/sql-reference/sql/create-secret
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Pulling secrets from AWS, Azure or Google Cloud secret managers through external secret providers is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access) (primary): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Secrets Manager](../aws/aws-secrets-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Key Vault](../microsoft/azure-key-vault.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Secret Manager](../google-cloud/gcp-secret-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Secrets in Unity Catalog](../databricks/databricks-secrets-in-unity-catalog.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
