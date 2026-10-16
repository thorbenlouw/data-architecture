---
type: Technology
id: aws-config
title: AWS Config
description: Records resource configurations over time and evaluates them against managed or custom rules and conformance packs.
platform: platform-aws
kind: managed-service
availability: ga
realises: [compliance-evidence, configuration-guardrails]
resource: https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Conformance packs map rules to frameworks such as CIS. AWS Audit Manager, which compiled evidence for auditors, has been closed to new customers since March 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance) (primary): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) (Platform operations): Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Policy](../microsoft/azure-policy.md), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Assured Workloads](../google-cloud/gcp-assured-workloads.md), [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks compliance security profile](../databricks/databricks-compliance-security-profile.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Solidatus](../independent/solidatus.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
