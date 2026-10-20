---
type: Capability
id: role-based-access
title: Role-based access control
description: Grant permissions to roles and assign roles to people and groups.
aliases: [RBAC]
broader: [access-control]
related: [attribute-based-access, identity-authentication, infrastructure-as-code, access-requests]
depends_on: [identity-authentication]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Permissions such as reading a schema or creating tables are granted to roles, and roles are granted to users and groups. A common design has functional roles such as `finance_analyst` or `marketing_engineer` that bundle access roles for particular schemas or data products, which in turn hold the actual object grants. Many platforms let roles inherit from other roles, so a senior role includes everything a junior one has.

Role-based access control (RBAC) is supported by almost every database and tool and is easy to reason about with a modest number of datasets and teams. Its limits show at scale: every new combination of data and audience needs another role, and organisations end up with thousands of roles nobody can review. Attribute-based access control addresses that by deciding from tags and user attributes instead. Most platforms combine the two: roles for broad entitlements such as workspace and schema access, and attributes and tags for sensitive data within them.

# Key considerations

- Separate access roles, which hold object grants, from functional roles, which match job functions. Grants stay manageable as teams change.
- Map roles to identity-provider groups so membership is managed where joiners and leavers are handled.
- Define roles and grants as infrastructure as code and review changes, rather than granting by hand in a console.
- Watch for role explosion. If roles multiply for every dataset and region, move those distinctions into attribute-based policies.

# Questions to ask

- How many roles exist today, and can anyone explain what each grants?
- Are role memberships driven by identity-provider groups?
- How are roles and grants changed, reviewed and audited?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Access control](access-control.md) |
| Related | [Access requests and reviews](access-requests.md), [Attribute- and tag-based access control](attribute-based-access.md), [Identity and authentication](identity-authentication.md), [Infrastructure as code](../platform-operations/infrastructure-as-code.md) |
| Depends on | [Identity and authentication](identity-authentication.md) |
| Needed by | [Access requests and reviews](access-requests.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 11 – Distribution · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 7 Entitlements and Access for Sensitive Data (Accessibility and usage) · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Roles

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift row-level security and dynamic data masking](../../technologies/aws/aws-redshift-fine-grained-security.md), [AWS IAM Identity Center](../../technologies/aws/aws-iam-identity-center.md), [AWS Identity and Access Management](../../technologies/aws/aws-iam.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric workspaces](../../technologies/microsoft/fabric-workspaces.md), [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md), [OneLake security](../../technologies/microsoft/fabric-onelake-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Identity and Access Management](../../technologies/google-cloud/gcp-iam.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake access control (RBAC and database roles)](../../technologies/snowflake/snowflake-access-control.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog](../../technologies/databricks/databricks-unity-catalog.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../../technologies/clickhouse/clickhouse-access-control.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [IDMC Administrator](../../technologies/informatica/informatica-administrator.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Shared Data Experience (SDX)](../../technologies/cloudera/cloudera-sdx.md) |
| [Teradata](../../platforms/platform-teradata.md) |  | [Teradata Database security (roles, row-level security, encryption)](../../technologies/teradata/teradata-security.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Foundry security controls](../../technologies/palantir/palantir-security-controls.md) |
| [SAS](../../platforms/platform-sas.md) | General authorization rules | [SAS Viya security controls](../../technologies/sas/sas-viya-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Polaris](../../technologies/open-source/apache-polaris.md), [Keycloak](../../technologies/open-source/keycloak.md) |
