---
type: Technology
id: oracle-data-safe
title: Oracle Data Safe
description: Security service for Oracle databases that assesses configuration and users, discovers and masks sensitive data, collects audit records and manages SQL Firewall.
platform: platform-oracle
kind: managed-service
availability: ga
realises:
- data-security-posture
- data-classification
- audit-logging
- deidentification
- test-data-management
- data-threat-detection
resource: https://www.oracle.com/security/database-security/data-safe/features/
tags: [oracle]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Works with Autonomous AI Database, Exadata, Base Database Service and on-premises Oracle databases. Masking produces safe non-production copies; sensitive-data discovery has over 150 predefined types.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Test data management](../../capabilities/development-lifecycle/test-data-management.md) (Development and DataOps): Provide realistic, safe data for development and testing through subsetting, masking or generation.
- [Data threat detection](../../capabilities/security/data-threat-detection.md) (Security and access): Analyse data access behaviour to detect and respond to insider threats, ransomware and abnormal access.

**Platform:** [Oracle](../../platforms/platform-oracle.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md), [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md), [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trust Center](../snowflake/snowflake-trust-center.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Cyera DSPM](../independent/cyera-dspm.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [Data threat detection](../../capabilities/security/data-threat-detection.md) |
