---
type: Technology
id: clickhouse-cloud
title: ClickHouse Cloud
description: Fully managed ClickHouse on AWS, GCP and Azure that stores data in object storage and scales, idles and upgrades services automatically.
platform: platform-clickhouse
kind: managed-service
availability: ga
realises: [real-time-analytics, serverless-compute, elastic-scaling, identity-authentication]
resource: https://clickhouse.com/docs/cloud/manage/cloud-tiers
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tiers were restructured in January 2025 into Basic (single zone, 1 TB limit, no scaling), Scale (multi-zone, autoscaling, private networking, compute-compute separation) and Enterprise (adds SAML SSO, CMEK, HIPAA/PCI, custom hardware profiles, scheduled upgrades). Vertical autoscaling and idling are GA; horizontal autoscaling entered private preview in June 2026 and On-Demand Compute for burst queries over Iceberg/Delta in September 2026. JWT authentication against customer identity providers became GA for Enterprise in September 2026.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) (Query and compute) (primary): Answer analytical queries in milliseconds over fresh, high-volume data, often for user-facing applications.
- [Serverless compute](../../capabilities/compute/serverless-compute.md) (Query and compute): Run workloads without managing servers, with capacity allocated on demand and billed by use.
- [Elastic scaling](../../capabilities/compute/elastic-scaling.md) (Query and compute): Add and remove compute automatically as load changes, including for bursts of concurrent users.
- [Identity and authentication](../../capabilities/security/identity-authentication.md) (Security and access): Authenticate people and services through central identity, single sign-on and short-lived credentials.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Timestream for InfluxDB](../aws/aws-timestream-influxdb.md), [Amazon OpenSearch Service](../aws/aws-opensearch-service.md), [Amazon Redshift Serverless](../aws/aws-redshift-serverless.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Explorer](../microsoft/azure-data-explorer.md), [Eventhouse and KQL database](../microsoft/fabric-eventhouse.md), [Fabric Real-Time Dashboard](../microsoft/fabric-real-time-dashboards.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake interactive tables and interactive warehouses](../snowflake/snowflake-interactive-tables.md), [Snowflake Adaptive Compute](../snowflake/snowflake-adaptive-compute.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md), [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks Lakehouse Real-Time](../databricks/databricks-lakehouse-real-time.md) (preview) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Informatica](../../platforms/platform-informatica.md) | [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Elastic scaling](../../capabilities/compute/elastic-scaling.md), [Serverless compute](../../capabilities/compute/serverless-compute.md) |
| [Oracle](../../platforms/platform-oracle.md) | [MySQL HeatWave](../oracle/oracle-mysql-heatwave.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Doris](../open-source/apache-doris.md), [Apache Pinot](../open-source/apache-pinot.md), [StarRocks](../open-source/starrocks.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Imply Polaris](../independent/imply-polaris.md), [StarTree Cloud](../independent/startree-cloud.md), [Tinybird](../independent/tinybird.md) | [Real-time analytical database](../../capabilities/compute/real-time-analytics.md) |
