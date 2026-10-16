---
type: Capability
id: hybrid-data-plane
title: Customer-hosted data plane
description: Run processing inside your own network or cloud account while the vendor operates the control plane as a service.
aliases: [secure agent, BYOC data plane, bring your own cloud]
broader: [deployment-options]
related: [data-residency, customer-managed-keys, edge-data-processing, multi-tenancy]
depends_on: [network-security]
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The platform is split in two. The control plane, run by the vendor as a service, holds the user interface, scheduling, metadata and administration. The data plane, where data is read and processed, runs inside the customer's own cloud account or network: clusters or agents run there, read from the customer's storage and databases, and send back only status, metadata and results. For example, an integration service's agent installed on premises extracts from an internal database and writes to the lake without the data passing through the vendor's servers.

This answers security and residency concerns that rule out fully hosted services, and lets processing run close to sources that cannot be reached from the internet. The customer keeps control of networks, encryption keys and storage, but takes on part of the operating effort: capacity, agent updates and network rules. Check exactly what crosses to the control plane, since logs, error messages, query text and data previews can carry sensitive values. The model is also called bring your own cloud (BYOC).

# Key considerations

- Document every flow from the data plane to the vendor's control plane, including logs, error messages, query text and previews.
- Agree how the data plane is upgraded. Delayed agent or runtime updates can break compatibility with the control plane.
- The data plane needs outbound connections to the control plane. Confirm this fits network policy and uses private connectivity where available.
- Check what keeps working if the control plane is unavailable, such as running jobs or scheduled pipelines.

# Questions to ask

- Must data never leave your own network or cloud account, even briefly?
- Which sources can only be reached from inside your network?
- Who will operate the infrastructure the data plane runs on?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Hybrid and multi-cloud deployment](deployment-options.md) |
| Related | [Customer-managed keys](../security/customer-managed-keys.md), [Data residency and sovereignty](../governance/data-residency.md), [Edge data processing](../processing/edge-data-processing.md), [Multi-tenancy and workspace isolation](multi-tenancy.md), [Network security](../security/network-security.md) |
| Depends on | [Network security](../security/network-security.md) |

# Where it appears

- **Personas:** [Data platform engineer](../../personas/persona-platform-engineer.md)
- **Maturity tracks:** [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Outposts](../../technologies/aws/aws-outposts.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure Data Factory](../../technologies/microsoft/azure-data-factory.md), [Microsoft on-premises and virtual network data gateways](../../technologies/microsoft/fabric-data-gateways.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Openflow](../../technologies/snowflake/snowflake-openflow.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks classic compute (Databricks Runtime clusters)](../../technologies/databricks/databricks-classic-compute.md), [Databricks SQL warehouses (serverless, pro and classic)](../../technologies/databricks/databricks-sql-warehouses.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse BYOC (Bring Your Own Cloud)](../../technologies/clickhouse/clickhouse-byoc.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [IDMC serverless runtime environment](../../technologies/informatica/informatica-serverless-runtime-environment.md), [Informatica Cloud Data Integration (CDI)](../../technologies/informatica/informatica-cloud-data-integration.md), [Informatica Cloud Data Integration for PowerCenter (CDI-PC)](../../technologies/informatica/informatica-cdi-pc.md), [Informatica Intelligent Data Management Cloud (IDMC)](../../technologies/informatica/informatica-idmc.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera on cloud](../../technologies/cloudera/cloudera-on-cloud.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database](../../technologies/oracle/oracle-autonomous-ai-database.md), [Oracle Exadata](../../technologies/oracle/oracle-exadata.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM StreamSets](../../technologies/ibm/ibm-streamsets.md), [IBM watsonx.data](../../technologies/ibm/ibm-watsonx-data.md), [IBM watsonx.data integration](../../technologies/ibm/ibm-watsonx-data-integration.md), [WarpStream](../../technologies/ibm/warpstream.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Airbyte Cloud](../../technologies/independent/airbyte-cloud.md), [Astronomer Astro](../../technologies/independent/astronomer-astro.md), [Dagster+](../../technologies/independent/dagster-plus.md), [Estuary](../../technologies/independent/estuary.md), [Fivetran](../../technologies/independent/fivetran.md), [Matillion Maia Foundation](../../technologies/independent/matillion-maia-foundation.md), [Pinecone](../../technologies/independent/pinecone.md), [Prefect Cloud](../../technologies/independent/prefect-cloud.md), [Qlik Open Lakehouse](../../technologies/independent/qlik-open-lakehouse.md), [Qlik Talend Cloud](../../technologies/independent/qlik-talend-cloud.md), [Redpanda Cloud](../../technologies/independent/redpanda-cloud.md), [StarTree Cloud](../../technologies/independent/startree-cloud.md) |
