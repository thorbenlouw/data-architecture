---
type: Technology
id: clickhouse-byoc
title: ClickHouse BYOC (Bring Your Own Cloud)
description: Runs the ClickHouse Cloud data plane, including clusters, data and backups, inside the customer's own cloud account while ClickHouse operates the control plane.
platform: platform-clickhouse
kind: managed-service
availability: ga
realises: [hybrid-data-plane, data-residency, network-security]
resource: https://clickhouse.com/docs/cloud/reference/byoc/overview
tags: [clickhouse]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA on AWS (February 2025), GCP (April 2026) and Azure, with an Azure Marketplace listing from June 2026. Requires a committed contract. For fully self-managed estates ClickHouse also offers ClickHouse Private, which carries some Cloud-only features such as masking policies.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations) (primary): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Data residency and sovereignty](../../capabilities/governance/data-residency.md) (Governance and compliance): Keep data and its processing in approved jurisdictions and prove that you have.
- [Network security](../../capabilities/security/network-security.md) (Security and access): Keep data traffic on private networks and restrict where the platform can be reached from.

**Platform:** [ClickHouse](../../platforms/platform-clickhouse.md)  
**Availability:** ga  
**Product family:** ClickHouse Cloud

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft on-premises and virtual network data gateways](../microsoft/fabric-data-gateways.md), [Azure Data Factory](../microsoft/azure-data-factory.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Network security](../../capabilities/security/network-security.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Intelligent Data Management Cloud (IDMC)](../informatica/informatica-idmc.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../informatica/informatica-cdi-pc.md), [IDMC serverless runtime environment](../informatica/informatica-serverless-runtime-environment.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Data residency and sovereignty](../../capabilities/governance/data-residency.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md), [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [IBM](../../platforms/platform-ibm.md) | [WarpStream](../ibm/warpstream.md), [IBM StreamSets](../ibm/ibm-streamsets.md), [IBM watsonx.data](../ibm/ibm-watsonx-data.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Prefect Cloud](../independent/prefect-cloud.md), [Redpanda Cloud](../independent/redpanda-cloud.md), [Matillion Maia Foundation](../independent/matillion-maia-foundation.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
