---
type: Capability
id: customer-managed-keys
title: Customer-managed keys
description: Encrypt platform data with keys you control, so you can rotate or revoke them.
aliases: [CMK, BYOK, HYOK]
broader: [encryption]
related: [data-residency, data-retention, hybrid-data-plane, secrets-management, data-subject-requests]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

With customer-managed keys, the key-encryption keys protecting platform data sit in a key management service or hardware security module you control, not one the operator controls. The platform asks your key service to unwrap data keys, and each use is logged. You rotate the key on your own schedule and can disable or revoke it, after which the platform can no longer read the data it protects. Variants include keys created in the cloud provider's key service, keys you generate and import ("bring your own key") and keys kept in an external key manager ("hold your own key").

Regulated firms, public bodies and enterprise customers often require this to show control over who can read their data and to allow crypto-shredding, where destroying a key makes all data under it unreadable. The cost is operational risk: if the key service fails, the platform stops; if a key is deleted, the data is lost for good. The encryption is no stronger than the default; only control over keys changes.

# Key considerations

- Check which data the customer key really covers. Metadata, result caches, logs, search indexes and AI features may use separate keys.
- Protect keys against accidental deletion with deletion delays, dual approval and backups where the key service allows.
- Key service availability becomes platform availability. Plan for regional outages and replicate keys where disaster recovery needs them.
- Revoking a key is an emergency stop. Test what happens to running workloads and how quickly service returns when the key is re-enabled.

# Questions to ask

- Is control over keys a regulatory, contractual or sovereignty requirement, or a preference?
- Who may rotate, disable or delete keys, and with what approval?
- Does the requirement extend to backups, logs, metadata and AI services?
- Would the organisation use key revocation as an exit or emergency control?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Encryption](encryption.md) |
| Related | [Crypto-shredding](crypto-shredding.md), [Cryptographic agility](cryptographic-agility.md), [Customer-hosted data plane](../platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../governance/data-residency.md), [Data subject requests](../governance/data-subject-requests.md), [Retention and disposal](../governance/data-retention.md), [Secrets management](secrets-management.md) |

# Where it appears

- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 4, Measured)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 9 Appropriate Security Controls (Protection and privacy) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VII – Unlawful international governmental access · [GDPR](../../frameworks/framework-gdpr.md): Articles 44 to 49 – Transfers to third countries

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | AWS KMS customer managed keys | [AWS Key Management Service](../../technologies/aws/aws-kms.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Key Vault](../../technologies/microsoft/azure-key-vault.md), [Customer-managed keys for Fabric workspaces](../../technologies/microsoft/fabric-customer-managed-keys.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | CMEK with Cloud KMS | [Google Cloud Key Management Service](../../technologies/google-cloud/gcp-cloud-kms.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Tri-Secret Secure | [Snowflake Tri-Secret Secure](../../technologies/snowflake/snowflake-tri-secret-secure.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks customer-managed keys](../../technologies/databricks/databricks-customer-managed-keys.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud TDE and customer-managed encryption keys (CMEK)](../../technologies/clickhouse/clickhouse-cmek.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database security features](../../technologies/oracle/oracle-database-security.md) |
