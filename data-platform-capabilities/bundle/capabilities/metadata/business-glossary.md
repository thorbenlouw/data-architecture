---
type: Capability
id: business-glossary
title: Business glossary
description: Define business terms and link them to the data that represents them.
broader: [data-catalogue]
related: [semantic-layer, metric-definitions, critical-data-elements, knowledge-graphs, ai-context-layer]
depends_on: [data-ownership]
tags: [metadata]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

A glossary holds agreed definitions of business terms such as active customer, net revenue or churn. Each term has an owner, an approval status, synonyms and related terms, and links to the tables, columns, metrics and reports that represent it. Stewards move terms through draft, review and approval. For example, finance and marketing count active customers differently; the glossary records two distinctly named terms and links each to the column used to calculate it.

It bridges the language of the business and the names in the data. Glossaries range from flat lists of terms, through hierarchical taxonomies, to ontologies with formal relationships, often expressed in the W3C SKOS standard. Terms frequently drive classification and policy, for example marking every column linked to "national insurance number" as personal data. The semantic layer and metric definitions encode calculations that tools execute; the glossary records meaning and ownership in words. Linking glossary terms to metric definitions keeps the two consistent.

# Key considerations

- Start with terms that cause real disputes or regulatory exposure, not a complete dictionary.
- Where departments genuinely differ, record separate, distinctly named terms rather than forcing one definition nobody uses.
- Linking terms to physical columns is the costly part. AI suggestions speed it up but need review.
- Keep the glossary aligned with the semantic layer. Two independent sources of meaning will drift apart.

# Questions to ask

- Which business terms cause the most disputes or reporting errors?
- Who has the authority to approve a definition?
- Do regulations require documented definitions, for example for critical data elements?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Metadata and discovery](metadata.md) |
| Broader | [Data catalogue](data-catalogue.md) |
| Related | [AI context layer](ai-context-layer.md), [AI-generated documentation](ai-generated-documentation.md), [Critical data elements](../governance/critical-data-elements.md), [Data modelling and design](../development-lifecycle/data-modelling.md), [Governed metric definitions](../analytics-bi/metric-definitions.md), [Knowledge graphs](../specialised-data/knowledge-graphs.md), [Reference data management](../master-data/reference-data-management.md), [Semantic layer](../analytics-bi/semantic-layer.md), [Stewardship workflows](../governance/stewardship-workflows.md) |
| Depends on | [Ownership and stewardship](../governance/data-ownership.md) |

# Where it appears

- **Use cases:** [Conversational analytics for business users](../../use-cases/usecase-conversational-bi.md) (requires, level 2) · [Self-service BI](../../use-cases/usecase-self-service-bi.md) (benefits from)
- **Personas:** [Business user](../../personas/persona-business-user.md) · [Data analyst](../../personas/persona-data-analyst.md) · [Data steward](../../personas/persona-data-steward.md)
- **Maturity tracks:** [Metadata and catalogue](../../maturity/track-metadata-catalogue.md) (from level 3, Defined)
- **Frameworks:** [BCBS 239](../../frameworks/framework-bcbs-239.md): Principle 2 – Data architecture and IT infrastructure; Principle 3 – Accuracy and integrity; Principle 9 – Clarity and usefulness · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Metadata Management · [DCAM v3](../../frameworks/framework-edm-dcam.md): 4 Business Data Knowledge · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Authoritative Definitions · [Open Data Product Standard (ODPS)](../../frameworks/framework-bitol-odps.md): Authoritative Definitions; Synonyms

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon SageMaker Catalog](../../technologies/aws/aws-sagemaker-catalog.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Microsoft Purview Unified Catalog](../../technologies/microsoft/purview-unified-catalog.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [Knowledge Catalog](../../technologies/google-cloud/gcp-knowledge-catalog.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [OCI Data Catalog](../../technologies/oracle/oracle-oci-data-catalog.md) |
| [SAP](../../platforms/platform-sap.md) |  | [SAP Datasphere catalog and Data Marketplace](../../technologies/sap/sap-datasphere-catalog.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [DataHub](../../technologies/open-source/datahub.md), [OpenMetadata](../../technologies/open-source/openmetadata.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Collibra Data Governance](../../technologies/independent/collibra-data-governance.md), [data.world](../../technologies/independent/data-world.md) |
