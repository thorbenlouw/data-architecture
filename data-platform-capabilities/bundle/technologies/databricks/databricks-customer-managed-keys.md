---
type: Technology
id: databricks-customer-managed-keys
title: Databricks customer-managed keys
description: Customer-held cloud KMS keys that encrypt control-plane data (notebooks, secrets, queries), workspace storage and, at catalogue level, Unity Catalog managed data.
platform: platform-databricks
kind: feature
availability: ga
realises: [customer-managed-keys]
resource: https://docs.databricks.com/aws/en/security/keys/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Unity Catalog CMK became GA in April 2026 and CMK for query history in October 2026. This feature requires the Enterprise tier on AWS.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access) (primary): Encrypt platform data with keys you control, so you can rotate or revoke them.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Key Management Service](../aws/aws-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Customer-managed keys for Fabric workspaces](../microsoft/fabric-customer-managed-keys.md), [Azure Key Vault](../microsoft/azure-key-vault.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Tri-Secret Secure](../snowflake/snowflake-tri-secret-secure.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](../clickhouse/clickhouse-cmek.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) |
