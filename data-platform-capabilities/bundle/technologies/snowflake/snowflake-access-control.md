---
type: Technology
id: snowflake-access-control
title: Snowflake access control (RBAC and database roles)
description: A hierarchy of account roles, database roles and application roles that hold privileges on securable objects, with secondary roles and managed access schemas.
aliases: [Snowflake RBAC]
platform: platform-snowflake
kind: feature
availability: ga
realises: [role-based-access]
resource: https://docs.snowflake.com/en/user-guide/security-access-control-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Identity and Access Management](../aws/aws-iam.md), [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspaces](../microsoft/fabric-workspaces.md), [OneLake security](../microsoft/fabric-onelake-security.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
