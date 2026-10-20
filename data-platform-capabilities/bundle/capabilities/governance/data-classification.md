---
type: Capability
id: data-classification
title: Data classification
description: Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
aliases: [sensitive data discovery, PII detection, tagging]
broader: [governance, data-catalogue]
related:
- data-security-posture
- attribute-based-access
- column-lineage
- data-loss-prevention
- active-metadata
depends_on: [metadata-harvesting, data-profiling]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Classification attaches labels that say what data is and how sensitive it is, such as `personal`, `health`, `payment card`, `confidential` or `public`. Labels go on tables, columns and sometimes files or documents. People set them by hand, rules set them from names and patterns (a column called `iban`, or values that pass a card-number checksum), and machine-learning classifiers set them by sampling content. Labels then drive policies, masking, retention and data loss prevention, and propagate through lineage to derived tables.

Most other controls take classification as their input, so its coverage and accuracy limit everything downstream. A scheme usually combines a sensitivity level with data types, kept small enough that people apply it consistently. Automated scanning finds sensitive data at scale but produces false positives and misses context, such as a harmless-looking column that becomes identifying when joined to another. Classification differs from data security posture management, which combines classification results with access and configuration data to find risk.

# Key considerations

- Keep the taxonomy short and tie each label to concrete handling rules. Labels that change nothing about how data is treated are not maintained.
- Plan for review of automated suggestions. Decide which confidence levels apply tags directly and which need a steward to confirm.
- Propagate labels through lineage so derived tables inherit them, with a controlled way to remove a label when a transformation genuinely removes the sensitive content.
- Rescan regularly. New columns, schema changes and new files arrive unlabelled.
- Documents, chat logs and free-text fields need content inspection, not only rules on column names.

# Questions to ask

- Which classification scheme does the organisation already use, and is it applied to data or only to documents?
- What share of tables and columns holding personal or regulated data is labelled today?
- Should labels be applied automatically, or approved by a steward first?
- Which controls must change behaviour when a label is added?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Governance and compliance](governance.md), [Data catalogue](../metadata/data-catalogue.md) |
| Related | [Security and access](../security/security.md), [Access control](../security/access-control.md), [Active metadata](../metadata/active-metadata.md), [AI guardrails](../generative-ai/ai-guardrails.md), [AI-generated documentation](../metadata/ai-generated-documentation.md), [Analytical sandboxes](../analytics-bi/analytical-sandboxes.md), [Attribute- and tag-based access control](../security/attribute-based-access.md), [Bias and fairness assessment](../machine-learning/fairness-assessment.md), [Column security and dynamic masking](../security/column-masking.md), [Column-level lineage](../metadata/column-lineage.md), [Data loss prevention](../security/data-loss-prevention.md), [Data profiling](../data-quality/data-profiling.md), [Data security posture management](../security/data-security-posture.md), [Feature store](../machine-learning/feature-store.md), [Permission-aware retrieval](../generative-ai/permission-aware-retrieval.md), [Privacy impact assessment](privacy-impact-assessment.md), [Privacy management](privacy-management.md), [Records of processing](records-of-processing.md), [Semi-structured data](../storage/semi-structured-data.md), [Stewardship workflows](stewardship-workflows.md), [Unstructured data management](../specialised-data/unstructured-data.md), [Unstructured data quality](../data-quality/unstructured-data-quality.md) |
| Depends on | [Metadata harvesting](../metadata/metadata-harvesting.md), [Data profiling](../data-quality/data-profiling.md) |
| Needed by | [Attribute- and tag-based access control](../security/attribute-based-access.md), [Column security and dynamic masking](../security/column-masking.md), [Data breach response](../security/data-breach-response.md), [Data loss prevention](../security/data-loss-prevention.md), [Data residency and sovereignty](data-residency.md), [Data security posture management](../security/data-security-posture.md), [Data subject requests](data-subject-requests.md), [De-identification](deidentification.md), [Policy management](data-policy-management.md), [Privacy impact assessment](privacy-impact-assessment.md), [Privacy management](privacy-management.md), [Records of processing](records-of-processing.md), [Retention and disposal](data-retention.md), [Test data management](../development-lifecycle/test-data-management.md) |

