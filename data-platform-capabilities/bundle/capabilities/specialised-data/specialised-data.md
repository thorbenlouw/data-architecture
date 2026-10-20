---
type: Capability
id: specialised-data
title: Specialised data types
description: Store and analyse data types that need specialised models, functions or engines.
broader: []
related:
- sql-query-engine
- open-table-formats
- engine-interoperability
- data-skipping-indexes
- generative-ai
order: 20
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Some data does not fit naturally into rows and columns, or needs operations that general SQL engines handle poorly. Sensor readings need downsampling and gap filling; locations need distance and containment tests; networks of relationships need path traversal; text needs relevance ranking; images and audio need content extracted before they can be analysed. This domain covers the data types, functions, indexes and engines built for these cases.

The capabilities fall into three groups. Specialised structured data covers time series, geospatial, graphs and knowledge graphs, bitemporal and semi-structured data, increasingly handled inside a general platform through native types and functions. Content covers full-text search, unstructured data management, document processing and audio and video processing, which turn files into material that can be searched and analysed. Similarity search through vector search is shared with generative AI. Observability analytics combines several of these for logs, metrics and traces.

The recurring decision is whether to use native features of the main platform or a dedicated engine. Native support keeps one copy of the data, one security model and one catalogue, and is often enough. A dedicated engine is faster or more expressive for heavy workloads, such as deep graph traversal or sub-second search across billions of log lines, but adds copies, synchronisation and another system to govern.

# Key considerations

- Start from the queries, not the data type. Many geospatial and time-series needs are met by functions in the main engine.
- Every dedicated engine needs ingestion, security, backup and monitoring. Count that running cost before adding one.
- Keep one system of record and treat specialised stores as derived indexes that can be rebuilt from it.
- Check that specialised types survive the whole path, through file and table formats, connectors and BI tools.

# Questions to ask

- Which specialised query patterns do users run today, and how fast must they be?
- Can the main platform's native types and functions meet them, or are volume and complexity beyond it?
- How will data in a dedicated engine be kept consistent with the platform and governed the same way?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Narrower | [Bitemporal data](temporal-data.md), [Document processing](../processing/document-processing.md), [Full-text search](full-text-search.md), [Geospatial data](geospatial-data.md), [Graph data](graph-data.md), [Observability data analytics](observability-analytics.md), [Semi-structured data](../storage/semi-structured-data.md), [Time-series data](time-series-data.md), [Unstructured data management](unstructured-data.md), [Vector search](../generative-ai/vector-search.md) |
| Related | [Generative AI](../generative-ai/generative-ai.md), [Indexes and data skipping](../compute/data-skipping-indexes.md), [Multi-engine interoperability](../compute/engine-interoperability.md), [Open table formats](../storage/open-table-formats.md), [SQL query engine](../compute/sql-query-engine.md) |

# Where it appears

- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md)

# How platforms provide it

No technology in this bundle realises this capability directly yet.

Narrower capabilities are realised by a further 129 technologies; see their pages.
