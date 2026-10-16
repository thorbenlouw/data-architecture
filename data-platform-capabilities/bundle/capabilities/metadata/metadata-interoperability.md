---
type: Capability
id: metadata-interoperability
title: Metadata interoperability
description: Exchange metadata between tools through open APIs and standards.
aliases: [open metadata standards]
broader: [metadata]
related: [catalogue-federation, data-product-specification, cross-system-lineage, open-protocol-sharing]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Tools exchange schemas, lineage, definitions, classifications, ownership and quality results through documented APIs and shared formats rather than proprietary exports. Relevant standards include OpenLineage for run-time lineage events, the Apache Iceberg REST catalogue specification for table metadata, W3C DCAT for dataset catalogues, SKOS for vocabularies and the Open Data Contract Standard. For example, an orchestrator emits OpenLineage events that both the catalogue and the observability tool consume, so neither needs its own connector to the orchestrator.

Most organisations run several catalogues and governance tools. Interoperability avoids entering the same metadata twice, reduces lock-in and lets metadata outlive any single tool. Support for standards is uneven: lineage and table metadata are well covered, while glossary, policy and quality results are exchanged mostly through vendor APIs. MCP is also becoming a common way to expose metadata to AI agents. Catalogue federation presents tables from several catalogues through one; interoperability is the broader exchange of all kinds of metadata between tools.

# Key considerations

- Check what each tool actually exports and imports. Claiming support for a standard can mean only a subset of fields.
- Decide which tool masters each kind of metadata, and synchronise in one direction where possible.
- Mapping identifiers across tools, for datasets and for people, is most of the integration effort.
- Use event-based exchange for freshness and bulk export for migration and backup.

# Questions to ask

- How many tools hold metadata today, and do they disagree?
- Which open standards do current tools support in practice?
- Could you move your metadata to another catalogue if you replaced the current one?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md) |
| Narrower | [Semantic model interchange](../analytics-bi/semantic-model-interchange.md) |
| Related | [Catalogue federation](../storage/catalogue-federation.md), [Data lineage](data-lineage.md), [Data product specification](../data-products/data-product-specification.md), [End-to-end lineage](cross-system-lineage.md), [Metadata harvesting](metadata-harvesting.md), [Open-protocol sharing](../data-sharing/open-protocol-sharing.md) |
| Needed by | [Active metadata](active-metadata.md), [End-to-end lineage](cross-system-lineage.md) |

# Where it appears

- **Patterns:** [Data fabric](../../patterns/data-fabric.md)
- **Personas:** [Data architect](../../personas/persona-data-architect.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 4, Measured)
- **Frameworks:** [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Architecture; Metadata Management · [DCAM v3](../../frameworks/framework-edm-dcam.md): 3 Architecture – Business, Data & Technology · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter VIII – Interoperability · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Custom & Other Properties · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Custom & Other Properties

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog data lineage](../../technologies/aws/aws-sagemaker-catalog-lineage.md), [AWS Glue Data Catalog](../../technologies/aws/aws-glue-data-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Data Map](../../technologies/microsoft/purview-data-map.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Google Cloud Lakehouse runtime catalog](../../technologies/google-cloud/gcp-lakehouse-runtime-catalog.md), [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md), [Knowledge Catalog data lineage](../../technologies/google-cloud/gcp-knowledge-catalog-data-lineage.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake external lineage](../../technologies/snowflake/snowflake-external-lineage.md), [Snowflake Horizon Iceberg REST Catalog API](../../technologies/snowflake/snowflake-horizon-iceberg-rest-catalog.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks catalog federation](../../technologies/databricks/databricks-catalog-federation.md), [Unity Catalog Iceberg REST Catalog API](../../technologies/databricks/databricks-iceberg-rest-catalog.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Metadata Command Center (MCC)](../../technologies/informatica/informatica-metadata-command-center.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Iceberg REST Catalog](../../technologies/cloudera/cloudera-iceberg-rest-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Autonomous AI Database Catalog](../../technologies/oracle/oracle-autonomous-ai-database-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Business Data Cloud Connect](../../technologies/sap/sap-bdc-connect.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [Iceberg REST Catalog specification](../../technologies/open-source/apache-iceberg-rest-catalog-spec.md), [OpenLineage](../../technologies/open-source/openlineage.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Atlan](../../technologies/independent/atlan.md) |

Narrower capabilities are realised by a further 3 technologies; see their pages.
