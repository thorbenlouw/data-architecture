---
type: Technology
id: fabric-iq-ontology
title: Fabric IQ ontology
description: Defines business entity types, properties, relationships, rules and metrics and binds them to OneLake data, giving people and agents a shared business vocabulary.
platform: platform-microsoft
kind: feature
availability: preview
realises: [knowledge-graphs, semantic-layer, agent-tool-access, ai-context-layer]
resource: https://learn.microsoft.com/en-us/fabric/iq/ontology/overview
tags: [microsoft]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Part of the Fabric IQ workload, alongside Power BI semantic models, Graph, Planning, data agents and operations agents. A virtual layer that queries bound sources in place; metrics can come from DAX measures. Available as a knowledge source for Foundry IQ. The old ontology experience retires on 31 January 2027. Digital twin builder (preview) is a related item for operational assets.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) (Specialised data types) (primary): Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
- [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) (Analytics and BI): Define business entities, measures and relationships once so every tool calculates them the same way.
- [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md) (Generative AI): Give agents governed access to data and actions through tools and protocols such as MCP.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.

**Platform:** [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md)  
**Availability:** preview  
**Product family:** Fabric IQ

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Neptune](../aws/aws-neptune.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery Graph](../google-cloud/gcp-bigquery-graph.md) | [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Knowledge Graph](../sap/sap-knowledge-graph.md), [SAP HANA Cloud knowledge graph engine](../sap/sap-hana-cloud-knowledge-graph-engine.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Ontology](../palantir/palantir-ontology.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
| [Independent vendors](../../platforms/platform-independent.md) | [data.world](../independent/data-world.md), [Neo4j Aura](../independent/neo4j-aura.md), [AtScale](../independent/atscale.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Knowledge graphs](../../capabilities/specialised-data/knowledge-graphs.md), [Agent tool and data access](../../capabilities/generative-ai/agent-tool-access.md), [Semantic layer](../../capabilities/analytics-bi/semantic-layer.md) |
