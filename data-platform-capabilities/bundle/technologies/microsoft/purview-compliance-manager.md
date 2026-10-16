---
type: Technology
id: purview-compliance-manager
title: Microsoft Purview Compliance Manager
description: Maps regulatory requirements to improvement actions and Microsoft controls, and tracks evidence and a compliance score.
platform: platform-microsoft
kind: saas
availability: ga
realises: [compliance-evidence, ai-governance]
resource: https://learn.microsoft.com/en-us/purview/compliance-manager
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Includes assessment templates for AI regulations such as the EU AI Act.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance) (primary): Map regulatory requirements to platform controls and produce evidence for auditors.
- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Config](../aws/aws-config.md), [AWS CloudTrail](../aws/aws-cloudtrail.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Assured Workloads](../google-cloud/gcp-assured-workloads.md), [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks compliance security profile](../databricks/databricks-compliance-security-profile.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [AI governance](../../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md), [Holistic AI Governance Platform](../independent/holistic-ai-governance-platform.md) | [AI governance](../../capabilities/governance/ai-governance.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
