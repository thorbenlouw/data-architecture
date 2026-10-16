---
type: Capability
id: deidentification
title: De-identification
description: Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
aliases:
- anonymisation
- anonymization
- pseudonymisation
- pseudonymization
- tokenisation
- tokenization
- PII redaction
- format-preserving encryption
broader: [privacy-management, security]
related:
- column-masking
- test-data-management
- synthetic-data
- privacy-enhancing-technologies
- data-clean-rooms
depends_on: [data-classification, secrets-management]
tags: [governance]
status: draft
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

De-identification transforms personal data so individuals are harder or impossible to identify. Pseudonymisation replaces identifiers with consistent substitutes, for example a keyed hash of the customer number, so records can still be joined but not read directly. Tokenisation swaps values for random tokens held in a secure vault, which allows authorised re-identification. Anonymisation goes further, using generalisation, suppression, aggregation or added noise so that nobody can reasonably identify a person, even with other data.

The distinction matters legally. Under the GDPR, pseudonymised data generally remains personal data, at least for anyone able to link it back, while properly anonymised data falls outside its scope. True anonymisation is hard: a combination of postcode, birth date and gender identifies many people, and detailed behavioural data resists it. De-identification serves analytics, test data, sharing and model training. It differs from dynamic masking, which hides values at query time and leaves stored data unchanged; de-identification changes the data itself, usually in a pipeline.

# Key considerations

- Unkeyed hashes of emails, phone numbers and other guessable identifiers can be reversed by hashing a list of candidates. Use keyed hashes or tokens and protect the key.
- Measure re-identification risk, for example with k-anonymity checks on combinations of quasi-identifiers, rather than assuming that removing names is enough.
- Hold the re-identification key or token vault under separate control from the de-identified data, with its own access review.
- Decide whether pseudonyms must be stable across datasets and over time. Stable pseudonyms allow joins but also make linkage easier.

# Questions to ask

- Which uses need data that can be re-identified, and which can work with fully anonymised data?
- Who would hold the keys or token vault, and who may re-identify records?
- Has anyone assessed re-identification risk for datasets currently treated as anonymous?
- Is de-identified data shared outside the organisation or used to train models?

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Relationships

| Relationship | Capabilities |
|---|---|
| Domain | [Governance and compliance](governance.md) |
| Broader | [Privacy management](privacy-management.md), [Security and access](../security/security.md) |
| Related | [AI guardrails](../generative-ai/ai-guardrails.md), [Audience building and activation](../serving/audience-activation.md), [Audio and video processing](../specialised-data/audio-video-processing.md), [Column security and dynamic masking](../security/column-masking.md), [Crypto-shredding](../security/crypto-shredding.md), [Data clean rooms](../data-sharing/data-clean-rooms.md), [Data labelling](../machine-learning/data-labelling.md), [Encryption](../security/encryption.md), [External data sharing](../data-sharing/external-data-sharing.md), [Geospatial data](../specialised-data/geospatial-data.md), [Privacy-enhancing technologies](privacy-enhancing-technologies.md), [Synthetic data generation](../development-lifecycle/synthetic-data.md), [Test data management](../development-lifecycle/test-data-management.md), [Zero-copy cloning](../storage/zero-copy-cloning.md) |
| Depends on | [Data classification](data-classification.md), [Secrets management](../security/secrets-management.md) |

# Where it appears

