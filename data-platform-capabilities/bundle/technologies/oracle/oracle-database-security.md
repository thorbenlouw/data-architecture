---
type: Technology
id: oracle-database-security
title: Oracle Database security features
description: Built-in controls in Oracle AI Database for row-level policies, query-time masking, separation of duties and encryption of data at rest with managed keys.
aliases:
- Virtual Private Database
- VPD
- Oracle Data Redaction
- Oracle Database Vault
- Transparent Data Encryption
- TDE
- Oracle Advanced Security
platform: platform-oracle
kind: feature
availability: ga
realises: [row-level-security, column-masking, encryption, customer-managed-keys]
resource: https://www.oracle.com/security/database-security/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some features need the Advanced Security or Database Vault options on premises but are included in Autonomous AI Database. Keys can be held in OCI Vault or external key managers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access) (primary): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.
- [Customer-managed keys](../../capabilities/security/customer-managed-keys.md) (Security and access): Encrypt platform data with keys you control, so you can rotate or revoke them.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga  
**Product family:** Oracle AI Database

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../aws/aws-lake-formation.md), [AWS Key Management Service](../aws/aws-kms.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery row-level security](../google-cloud/gcp-bigquery-row-level-security.md), [Google Cloud Key Management Service](../google-cloud/gcp-cloud-kms.md) | [Row-level security](../../capabilities/security/row-level-security.md), [Customer-managed keys](../../capabilities/security/customer-managed-keys.md), [Encryption](../../capabilities/security/encryption.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeguard](../databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Encryption](../../capabilities/security/encryption.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [PostgreSQL](../open-source/postgresql.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
