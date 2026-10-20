---
type: Technology
id: sas-viya-security
title: SAS Viya security controls
description: Authentication through SAS Logon with OpenID Connect, SAML or LDAP, rule-based permissions on folders, reports and services, row-level permissions on CAS tables, and audit records of user activity.
aliases: [SAS Logon, SAS Viya authorization]
platform: platform-sas
kind: feature
availability: ga
realises: [role-based-access, row-level-security, identity-authentication, audit-logging]
resource: https://go.documentation.sas.com/doc/en/sasadmincdc/default/calauthzgen/titlepage.htm
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

General authorisation rules govern Viya services and content; CAS has its own access controls on caslibs, tables and rows. Network traffic to and between services is protected with TLS.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access): Authenticate people and services through central identity, single sign-on and short-lived credentials.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Identity and Access Management](../aws/aws-iam.md), [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md), [Fabric workspaces](../microsoft/fabric-workspaces.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md), [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
