---
type: Capability
id: infrastructure-as-code
title: Infrastructure as code
description: Define platform resources, permissions and configuration as code and apply them automatically.
aliases: [IaC, Terraform]
broader: [platform-operations]
related:
- ci-cd
- self-service-provisioning
- environment-promotion
- schema-change-management
- data-policy-management
depends_on: [version-control, secrets-management]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A declarative tool reads text files that describe the desired resources (accounts, workspaces, storage, clusters and warehouses, network settings, catalogues, schemas, roles, grants and budgets), compares them with what exists, shows a plan of the differences and applies it. Terraform and OpenTofu are common, alongside cloud providers' own template languages, and most data platforms publish providers for them. A change such as "give the finance analyst role read access to the sales schema" becomes a reviewed pull request rather than a console click.

Environments become reproducible, so test matches production and a lost environment can be rebuilt. Every change to permissions and configuration has a reviewed, logged history, which is strong audit evidence. The main design choices are which tool owns which resources, how state is stored and locked, and how to handle drift when someone changes things outside the code. Some teams also manage tables this way; others leave them to schema change or transformation tools, so that two tools never claim the same object.

# Key considerations

- Give each resource exactly one owning tool. Two tools managing the same grants or tables will undo each other's changes.
- Protect state files. They list every managed resource and can contain secrets, so store them encrypted, with locking and limited access.
- Detect drift from console changes and decide whether to revert or import it.
- Split code into modules and keep separate state per environment or domain, so one change cannot plan the destruction of everything.
- Provider coverage varies. Check that every resource you need, including newer features, can be managed as code.

# Questions to ask

- Which platform resources are created by hand today, and could you rebuild them after an incident?
- Who reviews permission changes before they take effect?
- Which tool, if any, does the organisation already use for cloud infrastructure?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Related | [Backup and disaster recovery](business-continuity.md), [CI/CD](../development-lifecycle/ci-cd.md), [CI/CD for machine learning](../mlops/ml-cicd.md), [Compliance controls and evidence](../governance/compliance-evidence.md), [Cross-region replication and failover](cross-region-failover.md), [Data product specification](../data-products/data-product-specification.md), [Environment promotion](../development-lifecycle/environment-promotion.md), [Network security](../security/network-security.md), [Policy management](../governance/data-policy-management.md), [Provisioned compute](../compute/provisioned-compute.md), [Resilience and recovery testing](resilience-testing.md), [Resource configuration guardrails](configuration-guardrails.md), [Role-based access control](../security/role-based-access.md), [Runtime and environment management](../development-lifecycle/runtime-management.md), [Schema change management](../development-lifecycle/schema-change-management.md), [Self-service provisioning](self-service-provisioning.md), [Version control integration](../development-lifecycle/version-control.md) |
| Depends on | [Version control integration](../development-lifecycle/version-control.md), [Secrets management](../security/secrets-management.md) |
| Needed by | [Self-service provisioning](self-service-provisioning.md) |

# Where it appears

- **Use cases:** [Legacy warehouse migration](../../use-cases/usecase-platform-modernisation.md) (benefits from) · [Self-service domain onboarding](../../use-cases/usecase-domain-onboarding.md) (requires, level 3)
- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Platform self-service](../../maturity/track-platform-self-service.md) (from level 2, Managed)
- **Frameworks:** [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve data platform; Self-serve platform – infrastructure provisioning plane

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Cloud Development Kit](../../technologies/aws/aws-cdk.md), [AWS CloudFormation](../../technologies/aws/aws-cloudformation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Bicep](../../technologies/microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../../technologies/microsoft/fabric-terraform-provider.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Infrastructure Manager](../../technologies/google-cloud/gcp-infrastructure-manager.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake DCM Projects](../../technologies/snowflake/snowflake-dcm-projects.md), [Snowflake Terraform provider](../../technologies/snowflake/snowflake-terraform-provider.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Declarative Automation Bundles](../../technologies/databricks/databricks-declarative-automation-bundles.md), [Databricks Terraform provider](../../technologies/databricks/databricks-terraform-provider.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse Terraform provider](../../technologies/clickhouse/clickhouse-terraform.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Apollo](../../technologies/palantir/palantir-apollo.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [HashiCorp Terraform](../../technologies/open-source/terraform.md), [OpenTofu](../../technologies/open-source/opentofu.md) |
