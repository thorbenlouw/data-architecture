---
type: Maturity Track
id: track-specialised-data
title: Specialised data
description: How well the organisation stores, governs and analyses data that needs specialised types, indexes or engines, such as time series, location, graphs, searchable text, media, logs and bitemporal history.
covers:
- specialised-data
- time-series-data
- geospatial-data
- full-text-search
- observability-analytics
- unstructured-data
- graph-data
- temporal-data
- document-processing
- audio-video-processing
- knowledge-graphs
related_tracks: [track-storage, track-genai, track-real-time]
levels:
- level: 1
  name: Initial
  summary: Specialised data is squeezed into ordinary tables as text or kept in stores that individual projects chose and run.
  criteria:
  - Coordinates, sensor readings and documents are held as text or loose files, and each script or report parses them in its own way.
  - Projects that need search, spatial, graph or time-series features run their own databases outside the platform's catalogue and access control.
  - Documents, images and recordings sit on file shares with no record of what they contain, who owns them or who may use them.
  - Corrections overwrite earlier values, so a report cannot be reproduced as it was first published.
  capabilities: []
- level: 2
  name: Managed
  summary: Teams use native types, indexes or engines for the specialised data their use case needs.
  criteria:
  - Sensor, meter and metric readings are stored in a time-series engine or in tables partitioned by time, with downsampling and retention set per series.
  - Location data uses native spatial types and indexes, and spatial joins run in the engine rather than in desktop mapping tools.
  - Text that users search, such as product descriptions or case notes, is held in a full-text index with relevance ranking instead of being matched with LIKE queries.
  - Application and infrastructure logs, metrics and traces are collected into a store that supports search, dashboards and alerts, with a retention period set for each.
  capabilities: [time-series-data, geospatial-data, full-text-search, observability-analytics]
- level: 3
  name: Defined
  summary: Each specialised type has a supported engine, and its data is catalogued and governed like the rest of the platform.
  criteria:
  - A written guide names the supported engine, extension or format for each specialised data type, and any other choice needs an approved exception.
  - Documents, images, audio and video are stored in governed volumes or tables with metadata, classification and the same access controls as structured data.
  - Connected data, such as networks of customers, accounts and devices, is held as nodes and relationships and queried with a graph query language instead of repeated self-joins.
  - Tables behind regulated or audited reports record both when each fact was true and when it was recorded, so any past report can be reproduced as first published and as since corrected.
  - Specialised stores are registered in the catalogue, and their lineage connects to the pipelines that feed them.
  capabilities: [unstructured-data, graph-data, temporal-data]
- level: 4
  name: Measured
  summary: Specialised workloads have performance and quality targets, and content in documents and media is extracted at scale with measured accuracy.
  criteria:
  - Each specialised workload, such as spatial joins, search queries or time-series dashboards, has a latency target, and results against it are reported.
  - Text, tables and fields are extracted from documents, and speech from audio and video, in pipelines whose accuracy is measured on a reviewed sample.
  - Search relevance is measured against a set of judged queries, and a change to text analysis or ranking that lowers the score is not released.
  - A knowledge graph with a maintained ontology links key business entities across sources, and checks for missing or contradictory relationships run on every load.
  capabilities: [document-processing, audio-video-processing, knowledge-graphs]
- level: 5
  name: Optimising
  summary: Engines, retention and ranking for specialised data are tuned from usage, and the knowledge graph grounds AI answers and search.
  criteria:
  - Retention and downsampling for time-series and observability data are set from how far back queries actually reach and what the storage costs.
  - AI assistants and search use the knowledge graph to resolve entities and relationships, and answer accuracy is measured against reference questions with and without it.
  - Relevance ranking is tuned from what users click and how they rephrase searches, and each change is checked against the judged queries.
  - Stand-alone specialised stores are moved onto platform engines when benchmarks show these meet the workload's target, and the number of separate stores is tracked.
  capabilities: []
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Moving up brings time series, location data, graphs, searchable text, documents and media, and logs and traces out of stand-alone stores that each project runs and into supported engines under the platform's catalogue, access control and lineage, with performance, quality and retention managed against targets. The types differ, so assess only those the use cases need: an organisation with no graph use case is not held back by having no graph store. Typical blockers are specialist databases bought for one project and never integrated, documents and recordings held on file shares with no classification, and corrections that overwrite history in tables that regulated reports depend on.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Levels

