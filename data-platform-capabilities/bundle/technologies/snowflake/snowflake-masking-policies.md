---
type: Technology
id: snowflake-masking-policies
title: Snowflake masking policies
description: Schema-level policies that mask, tokenise or reveal column values at query time depending on role, other context or tags, including external tokenisation through external functions.
platform: platform-snowflake
kind: feature
availability: ga
realises: [column-masking, attribute-based-access, deidentification]
resource: https://docs.snowflake.com/en/user-guide/security-column-ddm-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition. Policies are enforced for every engine that goes through Snowflake, including the Horizon Iceberg REST path, where protected tables are not given direct file access.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access) (primary): Hide or mask sensitive columns depending on who is querying.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Lake Formation](../aws/aws-lake-formation.md), [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data masking](../google-cloud/gcp-bigquery-data-masking.md), [BigQuery policy tags](../google-cloud/gcp-bigquery-policy-tags.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md), [Lakeguard](../databricks/databricks-lakeguard.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md), [Collibra Data Access](../independent/collibra-data-access.md), [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) |
