---
type: Technology
id: palantir-sensitive-data-scanner-cipher
title: Palantir Sensitive Data Scanner and Cipher
description: Tools that scan Foundry datasets for sensitive data such as personal identifiers, and that encrypt, hash or obscure columns with managed keys and algorithms.
platform: platform-palantir
kind: feature
availability: ga
realises: [data-classification, deidentification, encryption]
resource: https://www.palantir.com/docs/foundry/getting-started/application-reference/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Scanner results can apply Markings automatically. Cipher supports reversible encryption for authorised users and visual obfuscation in applications.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Comprehend](../aws/aws-comprehend.md), [Amazon Macie](../aws/aws-macie.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Data classification](../../capabilities/governance/data-classification.md), [Encryption](../../capabilities/security/encryption.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md), [Apache Atlas](../open-source/apache-atlas.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [BigID Next](../independent/bigid-next.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md), [Encryption](../../capabilities/security/encryption.md) |
