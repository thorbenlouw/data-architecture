---
type: Capability
id: metadata
title: Metadata and discovery
description: Capture, organise and expose information about data so people and machines can find, understand and trust it.
aliases: [metadata management]
broader: []
related: [table-catalogue, governance, data-quality, data-products, semantic-layer]
order: 11
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Metadata is information about data. Technical metadata covers schemas, types, locations and partitions. Operational metadata covers job runs, freshness and row counts. Business metadata covers definitions, owners and classifications, and usage metadata records who queries what. This domain is about collecting that information, organising it and putting it to work for people and for machines.

The data catalogue is the inventory people search. Harvesting fills it automatically, and the business glossary, usage signals, AI-drafted documentation and certification add meaning and trust. Lineage records how data flows, at table and column level, across systems, and through documents and models; impact analysis turns it into decisions about changes and incidents. The schema registry plays a similar role for event streams, controlling how message formats change.

Metadata is increasingly read by machines as well as people. Active metadata triggers actions such as propagating tags or alerting owners; metadata interoperability lets tools exchange it through open standards; and the AI context layer serves definitions and verified queries to agents. This domain differs from the table catalogue in the storage domain, which engines use to resolve table names and storage locations. Many platforms combine the two, but the needs differ: engines need accuracy and speed, people and agents need meaning and context.

# Key considerations

- Capture metadata automatically wherever possible. Anything maintained only by hand goes stale.
- Decide which system is the source of truth for each kind of metadata, such as definitions, owners and classifications, to avoid conflicting copies.
- Coverage across the whole estate is worth more than rich detail on one platform.
- Agents now read descriptions and definitions directly, so errors in metadata become errors in automated answers and actions.

# Questions to ask

- How do people find and judge data today, and how long does it take?
- Which metadata do regulators or auditors require, such as lineage, ownership or classifications?
- How many platforms and tools must be covered?
- Who will own and maintain descriptions and definitions?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Active metadata](active-metadata.md), [AI context layer](ai-context-layer.md), [Data catalogue](data-catalogue.md), [Data lineage](data-lineage.md), [Metadata interoperability](metadata-interoperability.md), [Schema registry](schema-registry.md) |
| Related | [Data quality and observability](../data-quality/data-quality.md), [Governance and compliance](../governance/governance.md), [Data products](../data-products/data-products.md), [Semantic layer](../analytics-bi/semantic-layer.md), [Table catalogue](../storage/table-catalogue.md) |

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 135 technologies; see their pages.