## Level 1: Initial

Specialised data is squeezed into ordinary tables as text or kept in stores that individual projects chose and run.

- Coordinates, sensor readings and documents are held as text or loose files, and each script or report parses them in its own way.
- Projects that need search, spatial, graph or time-series features run their own databases outside the platform's catalogue and access control.
- Documents, images and recordings sit on file shares with no record of what they contain, who owns them or who may use them.
- Corrections overwrite earlier values, so a report cannot be reproduced as it was first published.

## Level 2: Managed

Teams use native types, indexes or engines for the specialised data their use case needs.

- Sensor, meter and metric readings are stored in a time-series engine or in tables partitioned by time, with downsampling and retention set per series.
- Location data uses native spatial types and indexes, and spatial joins run in the engine rather than in desktop mapping tools.
- Text that users search, such as product descriptions or case notes, is held in a full-text index with relevance ranking instead of being matched with LIKE queries.
- Application and infrastructure logs, metrics and traces are collected into a store that supports search, dashboards and alerts, with a retention period set for each.

**Capabilities first relied on:** [Time-series data](../capabilities/specialised-data/time-series-data.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md)

## Level 3: Defined

Each specialised type has a supported engine, and its data is catalogued and governed like the rest of the platform.

- A written guide names the supported engine, extension or format for each specialised data type, and any other choice needs an approved exception.
- Documents, images, audio and video are stored in governed volumes or tables with metadata, classification and the same access controls as structured data.
- Connected data, such as networks of customers, accounts and devices, is held as nodes and relationships and queried with a graph query language instead of repeated self-joins.
- Tables behind regulated or audited reports record both when each fact was true and when it was recorded, so any past report can be reproduced as first published and as since corrected.
- Specialised stores are registered in the catalogue, and their lineage connects to the pipelines that feed them.

**Capabilities first relied on:** [Unstructured data management](../capabilities/specialised-data/unstructured-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md)

## Level 4: Measured

Specialised workloads have performance and quality targets, and content in documents and media is extracted at scale with measured accuracy.

- Each specialised workload, such as spatial joins, search queries or time-series dashboards, has a latency target, and results against it are reported.
- Text, tables and fields are extracted from documents, and speech from audio and video, in pipelines whose accuracy is measured on a reviewed sample.
- Search relevance is measured against a set of judged queries, and a change to text analysis or ranking that lowers the score is not released.
- A knowledge graph with a maintained ontology links key business entities across sources, and checks for missing or contradictory relationships run on every load.

**Capabilities first relied on:** [Document processing](../capabilities/processing/document-processing.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md)

## Level 5: Optimising

Engines, retention and ranking for specialised data are tuned from usage, and the knowledge graph grounds AI answers and search.

- Retention and downsampling for time-series and observability data are set from how far back queries actually reach and what the storage costs.
- AI assistants and search use the knowledge graph to resolve entities and relationships, and answer accuracy is measured against reference questions with and without it.
- Relevance ranking is tuned from what users click and how they rephrase searches, and each change is checked against the judged queries.
- Stand-alone specialised stores are moved onto platform engines when benchmarks show these meet the workload's target, and the number of separate stores is tracked.

# Capabilities in scope

[Specialised data types](../capabilities/specialised-data/specialised-data.md), [Audio and video processing](../capabilities/specialised-data/audio-video-processing.md), [Bitemporal data](../capabilities/specialised-data/temporal-data.md), [Document processing](../capabilities/processing/document-processing.md), [Full-text search](../capabilities/specialised-data/full-text-search.md), [Geospatial data](../capabilities/specialised-data/geospatial-data.md), [Graph data](../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../capabilities/specialised-data/knowledge-graphs.md), [Observability data analytics](../capabilities/specialised-data/observability-analytics.md), [Time-series data](../capabilities/specialised-data/time-series-data.md), [Unstructured data management](../capabilities/specialised-data/unstructured-data.md)

# Related tracks

- [Storage and table management](track-storage.md): How well data is kept in durable, open, maintained tables that many engines can read, update and trust.
- [Generative AI](track-genai.md): How safely and reliably the organisation builds, evaluates and runs applications that use language models and agents with its own data.
- [Real-time and streaming](track-real-time.md): How well the organisation moves, processes and queries data continuously, with predictable latency and correct results, instead of in scheduled batches.

Levels follow the shared [maturity scale](maturity-scale.md).
