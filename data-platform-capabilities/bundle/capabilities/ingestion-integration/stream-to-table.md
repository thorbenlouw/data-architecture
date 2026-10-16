---
type: Capability
id: stream-to-table
title: Stream-to-table materialisation
description: Expose event-stream topics directly as open-format tables, with schema mapping, compaction and catalogue registration handled for you.
aliases: [Tableflow, Iceberg topics, stream-lake tiering]
broader: [streaming-ingestion]
related: [schema-registry, table-maintenance, schema-evolution, engine-interoperability]
depends_on: [event-streaming, open-table-formats, table-catalogue]
tags: [ingestion-integration]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Instead of a separate job reading a topic and writing a table, the streaming platform or a managed service writes topic data in an open table format such as Apache Iceberg or Delta Lake itself. Each topic appears as a table in a catalogue; its event schema, taken from the schema registry, becomes the table schema; and the service compacts small files and expires old snapshots. An analyst can query the last hour of a payments topic with SQL without anyone building a pipeline.

It removes a class of glue jobs and the work of keeping them running, and it can avoid storing data twice when the table doubles as the stream's long-term storage. The trade-offs are less control over table layout, limited transformation on the way in, and reliance on how well the service handles schema changes and upserts. Where data needs substantial reshaping before it is useful, a stream processor writing to tables is still the better fit.

# Key considerations

- Check whether keyed topics can be written as upserts and deletes, or only appended. Change-event topics need the former.
- Partitioning chosen by the service may not suit query patterns. Confirm what can be configured.
- Find out which catalogue the tables are registered in, and whether other engines can read and govern them there.
- Topic schema changes must map cleanly to table schema evolution, or tables stop updating.

# Questions to ask

- Which topics are queried as tables today, and through how many hand-built pipelines?
- Do consumers need raw events, or transformed and joined data?
- Which table format and catalogue do the platform's engines use?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Ingestion and integration](ingestion-integration.md) |
| Broader | [Streaming ingestion](streaming-ingestion.md) |
| Related | [Multi-engine interoperability](../compute/engine-interoperability.md), [Schema enforcement and evolution](../storage/schema-evolution.md), [Schema registry](../metadata/schema-registry.md), [Table maintenance and optimisation](../storage/table-maintenance.md) |
| Depends on | [Event streaming](event-streaming.md), [Open table formats](../storage/open-table-formats.md), [Table catalogue](../storage/table-catalogue.md) |

# Where it appears

- **Use cases:** [Application data publishing](../../use-cases/usecase-application-data-publishing.md) (benefits from)
- **Patterns:** [Kappa architecture](../../patterns/kappa-architecture.md)
- **Maturity tracks:** [Ingestion and integration](../../maturity/track-ingestion.md) (from level 3, Defined) · [Real-time and streaming](../../maturity/track-real-time.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Data Firehose](../../technologies/aws/aws-data-firehose.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Fabric Eventstream](../../technologies/microsoft/fabric-eventstream.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [Confluent Tableflow](../../technologies/ibm/confluent-tableflow.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Fluss (incubating)](../../technologies/open-source/apache-fluss.md) (preview) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Qlik Open Lakehouse](../../technologies/independent/qlik-open-lakehouse.md), [Redpanda Cloud](../../technologies/independent/redpanda-cloud.md), [Starburst Galaxy](../../technologies/independent/starburst-galaxy.md) |
