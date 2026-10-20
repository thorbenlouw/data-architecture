---
type: Technology
id: clickhouse-access-control
title: ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)
description: SQL-managed access entities that grant privileges to roles, filter rows per user, mask column values per user, and cap settings and resource use per user or role.
platform: platform-clickhouse
kind: feature
availability: ga
realises: [role-based-access, row-level-security, column-masking, workload-management, spend-controls]
resource: https://clickhouse.com/docs/operations/access-rights
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Row policies only protect data for users with read-only access. Masking policies are documented as available in ClickHouse Cloud, ClickHouse Private and BYOC, not the open-source build. External authentication (LDAP, Kerberos, certificates) is supported for self-managed servers. Cloud console access (organisation roles, SAML SSO, MFA) is a separate layer, and database grants can be managed with the clickhousedbops Terraform provider.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Workload management](../../capabilities/compute/workload-management.md) (Query and compute): Prioritise, queue and limit queries and jobs so the most important work meets its service levels.
- [Budgets and spend controls](../../capabilities/platform-operations/spend-controls.md) (Platform operations): Set budgets, quotas and alerts, and stop runaway spend automatically.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Identity and Access Management](../aws/aws-iam.md), [AWS IAM Identity Center](../aws/aws-iam-identity-center.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Fabric workspaces](../microsoft/fabric-workspaces.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
