---
type: Technology
id: sap-knowledge-graph
title: SAP Knowledge Graph
description: SAP-managed graph of business entities, fields and relationships across SAP applications that gives Joule and custom agents business context.
platform: platform-sap
kind: saas
availability: ga
realises: [knowledge-graphs, semantic-layer, retrieval-augmented-generation, ai-context-layer]
resource: https://www.sap.com/products/artificial-intelligence/knowledge-graph.html
tags: [sap]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

SAP reports it maps over seven million data fields (October 2026). Part of the SAP Business AI Platform with BDC and Joule Studio.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types) (primary): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Retrieval-augmented generation](../../capabilities/generative-ai/retrieval-augmented-generation.md) (Generative AI): Ground model answers in your own content by retrieving relevant passages at query time.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [SAP](../../platforms/platform-sap.md)  
**Availability:** ga  
**Product family:** SAP Business AI Platform

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Neptune](../aws/aws-neptune.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Fabric IQ ontology](../microsoft/fabric-iq-ontology.md) (preview) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Neo4j Aura](../independent/neo4j-aura.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
