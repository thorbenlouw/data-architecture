---
type: Technology
id: neo4j-aura
title: Neo4j Aura
description: Managed Neo4j graph database (AuraDB) with vector indexes, graph data science and on-demand graph analytics sessions.
aliases: [AuraDB, Neo4j AuraDB]
platform: platform-independent
vendor: Neo4j
kind: managed-service
availability: ga
realises: [graph-data, knowledge-graphs, vector-search]
resource: https://neo4j.com/docs/aura/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tiers are Free, Professional, Business Critical and Virtual Dedicated Cloud. Aura Graph Analytics runs Graph Data Science in temporary, isolated sessions over AuraDB, self-managed Neo4j or DataFrames. Virtual Graph is in public preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types) (primary): Model and query connected data as nodes and relationships.
- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Neptune](../aws/aws-neptune.md), [Amazon Neptune Analytics](../aws/aws-neptune-analytics.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Graph in Microsoft Fabric](../microsoft/fabric-graph.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md), [Spanner](../google-cloud/gcp-spanner.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
