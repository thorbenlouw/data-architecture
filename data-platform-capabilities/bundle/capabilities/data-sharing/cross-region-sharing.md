---
type: Capability
id: cross-region-sharing
title: Cross-region and cross-cloud sharing
description: Share data with consumers on other clouds or regions, replicating it where needed.
broader: [external-data-sharing]
related: [data-residency, cross-region-failover, cost-attribution, data-slas, open-protocol-sharing]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Serving every query across regions would be slow and incur network egress charges, so the platform replicates shared tables to the consumer's region or cloud, refreshes them on a schedule or continuously, and presents them to the consumer as an ordinary share. A European provider sharing with a partner in Asia-Pacific, for example, pays to store and refresh one replica there rather than serving each query across continents.

It matters for global organisations and for providers whose customers use several clouds. The trade-offs are cost, freshness and law: replicas add storage and transfer charges, lag behind the source, and place data in another jurisdiction. Some platforms replicate only the parts consumers actually query, to reduce cost. It differs from cross-region failover, which copies data for recovery rather than for consumers.

# Key considerations

- Replicating data to another region may breach residency requirements. Check before enabling, and record where replicas live.
- Egress and replica storage can cost more than the source data. Model costs per consumer region.
- Consumers see data with a delay. State the replication lag in the share's service level.
- Revocation and deletion must reach replicas promptly.

# Questions to ask

- In which regions and clouds are your consumers?
- Is any of the shared data subject to residency or sovereignty rules?
- How fresh must the data be at the consumer's end?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [External data sharing](external-data-sharing.md) |
| Related | [Cost attribution and chargeback](../platform-operations/cost-attribution.md), [Cross-region replication and failover](../platform-operations/cross-region-failover.md), [Data residency and sovereignty](../governance/data-residency.md), [Data service levels](../data-products/data-slas.md), [Open-protocol sharing](open-protocol-sharing.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 4 Data Sovereignty and Cross-Border Movement (Governance and accountability) · [GDPR](../../frameworks/framework-gdpr.md): Articles 44 to 49 – Transfers to third countries

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Redshift data sharing](../../technologies/aws/aws-redshift-data-sharing.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery sharing](../../technologies/google-cloud/gcp-bigquery-sharing.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | Cross-Cloud Auto-Fulfillment | [Snowflake listings (with Cross-Cloud Auto-Fulfillment)](../../technologies/snowflake/snowflake-listings.md), [Snowflake replication and failover groups](../../technologies/snowflake/snowflake-replication-failover.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks OpenSharing](../../technologies/databricks/databricks-opensharing.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenSharing protocol](../../technologies/open-source/delta-sharing.md) |
