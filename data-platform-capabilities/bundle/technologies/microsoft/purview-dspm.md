---
type: Technology
id: purview-dspm
title: Microsoft Purview Data Security Posture Management
description: Finds sensitive data and oversharing risks across Microsoft 365, AI apps and agents and connected third-party stores, and recommends DLP, labelling and insider risk policies.
aliases: [Purview DSPM]
formerly: [Microsoft Purview AI Hub, DSPM for AI]
platform: platform-microsoft
kind: saas
availability: ga
realises: [data-security-posture, ai-system-discovery]
resource: https://learn.microsoft.com/en-us/purview/data-security-posture-management-learn-about
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A new unified DSPM replaces DSPM (classic) and DSPM for AI (classic); coverage of Fabric Copilots and data agents is preview, and third-party sources (Snowflake, Databricks, GCP) arrive through connectors and partners. Complements Defender for Cloud DSPM, which focuses on cloud infrastructure.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access) (primary): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [AI system discovery](../../capabilities/governance/ai-system-discovery.md) (Governance and compliance): Find the AI models, agents and services in use, including unapproved ones, to build and maintain the AI inventory.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Security Command Center](../google-cloud/gcp-security-command-center.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Trust Center](../snowflake/snowflake-trust-center.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Governance Hub](../databricks/databricks-governance-hub.md) (preview), [Databricks Data Classification](../databricks/databricks-data-classification.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Securiti DataAI Command Platform](../independent/securiti-dataai-command-platform.md), [Cyera DSPM](../independent/cyera-dspm.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md) | [AI system discovery](../../capabilities/governance/ai-system-discovery.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
