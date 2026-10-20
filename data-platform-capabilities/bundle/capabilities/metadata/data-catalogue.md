---
type: Capability
id: data-catalogue
title: Data catalogue
description: Provide a searchable inventory of data assets with descriptions, owners, quality and usage.
aliases: [data catalog, data discovery]
broader: [metadata]
related: [table-catalogue, data-domains, access-requests, data-marketplace, data-ownership]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A catalogue lists datasets, tables, dashboards, models, pipelines and other assets in one searchable place. Each asset has a page showing its schema, description, owner, classification, quality status, lineage and usage. People search by keyword or browse by domain, and the page links to where they can request access or open the data. For example, an analyst searching for churn finds a certified churn table, its owner, the dashboard built on it and a note that an older copy is deprecated.

It cuts the time spent finding and checking data and is the main workspace for stewardship and classification. Catalogues come built into data platforms, often merged with the table catalogue and permissions; as independent products covering many systems; and as open-source projects. They are increasingly also an interface for AI agents, which query them through APIs or MCP. The table catalogue lets engines resolve table names to storage; the data catalogue helps people and agents decide what to use and whether to trust it.

# Key considerations

- A catalogue that covers only one platform sends users elsewhere to search. Plan coverage of BI, ingestion and ML tools from the start.
- Search relevance depends on usage and certification signals, not only text matching.
- Assign owners for descriptions. A catalogue full of empty pages loses its users quickly.
- Link access requests from asset pages so finding data leads directly to using it.
- Check that permissions shown in the catalogue match what the engines actually enforce.

# Questions to ask

- How many systems and assets must be catalogued?
- Who are the main users: engineers, analysts, stewards, business users or agents?
- Must the catalogue enforce access, or only describe it?
- How will descriptions be kept current?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Metadata and discovery](metadata.md) |
| Narrower | [AI-generated documentation](ai-generated-documentation.md), [Business glossary](business-glossary.md), [Data certification](data-certification.md), [Data classification](../governance/data-classification.md), [Data trust indicators](data-trust-indicators.md), [Event and API catalogue](event-api-catalogue.md), [Metadata harvesting](metadata-harvesting.md), [Usage and popularity metadata](usage-metadata.md) |
| Related | [Governance and compliance](../governance/governance.md), [Access requests and reviews](../security/access-requests.md), [Ad hoc analysis](../analytics-bi/ad-hoc-analysis.md), [Agent and tool registry](../generative-ai/agent-registry.md), [Catalogue federation](../storage/catalogue-federation.md), [Data consumer portal](../analytics-bi/data-consumer-portal.md), [Data domains](../governance/data-domains.md), [Data lineage](data-lineage.md), [Data marketplace](../data-sharing/data-marketplace.md), [Data product specification](../data-products/data-product-specification.md), [Data quality scorecards](../data-quality/data-quality-scorecards.md), [Feature store](../machine-learning/feature-store.md), [Governance coverage metrics](../governance/governance-metrics.md), [Ownership and stewardship](../governance/data-ownership.md), [Records of processing](../governance/records-of-processing.md), [Table catalogue](../storage/table-catalogue.md) |
| Needed by | [Governance and compliance](../governance/governance.md), [Data products](../data-products/data-products.md), [Active metadata](active-metadata.md), [AI context layer](ai-context-layer.md), [Data domains](../governance/data-domains.md), [Governance coverage metrics](../governance/governance-metrics.md), [Ownership and stewardship](../governance/data-ownership.md), [Records of processing](../governance/records-of-processing.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (benefits from) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (requires, level 3)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md) · [Data lake](../../patterns/data-lake.md) · [Data mesh](../../patterns/data-mesh.md)
- **Personas:** [Analytics engineer](../../personas/persona-analytics-engineer.md) · [Chief data officer](../../personas/persona-cdo.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data product owner](../../personas/persona-data-product-owner.md) · [Data scientist](../../personas/persona-data-scientist.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 2, Managed)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 9 – Clarity and usefulness · [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 2 Ownership Field (Governance and accountability); 3 Authoritative Data Sources and Provisioning Points (Governance and accountability); 5 Cataloguing (Cataloguing and classification) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Metadata Management · [Data mesh principles](../../frameworks/framework-data-mesh.md): Data as a product; Self-serve platform – mesh supervision plane · [DCAM v3](../../frameworks/framework-edm-dcam.md): 4 Business Data Knowledge · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 8 – Identification · [GDPR](../../frameworks/framework-gdpr.md): Article 15 – Right of access; Article 30 – Records of processing activities · [ISO/IEC 42001:2023](../../frameworks/framework-iso-iec-42001.md): Annex A.4 – Resources for AI systems; Annex A.7 – Data for AI systems · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Tags · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Management Ports; Synonyms

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon SageMaker Catalog (Amazon DataZone) | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | OneLake catalog (Fabric); Unified Catalog (Purview) | [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md), [OneLake catalog](../../technologies/microsoft/fabric-onelake-catalog.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Knowledge Catalog (formerly Dataplex Universal Catalog) | [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md), [Google Cloud Data Catalog](../../technologies/google-cloud/gcp-data-catalog.md) (deprecated) |
| [Snowflake](../../platforms/platform-snowflake.md) | Horizon Catalog (Catalog Explorer, Universal Search) | [Snowflake Horizon Catalog](../../technologies/snowflake/snowflake-horizon-catalog.md), [Snowflake Universal Search](../../technologies/snowflake/snowflake-universal-search.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Catalog Explorer](../../technologies/databricks/databricks-catalog-explorer.md), [Databricks Discover](../../technologies/databricks/databricks-discover.md) |
| [Informatica](../../platforms/platform-informatica.md) | Cloud Data Governance and Catalog (CDGC) | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Catalog](../../technologies/cloudera/cloudera-data-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Catalog](../../technologies/oracle/oracle-oci-data-catalog.md), [Oracle AI Data Platform](../../technologies/oracle/oracle-ai-data-platform.md), [Oracle Autonomous AI Database Catalog](../../technologies/oracle/oracle-autonomous-ai-database-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere catalog and Data Marketplace](../../technologies/sap/sap-datasphere-catalog.md) |
| [IBM](../../platforms/platform-ibm.md) | watsonx.data intelligence (Knowledge Catalog) | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [SAS](../../platforms/platform-sas.md) | SAS Data Governance | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Dataiku](../../platforms/platform-dataiku.md) |  | [Dataiku Catalog](../../technologies/dataiku/dataiku-catalog.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Atlas](../../technologies/open-source/apache-atlas.md), [Apache Gravitino](../../technologies/open-source/apache-gravitino.md), [DataHub](../../technologies/open-source/datahub.md), [OpenMetadata](../../technologies/open-source/openmetadata.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Alation Intelligence Operating System (AIOS)](../../technologies/independent/alation-aios.md), [Ataccama ONE](../../technologies/independent/ataccama-one.md), [Atlan](../../technologies/independent/atlan.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [data.world](../../technologies/independent/data-world.md), [DataHub Cloud](../../technologies/independent/datahub-cloud.md), [dbt Catalog](../../technologies/independent/dbt-catalog.md), [Precisely Data Integrity Suite](../../technologies/independent/precisely-data-integrity-suite.md), [Secoda](../../technologies/independent/secoda.md), [Select Star](../../technologies/independent/select-star.md), [Sifflet](../../technologies/independent/sifflet.md) |

Narrower capabilities are realised by a further 71 technologies; see their pages.
