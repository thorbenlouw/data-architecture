---
type: Technology
id: gcp-security-command-center
title: Google Cloud Security Command Center
description: Security and risk management service that finds misconfigurations, vulnerabilities and threats across Google Cloud, including where sensitive data is exposed.
aliases: [SCC]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [data-security-posture, compliance-evidence, data-threat-detection, ai-system-discovery]
resource: https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Combines Sensitive Data Protection discovery findings with IAM and network posture, and includes AI-specific findings for agents and models.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Data threat detection](../../capabilities/security/data-threat-detection.md) (Security and access): Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md), [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trust Center](../snowflake/snowflake-trust-center.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview), [Databricks Data Classification](../databricks/databricks-data-classification.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md), [AI system discovery](../../capabilities/governance/ai-system-discovery.md) |
