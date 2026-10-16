---
type: Technology
id: purview-information-protection
title: Microsoft Purview Information Protection
description: Sensitivity labels applied manually or automatically to files, emails and Fabric and Power BI items, with encryption and inheritance downstream.
aliases: [Microsoft Purview sensitivity labels]
formerly: [Microsoft Information Protection]
platform: platform-microsoft
kind: saas
availability: ga
realises: [data-classification, encryption]
resource: https://learn.microsoft.com/en-us/fabric/governance/information-protection
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

In Fabric, labels propagate through lineage and travel with exports to Excel, PDF and PowerPoint. Label-based access control does not apply across tenants or to CSV exports.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** ga  
**Product family:** Microsoft Purview

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Data Classification](../databricks/databricks-data-classification.md), [Databricks governed tags](../databricks/databricks-governed-tags.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md), [Encryption](../../capabilities/security/encryption.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [Microsoft Presidio](../open-source/presidio.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [BigID Next](../independent/bigid-next.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [Encryption](../../capabilities/security/encryption.md) |
