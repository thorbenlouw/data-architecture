---
type: Technology
id: cloudera-sdx
title: Cloudera Shared Data Experience (SDX)
description: Common security and governance layer, built on Apache Ranger, Apache Atlas and Apache Knox, applied to every engine on the same data.
platform: platform-cloudera
kind: feature
availability: ga
realises: [attribute-based-access, row-level-security, column-masking, audit-logging, role-based-access]
resource: https://docs.cloudera.com/
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

[Apache Ranger](../open-source/apache-ranger.md) provides resource- and tag-based policies, row filters and masking; [Apache Atlas](../open-source/apache-atlas.md) holds metadata, classifications and table and column lineage inside the platform; Apache Knox handles gateway authentication and token exchange. Policies defined once apply to Hive, Impala, Spark, Trino, Kafka and NiFi.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access) (primary): Grant or deny access based on attributes of the user and tags on the data.
- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Audit logging](../../capabilities/security/audit-logging.md) (Security and access): Record who accessed or changed what, when and from where, and keep the records tamper-evident.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Shared Data Experience

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Lake Formation](../aws/aws-lake-formation.md), [AWS Identity and Access Management](../aws/aws-iam.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md), [Google Cloud Identity and Access Management](../google-cloud/gcp-iam.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md), [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake object tagging](../snowflake/snowflake-object-tagging.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Audit logging](../../capabilities/security/audit-logging.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Audit logging](../../capabilities/security/audit-logging.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [Open Policy Agent (OPA)](../open-source/open-policy-agent.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Audit logging](../../capabilities/security/audit-logging.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md), [Privacera](../independent/privacera.md), [Collibra Data Access](../independent/collibra-data-access.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md), [Audit logging](../../capabilities/security/audit-logging.md) |
