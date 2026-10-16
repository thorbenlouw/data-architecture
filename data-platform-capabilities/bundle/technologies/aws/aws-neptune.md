---
type: Technology
id: aws-neptune
title: Amazon Neptune
description: Managed graph database for property graphs (Gremlin, openCypher) and RDF (SPARQL) with read replicas and global databases.
aliases: [Neptune Database]
platform: platform-aws
kind: managed-service
availability: ga
realises: [graph-data, knowledge-graphs]
resource: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Neptune Database handles transactional graph workloads; analytical algorithms and vector search over graphs belong in Neptune Analytics.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types) (primary): Model and query connected data as nodes and relationships.
- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Neptune

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Graph in Microsoft Fabric](../microsoft/fabric-graph.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md), [Spanner](../google-cloud/gcp-spanner.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud knowledge graph engine](../sap/sap-hana-cloud-knowledge-graph-engine.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Neo4j Aura](../independent/neo4j-aura.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
