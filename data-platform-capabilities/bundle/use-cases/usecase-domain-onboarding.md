---
type: Use Case
id: usecase-domain-onboarding
title: Self-service domain onboarding
description: Give a new domain or product team a governed workspace, path to live and budget on the shared platform within a day.
requires:
- {capability: self-service-provisioning, level: 3, why: 'Teams create workspaces, environments and pipelines from approved templates without raising tickets.'}
- capability: infrastructure-as-code
  level: 3
  why: Every tenant's resources, grants and settings are created and changed from code, so environments stay identical.
- {capability: multi-tenancy, level: 3, why: 'Each domain needs its own workspace, catalogue area, administrators and budget on shared foundations.'}
- capability: configuration-guardrails
  level: 3
  why: Rules on regions, networking, encryption, compute sizes and tags must hold even for resources created outside the templates.
- capability: environment-promotion
  level: 3
  why: Every team gets the same development, test and production route, with configuration supplied per environment.
- {capability: ci-cd, level: 3, why: A starter pipeline tests and deploys code from the first commit.}
- {capability: version-control, level: 2, why: 'Starter repositories live in the organisation''s Git provider, and production is deployed only from them.'}
- {capability: identity-authentication, level: 3, why: 'Groups and service identities come from the central identity provider, with no local accounts.'}
- {capability: role-based-access, level: 3, why: 'Default roles for the domain are granted to groups, not to individuals.'}
- {capability: network-security, level: 3, why: Private connectivity to sources and to the platform is part of every template.}
- {capability: secrets-management, level: 2, why: 'Pipelines receive credentials from a secrets store, never from code or configuration files.'}
- {capability: cost-attribution, level: 2, why: 'Every resource carries the domain''s tags from creation, so its spend can be reported.'}
- {capability: platform-observability, level: 2, why: 'Each team sees its own job runs, failures and usage from the first day.'}
benefits_from:
- {capability: ephemeral-environments, why: Gives each developer and pull request an isolated environment on realistic data.}
- {capability: test-data-management, why: Provides masked or synthetic data so development environments are useful.}
- {capability: spend-controls, why: Sandbox and development budgets stop forgotten resources running up cost.}
- {capability: runtime-management, why: 'Templates pin supported runtimes and libraries, and upgrades can be rolled out across tenants.'}
- {capability: data-domains, why: 'Ties the new workspace to the business domain, owners and policies it belongs to.'}
- {capability: internal-data-sharing, why: Lets the new team read certified data from other domains without copying it.}
- {capability: audit-logging, why: 'Records what was provisioned, by whom and from which template version.'}
personas:
- persona-platform-engineer
- persona-data-engineer
- persona-analytics-engineer
- persona-data-architect
- persona-security-officer
- persona-finops-practitioner
- persona-data-product-owner
patterns: [data-mesh, lakehouse]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In large organisations the data platform serves dozens of domain and product teams. When each team waits weeks for a workspace, service accounts, network access, CI/CD and a catalogue area, it builds a shadow platform or shares credentials. Self-service onboarding lets a team request its space through a portal, a command or a pull request and receive it from templates: development, test and production environments, a catalogue and schemas named to standard, groups and service identities, secrets, compute with approved sizes, cost tags and a budget, monitoring, and a starter repository whose pipeline already tests and promotes code.

Good looks like a new team running its first pipeline in production within days of asking, with every security, tagging and network rule applied by the templates rather than checked by hand. The platform team spends its time improving templates, rolls improvements out to existing tenants, and can see from telemetry which teams are on which template version and what each one costs.

# Non-functional requirements

- A standard domain workspace with all its environments is ready within one working day of an approved request, and routine requests need no manual step.
- Every provisioned resource passes the platform's security and tagging rules when it is created.
- Template changes reach all existing tenants within an agreed period, such as one quarter.
- Tenants cannot read or write each other's data except through explicit grants or shares.

# Risks

- Templates multiply into variants that the platform team cannot maintain.
- Teams outgrow the templates and fall back to hand-built resources, which drift.
- Isolation is so strict that teams copy data between workspaces instead of sharing it.
- Older tenants stay on outdated template versions with weaker security settings.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Required capabilities

