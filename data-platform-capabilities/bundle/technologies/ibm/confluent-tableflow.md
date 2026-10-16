---
type: Technology
id: confluent-tableflow
title: Confluent Tableflow
description: Materialises Kafka topics and their schemas as Apache Iceberg or Delta Lake tables, taking care of type conversion, schema evolution, compaction and catalogue sync.
aliases: [Tableflow]
platform: platform-ibm
kind: feature
availability: ga
realises: [stream-to-table, table-maintenance, table-catalogue]
resource: https://docs.confluent.io/cloud/current/topics/tableflow/overview.html
tags: [ibm]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tables can live in Confluent-managed storage or in the customer's S3, Azure or GCS. External catalogue sync (AWS Glue, Unity Catalog, Polaris, Snowflake Open Catalog) works only with customer storage. Iceberg went GA in March 2025, and Delta Lake is now GA.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) (Ingestion and integration) (primary): Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.
- [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) (Storage and table management): Compact small files, remove obsolete files and reorganise data so tables stay fast and cheap.
- [Table catalogue](../../capabilities/storage/table-catalogue.md) (Storage and table management): Register tables, their schemas and storage locations so engines can find, govern and share them.

**Platform:** [IBM](../../platforms/platform-ibm.md)  
**Availability:** ga  
**Product family:** Confluent

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Data Firehose](../aws/aws-data-firehose.md) | [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric Eventstream](../microsoft/fabric-eventstream.md) | [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Apache Fluss (incubating)](../open-source/apache-fluss.md) (preview) | [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Qlik Open Lakehouse](../independent/qlik-open-lakehouse.md), [Redpanda Cloud](../independent/redpanda-cloud.md), [Starburst Galaxy](../independent/starburst-galaxy.md) | [Stream-to-table materialisation](../../capabilities/ingestion-integration/stream-to-table.md), [Table maintenance and optimisation](../../capabilities/storage/table-maintenance.md) |
