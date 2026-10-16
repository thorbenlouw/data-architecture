---
type: Technology
id: terraform
title: HashiCorp Terraform
description: Infrastructure-as-code tool that declares infrastructure in HCL and creates, changes and destroys it through providers.
aliases: [Terraform]
platform: platform-open-source
kind: software
availability: ga
realises: [infrastructure-as-code, self-service-provisioning]
resource: https://www.hashicorp.com/en/license-faq
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Licence change. Terraform moved from MPL 2.0 to the Business Source License 1.1 in August 2023 (from version 1.6), so it is no longer open source; internal use is still allowed. HashiCorp has been part of IBM since 2025. OpenTofu is the open-source fork.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) (Platform operations) (primary): Define platform resources, permissions and configuration as code and apply them automatically.
- [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) (Platform operations): Let teams create approved workspaces, pipelines and resources from templates without waiting for a central team.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Cloud Development Kit](../aws/aws-cdk.md), [AWS CloudFormation](../aws/aws-cloudformation.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Bicep](../microsoft/azure-bicep.md), [Terraform Provider for Microsoft Fabric](../microsoft/fabric-terraform-provider.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Infrastructure Manager](../google-cloud/gcp-infrastructure-manager.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Terraform provider](../snowflake/snowflake-terraform-provider.md), [Snowflake DCM Projects](../snowflake/snowflake-dcm-projects.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Terraform provider](../databricks/databricks-terraform-provider.md), [Databricks Declarative Automation Bundles](../databricks/databricks-declarative-automation-bundles.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md), [Self-service provisioning](../../capabilities/platform-operations/self-service-provisioning.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse Terraform provider](../clickhouse/clickhouse-terraform.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Apollo](../palantir/palantir-apollo.md) | [Infrastructure as code](../../capabilities/platform-operations/infrastructure-as-code.md) |
