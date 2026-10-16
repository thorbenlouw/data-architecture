---
type: Capability
id: cross-system-lineage
title: End-to-end lineage
description: Stitch lineage across ingestion tools, platforms and BI tools into one connected view.
aliases: [cross-platform lineage, report lineage, OpenLineage]
broader: [data-lineage]
related: [semantic-layer, reverse-etl, impact-analysis, column-lineage]
depends_on: [metadata-harvesting, metadata-interoperability]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

End-to-end lineage joins the graphs produced by different tools, from source applications through ingestion, change data capture, streaming, transformation and the warehouse to BI and reverse ETL. It works by matching the same dataset across tools through shared identifiers or naming rules. For example, a wrong figure on a sales dashboard is traced back through the BI semantic model, two warehouse models and an ingestion connector to a single field in the CRM.

Investigations usually begin at the edges, in a report or a source system, so lineage confined to one platform often stops just short of the answer. Common approaches are a central catalogue with connectors for each tool, tools emitting events in a shared format such as OpenLineage to one collector, and lineage registered manually or by API for systems that expose nothing. The hardest part is recognising the same table under different names in each tool, because of hostnames, aliases or letter case.

# Key considerations

- Agree a naming scheme for datasets across tools so edges join up. OpenLineage defines namespaces and names for this purpose.
- Spreadsheets, scripts and legacy ETL will need lineage registered by hand or by API. Mark it as such so users know it may be incomplete.
- Decide which tool holds the combined graph, or you end up with several partial ones.
- Wrong matches create false edges. Have owners confirm the lineage of critical paths.

# Questions to ask

- Which tools sit between source systems and reports today?
- Where do investigations most often lose the trail?
- Which tools can emit lineage in an open format?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data lineage](data-lineage.md) |
| Related | [Ingestion and integration](../ingestion-integration/ingestion-integration.md), [Column-level lineage](column-lineage.md), [Impact analysis](impact-analysis.md), [Metadata interoperability](metadata-interoperability.md), [Reverse ETL](../serving/reverse-etl.md), [Semantic layer](../analytics-bi/semantic-layer.md) |
| Depends on | [Metadata harvesting](metadata-harvesting.md), [Metadata interoperability](metadata-interoperability.md) |

# Where it appears

- **Use cases:** [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 2) · [Regulatory reporting](../../use-cases/usecase-regulatory-reporting.md) (requires, level 3)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md)
- **Personas:** [Risk and compliance officer](../../personas/persona-risk-compliance.md)
- **Maturity tracks:** [Lineage](../../maturity/track-lineage.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 12 – Review · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 4 Data Sovereignty and Cross-Border Movement (Governance and accountability); 13 Data Lineage (Data and technical architecture) · [Data mesh principles](../../frameworks/framework-data-mesh.md): Self-serve platform – mesh supervision plane · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 8 – Identification

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog data lineage](../../technologies/aws/aws-sagemaker-catalog-lineage.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Data lineage in Microsoft Purview](../../technologies/microsoft/purview-lineage.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog data lineage](../../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake external lineage](../../technologies/snowflake/snowflake-external-lineage.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Unity Catalog data lineage](../../technologies/databricks/databricks-unity-catalog-lineage.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica CDGC lineage](../../technologies/informatica/informatica-cdgc-lineage.md), [Informatica Data 360 Connector and Scanner](../../technologies/informatica/informatica-data-360-connector-and-scanner.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Lineage](../../technologies/cloudera/cloudera-data-lineage.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Manta Data Lineage](../../technologies/ibm/ibm-manta-data-lineage.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [OpenLineage](../../technologies/open-source/openlineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Bigeye AI Trust Platform](../../technologies/independent/bigeye.md), [Collibra Data Lineage](../../technologies/independent/collibra-data-lineage.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [Secoda](../../technologies/independent/secoda.md), [Sifflet](../../technologies/independent/sifflet.md), [Solidatus](../../technologies/independent/solidatus.md) |
