---
type: Technology
id: gcp-bigquery-graph
title: BigQuery Graph
description: Defines property graphs over existing BigQuery tables and queries them with ISO GQL, without copying data.
platform: platform-google-cloud
kind: feature
availability: ga
realises: [graph-data, knowledge-graphs]
resource: https://docs.cloud.google.com/bigquery/docs/graph-overview
tags: [google-cloud]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

GA August 2026; it shares its schema and query language with Spanner Graph. GQL requires Enterprise or Enterprise Plus reservations, and Google has announced that core graph processing will require those editions from 26 April 2027. The visual graph modeller is in preview.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types) (primary): Model and query connected data as nodes and relationships.
- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.

**Platform:** [Google Cloud](../../platforms/platform-google-cloud.md)  
**Availability:** ga  
**Product family:** BigQuery

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Neptune](../aws/aws-neptune.md), [Amazon Neptune Analytics](../aws/aws-neptune-analytics.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Graph in Microsoft Fabric](../microsoft/fabric-graph.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md), [SAP HANA Cloud knowledge graph engine](../sap/sap-hana-cloud-knowledge-graph-engine.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Neo4j Aura](../independent/neo4j-aura.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
