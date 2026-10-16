---
type: Technology
id: teradata-security
title: Teradata Database security (roles, row-level security, encryption)
description: Built-in database controls for role-based privileges, row-level security constraints, column masking through views and functions, access logging and encryption.
platform: platform-teradata
kind: feature
availability: ga
realises: [role-based-access, row-level-security, audit-logging, encryption]
resource: https://www.teradata.com/platform
tags: [teradata]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Row-level security uses security constraint columns, often used in government and defence. Teradata Cloud adds network isolation and customer-managed key options; the Trust and Security Center documents certifications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.

**Platform:** [Teradata](../../platforms/platform-teradata.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Identity and Access Management](../aws/aws-iam.md), [AWS IAM Identity Center](../aws/aws-iam-identity-center.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Fabric workspaces](../microsoft/fabric-workspaces.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
