---
type: Capability
id: data-export
title: Data export
description: Unload query results or tables to files and external systems in bulk.
aliases: [unload, extracts]
broader: [serving]
related:
- managed-file-transfer
- external-data-sharing
- data-loss-prevention
- data-reconciliation
- file-formats
tags: [serving]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data export writes query results or whole tables out of the platform in bulk: to files in object storage as CSV, JSON or Parquet, to another database, or to a partner's location. A monthly job might query transactions for a regulator, write compressed Parquet files to a bucket, create a manifest with row counts and checksums, and hand the files to managed file transfer for delivery. Most engines provide an unload or COPY INTO command that writes in parallel from many nodes.

Exports serve consumers who cannot or will not connect to the platform, such as regulators, partners, legacy systems and archives. They are simple and widely understood, but each export is a copy outside the platform's access control, lineage and retention. That is why live data sharing is preferred where both sides can use it. Reverse ETL differs by mapping records into a particular application's objects, and change feeds by delivering changes continuously.

# Key considerations

- Exported files leave platform governance. Classify exports, record their destinations and apply retention to the files.
- Choose formats the consumer can read reliably. CSV is universal but loses types; Parquet keeps them but needs suitable tools.
- Parallel writers produce many files. Agree file sizes and naming with the consumer.
- Include a manifest with counts and checksums so the receiver can confirm the delivery is complete.

# Questions to ask

- Who receives exported data, in what format and how often?
- Could the consumer use live sharing or SQL access instead of files?
- What controls apply to the data once it leaves the platform?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Serving and activation](serving.md) |
| Broader | [Serving and activation](serving.md) |
| Related | [Data loss prevention](../security/data-loss-prevention.md), [Data reconciliation](../data-quality/data-reconciliation.md), [External data sharing](../data-sharing/external-data-sharing.md), [Managed file transfer](../ingestion-integration/managed-file-transfer.md), [Open file formats](../storage/file-formats.md), [Paginated reports](../analytics-bi/paginated-reports.md) |

# Where it appears

- **Use cases:** [Customer-facing analytics](../../use-cases/usecase-customer-facing-analytics.md) (benefits from) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (benefits from)
- **Maturity tracks:** [Data serving](../../maturity/track-serving.md) (from level 1, Initial)
- **Frameworks:** [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter V, Section I – ICT third-party risk management (Articles 28 to 30) · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapters II and III – Access to and sharing of connected-product data; Chapter V – Business-to-government access in exceptional need; Chapter VI – Switching between data processing services · [GDPR](../../frameworks/framework-gdpr.md): Article 20 – Right to data portability

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Athena](../../technologies/aws/aws-athena.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Power BI paginated reports](../../technologies/microsoft/powerbi-paginated-reports.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery EXPORT DATA](../../technologies/google-cloud/gcp-bigquery-export-data.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | unloading (COPY INTO <location>) | [Snowflake data unloading (COPY INTO <location>)](../../technologies/snowflake/snowflake-unload.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) |  | [ClickHouse data lake table engines and functions (Iceberg, Delta Lake, Hudi, Paimon)](../../technologies/clickhouse/clickhouse-data-lake.md), [ClickHouse integration table engines and table functions](../../technologies/clickhouse/clickhouse-integration-engines.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere replication flows](../../technologies/sap/sap-datasphere-replication-flows.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Data Connection](../../technologies/palantir/palantir-data-connection.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Kafka Connect](../../technologies/open-source/apache-kafka-connect.md) |
