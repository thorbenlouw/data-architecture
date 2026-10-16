---
type: Technology
id: gcp-bigquery-export-data
title: BigQuery EXPORT DATA
description: SQL statement that writes query results to Cloud Storage files or directly into Bigtable, Spanner, Pub/Sub and AlloyDB.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [data-export, reverse-etl]
resource: https://docs.cloud.google.com/bigquery/docs/exporting-data
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Exports to Spanner went GA in March 2026; exports to Bigtable, Spanner and AlloyDB require Enterprise or higher. For continuous streaming to these targets use continuous queries.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data export](../../capabilities/serving/data-export.md) (Serving and activation) (primary): Unload query results or tables to files and external systems in bulk.
- [Reverse ETL](../../capabilities/serving/reverse-etl.md) (Serving and activation): Sync modelled data from the platform back into operational tools such as CRM and marketing systems.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI paginated reports](../microsoft/powerbi-paginated-reports.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake data unloading (COPY INTO <location>)](../snowflake/snowflake-unload.md) | [Data export](../../capabilities/serving/data-export.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Data export](../../capabilities/serving/data-export.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md) | [Data export](../../capabilities/serving/data-export.md) |
