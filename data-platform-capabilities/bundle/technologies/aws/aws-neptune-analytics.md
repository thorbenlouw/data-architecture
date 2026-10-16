---
type: Technology
id: aws-neptune-analytics
title: Amazon Neptune Analytics
description: In-memory graph analytics engine that loads graphs from Neptune or S3 and runs graph algorithms, openCypher queries and vector similarity search.
platform: platform-aws
kind: managed-service
availability: ga
realises: [graph-data, vector-search]
resource: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html
tags: [aws]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Used by Bedrock Knowledge Bases for GraphRAG, combining graph traversal with vector retrieval.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Graph data](../../capabilities/specialised-data/graph-data.md) (Specialised data types) (primary): Model and query connected data as nodes and relationships.
- [Vector search](../../capabilities/generative-ai/vector-search.md) (Generative AI): Store embeddings and find the most similar items quickly.

**Platform:** [Amazon Web Services](../../platforms/platform-aws.md)  
**Availability:** ga  
**Product family:** Amazon Neptune

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Graph in Microsoft Fabric](../microsoft/fabric-graph.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md), [Spanner](../google-cloud/gcp-spanner.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [ClickHouse](../../platforms/platform-clickhouse.md) | [ClickHouse vector similarity indexes](../clickhouse/clickhouse-vector-search.md) | [Vector search](../../capabilities/generative-ai/vector-search.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle AI Database 26ai](../oracle/oracle-ai-database-26ai.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP HANA Cloud](../sap/sap-hana-cloud.md) | [Graph data](../../capabilities/specialised-data/graph-data.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [Neo4j Aura](../independent/neo4j-aura.md) | [Graph data](../../capabilities/specialised-data/graph-data.md), [Vector search](../../capabilities/generative-ai/vector-search.md) |
