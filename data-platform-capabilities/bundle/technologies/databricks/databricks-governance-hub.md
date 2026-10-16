---
type: Technology
id: databricks-governance-hub
title: Databricks Governance Hub
description: An account-level console that brings together data health and governance coverage, tag usage, AI usage and spend, and cost drivers, with recommended actions.
platform: platform-databricks
kind: feature
availability: preview
realises: [data-security-posture, ai-governance, cost-management, governance-metrics]
resource: https://docs.databricks.com/aws/en/admin/governance-hub/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Beta since July 2026, and an account admin must enable it. It processes metadata in a US region, and opting out for residency reasons is permanent.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [AI governance](../../capabilities/governance/ai-governance.md) (Governance and compliance): Inventory AI systems and govern their risk, approval, documentation and use in line with regulation.
- [Cost management](../../capabilities/platform-operations/cost-management.md) (Platform operations): Understand, allocate and control what the platform costs.
- [Governance coverage metrics](../../capabilities/governance/governance-metrics.md) (Governance and compliance): Measure how much of the estate is owned, described, classified, monitored and access-controlled, and track improvement.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** preview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md), [Microsoft Purview Data Security Posture Management](../microsoft/purview-dspm.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trust Center](../snowflake/snowflake-trust-center.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Cyera DSPM](../independent/cyera-dspm.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
