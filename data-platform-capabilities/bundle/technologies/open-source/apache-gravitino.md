---
type: Technology
id: apache-gravitino
title: Apache Gravitino
description: Federated metadata catalogue that manages tables, filesets, message topics and models across many sources, with an Iceberg REST service and unified access control.
aliases: [Gravitino]
platform: platform-open-source
kind: open-source
availability: ga
realises:
- table-catalogue
- metadata-interoperability
- access-control
- data-catalogue
- catalogue-federation
- credential-vending
- object-file-access
resource: https://gravitino.apache.org/blog/gravitino-top-level-project
tags: [open-source]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Apache 2.0, led by Datastrato; became an ASF top-level project in June 2025 and is on the 1.x line. Connects Hive, Iceberg, Paimon, Hudi, Kafka and relational databases under one namespace. Useful when several catalogues need to be governed together.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management) (primary): Register tables, their schemas and storage locations so engines can find, govern and share them.
- [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md) (Metadata and discovery): Exchange metadata between tools through open APIs and standards.
- [Access control](../../capabilities/security/access-control.md) (Security and access): Decide who can see and change which data, at every level from account down to individual values.
- [Data catalogue](../../capabilities/metadata/data-catalogue.md) (Metadata and discovery): Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
- [Catalogue federation](../../capabilities/storage/catalogue-federation.md) (Storage and table management): Present tables from several catalogues through one catalogue with one set of permissions, without copying metadata by hand.
- [Storage credential vending](../../capabilities/storage/credential-vending.md) (Storage and table management): Have the catalogue issue short-lived, table-scoped storage credentials to engines so they never hold broad storage access.
- [File-system access to object storage](../../capabilities/storage/object-file-access.md) (Storage and table management): Mount object storage as a file system so file-based tools, ML jobs and agents can work on lake data without copies.

**Platform:** [Open-source ecosystem](../../platforms/platform-open-source.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Glue Data Catalog](../aws/aws-glue-data-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Lakehouse](../microsoft/fabric-lakehouse.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Google Cloud Lakehouse runtime catalog](../google-cloud/gcp-lakehouse-runtime-catalog.md), [Dataproc Metastore](../google-cloud/gcp-dataproc-metastore.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Horizon Catalog](../snowflake/snowflake-horizon-catalog.md) | [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Unity Catalog](../databricks/databricks-unity-catalog.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Iceberg REST Catalog](../cloudera/cloudera-iceberg-rest-catalog.md) | [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Autonomous AI Database Catalog](../oracle/oracle-autonomous-ai-database-catalog.md), [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Catalogue federation](../../capabilities/storage/catalogue-federation.md), [Data catalogue](../../capabilities/metadata/data-catalogue.md), [Metadata interoperability](../../capabilities/metadata/metadata-interoperability.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [SAP](../../platforms/platform-sap.md) | [Dremio Cloud](../sap/dremio-cloud.md) | [Storage credential vending](../../capabilities/storage/credential-vending.md), [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [IBM](../../platforms/platform-ibm.md) | [Confluent Tableflow](../ibm/confluent-tableflow.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Iceberg tables in Palantir Foundry](../palantir/palantir-iceberg-tables.md) (preview) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Fivetran Managed Data Lake Service](../independent/fivetran-managed-data-lake-service.md) | [Table catalogue](../../capabilities/storage/table-catalogue.md) |