- **Use cases:** [Data sharing and monetisation](../../use-cases/usecase-data-monetisation.md) (requires, level 3) · [Document data extraction](../../use-cases/usecase-document-extraction.md) (benefits from) · [Marketing audience activation](../../use-cases/usecase-marketing-activation.md) (requires, level 2) · [Privacy rights handling](../../use-cases/usecase-privacy-rights.md) (benefits from) · [Security and log analytics](../../use-cases/usecase-security-log-analytics.md) (benefits from) · [Sensitive data protection](../../use-cases/usecase-sensitive-data-protection.md) (requires, level 2)
- **Patterns:** [ETL](../../patterns/etl.md)
- **Personas:** [Data scientist](../../personas/persona-data-scientist.md) · [Security and privacy officer](../../personas/persona-security-officer.md)
- **Maturity tracks:** [Privacy](../../maturity/track-privacy.md) (from level 2, Managed) · [Security and access control](../../maturity/track-security.md) (from level 3, Defined)
- **Frameworks:** [CDMC (Cloud Data Management Capabilities)](../../frameworks/framework-edm-cdmc.md): 9 Appropriate Security Controls (Protection and privacy) · [DORA (Digital Operational Resilience Act)](../../frameworks/framework-eu-dora.md): Chapter VI – Information-sharing arrangements (Article 45) · [EU AI Act](../../frameworks/framework-eu-ai-act.md): Article 4a – Special categories of personal data for bias detection · [EU Data Act](../../frameworks/framework-eu-data-act.md): Chapter V – Business-to-government access in exceptional need · [GDPR](../../frameworks/framework-gdpr.md): Article 5(1)(c) – Data minimisation; Article 5(1)(e) – Storage limitation; Article 9 – Special categories of personal data; Article 25 – Data protection by design and by default; Article 32 – Security of processing

# How platforms provide it

| Platform | Name used | Technologies |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) |  | [Amazon Bedrock Guardrails](../../technologies/aws/aws-bedrock-guardrails.md), [Amazon Comprehend](../../technologies/aws/aws-comprehend.md), [AWS Glue DataBrew](../../technologies/aws/aws-glue-databrew.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) |  | [Azure AI Language PII detection](../../technologies/microsoft/azure-ai-language-pii.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | Sensitive Data Protection de-identification | [BigQuery data masking](../../technologies/google-cloud/gcp-bigquery-data-masking.md), [Google Cloud Sensitive Data Protection](../../technologies/google-cloud/gcp-sensitive-data-protection.md) |
| [Snowflake](../../platforms/platform-snowflake.md) |  | [Snowflake Cortex AI Functions](../../technologies/snowflake/snowflake-cortex-ai-functions.md), [Snowflake masking policies](../../technologies/snowflake/snowflake-masking-policies.md) |
| [Databricks](../../platforms/platform-databricks.md) |  | [Databricks AI Functions](../../technologies/databricks/databricks-ai-functions.md) |
| [Informatica](../../platforms/platform-informatica.md) | data de-identification policies and Data Masking | [Informatica Cloud Data Access Management (CDAM)](../../technologies/informatica/informatica-cloud-data-access-management.md), [Informatica Data Masking transformation](../../technologies/informatica/informatica-data-masking-transformation.md), [Informatica Test Data Management (TDM)](../../technologies/informatica/informatica-test-data-management.md) |
| [Oracle](../../platforms/platform-oracle.md) |  | [Oracle Data Safe](../../technologies/oracle/oracle-data-safe.md) |
| [IBM](../../platforms/platform-ibm.md) |  | [IBM InfoSphere Optim](../../technologies/ibm/ibm-optim.md) |
| [Palantir](../../platforms/platform-palantir.md) |  | [Palantir Sensitive Data Scanner and Cipher](../../technologies/palantir/palantir-sensitive-data-scanner-cipher.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) |  | [Microsoft Presidio](../../technologies/open-source/presidio.md) |
| [Independent vendors](../../platforms/platform-independent.md) |  | [Perforce Delphix](../../technologies/independent/perforce-delphix.md), [Protegrity Data Security Platform](../../technologies/independent/protegrity-data-security-platform.md), [Skyflow Data Privacy Vault](../../technologies/independent/skyflow-data-privacy-vault.md), [Tonic Structural](../../technologies/independent/tonic-structural.md), [Tonic Textual](../../technologies/independent/tonic-textual.md) |
