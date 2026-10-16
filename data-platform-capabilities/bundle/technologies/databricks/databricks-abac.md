---
type: Technology
id: databricks-abac
title: Unity Catalog attribute-based access control (ABAC)
description: Policies attached at catalogue, schema or table level that use governed tags and user attributes to apply row filters, column masks and dynamic grants automatically.
platform: platform-databricks
kind: feature
availability: ga
realises: [attribute-based-access, row-level-security, column-masking, data-policy-management]
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

ABAC became GA in April 2026. Cross-engine ABAC (GA October 2026) lets external engines read protected managed tables, with serverless compute applying the filters. Metastore-level, DENY, identity-attribute and context-attribute policies are in Beta. Hand-written per-table row filters, column masks and dynamic views are still available.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access) (primary): Grant or deny access based on attributes of the user and tags on the data.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Lake Formation](../aws/aws-lake-formation.md), [AWS Identity and Access Management](../aws/aws-iam.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md), [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md), [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md), [Policy management](../../capabilities/governance/data-policy-management.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md), [Collibra Data Access](../independent/collibra-data-access.md), [Privacera](../independent/privacera.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
