---
type: Technology
id: clickhouse-terraform
title: ClickHouse Terraform provider
description: Official Terraform provider for ClickHouse Cloud services, scaling, private endpoints, organisation roles and API keys, ClickPipes, ClickStack resources and Managed Postgres.
platform: platform-clickhouse
kind: open-source
availability: ga
realises: [infrastructure-as-code, environment-promotion]
resource: https://github.com/ClickHouse/terraform-provider-clickhouse
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Database users, roles and grants are handled by the separate clickhousedbops provider. Managed Postgres support was alpha in mid-2026. A clickhousectl CLI entered public beta in April 2026 and an official Kubernetes operator exists for self-managed clusters.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS CloudFormation](../aws/aws-cloudformation.md), [AWS Cloud Development Kit](../aws/aws-cdk.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Bicep](../microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../microsoft/fabric-terraform-provider.md), [Fabric variable library](../microsoft/fabric-variable-library.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Terraform provider](../snowflake/snowflake-terraform-provider.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [HashiCorp Terraform](../open-source/terraform.md), [OpenTofu](../open-source/opentofu.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
