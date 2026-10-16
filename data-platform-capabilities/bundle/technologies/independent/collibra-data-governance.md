---
type: Technology
id: collibra-data-governance
title: Collibra Data Governance
description: Governance workspace for business glossaries, ownership and stewardship roles, policies and the workflows that route approvals and issues to stewards.
platform: platform-independent
vendor: Collibra
kind: saas
availability: ga
realises:
- business-glossary
- data-ownership
- data-policy-management
- reference-data-management
- critical-data-elements
- records-of-processing
- privacy-impact-assessment
- data-domains
- ai-context-layer
- data-issue-management
- stewardship-workflows
resource: https://www.collibra.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

The operating model layer of Collibra. Its configurable metamodel and workflow engine are why large regulated organisations choose it, but they need dedicated administration. Critical data elements, reference data and data issues are managed here too. The Collibra Data Privacy module adds GDPR and CCPA process registers and privacy risk assessments linked to governed assets, but it does not fulfil data subject requests.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [Business glossary](../../capabilities/metadata/business-glossary.md) (Metadata and discovery) (primary): Define business terms and link them to the data that represents them.
- [Ownership and stewardship](../../capabilities/governance/data-ownership.md) (Governance and compliance): Assign accountable owners and stewards to data and record their responsibilities.
- [Policy management](../../capabilities/governance/data-policy-management.md) (Governance and compliance): Define data policies centrally and apply them consistently across platforms and tools.
- [Reference data management](../../capabilities/master-data/reference-data-management.md) (Master and reference data): Manage shared code lists and mappings, such as country codes and product categories, with versions and approvals.
- [Critical data elements](../../capabilities/governance/critical-data-elements.md) (Governance and compliance): Identify the data items that matter most for regulatory, risk and financial reporting and apply stricter controls to them.
- [Records of processing](../../capabilities/governance/records-of-processing.md) (Governance and compliance): Keep a register of personal data processing with purposes, categories, recipients and retention, linked to the data involved.
- [Privacy impact assessment](../../capabilities/governance/privacy-impact-assessment.md) (Governance and compliance): Trigger, carry out and record data protection impact assessments for high-risk processing, linked to the data and pipelines concerned.
- [Data domains](../../capabilities/governance/data-domains.md) (Governance and compliance): Group data assets, products and owners into business domains with their own stewardship and policies.
- [AI context layer](../../capabilities/metadata/ai-context-layer.md) (Metadata and discovery): Curate and serve business definitions, verified queries, relationships and usage guidance to AI agents so they interpret and use data correctly.
- [Data issue management](../../capabilities/data-quality/data-issue-management.md) (Data quality and observability): Log, assign, track and resolve data quality incidents with their owners.
- [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) (Governance and compliance): Route governance tasks such as term approvals, classification reviews, access approvals and match reviews to the right steward, with queues, deadlines, delegation and a record of each decision.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon SageMaker Catalog](../aws/aws-sagemaker-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Data domains](../../capabilities/governance/data-domains.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Microsoft Purview Unified Catalog](../microsoft/purview-unified-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Critical data elements](../../capabilities/governance/critical-data-elements.md), [Data domains](../../capabilities/governance/data-domains.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [Knowledge Catalog](../google-cloud/gcp-knowledge-catalog.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Cloud Data Governance and Catalog (CDGC)](../informatica/informatica-cloud-data-governance-and-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md), [Ownership and stewardship](../../capabilities/governance/data-ownership.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Oracle](../../platforms/platform-oracle.md) | [OCI Data Catalog](../oracle/oracle-oci-data-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md) |
| [SAP](../../platforms/platform-sap.md) | [SAP Datasphere catalog and Data Marketplace](../sap/sap-datasphere-catalog.md) | [Business glossary](../../capabilities/metadata/business-glossary.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM watsonx.data intelligence](../ibm/ibm-watsonx-data-intelligence.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Policy management](../../capabilities/governance/data-policy-management.md), [Stewardship workflows](../../capabilities/governance/stewardship-workflows.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [DataHub](../open-source/datahub.md), [OpenMetadata](../open-source/openmetadata.md) | [AI context layer](../../capabilities/metadata/ai-context-layer.md), [Business glossary](../../capabilities/metadata/business-glossary.md), [Data domains](../../capabilities/governance/data-domains.md) |
