---
type: Technology
id: collibra-data-access
title: Collibra Data Access
description: Manages access requests, masking, row filtering and role-based grants centrally and provisions them into Snowflake, Databricks and BigQuery.
platform: platform-independent
vendor: Collibra
kind: saas
availability: ga
realises:
- access-requests
- attribute-based-access
- column-masking
- row-level-security
- data-policy-management
resource: https://www.collibra.com/products/data-access
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Collibra bought Raito (data access governance) in June 2025 to strengthen this area. Policies can be driven by classifications such as PII and PHI. It uses Okta or Microsoft Entra ID groups and keeps an audit log of provisioning. Check how far enforcement goes on each target platform.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Access requests and reviews](../../capabilities/security/access-requests.md) (Security and access) (primary): Let people request access to data, have owners approve and time-limit it, and review existing access on a regular cycle.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Access requests and reviews](../../capabilities/security/access-requests.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Data products in Microsoft Purview Unified Catalog](../microsoft/purview-data-products.md), [Microsoft Entra ID](../microsoft/azure-entra-id.md) | [Access requests and reviews](../../capabilities/security/access-requests.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog data products](../google-cloud/gcp-knowledge-catalog-data-products.md) | [Access requests and reviews](../../capabilities/security/access-requests.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Internal Marketplace (organisational listings)](../snowflake/snowflake-internal-marketplace.md), [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Marketplace (CDMP)](../informatica/informatica-cloud-data-marketplace.md), [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Access requests and reviews](../../capabilities/security/access-requests.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM Data Product Hub](../ibm/ibm-data-product-hub.md) | [Access requests and reviews](../../capabilities/security/access-requests.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
