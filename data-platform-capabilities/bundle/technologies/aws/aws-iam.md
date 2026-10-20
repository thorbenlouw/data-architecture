---
type: Technology
id: aws-iam
title: AWS Identity and Access Management
description: Account-wide service that authenticates principals with short-lived role credentials and authorises every AWS API call through JSON policies.
aliases: [IAM]
platform: platform-aws
kind: managed-service
availability: ga
realises: [role-based-access, attribute-based-access, identity-authentication]
resource: https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tag-based ABAC conditions, service control and resource control policies in AWS Organizations, and permissions boundaries are the foundations that Lake Formation and service-specific grants build on.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access): Authenticate people and services through central identity, single sign-on and short-lived credentials.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Entra ID](../microsoft/azure-entra-id.md), [Fabric workspaces](../microsoft/fabric-workspaces.md), [OneLake security](../microsoft/fabric-onelake-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
