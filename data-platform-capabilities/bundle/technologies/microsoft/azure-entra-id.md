---
type: Technology
id: azure-entra-id
title: Microsoft Entra ID
description: Microsoft's cloud identity service providing single sign-on, conditional access, managed identities, groups and access governance for Azure, Fabric and Microsoft 365.
aliases:
- Entra ID
- Microsoft Entra ID Governance
- Microsoft Entra Privileged Identity Management
- Microsoft Entra Agent ID
formerly: [Azure Active Directory, Azure AD]
platform: platform-microsoft
kind: saas
availability: ga
realises:
- identity-authentication
- role-based-access
- access-requests
- agent-identity
- external-identity
- privileged-access
resource: https://learn.microsoft.com/en-us/entra/fundamentals/whatis
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Entra ID Governance access packages provide time-limited, approved access. Entra Agent ID gives AI agents their own identities.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access) (primary): Authenticate people and services through central identity, single sign-on and short-lived credentials.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.
- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Agent identity and authorisation](../../capabilities/generative-ai/agent-identity.md) (Generative AI): Give each agent its own identity and scoped, short-lived access to data on behalf of named users, enforced at request time.
- [External user and tenant identity](../../capabilities/security/external-identity.md) (Security and access): Manage identities, tenants and permissions for customers and partners who use data products or embedded analytics.
- [Privileged access management](../../capabilities/security/privileged-access.md) (Security and access): Grant administrator, emergency and vendor support access to the platform only when needed, with approval, time limits and a record of what was done.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [AWS Identity and Access Management](../aws/aws-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Privileged access management](../../capabilities/security/privileged-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../snowflake/snowflake-authentication.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks automatic identity management](../databricks/databricks-automatic-identity-management.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md) | [External user and tenant identity](../../capabilities/security/external-identity.md), [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
