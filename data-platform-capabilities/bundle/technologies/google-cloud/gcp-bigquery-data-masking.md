---
type: Technology
id: gcp-bigquery-data-masking
title: BigQuery data masking
description: Masks column values at query time according to data policies, using rules such as hashing, nullifying, partial masking or custom masking routines.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [column-masking, deidentification]
resource: https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data policies attach to policy tags or, more recently, directly to columns; the Masked Reader role sees masked values and Fine-Grained Reader sees clear values. Masking applies across BigQuery and Lakehouse tables.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access) (primary): Hide or mask sensitive columns depending on who is querying.
- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../aws/aws-lake-formation.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Azure AI Language PII detection](../microsoft/azure-ai-language-pii.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake projection policies](../snowflake/snowflake-projection-policies.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeguard](../databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Skyflow Data Privacy Vault](../independent/skyflow-data-privacy-vault.md), [Protegrity Data Security Platform](../independent/protegrity-data-security-platform.md), [Collibra Data Access](../independent/collibra-data-access.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md) |
