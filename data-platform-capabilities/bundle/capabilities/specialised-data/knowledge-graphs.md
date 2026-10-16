---
type: Capability
id: knowledge-graphs
title: Knowledge graphs
description: Represent entities and their meaning in a graph with an ontology, for integration, search and grounding AI.
aliases: [semantic graph, ontology]
broader: [graph-data]
related:
- business-glossary
- ai-context-layer
- retrieval-augmented-generation
- semantic-layer
- master-data-management
depends_on: [entity-resolution]
tags: [specialised-data]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A knowledge graph stores facts as connected entities and gives them agreed meaning through an ontology: a formal model of classes, properties and rules, such as "a drug treats a condition" or "every subsidiary has exactly one parent company". W3C standards describe the model and data (RDF, OWL and SKOS), query them (SPARQL) and validate them (SHACL). Each entity has a stable identifier that every source can refer to, so facts about the same customer or product from several systems combine in one place.

Knowledge graphs integrate data across silos by meaning rather than table structure, support semantic search and recommendations, and increasingly ground AI by giving models and agents verified entities and relationships to retrieve and reason over. They need modelling effort and continuing curation, and pay back through reuse across many uses. A plain graph database stores connected data without a shared formal model; a business glossary defines terms for people rather than for machines.

# Key considerations

- Reuse published ontologies and industry vocabularies where they exist rather than modelling everything from scratch.
- Ontology design needs domain experts and ongoing stewardship. Without them the model goes stale.
- Choose between RDF and property graph approaches early. Tools, query languages and skills differ.
- Populate and update the graph from governed sources through pipelines, not by hand, so it stays current.

# Questions to ask

- Which questions require combining facts about the same entities from many systems?
- Is there an existing ontology or industry standard for your domain?
- Will AI applications retrieve from the graph, and how will their answers be evaluated?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Specialised data types](specialised-data.md) |
| Broader | [Graph data](graph-data.md) |
| Related | [Generative AI](../generative-ai/generative-ai.md), [AI context layer](../metadata/ai-context-layer.md), [Business glossary](../metadata/business-glossary.md), [Master data management](../master-data/master-data-management.md), [Retrieval-augmented generation](../generative-ai/retrieval-augmented-generation.md), [Semantic layer](../analytics-bi/semantic-layer.md), [Vector search](../generative-ai/vector-search.md) |
| Depends on | [Entity resolution](../master-data/entity-resolution.md) |

# Where it appears

- **Use cases:** [IoT predictive maintenance](../../use-cases/usecase-iot-predictive-maintenance.md) (benefits from) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md)
- **Maturity tracks:** [Specialised data](../../maturity/track-specialised-data.md) (from level 4, Measured)

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Neptune](../../technologies/aws/aws-neptune.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Ontology (Fabric IQ) | [Fabric IQ ontology](../../technologies/microsoft/fabric-iq-ontology.md) (preview) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery Graph](../../technologies/google-cloud/gcp-bigquery-graph.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP HANA Cloud knowledge graph engine](../../technologies/sap/sap-hana-cloud-knowledge-graph-engine.md), [SAP Knowledge Graph](../../technologies/sap/sap-knowledge-graph.md) |
| [Palantir](../../platforms/platform-palantir.md) | Ontology | [Palantir Ontology](../../technologies/palantir/palantir-ontology.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [data.world](../../technologies/independent/data-world.md), [Neo4j Aura](../../technologies/independent/neo4j-aura.md) |
