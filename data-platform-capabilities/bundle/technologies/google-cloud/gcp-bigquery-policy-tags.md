---
type: Technology
id: gcp-bigquery-policy-tags
title: BigQuery policy tags
description: Hierarchical taxonomies of tags attached to columns that drive column-level access control and data masking policies.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [attribute-based-access, column-masking, data-classification]
resource: https://docs.cloud.google.com/bigquery/docs/column-level-security-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Taxonomies still live under the Data Catalog API (datacatalog.googleapis.com), which must stay enabled even though Data Catalog search has been replaced by Knowledge Catalog. Data governance tags (Resource Manager tags used for column access and masking, preview July 2026) are an alternative.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access) (primary): Grant or deny access based on attributes of the user and tags on the data.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Lake Formation](../aws/aws-lake-formation.md), [AWS Identity and Access Management](../aws/aws-iam.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md), [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Privacera](../independent/privacera.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md), [Collibra Data Access](../independent/collibra-data-access.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Data classification](../../capabilities/governance/data-classification.md) |
