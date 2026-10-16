---
type: Technology
id: azure-defender-for-cloud-dspm
title: Data security posture management in Microsoft Defender for Cloud
description: Discovers sensitive data in cloud storage and databases across Azure, AWS and GCP by sampling, and shows attack paths and exposures that put it at risk.
aliases: [Defender CSPM]
platform: platform-microsoft
kind: feature
availability: ga
realises: [data-security-posture]
resource: https://learn.microsoft.com/en-us/azure/defender-for-cloud/concept-data-security-posture
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of Defender CSPM and Defender for Storage plans, using Purview sensitive information types and labels. Infrastructure-centred, whereas Purview DSPM is user- and content-centred.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake Trust Center](../snowflake/snowflake-trust-center.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Cyera DSPM](../independent/cyera-dspm.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md), [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
