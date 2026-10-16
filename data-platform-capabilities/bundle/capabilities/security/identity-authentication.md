---
type: Capability
id: identity-authentication
title: Identity and authentication
description: Authenticate people and services through central identity, single sign-on and short-lived credentials.
aliases:
- SSO
- SCIM
- service principals
- workload identity federation
- identity propagation
- end-user identity pass-through
- trusted identity propagation
- OAuth to data sources
broader: [security]
related: [agent-identity, secrets-management, credential-vending, role-based-access, audit-logging]
tags: [security]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Authentication proves who is connecting before any permission is checked. For people, the platform delegates sign-in to a central identity provider through single sign-on standards such as SAML or OpenID Connect, which enforce multi-factor authentication and conditions such as device or location. Users and groups are provisioned automatically, often with SCIM, so leavers lose access when they leave the directory. For pipelines, services and agents, workload identity replaces stored passwords: a job exchanges a signed token from its own runtime environment for a short-lived platform token.

Every other control depends on knowing who is acting, and weak authentication is a common way into data platforms: shared accounts, long-lived keys in scripts, passwords without a second factor. Two choices matter most. One is whether tools connect as the end user or through a shared service account; passing the user's identity through keeps fine-grained access and audit meaningful. The other is how machine identities are issued and rotated. Authentication establishes identity; authorisation then decides what that identity may do.

# Key considerations

- Disable local platform accounts and password sign-in, apart from tightly controlled break-glass access.
- Base access decisions on groups from the identity provider, synced automatically so joiners, movers and leavers are handled promptly.
- Replace long-lived keys in pipelines with federated workload identity or short-lived tokens, and inventory any keys that remain.
- Check how BI tools, notebooks and agents authenticate to the data, since many default to a shared service account.

# Questions to ask

- Which identity provider is authoritative, and do all platform tools use it for sign-in?
- How many service accounts and long-lived keys exist, and who owns each?
- Do BI tools and applications pass the end user's identity to the platform?
- How quickly is access removed when someone leaves?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Security and access](security.md) |
| Broader | [Security and access](security.md) |
| Narrower | [External user and tenant identity](external-identity.md) |
| Related | [Access control](access-control.md), [Agent identity and authorisation](../generative-ai/agent-identity.md), [Audit logging](audit-logging.md), [IoT and telemetry ingestion](../ingestion-integration/iot-ingestion.md), [Privileged access management](privileged-access.md), [Role-based access control](role-based-access.md), [Secrets management](secrets-management.md), [SQL and programmatic access](../serving/sql-access.md), [Storage credential vending](../storage/credential-vending.md) |
| Needed by | [Access control](access-control.md), [Agent identity and authorisation](../generative-ai/agent-identity.md), [AI gateway](../generative-ai/ai-gateway.md), [Attribute- and tag-based access control](attribute-based-access.md), [Audit logging](audit-logging.md), [Data APIs](../serving/data-apis.md), [Data application hosting](../development-lifecycle/data-applications.md), [Embedded analytics](../analytics-bi/embedded-analytics.md), [Foundation model access](../generative-ai/foundation-model-access.md), [IDE and local development](../development-lifecycle/local-development.md), [Multi-tenancy and workspace isolation](../platform-operations/multi-tenancy.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Privileged access management](privileged-access.md), [Role-based access control](role-based-access.md), [Row-level security](row-level-security.md), [Storage credential vending](../storage/credential-vending.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (requires, level 3) · [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (requires, level 3) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md) · [Security and privacy officer](../../personas/persona-security-officer.md) · [Software engineer](../../personas/persona-software-engineer.md)
- **Maturity tracks:** [Security and access control](../../maturity/track-security.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 9 – Protection and prevention · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(f) – Integrity and confidentiality

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | IAM roles; IAM Identity Center trusted identity propagation | [AWS IAM Identity Center](../../technologies/aws/aws-iam-identity-center.md), [AWS Identity and Access Management](../../technologies/aws/aws-iam.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric workspace identity](../../technologies/microsoft/fabric-workspace-identity.md), [Microsoft Entra ID](../../technologies/microsoft/azure-entra-id.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Identity and Access Management](../../technologies/google-cloud/gcp-iam.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake authentication (SSO, OAuth, key pair, PATs, workload identity federation)](../../technologies/snowflake/snowflake-authentication.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks automatic identity management](../../technologies/databricks/databricks-automatic-identity-management.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Cloud](../../technologies/clickhouse/clickhouse-cloud.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [IDMC Administrator](../../technologies/informatica/informatica-administrator.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Keycloak](../../technologies/open-source/keycloak.md) |

Narrower capabilities are realised by a further 5 technologies; see their pages.
