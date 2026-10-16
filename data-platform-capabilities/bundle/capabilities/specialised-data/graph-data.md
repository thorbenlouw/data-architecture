---
type: Capability
id: graph-data
title: Graph data
description: Model and query connected data as nodes and relationships.
aliases: [graph database]
broader: [specialised-data]
related:
- entity-resolution
- hierarchy-management
- low-latency-serving
- feature-engineering
- retrieval-augmented-generation
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Data is modelled as nodes, such as customers, accounts and devices, joined by edges, such as owns, pays or logged in from, each with properties. Graph query languages such as Cypher, the ISO standard GQL and SQL/PGQ express patterns and paths directly: "find accounts within three transfers of a known fraudulent account". Graph databases store links so a query can follow them without repeated joins, and graph algorithms such as shortest path, centrality and community detection run across the whole network.

Graphs suit problems where relationships are the point: fraud rings, supply chain dependencies, IT and network topology, identity resolution and recommendations. In relational tables, multi-hop questions become chains of self-joins whose cost rises steeply with depth. Options range from graph queries and algorithms over existing tables, through dedicated property graph databases, to RDF stores used for knowledge graphs. Whole-graph analytics in batch and fast traversals for live applications often need different engines.

# Key considerations

- Work out whether the main need is pattern queries, whole-graph algorithms or real-time traversal. Each favours different engines.
- Nodes with huge numbers of links, such as a phone number shared by thousands of accounts, can make traversals explode. Plan for them.
- A separate graph database must be kept in step with source tables, which adds pipelines and delay.
- Graph query languages are less widely known than SQL. Consider skills and tool support.

# Questions to ask

- Which questions involve following relationships across more than two or three hops?
- How many nodes and edges are there, and how fast do they change?
- Do results serve batch analysis or live applications such as fraud checks?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Specialised data types](specialised-data.md) |
| Narrower | [Knowledge graphs](knowledge-graphs.md) |
| Related | [Entity resolution](../master-data/entity-resolution.md), [Feature engineering](../machine-learning/feature-engineering.md), [Hierarchy management](../master-data/hierarchy-management.md), [Low-latency serving](../serving/low-latency-serving.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (benefits from) · [Real-time fraud detection](../../use-cases/usecase-fraud-detection.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 3, Defined)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Neptune](../../technologies/aws/aws-neptune.md), [Amazon Neptune Analytics](../../technologies/aws/aws-neptune-analytics.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Graph in Microsoft Fabric](../../technologies/microsoft/fabric-graph.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Graph](../../technologies/google-cloud/gcp-bigquery-graph.md), [Spanner](../../technologies/google-cloud/gcp-spanner.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle AI Database 26ai](../../technologies/oracle/oracle-ai-database-26ai.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud](../../technologies/sap/sap-hana-cloud.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Neo4j Aura](../../technologies/independent/neo4j-aura.md) |

Narrower capabilities are realised by a further 8 technologies; see their pages.
