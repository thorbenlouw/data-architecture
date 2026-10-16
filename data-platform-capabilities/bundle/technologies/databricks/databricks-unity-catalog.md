---
type: Technology
id: databricks-unity-catalog
title: Unity Catalog
description: The account-wide catalogue and governance layer for tables, volumes, functions, models, AI services and connections. It provides a three-level namespace, SQL privileges, audit and workspace bindings.
aliases: [UC]
platform: platform-databricks
kind: managed-service
availability: ga
realises: [table-catalogue, role-based-access]
resource: https://docs.databricks.com/aws/en/data-governance/unity-catalog/
tags: [databricks]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The open-source project is [Unity Catalog (open source)](../open-source/unity-catalog.md). Newer features include Databricks RBAC role assumption (GA August 2026), the READ METADATA privilege and INSERT, UPDATE and DELETE privileges (Beta). Discovery, policy and audit features built on Unity Catalog include [Catalog Explorer](databricks-catalog-explorer.md), [Discover](databricks-discover.md), [lineage](databricks-unity-catalog-lineage.md), [ABAC](databricks-abac.md), [governed tags](databricks-governed-tags.md), [Data Classification](databricks-data-classification.md), [metric views](databricks-metric-views.md), the [Iceberg REST Catalog API](databricks-iceberg-rest-catalog.md) and audit logs in [system tables](databricks-system-tables.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Role-based access control](../../capabilities/security/role-based-access.md) (Security and access): Grant permissions to roles and assign roles to people and groups.

**Platform:** [Databricks](../../platforms/platform-databricks.md)  
**Availability:** ga  
**Product family:** Unity Catalog

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md), [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake access control (RBAC and database roles)](../snowflake/snowflake-access-control.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Tableflow](../ibm/confluent-tableflow.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Hive Metastore](../open-source/apache-hive-metastore.md), [Apache Polaris](../open-source/apache-polaris.md), [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Role-based access control](../../capabilities/security/role-based-access.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