# Where it appears

- **Use cases:** [Customer 360](../../use-cases/usecase-customer-360.md) (requires, level 3) · [Knowledge assistant](../../use-cases/usecase-rag-assistant.md) (benefits from) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (requires, level 3) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 4)
- **Patterns:** [Data fabric](../../patterns/data-fabric.md) · [Shift-left data quality and governance](../../patterns/shift-left.md)
- **Personas:** [Chief data officer](../../personas/persona-cdo.md) · [Data architect](../../personas/persona-data-architect.md) · [Data steward](../../personas/persona-data-steward.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Governance operating model](../../maturity/track-governance.md) (from level 2, Managed)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 1 Data Control Compliance (Governance and accountability); 6 Classification (Cataloguing and classification); 10 Data Privacy Impact Assessments (Protection and privacy) · [DAMA-DMBOK 2](../../frameworks/framework-dama-dmbok.md): Data Security · [Data mesh principles](../../frameworks/framework-data-mesh.md): Federated computational governance · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Article 8 – Identification; Chapter VI – Information-sharing arrangements (Article 45) · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(c) – Data minimisation; Article 9 – Special categories of personal data; Article 15 – Right of access; Article 25 – Data protection by design and by default; Article 30 – Records of processing activities; Articles 33 and 34 – Personal data breach notification; Article 35 – Data protection impact assessment · [Open Data Contract Standard (ODCS)](../../frameworks/framework-bitol-odcs.md): Schema; Tags

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | Amazon Macie sensitive data discovery | [Amazon Comprehend](../../technologies/aws/aws-comprehend.md), [Amazon Macie](../../technologies/aws/aws-macie.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | Sensitivity labels and classifications | [Microsoft Purview Data Map](../../technologies/microsoft/purview-data-map.md), [Microsoft Purview Information Protection](../../technologies/microsoft/purview-information-protection.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) |  | [BigQuery policy tags](../../technologies/google-cloud/gcp-bigquery-policy-tags.md), [Google Cloud Sensitive Data Protection](../../technologies/google-cloud/gcp-sensitive-data-protection.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Intent-Driven Governance](../../technologies/snowflake/snowflake-intent-driven-governance.md) (preview), [Snowflake object tagging](../../technologies/snowflake/snowflake-object-tagging.md), [Snowflake sensitive data classification](../../technologies/snowflake/snowflake-sensitive-data-classification.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks Data Classification](../../technologies/databricks/databricks-data-classification.md), [Databricks governed tags](../../technologies/databricks/databricks-governed-tags.md) |
| [Informatica](../../platforms/platform-informatica.md) |  | [Informatica Cloud Data Governance and Catalog (CDGC)](../../technologies/informatica/informatica-cloud-data-governance-and-catalog.md), [Informatica Unstructured Data Governance](../../technologies/informatica/informatica-unstructured-data-governance.md) (preview) |
| [Cloudera](../../platforms/platform-cloudera.md) |  | [Cloudera Data Catalog](../../technologies/cloudera/cloudera-data-catalog.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM Guardium Data Security Center](../../technologies/ibm/ibm-guardium-data-security-center.md), [IBM watsonx.data intelligence](../../technologies/ibm/ibm-watsonx-data-intelligence.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Sensitive Data Scanner and Cipher](../../technologies/palantir/palantir-sensitive-data-scanner-cipher.md) |
| [SAS](../../platforms/platform-sas.md) |  | [SAS Data Governance](../../technologies/sas/sas-data-governance.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Apache Atlas](../../technologies/open-source/apache-atlas.md), [Microsoft Presidio](../../technologies/open-source/presidio.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Bigeye AI Trust Platform](../../technologies/independent/bigeye.md), [BigID Next](../../technologies/independent/bigid-next.md), [Collibra Data Catalog](../../technologies/independent/collibra-data-catalog.md), [Cyera DSPM](../../technologies/independent/cyera-dspm.md), [Privacera](../../technologies/independent/privacera.md), [Protegrity Data Security Platform](../../technologies/independent/protegrity-data-security-platform.md), [Varonis Data Security Platform](../../technologies/independent/varonis-data-security-platform.md) |
