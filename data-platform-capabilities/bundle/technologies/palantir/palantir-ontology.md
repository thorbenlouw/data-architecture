---
type: Technology
id: palantir-ontology
title: Palantir Ontology
description: Semantic and operational layer that maps datasets, virtual tables and models to business object types, properties and links, with action types and functions that write decisions back.
aliases: [Foundry Ontology, Ontology SDK, OSDK]
platform: platform-palantir
kind: feature
availability: ga
realises:
- knowledge-graphs
- semantic-layer
- data-apis
- operational-data-store
- low-latency-serving
- data-writeback
- ai-context-layer
resource: https://www.palantir.com/docs/foundry/ontology/overview/
tags: [palantir]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Objects are indexed in Palantir's object storage (Object Storage V2) for fast search and lookups. Action types capture edits and can call external systems; functions hold business logic in TypeScript or Python. The Ontology SDK (OSDK) generates typed Python, TypeScript and Java clients and REST APIs over object types. It is the main thing applications, AIP and external agents consume.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types) (primary): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Data APIs](../../capabilities/serving/data-apis.md) (Serving and activation): Expose datasets through managed REST or GraphQL APIs with authentication, paging and rate limits.
- [Operational data store](../../capabilities/serving/operational-data-store.md) (Serving and activation): Hold a current, integrated view of data from several operational systems for operational reporting and lookups.
- [Low-latency serving](../../capabilities/serving/low-latency-serving.md) (Serving and activation): Serve individual records or small result sets to applications in milliseconds.
- [Data entry and write-back](../../capabilities/analytics-bi/data-writeback.md) (Analytics and BI): Let users enter or correct data in analytics tools and write it back to governed tables with an audit trail.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Palantir](../../platforms/platform-palantir.md)  
**Availability:** ga  
**Product family:** Palantir Foundry

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Neptune](../aws/aws-neptune.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [SAP HANA Cloud knowledge graph engine](../sap/sap-hana-cloud-knowledge-graph-engine.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Neo4j Aura](../independent/neo4j-aura.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
