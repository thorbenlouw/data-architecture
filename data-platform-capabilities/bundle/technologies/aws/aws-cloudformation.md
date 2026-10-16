---
type: Technology
id: aws-cloudformation
title: AWS CloudFormation
description: Provisions and updates AWS resources from declarative JSON or YAML templates as versioned stacks.
platform: platform-aws
kind: managed-service
availability: ga
realises: [infrastructure-as-code, environment-promotion]
resource: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

StackSets deploy across accounts and Regions; most data services, including Lake Formation permissions and DataZone resources, have resource types. Terraform is the common alternative.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.
- [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) (Development and DataOps): Promote the same artefacts through development, test and production with environment-specific configuration.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Bicep](../microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../microsoft/fabric-terraform-provider.md), [Fabric variable library](../microsoft/fabric-variable-library.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Terraform provider](../snowflake/snowflake-terraform-provider.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Environment promotion](../../capabilities/development-lifecycle/environment-promotion.md), [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [HashiCorp Terraform](../open-source/terraform.md), [OpenTofu](../open-source/opentofu.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
