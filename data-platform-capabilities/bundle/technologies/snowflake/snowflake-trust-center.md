---
type: Technology
id: snowflake-trust-center
title: Snowflake Trust Center
description: Runs scanner packages (Security Essentials, CIS Benchmarks, Threat Intelligence, AI Security) against accounts and reports violations, detections and at-risk entities.
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-security-posture, compliance-evidence, audit-logging, data-threat-detection]
resource: https://docs.snowflake.com/en/user-guide/trust-center/overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Account posture PDF reports, programmatic notifications, and the Sensitive Data Access and Entitlement reports are in preview. Sensitive data classification is configured from here.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) (Governance and compliance): Map regulatory requirements to platform controls and produce evidence for auditors.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Data threat detection](../../capabilities/security/data-threat-detection.md) (Security and access): Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [AWS CloudTrail](../aws/aws-cloudtrail.md) | [Data security posture management](../../capabilities/security/data-security-posture.md), [Audit logging](../../capabilities/security/audit-logging.md), [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md), [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Compliance controls and evidence](../../capabilities/governance/compliance-evidence.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview), [Databricks Data Classification](../databricks/databricks-data-classification.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Cyera DSPM](../independent/cyera-dspm.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
