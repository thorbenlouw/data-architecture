---
type: Technology
id: informatica-cdi-pc
title: Informatica Cloud Data Integration for PowerCenter (CDI-PC)
description: Runs existing PowerCenter sessions and workflows unchanged in a customer-hosted domain whose management, monitoring and upgrades are handled from IDMC.
aliases: [CDI-PC]
platform: platform-informatica
kind: managed-service
availability: ga
realises: [hybrid-data-plane, low-code-transformation]
resource: https://onlinehelp.informatica.com/IICS/prod/dmsui/en/aa-gettingstarted-x/Introducing_Cloud_Data_Integration_for_PowerCenter_CDI-PC.html
tags: [informatica]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Use it to lift and shift PowerCenter first and convert to native CDI later. It needs a Secure Agent to connect the domain to IDMC.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) (Platform operations) (primary): Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
- [Low-code transformation](../../capabilities/processing/low-code-transformation.md) (Processing and transformation): Build transformation logic visually from configurable components rather than writing code.

**Platform:** [Informatica](../../platforms/platform-informatica.md)  
**Availability:** ga  
**Product family:** Intelligent Data Management Cloud, Cloud Data Integration, PowerCenter

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [AWS Outposts](../aws/aws-outposts.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure Data Factory](../microsoft/azure-data-factory.md), [Microsoft on-premises and virtual network data gateways](../microsoft/fabric-data-gateways.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake Openflow](../snowflake/snowflake-openflow.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks SQL warehouses (serverless, pro and classic)](../databricks/databricks-sql-warehouses.md), [Databricks classic compute (Databricks Runtime clusters)](../databricks/databricks-classic-compute.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse BYOC (Bring Your Own Cloud)](../clickhouse/clickhouse-byoc.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Cloudera](../../platforms/platform-cloudera.md) | [Cloudera on cloud](../cloudera/cloudera-on-cloud.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Exadata](../oracle/oracle-exadata.md), [Oracle Autonomous AI Database](../oracle/oracle-autonomous-ai-database.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data integration](../ibm/ibm-watsonx-data-integration.md), [WarpStream](../ibm/warpstream.md), [IBM StreamSets](../ibm/ibm-streamsets.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Data Connection](../palantir/palantir-data-connection.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Matillion Maia Foundation](../independent/matillion-maia-foundation.md), [Qlik Talend Cloud](../independent/qlik-talend-cloud.md), [Prefect Cloud](../independent/prefect-cloud.md) | [Customer-hosted data plane](../../capabilities/platform-operations/hybrid-data-plane.md), [Low-code transformation](../../capabilities/processing/low-code-transformation.md) |
