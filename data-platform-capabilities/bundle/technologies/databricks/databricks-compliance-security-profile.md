---
type: Technology
id: databricks-compliance-security-profile
title: Databricks compliance security profile
description: A workspace setting that applies a hardened, FIPS-validated compute image, enhanced security monitoring and encrypted egress, required for HIPAA, PCI-DSS, FedRAMP and similar regulated data.
platform: platform-databricks
kind: feature
availability: ga
realises: [compliance-evidence, data-residency, configuration-guardrails]
resource: https://docs.databricks.com/aws/en/security/privacy/security-profile
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

It is part of the paid Enhanced Security and Compliance add-on. Some newer features arrive later on these workspaces, and account-level Genie One does not aggregate their data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance) (primary): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Data residency and sovereignty](../../capabilities/governance/data-residency.md) (Governance and compliance): Keep data and its processing in approved jurisdictions and prove that you have.
- [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) (Platform operations): Restrict which platform resources can be created and how they are configured, such as allowed sizes, regions, tags and network settings, and report anything that breaks the rules.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Config](../aws/aws-config.md), [AWS CloudTrail](../aws/aws-cloudtrail.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Policy](../microsoft/azure-policy.md), [Microsoft Purview Compliance Manager](../microsoft/purview-compliance-manager.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Assured Workloads](../google-cloud/gcp-assured-workloads.md), [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Resource Manager](../google-cloud/gcp-resource-manager.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md), [Resource configuration guardrails](../../capabilities/platform-operations/configuration-guardrails.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Virtual Private Snowflake (VPS)](../snowflake/snowflake-virtual-private-snowflake.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.governance](../ibm/ibm-watsonx-governance.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Solidatus](../independent/solidatus.md), [Collibra AI Command Center](../independent/collibra-ai-command-center.md) (unconfirmed), [Credo AI Governance Platform](../independent/credo-ai-governance-platform.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
