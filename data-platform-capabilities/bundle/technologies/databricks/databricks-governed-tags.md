---
type: Technology
id: databricks-governed-tags
title: Databricks governed tags
description: Account-level tag definitions with controlled values and assignment permissions, applied to Unity Catalog objects and workspace assets and used by ABAC, classification and cost reporting.
platform: platform-databricks
kind: feature
availability: ga
realises: [data-classification, active-metadata, data-policy-management]
resource: https://docs.databricks.com/aws/en/release-notes/product/2026/april
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Governed tags became GA in April 2026. Tag automations and lineage-based governed tag propagation are in Beta. Tags on dashboards, notebooks, apps and Genie Agents became GA in September 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Active metadata](../../capabilities/metadata/active-metadata.md) (Metadata and discovery): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Intent-Driven Governance](../snowflake/snowflake-intent-driven-governance.md) (preview), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake sensitive data classification](../snowflake/snowflake-sensitive-data-classification.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Active metadata](../../capabilities/metadata/active-metadata.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md), [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [Microsoft Presidio](../open-source/presidio.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Privacera](../independent/privacera.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
