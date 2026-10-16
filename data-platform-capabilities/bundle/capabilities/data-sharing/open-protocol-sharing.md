---
type: Capability
id: open-protocol-sharing
title: Open-protocol sharing
description: Share live tables with consumers on other platforms through open protocols, so they need not use the same vendor.
aliases: [open sharing, Iceberg REST sharing]
broader: [external-data-sharing]
related: [credential-vending, engine-interoperability, catalogue-federation, cross-region-sharing]
depends_on: [open-table-formats]
tags: [data-sharing]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Delta Sharing is a widely used example. The provider runs a sharing server and issues the recipient a credential. The recipient's client asks the server for a table and receives short-lived signed links to the underlying Parquet files, which it reads straight from storage. Any engine with a compatible client can read the share. Open catalogue APIs, such as the Apache Iceberg REST catalogue, achieve a similar result by letting outside engines read tables with credentials the catalogue issues.

It matters when partners or internal teams use different platforms and neither side wants to build an export pipeline or adopt the other's vendor. Data is read in place, so there is still one copy and access can be revoked. Trade-offs include controls that do not cross the protocol in every implementation, such as row filters, masking and views, and the provider paying egress when consumers read from another cloud or region.

# Key considerations

- Check which tools and engines your consumers use and whether they support the protocol natively.
- Confirm how row filters, masking and views are applied, since the consumer reads files directly.
- Credentials and signed links must be short-lived and scoped. Long-lived bearer tokens passed around by email are a common weakness.
- Cross-cloud reads put egress charges on the provider. Consider replicas for heavy consumers.

# Questions to ask

- Which platforms do your consumers use?
- Do shared datasets need row- or column-level restrictions per recipient?
- Who will operate the sharing endpoint and manage recipient credentials?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Data sharing and collaboration](data-sharing.md) |
| Broader | [External data sharing](external-data-sharing.md) |
| Related | [Catalogue federation](../storage/catalogue-federation.md), [Cross-region and cross-cloud sharing](cross-region-sharing.md), [Metadata interoperability](../metadata/metadata-interoperability.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Storage credential vending](../storage/credential-vending.md) |
| Depends on | [Open table formats](../storage/open-table-formats.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (benefits from)
- **Maturity tracks:** [Data sharing](../../maturity/track-data-sharing.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Lakehouse](../../technologies/google-cloud/gcp-lakehouse.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Open Data Sharing](../../technologies/snowflake/snowflake-open-data-sharing.md) (preview) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks OpenSharing](../../technologies/databricks/databricks-opensharing.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Iceberg REST Catalog](../../technologies/cloudera/cloudera-iceberg-rest-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud Connect](../../technologies/sap/sap-bdc-connect.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Iceberg tables in Palantir Foundry](../../technologies/palantir/palantir-iceberg-tables.md) (preview) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenSharing protocol](../../technologies/open-source/delta-sharing.md) |
