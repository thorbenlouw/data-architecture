---
type: Technology
id: clickhouse-cmek
title: ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)
description: Adds database-level encryption to Cloud services and lets the customer supply and rotate the wrapping key in AWS KMS, GCP KMS or Azure Key Vault.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [customer-managed-keys]
resource: https://clickhouse.com/docs/cloud/security/cmek
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Enterprise tier; TDE must be chosen when the service is created and cannot be removed. Revoking key access stops the service within about ten minutes, and deleting the key makes data and backups unrecoverable. Expect a 5-15% performance cost. All Cloud data is encrypted at rest with provider-managed keys by default.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access) (primary): Encrypt platform data with keys you control, so you can rotate or revoke them.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Key Management Service](../aws/aws-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Customer-managed keys for Fabric workspaces](../microsoft/fabric-customer-managed-keys.md), [Azure Key Vault](../microsoft/azure-key-vault.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Tri-Secret Secure](../snowflake/snowflake-tri-secret-secure.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks customer-managed keys](../databricks/databricks-customer-managed-keys.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
