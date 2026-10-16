---
type: Technology
id: aws-cdk
title: AWS Cloud Development Kit
description: Open-source framework for defining AWS infrastructure in TypeScript, Python, Java, C# or Go that synthesises CloudFormation templates.
aliases: [AWS CDK, CDK]
platform: platform-aws
kind: open-source
availability: ga
realises: [infrastructure-as-code]
resource: https://docs.aws.amazon.com/cdk/v2/guide/home.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Higher-level constructs package common patterns; AgentCore constructs became stable in aws-cdk-lib in May 2026. Apache 2.0 licence.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Bicep](../microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../microsoft/fabric-terraform-provider.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Terraform provider](../snowflake/snowflake-terraform-provider.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [HashiCorp Terraform](../open-source/terraform.md), [OpenTofu](../open-source/opentofu.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
