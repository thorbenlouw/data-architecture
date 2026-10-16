---
type: Technology
id: snowflake-tri-secret-secure
title: Snowflake Tri-Secret Secure
description: Combines a Snowflake-maintained key with a customer-managed key in the cloud provider's KMS to create the composite master key for account data, so revoking the customer key makes data unreadable.
platform: platform-snowflake
kind: feature
availability: ga
realises: [customer-managed-keys]
resource: https://docs.snowflake.com/en/user-guide/security-encryption-manage
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Business Critical Edition. All data is encrypted at rest and in transit by default, with hierarchical key rotation and optional periodic rekeying.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access) (primary): Encrypt platform data with keys you control, so you can rotate or revoke them.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Key Management Service](../aws/aws-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Customer-managed keys for Fabric workspaces](../microsoft/fabric-customer-managed-keys.md), [Azure Key Vault](../microsoft/azure-key-vault.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks customer-managed keys](../databricks/databricks-customer-managed-keys.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](../clickhouse/clickhouse-cmek.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
