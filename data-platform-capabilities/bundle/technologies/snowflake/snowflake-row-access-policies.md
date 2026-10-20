---
type: Technology
id: snowflake-row-access-policies
title: Snowflake row access policies
description: Schema-level policies that decide, using the querying role and mapping tables, which rows of a table or view a query returns.
platform: platform-snowflake
kind: feature
availability: ga
realises: [row-level-security, attribute-based-access]
resource: https://docs.snowflake.com/en/user-guide/security-row-intro
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Requires Enterprise Edition.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access) (primary): Restrict which rows each user sees based on who they are.
- [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) (Security and access): Grant or deny access based on attributes of the user and tags on the data.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga  
**Product family:** Snowflake Horizon Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../aws/aws-lake-formation.md) | [Row-level security](../../capabilities/security/row-level-security.md), [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery row-level security](../google-cloud/gcp-bigquery-row-level-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md), [Lakeguard](../databricks/databricks-lakeguard.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAS](../../platforms/platform-sas.md) | [SAS Viya security controls](../sas/sas-viya-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [PostgreSQL](../open-source/postgresql.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Attribute- and tag-based access control](../../capabilities/security/attribute-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
