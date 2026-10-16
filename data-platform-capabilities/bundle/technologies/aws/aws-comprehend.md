---
type: Technology
id: aws-comprehend
title: Amazon Comprehend
description: Natural language processing API that detects entities, key phrases, sentiment, language and personal data in text, with custom classifiers.
platform: platform-aws
kind: managed-service
availability: ga
realises: [data-classification, deidentification, unstructured-data]
resource: https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

PII detection and redaction are common in data pipelines. Topic modelling, event detection and prompt safety classification have been closed to new customers since March 2026; LLMs on Bedrock now cover many of its tasks.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md), [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md), [Apache Atlas](../open-source/apache-atlas.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [BigID Next](../independent/bigid-next.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
