---
type: Technology
id: unity-catalog
title: Unity Catalog (open source)
description: Open-source catalogue for tables, volumes of files, functions and AI models, with an Iceberg REST and Hive Metastore compatible API.
aliases: [Unity Catalog OSS]
platform: platform-open-source
kind: open-source
availability: ga
realises: [table-catalogue, engine-interoperability, access-control, unstructured-data, credential-vending]
resource: https://github.com/unitycatalog/unitycatalog
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, a sandbox project in LF AI & Data, contributed by Databricks in 2024. It has fewer features than the [Databricks Unity Catalog](../databricks/databricks-unity-catalog.md) service (for example lineage, tag-based policies and monitoring are not in the open-source version). Strongest with Delta Lake.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Access control](../../capabilities/security/access-control.md) (Security and access): Decide who can see and change which data, at every level from account down to individual values.
- [Unstructured data management](../../capabilities/specialised-data/unstructured-data.md) (Specialised data types): Store, catalogue, govern and process documents, images, audio and video alongside structured data.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [Confluent Tableflow](../ibm/confluent-tableflow.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
