---
type: Technology
id: sas-data-hub
title: SAS Data Hub
description: Data connectivity application in SAS Viya for defining and monitoring connections to databases, cloud data platforms and file stores, and for browsing and previewing their data.
formerly: [SAS Data Explorer]
platform: platform-sas
kind: feature
availability: ga
realises: [database-extraction, query-federation]
resource: https://www.sas.com/en_us/software/data-hub.html
tags: [sas]
status: draft
stale_after: '2027-04-20T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-20T14:10:17Z'}
---

Renamed from SAS Data Explorer, with connection management added. Listed sources include Snowflake, Databricks, BigQuery, Redshift, Oracle, Teradata, MongoDB, and Parquet and ORC files. It pushes SQL processing down to supported databases, loads data in bulk, and through Cloud Data Exchange lets SAS applications read remote data as if it were SAS data.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) (Ingestion and integration) (primary): Extract full or incremental snapshots from relational and NoSQL databases using queries or bulk export.
- [Query federation](../../capabilities/compute/query-federation.md) (Query and compute): Query data where it lives, in other databases, storage accounts or clouds, without loading it into the platform first.

**Platform:** [SAS](../../platforms/platform-sas.md)  
**Availability:** ga  
**Product family:** SAS Viya, SAS Data Management

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Database Migration Service](../aws/aws-dms.md), [Amazon Redshift federated query](../aws/aws-redshift-federated-query.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Copy job](../microsoft/fabric-copy-job.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Data Transfer Service](../google-cloud/gcp-bigquery-data-transfer-service.md), [Dataflow templates](../google-cloud/gcp-dataflow-templates.md), [Cloud Data Fusion](../google-cloud/gcp-data-fusion.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Lakeflow Connect](../databricks/databricks-lakeflow-connect.md), [Lakehouse Federation (query federation)](../databricks/databricks-lakehouse-federation.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickPipes database connectors (Postgres CDC, MySQL CDC, MongoDB CDC, BigQuery)](../clickhouse/clickhouse-clickpipes-cdc.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Database Ingestion and Replication](../informatica/informatica-database-ingestion-and-replication.md), [Informatica Cloud Data Integration (CDI)](../informatica/informatica-cloud-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera Data Flow](../cloudera/cloudera-data-flow.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Integration](../oracle/oracle-oci-data-integration.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md), [Query federation](../../capabilities/compute/query-federation.md) |
| [Dataiku](../../platforms/platform-dataiku.md) | [Dataiku connections](../dataiku/dataiku-connections.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [dlt (data load tool)](../open-source/dlt.md), [Airbyte](../open-source/airbyte.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Airbyte Cloud](../independent/airbyte-cloud.md), [Fivetran](../independent/fivetran.md) | [Database extraction](../../capabilities/ingestion-integration/database-extraction.md) |
