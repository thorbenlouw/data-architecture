---
type: Technology
id: gcp-bigquery-row-level-security
title: BigQuery row-level security
description: Row access policies that filter which rows of a table each user or group can see, using SQL filter expressions and optional lookup subqueries.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [row-level-security]
resource: https://docs.cloud.google.com/bigquery/docs/row-level-security-intro
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Policies also apply to BigLake external tables. Tables with row access policies lose BI Engine and materialised view acceleration, and subquery-based policies cannot be combined with data masking.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Row-level security](../../capabilities/security/row-level-security.md) (Security and access) (primary): Restrict which rows each user sees based on who they are.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Redshift row-level security and dynamic data masking](../aws/aws-redshift-fine-grained-security.md), [AWS Lake Formation](../aws/aws-lake-formation.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [OneLake security](../microsoft/fabric-onelake-security.md), [Power BI semantic models](../microsoft/powerbi-semantic-models.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake row access policies](../snowflake/snowflake-row-access-policies.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeguard](../databricks/databricks-lakeguard.md), [Unity Catalog attribute-based access control (ABAC)](../databricks/databricks-abac.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse access control (users, roles, row policies, masking policies, settings profiles and quotas)](../clickhouse/clickhouse-access-control.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Shared Data Experience (SDX)](../cloudera/cloudera-sdx.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Database security features](../oracle/oracle-database-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere](../sap/sap-datasphere.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Teradata](../../platforms/platform-teradata.md) | [Teradata Database security (roles, row-level security, encryption)](../teradata/teradata-security.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Foundry security controls](../palantir/palantir-security-controls.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Ranger](../open-source/apache-ranger.md), [PostgreSQL](../open-source/postgresql.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Collibra Data Access](../independent/collibra-data-access.md), [Immuta Data Authorization Platform](../independent/immuta-data-authorization-platform.md) | [Row-level security](../../capabilities/security/row-level-security.md) |