| Capability | Domain | Minimum level | Why |
|---|---|---|---|
| [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Teams create workspaces, environments and pipelines from approved templates without raising tickets. |
| [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Every tenant's resources, grants and settings are created and changed from code, so environments stay identical. |
| [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Each domain needs its own workspace, catalogue area, administrators and budget on shared foundations. |
| [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 3 (Defined) | Rules on regions, networking, encryption, compute sizes and tags must hold even for resources created outside the templates. |
| [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | Every team gets the same development, test and production route, with configuration supplied per environment. |
| [CI/CD](../capabilities/development-lifecycle/ci-cd.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 3 (Defined) | A starter pipeline tests and deploys code from the first commit. |
| [Version control integration](../capabilities/development-lifecycle/version-control.md) | [Development and DataOps](../capabilities/development-lifecycle/development-lifecycle.md) | 2 (Managed) | Starter repositories live in the organisation's Git provider, and production is deployed only from them. |
| [Identity and authentication](../capabilities/security/identity-authentication.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Groups and service identities come from the central identity provider, with no local accounts. |
| [Role-based access control](../capabilities/security/role-based-access.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Default roles for the domain are granted to groups, not to individuals. |
| [Network security](../capabilities/security/network-security.md) | [Security and access](../capabilities/security/security.md) | 3 (Defined) | Private connectivity to sources and to the platform is part of every template. |
| [Secrets management](../capabilities/security/secrets-management.md) | [Security and access](../capabilities/security/security.md) | 2 (Managed) | Pipelines receive credentials from a secrets store, never from code or configuration files. |
| [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Every resource carries the domain's tags from creation, so its spend can be reported. |
| [Platform observability](../capabilities/platform-operations/platform-observability.md) | [Platform operations](../capabilities/platform-operations/platform-operations.md) | 2 (Managed) | Each team sees its own job runs, failures and usage from the first day. |

# Capabilities that help

| Capability | Why |
|---|---|
| [Ephemeral development environments](../capabilities/development-lifecycle/ephemeral-environments.md) | Gives each developer and pull request an isolated environment on realistic data. |
| [Test data management](../capabilities/development-lifecycle/test-data-management.md) | Provides masked or synthetic data so development environments are useful. |
| [Budgets and spend controls](../capabilities/platform-operations/spend-controls.md) | Sandbox and development budgets stop forgotten resources running up cost. |
| [Runtime and environment management](../capabilities/development-lifecycle/runtime-management.md) | Templates pin supported runtimes and libraries, and upgrades can be rolled out across tenants. |
| [Data domains](../capabilities/governance/data-domains.md) | Ties the new workspace to the business domain, owners and policies it belongs to. |
| [Internal data sharing](../capabilities/data-sharing/internal-data-sharing.md) | Lets the new team read certified data from other domains without copying it. |
| [Audit logging](../capabilities/security/audit-logging.md) | Records what was provisioned, by whom and from which template version. |

# Personas

- [Data platform engineer](../personas/persona-platform-engineer.md): Builds and runs the shared data platform and its self-service tooling.
- [Data engineer](../personas/persona-data-engineer.md): Builds and operates the pipelines that ingest, transform and deliver data.
- [Analytics engineer](../personas/persona-analytics-engineer.md): Turns raw data into tested, documented, analysis-ready models.
- [Data architect](../personas/persona-data-architect.md): Designs the data platform and how data flows, is modelled and is governed across the organisation.
- [Security and privacy officer](../personas/persona-security-officer.md): Protects data and makes sure it is used lawfully.
- [FinOps practitioner](../personas/persona-finops-practitioner.md): Tracks, allocates and optimises what the data platform costs.
- [Data product owner](../personas/persona-data-product-owner.md): Owns the value, roadmap and consumers of one or more data products.

# Patterns

- [Data mesh](../patterns/data-mesh.md)
- [Lakehouse](../patterns/lakehouse.md)

# Frameworks that apply

- [Data mesh principles](../frameworks/framework-data-mesh.md): Four principles for decentralising analytical data ownership to business domains while keeping data interoperable and governed.
- [Open Data Product Standard (ODPS)](../frameworks/framework-bitol-odps.md): An open YAML standard for describing a data product, its input and output ports, management interfaces, team and support.

# Platform fit

How many of the required capabilities each platform's technologies in this bundle realise. A capability counts as covered when it or a narrower capability is realised by a technology that is generally available (or whose stage is unconfirmed); preview-only coverage is shown separately, and deprecated products and redistributions of other vendors' platforms are not counted. This is a starting point for a conversation, not a recommendation.

| Platform | Covered | Not covered |
|---|---|---|
| [Amazon Web Services](../platforms/platform-aws.md) | 13 of 13 |  |
| [Microsoft Azure and Fabric](../platforms/platform-microsoft.md) | 13 of 13 |  |
| [Google Cloud](../platforms/platform-google-cloud.md) | 12 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md) |
| [Snowflake](../platforms/platform-snowflake.md) | 12 of 13 | [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md) |
| [Databricks](../platforms/platform-databricks.md) | 12 of 13 | [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md) |
| [ClickHouse](../platforms/platform-clickhouse.md) | 7 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Secrets management](../capabilities/security/secrets-management.md) |
| [Informatica](../platforms/platform-informatica.md) | 5 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md) |
| [Cloudera](../platforms/platform-cloudera.md) | 5 of 13 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md) |
| [Oracle](../platforms/platform-oracle.md) | 1 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Role-based access control](../capabilities/security/role-based-access.md), [Secrets management](../capabilities/security/secrets-management.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Platform observability](../capabilities/platform-operations/platform-observability.md) |
| [SAP](../platforms/platform-sap.md) | 1 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Role-based access control](../capabilities/security/role-based-access.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md), [Platform observability](../capabilities/platform-operations/platform-observability.md) |
| [Teradata](../platforms/platform-teradata.md) | 2 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| [IBM](../platforms/platform-ibm.md) | 3 of 13 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Environment promotion](../capabilities/development-lifecycle/environment-promotion.md), [CI/CD](../capabilities/development-lifecycle/ci-cd.md), [Version control integration](../capabilities/development-lifecycle/version-control.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Role-based access control](../capabilities/security/role-based-access.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| [Palantir](../platforms/platform-palantir.md) | 8 of 13 | [Self-service provisioning](../capabilities/platform-operations/self-service-provisioning.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md) |
| [Open-source ecosystem](../platforms/platform-open-source.md) | 11 of 13 | [Network security](../capabilities/security/network-security.md), [Cost attribution and chargeback](../capabilities/platform-operations/cost-attribution.md) |
| [Independent vendors](../platforms/platform-independent.md) | 6 of 13 | [Infrastructure as code](../capabilities/platform-operations/infrastructure-as-code.md), [Multi-tenancy and workspace isolation](../capabilities/platform-operations/multi-tenancy.md), [Resource configuration guardrails](../capabilities/platform-operations/configuration-guardrails.md), [Identity and authentication](../capabilities/security/identity-authentication.md), [Role-based access control](../capabilities/security/role-based-access.md), [Network security](../capabilities/security/network-security.md), [Secrets management](../capabilities/security/secrets-management.md) |
