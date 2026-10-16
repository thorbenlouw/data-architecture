---
type: Capability
id: self-service-provisioning
title: Self-service provisioning
description: Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.
aliases: [golden paths, internal developer platform]
broader: [platform-operations]
related: [multi-tenancy, spend-controls, access-requests, ci-cd, environment-promotion]
depends_on: [infrastructure-as-code]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Teams request standard resources, such as a domain workspace, a project with development, test and production environments, an ingestion pipeline or a sandbox, through a portal, a command-line tool or a pull request. An automated workflow then creates them from an approved template. The template sets the naming, networking, encryption, default permissions, cost tags, budgets and monitoring the central team requires, so every new resource starts compliant. Requests within agreed limits are approved automatically; only exceptions go to a person.

Without it, the central platform team becomes a queue: each new project waits days for tickets to be worked by hand, and the results differ. With it, teams move faster and the platform team spends its time improving templates rather than fulfilling requests. The templates are often called golden paths, and the portal is often part of an internal developer platform. Self-service provisioning is built on infrastructure as code and adds the catalogue of approved options, the request interface and the guard rails around them.

# Key considerations

- Offer a small set of well-maintained templates. Many variants become as hard to support as hand-built resources.
- Roll template changes out to resources already created from them, or older tenants fall behind on security and cost settings.
- Build in the end of life: expiry dates for sandboxes and a route to decommission projects, or unused resources pile up.
- Record what was provisioned, by whom and from which template version, so audit and cost questions can be answered.

# Questions to ask

- How long does it take today for a team to get a new workspace or project ready to use?
- Which requests are routine enough to automate, and which genuinely need review?
- Who maintains the templates, and how are improvements applied to existing tenants?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md) |
| Related | [Access requests and reviews](../security/access-requests.md), [Budgets and spend controls](spend-controls.md), [CI/CD](../development-lifecycle/ci-cd.md), [Data product specification](../data-products/data-product-specification.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Ephemeral development environments](../development-lifecycle/ephemeral-environments.md), [Infrastructure as code](infrastructure-as-code.md), [Multi-tenancy and workspace isolation](multi-tenancy.md), [Resource configuration guardrails](configuration-guardrails.md) |
| Depends on | [Infrastructure as code](infrastructure-as-code.md) |

# Where it appears

- **Use cases:** [Platform cost management and chargeback](../../use-cases/usecase-platform-cost-management.md) (benefits from) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Patterns:** [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 3, Defined)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve data platform; Self-serve platform – infrastructure provisioning plane

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Unified Studio project profiles | [Amazon SageMaker Unified Studio](../../technologies/aws/aws-sagemaker-unified-studio.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake organisations](../../technologies/snowflake/snowflake-organizations.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Terraform provider](../../technologies/databricks/databricks-terraform-provider.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Anywhere Cloud](../../technologies/cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Data Services on premises](../../technologies/cloudera/cloudera-data-services-on-premises.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Software Hub (Cloud Pak for Data)](../../technologies/ibm/ibm-software-hub.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [HashiCorp Terraform](../../technologies/open-source/terraform.md), [OpenTofu](../../technologies/open-source/opentofu.md) |

Narrower capabilities are realised by a further 4 technologies; see their pages.
