---
type: Technology
id: aws-secrets-manager
title: AWS Secrets Manager
description: Stores database credentials, API keys and tokens encrypted with KMS and rotates them on a schedule.
platform: platform-aws
kind: managed-service
availability: ga
realises: [secrets-management]
resource: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Glue connections, Redshift, DMS, AppFlow and AgentCore Identity can reference secrets directly.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Secrets management](../../capabilities/security/secrets-management.md) (Security and access) (primary): Store and rotate the credentials and keys used by pipelines and tools without putting them in code.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Key Vault](../microsoft/azure-key-vault.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Secret Manager](../google-cloud/gcp-secret-manager.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake secrets](../snowflake/snowflake-secrets.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Secrets in Unity Catalog](../databricks/databricks-secrets-in-unity-catalog.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [OpenBao](../open-source/openbao.md) | [Secrets management](../../capabilities/security/secrets-management.md) |
