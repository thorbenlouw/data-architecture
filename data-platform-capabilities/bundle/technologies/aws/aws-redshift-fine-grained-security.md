---
type: Technology
id: aws-redshift-fine-grained-security
title: Amazon Redshift row-level security and dynamic data masking
description: Redshift policies that filter rows and mask column values per role at query time, alongside role-based SQL permissions.
platform: platform-aws
kind: feature
availability: ga
realises: [row-level-security, column-masking, role-based-access]
resource: https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Policies attach to roles and apply to direct and data-shared queries. Lake Formation can govern Redshift data shares as an alternative central model.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access) (primary): Restrict which rows each user sees based on who they are.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Redshift

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery row-level security](../google-cloud/gcp-bigquery-row-level-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeguard](../databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Role-based access control](../../capabilities/security/role-based-access.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [PostgreSQL](../open-source/postgresql.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [Row-level security](../../capabilities/security/row-level-security.md) |
