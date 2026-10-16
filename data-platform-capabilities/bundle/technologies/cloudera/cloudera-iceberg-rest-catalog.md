---
type: Technology
id: cloudera-iceberg-rest-catalog
title: Cloudera Iceberg REST Catalog
description: Implementation of the Iceberg REST catalogue API on the Hive Metastore that lets external engines read Cloudera-governed Iceberg tables using short-lived, scoped storage credentials.
aliases: [Cloudera Data Sharing]
platform: platform-cloudera
kind: feature
availability: ga
realises:
- table-catalogue
- engine-interoperability
- metadata-interoperability
- credential-vending
- open-protocol-sharing
resource: https://docs.cloudera.com/runtime/7.3.2/overview/topics/cr-ds-cloudera-iceberg-rest-catalog.html
tags: [cloudera]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Marketed as "Cloudera Data Sharing powered by Iceberg REST Catalog" (October 2025). Authenticates through Knox OAuth tokens and authorises through Ranger; external clients tested include Snowflake, Databricks, Amazon Athena, EMR Spark and Trino. Storage credential vending supports S3 and ADLS Gen2.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.
- [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md) (Data sharing and collaboration): Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.

**Platform:** [Cloudera](../../platforms/platform-cloudera.md)  
**Availability:** ga  
**Product family:** Cloudera Open Data Lakehouse

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md), [SAP Business Data Cloud Connect](../sap/sap-bdc-connect.md) | [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data](../ibm/ibm-watsonx-data.md), [Confluent Tableflow](../ibm/confluent-tableflow.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Open-protocol sharing](../../capabilities/data-sharing/open-protocol-sharing.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Unity Catalog (open source)](../open-source/unity-catalog.md), [Apache Polaris](../open-source/apache-polaris.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
