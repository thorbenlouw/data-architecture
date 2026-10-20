---
type: Capability
id: deployment-options
title: Hybrid and multi-cloud deployment
description: Run the platform across clouds, regions or on-premises, or inside your own cloud account.
aliases: [BYOC, self-managed, sovereign cloud]
broader: [platform-operations]
related:
- data-residency
- engine-interoperability
- open-table-formats
- cross-region-failover
- network-security
tags: [platform-operations]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The deployment model decides who runs what and where data sits. Fully managed software as a service runs everything in the vendor's cloud account. A customer-hosted data plane runs processing, and usually storage, in your own cloud account while the vendor runs the control plane. Self-managed software runs entirely on infrastructure you operate, in a cloud or on premises. Multi-cloud runs the platform on more than one cloud provider; hybrid combines cloud with on-premises systems; sovereign cloud offerings run in one jurisdiction with locally controlled operations.

The usual drivers are data residency and sovereignty rules, existing on-premises investment, latency to sources, negotiating position with cloud providers and avoiding dependence on one vendor. Each step away from a fully managed service gives more control and usually more operational work. Multi-cloud brings the highest costs: data transfer between clouds, different security models and the need for portable formats and tools. Open table formats and shared catalogues reduce the cost of running several engines in several places.

# Key considerations

- Confirm feature parity. Self-managed, sovereign and smaller-region editions often lag the main service or lack some features.
- Count data transfer between clouds and regions. Egress charges and latency often decide which multi-cloud designs are practical.
- Be clear who patches, scales, backs up and responds to incidents in each model.
- Choose for actual requirements. Running in several clouds for theoretical portability multiplies operating cost.

# Questions to ask

- Which regulations or contracts limit where data may be stored and processed, and by whom?
- Does any data or processing need to stay on premises for latency, cost or policy reasons?
- Which cloud providers does the organisation already use and have agreements with?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Platform operations](platform-operations.md) |
| Broader | [Platform operations](platform-operations.md) |
| Narrower | [Customer-hosted data plane](hybrid-data-plane.md) |
| Related | [Backup and disaster recovery](business-continuity.md), [Cross-region replication and failover](cross-region-failover.md), [Data residency and sovereignty](../governance/data-residency.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Network security](../security/network-security.md), [Open table formats](../storage/open-table-formats.md) |

# Where it appears

- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Platform migration and portability](../../maturity/track-platform-migration.md) (from level 2, Managed)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Architecture · [DCAM v3](../../frameworks/framework-edm-dcam.md): 3 Architecture – Business, Data & Technology · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter V, Section I – ICT third-party risk management (Articles 28 to 30); Chapter V, Section II – Oversight of critical ICT third-party providers (Articles 31 to 44) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VI – Switching between data processing services

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [AWS Outposts](../../technologies/aws/aws-outposts.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure IoT Operations](../../technologies/microsoft/azure-iot-operations.md), [Power BI Report Server](../../technologies/microsoft/powerbi-report-server.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [AlloyDB for PostgreSQL](../../technologies/google-cloud/gcp-alloydb.md), [BigQuery Omni](../../technologies/google-cloud/gcp-bigquery-omni.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake organisations](../../technologies/snowflake/snowflake-organizations.md), [Virtual Private Snowflake (VPS)](../../technologies/snowflake/snowflake-virtual-private-snowflake.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | BYOC, ClickHouse Private |  |
| [Informatica](../../platforms/platform-informatica.md) | Secure Agent and points of delivery (PODs) | [Informatica Intelligent Data Management Cloud (IDMC)](../../technologies/informatica/informatica-idmc.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Anywhere Cloud](../../technologies/cloudera/cloudera-anywhere-cloud.md) (unconfirmed), [Cloudera Base on premises](../../technologies/cloudera/cloudera-base-on-premises.md), [Cloudera Data Services on premises](../../technologies/cloudera/cloudera-data-services-on-premises.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Database@AWS, Oracle Database@Azure and Oracle Database@Google Cloud](../../technologies/oracle/oracle-database-multicloud.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Warehouse in SAP Business Data Cloud](../../technologies/sap/sap-business-warehouse-bdc.md) |
| [Teradata](../../platforms/platform-teradata.md) | Teradata Cloud / Teradata Factory | [Teradata Autonomous Knowledge Platform](../../technologies/teradata/teradata-autonomous-knowledge-platform.md), [Teradata Factory](../../technologies/teradata/teradata-factory.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Platform](../../technologies/ibm/confluent-platform.md), [IBM Software Hub (Cloud Pak for Data)](../../technologies/ibm/ibm-software-hub.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Apollo](../../technologies/palantir/palantir-apollo.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Viya](../../technologies/sas/sas-viya.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Cloud](../../technologies/dataiku/dataiku-cloud.md), [Dataiku Cloud Stacks and Fleet Manager](../../technologies/dataiku/dataiku-cloud-stacks.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Fivetran HVR](../../technologies/independent/fivetran-hvr.md), [Starburst Enterprise](../../technologies/independent/starburst-enterprise.md) |

Narrower capabilities are realised by a further 31 technologies; see their pages.
