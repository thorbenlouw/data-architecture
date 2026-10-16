---
type: Technology
id: snowflake-unload
title: Snowflake data unloading (COPY INTO <location>)
description: Writes query results or tables to files in internal or external stages as CSV, JSON or Parquet, optionally partitioned.
platform: platform-snowflake
kind: feature
availability: ga
realises: [data-export]
resource: https://docs.snowflake.com/en/user-guide/data-unload-overview
tags: [snowflake]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---


<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Data export](../../capabilities/serving/data-export.md) (Serving and activation) (primary): Unload query results or tables to files and external systems in bulk.

**Platform:** [Snowflake](../../platforms/platform-snowflake.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Athena](../aws/aws-athena.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Power BI paginated reports](../microsoft/powerbi-paginated-reports.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery EXPORT DATA](../google-cloud/gcp-bigquery-export-data.md) | [Data export](../../capabilities/serving/data-export.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse integration table engines and table functions](../clickhouse/clickhouse-integration-engines.md), [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../clickhouse/clickhouse-data-lake.md) | [Data export](../../capabilities/serving/data-export.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere replication flows](../sap/sap-datasphere-replication-flows.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Data export](../../capabilities/serving/data-export.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Kafka Connect](../open-source/apache-kafka-connect.md) | [Data export](../../capabilities/serving/data-export.md) |
