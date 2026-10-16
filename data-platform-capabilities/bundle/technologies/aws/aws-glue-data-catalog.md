---
type: Technology
id: aws-glue-data-catalog
title: AWS Glue Data Catalog
description: Central metastore for databases, tables, schemas and partitions that AWS engines and external Iceberg clients use to find and govern data.
aliases: [AWS Glue crawlers]
platform: platform-aws
kind: feature
availability: ga
realises:
- table-catalogue
- metadata-harvesting
- engine-interoperability
- metadata-interoperability
- table-maintenance
- catalogue-federation
- credential-vending
resource: https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exposes an Apache Iceberg REST endpoint plus AWS extensions, and is Hive-metastore compatible. Crawlers infer schemas and partitions from S3 and JDBC sources; column statistics feed cost-based optimisers. Table optimizers compact Iceberg tables in general purpose buckets and can also expire snapshots and remove orphan files. A business context feature (glossary terms, custom metadata and semantic search) is in preview. Permissions are enforced through IAM or Lake Formation.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) (Metadata and discovery): Collect technical metadata automatically from databases, pipelines, BI tools and files.
- [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) (Query and compute): Let several engines read and write the same tables through open formats and shared catalogues.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** AWS Glue

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md), [Snowflake Horizon Iceberg REST Catalog API](../snowflake/snowflake-horizon-iceberg-rest-catalog.md) | [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md), [Databricks catalog federation](../databricks/databricks-catalog-federation.md), [Unity Catalog Iceberg REST Catalog API](../databricks/databricks-iceberg-rest-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Metadata harvesting](../../capabilities/metadata/metadata-harvesting.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Tableflow](../ibm/confluent-tableflow.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Iceberg REST Catalog specification](../open-source/apache-iceberg-rest-catalog-spec.md), [Apache Polaris](../open-source/apache-polaris.md), [Apache Gravitino](../open-source/apache-gravitino.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Multi-engine interoperability](../../capabilities/compute/engine-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
