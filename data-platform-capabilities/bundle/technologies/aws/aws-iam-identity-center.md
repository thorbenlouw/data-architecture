---
type: Technology
id: aws-iam-identity-center
title: AWS IAM Identity Center
description: Workforce single sign-on that federates an external identity provider and propagates the user's identity to data services for per-user authorisation and auditing.
formerly: [AWS Single Sign-On, AWS SSO]
platform: platform-aws
kind: managed-service
availability: ga
realises: [identity-authentication, role-based-access]
resource: https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Trusted identity propagation passes user identity from Quick, Unified Studio, Athena, Redshift, EMR and S3 Access Grants down to Lake Formation, so CloudTrail shows the end user rather than a shared role.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access) (primary): Authenticate people and services through central identity, single sign-on and short-lived credentials.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric workspace identity](../microsoft/fabric-workspace-identity.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../snowflake/snowflake-authentication.md), [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks automatic identity management](../databricks/databricks-automatic-identity-management.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Cloud](../clickhouse/clickhouse-cloud.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
