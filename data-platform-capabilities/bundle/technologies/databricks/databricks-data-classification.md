---
type: Technology
id: databricks-data-classification
title: Databricks Data Classification
description: A serverless agent that scans Unity Catalog tables incrementally, detects sensitive data such as PII and payment-card data, and tags the columns.
platform: platform-databricks
kind: feature
availability: ga
realises: [data-classification, data-security-posture]
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data Classification became GA in April 2026. Results go to a system table and can drive ABAC masking. Scanning views and detection exclusions are in Beta. Scans bill as serverless usage.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md), [Data security posture management in Microsoft Defender for Cloud](../microsoft/azure-defender-for-cloud-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [Microsoft Presidio](../open-source/presidio.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Cyera DSPM](../independent/cyera-dspm.md), [Varonis Data Security Platform](../independent/varonis-data-security-platform.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
