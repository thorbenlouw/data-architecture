---
type: Technology
id: informatica-administrator
title: IDMC Administrator
description: Organisation-wide administration service for users, groups, roles, SAML single sign-on, licences, runtime environments, connections and sub-organisations.
aliases: [Informatica Administrator]
platform: platform-informatica
kind: feature
availability: ga
realises: [identity-authentication, role-based-access, multi-tenancy, audit-logging]
resource: https://onlinehelp.informatica.com/IICS/prod/mde/en/zz-cloud-helpoverview/Help_for_Other_Services.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Sub-organisations give business units separate assets and IPU tracking under one parent organisation. Multi-factor authentication was added in the Fall 2025 release, and in 2026 audit, user and Secure Agent management were also exposed as MCP servers.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access) (primary): Authenticate people and services through central identity, single sign-on and short-lived credentials.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.
- [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) (Platform operations): Give teams or domains their own isolated workspaces, catalogues and budgets on shared foundations.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [AWS Identity and Access Management](../aws/aws-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace identity](../microsoft/fabric-workspace-identity.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md), [Fabric workspaces](../microsoft/fabric-workspaces.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Multi-tenancy and workspace isolation](../../capabilities/platform-operations/multi-tenancy.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../snowflake/snowflake-authentication.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks automatic identity management](../databricks/databricks-automatic-identity-management.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
