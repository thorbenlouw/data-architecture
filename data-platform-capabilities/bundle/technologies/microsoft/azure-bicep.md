---
type: Technology
id: azure-bicep
title: Bicep
description: A declarative language that compiles to Azure Resource Manager templates for deploying Azure resources as code.
aliases: [Azure Bicep]
platform: platform-microsoft
kind: open-source
availability: ga
realises: [infrastructure-as-code]
resource: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Covers Azure resources, including Fabric capacities, but not Fabric items, for which Terraform, fabric-cicd or the REST APIs are used.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cloud Development Kit](../aws/aws-cdk.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Terraform provider](../snowflake/snowflake-terraform-provider.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [HashiCorp Terraform](../open-source/terraform.md), [OpenTofu](../open-source/opentofu.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
