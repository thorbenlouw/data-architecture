---
type: Technology
id: ibm-guardium-data-security-center
title: IBM Guardium Data Security Center
description: Data security suite that discovers and classifies sensitive data, monitors database activity, assesses vulnerabilities, detects risky behaviour and manages cryptography.
aliases: [IBM Guardium]
platform: platform-ibm
kind: saas
availability: ga
realises:
- data-security-posture
- audit-logging
- data-classification
- data-threat-detection
- cryptographic-agility
- ai-system-discovery
resource: https://www.ibm.com/products/guardium-data-security-center
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Combines Guardium Data Protection (activity monitoring), Vulnerability Assessment, DDR and Cryptography Manager, which includes post-quantum readiness. Guardium AI Security extends coverage to AI models and agents.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Data threat detection](../../capabilities/security/data-threat-detection.md) (Security and access): Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.
- [Cryptographic agility](../../capabilities/security/cryptographic-agility.md) (Security and access): Inventory the cryptography protecting data and change algorithms, for example to post-quantum ciphers, without rework.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md), [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trust Center](../snowflake/snowflake-trust-center.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Cyera DSPM](../independent/cyera-dspm.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
