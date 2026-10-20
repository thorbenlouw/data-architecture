---
type: Technology
id: snowflake-object-tagging
title: Snowflake object tagging
description: Schema-level tags with allowed values that are attached to objects and columns, inherited down the hierarchy, and used for classification, cost attribution and tag-based policies.
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-classification, attribute-based-access, cost-attribution, active-metadata]
resource: https://docs.snowflake.com/en/user-guide/object-tagging
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tag-based masking attaches a policy to a tag, so tagged columns are protected as soon as they are tagged. Tags can propagate automatically through lineage. Snowflake-provided tags are in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance) (primary): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Cost attribution and chargeback](../../capabilities/platform-operations/cost-attribution.md) (Platform operations): Attribute spend to teams, products and workloads using tags and usage data.
- [Active metadata](../../capabilities/metadata/active-metadata.md) (Metadata and discovery): Use metadata to trigger actions automatically, such as propagating tags, alerting owners or blocking bad data.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Macie](../aws/aws-macie.md), [Amazon Comprehend](../aws/aws-comprehend.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md), [Microsoft Purview Data Map](../microsoft/purview-data-map.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks governed tags](../databricks/databricks-governed-tags.md), [Databricks Data Classification](../databricks/databricks-data-classification.md) | [Active metadata](../../capabilities/metadata/active-metadata.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Unstructured Data Governance](../informatica/informatica-unstructured-data-governance.md) (preview), [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Catalog](../cloudera/cloudera-data-catalog.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Guardium Data Security Center](../ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Data Governance](../sas/sas-data-governance.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Atlas](../open-source/apache-atlas.md), [Microsoft Presidio](../open-source/presidio.md) | [Data classification](../../capabilities/governance/data-classification.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [BigID Next](../independent/bigid-next.md), [Privacera](../independent/privacera.md), [Cyera DSPM](../independent/cyera-dspm.md) | [Data classification](../../capabilities/governance/data-classification.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) |
