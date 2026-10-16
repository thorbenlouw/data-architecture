---
type: Technology
id: snowflake-terraform-provider
title: Snowflake Terraform provider
description: A Terraform provider for managing Snowflake accounts, warehouses, databases, roles, grants and policies as code.
platform: platform-snowflake
kind: open-source
availability: ga
realises: [infrastructure-as-code]
resource: https://docs.snowflake.com/en/user-guide/terraform
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Officially supported by Snowflake from version 2.0, and only for the latest version. Resources marked preview are not supported.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cloud Development Kit](../aws/aws-cdk.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Bicep](../microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../microsoft/fabric-terraform-provider.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [HashiCorp Terraform](../open-source/terraform.md), [OpenTofu](../open-source/opentofu.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
