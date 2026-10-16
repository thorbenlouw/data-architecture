---
type: Technology
id: gcp-iam
title: Google Cloud Identity and Access Management
description: Grants roles to users, groups and service accounts on organisation, folder, project and resource levels, with conditions, deny policies and identity federation.
aliases: [Google Cloud IAM, Privileged Access Manager]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [role-based-access, identity-authentication, attribute-based-access, privileged-access]
resource: https://docs.cloud.google.com/iam/docs/overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

IAM Conditions and Resource Manager tags support attribute-based grants; deny policies and principal access boundaries restrict access. Workforce and Workload Identity Federation remove long-lived keys.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access) (primary): Grant permissions to roles and assign roles to people and groups.
- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access): Authenticate people and services through central identity, single sign-on and short-lived credentials.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Privileged access management](../../capabilities/security/privileged-access.md) (Security and access): Grant administrator, emergency and vendor support access to the platform only when needed, with approval, time limits and a record of what was done.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Identity and Access Management](../aws/aws-iam.md), [AWS IAM Identity Center](../aws/aws-iam-identity-center.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Entra ID](../microsoft/azure-entra-id.md), [Fabric workspaces](../microsoft/fabric-workspaces.md), [OneLake security](../microsoft/fabric-onelake-security.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Privileged access management](../../capabilities/security/privileged-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC Administrator](../informatica/informatica-administrator.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Keycloak](../open-source/keycloak.md), [Apache Polaris](../open-source/apache-polaris.md) | [Identity and authentication](../../capabilities/security/identity-authentication.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
