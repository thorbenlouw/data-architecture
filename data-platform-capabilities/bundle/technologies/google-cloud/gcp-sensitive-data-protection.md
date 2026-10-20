---
type: Technology
id: gcp-sensitive-data-protection
title: Google Cloud Sensitive Data Protection
description: Discovers, classifies and de-identifies sensitive data across BigQuery, Cloud SQL, Cloud Storage and arbitrary content, and measures re-identification risk.
aliases: [DLP API]
formerly: [Cloud Data Loss Prevention, Cloud DLP]
platform: platform-google-cloud
kind: managed-service
availability: ga
realises: [data-classification, deidentification, data-security-posture, privacy-enhancing-technologies]
resource: https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The discovery service builds organisation-wide data profiles and publishes findings to Security Command Center and as Knowledge Catalog aspects. De-identification supports masking, bucketing, date shifting, tokenisation and format-preserving encryption. The API is still called the DLP API, and Model Armor uses it for sensitive-data screening.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Data security posture management](../../capabilities/security/data-security-posture.md) (Security and access): Find continuously where sensitive data lives, who can reach it and which configurations put it at risk.
- [Privacy-enhancing technologies](../../capabilities/governance/privacy-enhancing-technologies.md) (Governance and compliance): Analyse data while limiting what is revealed, using techniques such as differential privacy, aggregation thresholds and secure computation.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md), [Apache Atlas](../open-source/apache-atlas.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Cyera DSPM](../independent/cyera-dspm.md), [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md) | [Data classification](../../capabilities/governance/data-classification.md), [Data security posture management](../../capabilities/security/data-security-posture.md), [De-identification](../../capabilities/governance/deidentification.md) |
