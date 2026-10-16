---
type: Technology
id: snowflake-open-catalog
title: Snowflake Open Catalog
description: A separate managed Apache Polaris service that acts as an Iceberg REST catalogue with central access control for Iceberg tables shared across engines.
formerly: [Polaris Catalog]
platform: platform-snowflake
kind: managed-service
availability: deprecated
realises: [table-catalogue, engine-interoperability, credential-vending]
resource: https://docs.snowflake.com/en/user-guide/opencatalog/overview
tags: [snowflake]
status: deprecated
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Closed to new customers. Snowflake directs new Iceberg deployments to [Horizon Catalog](snowflake-horizon-catalog.md), and existing customers can keep using Open Catalog. Snowflake set billing on REST API requests to start in the first half of 2026. The open-source project behind it is [Apache Polaris](../open-source/apache-polaris.md).

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** deprecated  
Not counted in platform coverage because it is deprecated.

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md), [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [Confluent Tableflow](../ibm/confluent-tableflow.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Unity Catalog (open source)](../open-source/unity-catalog.md), [Apache Polaris](../open-source/apache-polaris.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
