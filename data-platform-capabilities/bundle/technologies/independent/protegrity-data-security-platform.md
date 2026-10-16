---
type: Technology
id: protegrity-data-security-platform
title: Protegrity Data Security Platform
description: Protects sensitive fields with vaultless tokenisation, encryption and masking applied consistently across databases, data platforms, applications and AI pipelines, with central policy.
aliases: [Protegrity]
platform: platform-independent
vendor: Protegrity
kind: software
availability: ga
realises: [deidentification, column-masking, encryption, data-classification, ai-guardrails]
resource: https://www.protegrity.com/
tags: [independent]
status: draft
stale_after: '2027-04-16T00:00:00Z'
generated: {by: claude/opus-5.5, at: '2026-10-16T12:00:00Z'}
---

Its protectors are installed in Snowflake, Databricks, Teradata, mainframes and so on, so tokens stay usable across systems. Semantic Guardrails and Protegrity AI Team Edition (2026) target LLM and agent pipelines. Common in banking and payments.

<!-- dpc:generated: everything below this line is rebuilt by `python tools/dpc.py build`; edit above it -->

# Realises

- [De-identification](../../capabilities/governance/deidentification.md) (Governance and compliance) (primary): Pseudonymise, tokenise or anonymise data so it can be used with less privacy risk.
- [Column security and dynamic masking](../../capabilities/security/column-masking.md) (Security and access): Hide or mask sensitive columns depending on who is querying.
- [Encryption](../../capabilities/security/encryption.md) (Security and access): Encrypt data at rest and in transit, with keys managed securely.
- [Data classification](../../capabilities/governance/data-classification.md) (Governance and compliance): Label data by sensitivity and type, such as personal, confidential or regulated, manually or automatically.
- [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md) (Generative AI): Check model inputs, outputs and agent tool calls against policy to block harmful content, data leakage, prompt injection and disallowed actions.

**Platform:** [Independent vendors](../../platforms/platform-independent.md)  
**Availability:** ga

# Equivalents on other platforms

The closest technologies on each other platform, ranked by how many of the same capabilities they realise.

| Platform | Technologies | Shared capabilities |
|---|---|---|
| [Amazon Web Services](../../platforms/platform-aws.md) | [Amazon Bedrock Guardrails](../aws/aws-bedrock-guardrails.md), [Amazon Comprehend](../aws/aws-comprehend.md), [AWS Glue DataBrew](../aws/aws-glue-databrew.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [De-identification](../../capabilities/governance/deidentification.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Microsoft Azure and Fabric](../../platforms/platform-microsoft.md) | [Azure AI Language PII detection](../microsoft/azure-ai-language-pii.md), [Microsoft Purview Information Protection](../microsoft/purview-information-protection.md) | [De-identification](../../capabilities/governance/deidentification.md), [Data classification](../../capabilities/governance/data-classification.md), [Encryption](../../capabilities/security/encryption.md) |
| [Google Cloud](../../platforms/platform-google-cloud.md) | [BigQuery data masking](../google-cloud/gcp-bigquery-data-masking.md), [Google Cloud Sensitive Data Protection](../google-cloud/gcp-sensitive-data-protection.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md), [Data classification](../../capabilities/governance/data-classification.md) |
| [Snowflake](../../platforms/platform-snowflake.md) | [Snowflake masking policies](../snowflake/snowflake-masking-policies.md), [Snowflake Cortex AI Functions](../snowflake/snowflake-cortex-ai-functions.md) | [Column security and dynamic masking](../../capabilities/security/column-masking.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [Databricks](../../platforms/platform-databricks.md) | [Databricks AI Functions](../databricks/databricks-ai-functions.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Informatica](../../platforms/platform-informatica.md) | [Informatica Data Masking transformation](../informatica/informatica-data-masking-transformation.md), [Informatica Test Data Management (TDM)](../informatica/informatica-test-data-management.md), [Informatica Cloud Data Access Management (CDAM)](../informatica/informatica-cloud-data-access-management.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Oracle](../../platforms/platform-oracle.md) | [Oracle Data Safe](../oracle/oracle-data-safe.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
| [IBM](../../platforms/platform-ibm.md) | [IBM InfoSphere Optim](../ibm/ibm-optim.md) | [De-identification](../../capabilities/governance/deidentification.md) |
| [Palantir](../../platforms/platform-palantir.md) | [Palantir Sensitive Data Scanner and Cipher](../palantir/palantir-sensitive-data-scanner-cipher.md) | [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md), [Encryption](../../capabilities/security/encryption.md) |
| [Open-source ecosystem](../../platforms/platform-open-source.md) | [Microsoft Presidio](../open-source/presidio.md) | [AI guardrails](../../capabilities/generative-ai/ai-guardrails.md), [Data classification](../../capabilities/governance/data-classification.md), [De-identification](../../capabilities/governance/deidentification.md) |
